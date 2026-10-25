#!/usr/bin/env python3
"""Extract the real experiment ledger from the exported tool-call dump.

Input : data/raw/newpaper_tool_output_export_20261025.md
Output: data/real/runs.csv, data/real/runs.json, data/real/runs_summary.md,
        data/real/campaign_log_tail.txt

Every number written here is copied verbatim from the suite JSON files that the
local campaign runner (`api_campaign_pt`) wrote on the user's machine; nothing is
estimated or simulated. Jobs that appear in several suite files (the runner
re-dumps the suite state) are de-duplicated on `run_dir`; a job without a
`run_dir` (never started / still pending) is kept once per (suite, label).
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/newpaper_tool_output_export_20261025.md"
OUT = ROOT / "data/real"

LINE_NO = re.compile(r"(?m)^\s{0,6}\d+\|")


def load_text() -> str:
    txt = RAW.read_text(encoding="utf-8")
    # the export tool prefixes every 10th line with a right-aligned line number
    return LINE_NO.sub("", txt)


def parse_json_block(body: str):
    """Parse the first JSON object in `body`, tolerating trailing garbage."""
    j = body.find("{")
    if j < 0:
        return None
    s = body[j:]
    k = s.rfind("}")
    while k > 0:
        try:
            return json.loads(s[: k + 1])
        except json.JSONDecodeError:
            k = s.rfind("}", 0, k)
    return None


def flag_value(argv: list[str], flag: str):
    if flag in argv:
        i = argv.index(flag)
        if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
            return argv[i + 1]
        return True
    return None


def main() -> int:
    txt = load_text()
    parts = re.split(r"(?m)^== (.+)$", txt)
    rows: "OrderedDict[str, dict]" = OrderedDict()
    pending = []
    suites = 0
    for i in range(1, len(parts), 2):
        suite = parts[i].strip()
        obj = parse_json_block(parts[i + 1])
        if obj is None or "jobs" not in obj:
            continue
        suites += 1
        for job in obj["jobs"]:
            argv = job.get("argv") or []
            st = job.get("stats") or {}
            audit = st.get("served_model_audit") or {}
            run_dir = job.get("run_dir")
            row = {
                "suite_file": suite,
                "alias": obj.get("alias"),
                "provider_model": obj.get("provider_model"),
                "family": obj.get("family"),
                "suite_started": obj.get("started"),
                "label": job.get("label"),
                "exp": job.get("exp"),
                "script": argv[0] if argv else None,
                "level": flag_value(argv, "--level"),
                "split": flag_value(argv, "--split"),
                "k": flag_value(argv, "--k"),
                "limit": flag_value(argv, "--limit"),
                "task": flag_value(argv, "--task"),
                "n": flag_value(argv, "--n"),
                "max_steps": flag_value(argv, "--max-steps"),
                "pool": flag_value(argv, "--pool"),
                "extra_flags": " ".join(
                    a for a in argv[1:] if a.startswith("--")
                    and a not in {"--backend", "--model", "--split", "--limit", "--k", "--level", "--task", "--n"}
                ),
                "argv": " ".join(argv),
                "rc": job.get("rc"),
                "seconds": job.get("seconds"),
                "calls": st.get("calls"),
                "usage_records": st.get("usage_records"),
                "prompt_tokens": st.get("prompt_tokens"),
                "completion_tokens": st.get("completion_tokens"),
                "cost_usd": st.get("cost_usd"),
                "cache_hits": st.get("cache_hits"),
                "api_errors": st.get("api_errors"),
                "served_requested": audit.get("requested"),
                "served_other": audit.get("served_other"),
                "served_as": json.dumps(audit.get("served_as")) if audit.get("served_as") else None,
                "run_dir": run_dir,
                "output_file": job.get("output"),
                "follow_up": " || ".join(job.get("follow_up") or []),
                "n_reports": len(job.get("reports") or []),
            }
            if run_dir:
                # keep the most complete record (the later re-dumps contain follow_up info)
                prev = rows.get(run_dir)
                if prev is None or (row["follow_up"] and not prev["follow_up"]):
                    rows[run_dir] = row
            else:
                pending.append(row)

    done = list(rows.values())
    # derived per-call metrics (only where the counts exist)
    for r in done + pending:
        c = r.get("calls") or 0
        if c:
            r["prompt_tok_per_call"] = round((r["prompt_tokens"] or 0) / c, 1)
            r["completion_tok_per_call"] = round((r["completion_tokens"] or 0) / c, 1)
            r["cost_per_call_usd"] = round((r["cost_usd"] or 0) / c, 5)
            r["sec_per_call"] = round((r["seconds"] or 0) / c, 2)
            pt = r["prompt_tokens"] or 0
            r["completion_to_prompt_ratio"] = round((r["completion_tokens"] or 0) / pt, 4) if pt else None
        else:
            for kk in ("prompt_tok_per_call", "completion_tok_per_call", "cost_per_call_usd", "sec_per_call", "completion_to_prompt_ratio"):
                r[kk] = None

    OUT.mkdir(parents=True, exist_ok=True)
    fields = list(done[0].keys())
    with (OUT / "runs.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in done:
            w.writerow(r)
    (OUT / "runs.json").write_text(json.dumps({"completed_or_started": done, "pending_or_never_started": pending}, indent=1, ensure_ascii=False), encoding="utf-8")

    # campaign log tail + state (verbatim)
    m = re.search(r"--- pt log tail ---\n(.*?)\n--- pt state ---", txt, re.S)
    if m:
        (OUT / "campaign_log_tail.txt").write_text(m.group(1).strip() + "\n", encoding="utf-8")

    # summary
    ok = [r for r in done if r["rc"] == 0]
    failed = [r for r in done if r["rc"] not in (0, None)]
    tot_cost = sum(r["cost_usd"] or 0 for r in done)
    tot_calls = sum(r["calls"] or 0 for r in done)
    tot_pt = sum(r["prompt_tokens"] or 0 for r in done)
    tot_ct = sum(r["completion_tokens"] or 0 for r in done)
    tot_sec = sum(r["seconds"] or 0 for r in done)
    lines = [
        "# Real experiment ledger (extracted verbatim from the export)",
        "",
        f"- suite JSON dumps parsed: **{suites}**",
        f"- distinct runs (unique `run_dir`): **{len(done)}** — rc=0: {len(ok)}, rc≠0: {len(failed)}",
        f"- pending / never-started job entries: {len(pending)}",
        f"- total API calls: **{tot_calls:,}**; prompt tokens: **{tot_pt:,}**; completion tokens: **{tot_ct:,}**",
        f"- total relay cost: **${tot_cost:,.2f}**; total wall time: **{tot_sec/3600:.1f} h**",
        "",
        "## Per-model totals",
        "",
        "| model | runs | calls | prompt tok | completion tok | cost USD | wall h |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    by_model: dict[str, list] = {}
    for r in done:
        by_model.setdefault(r["alias"], []).append(r)
    for mname, rs in sorted(by_model.items()):
        lines.append(
            f"| {mname} | {len(rs)} | {sum(x['calls'] or 0 for x in rs):,} | {sum(x['prompt_tokens'] or 0 for x in rs):,} | "
            f"{sum(x['completion_tokens'] or 0 for x in rs):,} | {sum(x['cost_usd'] or 0 for x in rs):,.2f} | {sum(x['seconds'] or 0 for x in rs)/3600:.1f} |"
        )
    lines += ["", "## Failed runs (rc≠0)", ""]
    for r in failed:
        lines.append(f"- `{r['run_dir']}` ({r['alias']}, {r['label']}): rc={r['rc']}, calls={r['calls']}, api_errors={r['api_errors']}, {r['seconds']} s")
    lines += ["", "## Served-model audit", ""]
    bad = [r for r in done if (r["served_other"] or 0) > 0]
    lines.append(f"- runs where the relay served a different model than requested: **{len(bad)}**" + ("" if not bad else " → " + ", ".join(r["run_dir"] for r in bad)))
    (OUT / "runs_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
