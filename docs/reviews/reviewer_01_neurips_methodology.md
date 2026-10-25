# Reviewer 01 — NeurIPS Datasets & Benchmarks (senior reviewer, statistical methodology)

## Summary of the submission as I understand it
The submission proposes a benchmark and an LLM "reunion agent" for re-assembling dispersed cultural-heritage ensembles: given one catalogue record and a K=30 shortlist, the model selects the candidates that belong to the same ensemble. The central manipulation is an information ladder (L1 → L2-T → L3 → L3-H → L5 → L5-P → L6) that strips fields so evidence use can be separated from memorised associations, supported by a closed-book probe (E5), a counterfactual forced choice (E8v4) and shortlist-shortcut controls. Splits are 80 dev / 294 test queries (L2-T subset 32 / 91); about ten models are compared; every E10 run is post-processed by `e10_regate.py`. I have the run ledger (`runs.csv`, 65 runs, 9,178 calls, $100.07) but no accuracy numbers, so every judgement below is conditional on the results tables.

## Scores (1–10) with one-line justification each
- Novelty: 6 — the leakage-aware ladder is well motivated; the selector and the statistics are standard.
- Technical soundness: 5 — sensible controls, but uncontrolled degrees of freedom (regate rule, mid-campaign subset redefinition, one replicate in one cell).
- Evaluation rigour: 4 — most rungs are dev-only (n=80); no visible plan for CIs, pairing, clustering or multiplicity across >70 cells.
- Clarity (of the design, as reconstructed): 6 — the flags make the ladder legible; field sets per rung and the regate rule are opaque.
- Impact / significance: 7 — a real, non-synthetic task where contamination is the scientific question; a reference protocol if the inference is done properly.
- Overall: 5 — borderline; 7 if items 1–4 below are delivered on the test split.

## Strengths
- Served-model audit on all 9,178 calls, 0 mismatches, plus a verbatim per-run token/cost/latency ledger.
- One ablation per leakage channel (title, holder, creator, dimensions); the prompt-token fingerprint (1,959 → 1,735 → 1,208 → 1,064 tok/call) confirms the rungs really remove content.
- Both-orders presentation in E8, `--balance-source` in E7, a replicate and two prompt variants at L1 — the right instincts, if extended.
- Honest cost accounting (reasoning tax of GPT-5.4-mini; pointwise 3× cost / 14× wall).

## Weaknesses
1. **BLOCKER — sample size with no uncertainty plan.** Wilson 95 % half-widths at p≈0.7: ±10 pp at n=80, ±15 pp at n=32 (L2-T dev), ±5 pp at n=294. Yet most rungs exist only on dev: L3 has four dev runs and no test run; L6, L5-P and `--holder-scrub v2` exist only for GPT-5.4 on dev; `20261024_234820_e10_agent_L5-P_xj-gpt-5.4` (test) failed, rc=1, 4 API errors. A dev-only "L1→L3 drop" below ~15 pp is indistinguishable from zero (paired McNemar power at n=80, 20 % discordance, Δ=10 pp ≈ 0.5).
2. **BLOCKER — queries are not independent.** Queries from the same ensemble share the memorised fact and overlapping shortlists, so outcomes are correlated within ensemble. Bootstrapping over queries overstates precision: with 3 queries/ensemble and ICC 0.3 the design effect is 1.6 (n_eff ≈ 184 test, ≈ 50 dev). The number of ensembles per split appears nowhere.
3. **MAJOR — multiplicity.** ~10 models × 7 rungs × {dev, test} × {pre, post-regate} × prompt variants exceeds 300 numbers. At a Bonferroni level for 70 cells (z = 3.38) the detectable unpaired difference is 14 pp at n=294 and 27 pp at n=80. Without ≤5 pre-specified contrasts the grid is noise with a few lucky cells.
4. **MAJOR — `e10_regate.py` is a hidden degree of freedom.** It runs after every E10 run (`follow_up` column) with an undisclosed acceptance rule. If its threshold was tuned after seeing dev — or any test — outcomes, every headline number is optimistically biased.
5. **MAJOR — the L2-T subset was redefined mid-campaign, on test.** `E10_agent_L2T_dev/test` (10-23) ran 5 dev / 17 test queries at 1,730 tok/call; `E10_agent_L2Ttitle_dev/test` (10-24) ran 32 / 91 at 2,316 tok/call. Two definitions touched the test split; the ledger cannot tell me whether the first results were seen before the second rule was written. More generally, L1 test ran on 10-22, before L5-P, L6 and scrub v2 existed — state the freeze policy.
6. **MAJOR — the ladder is not nested.** Withholding the title *adds* ≈360 prompt tokens (2,316 vs 1,959): something was substituted. If that is description or provenance text absent at L1, L2-T is a different condition, not a rung. Test prompts are also 3–4 % longer than dev at every rung (2,023/1,959; 1,807/1,735; 1,230/1,208).
7. **MAJOR — variance is measured in one cell.** `--replicate 1`, `v1`, `v2` exist only for GPT-4.1-mini at L1 dev, and completion tokens swing 59 → 105 /call between v2 and v1, so the variants also change output format. No replicate on test, none for the temperature-less GPT-5.x family (450–770 hidden-reasoning tokens/call on GPT-5.4-mini), none at L5/L6 where effects are smallest.
8. **MINOR — ledger anomalies needing one sentence each.** (a) `cache_hits = 3` on every L1 test run and 2 on every L3-H/L5 test run: if the cache key is prompt text, 2–3 test prompts are byte-identical to an earlier prompt (duplicate test queries, or dev/test overlap). (b) GPT-5.4 was served under two identifiers inside one run (`gpt-5.4-2026-03-05` 221 / `gpt-5.4` 73 on L1 test); the audit counts both as matches. (c) E8 uses 100 pairs (Wilson CI at p = 0.75: [0.66, 0.82]) and the with-evidence variant exists only for GPT-4.1-mini, so the within-model memory-vs-evidence gap is one unreplicated number.

