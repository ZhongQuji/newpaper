# Red-team review — the practitioner who has to run it

Premise: the scripts and flags named in the brief, the campaign runner (JSON plan with stages and `max_parallel`), the four `xj-*` aliases through the paid relay, and $100. All rates below come from `data/real/runs.csv` (rc = 0 rows) via pandas. Fitted relay prices (least squares, max error 5.6 %), $ per M prompt/completion tokens: GPT-4.1-mini 1.71/8.10, GPT-4.1 8.88/36.2, GPT-5.4 7.92/47.9, GPT-5.4-mini 3.29/20.3. Token model fitted from E10 and E10e: listwise prompt ≈ 128 + 31·r, with r = 59 tok/record at L1 and 35 at L5; pointwise ≈ 128 + 2r, 29.3 requests/query, 2.70 s/request. Observed sequential rates: 4.2–6.6 s/call (non-thinking), 6.6–15 s (GPT-5.4-mini).

## (a) Existing flags, small change, or new infrastructure

**E** = runs with existing flags; **S** = small code change (one script, one flag); **N** = new infrastructure.

| item | | what exactly |
| --- | --- | --- |
| A1 ensemble-level metric | S | new scorer over existing run dirs + gold groups: pairwise P/R/F1, B-cubed, bootstrap by ensemble; no API |
| A2 nested ladder schema (= M7) | S→N | documenting fields per rung is free; making L2…L6 nested changes the level definitions in `llm_reunion_agent.py` and invalidates every rung except L1 → a $74 test re-run (5 rungs × 4 models × 294 queries, one seed) |
| A3 recall@30, shortcut row, no-gold stratum | E/S | `e10_shortlist_controls.py` already emits `shortlist_shortcuts`; recall@30 is a join of shortlist files with gold; injecting no-gold shortlists needs a flag in the shortlist builder |
| A4 disclose/freeze `e10_regate` (= M15) | E | read the script, write the rule into a pre-registration file, git-tag it before the next test run |
| A5 stratify by fame / E8 outcome (= M10, M13 reporting) | S | join `commons_views`, `nga_views`, `--analyze-run` output on query id; analysis only |
| A6 GPT-5.4 L5-P and L6 on test | E | `--level L5 --dims-permute 20261024 --split test`; `--level L5 --withhold-title --split test`; L5-P failed on 10-24 with 4 `api_errors` → needs retry/resume (risk 2) |
| A7 test seeds | E/S | `--replicate N` is a real replicate on GPT-4.1(-mini); the GPT-5 family rejects temperature, so on GPT-5.4 it is a near-deterministic re-run — needs `--shuffle-seed` |
| A8 E8v4 on the GPT-5.4 family | E/S | both arms run today; the *truly* evidence-free arm (ids only) and period-matched counterfactuals are new options in `llm_cf_forced_choice.py` |
| A9 `--k 10` vs `--k 30` + shuffled order (M6 proxy) | E/S | `--k 10` exists; `--dims-permute <seed>` permutes dimensions, not positions — add `--shuffle-seed <int>` beside it |
| A10 cost-matched self-consistency | E/S | five `--replicate` runs + a 50-line majority-vote script over run dirs |
| A11 CLIP/SigLIP/DINOv2 cosine (M8 part) | N | GPU, local image cache (E16 fetched thumbnails), embedding script; $0 API |
| A12 datasheet / licence audit | N | documentation; `release_validation` report is the seed |
| M1 evidence-minimal prompt | E | L1/L5/L6 rows exist; stratified comparison is analysis |
| M2 ids-only output | S | prompt template + strict JSON parse (`--prompt-variant v2` already cut completions 105 → 59 tok) |
| M3 reasoning-effort sweep | S | `reasoning_effort` is hard-wired to `low`; expose `--reasoning-effort` |
| M4 / M5 cascade, evidence escalation | S→N | prototype: `llm_pointwise_rerank.py --from-run <mini L5 run>` (E) → offline band → flagship listwise on survivors (needs `--candidates-from <json>`); a production driver is N |
| M4′ retriever prune, M6 adaptive K | S or N | S if shortlist files carry retriever scores; N if only ranks exist (calibration step) |
| M8 visual closed-book, same-holder negatives | N | new probe script; shortlist-builder change |
| M9 grounding call + checker | S | one short call per predicted member + deterministic field-presence check |
| M11 abstention | S | allow `[]` + confidence in prompt and parser; risk–coverage offline; needs A3's no-gold stratum |
| M12 routing, M14 VoI gate | N | drivers — but both can first be *replayed offline* from existing mini + flagship dev runs ($0) |
| M13 non-Western stratum | N | dataset work (≈$130 per `docs/04`) |
| M16 Pareto reporting | E | `tools/extract_real_runs.py` already yields the cost column |

