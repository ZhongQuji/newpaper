# sim/ — calibrated design-space and measurement simulations (v2)

Three scripts, pure NumPy/SciPy/pandas, each writes a run log. **v2** of `reunion_sim.py` implements the
red-team code review (`docs/reviews/redteam_sim_code_review.md`); the v1 verdicts it replaced are
listed at the end so the correction is visible.

| script | question | outputs |
| --- | --- | --- |
| `reunion_sim.py` | At matched operating points and identical token accounting, which budget-allocation policy for the shortlist agent is best, and on which assumptions does the answer hinge? | `results/policies_summary.csv` (tuned thresholds, held-out seeds), `results/policies_summary_fixed_thr.csv`, `results/sensitivity_sweep.csv`, `results/RUNLOG.md`, `figures/sim/S1–S6, S8` |
| `power_analysis.py` | With 80 dev / 294 test queries, how big must a level-to-level drop be before it is statistically real? | `results/power_curves.csv`, `results/POWER.md`, `figures/sim/S7` |
| `measurement_sim.py` | Evaluation unit (S9), forking paths of a post-hoc rule (S10), position bias and the shuffled-order control (S11) | `results/MEASUREMENT.md`, `results/s9–s11_*.csv`, `figures/sim/S9–S11` |

```bash
python3 sim/reunion_sim.py                 # base world: 3,000 queries × 8 seeds (thresholds on 4, metrics on 4), ~10 s
python3 sim/reunion_sim.py --sweep         # + 648-world grid, 4 seeds each (thresholds 0–1 · select 2 · evaluate 3), ~10 min
python3 sim/measurement_sim.py             # ~1 min
python3 sim/power_analysis.py              # ~5 min
```

## What is real, what is synthetic

**Real (from `data/real/runs.csv`):** prompt tokens per 30-candidate call at each level, fitted to
`prompt = 128 + (K+1)·r_level` with r = 59 (L1), 53 (L3), 35 (L5), 30 (L6) tokens per record — a model
that also reproduces the measured pointwise call (128 + 2r = 246 tokens at L1, run E10e); completion
tokens per call (≈70 non-thinking, ≈500 thinking-class listwise; 1 vs ≈300 for score-only pointwise);
effective relay prices by least squares on 55 text-only runs (≤5.6 % error): GPT-4.1 mini $1.71/$8.10
per M prompt/completion, GPT-4.1 $8.88/$36.2, GPT-5.4 $7.92/$47.9, GPT-5.4 mini $3.29/$20.3.

**Synthetic (assumed):** number of members per query P(m=0..5) = .15/.35/.25/.13/.08/.04; first-stage
retriever separation d'_r; the LLM's evidence discriminability per level (L1 2.4 · L3 2.0 · L5 1.3 ·
L6 1.0) × model class (mini .75, flagship 1.0, thinking-mini .9); memorisation as a nested set of
"famous" queries (flagship share p_mem, mini 0.6·p_mem, thinking-mini 0.8·p_mem) with sharper evidence
(d'_mem 4.0 / 3.0 / 3.5), **record-keyed** (fires at every rung) or **word-keyed** (fires only where
title/creator are shown); list dilution β (d' loss per log₂(K/8)); evidence-noise correlation between
models ρ_models = .5; **retriever–LLM error correlation ρ** (share of the retriever's noise that is the
same item difficulty the LLM sees); confidence noise for the controller; believed vs true retriever d'.

**Swept** (648 worlds): p_mem {0, .3, .6} × β {0, .06, .12} × d'_r {1, 1.5, 2} × ρ {0, .5, .8} ×
conf_noise {0, 1} × belief {×0.67, ×1.5} × keying {record, word}. **Fixed** (not swept — say so):
member distribution, d'_mem, per-level d' values, model-class multipliers, ρ_models, pointwise jitter
.35, the 128-token overhead, base accuracy and λ in the power model.

**Therefore:** absolute F1 values mean nothing for the real system. What transfers is the *decision
table* below and the list of cheap real experiments that fill it in — not the verdicts.

## How policies are compared (the v1 mistake, fixed)

v1 scored every policy at a fixed posterior threshold of 0.5 under a 5.8 % prior — a different operating
point for each policy, and one at which the L5 evidence channel was dead on the non-memorised stratum
(F1 0.06). v2 tunes each policy's threshold for F1 on selection seeds and evaluates on held-out seeds;
the sweep adds a third split (select the winning policy on one held-out seed, evaluate it on another) so
that "beats today's design" is not a winner's-curse statistic. CIs use the t quantile for the number of
seeds. Every headline is also reported on the non-memorised stratum.

## Policies

| policy | idea | real-world requirement |
| --- | --- | --- |
| retriever-only | no LLM call; threshold the calibrated retriever score | retriever scores — the **no-intervention null**, first row of every table |
| listwise K=30 | one call, whole shortlist | today's E10 agent |
| **listwise + retriever prior** | same call; the LLM's per-candidate P(member) is combined with a per-candidate prior from the calibrated retriever score instead of a flat prevalence prior | a per-candidate score from the LLM (logprob P(yes) or verbalised score) + a calibrated retriever |
| listwise K=10 / adaptive-K / retriever-prune | read fewer candidates (fixed prefix / posterior-tail rule / score threshold at any position) | `--k 10`; calibrated retriever scores for the other two |
| … + retriever prior | the two above combined | both of the above |
| pointwise ×30 | one call per candidate | E10e |
| cascade (band / reject-only) | mini judges all; flagship re-judges the uncertain band (or all non-rejected) | a per-candidate score from the mini |
| evidence-cascade L5→L1 | mini screens at the austere rung, flagship judges survivors at the full rung | as above; see docs/04 §1 for why this is a *system* option only |
| route | mini answers; whole query escalates on low in-play margin | as above |
| self-consistency n=5 | 5 correlated samples, vote share as score | `--replicate` ×5 (not on GPT-5: no temperature) |
| abstain | answer only when the least-confident in-play decision is confident (threshold 0.5 regime) | selective prediction |

## Findings (base world has ρ = 0 and record-keyed memory; the sweep qualifies every line)

1. **The zero-cost no-LLM null is not trivial.** Retriever score alone: F1 0.39. At L5 it beats the
   flagship's listwise K=30 in **51 % of swept worlds** (whenever d'_r ≥ 1.5 and the LLM's L5 evidence is
   weak). The first thing to establish on the real data is that the LLM beats the retriever at all at L5.
