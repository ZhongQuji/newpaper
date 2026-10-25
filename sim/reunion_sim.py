#!/usr/bin/env python3
"""Calibrated design-space simulation for the shortlist-reunion agent — v2.

v2 implements the red-team code review (docs/reviews/redteam_sim_code_review.md):
  * every policy is compared at a MATCHED OPERATING POINT: its decision threshold is tuned for F1
    on selection seeds and evaluated on held-out seeds (the fixed-0.5 numbers are still written);
  * memorisation is model-specific (the mini remembers a subset of what the flagship remembers, less
    sharply) and can be WORD-KEYED (fires only at rungs that show title/creator) or RECORD-KEYED;
  * the retriever posterior can be mis-specified (believed d'_r ≠ true d'_r);
  * confidence used for routing / cascading / abstaining can be made less informative (conf_noise),
    separately from the decision itself;
  * two zero-extra-cost baselines the review found missing: "retriever-only" (no LLM call at all —
    the no-intervention null) and "listwise with retriever-informed per-candidate prior";
  * pointwise cost is level- and model-specific; self-consistency correlation is composed correctly;
    routing escalates on the margin of candidates in play, not of all 30;
  * the sweep selects the best policy on 2 seeds and evaluates it on 2 held-out seeds, and calls a
    policy better only if the held-out gain exceeds 0.02 F1;
  * CIs use the t quantile for the number of seeds; every headline is also reported on the
    non-memorised stratum.

WHAT IS REAL (data/real/runs.csv): prompt tokens per 30-candidate call per level, fitted to the
token model  prompt = 128 + (K+1)·r_level  (r = tokens per record: L1 59, L3 53, L5 35, L6 30),
which also reproduces the measured pointwise call (128 + 2r = 246 tok at L1, E10e); completion tokens
per listwise call (≈70 non-thinking, ≈500 thinking); effective relay prices (least squares on 55
text-only runs, ≤5.6 % error).

WHAT IS SYNTHETIC: everything about accuracy. Absolute F1 values do not transfer; orderings and
sensitivities are the deliverable, and even those only within the swept assumptions (sim/README.md).

Run:  python3 sim/reunion_sim.py                  # base world, 3,000 queries × 8 seeds
      python3 sim/reunion_sim.py --sweep          # + 324-world sensitivity grid (held-out seeds)
      python3 sim/reunion_sim.py --plot-sweep-only
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass, asdict, replace, field
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import t as student_t

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import figstyle as fs  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

RES = ROOT / "sim/results"
FIG = ROOT / "figures/sim"

# ----------------------------------------------------------------------------- calibration (real)
PRICES = {  # USD per token (prompt, completion), fitted on the real ledger
    "mini": (1.709e-6, 8.098e-6),
    "flagship": (8.877e-6, 36.195e-6),
    "mini-thinking": (3.290e-6, 20.344e-6),
}
OUT_LISTWISE = {"mini": 70, "flagship": 70, "mini-thinking": 500}      # completion tokens / listwise call
OUT_POINTWISE = {"mini": 1, "flagship": 1, "mini-thinking": 300}       # score-only P(yes) vs hidden reasoning
LEVEL_PROMPT = {"L1": 1959, "L3": 1784, "L5": 1208, "L6": 1064}       # measured, K=30
OVERHEAD = 128                                                        # instructions (fitted)


def rec_tokens(level: str) -> float:
    return (LEVEL_PROMPT[level] - OVERHEAD) / 31.0


def listwise_prompt(level: str, k) -> np.ndarray | float:
    return OVERHEAD + (np.asarray(k) + 1) * rec_tokens(level)


def pointwise_prompt(level: str) -> float:
    return OVERHEAD + 2 * rec_tokens(level)


def cost(model: str, prompt_tokens, completion_tokens):
    pi, po = PRICES[model]
    return np.asarray(prompt_tokens) * pi + np.asarray(completion_tokens) * po


# ----------------------------------------------------------------------------- world (synthetic)
@dataclass
class World:
    Q: int = 3000
    K: int = 30
    member_probs: tuple = (0.15, 0.35, 0.25, 0.13, 0.08, 0.04)
    retriever_dprime: float = 1.5
    belief_factor: float = 1.0        # believed d'_r = belief_factor × true d'_r (1 = well calibrated)
    p_mem: float = 0.30               # share of queries the FLAGSHIP remembers
    mem_share: tuple = (("mini", 0.6), ("flagship", 1.0), ("mini-thinking", 0.8))   # × p_mem, nested sets
    dprime_mem: tuple = (("mini", 3.0), ("flagship", 4.0), ("mini-thinking", 3.5))
    mem_keying: str = "record"        # "record": memory fires at every rung; "word": only where title/creator shown
    word_rungs: tuple = ("L1", "L3")  # rungs that still show the words memory is keyed to
    dprime_level: tuple = (("L1", 2.4), ("L3", 2.0), ("L5", 1.3), ("L6", 1.0))
    model_quality: tuple = (("mini", 0.75), ("flagship", 1.0), ("mini-thinking", 0.9))
    beta_dilution: float = 0.06
    pointwise_threshold_jitter: float = 0.35
    rho_sc: float = 0.5               # TOTAL correlation between self-consistency samples
    rho_models: float = 0.5           # correlation of evidence noise between two models (shared item difficulty)
    conf_noise: float = 0.0           # sd of logit noise on the confidence used for routing/cascading/abstaining
    rho_retriever_llm: float = 0.0    # share of the retriever's noise that is the SAME item difficulty the LLM sees
    seed: int = 0

    def dprime(self, level, model):
        return dict(self.dprime_level)[level] * dict(self.model_quality)[model]


@dataclass
class Out:
    score: np.ndarray          # per-candidate posterior-like score; unread candidates = 0
    usd: float                 # mean USD per query
    prompt_tok: float
    completion_tok: float
    calls: float
    extra: str = ""


def sample_world(w: World, rng):
    m = rng.choice(len(w.member_probs), size=w.Q, p=np.array(w.member_probs))
    y = np.zeros((w.Q, w.K), dtype=bool)
    for q in range(w.Q):
        if m[q]:
            y[q, rng.choice(w.K, size=m[q], replace=False)] = True
    item = rng.normal(0, 1, (w.Q, w.K))                   # shared item difficulty (seen by every model)
    r_noise = np.sqrt(w.rho_retriever_llm) * item + np.sqrt(1 - w.rho_retriever_llm) * rng.normal(0, 1, (w.Q, w.K))
    r = r_noise + w.retriever_dprime * y
    order = np.argsort(-r, axis=1)
    y = np.take_along_axis(y, order, axis=1); r = np.take_along_axis(r, order, axis=1); item = np.take_along_axis(item, order, axis=1)
    u = rng.random(w.Q)                                   # latent "fame": nested memorised sets per model
    rem = {mname: u < w.p_mem * share for mname, share in w.mem_share}
    return y, r, rem, item


def retriever_posterior(w: World, r):
    """What the system BELIEVES: ideal-observer posterior with believed d'_r and true prevalence."""
    pi = float(np.dot(np.arange(len(w.member_probs)), w.member_probs)) / w.K
    d = w.retriever_dprime * w.belief_factor
    llr = d * r - d ** 2 / 2
    return 1 / (1 + np.exp(-(llr + np.log(pi / (1 - pi)))))


