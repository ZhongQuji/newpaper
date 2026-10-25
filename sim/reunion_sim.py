#!/usr/bin/env python3
"""Calibrated design-space simulation for the shortlist-reunion agent.

WHAT THIS IS
    A synthetic generative model of the decision problem the real agent faces
    (query + K=30 shortlist → which candidates belong to the same ensemble), used to
    compare *budget-allocation policies* under identical token accounting.

WHAT IS REAL (taken from data/real/runs.csv)
    - prompt tokens per query at each information level (L1 1,959 · L3 1,784 · L5 1,208 · L6 1,064)
    - completion tokens per call for non-thinking (≈70) and thinking-class (≈500) models
    - effective relay prices per model (least-squares fit on 55 text-only runs, ≤5 % error):
          GPT-4.1 mini  $1.71 / $8.10 per M (prompt / completion)
          GPT-4.1       $8.88 / $36.2
          GPT-5.4       $7.92 / $47.9
          GPT-5.4 mini  $3.29 / $20.3
    - pointwise cost structure: ≈240 prompt tokens per candidate call (E10e: 7.2k tokens/query)

WHAT IS SYNTHETIC (assumptions, every one of them swept in `--sweep`)
    - how many true members a query has, how well the first-stage retriever ranks them,
    - the discriminability d' of the LLM's evidence signal per level and per model class,
    - the share of 'famous' queries the model simply remembers (p_mem),
    - context-dilution of listwise calls with long lists (beta), sample correlation of
      self-consistency draws (rho), threshold jitter of pointwise calls.

    Accuracy numbers produced here are therefore NOT predictions of the real system.
    The *ordering of policies at equal budget* and the *shape of the trade-off curves*
    are the deliverable, together with which assumptions they are sensitive to.

Run:  python3 sim/reunion_sim.py            (defaults: Q=3000 queries × 8 seeds)
      python3 sim/reunion_sim.py --sweep    (sensitivity grid; slower)
Outputs: sim/results/*.csv, figures/sim/*.pdf|png, sim/results/RUNLOG.md
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass, asdict, replace
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import figstyle as fs  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

RES = ROOT / "sim/results"
FIG = ROOT / "figures/sim"

# ----------------------------------------------------------------------------- calibration
PRICES = {  # USD per token, effective relay prices fitted on the real ledger
    "mini": (1.709e-6, 8.098e-6),          # GPT-4.1 mini
    "flagship": (8.877e-6, 36.195e-6),     # GPT-4.1 (GPT-5.4 is within 10 %)
    "mini-thinking": (3.290e-6, 20.344e-6),  # GPT-5.4 mini
}
OUT_TOKENS = {"mini": 70, "flagship": 70, "mini-thinking": 500}   # completion tokens per listwise call (ledger)
LEVEL_PROMPT = {"L1": 1959, "L3": 1784, "L5": 1208, "L6": 1064}  # prompt tokens per 30-candidate call (ledger)
FIXED_PROMPT = 400                                                 # assumed instruction+query overhead
POINTWISE_PER_CALL = 240                                          # ≈ 7,200 / 30 (ledger E10e)


def per_cand_tokens(level: str) -> float:
    return (LEVEL_PROMPT[level] - FIXED_PROMPT) / 30.0


@dataclass
class World:
    Q: int = 3000
    K: int = 30
    member_probs: tuple = (0.15, 0.35, 0.25, 0.13, 0.08, 0.04)  # P(m = 0..5)
    retriever_dprime: float = 1.5     # separation of member vs non-member retriever scores
    p_mem: float = 0.30               # share of queries the LLM 'remembers' regardless of evidence
    dprime_mem: float = 4.0           # evidence quality when remembered
    dprime_level: tuple = (("L1", 2.4), ("L3", 2.0), ("L5", 1.3), ("L6", 1.0))
    model_quality: tuple = (("mini", 0.75), ("flagship", 1.0), ("mini-thinking", 0.9))
    beta_dilution: float = 0.06       # listwise d' loss per log2(K/8)
    pointwise_threshold_jitter: float = 0.35
    rho_sc: float = 0.5               # correlation of noise between self-consistency samples
    rho_models: float = 0.5           # correlation of evidence noise between two different models (shared item difficulty)
    overconfidence: float = 1.0       # LLM's assumed d' / true d' (1 = calibrated, >1 = over-confident posteriors)
    seed: int = 0

    def dprime(self, level: str, model: str) -> float:
        return dict(self.dprime_level)[level] * dict(self.model_quality)[model]


@dataclass
class Result:
    policy: str
    level: str
    model: str
    f1: float
    precision: float
    recall: float
    exact_set: float
    prompt_tokens: float
    completion_tokens: float
    usd_per_query: float
    calls_per_query: float
    coverage: float = 1.0
    seed: int = 0
    extra: str = ""


# ----------------------------------------------------------------------------- world sampling
def sample_world(w: World, rng: np.random.Generator):
    m = rng.choice(len(w.member_probs), size=w.Q, p=np.array(w.member_probs))
    y = np.zeros((w.Q, w.K), dtype=bool)
    for q in range(w.Q):
        if m[q]:
            y[q, rng.choice(w.K, size=m[q], replace=False)] = True
    r = rng.normal(0, 1, (w.Q, w.K)) + w.retriever_dprime * y
    order = np.argsort(-r, axis=1)                       # shortlist sorted by retriever score
    y = np.take_along_axis(y, order, axis=1)
    r = np.take_along_axis(r, order, axis=1)
    remembered = rng.random(w.Q) < w.p_mem
    w.__dict__["_item_noise"] = rng.normal(0, 1, (w.Q, w.K))   # shared item difficulty (for model correlation)
    return y, r, remembered


def retriever_posterior(w: World, r: np.ndarray) -> np.ndarray:
    """Ideal-observer P(member | retriever score) with the marginal prevalence."""
    pi = float(np.dot(np.arange(len(w.member_probs)), w.member_probs)) / w.K
    llr = w.retriever_dprime * r - w.retriever_dprime ** 2 / 2
    logit = llr + np.log(pi / (1 - pi))
    return 1 / (1 + np.exp(-logit))


def llm_evidence(w: World, y, remembered, level, model, rng, k_eff=None, dilute=True, shared_noise=None, rho=0.0):
    """Observed evidence e = d'·y + noise. Remembered queries use d'_mem.
    `k_eff`: list length actually shown (for dilution). `shared_noise`/`rho`: for self-consistency."""
    d = np.full(w.Q, w.dprime(level, model))
    d[remembered] = w.dprime_mem
    if dilute:
        k_eff = w.K if k_eff is None else k_eff
        d = d * (1 - w.beta_dilution * np.maximum(0.0, np.log2(np.asarray(k_eff) / 8.0)))
    noise = rng.normal(0, 1, y.shape)
    item = w.__dict__.get("_item_noise")
    if item is not None and w.rho_models > 0:
        noise = np.sqrt(w.rho_models) * item + np.sqrt(1 - w.rho_models) * noise
    if shared_noise is not None:
        noise = np.sqrt(rho) * shared_noise + np.sqrt(1 - rho) * noise
    return d[:, None] * y + noise, d


def llm_posterior(e, d, prior, overconfidence: float = 1.0):
    """The LLM's own P(member | evidence). With overconfidence > 1 it believes its evidence is
    sharper than it is, so posteriors (and the margins used by routing / abstention) are too extreme."""
    d = d * overconfidence
    llr = d[:, None] * e - d[:, None] ** 2 / 2
    logit = llr + np.log(prior / (1 - prior))
    return 1 / (1 + np.exp(-logit))


# ----------------------------------------------------------------------------- metrics
def metrics(pred: np.ndarray, y: np.ndarray, mask_q=None):
    if mask_q is not None:
        pred, y = pred[mask_q], y[mask_q]
    tp = np.logical_and(pred, y).sum(); fp = np.logical_and(pred, ~y).sum(); fn = np.logical_and(~pred, y).sum()
    p = tp / max(tp + fp, 1); r = tp / max(tp + fn, 1)
    f1 = 2 * p * r / max(p + r, 1e-12)
    exact = np.mean(np.all(pred == y, axis=1)) if len(y) else float("nan")
    return f1, p, r, exact


def cost(model, prompt_tokens, completion_tokens):
    pi, po = PRICES[model]
    return prompt_tokens * pi + completion_tokens * po


# ----------------------------------------------------------------------------- policies
def pol_listwise(w, y, r, rem, level, model, rng, k=None):
    """One call over the top-k of the shortlist (k=None → all 30)."""
    k = w.K if k is None else k
    prior = np.mean(y)
    e, d = llm_evidence(w, y, rem, level, model, rng, k_eff=k)
    post = llm_posterior(e, d, prior, w.overconfidence)
    pred = post > 0.5
    pred[:, k:] = False
    pt = FIXED_PROMPT + per_cand_tokens(level) * k
    ct = OUT_TOKENS[model]
    return pred, post, pt, ct, 1.0


def pol_pointwise(w, y, r, rem, level, model, rng):
    """K independent calls, one candidate each: no dilution, but per-call threshold jitter and K× cost."""
    prior = np.mean(y)
    e, d = llm_evidence(w, y, rem, level, model, rng, dilute=False)
    post = llm_posterior(e, d, prior, w.overconfidence)
    jitter = rng.normal(0, w.pointwise_threshold_jitter, y.shape)
    pred = (np.log(post / (1 - post)) + jitter) > 0
    pt = POINTWISE_PER_CALL * w.K
    ct = 5 * w.K  # score-only answers
    return pred, post, pt, ct, float(w.K)


def pol_adaptive_k(w, y, r, rem, level, model, rng, tau=0.05, kmin=5):
    """知止 — decide BEFORE calling how many candidates to read: the smallest k such that the
    retriever-posterior mass beyond k is < tau (expected members left unread)."""
    rp = retriever_posterior(w, r)
    tail = np.cumsum(rp[:, ::-1], axis=1)[:, ::-1]          # mass from position j to end
    tail = np.concatenate([tail[:, 1:], np.zeros((w.Q, 1))], axis=1)  # mass strictly after j
    k = np.argmax(tail < tau, axis=1) + 1
    k = np.clip(k, kmin, w.K)
    prior = np.mean(y)
    e, d = llm_evidence(w, y, rem, level, model, rng, k_eff=k)
    post = llm_posterior(e, d, prior, w.overconfidence)
    pos = np.arange(w.K)[None, :]
    pred = (post > 0.5) & (pos < k[:, None])
    pt = FIXED_PROMPT + per_cand_tokens(level) * k.mean()
    ct = OUT_TOKENS[model]
    return pred, post, pt, ct, 1.0, k


def pol_cascade(w, y, r, rem, level, rng, band=0.3, cheap="mini", strong="flagship"):
    """无为 — cheap model judges all K; only candidates whose cheap posterior is in the uncertain
    band [0.5-band, 0.5+band] are re-judged by the strong model in one shorter listwise call."""
    prior = np.mean(y)
    e1, d1 = llm_evidence(w, y, rem, level, cheap, rng)
    p1 = llm_posterior(e1, d1, prior, w.overconfidence)
    uncertain = np.abs(p1 - 0.5) < band
    n_unc = uncertain.sum(axis=1)
    e2, d2 = llm_evidence(w, y, rem, level, strong, rng, k_eff=np.maximum(n_unc, 1))
    p2 = llm_posterior(e2, d2, prior, w.overconfidence)
    pred = np.where(uncertain, p2 > 0.5, p1 > 0.5)
    pt_cheap = FIXED_PROMPT + per_cand_tokens(level) * w.K
    pt_strong = np.where(n_unc > 0, FIXED_PROMPT + per_cand_tokens(level) * n_unc, 0.0)
    usd = cost(cheap, pt_cheap, OUT_TOKENS[cheap]) + cost(strong, pt_strong, np.where(n_unc > 0, OUT_TOKENS[strong], 0)).mean()
    calls = 1 + (n_unc > 0).mean()
    return pred, pt_cheap + pt_strong.mean(), OUT_TOKENS[cheap] + OUT_TOKENS[strong] * (n_unc > 0).mean(), usd, calls, (n_unc > 0).mean()


def pol_cascade_evidence(w, y, r, rem, rng, band=0.4, cheap="mini", strong="flagship", lo="L5", hi="L1"):
    """Evidence escalation (M5): the cheap model screens all K at the austere level `lo`; only the
    uncertain band is re-judged by the strong model at the rich level `hi`. Cost mixes the two levels."""
    prior = np.mean(y)
    e1, d1 = llm_evidence(w, y, rem, lo, cheap, rng)
    p1 = llm_posterior(e1, d1, prior, w.overconfidence)
    uncertain = np.abs(p1 - 0.5) < band
    n_unc = uncertain.sum(axis=1)
    e2, d2 = llm_evidence(w, y, rem, hi, strong, rng, k_eff=np.maximum(n_unc, 1))
    p2 = llm_posterior(e2, d2, prior, w.overconfidence)
    pred = np.where(uncertain, p2 > 0.5, p1 > 0.5)
    pt_cheap = FIXED_PROMPT + per_cand_tokens(lo) * w.K
    pt_strong = np.where(n_unc > 0, FIXED_PROMPT + per_cand_tokens(hi) * n_unc, 0.0)
    usd = cost(cheap, pt_cheap, OUT_TOKENS[cheap]) + cost(strong, pt_strong, np.where(n_unc > 0, OUT_TOKENS[strong], 0)).mean()
    calls = 1 + (n_unc > 0).mean()
    return pred, pt_cheap + pt_strong.mean(), OUT_TOKENS[cheap] + OUT_TOKENS[strong] * (n_unc > 0).mean(), usd, calls, (n_unc > 0).mean(), uncertain.mean()


def pol_retriever_prune(w, y, r, rem, level, model, rng, thr=0.02):
    """大道至简 — no cheap model at all: drop candidates whose calibrated retriever posterior is < thr,
    then one listwise call of `model` over the survivors (any position, not just a prefix)."""
    prior = np.mean(y)
    keep = retriever_posterior(w, r) >= thr
    n = keep.sum(axis=1)
    e, d = llm_evidence(w, y, rem, level, model, rng, k_eff=np.maximum(n, 1))
    post = llm_posterior(e, d, prior, w.overconfidence)
    pred = np.where(keep, post > 0.5, False)
    pt = np.where(n > 0, FIXED_PROMPT + per_cand_tokens(level) * n, 0.0)
    ct = np.where(n > 0, OUT_TOKENS[model], 0)
    return pred, pt.mean(), ct.mean(), cost(model, pt, ct).mean(), (n > 0).mean(), n.mean()


def pol_cascade_evidence_reject_only(w, y, r, rem, rng, thr=0.05, cheap="mini", strong="flagship", lo="L5", hi="L1"):
    """Asymmetric evidence escalation: the cheap austere screen may only REJECT (p̂ < thr); every
    survivor is judged by the strong model at the rich level."""
    prior = np.mean(y)
    e1, d1 = llm_evidence(w, y, rem, lo, cheap, rng)
    p1 = llm_posterior(e1, d1, prior, w.overconfidence)
    keep = p1 >= thr
    n = keep.sum(axis=1)
    e2, d2 = llm_evidence(w, y, rem, hi, strong, rng, k_eff=np.maximum(n, 1))
    p2 = llm_posterior(e2, d2, prior, w.overconfidence)
    pred = np.where(keep, p2 > 0.5, False)
    pt1 = FIXED_PROMPT + per_cand_tokens(lo) * w.K
    pt2 = np.where(n > 0, FIXED_PROMPT + per_cand_tokens(hi) * n, 0.0)
    usd = cost(cheap, pt1, OUT_TOKENS[cheap]) + cost(strong, pt2, np.where(n > 0, OUT_TOKENS[strong], 0)).mean()
    return pred, pt1 + pt2.mean(), OUT_TOKENS[cheap] + OUT_TOKENS[strong] * (n > 0).mean(), usd, 1 + (n > 0).mean(), n.mean()


def pol_route(w, y, r, rem, level, rng, theta=0.25, cheap="mini", strong="flagship"):
    """按需分配 — cheap model answers; if its least-confident decision has margin < theta,
    the whole query is escalated to the strong model (need-based budget per query)."""
    prior = np.mean(y)
    e1, d1 = llm_evidence(w, y, rem, level, cheap, rng)
    p1 = llm_posterior(e1, d1, prior, w.overconfidence)
    margin = np.abs(p1 - 0.5)
    # confidence of the query = the smallest margin among candidates that are 'in play'
    q_conf = np.min(margin, axis=1)
    escalate = q_conf < theta
    e2, d2 = llm_evidence(w, y, rem, level, strong, rng)
    p2 = llm_posterior(e2, d2, prior, w.overconfidence)
    pred = np.where(escalate[:, None], p2 > 0.5, p1 > 0.5)
    pt = FIXED_PROMPT + per_cand_tokens(level) * w.K
    usd = cost(cheap, pt, OUT_TOKENS[cheap]) + escalate.mean() * cost(strong, pt, OUT_TOKENS[strong])
    return pred, pt * (1 + escalate.mean()), OUT_TOKENS[cheap] + escalate.mean() * OUT_TOKENS[strong], usd, 1 + escalate.mean(), escalate.mean()


def pol_self_consistency(w, y, r, rem, level, model, rng, n=5):
    prior = np.mean(y)
    shared = rng.normal(0, 1, y.shape)
    votes = np.zeros(y.shape)
    for _ in range(n):
        e, d = llm_evidence(w, y, rem, level, model, rng, shared_noise=shared, rho=w.rho_sc)
        votes += llm_posterior(e, d, prior, w.overconfidence) > 0.5
    pred = votes > n / 2
    pt = (FIXED_PROMPT + per_cand_tokens(level) * w.K) * n
    ct = OUT_TOKENS[model] * n
    return pred, pt, ct


# ----------------------------------------------------------------------------- experiment driver
def run_all(w: World, seeds: int) -> pd.DataFrame:
    rows: list[Result] = []
    for s in range(seeds):
        rng = np.random.default_rng(w.seed * 1000 + s)
        y, r, rem = sample_world(w, rng)
        for level in ["L1", "L5"]:
            for model in ["mini", "flagship", "mini-thinking"]:
                # listwise K=30 (the current E10 design)
                pred, post, pt, ct, calls = pol_listwise(w, y, r, rem, level, model, rng)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result("listwise K=30", level, model, f1, p, rc, ex, pt, ct, cost(model, pt, ct), calls, seed=s))
                # listwise K=10 (cheaper fixed cut)
                pred, post, pt, ct, calls = pol_listwise(w, y, r, rem, level, model, rng, k=10)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result("listwise K=10", level, model, f1, p, rc, ex, pt, ct, cost(model, pt, ct), calls, seed=s))
                # pointwise
                pred, post, pt, ct, calls = pol_pointwise(w, y, r, rem, level, model, rng)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result("pointwise ×30", level, model, f1, p, rc, ex, pt, ct, cost(model, pt, ct), calls, seed=s))
                # adaptive k
                for tau in (0.02, 0.05, 0.10):
                    pred, post, pt, ct, calls, k = pol_adaptive_k(w, y, r, rem, level, model, rng, tau=tau)
                    f1, p, rc, ex = metrics(pred, y)
                    rows.append(Result(f"adaptive-K τ={tau}", level, model, f1, p, rc, ex, pt, ct, cost(model, pt, ct), calls, seed=s, extra=f"mean_k={k.mean():.1f}"))
                # self-consistency n=5 (flagship only is the interesting comparison, but do all)
                pred, pt, ct = pol_self_consistency(w, y, r, rem, level, model, rng, n=5)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result("self-consistency n=5", level, model, f1, p, rc, ex, pt, ct, cost(model, pt, ct), 5.0, seed=s))
                # abstention (selective prediction) on listwise K=30
                pred, post, pt, ct, calls = pol_listwise(w, y, r, rem, level, model, rng)
                conf = np.max(np.abs(post - 0.5), axis=1) * 2  # confidence of the most certain decision
                qmargin = np.min(np.abs(post - 0.5), axis=1) * 2  # least certain decision
                for tau in (0.2, 0.4, 0.6):
                    keep = qmargin >= tau
                    f1, p, rc, ex = metrics(pred, y, mask_q=keep)
                    rows.append(Result(f"abstain if min-margin<{tau}", level, model, f1, p, rc, ex, pt, ct, cost(model, pt, ct), calls, coverage=keep.mean(), seed=s))
            # two-model policies
            for band in (0.2, 0.3, 0.4):
                pred, pt, ct, usd, calls, frac = pol_cascade(w, y, r, rem, level, rng, band=band)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result(f"cascade mini→flagship band={band}", level, "mini+flagship", f1, p, rc, ex, pt, ct, usd, calls, seed=s, extra=f"strong_call_frac={frac:.2f}"))
            for thr in (0.02, 0.05):
                pred, pt, ct, usd, calls, nkeep = pol_retriever_prune(w, y, r, rem, level, "flagship", rng, thr=thr)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result(f"retriever-prune p≥{thr} → flagship", level, "flagship", f1, p, rc, ex, pt, ct, usd, calls, seed=s, extra=f"mean_kept={nkeep:.1f}"))
            if level == "L1":
                pred, pt, ct, usd, calls, nkeep = pol_cascade_evidence_reject_only(w, y, r, rem, rng, thr=0.05)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result("evidence-cascade reject-only mini@L5 p<0.05 → flagship@L1", level, "mini+flagship", f1, p, rc, ex, pt, ct, usd, calls, seed=s, extra=f"mean_kept={nkeep:.1f}"))
                for band in (0.4, 0.45):
                    pred, pt, ct, usd, calls, frac, cand_frac = pol_cascade_evidence(w, y, r, rem, rng, band=band)
                    f1, p, rc, ex = metrics(pred, y)
                    rows.append(Result(f"evidence-cascade mini@L5→flagship@L1 band={band}", level, "mini+flagship", f1, p, rc, ex, pt, ct, usd, calls, seed=s,
                                       extra=f"strong_call_frac={frac:.2f} escalated_cands={cand_frac*w.K:.1f}"))
            for theta in (0.15, 0.25, 0.35):
                pred, pt, ct, usd, calls, frac = pol_route(w, y, r, rem, level, rng, theta=theta)
                f1, p, rc, ex = metrics(pred, y)
                rows.append(Result(f"route mini→flagship θ={theta}", level, "mini+flagship", f1, p, rc, ex, pt, ct, usd, calls, seed=s, extra=f"escalated={frac:.2f}"))
    return pd.DataFrame([asdict(x) for x in rows])


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(["level", "model", "policy"])
    out = g.agg(f1=("f1", "mean"), f1_sd=("f1", "std"), precision=("precision", "mean"), recall=("recall", "mean"),
                exact_set=("exact_set", "mean"), prompt_tokens=("prompt_tokens", "mean"), completion_tokens=("completion_tokens", "mean"),
                usd_per_query=("usd_per_query", "mean"), calls_per_query=("calls_per_query", "mean"), coverage=("coverage", "mean"),
                n_seeds=("seed", "nunique")).reset_index()
    out["f1_ci95"] = 1.96 * out["f1_sd"] / np.sqrt(out["n_seeds"])
    return out


# ----------------------------------------------------------------------------- figures
def fig_pareto(summary: pd.DataFrame, level: str, fname: str):
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.DOUBLE_COL, 3.4))
    d = summary[(summary.level == level) & (summary.coverage >= 0.999)]
    markers = {"mini": "o", "flagship": "s", "mini-thinking": "^", "mini+flagship": "D"}
    colors = {"mini": fs.MODEL_COLORS["xj-gpt-4.1-mini"], "flagship": fs.MODEL_COLORS["xj-gpt-4.1"],
              "mini-thinking": fs.MODEL_COLORS["xj-gpt-5.4-mini"], "mini+flagship": fs.OKABE_ITO["green"]}
    for _, r in d.iterrows():
        ax.errorbar(r.usd_per_query * 100, r.f1, yerr=r.f1_ci95, fmt=markers[r.model], color=colors[r.model], ms=5, capsize=1.5, lw=0.8, mec="black", mew=0.4)
        lab = r.policy.replace("listwise ", "LW ").replace("adaptive-K ", "aK ").replace("self-consistency", "SC").replace("cascade mini→flagship ", "cascade ").replace("route mini→flagship ", "route ").replace("evidence-cascade mini@L5→flagship@L1 ", "evid-cascade L5→L1 ").replace("evidence-cascade reject-only mini@L5 p<0.05 → flagship@L1", "evid-cascade reject-only L5→L1").replace("retriever-prune ", "r-prune ")
        ax.annotate(lab, (r.usd_per_query * 100, r.f1), xytext=(4, 2), textcoords="offset points", fontsize=5.4, color=colors[r.model])
    # Pareto frontier
    dd = d.sort_values("usd_per_query")
    best = -1; fx, fy = [], []
    for _, r in dd.iterrows():
        if r.f1 > best:
            best = r.f1; fx.append(r.usd_per_query * 100); fy.append(r.f1)
    ax.step(fx, fy, where="post", color="black", lw=0.9, alpha=0.6, label="Pareto frontier")
    # iso-budget: flagship listwise K=30 (today's design) — highlighted
    today = d[(d.policy == "listwise K=30") & (d.model == "flagship")].iloc[0]
    ref = today.usd_per_query * 100
    ax.axvline(ref, color="grey", ls="--", lw=0.8)
    ax.scatter([ref], [today.f1], marker="*", s=160, color="gold", edgecolor="black", linewidth=0.6, zorder=5)
    ax.annotate("today's design:\nflagship listwise K=30", (ref, today.f1), xytext=(8, -26), textcoords="offset points", fontsize=6.2,
                arrowprops=dict(arrowstyle="-", lw=0.5, color="black"))
    ax.annotate("iso-budget", (ref, ax.get_ylim()[1]), xytext=(3, -8), textcoords="offset points", fontsize=6, color="grey")
    ax.set_xscale("log"); ax.set_xlabel("simulated relay cost per query (US cents, log; prices from the real ledger)")
    ax.set_ylabel("pairwise F1 (synthetic world)")
    for m, mk in markers.items():
        ax.scatter([], [], marker=mk, color=colors[m], edgecolor="black", linewidth=0.4, label={"mini": "GPT-4.1-mini class", "flagship": "flagship class", "mini-thinking": "thinking-mini class", "mini+flagship": "two-model policies"}[m])
    ax.legend(loc="lower right", fontsize=6.5)
    ax.set_title(f"Quality–cost design space at level {level} (synthetic accuracy, real token prices; mean ± 95 % CI over seeds)", loc="left", fontsize=8)
    fs.save(fig, FIG / fname)


def fig_adaptive_k(w: World, fname: str):
    """Recall vs tokens as a function of how many shortlist positions are read, for 3 retriever strengths."""
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.SINGLE_COL * 1.7, 2.6))
    rng = np.random.default_rng(123)
    for dr, col in zip((1.0, 1.5, 2.0), (fs.OKABE_ITO["vermilion"], fs.OKABE_ITO["blue"], fs.OKABE_ITO["green"])):
        ww = replace(w, retriever_dprime=dr, Q=20000)
        y, r, rem = sample_world(ww, rng)
        ks = np.arange(1, 31)
        rec = [y[:, :k].sum() / y.sum() for k in ks]
        toks = [FIXED_PROMPT + per_cand_tokens("L1") * k for k in ks]
        ax.plot(toks, rec, color=col, label=f"retriever d'={dr}")
        for k in (5, 10, 15, 20, 30):
            ax.annotate(f"K={k}", (toks[k - 1], rec[k - 1]), xytext=(3, -8), textcoords="offset points", fontsize=5.5, color=col)
    ax.set_xlabel("prompt tokens per query (L1 calibration)"); ax.set_ylabel("recall of the read prefix\n(relative to recall@30 of the shortlist)")
    ax.set_title("Knowing when to stop: how much of the shortlist is worth reading", loc="left")
    ax.legend(fontsize=6.5, loc="lower right")
    fs.save(fig, FIG / fname)


def fig_memory_mixing(w: World, fname: str):
    """Observed ladder accuracy = mixture of remembered and evidence-driven queries."""
    fs.apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(fs.DOUBLE_COL, 2.7))
    rng = np.random.default_rng(7)
    levels = ["L1", "L3", "L5", "L6"]
    ax = axes[0]
    for pm, col in zip((0.0, 0.3, 0.6), (fs.OKABE_ITO["blue"], fs.OKABE_ITO["orange"], fs.OKABE_ITO["vermilion"])):
        ww = replace(w, p_mem=pm, Q=6000)
        y, r, rem = sample_world(ww, rng)
        f1s = []
        for lv in levels:
            pred, *_ = pol_listwise(ww, y, r, rem, lv, "flagship", rng)
            f1s.append(metrics(pred, y)[0])
        ax.plot(levels, f1s, "o-", color=col, label=f"p_mem={pm:.1f}")
    ax.set_ylabel("observed pairwise F1"); ax.set_title("(a) Memorised queries flatten the ladder", loc="left")
    ax.legend(fontsize=6.5)
    ax = axes[1]
    ww = replace(w, p_mem=0.3, Q=6000)
    y, r, rem = sample_world(ww, rng)
    obs, evid, memo = [], [], []
    for lv in levels:
        pred, *_ = pol_listwise(ww, y, r, rem, lv, "flagship", rng)
        obs.append(metrics(pred, y)[0]); evid.append(metrics(pred, y, mask_q=~rem)[0]); memo.append(metrics(pred, y, mask_q=rem)[0])
    ax.plot(levels, obs, "o-", color="black", label="all queries (what a leaderboard reports)")
    ax.plot(levels, evid, "s--", color=fs.OKABE_ITO["blue"], label="non-memorised queries only")
    ax.plot(levels, memo, "^:", color=fs.OKABE_ITO["vermilion"], label="memorised queries only")
    ax.set_title("(b) Stratify by the forced-choice probe to un-mix", loc="left")
    ax.legend(fontsize=6.2, loc="lower left")
    for a in axes:
        a.set_ylim(0, 1.02)
    fs.save(fig, FIG / fname)


def fig_risk_coverage(df: pd.DataFrame, fname: str):
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.SINGLE_COL * 1.6, 2.5))
    d = df[df.policy.str.startswith("abstain") | (df.policy == "listwise K=30")]
    d = d[d.level == "L5"]
    for model, col in (("mini", fs.OKABE_ITO["orange"]), ("flagship", fs.OKABE_ITO["blue"])):
        s = d[d.model == model].groupby("policy").agg(cov=("coverage", "mean"), prec=("precision", "mean"), f1=("f1", "mean")).sort_values("cov")
        name = "mini class" if model == "mini" else "flagship class"
        ax.plot(s["cov"], s["prec"], "o-", color=col, label=f"{name} — precision on answered")
        ax.plot(s["cov"], s["f1"], "s--", color=col, alpha=0.7, label=f"{name} — F1 on answered")
    ax.set_xlabel("coverage (share of queries the agent answers)"); ax.set_ylabel("precision / F1 on answered queries")
    ax.set_title("Abstaining on low-margin queries (L5)", loc="left")
    ax.legend(fontsize=5.8, loc="lower left")
    fs.save(fig, FIG / fname)


def fig_equal_budget_bars(summary: pd.DataFrame, fname: str):
    """At the budget of today's design (flagship listwise K=30), what does each policy deliver?"""
    fs.apply_style()
    fig, axes = plt.subplots(2, 1, figsize=(fs.DOUBLE_COL, 5.2))
    for ax, level in zip(axes, ("L1", "L5")):
        d = summary[(summary.level == level) & (summary.coverage >= 0.999)].copy()
        ref = d[(d.policy == "listwise K=30") & (d.model == "flagship")]
        ref_cost = ref.usd_per_query.iloc[0]; ref_f1 = ref.f1.iloc[0]
        d["rel_cost"] = d.usd_per_query / ref_cost
        d = d[(d.rel_cost <= 1.05)].sort_values("f1", ascending=False).head(12).sort_values("f1", ascending=True)
        lab = d.model.map({"mini": "mini", "flagship": "flagship", "mini-thinking": "thinking-mini", "mini+flagship": "two-model"}) + " · " + d.policy
        colors = d.model.map({"mini": fs.MODEL_COLORS["xj-gpt-4.1-mini"], "flagship": fs.MODEL_COLORS["xj-gpt-4.1"], "mini-thinking": fs.MODEL_COLORS["xj-gpt-5.4-mini"], "mini+flagship": fs.OKABE_ITO["green"]})
        bars = ax.barh(lab, d.f1, xerr=d.f1_ci95, color=colors, zorder=2, error_kw={"lw": 0.6}, height=0.7)
        for b, rc_, pol in zip(bars, d.rel_cost, d.policy):
            txt = f"{rc_*100:.0f}% of budget" + ("  ← today" if pol == "listwise K=30" and rc_ > 0.99 else "")
            ax.annotate(txt, (b.get_width(), b.get_y() + b.get_height() / 2), xytext=(3, 0), textcoords="offset points", va="center", fontsize=6)
        ax.axvline(ref_f1, color="grey", ls="--", lw=0.8)
        ax.set_xlim(max(0, d.f1.min() - 0.08), min(1, d.f1.max() + 0.1))
        ax.tick_params(axis="y", labelsize=6.5)
        ax.set_xlabel("pairwise F1 (synthetic world; mean ± 95 % CI over seeds)")
        ax.set_title(f"{level}: the 12 best policies costing ≤ 105 % of today's design (flagship listwise K=30, dashed = its F1)", loc="left", fontsize=7.5)
        ax.grid(axis="x", linestyle=":", alpha=0.7); ax.grid(axis="y", visible=False)
    fig.tight_layout(h_pad=1.5)
    fs.save(fig, FIG / fname)


