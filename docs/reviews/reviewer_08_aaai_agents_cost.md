# Reviewer 08 — AAAI/ICML persona (LLM agents, test-time compute, cost-efficiency)

## Summary of the submission as I understand it
The project asks whether LLM/MLLM "agents" can reassemble dispersed museum ensembles from catalogue evidence, using an information-level ladder (L1 → L6) to separate evidence use from memorisation. The headline method E10 is one listwise call per query over a 30-candidate shortlist; agentic variants are a deep-research harness over a closed pool (E15, ≤ 30 steps) and an open pool (E17, ≤ 14 steps), plus a pointwise reranker (E10e) and a replayed MLLM visual gate (E10c). The ledger covers GPT-4.1, GPT-4.1-mini, GPT-5.4 and GPT-5.4-mini: 9,178 calls, 16.6 M tokens, $100.07, 17.7 h. With no accuracy numbers available, I review compute allocation, fairness of the comparisons, and what would justify the agentic spend.

## Scores (1–10) with one-line justification each
- Novelty: 5 — the ladder is good design; "single call vs. tool loop" is a known axis and no adaptive-compute mechanism is proposed.
- Technical soundness: 5 — the single-call method is sound; harness comparisons are not compute-matched and GPT-5.4 costs are "price estimated".
- Evaluation rigour: 4 — E17 has n=20 and E15 n=40 dev queries on one model each; no accuracy-vs-cost curves, CIs, or abstention handling.
- Clarity (of the design, as reconstructed): 6 — ledger and flags are exemplary; calling a single call an "agent" obscures what ran.
- Impact / significance: 5 — the reasoning-tax finding is useful; the agentic experiments as designed cannot settle whether extra compute pays.
- Overall: 5 — borderline; fixable with the compute-matched runs below.

## Strengths
- A complete per-call ledger (tokens, cost, wall time, served model, cache hits, rc) — rare and auditable.
- The reasoning tax is quantified cleanly: GPT-5.4-mini emits 475–766 completion tok/call vs 55–90 for GPT-4.1 / GPT-5.4; its cost/call ($0.016–0.023) equals the flagships' ($0.013–0.024) and is 4–6× GPT-4.1-mini's ($0.0025–0.0048).
- Replicate and prompt-variant runs at L1 (`_rep1`, `_v1`, `_v2`) give a variance estimate for free.
- The expensive branches (E15/E17) were kept small — responsible budgeting, if underpowered.

## Weaknesses
1. **BLOCKER** — Agentic baselines are neither compute-matched nor powered. E17: 20 queries, 10.6 steps/query (cap 14), 25k tokens, $0.22/query, 2 API errors in 211 records; E15: 40 queries, 7.4 steps/query (cap 30), 8.3k tokens, $0.016/query; comparator E10 L1: $0.004–0.020/query. With n=20 a 95 % CI is ≈ ±20 points, so an 11× spend can be neither justified nor refuted. E17 ran on GPT-5.4 and E15 on GPT-4.1-mini, confounding harness and model.
2. **MAJOR** — The reasoning tax is observed, not controlled. GPT-5.4-mini ran only at `reasoning_effort low`; its completion tokens grow as evidence shrinks (L1 475 → L3 617 → L3-H 660 → L5 694; completion/prompt ratio 0.24 → 0.58), so roughly 60–78 % of its cost is hidden reasoning. No effort sweep, no accuracy-per-token comparison.
3. **MAJOR** — No cost-adaptive mechanism in 65 runs: no cascade, early exit, adaptive K, routing by level, or abstention. Every run is single-model, fixed K=30, fixed level — the central omission for a paper about agents and cost.
4. **MAJOR** — The natural compute-matched test was not run: one GPT-4.1 call ($0.0200) buys 4.8 GPT-4.1-mini calls ($0.0042), so self-consistency n=5 on the mini is cost-equal to one flagship call, with GPT-5.4-mini ($0.016) in between.
5. **MAJOR** — Cost and latency accounting. GPT-5.4 prices are "estimated"; relay rates back out to ≈ $8.7 / $38 per M tokens for GPT-4.1 (≈ 4× list), so only ratios transfer. Wall time is relay-confounded: GPT-5.4-mini test rows at L3-H/L5 show 14–15 s/call vs 6.6 s at L1; GPT-5.4 L6 dev shows 20 s/call; E10e's 79 s/query is 29 sequential 2.7 s requests.
6. **MINOR** — "Agent" is a misnomer for E10: calls = queries (80 / 294), one usage record per call, no tool use. E6 `t1_rerank` and E10 are both single listwise calls over K=30; state the difference.
7. **MINOR** — Visual-gate replay (E10c): 229 image calls scored once on the GPT-4.1-mini L1/L3/L5 runs, then replayed. Sound only if the gate is a pure function of (query image, candidate image) and pair coverage of the replayed runs is complete; neither is documented, and tuning the threshold on the same runs is circular.