def llm_evidence(w, y, rem, item, level, model, rng, k_eff=None, dilute=True, shared=None, a_shared=0.0):
    d = np.full(w.Q, w.dprime(level, model))
    mem_active = w.mem_keying == "record" or level in w.word_rungs
    if mem_active:
        d[rem[model]] = dict(w.dprime_mem)[model]
    if dilute:
        k_eff = w.K if k_eff is None else k_eff
        d = d * (1 - w.beta_dilution * np.maximum(0.0, np.log2(np.asarray(k_eff) / 8.0)))
    fresh = rng.normal(0, 1, y.shape)
    if shared is not None:
        fresh = np.sqrt(a_shared) * shared + np.sqrt(1 - a_shared) * fresh
    noise = np.sqrt(w.rho_models) * item + np.sqrt(1 - w.rho_models) * fresh
    return d[:, None] * y + noise, d


def llm_posterior(e, d, prior):
    llr = d[:, None] * e - d[:, None] ** 2 / 2
    prior = np.asarray(prior)
    return 1 / (1 + np.exp(-(llr + np.log(prior / (1 - prior)))))


def noisy_conf(w, p, rng):
    """Confidence as seen by the controller (routing/cascade/abstention): may be less informative."""
    if w.conf_noise == 0:
        return p
    z = np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))) + rng.normal(0, w.conf_noise, p.shape)
    return 1 / (1 + np.exp(-z))


# ----------------------------------------------------------------------------- policies
def pol_retriever_only(w, y, r, rem, item, rng, **_):
    return Out(retriever_posterior(w, r), 0.0, 0.0, 0.0, 0.0, "no LLM call")


def pol_listwise(w, y, r, rem, item, rng, level, model, k=None, retriever_prior=False):
    k = w.K if k is None else k
    prior = np.mean(y)
    e, d = llm_evidence(w, y, rem, item, level, model, rng, k_eff=k)
    pr = retriever_posterior(w, r) if retriever_prior else prior
    post = llm_posterior(e, d, pr)
    post[:, k:] = 0.0
    pt = float(listwise_prompt(level, k)); ct = OUT_LISTWISE[model]
    return Out(post, float(cost(model, pt, ct)), pt, ct, 1.0)


def pol_pointwise(w, y, r, rem, item, rng, level, model):
    prior = np.mean(y)
    e, d = llm_evidence(w, y, rem, item, level, model, rng, dilute=False)
    post = llm_posterior(e, d, prior)
    z = np.log(post / (1 - post)) + rng.normal(0, w.pointwise_threshold_jitter, y.shape)
    pt = pointwise_prompt(level) * w.K; ct = OUT_POINTWISE[model] * w.K
    return Out(1 / (1 + np.exp(-z)), float(cost(model, pt, ct)), pt, ct, float(w.K))


def pol_adaptive_k(w, y, r, rem, item, rng, level, model, tau=0.05, kmin=5):
    rp = retriever_posterior(w, r)
    tail = np.cumsum(rp[:, ::-1], axis=1)[:, ::-1]
    tail = np.concatenate([tail[:, 1:], np.zeros((w.Q, 1))], axis=1)
    k = np.clip(np.argmax(tail < tau, axis=1) + 1, kmin, w.K)
    prior = np.mean(y)
    e, d = llm_evidence(w, y, rem, item, level, model, rng, k_eff=k)
    post = llm_posterior(e, d, prior)
    post[np.arange(w.K)[None, :] >= k[:, None]] = 0.0
    pt = listwise_prompt(level, k); ct = OUT_LISTWISE[model]
    return Out(post, float(cost(model, pt, ct).mean()), float(pt.mean()), ct, 1.0, f"mean_k={k.mean():.1f}")


def pol_retriever_prune(w, y, r, rem, item, rng, level, model, thr=0.02, retriever_prior=False):
    rp = retriever_posterior(w, r)
    keep = rp >= thr
    n = keep.sum(axis=1)
    prior = rp if retriever_prior else np.mean(y)
    e, d = llm_evidence(w, y, rem, item, level, model, rng, k_eff=np.maximum(n, 1))
    post = llm_posterior(e, d, prior)
    post[~keep] = 0.0
    pt = np.where(n > 0, listwise_prompt(level, n), 0.0); ct = np.where(n > 0, OUT_LISTWISE[model], 0)
    return Out(post, float(cost(model, pt, ct).mean()), float(pt.mean()), float(ct.mean()), float((n > 0).mean()), f"mean_kept={n.mean():.1f}")


def pol_cascade(w, y, r, rem, item, rng, lo_level, hi_level, band=0.4, cheap="mini", strong="flagship", reject_only=False, rej_thr=0.05):
    """Cheap model screens all K at lo_level; candidates in the uncertain band (or all non-rejected,
    if reject_only) are re-judged by the strong model at hi_level in one short listwise call."""
    prior = np.mean(y)
    e1, d1 = llm_evidence(w, y, rem, item, lo_level, cheap, rng)
    p1 = llm_posterior(e1, d1, prior)
    c1 = noisy_conf(w, p1, rng)
    esc = (c1 >= rej_thr) if reject_only else (np.abs(c1 - 0.5) < band)
    n = esc.sum(axis=1)
    e2, d2 = llm_evidence(w, y, rem, item, hi_level, strong, rng, k_eff=np.maximum(n, 1))
    p2 = llm_posterior(e2, d2, prior)
    score = np.where(esc, p2, p1)
    if reject_only:
        score = np.where(esc, p2, 0.0)
    pt1 = float(listwise_prompt(lo_level, w.K)); pt2 = np.where(n > 0, listwise_prompt(hi_level, n), 0.0)
    usd = float(cost(cheap, pt1, OUT_LISTWISE[cheap]) + cost(strong, pt2, np.where(n > 0, OUT_LISTWISE[strong], 0)).mean())
    return Out(score, usd, pt1 + float(pt2.mean()), OUT_LISTWISE[cheap] + OUT_LISTWISE[strong] * float((n > 0).mean()), 1 + float((n > 0).mean()),
               f"strong_call_frac={(n > 0).mean():.2f} esc_cands={n.mean():.1f}")


