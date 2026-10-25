# sim/ — calibrated design-space simulations

Two scripts, both pure NumPy/SciPy, both finish in minutes on a laptop, both write a run log.

| script | question | outputs |
| --- | --- | --- |
| `reunion_sim.py` | Under *identical* token accounting, which budget-allocation policy for the shortlist agent is best, and what does the answer depend on? | `results/policies_summary.csv`, `results/sensitivity_sweep.csv`, `results/RUNLOG.md`, `figures/sim/S1–S6, S8` |
| `power_analysis.py` | With 80 dev / 294 test queries, how big must a level-to-level drop be before it is statistically real? | `results/power_curves.csv`, `results/POWER.md`, `figures/sim/S7` |

```bash
python3 sim/reunion_sim.py                 # base world, 3,000 queries × 8 seeds, ~10 s
python3 sim/reunion_sim.py --sweep         # + 216-world sensitivity grid, ~1 min
python3 sim/power_analysis.py              # ~5 min (bootstrap)
```

## What is real, what is synthetic

**Real (copied from `data/real/runs.csv`):** prompt tokens per 30-candidate call at each level
(L1 1,959 · L3 1,784 · L5 1,208 · L6 1,064); completion tokens per call (≈70 non-thinking, ≈500
thinking-class); effective relay prices fitted by least squares on 55 text-only runs (max error
5.6 %): GPT-4.1 mini $1.71/$8.10 per M prompt/completion, GPT-4.1 $8.88/$36.2, GPT-5.4
$7.92/$47.9, GPT-5.4 mini $3.29/$20.3; pointwise cost structure (≈240 prompt tokens per
single-candidate call, from E10e's 7.2 k tokens/query).

**Synthetic (assumed, and every one swept):** number of true members per query
(P(m=0..5) = .15/.35/.25/.13/.08/.04), first-stage retriever separation d'_r ∈ {1, 1.5, 2},
LLM evidence discriminability per level (L1 2.4 · L3 2.0 · L5 1.3 · L6 1.0) × model-class
multiplier (mini .6–.9, flagship 1.0, thinking-mini .9), share of memorised queries
p_mem ∈ {0, .3, .6}, list dilution β ∈ {0, .06, .12} (d' loss per log₂(K/8)), evidence-noise
correlation between two models ρ_models ∈ {.3, .7}, LLM over-confidence ∈ {1.0, 1.4},
self-consistency sample correlation ρ_sc = .5, pointwise threshold jitter .35.

**Therefore:** absolute F1 values here mean nothing for the real system. What transfers is
(i) the *ordering* of policies at equal budget, (ii) the *shape* of trade-off curves,
(iii) *which assumption* each verdict hinges on — and that last item is a list of cheap real
experiments to run.

## Policies compared (all with the same decision rule: predict "member" iff posterior > 0.5)

| policy | idea | real-world analogue |
| --- | --- | --- |
| listwise K=30 | one call, whole shortlist | today's E10 agent |
| listwise K=10 | one call, top-10 only | `--k 10` |
| pointwise ×30 | 30 single-candidate calls | E10e |
| adaptive-K τ | before calling, read only as many shortlist positions as the retriever posterior says are worth reading (expected unread members < τ) | retriever-score gap rule; zero extra calls |
| cascade mini→flagship (band) | cheap model judges all 30; only candidates with posterior within ±band of 0.5 go to the flagship in one short call | two-model pipeline |
| route mini→flagship (θ) | cheap model answers; whole query escalates if its least-confident decision has margin < θ | need-based budget per query |
| self-consistency n=5 | 5 correlated samples, majority vote | `--replicate` ×5 |
| abstain if min-margin < τ | answer only when every decision is confident | selective prediction |

## Headline findings (base world; `results/RUNLOG.md` has the full tables)

1. **Today's design is rarely on the frontier.** In 86 % (L1) / 97 % (L5) of the 216 worlds some
   policy beats flagship-listwise-K=30 at ≤ 105 % of its cost. Mean gain of the best such policy ≈ +0.05 F1 at ≈ 60–75 % of
   the cost.
2. **The cheapest improvement is to read less.** Adaptive-K (τ = 0.05) costs 70–90 % of K=30 and
   never loses more than 0.01 F1; with a good retriever (d' = 2) it *gains* +0.04 while costing
   70 %. Plain K=10 is the best single-model policy in 74/432 cells.
3. **Two models beat one.** The mini→flagship cascade with band 0.4 is the most frequent
   equal-budget winner (192/432 cells), typically at 55–70 % of the flagship's cost. It stays the
   winner when model errors are correlated (ρ = 0.7) and when models are over-confident (×1.4),
   but its margin shrinks; it is *not* the winner when there is no list dilution (β = 0) — then
   flagship adaptive-K / K=10 win.
4. **Pointwise is a bet on dilution.** Its +0.06 median gain over listwise exists only if long
   lists degrade the model (β > 0); at β = 0 it is −0.00 ± 0.01 while costing 3.5×. The real
   system can measure β directly: run listwise with `--k 10` vs `--k 30` on the same queries.
5. **Self-consistency is poor value here.** n = 5 costs 5× and gains a median +0.009 F1
   (range −0.03 … +0.04); buy a better model or a cascade instead.
6. **Memorised queries flatten the ladder.** With p_mem = 0.3 the observed L1→L6 drop is roughly
   half the evidence-only drop (Fig. S5). The forced-choice probe should be used to stratify every
   ladder plot into memorised / non-memorised queries, not reported as a separate number.
7. **Abstention buys precision cheaply.** Refusing the 20 % least-confident queries lifts
   precision from 0.87 to 0.92 (L5, flagship) with no extra calls (Fig. S6) — relevant because a
   false "reunion" is costlier to a curator than a miss.
8. **Power.** Dev (n = 80) detects only ≥ 15–18-point level drops at 80 % power; test (n = 294)
   ≥ 7–9 points; absolute accuracies carry ±0.10 (dev) / ±0.055 (test) CIs. Ladder claims belong on
   the test split, with ensemble-level bootstrap.
