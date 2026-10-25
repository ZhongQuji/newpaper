"""Shared publication style for every figure in this repository.

Design rules (applied everywhere so the paper looks like one hand drew it):
- Okabe–Ito colour-blind-safe palette; one fixed colour per model family / per level.
- Single-column width 3.4 in, double-column 7.0 in; 8.5 pt base font (NeurIPS/ICLR body is 10 pt).
- No top/right spines, light dotted y-grid, direct labelling where possible.
- Every figure is exported as vector PDF (for the paper) and 300-dpi PNG (for review).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OKABE_ITO = {
    "orange": "#E69F00",
    "sky": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermilion": "#D55E00",
    "purple": "#CC79A7",
    "black": "#000000",
    "grey": "#7F7F7F",
}

MODEL_COLORS = {
    "xj-gpt-4.1-mini": OKABE_ITO["sky"],
    "xj-gpt-4.1": OKABE_ITO["blue"],
    "xj-gpt-5.4-mini": OKABE_ITO["orange"],
    "xj-gpt-5.4": OKABE_ITO["vermilion"],
}
MODEL_LABELS = {
    "xj-gpt-4.1-mini": "GPT-4.1 mini",
    "xj-gpt-4.1": "GPT-4.1",
    "xj-gpt-5.4-mini": "GPT-5.4 mini (thinking)",
    "xj-gpt-5.4": "GPT-5.4",
}
MODEL_ORDER = ["xj-gpt-4.1-mini", "xj-gpt-4.1", "xj-gpt-5.4-mini", "xj-gpt-5.4"]

LEVEL_ORDER = ["L1", "L1v2", "L2-T", "L3", "L3-H", "L3-H2", "L5", "L5-P", "L6"]
LEVEL_LABELS = {
    "L1": "L1\nfull record",
    "L1v2": "L1 v2\nenriched",
    "L2-T": "L2-T\ntitle withheld\n(leak subset)",
    "L3": "L3\nreduced",
    "L3-H": "L3-H\nholder\nscrubbed",
    "L3-H2": "L3-H2\nholder\nscrub v2",
    "L5": "L5\nphysical\nfacts",
    "L5-P": "L5-P\ndims\npermuted",
    "L6": "L6\nL5 − title",
}
# a sequential ramp for the ladder (dark = more information)
LEVEL_COLORS = {
    "L1": "#08306B", "L1v2": "#2171B5", "L2-T": "#4292C6", "L3": "#6BAED6", "L3-H": "#9ECAE1",
    "L3-H2": "#C6DBEF", "L5": "#FDAE6B", "L5-P": "#FD8D3C", "L6": "#E6550D",
}

SINGLE_COL = 3.4
DOUBLE_COL = 7.0


def apply_style() -> None:
    plt.rcParams.update({
        "font.size": 8.5,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
        "axes.titlesize": 9,
        "axes.labelsize": 8.5,
        "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5,
        "legend.fontsize": 7.5,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.linestyle": ":",
        "grid.linewidth": 0.6,
        "grid.alpha": 0.7,
        "axes.axisbelow": True,
        "lines.linewidth": 1.4,
        "lines.markersize": 4,
        "pdf.fonttype": 42,  # embed TrueType so text stays editable in Illustrator
        "ps.fonttype": 42,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "figure.dpi": 110,
    })


def save(fig, path_without_ext: str | Path, png: bool = True) -> list[Path]:
    """Save as PDF (+ PNG). Returns written paths."""
    p = Path(path_without_ext)
    p.parent.mkdir(parents=True, exist_ok=True)
    out = []
    fig.savefig(p.with_suffix(".pdf"))
    out.append(p.with_suffix(".pdf"))
    if png:
        fig.savefig(p.with_suffix(".png"), dpi=300)
        out.append(p.with_suffix(".png"))
    plt.close(fig)
    return out


def annotate_bars(ax, bars, fmt="{:.0f}", fontsize=6.5, dy=0.0, color="black", rotation=0):
    for b in bars:
        h = b.get_height()
        if h is None or h != h:
            continue
        ax.annotate(fmt.format(h), (b.get_x() + b.get_width() / 2, h + dy),
                    ha="center", va="bottom", fontsize=fontsize, color=color, rotation=rotation,
                    xytext=(0, 1.5), textcoords="offset points")
