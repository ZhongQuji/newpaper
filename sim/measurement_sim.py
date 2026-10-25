#!/usr/bin/env python3
"""Measurement-protocol simulations (companion to reunion_sim.py; all synthetic).

S9   Evaluation unit. Per-query micro F1, per-ensemble macro F1, B-cubed F1 and ARI disagree
     when ensembles differ in size; query-level bootstrap CIs are too narrow when queries share an
     ensemble; predictions can contradict transitivity. Quantifies blocker B2.
S10  Forking paths. If the post-hoc rule (`e10_regate`) has k candidate thresholds and the one
     that looks best on the TEST split is reported, how much optimism does that buy at n = 80 / 294?
     Quantifies blocker B6. Also shows that choosing on dev and freezing removes it.
S11  Position bias. A primacy-biased selector on a retriever-ordered shortlist looks better than it
     is; a shuffled-order replicate identifies the bias and its cost. Quantifies the panel's
     'shuffled-order run' request.

Uses tools/eval_toolkit.py for every metric, so this doubles as an integration test of the toolkit.
Outputs: sim/results/MEASUREMENT.md, sim/results/s9_*.csv, s10_*.csv, s11_*.csv, figures/sim/S9–S11.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import figstyle as fs  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from eval_toolkit import (all_metrics, pairwise_prf, exact_set_acc, predicted_clusters, bcubed, ari,  # noqa: E402
                          cluster_bootstrap_fast, position_bias)

RES = ROOT / "sim/results"; FIG = ROOT / "figures/sim"
LOG: list[str] = ["# Measurement-protocol simulations (synthetic)", ""]


# ----------------------------------------------------------------------------- world
def make_world(n_ens: int, rng: np.random.Generator, size_dist=((2, 0.45), (3, 0.25), (4, 0.15), (6, 0.10), (12, 0.05)), K: int = 30, pool: int = 1500):
    """`pool` singleton objects exist only as distractors (a realistic candidate universe); with
    pool=0 every object is a member of some ensemble and is reused as a distractor many times."""
    sizes = rng.choice([s for s, _ in size_dist], size=n_ens, p=[p for _, p in size_dist])
    objs = [(e, f"e{e}_o{i}") for e, s in enumerate(sizes) for i in range(s)]
    ens_of = {o: e for e, o in objs}
    for j in range(pool):
        ens_of[f"pool_{j}"] = n_ens + j
    ids = np.array(list(ens_of)); ens_arr = np.array([ens_of[o] for o in ids])
    return objs, ens_of, ids, ens_arr, sizes


def decide(objs, ens_of, ids, ens_arr, rng, K=30, d_prime=2.0, primacy=0.0, retriever_dprime=1.5, shuffle=False, run_id="A", size_effect=0.0):
    """One run: every object is a query; shortlist = other members present + random distractors.
    size_effect > 0 makes the selector better on large ensembles (and worse on small ones)."""
    rows = []
    sizes_by_ens = pd.Series([e for e, _ in objs]).value_counts()
    centre = float(np.log2(sizes_by_ens.values).mean())   # ensemble-weighted mean of log2(size)
    for e, q in objs:
        members = ids[(ens_arr == e) & (ids != q)]
        dis = rng.choice(ids[ens_arr != e], size=K - len(members), replace=False)
        cands = np.concatenate([members, dis]); gold = np.concatenate([np.ones(len(members), bool), np.zeros(len(dis), bool)])
        r = rng.normal(0, 1, K) + retriever_dprime * gold
        order = rng.permutation(K) if shuffle else np.argsort(-r)
        cands, gold = cands[order], gold[order]
        dq = d_prime + size_effect * (np.log2(len(members) + 1) - centre)
        evid = rng.normal(0, 1, K) + dq * gold
        logit = dq * evid - dq ** 2 / 2 + np.log(0.1 / 0.9) - primacy * np.arange(K) / K
        p = 1 / (1 + np.exp(-logit))
        for j in range(K):
            rows.append((run_id, q, e, cands[j], ens_of[cands[j]], int(p[j] > 0.5), float(p[j]), j))
    d = pd.DataFrame(rows, columns=["run_id", "query_id", "query_ens", "cand_id", "cand_ens", "pred", "score", "pos"])
    for c in ["query_id", "query_ens", "cand_id", "cand_ens"]:
        d[c] = d[c].astype(str)
    return d


def macro_f1_per_ensemble(d: pd.DataFrame) -> float:
    return float(np.mean([pairwise_prf(g)["pair_F1"] for _, g in d.groupby("query_ens")]))


# ----------------------------------------------------------------------------- S9
def s9(seed=0):
    rng = np.random.default_rng(seed)
    rows = []
    for rep in range(12):
        objs, ens_of, ids, ens_arr, sizes = make_world(70, rng)
        # system A: uniform quality; system B: better on big ensembles, worse on small ones; same mean d'
        A = decide(objs, ens_of, ids, ens_arr, rng, d_prime=1.8, run_id="A")
        B = decide(objs, ens_of, ids, ens_arr, rng, d_prime=1.8, size_effect=0.6, run_id="B")
        for name, d in (("A uniform", A), ("B big-ensemble specialist", B)):
            m = all_metrics(d); m["macro_F1_ens"] = macro_f1_per_ensemble(d)
            # CI widths: ensemble bootstrap vs (wrong) query bootstrap
            _, lo_e, hi_e = cluster_bootstrap_fast(d, "pair_F1", B=1500, seed=rep, unit="query_ens")
            _, lo_q, hi_q = cluster_bootstrap_fast(d, "pair_F1", B=1500, seed=rep, unit="query_id")
            m.update({"system": name, "rep": rep, "ci_w_ens": hi_e - lo_e, "ci_w_query": hi_q - lo_q})
            rows.append(m)
    df = pd.DataFrame(rows)
    df.to_csv(RES / "s9_eval_unit.csv", index=False)
    g = df.groupby("system")[["pair_F1", "macro_F1_ens", "b3_F1", "ARI", "exact_set", "contradiction_rate", "ci_w_ens", "ci_w_query"]].mean()
    wins = {}
    for col in ["pair_F1", "macro_F1_ens", "b3_F1", "ARI", "exact_set"]:
        a = df[df.system.str.startswith("A")].set_index("rep")[col]; b = df[df.system.str.startswith("B")].set_index("rep")[col]
        wins[col] = f"{(b > a).mean():.0%} of reps B > A"
    # dense-reuse regime (no distractor pool): closure collapses
    rngd = np.random.default_rng(99)
    objs, ens_of, ids, ens_arr, sizes = make_world(70, rngd, pool=0)
    dd = decide(objs, ens_of, ids, ens_arr, rngd, d_prime=1.8)
    md = all_metrics(dd)
    LOG.extend(["## S9 · evaluation unit (70 ensembles of size 2–12, every member a query, K=30, 1,500-object distractor pool; 12 reps)", "",
                g.round(3).to_markdown(), "",
                "Which system 'wins' depends on the metric: " + "; ".join(f"{k}: {v}" for k, v in wins.items()), "",
                f"- query-level bootstrap CI is {(df.ci_w_query / df.ci_w_ens).mean():.2f}× as wide as the ensemble-level one on average → it understates uncertainty by ~{(1 - (df.ci_w_query / df.ci_w_ens).mean()) * 100:.0f} %.",
                f"- {df[df.system.str.startswith('A')].contradiction_rate.mean():.1%} of explicit negative decisions are overturned by transitive closure of the positives (system A), i.e. the per-query output is not a consistent clustering.",
                f"- Dense-reuse regime (no distractor pool, every object reused as a distractor ~28×): pair F1 {md['pair_F1']:.3f} but B³ F1 {md['b3_F1']:.3f}, ARI {md['ARI']:.3f}, contradiction rate {md['contradiction_rate']:.1%} — naive transitive closure collapses into giant components at a ~2 % pairwise FPR. Stage 4 of the v2 design must use a proper clustering rule (e.g. correlation clustering), not closure.", ""])
    # figure
    fs.apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(fs.DOUBLE_COL, 2.9), gridspec_kw={"width_ratios": [1.5, 0.8, 1]})
    ax = axes[0]
    metrics = ["pair_F1", "macro_F1_ens", "b3_F1", "ARI", "exact_set"]
    x = np.arange(len(metrics)); w = 0.38
    for i, (name, col) in enumerate((("A uniform", fs.OKABE_ITO["blue"]), ("B big-ensemble specialist", fs.OKABE_ITO["orange"]))):
        s = df[df.system == name]
        ax.bar(x + (i - 0.5) * w, s[metrics].mean(), w, yerr=s[metrics].std(), color=col, label=name, capsize=2, zorder=2)
    ax.set_xticks(x); ax.set_xticklabels(["pair F1\n(micro)", "macro F1\n(per ens.)", "B³ F1", "ARI", "exact\nset"], fontsize=6.3)
    ax.set_ylim(0, 1.25); ax.set_ylabel("metric value")
    ax.set_title("(a) Same two systems, five verdicts", loc="left", fontsize=7.5); ax.legend(fontsize=5.8, loc="upper left", ncol=2)
    ax = axes[1]
    for j, (name, col) in enumerate((("A uniform", fs.OKABE_ITO["blue"]), ("B big-ensemble specialist", fs.OKABE_ITO["orange"]))):
        s = df[df.system == name]
        ax.bar([j - 0.18, j + 0.18], [s.ci_w_ens.mean(), s.ci_w_query.mean()], 0.34, color=[col, "lightgrey"], edgecolor=col, zorder=2)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["A", "B"])
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(facecolor="dimgrey", label="ensemble bootstrap"), Patch(facecolor="lightgrey", edgecolor="dimgrey", label="query bootstrap")], fontsize=5.6, loc="upper left")
    ax.set_ylabel("95 % CI width of pair F1"); ax.set_title("(b) Resampling queries\nunderstates uncertainty", loc="left", fontsize=7.5)
    ax = axes[2]
    # contradiction rate vs d'
    rng2 = np.random.default_rng(1)
    objs, ens_of, ids, ens_arr, sizes = make_world(70, rng2)
    dps = [0.8, 1.2, 1.6, 2.0, 2.6, 3.2]; crs = []
    for dp in dps:
        d = decide(objs, ens_of, ids, ens_arr, rng2, d_prime=dp)
        crs.append(predicted_clusters(d)[2])
    ax.plot(dps, crs, "o-", color=fs.OKABE_ITO["purple"])
    ax.set_xlabel("selector d'"); ax.set_ylabel("share of explicit 'no' overturned\nby transitive closure")
    ax.set_title("(c) Per-query outputs are not\na consistent clustering", loc="left", fontsize=7.5)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FIG / "S9_evaluation_unit")


# ----------------------------------------------------------------------------- S10
def s10(seed=1):
    """Regate = pick the best of k posterior thresholds. Report optimism of F1 when the pick is made on
    the same split that is reported, vs picked on dev and frozen for test."""
    rng = np.random.default_rng(seed)
    rows = []
    for n_q, label in ((80, "dev n=80"), (294, "test n=294")):
        n_ens = int(round(n_q / 3.1))  # ≈3.1 queries per ensemble under the size distribution
        for rep in range(150):
            objs, ens_of, ids, ens_arr, sizes = make_world(n_ens, rng)
            d = decide(objs, ens_of, ids, ens_arr, rng, d_prime=1.6)
            # a second, independent draw of the same world = the "frozen" evaluation set
            d2 = decide(objs, ens_of, ids, ens_arr, rng, d_prime=1.6)
            gold = (d.query_ens == d.cand_ens).values; gold2 = (d2.query_ens == d2.cand_ens).values
            qid = d.query_id.values; qid2 = d2.query_id.values
            for family in ("threshold only", "heterogeneous rules"):
                for k in (1, 3, 5, 10, 20):
                    thr = np.linspace(0.3, 0.7, k) if k > 1 else np.array([0.5])
                    f_same, f_frozen, e_same, e_frozen = [], [], [], []
                    for v, t_ in enumerate(thr):
                        s1, s2 = d.score.values.copy(), d2.score.values.copy()
                        if family == "heterogeneous rules" and k > 1:
                            # each variant is a heuristic that re-scores a different random 20 % of candidates
                            rv = np.random.default_rng(10_000 * rep + v)
                            touch = rv.random(len(s1)) < 0.2
                            s1 = np.where(touch, np.clip(s1 + rv.normal(0, 0.25, len(s1)), 0, 1), s1)
                            s2 = np.where(touch, np.clip(s2 + rv.normal(0, 0.25, len(s2)), 0, 1), s2)
                        pred, pred2 = s1 > t_, s2 > t_
                        f_same.append(_f1(pred, gold)); f_frozen.append(_f1(pred2, gold2))
                        e_same.append(_exact(pred, gold, qid)); e_frozen.append(_exact(pred2, gold2, qid2))
                    bf = int(np.argmax(f_same)); be = int(np.argmax(e_same))
                    rows.append({"split": label, "family": family, "k": k, "rep": rep,
                                 "f1_optimism": f_same[bf] - f_frozen[bf], "f1_honest_gain": f_frozen[bf] - _f1(d.score.values > 0.5, gold),
                                 "exact_optimism": e_same[be] - e_frozen[be]})
    df = pd.DataFrame(rows); df.to_csv(RES / "s10_forking_paths.csv", index=False)
    g = df.groupby(["family", "split", "k"])[["f1_optimism", "exact_optimism", "f1_honest_gain"]].mean().reset_index()
    LOG.extend(["## S10 · forking paths of a post-hoc rule (k variants tried, best reported; 150 reps)", "",
                g.round(3).to_markdown(index=False), "",
                "- 'optimism' = metric reported after picking the best variant on the split being reported − the same variant's metric on a fresh draw of the same queries (what a frozen rule would have scored).",
                "- 'threshold only': variants differ only in the posterior threshold (highly correlated → small optimism). 'heterogeneous rules': each variant re-scores a different 20 % of candidates (what a hand-written regate rule family looks like).",
                "- 'f1_honest_gain' = what tuning buys once the choice is frozen on another split (threshold tuning is genuinely useful; the problem is only where it is chosen).", ""])
    fs.apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(fs.DOUBLE_COL, 2.5), sharey=True)
    for ax, metric, title in zip(axes, ("f1_optimism", "exact_optimism"), ("(a) pair F1", "(b) exact-set accuracy")):
        for label, col in (("dev n=80", fs.OKABE_ITO["vermilion"]), ("test n=294", fs.OKABE_ITO["blue"])):
            for family, mk in (("threshold only", "o-"), ("heterogeneous rules", "s--")):
                s = g[(g.split == label) & (g.family == family)]
                ax.plot(s.k, s[metric] * 100, mk, color=col, label=f"{family}, {label}")
        ax.axhline(0, color="grey", lw=0.8)
        ax.set_xscale("log"); ax.set_xticks([1, 3, 5, 10, 20]); ax.set_xticklabels([1, 3, 5, 10, 20])
        ax.set_xlabel("post-hoc rule variants tried (k)"); ax.set_title(title + ": optimism of reporting the best variant", loc="left", fontsize=7.5)
    axes[0].set_ylabel("optimism (points)"); axes[1].legend(fontsize=5.6)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FIG / "S10_forking_paths")


def _exact(pred, gold, qid):
    return float(pd.Series(pred == gold).groupby(qid).all().mean())


def _f1(pred, gold):
    tp = np.sum(pred & gold); fp = np.sum(pred & ~gold); fn = np.sum(~pred & gold)
    p = tp / (tp + fp) if tp + fp else 0; r = tp / (tp + fn) if tp + fn else 0
    return 2 * p * r / (p + r) if p + r else 0.0


# ----------------------------------------------------------------------------- S11
def s11(seed=2):
    rng = np.random.default_rng(seed)
    rows = []
    for rep in range(15):
        objs, ens_of, ids, ens_arr, sizes = make_world(70, rng)
        for primacy in (0.0, 1.5, 3.0):
            for shuffle in (False, True):
                d = decide(objs, ens_of, ids, ens_arr, rng, d_prime=1.6, primacy=primacy, shuffle=shuffle, run_id=f"p{primacy}_{'shuf' if shuffle else 'ord'}")
                m = pairwise_prf(d)
                pb = position_bias(d, bins=3)
                rows.append({"rep": rep, "primacy": primacy, "order": "shuffled" if shuffle else "retriever", "pair_F1": m["pair_F1"], "pair_R": m["pair_R"],
                             "recall_first_third": pb.recall.iloc[0], "recall_last_third": pb.recall.iloc[-1]})
    df = pd.DataFrame(rows); df.to_csv(RES / "s11_position_bias.csv", index=False)
    g = df.groupby(["primacy", "order"])[["pair_F1", "pair_R", "recall_first_third", "recall_last_third"]].mean().round(3)
    LOG.extend(["## S11 · position bias and the shuffled-order control (15 reps)", "", g.to_markdown(), "",
                "- With a retriever-ordered list a primacy-biased selector loses little in aggregate F1 (gold sits early), so the ordered-list number flatters the selector by up to ~13 F1 points at primacy 3.0; the shuffled replicate reveals the loss that a weaker retriever or a different candidate order would expose.",
                "- The diagnostic recall(first third) − recall(last third) detects the bias under BOTH orderings here (recall is conditional on gold, so where gold sits does not bias it), but on the ordered list it rests on the few gold items that land late and is correspondingly noisier; FPR-by-position IS confounded on an ordered list because retriever score and similarity co-vary. Run one shuffled-order replicate per headline condition and report both numbers.", ""])
    fs.apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(fs.DOUBLE_COL, 2.5))
    ax = axes[0]
    for order, col, mk in (("retriever", fs.OKABE_ITO["blue"], "o-"), ("shuffled", fs.OKABE_ITO["vermilion"], "s--")):
        s = df[df.order == order].groupby("primacy")["pair_F1"]
        ax.errorbar(s.mean().index, s.mean(), yerr=s.std(), fmt=mk, color=col, capsize=2, label=f"{order}-ordered shortlist")
    ax.set_xlabel("selector primacy bias (logit penalty at the last position)"); ax.set_ylabel("pair F1"); ax.legend(fontsize=6.2)
    ax.set_title("(a) Ordered lists hide the cost of position bias", loc="left", fontsize=7.5)
    ax = axes[1]
    for order, col, mk in (("retriever", fs.OKABE_ITO["blue"], "o-"), ("shuffled", fs.OKABE_ITO["vermilion"], "s--")):
        s = df[df.order == order].groupby("primacy")
        gap = (s["recall_first_third"].mean() - s["recall_last_third"].mean())
        ax.plot(gap.index, gap.values, mk, color=col, label=f"{order}-ordered")
    ax.axhline(0, color="grey", lw=0.8)
    ax.set_xlabel("selector primacy bias"); ax.set_ylabel("recall(first third) − recall(last third)")
    ax.set_title("(b) The recall-gap diagnostic detects it in both orders", loc="left", fontsize=7.5); ax.legend(fontsize=6.2)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FIG / "S11_position_bias")


if __name__ == "__main__":
    t0 = time.time()
    RES.mkdir(parents=True, exist_ok=True); FIG.mkdir(parents=True, exist_ok=True)
    s9(); print("S9 ok", f"{time.time()-t0:.0f}s")
    s10(); print("S10 ok", f"{time.time()-t0:.0f}s")
    s11(); print("S11 ok", f"{time.time()-t0:.0f}s")
    LOG.append(f"- elapsed {time.time()-t0:.0f} s")
    (RES / "MEASUREMENT.md").write_text("\n".join(LOG), encoding="utf-8")
    print("\n".join(LOG))
