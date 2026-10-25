#!/usr/bin/env python3
"""Statistical power of the information-level ladder with the real split sizes.

Question: with n = 80 (dev) or n = 294 (test) queries, how large must the true accuracy
drop between two levels (e.g. L1 → L5) be before the paper can claim it?

Model (all synthetic, parameters swept):
  - each query q has a latent difficulty z_q ~ N(0,1); queries come in ensembles of size 1–4
    and share an ensemble effect u_c ~ N(0,1) with intra-cluster correlation `icc`
  - P(correct at level A) = Φ(a + λ·(√icc·u_c + √(1-icc)·z_q)); level B has a shifted a
    such that the marginal accuracy differs by Δ
  - outcomes are binary (exact-set correct) → paired McNemar test; and a cluster bootstrap of
    the paired mean difference (resampling ensembles, not queries) → 95 % CI excludes 0?
Outputs: sim/results/power_curves.csv, figures/sim/S7_power_curves.pdf|png, sim/results/POWER.md
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm, chi2

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import figstyle as fs  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

RES = ROOT / "sim/results"; FIG = ROOT / "figures/sim"


def simulate_pair(n, base_acc, delta, icc, lam, rng, rho_pair=0.5, cluster_sizes=(1, 2, 3, 4), cluster_probs=(0.45, 0.3, 0.15, 0.1)):
    # build clusters until n queries
    sizes = []
    while sum(sizes) < n:
        sizes.append(int(rng.choice(cluster_sizes, p=cluster_probs)))
    cl = np.repeat(np.arange(len(sizes)), sizes)[:n]
    u = rng.normal(0, 1, len(sizes))[cl]
    z = rng.normal(0, 1, n)
    latent = np.sqrt(icc) * u + np.sqrt(1 - icc) * z
    # choose intercepts so that marginal accuracy matches base_acc and base_acc - delta
    # marginal: E[Φ(a + λ·latent)] = Φ(a / sqrt(1 + λ²))
    s = np.sqrt(1 + lam ** 2)
    a1 = norm.ppf(base_acc) * s; a2 = norm.ppf(max(base_acc - delta, 1e-3)) * s
    p1 = norm.cdf(a1 + lam * latent); p2 = norm.cdf(a2 + lam * latent)
    # Gaussian-copula paired draws: the same query's two outcomes are correlated (rho_pair) but a
    # query can still be right at the poorer level and wrong at the richer one (LLM sampling noise)
    g1 = rng.normal(0, 1, n); g2 = rho_pair * g1 + np.sqrt(1 - rho_pair ** 2) * rng.normal(0, 1, n)
    y1 = norm.cdf(g1) < p1; y2 = norm.cdf(g2) < p2
    return y1, y2, cl


def mcnemar_p(y1, y2):
    b = np.sum(y1 & ~y2); c = np.sum(~y1 & y2)
    if b + c == 0:
        return 1.0
    stat = (abs(b - c) - 1) ** 2 / (b + c)  # continuity-corrected
    return 1 - chi2.cdf(stat, 1)


def cluster_boot_excludes_zero(y1, y2, cl, rng, B=400):
    d = y1.astype(float) - y2.astype(float)
    clusters = np.unique(cl)
    idx_by_c = [np.where(cl == c)[0] for c in clusters]
    means = np.empty(B)
    for b in range(B):
        pick = rng.integers(0, len(clusters), len(clusters))
        sel = np.concatenate([idx_by_c[i] for i in pick])
        means[b] = d[sel].mean()
    lo, hi = np.percentile(means, [2.5, 97.5])
    return lo > 0 or hi < 0


def main():
    t0 = time.time()
    rng = np.random.default_rng(2026)
    deltas = np.array([0.0, 0.03, 0.05, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25, 0.30])
    rows = []
    reps = 1500
    abs_ci = []
    for n in (80, 294):
        for icc in (0.0, 0.3):
            for rho_pair in (0.3, 0.7):
                for delta in deltas:
                    rej_mc = 0; rej_cb = 0
                    for _ in range(reps):
                        y1, y2, cl = simulate_pair(n, 0.6, delta, icc, lam=1.0, rng=rng, rho_pair=rho_pair)
                        rej_mc += mcnemar_p(y1, y2) < 0.05
                        if _ < 300:  # bootstrap is slower; 300 reps is enough for a curve
                            rej_cb += cluster_boot_excludes_zero(y1, y2, cl, rng)
                    rows.append({"n": n, "icc": icc, "rho_pair": rho_pair, "base_acc": 0.6, "delta": delta, "power_mcnemar": rej_mc / reps, "power_cluster_boot": rej_cb / 300})
            # half-width of the 95 % CI of a single level's absolute accuracy (cluster bootstrap)
            hw = []
            for _ in range(300):
                y1, _, cl = simulate_pair(n, 0.6, 0.0, icc, lam=1.0, rng=rng)
                clusters = np.unique(cl); idx = [np.where(cl == c)[0] for c in clusters]
                means = np.array([y1[np.concatenate([idx[i] for i in rng.integers(0, len(clusters), len(clusters))])].mean() for _ in range(300)])
                lo, hi = np.percentile(means, [2.5, 97.5]); hw.append((hi - lo) / 2)
            abs_ci.append({"n": n, "icc": icc, "ci_halfwidth_abs_acc": float(np.mean(hw))})
    df = pd.DataFrame(rows)
    df.to_csv(RES / "power_curves.csv", index=False)
    abs_ci = pd.DataFrame(abs_ci)

    # minimum detectable delta at 80 % power (linear interpolation)
    def mdd(sub, col):
        s = sub.sort_values("delta")
        x = s.delta.values; y = s[col].values
        for i in range(1, len(x)):
            if y[i] >= 0.8:
                return x[i - 1] + (0.8 - y[i - 1]) * (x[i] - x[i - 1]) / max(y[i] - y[i - 1], 1e-9)
        return float("nan")

    lines = ["# Power of the ladder comparison (synthetic; paired exact-set outcomes)", "",
             "| n | ICC (ensemble clustering) | ρ_pair (same-query correlation across levels) | MDD @80 % power, McNemar | MDD @80 % power, cluster bootstrap |", "| ---: | ---: | ---: | ---: | ---: |"]
    for (n, icc, rp), sub in df.groupby(["n", "icc", "rho_pair"]):
        lines.append(f"| {n} | {icc} | {rp} | {mdd(sub, 'power_mcnemar'):.3f} | {mdd(sub, 'power_cluster_boot'):.3f} |")
    lines += ["", "95 % CI half-width of one level's absolute accuracy (base 0.60, cluster bootstrap over ensembles):", "",
              "| n | ICC | ± |", "| ---: | ---: | ---: |"]
    for _, r in abs_ci.iterrows():
        lines.append(f"| {int(r.n)} | {r.icc} | {r.ci_halfwidth_abs_acc:.3f} |")
    m80 = df[(df.n == 80)].groupby(["icc", "rho_pair"]).apply(lambda s: mdd(s, 'power_mcnemar')).agg(['min', 'max'])
    m294 = df[(df.n == 294)].groupby(["icc", "rho_pair"]).apply(lambda s: mdd(s, 'power_mcnemar')).agg(['min', 'max'])
    lines += ["", f"- reps per cell: {reps} (McNemar), 300 (bootstrap, B=400); base accuracy 0.60; λ=1.0", f"- elapsed {time.time()-t0:.0f} s", "",
              f"Reading (computed from the table above): on the 80-query dev split a true drop must be about {m80['min']:.2f}–{m80['max']:.2f} (i.e. {m80['min']*100:.0f}–{m80['max']*100:.0f} accuracy points) before a paired McNemar test detects it with 80 % power; on the 294-query test split about {m294['min']:.2f}–{m294['max']:.2f}. "
              "Pairing cancels the shared ensemble effect, so ICC barely changes the power of a *difference*; it does widen the CI of each level's *absolute* accuracy (second table), so leaderboard numbers must be bootstrapped over ensembles, not queries. Lower same-query correlation (ρ_pair) — i.e. noisier LLM sampling — costs power: report replicate runs."]
    (RES / "POWER.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))

    fs.apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(fs.DOUBLE_COL, 2.6), sharey=True)
    for ax, n in zip(axes, (80, 294)):
        for rp, ls in ((0.7, "-"), (0.3, "--")):
            sub = df[(df.n == n) & (df.icc == 0.3) & (df.rho_pair == rp)]
            ax.plot(sub.delta, sub.power_mcnemar, ls, color=fs.OKABE_ITO["blue"], marker="o", ms=3, label=f"McNemar, ρ_pair={rp}")
            ax.plot(sub.delta, sub.power_cluster_boot, ls, color=fs.OKABE_ITO["vermilion"], marker="s", ms=3, label=f"cluster bootstrap, ρ_pair={rp}")
        ax.axhline(0.8, color="grey", lw=0.8, ls=":")
        ax.set_xlabel("true accuracy drop between two levels (Δ)"); ax.set_title(f"n = {n} queries ({'dev' if n == 80 else 'test'} split), ICC = 0.3", loc="left")
        ax.set_ylim(0, 1.02)
    axes[0].set_ylabel("power (P[reject H0: no drop], α = 0.05)")
    axes[1].legend(fontsize=6.3, loc="lower right")
    fs.save(fig, FIG / "S7_power_curves")


if __name__ == "__main__":
    main()