def pol_route(w, y, r, rem, item, rng, level, theta=0.25, cheap="mini", strong="flagship", inplay=0.05):
    prior = np.mean(y)
    e1, d1 = llm_evidence(w, y, rem, item, level, cheap, rng)
    p1 = llm_posterior(e1, d1, prior)
    c1 = noisy_conf(w, p1, rng)
    margin = np.where(c1 >= inplay, np.abs(c1 - 0.5), np.inf)        # only candidates in play count
    escalate = margin.min(axis=1) < theta
    e2, d2 = llm_evidence(w, y, rem, item, level, strong, rng)
    p2 = llm_posterior(e2, d2, prior)
    score = np.where(escalate[:, None], p2, p1)
    pt = float(listwise_prompt(level, w.K)); f = float(escalate.mean())
    usd = float(cost(cheap, pt, OUT_LISTWISE[cheap]) + f * cost(strong, pt, OUT_LISTWISE[strong]))
    return Out(score, usd, pt * (1 + f), OUT_LISTWISE[cheap] + f * OUT_LISTWISE[strong], 1 + f, f"escalated={f:.2f}")


def pol_self_consistency(w, y, r, rem, item, rng, level, model, n=5):
    prior = np.mean(y)
    # total inter-sample correlation = rho_models + (1 - rho_models) * a  →  a = (rho_sc - rho_models) / (1 - rho_models)
    a = float(np.clip((w.rho_sc - w.rho_models) / (1 - w.rho_models), 0, 1)) if w.rho_models < 1 else 0.0
    shared = rng.normal(0, 1, y.shape)
    votes = np.zeros(y.shape)
    for _ in range(n):
        e, d = llm_evidence(w, y, rem, item, level, model, rng, shared=shared, a_shared=a)
        votes += llm_posterior(e, d, prior) > 0.5
    pt = float(listwise_prompt(level, w.K)) * n; ct = OUT_LISTWISE[model] * n
    # score = vote share; threshold 0.5 ⇒ majority. (A tuned threshold on vote share is also legitimate.)
    return Out(votes / n, float(cost(model, pt, ct)), pt, ct, float(n))


# ----------------------------------------------------------------------------- metrics
def f1_at(score, y, thr, mask_q=None):
    pred = score > thr
    if mask_q is not None:
        pred, y = pred[mask_q], y[mask_q]
    tp = np.logical_and(pred, y).sum(); fp = np.logical_and(pred, ~y).sum(); fn = np.logical_and(~pred, y).sum()
    p = tp / max(tp + fp, 1); rc = tp / max(tp + fn, 1)
    return 2 * p * rc / max(p + rc, 1e-12), p, rc, float(np.mean(np.all(pred == y, axis=1))) if len(y) else float("nan")


THR_GRID = 1 / (1 + np.exp(-np.linspace(-4.0, 3.0, 29)))   # 0.018 … 0.953


def policy_set(w, y, r, rem, item, rng):
    """All policies for one seed → dict name → Out. Names carry level and model."""
    P = {}
    P[("—", "none", "retriever-only (no LLM)")] = pol_retriever_only(w, y, r, rem, item, rng)
    for level in ("L1", "L5"):
        for model in ("mini", "flagship", "mini-thinking"):
            P[(level, model, "listwise K=30")] = pol_listwise(w, y, r, rem, item, rng, level, model)
            P[(level, model, "listwise K=30 + retriever prior")] = pol_listwise(w, y, r, rem, item, rng, level, model, retriever_prior=True)
            P[(level, model, "listwise K=10")] = pol_listwise(w, y, r, rem, item, rng, level, model, k=10)
            P[(level, model, "pointwise ×30")] = pol_pointwise(w, y, r, rem, item, rng, level, model)
            P[(level, model, "adaptive-K τ=0.05")] = pol_adaptive_k(w, y, r, rem, item, rng, level, model, tau=0.05)
            P[(level, model, "retriever-prune p≥0.02")] = pol_retriever_prune(w, y, r, rem, item, rng, level, model, thr=0.02)
            P[(level, model, "retriever-prune p≥0.02 + retriever prior")] = pol_retriever_prune(w, y, r, rem, item, rng, level, model, thr=0.02, retriever_prior=True)
            P[(level, model, "listwise K=10 + retriever prior")] = pol_listwise(w, y, r, rem, item, rng, level, model, k=10, retriever_prior=True)
            P[(level, model, "self-consistency n=5")] = pol_self_consistency(w, y, r, rem, item, rng, level, model)
        for band in (0.3, 0.4):
            P[(level, "mini+flagship", f"cascade band={band}")] = pol_cascade(w, y, r, rem, item, rng, level, level, band=band)
        P[(level, "mini+flagship", "cascade reject-only p̂<0.05")] = pol_cascade(w, y, r, rem, item, rng, level, level, reject_only=True)
        for theta in (0.25, 0.35):
            P[(level, "mini+flagship", f"route θ={theta}")] = pol_route(w, y, r, rem, item, rng, level, theta=theta)
    # evidence escalation: screen at L5, judge at L1 (reported under L1 because its output competes with L1 designs)
    P[("L1", "mini+flagship", "evidence-cascade L5→L1 band=0.45")] = pol_cascade(w, y, r, rem, item, rng, "L5", "L1", band=0.45)
    P[("L1", "mini+flagship", "evidence-cascade L5→L1 reject-only")] = pol_cascade(w, y, r, rem, item, rng, "L5", "L1", reject_only=True)
    return P