## Experiments or artefacts that would change my score
1. Per-cell table with ensemble-clustered bootstrap 95 % CIs (resample ensembles, ≥10k draws) and n_ensembles per split. *Convince me:* test CIs for L1−L5 and L5−L5-P exclude zero.
2. Paired tests between adjacent rungs on identical queries (exact McNemar), risk difference with CI and Cohen's h, Holm-corrected over ≤5 pre-registered contrasts. *Convince me:* L5 vs L5-P paired difference with CI inside ±5 pp *or* a clear drop — not an unpowered "n.s.".
3. Pre- and post-regate numbers for every cell, the regate rule as hashed code, and a dev-only threshold sweep with test scored once at the frozen value. *Convince me:* orderings unchanged, |Δ| < CI half-width.
4. Three replicates (or three prompt variants for temperature-less models) of the full dev ladder for GPT-4.1-mini and GPT-5.4. *Convince me:* between-replicate SD < 3 pp, smaller than adjacent-rung gaps.
5. Both L2-T definitions reported, with the timestamp at which the final one was frozen. *Convince me:* same sign and comparable magnitude under both.
6. The decisive test cells completed: L5-P (the 10-25 00:20 restart), L6, L3 for at least GPT-5.4. *Convince me:* the dev ordering of rungs replicates on test within CI.
7. Closed-book E5 on the test split, and test accuracy stratified by closed-book success. *Convince me:* non-trivial L5/L6 accuracy on queries the model cannot name closed-book.
8. A power statement per contrast: minimum detectable paired difference at 80 % power given observed discordance.

## Token-efficiency / cost critique
- **Wasteful.** GPT-5.4-mini emits 1.02 M of 1.46 M completion tokens (70 %) for $33.19 (33 % of budget), costs the same per call as GPT-5.4 ($0.016–0.023 vs $0.013–0.020) and is 3× slower on test (14–15 s/call vs 4.6). The `--inputs v2` ablation (+73 % prompt tokens, $9.1) ran only on this model, confounding input richness with model. E16 spent $12.65 (12.6 %) on dev only, re-scoring a Qwen3-VL-2B shortlist. L1 test for four models cost $18.2 — the rung where title leakage and memory are maximal — while L3, L6 and L5-P have no test coverage.
- **Cheap and missing.** Extra dev replicate: $0.33 (GPT-4.1-mini) to $1.6 (GPT-4.1). Closed-book on test: $0.17–$2.2 per model. E8 on GPT-5.4 and GPT-5.4-mini: ≈$2.4 each, never run. E6 baseline from 40 to 80 queries: $0.22. Shuffled-shortlist-order run at L1: $0.33–$1.6. Regate ablation: $0. The ledger marks GPT-5.4 prices as *estimated*; say so.

## One idea the authors have not tried
Fit one hierarchical logistic model to all per-query outcomes instead of hundreds of cell-wise comparisons: logit P(correct) = α_model + β_rung + γ_model×rung + u_ensemble + v_query, with crossed random effects because the same queries are reused across models and rungs. This (a) handles ensemble clustering by construction, (b) borrows strength across the sparse test grid (L3/L6/L5-P missing for most models), (c) yields every contrast with a proper CI, and (d) lets closed-book success (E5) and forced-choice memorisation (E8) enter as per-query covariates, so "memory vs evidence" becomes an estimated interaction instead of a narrative. All inputs already exist in the per-run `reports/*.json`; zero API cost. Report ICC_ensemble as a headline number — it tells readers how many independent problems the benchmark actually contains.

## Confidence (1–5) and what I could not assess
4. I could not see the field sets per rung, the regate rule, the shortlist retriever, the metric (set-F1? exact set? MRR?), the ground-truth source, the number of ensembles, or any accuracy. My concerns are about the inferential design, which the ledger exposes directly; if clustered CIs and paired tests already exist, items 1–3 collapse.
