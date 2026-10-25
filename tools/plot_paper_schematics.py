#!/usr/bin/env python3
"""Vector schematics for the paper (figures/paper/). Pure matplotlib, editable PDF (Type 42 fonts).

P1  pipeline: today's single listwise call vs the proposed frugal, evidence-first v2 system
P2  the nested information-level ladder (v2) with the leakage channel each rung removes,
    annotated with the REAL prompt-token fingerprint of today's rungs where one exists
P3  memory-vs-evidence un-mixing: what a leaderboard reports vs what the probe lets you separate
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figstyle as fs  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures/paper"


def box(ax, x, y, w, h, text, fc="#F2F2F2", ec="#444444", fontsize=7, lw=0.8, style="round,pad=0.02,rounding_size=0.08", color="black", weight="normal"):
    p = FancyBboxPatch((x, y), w, h, boxstyle=style, fc=fc, ec=ec, lw=lw, zorder=2)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize, color=color, zorder=3, weight=weight, linespacing=1.25)
    return p


def arrow(ax, x0, y0, x1, y1, text=None, fontsize=6, color="#333333", lw=0.9, offset=(0, 4), style="-|>"):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=9, lw=lw, color=color, zorder=1)
    ax.add_patch(a)
    if text:
        ax.annotate(text, ((x0 + x1) / 2, (y0 + y1) / 2), xytext=offset, textcoords="offset points", ha="center", fontsize=fontsize, color=color)


def p1_pipeline():
    fs.apply_style()
    fig, axes = plt.subplots(2, 1, figsize=(fs.DOUBLE_COL, 5.0), gridspec_kw={"height_ratios": [1, 2.4]})
    for ax in axes:
        ax.set_xlim(0, 100); ax.axis("off")
    F = 6.3
    # ---- today
    ax = axes[0]; ax.set_ylim(0, 10)
    ax.text(0, 9.4, "(a) Today: one flagship call over a fixed 30-candidate shortlist", fontsize=8.5, weight="bold", va="center")
    box(ax, 0.5, 3, 13, 4, "query record", fc="#FFFFFF", fontsize=F)
    arrow(ax, 13.5, 5, 17.5, 5)
    box(ax, 17.5, 3, 21, 4, "retriever\n30 candidates", fc="#FFFFFF", fontsize=F)
    arrow(ax, 38.5, 5, 44.5, 5, "1,959 tok", offset=(0, 6))
    box(ax, 44.5, 2.4, 26, 5.2, "flagship LLM, one listwise call\n'which ids share the ensemble?'", fc="#FDE0DD", ec=fs.OKABE_ITO["vermilion"], fontsize=F)
    arrow(ax, 70.5, 5, 76.5, 5, "70 tok", offset=(0, 6))
    box(ax, 76.5, 3, 10, 4, "id set", fc="#FFFFFF", fontsize=F)
    arrow(ax, 86.5, 5, 89.5, 5)
    box(ax, 89.5, 3, 10, 4, "regate\n(rule ?)", fc="#EEEEEE", ec="#999999", fontsize=F)
    ax.text(50, 0.5, "$0.020 / query (GPT-4.1)  ·  fixed K  ·  no abstention  ·  no verification  ·  title still shown at L5", ha="center", fontsize=6.3, color="dimgrey")
    # ---- v2
    ax = axes[1]; ax.set_ylim(0, 24)
    ax.text(0, 23.2, "(b) Proposed v2: read less, escalate only what is open, test every claim", fontsize=8.5, weight="bold", va="center")
    box(ax, 0.5, 17, 13, 4, "query record", fc="#FFFFFF", fontsize=F)
    arrow(ax, 13.5, 19, 17.5, 19)
    box(ax, 17.5, 16.4, 21, 5.2, "retriever + calibrated\nscores; keep p ≥ 0.02\n(adaptive K)", fc="#E5F5E0", ec=fs.OKABE_ITO["green"], fontsize=F)
    arrow(ax, 38.5, 19, 44.5, 19, "~16 of 30", offset=(0, 6))
    box(ax, 44.5, 16.1, 29, 5.8, "Stage 1 · cheap screen (mini)\nL5 physical facts only\np̂(member) per candidate", fc="#DEEBF7", ec=fs.OKABE_ITO["blue"], fontsize=F)
    arrow(ax, 59, 16.1, 59, 13.2)
    box(ax, 38, 10.4, 42, 2.8, "p̂ < 0.05 → reject (final)      else → open band (~8 candidates)", fc="#FFFFFF", ec="#777777", fontsize=5.8)
    arrow(ax, 59, 10.4, 59, 7.6)
    box(ax, 36, 2.6, 46, 5.0, "Stage 2 · strong judge (flagship), L1 full record\nimages / open pool only if the VoI gate opens", fc="#FDE0DD", ec=fs.OKABE_ITO["vermilion"], fontsize=F)
    arrow(ax, 82, 5.1, 84.5, 5.1)
    box(ax, 84.5, 1.6, 15, 7.0, "Stage 3 · verify\ncite shown fields;\nchecker flags\nunshown facts;\nabstain if open", fc="#FFF5EB", ec=fs.OKABE_ITO["orange"], fontsize=5.5)
    arrow(ax, 92.5, 8.6, 92.5, 11.6)
    box(ax, 84.5, 11.6, 15, 5.2, "Stage 4 · ensemble\nclosure → clusters\n+ evidence dossier", fc="#F2F2F2", fontsize=5.5)
    # side notes (prices from real token counts × fitted relay rates)
    ax.text(1, 13.0, "≈ $0.0026 / query", fontsize=6.3, color=fs.OKABE_ITO["blue"])
    ax.text(1, 11.9, "mini @ L5, all kept candidates", fontsize=5.7, color="dimgrey")
    ax.text(1, 7.4, "≈ $0.0098 × ~40 % of queries", fontsize=6.3, color=fs.OKABE_ITO["vermilion"])
    ax.text(1, 6.3, "flagship @ L1, open band only", fontsize=5.7, color="dimgrey")
    ax.text(1, 3.6, "≈ $0.001–0.005 / query", fontsize=6.3, color=fs.OKABE_ITO["orange"])
    ax.text(1, 2.5, "verification, per predicted member", fontsize=5.7, color="dimgrey")
    ax.text(50, 0.3, "all-in ≈ $0.0075–0.0115 / query (−40 … −63 % vs today)  ·  share of decisions made from physical facts = a per-decision memorisation metric", ha="center", fontsize=6.2, color="dimgrey")
    fs.save(fig, OUT / "P1_pipeline_today_vs_v2")


def p2_ladder():
    fs.apply_style()
    df = pd.read_csv(ROOT / "data/real/runs.csv")
    ag = df[(df.rc == 0) & (df.script == "scripts/llm_reunion_agent.py") & (df.split == "dev")]
    def tok(level, flag=None, exclude=("--inputs", "--prompt-variant", "--replicate")):
        s = ag[ag.level == level]
        ef = s.extra_flags.fillna("")
        if flag:
            s = s[ef.str.contains(flag, regex=False)]
        else:
            s = s[~ef.str.contains("|".join(x.replace("-", "\\-") for x in exclude + ("--dims-permute", "--withhold-title", "--holder-scrub")))]
        return s.prompt_tok_per_call.mean()
    real = {"L1": tok("L1"), "L3": tok("L3"), "L3-H": tok("L3-H"), "L5": tok("L5"), "L5-P": tok("L5", "--dims-permute"), "L6": tok("L5", "--withhold-title")}

    rungs = [
        ("L1", "full catalogue record", "—", "#08306B", real["L1"], "L1"),
        ("L2", "L1 − title", "the field that names the ensemble", "#2171B5", None, "(today: L2-T = subset + substitution, 2,316 tok)"),
        ("L3", "L2 − holder, accession, credit line, image host", "institutional fingerprints", "#4292C6", real["L3-H"], "today L3-H (title kept)"),
        ("L4", "L3 − creator / workshop / Notname", "memorised attribution", "#6BAED6", None, "(not in today's grid)"),
        ("L5", "physical facts: dimensions, support, medium, technique, date band, iconography", "all words about people and places", "#FDAE6B", real["L6"], "today L6 (= L5 − title)"),
        ("L5-P", "L5 with dimensions permuted across candidates", "the physical channel itself (control)", "#FD8D3C", real["L5-P"], "today L5-P (title kept)"),
        ("L6", "images only (+ dimensions)", "all text — direct pointing", "#E6550D", None, "today E16 / E7 (visual)"),
    ]
    import textwrap
    fig, ax = plt.subplots(figsize=(fs.DOUBLE_COL, 4.2))
    ax.set_xlim(0, 100); ax.set_ylim(0, len(rungs) * 10 + 8); ax.axis("off")
    ax.text(0, len(rungs) * 10 + 6, "The nested information-level ladder (v2): each rung is a strict subset of the one above", fontsize=8.5, weight="bold")
    ax.text(0, len(rungs) * 10 + 2.6, "left: what the model sees · middle: the leakage channel the rung removes · right: today's closest rung and its real prompt length (tokens / query, dev)", fontsize=6.3, color="dimgrey")
    for i, (name, shows, removes, col, t, today) in enumerate(rungs):
        y = (len(rungs) - 1 - i) * 10 + 1
        dark = i < 4
        box(ax, 0, y, 7, 7, name, fc=col, ec=col, color="white" if dark else "black", weight="bold", fontsize=7.5)
        box(ax, 8, y, 42, 7, "\n".join(textwrap.wrap(shows, 44)), fc="#FFFFFF", ec=col, fontsize=6.4)
        ax.annotate("", (53, y + 3.5), (50.5, y + 3.5), arrowprops=dict(arrowstyle="-|>", lw=0.7, color="#777777"))
        ax.text(54, y + 3.5, "removes:\n" + "\n".join(textwrap.wrap(removes, 30)), va="center", fontsize=6.1, color="#333333", linespacing=1.15)
        if t is not None and not np.isnan(t):
            ax.text(100, y + 3.5, f"{today}\n{t:,.0f} tok", va="center", ha="right", fontsize=6, color="dimgrey")
        else:
            ax.text(100, y + 3.5, "\n".join(textwrap.wrap(today, 28)), va="center", ha="right", fontsize=6, color="dimgrey", style="italic")
    fs.save(fig, OUT / "P2_nested_ladder_v2")


def p3_unmixing():
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.SINGLE_COL * 1.9, 2.8))
    levels = ["L1", "L2", "L3", "L4", "L5", "L6"]
    x = np.arange(len(levels))
    evid = np.array([0.80, 0.74, 0.62, 0.50, 0.42, 0.30])    # illustrative shapes only
    memo = np.full(len(levels), 0.92)
    p = 0.3
    obs = p * memo + (1 - p) * evid
    ax.fill_between(x, evid, obs, color=fs.OKABE_ITO["orange"], alpha=0.25, label="contribution of memorised queries")
    ax.plot(x, obs, "o-", color="black", label="observed (what a leaderboard reports)")
    ax.plot(x, evid, "s--", color=fs.OKABE_ITO["blue"], label="evidence-only (non-memorised stratum)")
    ax.plot(x, memo, "^:", color=fs.OKABE_ITO["vermilion"], label="memorised stratum (flat: level-independent)")
    ax.set_xticks(x); ax.set_xticklabels(levels)
    ax.set_ylim(0, 1.0); ax.set_ylabel("accuracy (illustrative)")
    ax.set_title("Un-mixing the ladder:  acc_obs = p·acc_mem + (1−p)·acc_evid", loc="left", fontsize=8)
    ax.legend(fontsize=5.8, loc="lower left")
    ax.annotate("observed drop\n(understated)", (5, obs[-1]), xytext=(-62, 30), textcoords="offset points", fontsize=6, arrowprops=dict(arrowstyle="-|>", lw=0.6))
    ax.annotate("true evidence drop", (5, evid[-1]), xytext=(-70, -22), textcoords="offset points", fontsize=6, arrowprops=dict(arrowstyle="-|>", lw=0.6))
    fs.save(fig, OUT / "P3_unmixing_schematic")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    p1_pipeline(); print("P1 ok")
    p2_ladder(); print("P2 ok")
    p3_unmixing(); print("P3 ok")
    (OUT / "CAPTIONS.md").write_text(
        "# Captions for figures/paper\n\n"
        "**P1_pipeline_today_vs_v2** — (a) today's reference system (one listwise flagship call over a fixed 30-candidate shortlist; prices and token counts from the real ledger). (b) the proposed v2 system of `docs/04_method_redesign.md`: adaptive K from calibrated retriever scores, a cheap austere-level screen that may only reject, a strong judge on the open band at the full level with a value-of-information gate for images / open-pool search, a grounded verification step with abstention, and ensemble closure. Prices are real token counts × fitted relay rates; quality claims are simulated (`sim/`).\n\n"
        "**P2_nested_ladder_v2** — the proposed nested ladder. Right column: the closest rung in today's grid and its real mean prompt length (dev split). Note that today's L5 and L5-P still show the title; only L6 removes it, and L2-T is a subset-with-substitution (longer than L1).\n\n"
        "**P3_unmixing_schematic** — illustrative: the observed ladder is a mixture of a flat memorised stratum and a falling evidence-only stratum; stratifying by the evidence-free forced-choice probe recovers the true evidence drop. Shapes are schematic, not measured.\n",
        encoding="utf-8")
    print("captions ok")