def run_all(w: World, seeds: int, select_frac: float = 0.5):
    """Returns (fixed_df, tuned_df, abstain_df).
    fixed: metrics at threshold 0.5 on every seed.
    tuned: threshold chosen per policy for F1 on the first `select_frac` seeds (pooled), evaluated on the rest."""
    per_seed = []
    for s in range(seeds):
        rng = np.random.default_rng(w.seed * 1000 + s)
        y, r, rem, item = sample_world(w, rng)
        P = policy_set(w, y, r, rem, item, rng)
        per_seed.append((y, rem["flagship"], P))
    n_sel = max(1, int(round(seeds * select_frac))) if seeds > 1 else 1
    sel, ev = per_seed[:n_sel], (per_seed[n_sel:] if seeds > 1 else per_seed)
    keys = list(per_seed[0][2].keys())
    fixed_rows, tuned_rows = [], []
    for key in keys:
        level, model, pol = key
        # fixed threshold on all seeds
        for s, (y, remf, P) in enumerate(per_seed):
            o = P[key]
            f, p, rc, ex = f1_at(o.score, y, 0.5); fe, *_ = f1_at(o.score, y, 0.5, mask_q=~remf)
            fixed_rows.append(dict(level=level, model=model, policy=pol, seed=s, f1=f, precision=p, recall=rc, exact_set=ex, f1_nonmem=fe,
                                   usd_per_query=o.usd, prompt_tokens=o.prompt_tok, completion_tokens=o.completion_tok, calls_per_query=o.calls, extra=o.extra))
        # tuned threshold: select on pooled selection seeds
        ys = np.concatenate([y for y, _, _ in sel]); ss = np.concatenate([P[key].score for _, _, P in sel])
        f1s = [f1_at(ss, ys, t_)[0] for t_ in THR_GRID]
        thr = float(THR_GRID[int(np.argmax(f1s))])
        for s, (y, remf, P) in enumerate(ev):
            o = P[key]
            f, p, rc, ex = f1_at(o.score, y, thr); fe, *_ = f1_at(o.score, y, thr, mask_q=~remf)
            tuned_rows.append(dict(level=level, model=model, policy=pol, seed=s + (n_sel if seeds > 1 else 0), thr=thr, f1=f, precision=p, recall=rc, exact_set=ex, f1_nonmem=fe,
                                   usd_per_query=o.usd, prompt_tokens=o.prompt_tok, completion_tokens=o.completion_tok, calls_per_query=o.calls, extra=o.extra))
    # abstention (fixed threshold; coverage < 1) on listwise K=30, confidence = min noisy margin over candidates in play
    abst_rows = []
    for s, (y, remf, P) in enumerate(per_seed):
        rng = np.random.default_rng(777 + s)
        for level in ("L1", "L5"):
            for model in ("mini", "flagship"):
                o = P[(level, model, "listwise K=30")]
                c = noisy_conf(w, o.score, rng)
                margin = np.where(c >= 0.05, np.abs(c - 0.5), np.inf).min(axis=1) * 2
                margin = np.where(np.isinf(margin), 1.0, margin)
                for tau in (0.0, 0.2, 0.4, 0.6):
                    keep = margin >= tau
                    f, p, rc, ex = f1_at(o.score, y, 0.5, mask_q=keep)
                    abst_rows.append(dict(level=level, model=model, tau=tau, seed=s, coverage=float(keep.mean()), f1=f, precision=p, recall=rc, usd_per_query=o.usd))
    return pd.DataFrame(fixed_rows), pd.DataFrame(tuned_rows), pd.DataFrame(abst_rows)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(["level", "model", "policy"])
    out = g.agg(f1=("f1", "mean"), f1_sd=("f1", "std"), f1_nonmem=("f1_nonmem", "mean"), precision=("precision", "mean"), recall=("recall", "mean"),
                exact_set=("exact_set", "mean"), prompt_tokens=("prompt_tokens", "mean"), completion_tokens=("completion_tokens", "mean"),
                usd_per_query=("usd_per_query", "mean"), calls_per_query=("calls_per_query", "mean"), n_seeds=("seed", "nunique"),
                extra=("extra", "first"), **({"thr": ("thr", "mean")} if "thr" in df else {})).reset_index()
    if "thr" not in out:
        out["thr"] = 0.5
    tq = out["n_seeds"].apply(lambda n: student_t.ppf(0.975, max(n - 1, 1)))
    out["f1_ci95"] = tq * out["f1_sd"].fillna(0) / np.sqrt(out["n_seeds"])
    return out


# ----------------------------------------------------------------------------- figures
MODEL_STYLE = {"mini": ("o", fs.MODEL_COLORS["xj-gpt-4.1-mini"], "GPT-4.1-mini class"), "flagship": ("s", fs.MODEL_COLORS["xj-gpt-4.1"], "flagship class"),
               "mini-thinking": ("^", fs.MODEL_COLORS["xj-gpt-5.4-mini"], "thinking-mini class"), "mini+flagship": ("D", fs.OKABE_ITO["green"], "two-model policies"),
               "none": ("*", "black", "no LLM (retriever only)")}


def short(pol: str) -> str:
    return (pol.replace("listwise ", "LW ").replace("adaptive-K ", "aK ").replace("self-consistency", "SC").replace("retriever-prune ", "prune ")
               .replace(" + retriever prior", "+rp").replace("evidence-cascade L5→L1 ", "evid ").replace("cascade ", "casc ").replace("retriever-only (no LLM)", "retriever only"))


def fig_pareto(summary: pd.DataFrame, level: str, fname: str, title_extra: str):
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.DOUBLE_COL, 3.8))
    d = summary[summary.level == level].copy()
    null = summary[summary.level == "—"].iloc[0]
    ax.axhline(null.f1, color="black", lw=0.9, ls=":")
    ax.annotate(f"no-LLM floor: retriever score alone, $0 (F1 {null.f1:.2f})", (ax.get_xlim()[0], null.f1), xytext=(4, 3), textcoords="offset points", fontsize=6.2, xycoords=("axes fraction", "data"))
    # Pareto frontier among LLM policies
    dd = d.sort_values("usd_per_query"); best = -1; frontier = set(); fx, fy = [], []
    for idx, r in dd.iterrows():
        if r.f1 > best:
            best = r.f1; fx.append(r.usd_per_query * 100); fy.append(r.f1); frontier.add(idx)
    ax.step(fx, fy, where="post", color="black", lw=0.9, alpha=0.5, label="Pareto frontier", zorder=1)
    today = d[(d.policy == "listwise K=30") & (d.model == "flagship")].iloc[0]
    i = 0
    for idx, r in d.iterrows():
        mk, col, _ = MODEL_STYLE[r.model]
        ax.errorbar(r.usd_per_query * 100, r.f1, yerr=r.f1_ci95, fmt=mk, color=col, ms=5, capsize=1.5, lw=0.8, mec="black", mew=0.4, zorder=3)
        label_it = idx in frontier or r.f1 >= today.f1 - 0.005 or r.policy in ("listwise K=30",)
        if label_it and not (r.policy == "listwise K=30" and r.model == "flagship"):
            dy = 4 if i % 2 == 0 else -9; i += 1
            ax.annotate(f"{short(r.policy)} ({'mini' if r.model=='mini' else 'flag' if r.model=='flagship' else 'think' if r.model=='mini-thinking' else '2m'})",
                        (r.usd_per_query * 100, r.f1), xytext=(4, dy), textcoords="offset points", fontsize=5.0, color=col)
    ax.axvline(today.usd_per_query * 100, color="grey", ls="--", lw=0.8)
    ax.scatter([today.usd_per_query * 100], [today.f1], marker="*", s=190, color="gold", edgecolor="black", linewidth=0.6, zorder=5)
    ax.annotate("today's design\n(flagship LW K=30)", (today.usd_per_query * 100, today.f1), xytext=(10, -34), textcoords="offset points", fontsize=6.2, arrowprops=dict(arrowstyle="-", lw=0.5))
    ax.set_xscale("log"); ax.set_xlabel("simulated relay cost per query (US cents, log; token prices from the real ledger)")
    ax.set_ylabel("micro pairwise F1 (synthetic world)")
    for m, (mk, col, lab) in MODEL_STYLE.items():
        if m != "none":
            ax.scatter([], [], marker=mk, color=col, edgecolor="black", linewidth=0.4, label=lab)
    ax.legend(loc="lower right", fontsize=6.3)
    ax.set_title(f"Quality–cost design space at {level} — {title_extra}; labels: frontier and ≥ today's F1", loc="left", fontsize=7.5)
    fs.save(fig, FIG / fname)