def fig_sweep(sw: pd.DataFrame, fname: str):
    """What the equal-budget verdict depends on (216 synthetic worlds)."""
    fs.apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(fs.DOUBLE_COL, 3.1))
    # (a) pointwise − listwise as a function of list dilution
    ax = axes[0]
    g = sw.groupby("beta_dilution")["ptw_minus_lw"]
    ax.errorbar(g.mean().index, g.mean().values, yerr=[g.mean().values - g.min().values, g.max().values - g.mean().values], fmt="o-", color=fs.OKABE_ITO["blue"], capsize=3)
    ax.axhline(0, color="grey", lw=0.8)
    ax.set_xlabel("list-dilution β"); ax.set_ylabel("ΔF1, pointwise − listwise K=30")
    ax.set_title("(a) Pointwise (3.5× cost) pays only\nif long lists dilute the model", loc="left", fontsize=7.5)
    # (b) adaptive-K gain & cost vs retriever quality
    ax = axes[1]
    g = sw.groupby("retriever_dprime")[["ak05_minus_lw", "ak05_cost_frac"]].mean()
    ax.plot(g.index, g.ak05_minus_lw, "o-", color=fs.OKABE_ITO["green"])
    ax.set_ylabel("ΔF1, adaptive-K − K=30", color=fs.OKABE_ITO["green"])
    ax2 = ax.twinx(); ax2.plot(g.index, g.ak05_cost_frac * 100, "s--", color=fs.OKABE_ITO["vermilion"]); ax2.set_ylabel("cost, % of K=30", color=fs.OKABE_ITO["vermilion"])
    ax2.spines["right"].set_visible(True); ax2.grid(False)
    ax.set_xlabel("first-stage retriever d'"); ax.set_title("(b) Adaptive-K: the better the retriever,\nthe less you need to read", loc="left", fontsize=7.5)
    ax.axhline(0, color="grey", lw=0.8)
    # (c) best family at equal budget, by dilution
    ax = axes[2]
    fam = sw.best_policy_at_budget.str.extract(r"^(mini\+flagship · evidence-cascade|mini\+flagship · cascade|mini\+flagship · route|flagship · adaptive-K|flagship · retriever-prune|flagship · listwise K=10|flagship · listwise K=30|mini · pointwise)")[0]
    fam = fam.map({"mini+flagship · cascade": "cascade mini→flagship (same level)", "mini+flagship · evidence-cascade": "evidence cascade mini@L5→flagship@L1",
                   "mini+flagship · route": "route mini→flagship", "flagship · adaptive-K": "flagship adaptive-K", "flagship · retriever-prune": "flagship retriever-prune",
                   "flagship · listwise K=10": "flagship listwise K=10", "flagship · listwise K=30": "today's design", "mini · pointwise": "mini pointwise"})
    ct = pd.crosstab(sw.beta_dilution, fam, normalize="index") * 100
    order = ["cascade mini→flagship (same level)", "evidence cascade mini@L5→flagship@L1", "flagship adaptive-K", "flagship retriever-prune", "flagship listwise K=10", "route mini→flagship", "mini pointwise", "today's design"]
    ct = ct.reindex(columns=[c for c in order if c in ct.columns]).fillna(0)
    cols = [fs.OKABE_ITO["green"], "#66C2A5", fs.OKABE_ITO["blue"], "#4C72B0", fs.OKABE_ITO["sky"], fs.OKABE_ITO["purple"], fs.OKABE_ITO["orange"], "lightgrey"]
    bottom = np.zeros(len(ct))
    for c, col in zip(ct.columns, cols):
        ax.bar([str(b) for b in ct.index], ct[c], bottom=bottom, color=col, label=c, width=0.6, zorder=2)
        bottom += ct[c].values
    ax.set_xlabel("list-dilution β"); ax.set_ylabel("% of worlds where best at ≤ budget")
    ax.set_title("(c) Who wins at today's budget", loc="left", fontsize=7.5)
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=4, fontsize=6, bbox_to_anchor=(0.5, -0.04), frameon=False)
    fig.tight_layout(w_pad=1.6, rect=[0, 0.11, 1, 1])
    fs.save(fig, FIG / fname)