2. **Fusing the retriever score into the LLM decision is the largest gain — when the two see different
   things.** Base world (ρ = 0): flagship +0.09 F1 at L1, +0.16 at L5, at identical cost; the mini with the
   prior (0.63) nearly matches today's flagship (0.67) at a fifth of the price. Sweep: median +0.046
   (10–90 % −0.04 … +0.21). At ρ = 0.5 the L1 gain vanishes (−0.004) and at ρ = 0.8 it turns negative
   (−0.026) unless the retriever is strong (d'_r = 2: +0.09 even at ρ = 0.8); at L5 it stays positive at
   every ρ (Fig. S8b). *Real test:* fit the fused decision on dev from logged P(yes) and retriever scores — $0.
3. **"Read less" is a smaller, more robust gain.** K=10: median +0.045 (−0.06 … +0.15) at 47 % of cost;
   retriever-prune: +0.024 (−0.01 … +0.12) at 67 %; adaptive-K: +0.017 (−0.00 … +0.11) at 80 %. They lose
   only when β = 0 *and* the retriever is weak or mis-calibrated. *Real test:* `--k 10` vs `--k 30`, $1.
4. **Two models beat one only in one corner.** The reject-only cascade is the best choice at budget in
   158/648 L1 worlds — essentially those with ρ > 0 *and* β > 0 (Fig. S8c); the same-level band cascade is
   below today's design on median (−0.015). v1's "cascade wins 170/432" was an artefact of the fixed
   threshold.
5. **Today's design is already the best choice in 15 % of L1 worlds** — exactly those with correlated
   errors (ρ > 0) and no dilution (β = 0). If the two $0–$1 real tests come back null, keep it.
6. **Pointwise is a bet on dilution** (+0.10 at β = 0.12, −0.01 at β = 0) at 3.5–5× cost; self-consistency
   n = 5 gains +0.07 on median at 5× cost but is dominated by the fusion policies at a fifth of the price.
7. **Memory keying decides whether L5 is a clean rung.** Record-keyed memory keeps the memorised stratum
   flat to L6 (Fig. S5b); word-keyed memory collapses it at L5 (Fig. S5c), making L5/L6 clean even for
   famous objects. One E8 arm with L5-only evidence tells them apart (docs/04 §2.2).
8. **Abstention buys precision cheaply** (0.87 → 0.92 at 80 % coverage, L5, flagship; Fig. S6).
9. **Power** (`POWER.md`): dev n = 80 detects only ≥ 15–18-point level drops at 80 % power; test n = 294
   ≥ 7–9; absolute accuracies carry ±0.10 / ±0.055 CIs. Note the review's caveat: the simulated ICC is
   latent-scale (outcome ICC ≈ 0.09 with mean cluster 1.9), so the "bootstrap over ensembles" advice
   rests on S9 more than on S7.
10. **Measurement** (`MEASUREMENT.md`): the same two systems get opposite verdicts from micro pair F1 vs
    per-ensemble macro F1 / B³ / exact-set (S9); query-level bootstrap CIs are ~35 % too narrow; naive
    transitive closure collapses at ~2 % pairwise FPR under dense candidate reuse; a best-of-k post-hoc
    rule inflates F1 by ≤ 1.8 points at n = 80 (≤ 3.2 exact-set) — disclosure, not magnitude (S10);
    ordered shortlists flatter a primacy-biased selector by up to 13 F1 points (S11).

## The decision table (what to measure on the real system, in order)

| measure (cost) | if … | then the simulation says … |
| --- | --- | --- |
| fused decision on dev from logged scores ($0) | fusion ≥ +0.03 over the LLM alone | adopt the retriever prior (M1); it dominates everything else at equal cost |
| `--k 10` vs `--k 30` ($1) | K=10 ≥ K=30 on the top-10 (β > 0) | read less (K=10 / prune); consider the reject-only cascade if fusion was null |
| both null | — | today's design is the right one; spend on the measurement, not the system |
| retriever-only vs LLM at L5 ($0 once scores exist) | retriever ≥ LLM | the LLM adds nothing at the austere rung — a result in itself |

## What v1 said that v2 withdraws

"Cascade mini→flagship wins 170/432 cells"; "today's design is the best choice in 17/432"; "87 %/95 % of
worlds have a better policy at budget"; "evidence escalation at 49–64 % of cost"; "ρ_sc = 0.5" (it was
0.75); "pointwise costs 3.5×" (3.5× at L1, 5.2× at L5). All were consequences of the fixed-threshold
comparison, oracle confidence, or a cost model bug identified by the red-team review.