def fig_equal_budget(summary: pd.DataFrame, fname: str):
    fs.apply_style()
    fig, axes = plt.subplots(2, 1, figsize=(fs.DOUBLE_COL, 5.4))
    for ax, level in zip(axes, ("L1", "L5")):
        d = summary[(summary.level == level) | (summary.level == "—")].copy()
        ref = d[(d.policy == "listwise K=30") & (d.model == "flagship")].iloc[0]
        d["rel_cost"] = d.usd_per_query / ref.usd_per_query
        d = d[d.rel_cost <= 1.05].sort_values("f1", ascending=False).head(13).sort_values("f1", ascending=True)
        lab = d.model.map(lambda m: MODEL_STYLE[m][2].replace(" class", "").replace("GPT-4.1-mini", "mini").replace("two-model policies", "two-model").replace("no LLM (retriever only)", "")) + " · " + d.policy
        bars = ax.barh(lab, d.f1, xerr=d.f1_ci95, color=[MODEL_STYLE[m][1] for m in d.model], zorder=2, error_kw={"lw": 0.6}, height=0.7)
        for b, rc_, pol, fnm in zip(bars, d.rel_cost, d.policy, d.f1_nonmem):
            ax.annotate(f"{rc_*100:.0f}% of budget · non-mem F1 {fnm:.2f}" + ("  ← today" if pol == "listwise K=30" and rc_ > 0.99 else ""),
                        (b.get_width(), b.get_y() + b.get_height() / 2), xytext=(3, 0), textcoords="offset points", va="center", fontsize=5.6)
        ax.axvline(ref.f1, color="grey", ls="--", lw=0.8)
        ax.set_xlim(max(0, d.f1.min() - 0.08), min(1, d.f1.max() + 0.16))
        ax.tick_params(axis="y", labelsize=6.3)
        ax.set_xlabel("micro pairwise F1 at the policy's tuned threshold (held-out seeds; mean ± 95 % CI)")
        ax.set_title(f"{level}: best policies costing ≤ 105 % of today's design (dashed = its F1 at its own tuned threshold)", loc="left", fontsize=7.5)
        ax.grid(axis="x", linestyle=":", alpha=0.7); ax.grid(axis="y", visible=False)
    fig.tight_layout(h_pad=1.5)
    fs.save(fig, FIG / fname)


def fig_adaptive_k(w: World, fname: str):
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.SINGLE_COL * 1.7, 2.6))
    rng = np.random.default_rng(123)
    for dr, col in zip((1.0, 1.5, 2.0), (fs.OKABE_ITO["vermilion"], fs.OKABE_ITO["blue"], fs.OKABE_ITO["green"])):
        ww = replace(w, retriever_dprime=dr, Q=20000)
        y, r, rem, item = sample_world(ww, rng)
        ks = np.arange(1, 31); rec = [y[:, :k].sum() / y.sum() for k in ks]; toks = [float(listwise_prompt("L1", k)) for k in ks]
        ax.plot(toks, rec, color=col, label=f"retriever d'={dr}")
        for k in (5, 10, 15, 20, 30):
            ax.annotate(f"K={k}", (toks[k - 1], rec[k - 1]), xytext=(3, -8), textcoords="offset points", fontsize=5.5, color=col)
    ax.set_xlabel("prompt tokens per query (L1 calibration)"); ax.set_ylabel("recall of the read prefix\n(relative to recall@30 of the shortlist)")
    ax.set_title("How much of the shortlist is worth reading", loc="left"); ax.legend(fontsize=6.5, loc="lower right")
    fs.save(fig, FIG / fname)


def fig_memory_mixing(w: World, fname: str):
    fs.apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(fs.DOUBLE_COL, 2.7))
    rng = np.random.default_rng(7); levels = ["L1", "L3", "L5", "L6"]
    def ladder(ww, mask=None):
        y, r, rem, item = sample_world(ww, rng); out = []
        for lv in levels:
            o = pol_listwise(ww, y, r, rem, item, rng, lv, "flagship")
            # tuned threshold per rung (matched operating point)
            thr = THR_GRID[int(np.argmax([f1_at(o.score, y, t_)[0] for t_ in THR_GRID]))]
            out.append(f1_at(o.score, y, thr, mask_q=(None if mask is None else mask(rem)))[0])
        return out
    ax = axes[0]
    for pm, col in zip((0.0, 0.3, 0.6), (fs.OKABE_ITO["blue"], fs.OKABE_ITO["orange"], fs.OKABE_ITO["vermilion"])):
        ax.plot(levels, ladder(replace(w, p_mem=pm, Q=6000)), "o-", color=col, label=f"p_mem={pm:.1f}")
    ax.set_ylabel("observed pairwise F1 (tuned thr)"); ax.set_title("(a) Memorised queries flatten the ladder\n(record-keyed memory)", loc="left", fontsize=7.5); ax.legend(fontsize=6.5)
    ax = axes[1]
    ww = replace(w, p_mem=0.3, Q=6000)
    ax.plot(levels, ladder(ww), "o-", color="black", label="all queries")
    ax.plot(levels, ladder(ww, lambda rem: ~rem["flagship"]), "s--", color=fs.OKABE_ITO["blue"], label="non-memorised stratum")
    ax.plot(levels, ladder(ww, lambda rem: rem["flagship"]), "^:", color=fs.OKABE_ITO["vermilion"], label="memorised stratum")
    ax.set_title("(b) Stratify by the probe to un-mix\n(record-keyed)", loc="left", fontsize=7.5); ax.legend(fontsize=6.0, loc="lower left")
    ax = axes[2]
    ww = replace(w, p_mem=0.3, Q=6000, mem_keying="word")
    ax.plot(levels, ladder(ww), "o-", color="black", label="all queries")
    ax.plot(levels, ladder(ww, lambda rem: ~rem["flagship"]), "s--", color=fs.OKABE_ITO["blue"], label="non-memorised stratum")
    ax.plot(levels, ladder(ww, lambda rem: rem["flagship"]), "^:", color=fs.OKABE_ITO["vermilion"], label="memorised stratum")
    ax.set_title("(c) If memory is WORD-keyed, it dies with\nthe title/creator (L5, L6)", loc="left", fontsize=7.5); ax.legend(fontsize=6.0, loc="lower left")
    for a in axes:
        a.set_ylim(0, 1.02)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FIG / fname)