## (b) Hidden operational risks

1. **Relay rate limits.** The GPT-4.1 family note says "relay rate 9 / 36: decisive jobs only" — whatever the unit, GPT-4.1 was rationed. Observed sequential request rates: 10.8/min (mini L1), 11.3/min (GPT-4.1 L1), 14.2/min (GPT-5.4), 22/min (pointwise). Two GPT-4.1 stages under `max_parallel 2` double that; a parallel pointwise client (8 in flight) would hit ≈180/min. Confirm the quota on the relay dashboard first; give the plan a *per-model* concurrency cap, not only a global one.
2. **`api_errors` and the failed L5-P campaign.** On 10-24 22:31–23:56 all three stages (Gemini 3 Pro, Claude Opus 4.6, GPT-5.4) ended rc = 1; the GPT-5.4 job made 4 calls, 4 errors, 505 s (126 s per attempt → timeouts) and aborted. A relay incident, not a model problem. The 00:20 restart is unverified (`api_campaign_pt.log` ends 00:20:28; a lock file dated 00:37 may block the next start). E17 swallowed 2 errors in 211 steps — the agent lost steps silently. Needed: per-call retry with exponential backoff and jitter, resume from the last completed query in `run_dir`, cool-down between campaign attempts, and an `api_errors > 0 → do not quote` flag.
3. **Unpinned aliases.** GPT-5.4 was served as `gpt-5.4-2026-03-05` *and* bare `gpt-5.4` in 4–31 % of calls per run (73/294 on L1 test), while later runs (L6 dev, E17) were 100 % pinned — routing changed within 48 h. Request the dated snapshot explicitly, log `response.model` per call, stratify accuracy by served label before quoting GPT-5.4.
4. **Cache hits are duplicate prompts of four kinds.** Exactly 3 hits on every 294-call L1 test run and 2 on every L3-H/L5 test run, model-independent → 2–3 test queries have byte-identical prompts (duplicate records or identical shortlists). 8 hits in L3-H2 dev → scrubbing the holder made 8 prompts collide → near-duplicate records differing only by holder — a ground-truth problem. 135/2,344 pointwise hits → duplicate (query, candidate) pairs → duplicate candidates in the pool. 47/295 harness hits → the agent loops. None is analysable today: the cache key and the colliding call id are not logged (see (d)).
5. **Sequential pointwise.** 29.3 × 2.70 s = 79 s/query; the test split is 8,614 requests = 6.5 h on one worker. Every cascade plan needs an async client (8 in flight → ≈50 min) *and* risk 1 resolved. The query is re-sent 29×: put query + instructions first so provider prompt caching (`cached_tokens`) applies.
6. **Wall-time variance and thinking-model cost.** GPT-5.4-mini test ran at 14–15 s/call (L3-H, L5, 13:47–16:13 CST) vs 6.6 s at L1; GPT-5.4 L6 dev at 20 s/call vs 4.4 s typical — budget 2–4× slack, run flagship test jobs overnight. GPT-5.4-mini completion tokens swing 440–766/call and grow as evidence shrinks, so the dev→test cost predictor holds for non-thinking models only.
7. **Mid-campaign redefinitions and accounting.** L2-T changed from 5/17 to 32/91 queries between 10-23 and 10-24; `e10_regate` runs after every job; GPT-5.4 prices are "estimated"; failed calls show $0 but the relay may bill timeouts. Record detector and regate versions in `run_dir`; reserve 20 %.

