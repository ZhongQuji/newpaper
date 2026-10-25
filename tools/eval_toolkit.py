#!/usr/bin/env python3
"""Evaluation toolkit for set-valued reunion decisions, built for the statistics the review
panel asked for (docs/03 §2: blockers B1, B2, B6, B6b; docs/04 §4 protocol).

INPUT SCHEMA  (long form: one row per (run, query, candidate) decision)
    run_id        str   identifies one experimental condition (model × level × split × seed)
    query_id      str   object id of the query record
    query_ens     str   gold ensemble id of the query (the clustering unit)
    cand_id       str   object id of the candidate record
    cand_ens      str   gold ensemble id of the candidate
    pred          int   1 = agent says "same ensemble", 0 = not
    score         float optional: agent's P(member) or margin (for risk–coverage / calibration)
    pos           int   optional: 0-based position of the candidate in the shortlist shown
    memorised     int   optional: 1 if the query was solved by the evidence-free forced-choice probe
    stratum       str   optional: any grouping (fame tercile, region, period) for stratified reporting

  Gold label of a pair is derived: gold = (query_ens == cand_ens). A query whose shortlist
  contains no gold candidate is a legitimate "none of these" case and is kept.

WHAT IT COMPUTES
    pairwise P / R / F1 (micro over pairs), exact-set accuracy per query,
    B-cubed P / R / F1 and ARI on the transitive closure of positive decisions over all objects,
    contradiction rate (explicit negatives that the closure joins),
    cluster bootstrap CIs (resampling ENSEMBLES, not queries),
    paired comparison of two runs on the same queries (paired ensemble-bootstrap on any metric;
      McNemar on exact-set), Holm correction,
    un-mixing of observed accuracy into memorised / evidence strata (with probe-error inversion),
    risk–coverage curve and AURC from per-query confidence,
    position-bias diagnostics (FPR and recall by shortlist position).

USAGE
    python3 tools/eval_toolkit.py --selftest
    python3 tools/eval_toolkit.py --input decisions.csv --summary
    python3 tools/eval_toolkit.py --input decisions.csv --compare RUN_A RUN_B
    python3 tools/eval_toolkit.py --input decisions.csv --unmix RUN_A
    python3 tools/eval_toolkit.py --input decisions.csv --position-bias RUN_A
The adapter from the local `reports/*.json` to this schema is the one thing that must be
written on the user's machine (see tools/adapters/README.md).
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Callable, Iterable

import numpy as np
import pandas as pd
from scipy.stats import chi2

REQUIRED = ["run_id", "query_id", "query_ens", "cand_id", "cand_ens", "pred"]


# ----------------------------------------------------------------------------- basic metrics
def _prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return p, r, f


def pairwise_prf(d: pd.DataFrame) -> dict:
    gold = (d["query_ens"].values == d["cand_ens"].values)
    pred = d["pred"].values.astype(bool)
    tp = int(np.sum(pred & gold)); fp = int(np.sum(pred & ~gold)); fn = int(np.sum(~pred & gold))
    p, r, f = _prf(tp, fp, fn)
    return {"pair_P": p, "pair_R": r, "pair_F1": f, "tp": tp, "fp": fp, "fn": fn}


def exact_set_acc(d: pd.DataFrame) -> float:
    gold = (d["query_ens"].values == d["cand_ens"].values).astype(int)
    ok = (d["pred"].values.astype(int) == gold)
    return float(pd.Series(ok).groupby(d["query_id"].values).all().mean())


# ----------------------------------------------------------------------------- cluster metrics
class _DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, a: int) -> int:
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def predicted_clusters(d: pd.DataFrame) -> tuple[dict, dict, float]:
    """Transitive closure of positive decisions over every object id appearing in `d`.
    Returns (pred_cluster_of_obj, gold_cluster_of_obj, contradiction_rate) where
    contradiction_rate = share of explicit NEGATIVE decisions whose two objects the closure joins."""
    objs = pd.unique(np.concatenate([d["query_id"].values, d["cand_id"].values]))
    idx = {o: i for i, o in enumerate(objs)}
    dsu = _DSU(len(objs))
    q = d["query_id"].map(idx).values; c = d["cand_id"].map(idx).values
    pos = d["pred"].values.astype(bool)
    for a, b in zip(q[pos], c[pos]):
        dsu.union(a, b)
    pred_of = {o: dsu.find(idx[o]) for o in objs}
    gold = {}
    for o, e in zip(d["query_id"].values, d["query_ens"].values):
        gold[o] = e
    for o, e in zip(d["cand_id"].values, d["cand_ens"].values):
        gold[o] = e
    neg = ~pos
    n_neg = int(neg.sum())
    contra = int(np.sum([dsu.find(a) == dsu.find(b) for a, b in zip(q[neg], c[neg])])) if n_neg else 0
    return pred_of, gold, (contra / n_neg if n_neg else 0.0)


def bcubed(pred_of: dict, gold_of: dict) -> dict:
    objs = list(pred_of)
    from collections import defaultdict
    pc, gc = defaultdict(set), defaultdict(set)
    for o in objs:
        pc[pred_of[o]].add(o); gc[gold_of[o]].add(o)
    P = R = 0.0
    for o in objs:
        inter = len(pc[pred_of[o]] & gc[gold_of[o]])
        P += inter / len(pc[pred_of[o]]); R += inter / len(gc[gold_of[o]])
    P /= len(objs); R /= len(objs)
    F = 2 * P * R / (P + R) if P + R else 0.0
    return {"b3_P": P, "b3_R": R, "b3_F1": F}


def ari(pred_of: dict, gold_of: dict) -> float:
    """Adjusted Rand index (Hubert–Arabie) from the contingency table."""
    objs = list(pred_of)
    ct = pd.crosstab(pd.Series([pred_of[o] for o in objs]), pd.Series([gold_of[o] for o in objs])).values
    def c2(x):
        x = np.asarray(x, dtype=float); return (x * (x - 1) / 2).sum()
    sum_ij = c2(ct.ravel()); a = c2(ct.sum(1)); b = c2(ct.sum(0)); n = c2([ct.sum()])
    expected = a * b / n if n else 0.0
    max_idx = (a + b) / 2
    return float((sum_ij - expected) / (max_idx - expected)) if max_idx != expected else 1.0


def all_metrics(d: pd.DataFrame) -> dict:
    out = pairwise_prf(d)
    out["exact_set"] = exact_set_acc(d)
    pred_of, gold_of, contra = predicted_clusters(d)
    out.update(bcubed(pred_of, gold_of))
    out["ARI"] = ari(pred_of, gold_of)
    out["contradiction_rate"] = contra
    out["n_queries"] = d["query_id"].nunique(); out["n_ensembles"] = d["query_ens"].nunique()
    return out


# ----------------------------------------------------------------------------- bootstrap
def _group_stats(d: pd.DataFrame, unit: str = "query_ens") -> pd.DataFrame:
    gold = (d["query_ens"].values == d["cand_ens"].values)
    pred = d["pred"].values.astype(bool)
    df = pd.DataFrame({"u": d[unit].values, "q": d["query_id"].values, "tp": pred & gold, "fp": pred & ~gold, "fn": ~pred & gold, "ok": pred == gold})
    qs = df.groupby(["u", "q"])["ok"].all().reset_index()
    g = df.groupby("u")[["tp", "fp", "fn"]].sum()
    g["q_ok"] = qs.groupby("u")["ok"].sum(); g["q_n"] = qs.groupby("u")["ok"].size()
    return g


def cluster_bootstrap_fast(d: pd.DataFrame, key: str = "pair_F1", B: int = 2000, seed: int = 0, unit: str = "query_ens") -> tuple[float, float, float]:
    """Same resampling scheme as `cluster_bootstrap`, for metrics that decompose into per-ensemble
    sufficient statistics (pair_P / pair_R / pair_F1 / exact_set). Vectorised, ~1000× faster."""
    g = _group_stats(d, unit).values.astype(float)  # columns tp fp fn q_ok q_n
    rng = np.random.default_rng(seed)
    n = len(g)
    counts = rng.multinomial(n, np.full(n, 1 / n), size=B)      # B × n resample multiplicities
    s = counts @ g                                               # B × 5
    def f(s):
        tp, fp, fn, qok, qn = (s[..., i] for i in range(5))
        with np.errstate(divide="ignore", invalid="ignore"):
            P = np.where(tp + fp > 0, tp / (tp + fp), 0.0); R = np.where(tp + fn > 0, tp / (tp + fn), 0.0)
            F = np.where(P + R > 0, 2 * P * R / (P + R), 0.0); E = qok / qn
        return {"pair_P": P, "pair_R": R, "pair_F1": F, "exact_set": E}[key]
    vals = f(s); point = float(f(g.sum(0)[None, :])[0])
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return point, float(lo), float(hi)


def paired_bootstrap_fast(dA: pd.DataFrame, dB: pd.DataFrame, key: str = "pair_F1", B: int = 2000, seed: int = 0, unit: str = "query_ens") -> dict:
    gA = _group_stats(dA, unit); gB = _group_stats(dB, unit)
    keys = gA.index.intersection(gB.index)
    a = gA.loc[keys].values.astype(float); b = gB.loc[keys].values.astype(float)
    rng = np.random.default_rng(seed); n = len(keys)
    counts = rng.multinomial(n, np.full(n, 1 / n), size=B)
    def f(s):
        tp, fp, fn, qok, qn = (s[..., i] for i in range(5))
        with np.errstate(divide="ignore", invalid="ignore"):
            P = np.where(tp + fp > 0, tp / (tp + fp), 0.0); R = np.where(tp + fn > 0, tp / (tp + fn), 0.0)
            F = np.where(P + R > 0, 2 * P * R / (P + R), 0.0); E = qok / qn
        return {"pair_P": P, "pair_R": R, "pair_F1": F, "exact_set": E}[key]
    diffs = f(counts @ a) - f(counts @ b)
    point = float(f(a.sum(0)[None, :])[0] - f(b.sum(0)[None, :])[0])
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return {"diff": point, "ci_lo": float(lo), "ci_hi": float(hi), "p_two_sided": float(2 * min((diffs <= 0).mean(), (diffs >= 0).mean())), "n_ensembles": int(n)}


def cluster_bootstrap(d: pd.DataFrame, metric: Callable[[pd.DataFrame], float], B: int = 1000, seed: int = 0, unit: str = "query_ens") -> tuple[float, float, float]:
    """Percentile 95 % CI by resampling clusters (`unit`, default = gold ensemble of the query) with replacement."""
    rng = np.random.default_rng(seed)
    groups = {k: v for k, v in d.groupby(unit)}
    keys = np.array(list(groups))
    point = metric(d)
    vals = np.empty(B)
    for b in range(B):
        pick = rng.integers(0, len(keys), len(keys))
        # suffix ids so that a cluster drawn twice counts twice (otherwise closure merges copies)
        parts = []
        for j, k in enumerate(keys[pick]):
            g = groups[k]
            if (keys[pick] == k).sum() > 1:
                g = g.assign(query_id=g["query_id"] + f"#{j}", cand_id=g["cand_id"] + f"#{j}", query_ens=g["query_ens"] + f"#{j}", cand_ens=g["cand_ens"].where(g["cand_ens"] != k, g["cand_ens"] + f"#{j}"))
            parts.append(g)
        vals[b] = metric(pd.concat(parts, ignore_index=True))
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return point, float(lo), float(hi)


def paired_bootstrap(dA: pd.DataFrame, dB: pd.DataFrame, metric: Callable[[pd.DataFrame], float], B: int = 1000, seed: int = 0, unit: str = "query_ens") -> dict:
    """Paired ensemble-bootstrap of metric(A) − metric(B) on the same resampled ensembles."""
    rng = np.random.default_rng(seed)
    keys = np.array(sorted(set(dA[unit]) & set(dB[unit])))
    gA = {k: v for k, v in dA[dA[unit].isin(keys)].groupby(unit)}
    gB = {k: v for k, v in dB[dB[unit].isin(keys)].groupby(unit)}
    diffs = np.empty(B)
    for b in range(B):
        pick = keys[rng.integers(0, len(keys), len(keys))]
        a = pd.concat([gA[k].assign(query_ens=gA[k]["query_ens"] + f"#{j}", query_id=gA[k]["query_id"] + f"#{j}", cand_id=gA[k]["cand_id"] + f"#{j}", cand_ens=gA[k]["cand_ens"].where(gA[k]["cand_ens"] != k, gA[k]["cand_ens"] + f"#{j}")) for j, k in enumerate(pick)], ignore_index=True)
        bb = pd.concat([gB[k].assign(query_ens=gB[k]["query_ens"] + f"#{j}", query_id=gB[k]["query_id"] + f"#{j}", cand_id=gB[k]["cand_id"] + f"#{j}", cand_ens=gB[k]["cand_ens"].where(gB[k]["cand_ens"] != k, gB[k]["cand_ens"] + f"#{j}")) for j, k in enumerate(pick)], ignore_index=True)
        diffs[b] = metric(a) - metric(bb)
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    point = metric(dA[dA[unit].isin(keys)]) - metric(dB[dB[unit].isin(keys)])
    return {"diff": point, "ci_lo": float(lo), "ci_hi": float(hi), "p_two_sided": float(2 * min((diffs <= 0).mean(), (diffs >= 0).mean())), "n_ensembles": len(keys)}


def mcnemar_exact_set(dA: pd.DataFrame, dB: pd.DataFrame) -> dict:
    """Paired McNemar on per-query exact-set correctness (continuity-corrected chi²)."""
    def per_query(d):
        gold = (d["query_ens"].values == d["cand_ens"].values).astype(int)
        return pd.Series(d["pred"].values.astype(int) == gold).groupby(d["query_id"].values).all()
    a, b = per_query(dA), per_query(dB)
    common = a.index.intersection(b.index)
    a, b = a.loc[common], b.loc[common]
    n01 = int(np.sum(a & ~b)); n10 = int(np.sum(~a & b))
    if n01 + n10 == 0:
        return {"n01": n01, "n10": n10, "p": 1.0}
    stat = (abs(n01 - n10) - 1) ** 2 / (n01 + n10)
    return {"n01": n01, "n10": n10, "p": float(1 - chi2.cdf(stat, 1)), "n_queries": len(common)}


def holm(pvals: Iterable[float], alpha: float = 0.05) -> list[bool]:
    p = np.asarray(list(pvals)); m = len(p); order = np.argsort(p)
    reject = np.zeros(m, dtype=bool)
    for rank, i in enumerate(order):
        if p[i] <= alpha / (m - rank):
            reject[i] = True
        else:
            break
    return reject.tolist()


# ----------------------------------------------------------------------------- un-mixing
def unmix(acc_obs: float, p_mem_hat: float, acc_mem_hat: float, fpr: float = 0.0, fnr: float = 0.0) -> dict:
    """Observed accuracy is a mixture: acc_obs = p·acc_mem + (1−p)·acc_evid.
    If the memorisation probe flags a query as memorised with false-positive rate `fpr`
    (non-memorised flagged) and false-negative rate `fnr` (memorised missed), the flagged share is
    p_hat = p(1−fnr) + (1−p)fpr  →  p = (p_hat − fpr) / (1 − fnr − fpr)."""
    denom = 1 - fnr - fpr
    p = (p_mem_hat - fpr) / denom if denom > 0 else float("nan")
    p = float(np.clip(p, 0, 1))
    acc_evid = (acc_obs - p * acc_mem_hat) / (1 - p) if p < 1 else float("nan")
    return {"p_mem": p, "acc_evid": acc_evid, "acc_mem": acc_mem_hat, "acc_obs": acc_obs}


def stratified_accuracy(d: pd.DataFrame, by: str = "memorised", metric: Callable[[pd.DataFrame], float] = exact_set_acc) -> pd.DataFrame:
    rows = []
    for k, g in d.groupby(by):
        rows.append({by: k, "n_queries": g["query_id"].nunique(), "value": metric(g)})
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- risk–coverage
def risk_coverage(d: pd.DataFrame, confidence: pd.Series, metric: Callable[[pd.DataFrame], float] = lambda x: pairwise_prf(x)["pair_P"], grid: int = 20) -> pd.DataFrame:
    """`confidence` indexed by query_id (higher = more confident). Answers the top-coverage share and
    reports metric on the answered subset. Also returns AURC-style area under (coverage, 1−metric)."""
    conf = confidence.sort_values(ascending=False)
    rows = []
    for cov in np.linspace(1 / grid, 1, grid):
        keep = conf.index[: max(1, int(round(cov * len(conf))))]
        sub = d[d["query_id"].isin(keep)]
        rows.append({"coverage": len(keep) / len(conf), "metric": metric(sub)})
    out = pd.DataFrame(rows)
    out.attrs["AURC"] = float(np.trapezoid(1 - out["metric"], out["coverage"]))
    return out


# ----------------------------------------------------------------------------- position bias
def position_bias(d: pd.DataFrame, bins: int = 6) -> pd.DataFrame:
    """False-positive rate on gold negatives and recall on gold positives by shortlist position bin."""
    if "pos" not in d:
        raise ValueError("position_bias needs a `pos` column")
    gold = (d["query_ens"] == d["cand_ens"])
    pb = pd.cut(d["pos"], bins=bins, labels=False, include_lowest=True)
    rows = []
    for b, g in d.assign(_b=pb, _g=gold).groupby("_b"):
        neg = g[~g["_g"]]; posg = g[g["_g"]]
        rows.append({"pos_bin": int(b), "pos_min": int(g["pos"].min()), "pos_max": int(g["pos"].max()),
                     "FPR": float(neg["pred"].mean()) if len(neg) else np.nan, "recall": float(posg["pred"].mean()) if len(posg) else np.nan,
                     "n_neg": len(neg), "n_pos": len(posg)})
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- synthetic data (self-test)
def synth_decisions(n_ens: int = 60, rng: np.random.Generator | None = None, K: int = 30, d_prime: float = 2.0, run_id: str = "A", primacy: float = 0.0, retriever_ordered: bool = True) -> pd.DataFrame:
    """Ensembles of size 2–6; every member is a query; shortlist = other members present + distractors
    from other ensembles; predictions from a Gaussian evidence model with optional primacy bias."""
    rng = rng or np.random.default_rng(0)
    sizes = rng.integers(2, 7, n_ens)
    objs = [(f"e{e}", f"e{e}_o{i}") for e, s in enumerate(sizes) for i in range(s)]
    ens_of = dict((o, e) for e, o in objs)
    all_ids = np.array([o for _, o in objs])
    rows = []
    for e, q in objs:
        members = [o for ee, o in objs if ee == e and o != q]
        n_dis = K - len(members)
        pool = all_ids[np.array([ens_of[o] != e for o in all_ids])]
        dis = rng.choice(pool, size=n_dis, replace=False)
        cands = np.array(members + list(dis))
        gold = np.array([ens_of[c] == e for c in cands])
        r = rng.normal(0, 1, K) + 1.5 * gold                # retriever score
        order = np.argsort(-r) if retriever_ordered else rng.permutation(K)
        cands, gold = cands[order], gold[order]
        evid = rng.normal(0, 1, K) + d_prime * gold
        logit = d_prime * evid - d_prime ** 2 / 2 + np.log(0.1 / 0.9)
        logit = logit - primacy * np.arange(K) / K            # later positions less likely to be selected
        p = 1 / (1 + np.exp(-logit))
        pred = (p > 0.5).astype(int)
        for j, (c, g) in enumerate(zip(cands, gold)):
            rows.append({"run_id": run_id, "query_id": q, "query_ens": e, "cand_id": c, "cand_ens": ens_of[c], "pred": int(pred[j]), "score": float(p[j]), "pos": j})
    return pd.DataFrame(rows)


def selftest(verbose: bool = True) -> bool:
    ok = True
    rng = np.random.default_rng(42)
    def check(name, cond):
        nonlocal ok
        ok &= bool(cond)
        if verbose:
            print(("PASS " if cond else "FAIL ") + name)
    # 1. perfect predictions → all metrics 1, no contradictions
    d = synth_decisions(40, rng)
    perf = d.assign(pred=(d["query_ens"] == d["cand_ens"]).astype(int))
    m = all_metrics(perf)
    check("perfect predictions give pair_F1=b3_F1=ARI=exact=1 and 0 contradictions",
          abs(m["pair_F1"] - 1) < 1e-9 and abs(m["b3_F1"] - 1) < 1e-9 and abs(m["ARI"] - 1) < 1e-9 and m["exact_set"] == 1 and m["contradiction_rate"] == 0)
    # 2. all-negative predictions → recall 0, B-cubed P = 1 (singletons), ARI ≤ 0
    allneg = d.assign(pred=0); m = all_metrics(allneg)
    check("all-negative gives pair_R=0, b3_P=1, ARI<=0", m["pair_R"] == 0 and abs(m["b3_P"] - 1) < 1e-9 and m["ARI"] <= 1e-9)
    # 3. random predictions → ARI ≈ 0 (|ARI| < 0.05 on average)
    aris = []
    for s in range(10):
        dd = synth_decisions(40, np.random.default_rng(s)); dd["pred"] = np.random.default_rng(100 + s).integers(0, 2, len(dd))
        aris.append(all_metrics(dd)["ARI"])
    check(f"random predictions give ARI≈0 (mean {np.mean(aris):+.3f})", abs(np.mean(aris)) < 0.05)
    # 4. contradiction detection: a→b positive, b→c positive, a→c explicitly negative → rate > 0
    tiny = pd.DataFrame([
        {"run_id": "t", "query_id": "a", "query_ens": "E", "cand_id": "b", "cand_ens": "E", "pred": 1},
        {"run_id": "t", "query_id": "b", "query_ens": "E", "cand_id": "c", "cand_ens": "E", "pred": 1},
        {"run_id": "t", "query_id": "a", "query_ens": "E", "cand_id": "c", "cand_ens": "E", "pred": 0},
    ])
    _, _, cr = predicted_clusters(tiny)
    check("transitivity contradiction detected (rate = 1.0 on the toy triple)", abs(cr - 1.0) < 1e-9)
    # 5. bootstrap coverage: 95 % CI of pair_F1 should contain the large-sample truth ≈ 90–98 % of the time
    big = synth_decisions(3000, np.random.default_rng(7), d_prime=2.0)
    truth = pairwise_prf(big)["pair_F1"]
    hits = 0; reps = 300
    for s in range(reps):
        dd = synth_decisions(60, np.random.default_rng(1000 + s), d_prime=2.0)
        _, lo, hi = cluster_bootstrap_fast(dd, "pair_F1", B=1000, seed=s)
        hits += lo <= truth <= hi
    cov = hits / reps
    check(f"ensemble-bootstrap 95% CI coverage of pair_F1 ≈ 0.95 (got {cov:.3f} over {reps} reps)", 0.90 <= cov <= 0.99)
    dd = synth_decisions(60, np.random.default_rng(77), d_prime=2.0)
    pf, lof, hif = cluster_bootstrap_fast(dd, "pair_F1", B=2000, seed=1)
    pg, log_, hig = cluster_bootstrap(dd, lambda x: pairwise_prf(x)["pair_F1"], B=300, seed=1)
    check(f"fast and general bootstrap agree on pair_F1 CI (fast [{lof:.3f},{hif:.3f}] vs general [{log_:.3f},{hig:.3f}])", abs(pf - pg) < 1e-9 and abs(lof - log_) < 0.03 and abs(hif - hig) < 0.03)
    # 6. McNemar under the null: two runs with same d' → p < 0.05 about 5 % of the time
    rej = 0; reps2 = 200
    for s in range(reps2):
        dA = synth_decisions(40, np.random.default_rng(5000 + s), run_id="A")
        dB = dA.copy(); dB["run_id"] = "B"
        # new independent noise draw with identical d'
        r2 = np.random.default_rng(9000 + s)
        gold = (dB["query_ens"] == dB["cand_ens"]).values
        evid = r2.normal(0, 1, len(dB)) + 2.0 * gold
        dB["pred"] = ((2.0 * evid - 2.0 + np.log(0.1 / 0.9)) > 0).astype(int)
        rej += mcnemar_exact_set(dA, dB)["p"] < 0.05
    check(f"McNemar type-I error ≈ 0.05 under the null (got {rej/reps2:.3f})", 0.01 <= rej / reps2 <= 0.10)
    # 7. un-mixing recovers acc_evid with a perfect probe and corrects for probe error
    u = unmix(acc_obs=0.3 * 0.9 + 0.7 * 0.5, p_mem_hat=0.3, acc_mem_hat=0.9)
    check(f"unmix recovers acc_evid=0.5 with a perfect probe (got {u['acc_evid']:.3f})", abs(u["acc_evid"] - 0.5) < 1e-9)
    p_hat = 0.3 * (1 - 0.1) + 0.7 * 0.05
    u2 = unmix(acc_obs=0.3 * 0.9 + 0.7 * 0.5, p_mem_hat=p_hat, acc_mem_hat=0.9, fpr=0.05, fnr=0.1)
    check(f"unmix inverts probe error (fpr .05, fnr .10) → p_mem=0.300 (got {u2['p_mem']:.3f})", abs(u2["p_mem"] - 0.3) < 1e-9)
    # 8. position bias is detected when injected and absent when not
    dp = synth_decisions(80, np.random.default_rng(11), primacy=3.0, retriever_ordered=False)
    pb = position_bias(dp, bins=3)
    d0 = synth_decisions(80, np.random.default_rng(11), primacy=0.0, retriever_ordered=False)
    pb0 = position_bias(d0, bins=3)
    check(f"primacy bias shows as recall drop first→last bin ({pb.recall.iloc[0]:.2f}→{pb.recall.iloc[-1]:.2f}) and is flat without bias ({pb0.recall.iloc[0]:.2f}→{pb0.recall.iloc[-1]:.2f})",
          pb.recall.iloc[0] - pb.recall.iloc[-1] > 0.15 and abs(pb0.recall.iloc[0] - pb0.recall.iloc[-1]) < 0.12)
    # 9. risk–coverage is monotone-ish: precision at 50 % coverage ≥ precision at 100 %
    dd = synth_decisions(80, np.random.default_rng(3), d_prime=1.2)
    conf = dd.groupby("query_id")["score"].apply(lambda s: float(np.max(np.abs(s - 0.5))))
    rc = risk_coverage(dd, conf, grid=10)
    check(f"risk–coverage: precision@50% ({rc.metric.iloc[4]:.3f}) ≥ precision@100% ({rc.metric.iloc[-1]:.3f})", rc.metric.iloc[4] >= rc.metric.iloc[-1] - 0.02)
    # 10. Holm
    check("Holm rejects the right set", holm([0.001, 0.01, 0.03, 0.5]) == [True, True, False, False] and holm([0.001, 0.02, 0.03, 0.5]) == [True, False, False, False])
    print("SELFTEST", "PASSED" if ok else "FAILED")
    return ok


# ----------------------------------------------------------------------------- CLI
def _load(path: str) -> pd.DataFrame:
    d = pd.read_csv(path) if path.endswith(".csv") else pd.read_json(path, lines=path.endswith(".jsonl"))
    missing = [c for c in REQUIRED if c not in d]
    if missing:
        raise SystemExit(f"missing required columns: {missing}")
    for c in ["run_id", "query_id", "query_ens", "cand_id", "cand_ens"]:
        d[c] = d[c].astype(str)
    return d


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--input")
    ap.add_argument("--summary", action="store_true", help="all metrics with ensemble-bootstrap CIs per run_id")
    ap.add_argument("--compare", nargs=2, metavar=("RUN_A", "RUN_B"))
    ap.add_argument("--unmix", metavar="RUN", help="stratify RUN by the `memorised` column and un-mix")
    ap.add_argument("--position-bias", metavar="RUN")
    ap.add_argument("-B", type=int, default=1000)
    args = ap.parse_args()
    if args.selftest:
        return 0 if selftest() else 1
    if not args.input:
        ap.print_help(); return 2
    d = _load(args.input)
    if args.summary:
        rows = []
        for run, g in d.groupby("run_id"):
            m = all_metrics(g)
            for key in ("pair_F1", "exact_set"):
                _, lo, hi = cluster_bootstrap_fast(g, key, B=args.B)
                m[f"{key}_ci"] = f"[{lo:.3f}, {hi:.3f}]"
            _, lo, hi = cluster_bootstrap(g, (lambda x: bcubed(*predicted_clusters(x)[:2])["b3_F1"]), B=min(args.B, 300))
            m["b3_F1_ci"] = f"[{lo:.3f}, {hi:.3f}]"
            rows.append({"run_id": run, **m})
        pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
        print(pd.DataFrame(rows).round(3).to_string(index=False))
    if args.compare:
        a, b = (d[d.run_id == r] for r in args.compare)
        for key in ("pair_F1", "exact_set"):
            res = paired_bootstrap_fast(a, b, key, B=args.B)
            print(f"{key}: Δ={res['diff']:+.3f}  95% CI [{res['ci_lo']:+.3f}, {res['ci_hi']:+.3f}]  p={res['p_two_sided']:.3f}  (n_ens={res['n_ensembles']})")
        res = paired_bootstrap(a, b, (lambda x: bcubed(*predicted_clusters(x)[:2])["b3_F1"]), B=min(args.B, 300))
        print(f"b3_F1: Δ={res['diff']:+.3f}  95% CI [{res['ci_lo']:+.3f}, {res['ci_hi']:+.3f}]  p={res['p_two_sided']:.3f}  (n_ens={res['n_ensembles']})")
        print("McNemar exact-set:", mcnemar_exact_set(a, b))
    if args.unmix:
        g = d[d.run_id == args.unmix]
        if "memorised" not in g:
            raise SystemExit("--unmix needs a `memorised` column")
        s = stratified_accuracy(g, "memorised")
        print(s.to_string(index=False))
        p_hat = g.groupby("query_id")["memorised"].first().mean()
        acc_mem = s[s.memorised == 1]["value"].iloc[0] if (s.memorised == 1).any() else float("nan")
        print("un-mixed:", unmix(exact_set_acc(g), p_hat, acc_mem))
    if args.position_bias:
        print(position_bias(d[d.run_id == args.position_bias]).round(3).to_string(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