def fig_risk_coverage(abst: pd.DataFrame, fname: str):
    fs.apply_style()
    fig, ax = plt.subplots(figsize=(fs.SINGLE_COL * 1.6, 2.5))
    d = abst[abst.level == "L5"]
    for model, col in (("mini", fs.OKABE_ITO["orange"]), ("flagship", fs.OKABE_ITO["blue"])):
        s = d[d.model == model].groupby("tau").agg(cov=("coverage", "mean"), prec=("precision", "mean"), f1=("f1", "mean")).sort_values("cov")
        name = "mini class" if model == "mini" else "flagship class"
        ax.plot(s["cov"], s["prec"], "o-", color=col, label=f"{name} — precision on answered")
        ax.plot(s["cov"], s["f1"], "s--", color=col, alpha=0.7, label=f"{name} — F1 on answered")
    ax.set_xlabel("coverage (share of queries the agent answers)"); ax.set_ylabel("precision / F1 on answered queries")
    ax.set_title("Abstaining on low-margin queries (L5, threshold 0.5)", loc="left"); ax.legend(fontsize=5.8, loc="lower left")
    fs.save(fig, FIG / fname)


def fig_sweep(sw: pd.DataFrame, fname: str):
    fs.apply_style()
    fig, axes = plt.subplots(1, 3, figsize=(fs.DOUBLE_COL, 3.3), gridspec_kw={"width_ratios": [0.8, 1.05, 1.5]})
    # (a) pointwise vs dilution
    ax = axes[0]
    g = sw.groupby("beta_dilution")["ptw_minus_lw"]
    ax.errorbar(g.mean().index, g.mean().values, yerr=[g.mean().values - g.quantile(0.1).values, g.quantile(0.9).values - g.mean().values], fmt="o-", color=fs.OKABE_ITO["blue"], capsize=3)
    ax.axhline(0, color="grey", lw=0.8); ax.set_xlabel("list-dilution β"); ax.set_ylabel("ΔF1 vs listwise K=30 (flagship)")
    ax.set_title("(a) Pointwise (3.5–5× cost) pays\nonly if long lists dilute", loc="left", fontsize=7.5)
    # (b) fusion / read-less vs retriever–LLM error correlation
    ax = axes[1]
    series = (("rp_minus_lw", "o-", fs.OKABE_ITO["purple"], "LW K=30 + retriever prior (1.0× cost)"), ("k10_rp_minus_lw", "s-", "#C994C7", "LW K=10 + retriever prior (0.47×)"),
              ("k10_minus_lw", "^:", fs.OKABE_ITO["blue"], "LW K=10 (0.47×)"), ("prune_minus_lw", "v:", fs.OKABE_ITO["sky"], "retriever-prune (0.67×)"),
              ("casc04_minus_lw", "D-.", fs.OKABE_ITO["green"], "cascade band 0.4 (0.57×)"))
    for i, (col, mk, c, lab) in enumerate(series):
        gc = sw.groupby("rho_retriever_llm")[col]; m = gc.mean(); lo = gc.quantile(0.1); hi = gc.quantile(0.9)
        x = m.index.values + (i - 2) * 0.02
        ax.errorbar(x, m.values, yerr=[m.values - lo.values, hi.values - m.values], fmt=mk, color=c, capsize=2, label=lab, lw=1, ms=4)
    ax.axhline(0, color="grey", lw=0.8); ax.set_xlabel("retriever–LLM error correlation ρ"); ax.set_ylabel("ΔF1 vs listwise K=30 (flagship)")
    ax.set_title("(b) Fusing the retriever score pays only\nif its errors are not the LLM's errors", loc="left", fontsize=7.5)
    ax.set_xticks([0.0, 0.5, 0.8])
    # (c) best policy at budget, L1, by (rho, beta)
    ax = axes[2]
    l1 = sw[sw.level == "L1"].copy()
    def family(s: str) -> str:
        m, pol = s.split(" · ", 1)
        if "retriever prior" in pol:
            return "fusion: + retriever prior (any K)"
        if pol.startswith(("listwise K=10", "retriever-prune", "adaptive-K")):
            return "read less: K=10 / prune / adaptive-K"
        if pol.startswith(("cascade", "route", "evidence")):
            return "two models: cascade / route"
        if pol == "listwise K=30":
            return "today's design (flagship K=30)"
        if pol.startswith("retriever-only"):
            return "no LLM: retriever only"
        return "other"
    l1["fam"] = l1.best_policy_at_budget.map(family)
    key = l1.beta_dilution.map({0.0: "β0", 0.06: "β.06", 0.12: "β.12"}) + "\nρ" + l1.rho_retriever_llm.map({0.0: "0", 0.5: ".5", 0.8: ".8"})
    ct = pd.crosstab(key, l1.fam, normalize="index") * 100
    ct = ct.reindex([f"{b}\nρ{r}" for r in ("0", ".5", ".8") for b in ("β0", "β.06", "β.12")])
    order = [c for c in ["fusion: + retriever prior (any K)", "read less: K=10 / prune / adaptive-K", "two models: cascade / route", "today's design (flagship K=30)", "no LLM: retriever only", "other"] if c in ct.columns]
    ct = ct[order]
    cols = {"fusion: + retriever prior (any K)": fs.OKABE_ITO["purple"], "read less: K=10 / prune / adaptive-K": fs.OKABE_ITO["blue"], "two models: cascade / route": fs.OKABE_ITO["green"],
            "today's design (flagship K=30)": "lightgrey", "no LLM: retriever only": "black", "other": "white"}
    bottom = np.zeros(len(ct))
    for c in order:
        ax.bar(range(len(ct)), ct[c], bottom=bottom, color=cols[c], label=c, width=0.7, zorder=2, edgecolor="white", linewidth=0.4)
        bottom += ct[c].values
    ax.set_xticks(range(len(ct))); ax.set_xticklabels(ct.index, fontsize=5.6)
    for xpos in (2.5, 5.5):
        ax.axvline(xpos, color="white", lw=2)
    ax.set_ylabel("% of worlds (L1)"); ax.set_title("(c) Best policy at ≤ today's budget, L1,\nby error correlation and dilution", loc="left", fontsize=7.5)
    h1, l1_ = axes[1].get_legend_handles_labels(); h2, l2_ = ax.get_legend_handles_labels()
    fig.legend(h1 + h2, l1_ + l2_, loc="lower center", ncol=4, fontsize=5.6, bbox_to_anchor=(0.5, -0.06), frameon=False)
    fig.tight_layout(w_pad=1.4, rect=[0, 0.14, 1, 1])
    fs.save(fig, FIG / fname)