## (c) The next $100 as a decision tree

Per-node cost and wall time are sequential sums from the per-call rates above; "noise" = replicate-to-replicate ΔF1 from N2; MDD on test = 7–9 points (`sim/results/POWER.md`). Never run two GPT-4.1 stages in parallel.

- **N0 — $0, analysis only; gates everything.** A1, A3, A4, A5; dedupe the 2–3 duplicate test prompts; verify the 00:20 L5-P restart; per-query Jaccard of `E10_agent_L1_dev` vs `_rep1` and `_v1` vs `_v2`.
  - Jaccard > 0.9 → skip N9 for good. Recall@30 at L5 < 0.8 → the retriever is the ceiling; K stays 30; go to N3, not "read less".
- **N1 — dilution and position, GPT-4.1-mini dev: $1.64, 53 min (4 jobs; 2 in parallel → 27 min).** `--k 10` at L1 ($0.17, 778 tok/call) and L5 ($0.10); `--shuffle-seed` at K = 30, L1 ($0.33) and L5 ($0.20).
  - F1(k10) ≈ F1(k30) within noise and recall@10 ≈ recall@30 → β ≈ 0 → adopt "read less" (M6/M4′ replayed offline, $0); skip N9; N3 only if the mini trails the flagship by > noise.
  - F1(k10) > F1(k30) → β > 0 → N3 mandatory.
  - F1(k10) < F1(k30) with recall@10 < recall@30 → retriever-limited → K = 30; savings must come from N3.
  - κ(shuffled, original) < 0.7 → position bias is real → every later test run needs two orders (doubles N6); κ ≥ 0.7 → one order.
- **N2 — dev noise floor, GPT-4.1-mini: $0.72, 20 min; run alongside N1.** L1 rep2 ($0.33), L5 rep1 + rep2 ($0.39).
  - noise > 8 F1 points → dev is uninterpretable; stop buying dev variants, move comparisons to N6.
- **N3 — cascade prototype on dev: $1.07, 108 min (105 of them the sequential pointwise run).** `llm_pointwise_rerank.py --from-run <mini L5 dev run>` ($0.81, 2,344 requests) → offline reject-only band (p̂ < 0.05) → GPT-4.1 `--level L1 --candidates-from` on ≈8 survivors for ≈40 % of queries ($0.26, 32 calls); paired against the existing GPT-4.1 L1 dev run.
  - cascade F1 ≥ flagship − noise at ≤ 60 % cost → v2 reference system → N7, N10.
  - else → the paper's saving is M1–M3; M4/M5 stay simulation.
- **N4 — ladder floor on test, GPT-5.4: $7.11, 45 min (≤ 2 h in a slow relay period).** L5-P rerun ($3.81, 294 calls) and L6 ($3.30). Needs retry/resume or it fails the same way.
  - L5 − L5-P > MDD → dimensions carry the physical channel. L5 − L6 > MDD → title is the leak at the bottom (B4) → the $74 nested ladder becomes unavoidable before any ladder claim; L5 ≈ L6 → defer A2, report L6 as the floor.