## Experiments or artefacts that would change my score
1. Accuracy-vs-cost curve with bootstrap CIs, one point per (method, model, level), tokens on the x-axis, dollars secondary with the price table printed. *Convince me:* the headline configuration is Pareto-optimal and GPT-5.4-mini is either strictly better than GPT-5.4 or dropped.
2. Compute-matched test on the 294-query split at L1 and L5: GPT-4.1-mini × 5 (candidate-level majority vote, order shuffled per sample) vs GPT-4.1 × 1 vs GPT-5.4-mini × 1 at ≈ $0.02/query (≈ $17 per level). *Convince me:* a gap whose CI excludes zero.
3. Reasoning-effort sweep at L5 dev: GPT-5.4-mini low/medium/high plus GPT-5.4 at low ($1.5–4 per cell). *Convince me:* accuracy rises with completion tokens; if flat, report the tax as waste.
4. Harness at matched n and model: E15 and E17 on the same 80 dev queries with GPT-4.1-mini and GPT-5.4, with step-count distribution and % hitting the cap. *Convince me:* ≥ 10 F1 points over the single call at ≥ 5× cost, or the harness leaves the headline.
5. One cascade (idea below) with realised cost per query. *Convince me:* ≥ 90 % of flagship accuracy at ≤ 40 % of its cost.
6. Per-query Jaccard between `E10_agent_L1_dev` and `_rep1`, and between `_v1` and `_v2`. *Convince me:* if agreement > 0.9, say so and skip self-consistency; if < 0.7, item 2 is mandatory.
7. Visual-gate replay audit: pair coverage %, gate-only accuracy, threshold fixed on a split not used for replay.
8. Abstention: share of queries whose gold set within the shortlist is empty and how the agent is scored on them.

## Token-efficiency / cost critique
- Wasteful: GPT-5.4-mini is 33 % of the budget ($33.19) and at L5 costs more per call ($0.018) than GPT-5.4 ($0.0127) while emitting 11× its visible completion tokens. Unless it wins by a wide margin it is the dominated point.
- Wasteful: E17 — $4.40 for 20 queries; the full test split for one model at one level would cost ≈ $65, infeasible within this project's $100 — itself a result worth stating.
- Wasteful: E10e re-sends the query 29 times (135/2,344 cache hits); caching or setwise batching cuts it 3–5×. E16 ($12.4, 12 % of budget) re-scores a 2B model's top-8 on 80 dev queries only.
- Cheap-and-missing: self-consistency n=5 with GPT-4.1-mini on dev ($1.7/level); GPT-5.4-mini's completion-token count, which rises with uncertainty, as a free escalation/abstention signal; shuffled-order replicates; adaptive K (prompt tokens ≈ linear in K; K=10 roughly halves L1 cost).
- Test-time scaling estimate (test split, L1): SC n=5 costs $6.3 (GPT-4.1-mini), $30 (GPT-4.1), $25 (GPT-5.4-mini); a pointwise P(yes) verifier over the selected candidates adds ≈ $0.002/query ($0.00042/request). Payoff is likely small: listwise errors are mostly systematic (hard negatives, gold missing from the shortlist), not sampling noise, and the GPT-5 family rejects temperature, so diversity must come from order shuffles. Worth running only for the mini model, where it is cost-neutral against the flagship.

## One idea the authors have not tried
Budget-aware cascade with disagreement routing. Stage 1: GPT-4.1-mini listwise with two shuffled candidate orders (2 × $0.0042); if the selections agree (Jaccard = 1) and are non-empty, stop. Stage 2 (disagreement or empty set): GPT-5.4 listwise over the stage-1 union ∪ shortlist top-10 (K ≈ 10–14, ≈ $0.01). Stage 3 (still conflicting): pointwise P(yes) on the disputed candidates only (≈ $0.0004 each), dev-tuned threshold; nothing above threshold = abstain. Expected realised cost ≈ $0.006–0.012/query vs $0.020 for the flagship alone, with order bias averaged out at stage 1 and a principled abstention output. Report an accuracy-vs-realised-cost curve by sweeping the stage-1 agreement rule (Jaccard = 1, ≥ 0.5, any overlap).

## Confidence (1–5) and what I could not assess
Confidence 4 on the cost/compute analysis (every number is from `runs.csv` or `runs_summary.md`), 2 on the task side. Not assessable: any accuracy, the relay price table, harness tool definitions and step logs, the `e10_regate` rule, non-OpenAI ledgers, and whether the 10-25 L5-P test restart succeeded (`E10_agent_L5P_test`, rc=1, 4 API errors on 10-24).