# ----------------------------------------------------------------------------- sweep
def sweep(base: World, seeds: int = 4) -> pd.DataFrame:
    grid = []
    for p_mem in (0.0, 0.3, 0.6):
        for beta in (0.0, 0.06, 0.12):
            for rd in (1.0, 1.5, 2.0):
                for rrl in (0.0, 0.5, 0.8):
                    for cn in (0.0, 1.0):
                        for bf in (0.67, 1.5):
                            for mk in ("record", "word"):
                                grid.append(dict(p_mem=p_mem, beta_dilution=beta, retriever_dprime=rd, rho_retriever_llm=rrl, conf_noise=cn, belief_factor=bf, mem_keying=mk))
    rows = []
    for i, g in enumerate(grid):
        w = replace(base, Q=1500, **g)
        fixed, tuned, _ = run_all(w, seeds)
        s = summarize(tuned)
        for level in ("L1", "L5"):
            d = s[(s.level == level) | (s.level == "—")]
            ref = d[(d.policy == "listwise K=30") & (d.model == "flagship")].iloc[0]
            # three-way split: thresholds were tuned on seeds 0..n_sel-1 inside run_all; the first held-out seed
            # selects the best policy at budget; the remaining held-out seed(s) evaluate it (winner's-curse free)
            ev_seeds = sorted(tuned.seed.unique())
            sel_seed, ev_rest = ev_seeds[0], ev_seeds[1:]
            t_sel = tuned[(tuned.seed == sel_seed) & ((tuned.level == level) | (tuned.level == "—"))]
            t_ev = tuned[(tuned.seed.isin(ev_rest)) & ((tuned.level == level) | (tuned.level == "—"))]
            ref_cost = ref.usd_per_query
            cand = t_sel[t_sel.usd_per_query <= ref_cost * 1.05].sort_values("f1", ascending=False)
            best = cand.iloc[0]
            ev_best = t_ev[(t_ev.level == best.level) & (t_ev.model == best.model) & (t_ev.policy == best.policy)].f1.mean()
            ev_ref = t_ev[(t_ev.level == level) & (t_ev.model == "flagship") & (t_ev.policy == "listwise K=30")].f1.mean()
            def dlt(model, pol, lev=level):
                return d[(d.level == lev) & (d.model == model) & (d.policy == pol)].f1.iloc[0] - ref.f1
            rows.append({**g, "level": level, "ref_f1": ref.f1, "ref_f1_nonmem": ref.f1_nonmem,
                         "best_policy_at_budget": f"{best.model} · {best.policy}", "best_cost_frac": best.usd_per_query / ref_cost,
                         "gain_heldout": ev_best - ev_ref,
                         "ptw_minus_lw": dlt("flagship", "pointwise ×30"), "sc5_minus_lw": dlt("flagship", "self-consistency n=5"),
                         "ak_minus_lw": dlt("flagship", "adaptive-K τ=0.05"), "prune_minus_lw": dlt("flagship", "retriever-prune p≥0.02"),
                         "rp_minus_lw": dlt("flagship", "listwise K=30 + retriever prior"), "k10_minus_lw": dlt("flagship", "listwise K=10"),
                         "prune_rp_minus_lw": dlt("flagship", "retriever-prune p≥0.02 + retriever prior"), "k10_rp_minus_lw": dlt("flagship", "listwise K=10 + retriever prior"),
                         "mini_rp_minus_lw": dlt("mini", "listwise K=30 + retriever prior"),
                         "casc04_minus_lw": dlt("mini+flagship", "cascade band=0.4"), "retr_only_minus_lw": d[d.level == "—"].f1.iloc[0] - ref.f1,
                         "casc04_cost_frac": d[(d.level == level) & (d.policy == "cascade band=0.4")].usd_per_query.iloc[0] / ref_cost,
                         "ak_cost_frac": d[(d.level == level) & (d.model == "flagship") & (d.policy == "adaptive-K τ=0.05")].usd_per_query.iloc[0] / ref_cost,
                         "prune_cost_frac": d[(d.level == level) & (d.model == "flagship") & (d.policy == "retriever-prune p≥0.02")].usd_per_query.iloc[0] / ref_cost})
        if (i + 1) % 72 == 0:
            print(f"  sweep {i+1}/{len(grid)}", flush=True)
    return pd.DataFrame(rows)


