#!/usr/bin/env python3
"""Figures drawn ONLY from the real run ledger (data/real/runs.csv).

Each figure states in its caption file (figures/real/CAPTIONS.md) exactly which rows it
uses. Nothing here is simulated.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figstyle as fs  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.dates as mdates  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures/real"
df = pd.read_csv(ROOT / "data/real/runs.csv")
ok = df[df.rc == 0].copy()

captions: list[str] = ["# Captions and provenance for figures/real\n",
                       "All data: `data/real/runs.csv` (rc = 0 rows unless stated). Derived columns are per-call ratios of verbatim totals.\n"]


def level_key(r) -> str | None:
    if r["script"] != "scripts/llm_reunion_agent.py":
        return None
    lvl = str(r["level"])
    ef = str(r["extra_flags"]) if isinstance(r["extra_flags"], str) else ""
    if "--inputs" in ef:
        return "L1v2" if lvl == "L1" else None  # L5 v2 exists for one model only; keep ladder clean
    if "--dims-permute" in ef:
        return "L5-P"
    if "--withhold-title" in ef:
        return "L6"
    if "--holder-scrub" in ef:
        return "L3-H2"
    if "--prompt-variant" in ef or "--replicate" in ef:
        return None  # prompt-variant / replicate runs are controls, not ladder points
    if lvl == "L2-T" and r["calls"] not in (32, 91):
        return None  # 10-23 pilot of L2-T ran on a 5/17-query subset with a different prompt; not comparable
    return lvl


ok["ladder"] = ok.apply(level_key, axis=1)
ag = ok[ok.ladder.notna()].copy()
agd = ag[ag.split == "dev"]


# ---------------------------------------------------------------- Fig R1: prompt-token fingerprint
def fig_r1():
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.DOUBLE_COL, 2.6))
    lv = [l for l in fs.LEVEL_ORDER if l in set(agd.ladder)]
    means = agd.groupby("ladder")["prompt_tok_per_call"].mean().reindex(lv)
    bars = ax.bar(range(len(lv)), means.values, color=[fs.LEVEL_COLORS[l] for l in lv], width=0.62, zorder=2)
    for b in bars:  # label above the per-model markers
        ax.annotate(f"{b.get_height():,.0f}", (b.get_x() + b.get_width() / 2, b.get_height()), xytext=(0, 7),
                    textcoords="offset points", ha="center", va="bottom", fontsize=6.5)
    # overlay per-model points to show the fingerprint is model-independent
    for m in fs.MODEL_ORDER:
        sub = agd[agd.alias == m].groupby("ladder")["prompt_tok_per_call"].mean().reindex(lv)
        ax.scatter(range(len(lv)), sub.values, s=14, color="white", edgecolor=fs.MODEL_COLORS[m], linewidth=1.1,
                   zorder=3, label=fs.MODEL_LABELS[m])
    ax.set_xticks(range(len(lv)))
    ax.set_xticklabels([fs.LEVEL_LABELS[l] for l in lv], fontsize=6.8)
    ax.set_ylabel("prompt tokens per query\n(query + 30-candidate shortlist)")
    ax.set_title("Information-level ladder, fingerprinted by prompt length (dev split)", loc="left")
    ax.legend(ncol=4, loc="upper right", bbox_to_anchor=(1.0, 1.02), handletextpad=0.2, columnspacing=0.8)
    ax.set_ylim(0, means.max() * 1.2)
    fs.save(fig, OUT / "R1_ladder_prompt_tokens")
    captions.append("**R1_ladder_prompt_tokens** — mean prompt tokens per call of `llm_reunion_agent.py` dev runs grouped by ladder level (L1, L1 v2 inputs, L2-T, L3, L3-H, L3-H2 holder-scrub v2, L5, L5-P dims-permute, L6 withhold-title). Circles: per-model means — identical to within ±2 tokens, proving all models saw the same prompts.\n")


# ---------------------------------------------------------------- Fig R2: reasoning tax
def fig_r2():
    fs.apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(fs.DOUBLE_COL, 2.7), gridspec_kw={"width_ratios": [1.6, 1]})
    ax = axes[0]
    lv = ["L1", "L2-T", "L3", "L3-H", "L5"]
    x = np.arange(len(lv)); w = 0.2
    for i, m in enumerate(fs.MODEL_ORDER):
        sub = agd[agd.alias == m].groupby("ladder")["completion_tok_per_call"].mean().reindex(lv)
        bars = ax.bar(x + (i - 1.5) * w, sub.values, w, color=fs.MODEL_COLORS[m], label=fs.MODEL_LABELS[m], zorder=2)
        fs.annotate_bars(ax, bars, fmt="{:.0f}", fontsize=5.6)
    ax.set_xticks(x); ax.set_xticklabels([l for l in lv])
    ax.set_ylabel("completion tokens per query")
    ax.set_title("(a) Completion tokens per query (dev)", loc="left")
    ax.set_ylim(0, 1080)
    ax.legend(ncol=2, loc="upper left", fontsize=6.8)
    ax = axes[1]
    # cost per call L1 dev
    sub = agd[agd.ladder == "L1"].groupby("alias")["cost_per_call_usd"].mean().reindex(fs.MODEL_ORDER)
    bars = ax.bar(range(4), sub.values * 100, color=[fs.MODEL_COLORS[m] for m in fs.MODEL_ORDER], zorder=2)
    fs.annotate_bars(ax, bars, fmt="{:.2f}¢")
    ax.set_xticks(range(4)); ax.set_xticklabels(["4.1 mini", "4.1", "5.4 mini\n(thinking)", "5.4"], fontsize=7)
    ax.set_ylabel("relay cost per query (US cents), L1")
    ax.set_title("(b) Cost per query at L1", loc="left")
    ax.set_ylim(0, sub.max() * 100 * 1.2)
    fs.save(fig, OUT / "R2_reasoning_tax")
    captions.append("**R2_reasoning_tax** — (a) mean completion tokens per call by model and level (dev agent runs). GPT-5.4 mini (reasoning_effort=low, hidden reasoning billed as completion) emits 475–766 tokens/query vs 41–91 for the non-thinking models. (b) Resulting relay cost per query at L1: the 'mini' thinking model (1.62¢) is within 20 % of GPT-4.1 (2.00¢) and GPT-5.4 (1.96¢) and 3.9× GPT-4.1 mini (0.42¢).\n")


# ---------------------------------------------------------------- Fig R3: cost of each road
def fig_r3():
    fs.apply_style()
    rows = []
    def add(name, sel, per="calls", note=""):
        s = ok[sel]
        for _, r in s.iterrows():
            q = r["calls"] if per == "calls" else (int(r["limit"]) if str(r["limit"]).isdigit() and int(r["limit"]) > 0 else r["calls"])
            if not q:
                continue
            rows.append({"road": name, "alias": r["alias"], "usd_per_query": r["cost_usd"] / q, "sec_per_query": r["seconds"] / q, "note": note})
    add("E5 closed-book\n(memory only)", (ok.script == "scripts/llm_eval_harness.py") & (ok.task == "t0_closedbook"))
    add("E6 single-shot\nlistwise rerank L1", (ok.script == "scripts/llm_eval_harness.py") & (ok.task == "t1_rerank") & (ok.level == "L1"))
    add("E10 reunion agent L1\n(listwise, K=30)", (ok.script == "scripts/llm_reunion_agent.py") & (ok.ladder == "L1") & (ok.split == "dev"))
    add("E10 reunion agent L5", (ok.script == "scripts/llm_reunion_agent.py") & (ok.ladder == "L5") & (ok.split == "dev"))
    add("E10e pointwise\nrerank L1", ok.script == "scripts/llm_pointwise_rerank.py")
    add("E16 visual reunion\n(MLLM, top-8 images)", (ok.script == "scripts/e16_visual_reunion.py"), per="calls")
    # E15 / E17: queries = --limit
    add("E15 deep-research\nclosed pool (≤30 steps)", (ok.script == "scripts/deep_research_harness.py") & (ok.pool != "open") & (ok.level == "L1"), per="limit")
    add("E17 deep-research\nOPEN pool (≤14 steps)", (ok.script == "scripts/deep_research_harness.py") & (ok.pool == "open"), per="limit")
    d = pd.DataFrame(rows)
    # E16 has 2 calls per query (160 calls / 80 queries): convert to per query
    d.loc[d.road.str.startswith("E16"), ["usd_per_query", "sec_per_query"]] *= 2
    order = list(dict.fromkeys(d.road))
    fig, ax = plt.subplots(figsize=(fs.DOUBLE_COL, 3.0))
    for i, road in enumerate(order):
        sub = d[d.road == road]
        for _, r in sub.iterrows():
            ax.scatter(r["usd_per_query"], i, s=38, color=fs.MODEL_COLORS[r["alias"]], edgecolor="black", linewidth=0.4, zorder=3)
        ax.hlines(i, sub.usd_per_query.min(), sub.usd_per_query.max(), color="grey", linewidth=1, zorder=2)
    ax.set_yticks(range(len(order))); ax.set_yticklabels(order, fontsize=7)
    ax.invert_yaxis()
    ax.set_xscale("log")
    ax.set_xlabel("relay cost per query (USD, log scale)")
    ax.grid(axis="x", linestyle=":", alpha=0.7); ax.grid(axis="y", visible=False)
    for m in fs.MODEL_ORDER:
        ax.scatter([], [], color=fs.MODEL_COLORS[m], edgecolor="black", linewidth=0.4, s=38, label=fs.MODEL_LABELS[m])
    ax.legend(loc="upper right", ncol=2, bbox_to_anchor=(1.0, 1.0))
    ax.set_title("What each road costs per query (real relay charges, dev split)", loc="left")
    # annotate ratios relative to the agent L1 on GPT-4.1 mini
    base = d[(d.road.str.startswith("E10 reunion agent L1")) & (d.alias == "xj-gpt-4.1-mini")].usd_per_query.iloc[0]
    for i, road in enumerate(order):
        mx = d[d.road == road].usd_per_query.max()
        ax.annotate(f"×{mx/base:.0f}" if mx / base >= 2 else f"×{mx/base:.1f}", (mx, i), xytext=(6, -3), textcoords="offset points", fontsize=6.5, color="dimgrey")
    fs.save(fig, OUT / "R3_cost_per_query_roads")
    captions.append(f"**R3_cost_per_query_roads** — relay USD per query for each experimental 'road', one dot per model run (dev split). Per-query = cost_usd / calls, except E15/E17 (cost_usd / --limit queries) and E16 (2 calls per query). Grey annotations: ratio of the most expensive dot on each row to the GPT-4.1 mini agent at L1 (${base:.4f}/query). The open-pool deep-research road (GPT-5.4, $0.22/query) is ~{0.22/base:.0f}× the cheapest shortlist agent and ~11× the same model's shortlist agent at L1 ($0.0196).\n")


# ---------------------------------------------------------------- Fig R4: where the $100 went
def fig_r4():
    fs.apply_style()
    fam = {
        "scripts/llm_reunion_agent.py": "E10 reunion agent (all levels)",
        "scripts/e16_visual_reunion.py": "E16 visual reunion",
        "scripts/deep_research_harness.py": "E15/E17 deep research",
        "scripts/llm_cf_forced_choice.py": "E8 counterfactual forced choice",
        "scripts/llm_eval_harness.py": "E5/E6 closed-book & rerank",
        "scripts/mllm_pair_verify.py": "E7 MLLM pair verify",
        "scripts/llm_pointwise_rerank.py": "E10e pointwise rerank",
        "scripts/e10_visual_gate.py": "E10c visual gate",
        "scripts/llm_t5_profile.py": "E9 T5 profile",
    }
    d = df.copy(); d["family"] = d.script.map(fam)
    g = d.groupby("family").agg(cost=("cost_usd", "sum"), calls=("calls", "sum"), hours=("seconds", lambda s: s.sum() / 3600)).sort_values("cost", ascending=True)
    fig, axes = plt.subplots(1, 3, figsize=(fs.DOUBLE_COL, 2.6), sharey=True)
    for ax, col, lab, fmt in zip(axes, ["cost", "calls", "hours"], ["relay cost (USD)", "API calls", "wall time (h)"], ["${:.1f}", "{:,.0f}", "{:.1f} h"]):
        bars = ax.barh(g.index, g[col], color=fs.OKABE_ITO["blue"], zorder=2)
        for b in bars:
            ax.annotate(fmt.format(b.get_width()), (b.get_width(), b.get_y() + b.get_height() / 2), xytext=(3, 0), textcoords="offset points", va="center", fontsize=6.5)
        ax.set_xlabel(lab); ax.grid(axis="x", linestyle=":", alpha=0.7); ax.grid(axis="y", visible=False)
        ax.set_xlim(0, g[col].max() * 1.3)
    axes[0].tick_params(axis="y", labelsize=7)
    fig.suptitle(f"Where the ${df.cost_usd.sum():.0f} / {int(df.calls.sum()):,} calls / {df.seconds.sum()/3600:.1f} h of the four OpenAI-family ledgers went", x=0.02, ha="left", fontsize=9)
    fs.save(fig, OUT / "R4_budget_breakdown")
    captions.append("**R4_budget_breakdown** — totals by experiment family over all 65 runs (including the 3 failed ones). The listwise agent is 54 % of calls but 74 % of spend.\n")


# ---------------------------------------------------------------- Fig R5: latency
def fig_r5():
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.SINGLE_COL * 1.6, 2.5))
    lv = ["L1", "L2-T", "L3", "L3-H", "L5"]
    for m in fs.MODEL_ORDER:
        sub = ag[(ag.alias == m)].groupby("ladder")["sec_per_call"].agg(["mean", "min", "max"]).reindex(lv)
        ax.errorbar(range(len(lv)), sub["mean"], yerr=[sub["mean"] - sub["min"], sub["max"] - sub["mean"]], fmt="o-", color=fs.MODEL_COLORS[m], label=fs.MODEL_LABELS[m], capsize=2, linewidth=1.1)
    ax.set_xticks(range(len(lv))); ax.set_xticklabels(lv)
    ax.set_ylabel("seconds per query (sequential)")
    ax.set_title("Latency per query, dev+test agent runs (min–max bars)", loc="left")
    ax.legend(fontsize=6.5)
    fs.save(fig, OUT / "R5_latency")
    captions.append("**R5_latency** — mean (dot) and min–max (bars) of seconds per call across dev and test agent runs per level. Interactive use would need <5 s; GPT-5.4 mini's test runs at L3-H/L5 took 14–15 s per query.\n")


# ---------------------------------------------------------------- Fig R6: campaign timeline
def fig_r6():
    fs.apply_style()
    d = df.copy()
    d["start"] = pd.to_datetime(d.run_dir.str.slice(0, 15), format="%Y%m%d_%H%M%S", errors="coerce")
    d = d[d.start.notna()].copy()
    d["end"] = d.start + pd.to_timedelta(d.seconds.fillna(0), unit="s")
    d = d.sort_values("start")
    fig, ax = plt.subplots(figsize=(fs.DOUBLE_COL, 2.9))
    ypos = {m: i for i, m in enumerate(fs.MODEL_ORDER)}
    for _, r in d.iterrows():
        y = ypos[r["alias"]]
        col = fs.MODEL_COLORS[r["alias"]]
        ax.barh(y, (r["end"] - r["start"]).total_seconds() / 3600, left=mdates.date2num(r["start"]), height=0.6, color=col if r["rc"] == 0 else "none", edgecolor="red" if r["rc"] != 0 else col, linewidth=0.8, zorder=2)
        # width in days for date axis
    # fix: barh width must be in days for date axes → redraw properly
    ax.cla()
    for _, r in d.iterrows():
        y = ypos[r["alias"]]
        col = fs.MODEL_COLORS[r["alias"]]
        left = mdates.date2num(r["start"]); width = (r["end"] - r["start"]).total_seconds() / 86400
        ax.barh(y, max(width, 0.004), left=left, height=0.6, color=col if r["rc"] == 0 else "white", edgecolor="red" if r["rc"] != 0 else col, linewidth=0.9, zorder=2)
    ax.set_yticks(range(4)); ax.set_yticklabels([fs.MODEL_LABELS[m] for m in fs.MODEL_ORDER], fontsize=7)
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.HourLocator(byhour=[0, 12]))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d\n%H:%M"))
    ax.xaxis.set_minor_locator(mdates.HourLocator(byhour=range(0, 24, 3)))
    ax.tick_params(axis="x", labelsize=6.5)
    ax.grid(axis="x", linestyle=":", alpha=0.7); ax.grid(axis="y", visible=False)
    ax.set_title("Campaign timeline (CST), one bar per run; red outline = rc≠0", loc="left")
    fs.save(fig, OUT / "R6_campaign_timeline")
    captions.append("**R6_campaign_timeline** — each bar is one run (start from `run_dir` timestamp, length = `seconds`). Three failed runs (red outline): E16 visual L3 on GPT-4.1 (10-24 04:28), E8v4 no-evidence on GPT-4.1 (10-24 04:29, 0 calls), and the L5-P test on GPT-5.4 (10-24 23:48, 4 API errors).\n")


# ---------------------------------------------------------------- Fig R7: cost scaling dev→test
def fig_r7():
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.SINGLE_COL * 1.6, 2.5))
    sub = ag[ag.ladder.isin(["L1", "L3-H", "L5", "L2-T"])]
    piv = sub.groupby(["alias", "ladder", "split"])["cost_usd"].sum().unstack("split")
    for m in fs.MODEL_ORDER:
        if m not in piv.index.get_level_values(0):
            continue
        p = piv.loc[m].dropna()
        ax.scatter(p["dev"], p["test"], color=fs.MODEL_COLORS[m], s=30, edgecolor="black", linewidth=0.4, label=fs.MODEL_LABELS[m], zorder=3)
        for lvl, r in p.iterrows():
            ax.annotate(lvl, (r["dev"], r["test"]), xytext=(3, 2), textcoords="offset points", fontsize=6)
    lim = max(piv.max().max(), 7)
    ax.plot([0, lim / 3.675], [0, lim], color="grey", linestyle="--", linewidth=0.8, label="×3.675 (294/80 queries, full ladder)")
    ax.plot([0, lim / 2.84], [0, lim], color="grey", linestyle=":", linewidth=0.8, label="×2.84 (91/32 queries, L2-T subset)")
    ax.set_xlabel("dev run cost (USD)"); ax.set_ylabel("test run cost (USD)")
    ax.set_title("Test cost is predictable from dev cost", loc="left")
    ax.legend(fontsize=6.3)
    fs.save(fig, OUT / "R7_dev_to_test_cost")
    captions.append("**R7_dev_to_test_cost** — for levels run on both splits, total cost of the dev run vs the test run. Full-ladder points lie on the 294/80 line and L2-T points on the 91/32 line, so a dev run predicts a full test run's cost to within a few percent — a useful planning fact for budgeting the remaining models.\n")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for f in (fig_r1, fig_r2, fig_r3, fig_r4, fig_r5, fig_r6, fig_r7):
        f()
        print("ok", f.__name__)
    (OUT / "CAPTIONS.md").write_text("\n".join(captions), encoding="utf-8")
    print("wrote", OUT / "CAPTIONS.md")