- **N5 — memorisation on the likeliest memorisers: core $12.49, ≈3.5 h (one GPT-5.4 stage at a time).** GPT-5.4 E8v4 both arms ($2.73 + $3.09) + ids-only arm ($2.07, A8's flag); GPT-4.1 E8v4 L1 arm, never run ($2.73); E5 closed-book on test, GPT-4.1 ($0.82) and GPT-5.4 ($1.05). Optional +$9.55: GPT-5.4-mini arms, only if it survives N8.
  - ids-only > 60 % on GPT-5.4 → p_mem is large → every ladder number stratified; N6's seeds go to L5/L6, not L1.
  - ids-only ≈ 50 % but the 260-token arm ≫ 50 % → that arm was period matching (R03); report it as such.
- **N6 — test-split power: core $4.71, ≈2.2 h.** GPT-4.1-mini L1 seeds 2–3 ($2.48, 588 calls) and L5 seeds 1–3 ($2.23, 882 calls; no mini L5 test run exists). Conditional +$12 per flagship — two shuffled-order L1 test runs on GPT-4.1 ($12.15) or GPT-5.4 ($11.85) — only for the headline model and only if N1 gave κ < 0.7 or N2 noise > 5 points.
- **N7 — v2 system on test (only if N3 passed): $3.95, 6.6 h sequential → ≈1 h with the async client.** Mini pointwise @L5 on 294 queries ($2.98, 8,614 requests) + GPT-4.1 @L1 on the band ($0.97, 118 calls).
- **N8 — reasoning-effort sweep, GPT-5.4-mini L5 dev: $3.01, 28 min (needs M3's flag).** `minimal` ($0.43) and `medium` ($2.58, assuming 2× low's hidden tokens). Flat accuracy → GPT-5.4-mini is the dominated point; drop it and save N5's optional $9.55.
- **N9 — cost-matched self-consistency, GPT-4.1-mini dev (only if N0 Jaccard < 0.9 and N1 β > 0): $1.57, 41 min.** Reps 3–5 at L1 ($0.98) and L5 ($0.59); vote offline against one GPT-4.1 call ($0.0200 = 4.8 mini calls).
- **N10 — M9 grounding pilot on dev (after N3): $0.14 mini / $0.70 GPT-4.1, 13 min.** ≈144 member calls; first evidence-grounding rate.
- **A11 CLIP baseline — $0 API, GPU minutes, any time.**

Totals: unconditional path N0–N6 core = **$27.7**; every conditional branch taken (N5-ext, N6-ext both flagships, N7–N10) = **$70.6**; the remaining ≈$29 is the 20 % retry reserve plus buffer. The $74 nested-ladder re-run does **not** fit in this $100 and must not start until N4 and N5 say it is necessary.

## (d) What to log per call that is not logged today

The suite JSON records per *run*: calls, tokens, cost, `cache_hits`, `api_errors`, a served-model histogram. Needed per *call*, one JSONL line in `run_dir`:

| field | enables |
| --- | --- |
| `query_id`, `split`, `level`, `schema_hash` (fields per rung), `prompt_template_version`, `regate_rule_hash`, `git_sha` | joining runs across rungs and days; A2, A4, M15 |
| `prompt_sha256` + `canonical_sha256` (ids and whitespace stripped) | the duplicate analysis: which call collided, and whether it is a duplicate record or a duplicate shortlist |
| `cache` = {hit/miss, key, `source_call_id`} | separating the four kinds of hit; excluding cached calls from variance |
| `candidates[]` = ordered {id, position, retriever_score, retriever_rank, is_gold, shown_fields_hash}, `shuffle_seed` | position bias (selection rate vs position), recall@K, offline replay of M6/M4′/M12, B3 |
| `response_raw`, `parsed_ids[]`, `parse_status`, `n_selected` | v1/v2 output-length effects; parse failures as their own error class |
| `logprobs` (first-token P(yes); per-id token logprobs where passed) + `confidence_verbalised` | calibration, cascade band, risk–coverage (M4, M11), un-mixing weights |
| `usage` incl. `reasoning_tokens`, `cached_tokens` | reasoning tax per query; provider-cache savings in pointwise |
| `requested_model`, `served_model` (`response.model`), `system_fingerprint`, `request_id` | stratify by served snapshot; audit trail with the relay |
| `attempts[]` = {t_start, t_end, http_status, error_class}, `latency_ms` | retries, timeouts, slow-relay periods; honest wall time |
| `sampling` = {temperature or "rejected", reasoning_effort, seed, max_tokens} | A7 and N8 interpretability |
| `pre_regate_ids[]`, `post_regate_ids[]` | B6 in one place |

With these, the position-bias, duplicate and un-mixing analyses become offline joins on `query_id`; without them each needs a re-run.