# ----------------------------------------------------------------------------- sweep
def sweep(base: World, seeds: int) -> pd.DataFrame:
    grid = []
    for p_mem in (0.0, 0.3, 0.6):
        for beta in (0.0, 0.06, 0.12):
            for rd in (1.0, 1.5, 2.0):
                for mq in (0.6, 0.9):
                    for rm in (0.3, 0.7):
                        for oc in (1.0, 1.4):
                            grid.append(dict(p_mem=p_mem, beta_dilution=beta, retriever_dprime=rd, mini_quality=mq, rho_models=rm, overconfidence=oc))
    rows = []
    for g in grid:
        w = replace(base, p_mem=g["p_mem"], beta_dilution=g["beta_dilution"], retriever_dprime=g["retriever_dprime"],
                    rho_models=g["rho_models"], overconfidence=g["overconfidence"],
                    model_quality=(("mini", g["mini_quality"]), ("flagship", 1.0), ("mini-thinking", 0.9)), Q=1500)
        df = run_all(w, seeds)
        s = summarize(df)
        for level in ("L1", "L5"):
            d = s[(s.level == level) & (s.coverage >= 0.999)]
            ref = d[(d.policy == "listwise K=30") & (d.model == "flagship")].iloc[0]
            cheaper = d[d.usd_per_query <= ref.usd_per_query * 1.05]
            best = cheaper.sort_values("f1", ascending=False).iloc[0]
            rows.append({**g, "level": level, "ref_f1": ref.f1, "best_policy_at_budget": f"{best.model} · {best.policy}", "best_f1": best.f1,
                         "best_cost_frac": best.usd_per_query / ref.usd_per_query, "gain": best.f1 - ref.f1,
                         "ptw_minus_lw": d[(d.policy == "pointwise ×30") & (d.model == "flagship")].f1.iloc[0] - ref.f1,
                         "sc5_minus_lw": d[(d.policy == "self-consistency n=5") & (d.model == "flagship")].f1.iloc[0] - ref.f1,
                         "ak05_minus_lw": d[(d.policy == "adaptive-K τ=0.05") & (d.model == "flagship")].f1.iloc[0] - ref.f1,
                         "ak05_cost_frac": d[(d.policy == "adaptive-K τ=0.05") & (d.model == "flagship")].usd_per_query.iloc[0] / ref.usd_per_query})
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Q", type=int, default=3000)
    ap.add_argument("--seeds", type=int, default=8)
    ap.add_argument("--sweep", action="store_true")
    ap.add_argument("--plot-sweep-only", action="store_true", help="re-draw the sweep figure from sim/results/sensitivity_sweep.csv")
    args = ap.parse_args()
    if args.plot_sweep_only:
        FIG.mkdir(parents=True, exist_ok=True)
        fig_sweep(pd.read_csv(RES / "sensitivity_sweep.csv"), "S8_sweep_sensitivity")
        print("sweep figure redrawn"); return
    RES.mkdir(parents=True, exist_ok=True); FIG.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    w = World(Q=args.Q)
    df = run_all(w, args.seeds)
    df.to_csv(RES / "policies_raw.csv", index=False)
    s = summarize(df)
    s.to_csv(RES / "policies_summary.csv", index=False)
    fig_pareto(s, "L1", "S1_pareto_L1")
    fig_pareto(s, "L5", "S2_pareto_L5")
    fig_equal_budget_bars(s, "S3_equal_budget")
    fig_adaptive_k(w, "S4_adaptive_k_recall_ceiling")
    fig_memory_mixing(w, "S5_memory_mixing")
    fig_risk_coverage(df, "S6_risk_coverage")
    log = [f"# Simulation run log", "", f"- started: {time.strftime('%Y-%m-%d %H:%M:%S %Z')}", f"- world: `{json.dumps({k: v for k, v in asdict(w).items() if not k.startswith('_')})}`",
           f"- seeds: {args.seeds}, queries per seed: {args.Q}", f"- elapsed: {time.time()-t0:.1f} s", "",
           "## Headline table (mean over seeds; coverage = 1 policies)", ""]
    for level in ("L1", "L5"):
        d = s[(s.level == level) & (s.coverage >= 0.999)].sort_values("usd_per_query")
        log.append(f"### {level}\n\n| model | policy | F1 ± CI95 | P | R | exact-set | ¢/query | calls/query |\n| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |")
        for _, r in d.iterrows():
            log.append(f"| {r.model} | {r.policy} | {r.f1:.3f} ± {r.f1_ci95:.3f} | {r.precision:.3f} | {r.recall:.3f} | {r.exact_set:.3f} | {r.usd_per_query*100:.2f} | {r.calls_per_query:.2f} |")
        log.append("")
    if args.sweep:
        t1 = time.time()
        sw = sweep(w, max(2, args.seeds // 4))
        sw.to_csv(RES / "sensitivity_sweep.csv", index=False)
        fig_sweep(sw, "S8_sweep_sensitivity")
        log += [f"## Sensitivity sweep ({len(sw)//2} worlds × 2 levels)", "",
                f"- elapsed: {time.time()-t1:.1f} s",
                f"- share of worlds where some policy beats today's design at ≤105 % of its budget: L1 {np.mean(sw[sw.level=='L1'].gain>0.005):.0%}, L5 {np.mean(sw[sw.level=='L5'].gain>0.005):.0%}",
                f"- pointwise − listwise (flagship) F1: median {sw.ptw_minus_lw.median():+.3f}, range [{sw.ptw_minus_lw.min():+.3f}, {sw.ptw_minus_lw.max():+.3f}] at 3× the cost",
                f"- self-consistency n=5 − single (flagship): median {sw.sc5_minus_lw.median():+.3f}, range [{sw.sc5_minus_lw.min():+.3f}, {sw.sc5_minus_lw.max():+.3f}] at 5× the cost",
                f"- adaptive-K τ=0.05 − K=30 (flagship): median {sw.ak05_minus_lw.median():+.3f}, range [{sw.ak05_minus_lw.min():+.3f}, {sw.ak05_minus_lw.max():+.3f}] at median {sw.ak05_cost_frac.median():.0%} of the cost",
                "", "Best policy at budget, by world:", "", sw.groupby(["level", "best_policy_at_budget"]).size().to_string(), ""]
    (RES / ("RUNLOG.md" if args.sweep else "RUNLOG_base.md")).write_text("\n".join(log), encoding="utf-8")
    print("\n".join(log))


if __name__ == "__main__":
    main()