def sweep_log(sw: pd.DataFrame, elapsed: float | None = None) -> list[str]:
    def q(col):
        return f"median {sw[col].median():+.3f}, 10–90 % [{sw[col].quantile(0.1):+.3f}, {sw[col].quantile(0.9):+.3f}]"
    return [f"## Sensitivity sweep ({len(sw)//2} worlds × 2 levels; 4 seeds: thresholds on seeds 0–1, policy selection on seed 2, evaluation on seed 3)", "",
            f"- elapsed: {elapsed:.1f} s" if elapsed is not None else "- (log regenerated from sensitivity_sweep.csv)",
            f"- share of worlds where the policy selected at ≤105 % of today's budget beats today's design by > 0.02 F1 on the held-out seed: L1 {np.mean(sw[sw.level=='L1'].gain_heldout>0.02):.0%}, L5 {np.mean(sw[sw.level=='L5'].gain_heldout>0.02):.0%} (mean held-out gain {sw[sw.level=='L1'].gain_heldout.mean():+.3f} / {sw[sw.level=='L5'].gain_heldout.mean():+.3f})",
            f"- listwise + retriever prior − listwise (flagship, same cost): {q('rp_minus_lw')}",
            f"- retriever-prune − listwise (flagship): {q('prune_minus_lw')} at median {sw.prune_cost_frac.median():.0%} of cost",
            f"- retriever-prune + retriever prior − listwise (flagship): {q('prune_rp_minus_lw')} at median {sw.prune_cost_frac.median():.0%} of cost",
            f"- K=10 + retriever prior − listwise K=30 (flagship): {q('k10_rp_minus_lw')} at ≈ 47 % of cost",
            f"- MINI listwise + retriever prior − FLAGSHIP listwise (≈ 20 % of cost): {q('mini_rp_minus_lw')}",
            f"- adaptive-K − listwise (flagship): {q('ak_minus_lw')} at median {sw.ak_cost_frac.median():.0%} of cost",
            f"- K=10 − K=30 (flagship): {q('k10_minus_lw')}",
            f"- cascade band 0.4 − listwise (flagship): {q('casc04_minus_lw')} at median {sw.casc04_cost_frac.median():.0%} of cost",
            f"- pointwise − listwise (flagship): {q('ptw_minus_lw')} at 3.5–5× cost",
            f"- self-consistency n=5 − single (flagship): {q('sc5_minus_lw')} at 5× cost",
            f"- retriever-only (no LLM) − flagship listwise: {q('retr_only_minus_lw')}",
            "", "Best policy at budget (selected on seed 2), by world:", "", sw.groupby(["level", "best_policy_at_budget"]).size().to_string(), "",
            "By assumption — mean held-out gain of the selected policy, and the fusion gain (LW+prior − LW, flagship):", "",
            sw.groupby(["level", "rho_retriever_llm", "mem_keying"])[["gain_heldout", "rp_minus_lw", "prune_minus_lw", "k10_minus_lw"]].mean().round(3).to_string(), "",
            "Fusion gain by retriever strength and error correlation:", "", sw.groupby(["retriever_dprime", "rho_retriever_llm"]).rp_minus_lw.mean().round(3).unstack().to_string(), "",
            "Share of worlds where the retriever alone (no LLM) beats the flagship listwise K=30, by level: " + ", ".join(f"{lv} {np.mean(sw[sw.level==lv].retr_only_minus_lw>0):.0%}" for lv in ("L1", "L5")), ""]


def table_md(d: pd.DataFrame) -> list[str]:
    out = ["| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |", "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |"]
    for _, r in d.sort_values("usd_per_query").iterrows():
        out.append(f"| {r.level} | {r.model} | {r.policy} | {r.thr:.2f} | {r.f1:.3f} ± {r.f1_ci95:.3f} | {r.f1_nonmem:.3f} | {r.precision:.3f} | {r.recall:.3f} | {r.exact_set:.3f} | {r.usd_per_query*100:.2f} | {r.calls_per_query:.2f} | {r.extra} |")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--Q", type=int, default=3000)
    ap.add_argument("--seeds", type=int, default=8)
    ap.add_argument("--sweep", action="store_true")
    ap.add_argument("--plot-sweep-only", action="store_true")
    args = ap.parse_args()
    RES.mkdir(parents=True, exist_ok=True); FIG.mkdir(parents=True, exist_ok=True)
    if args.plot_sweep_only:
        sw = pd.read_csv(RES / "sensitivity_sweep.csv")
        fig_sweep(sw, "S8_sweep_sensitivity")
        base = (RES / "RUNLOG_base.md").read_text(encoding="utf-8") if (RES / "RUNLOG_base.md").exists() else ""
        (RES / "RUNLOG.md").write_text(base + "\n" + "\n".join(sweep_log(sw)), encoding="utf-8")
        print("sweep figure and RUNLOG regenerated from CSV"); return
    t0 = time.time()
    w = World(Q=args.Q)
    fixed, tuned, abst = run_all(w, args.seeds)
    fixed.to_csv(RES / "policies_fixed_thr_raw.csv", index=False); tuned.to_csv(RES / "policies_tuned_thr_raw.csv", index=False); abst.to_csv(RES / "abstention_raw.csv", index=False)
    sf, st = summarize(fixed), summarize(tuned)
    sf.to_csv(RES / "policies_summary_fixed_thr.csv", index=False); st.to_csv(RES / "policies_summary.csv", index=False)
    fig_pareto(st, "L1", "S1_pareto_L1", "tuned thresholds, held-out seeds")
    fig_pareto(st, "L5", "S2_pareto_L5", "tuned thresholds, held-out seeds")
    fig_equal_budget(st, "S3_equal_budget")
    fig_adaptive_k(w, "S4_adaptive_k_recall_ceiling")
    fig_memory_mixing(w, "S5_memory_mixing")
    fig_risk_coverage(abst, "S6_risk_coverage")
    log = ["# Simulation run log (v2 — matched operating points)", "", f"- started: {time.strftime('%Y-%m-%d %H:%M:%S %Z')}",
           f"- world: `{json.dumps(asdict(w))}`", f"- seeds: {args.seeds} (threshold selected on the first {max(1, args.seeds // 2)}, metrics on the remaining held-out seeds); queries per seed: {args.Q}",
           f"- elapsed: {time.time()-t0:.1f} s", "",
           "## Headline tables — each policy at its own F1-optimal threshold (chosen on selection seeds), evaluated on held-out seeds", "",
           "F1 = micro pairwise F1 over (query, candidate) decisions; 'F1 non-mem' = same on the queries the flagship does NOT remember.", ""]
    for level in ("L1", "L5"):
        log += [f"### {level}", ""] + table_md(st[(st.level == level) | (st.level == "—")]) + [""]
    log += ["## Same policies at a fixed threshold of 0.5 (the v1 comparison; different operating points — for reference only)", ""]
    for level in ("L1", "L5"):
        log += [f"### {level}", ""] + table_md(sf[(sf.level == level) | (sf.level == "—")]) + [""]
    if args.sweep:
        t1 = time.time(); print("sweep…", flush=True)
        sw = sweep(w, seeds=4); sw.to_csv(RES / "sensitivity_sweep.csv", index=False)
        fig_sweep(sw, "S8_sweep_sensitivity")
        log += sweep_log(sw, time.time() - t1)
    (RES / ("RUNLOG.md" if args.sweep else "RUNLOG_base.md")).write_text("\n".join(log), encoding="utf-8")
    print("\n".join(log[:60]))


if __name__ == "__main__":
    main()
