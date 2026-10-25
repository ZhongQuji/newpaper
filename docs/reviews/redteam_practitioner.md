# Red-team review — the practitioner who has to run it

Premise: the scripts and flags in the brief, the campaign runner (JSON plan, stages, `max_parallel`), four `xj-*` aliases through the paid relay, $100. All rates are from `data/real/runs.csv` (rc = 0 rows) via pandas. Fitted relay prices (least squares, max error 5.6 %), $/M prompt/completion tokens: GPT-4.1-mini 1.71/8.10, GPT-4.1 8.88/36.2, GPT-5.4 7.92/47.9, GPT-5.4-mini 3.29/20.3. Token model from E10 + E10e: listwise prompt ≈ 128 + 31·r with r = 59 tok/record (L1), 35 (L5); pointwise ≈ 128 + 2r, 29.3 requests/query, 2.70 s/request. Sequential pace 4.2–6.6 s/call (non-thinking), 6.6–15 s (GPT-5.4-mini).

## (a) Existing flags (E), small code change (S), new infrastructure (N)

| item | | what exactly |
| --- | --- | --- |
| A1 ensemble-level metric | S | scorer over existing run dirs + gold groups: pairwise P/R/F1, B-cubed, bootstrap by ensemble; no API |
| A2 nested ladder (= M7) | S→N | documenting fields is free; nesting L2…L6 rewrites the level definitions in `llm_reunion_agent.py`, invalidates every rung but L1 → $74 test re-run (5 rungs × 4 models × 294 queries) |
| A3 recall@30, shortcut row, no-gold stratum | E/S | `e10_shortlist_controls.py` already emits `shortlist_shortcuts`; recall@30 is a join; no-gold shortlists need a builder flag |
| A4 freeze `e10_regate` (= M15) | E | rule into a pre-registration file; git-tag before the next test run |
| A5 stratify by fame / E8 outcome (= M10, M13) | S | join `commons_views`, `nga_views`, `--analyze-run` on query id |
| A6 GPT-5.4 L5-P + L6 on test | E | `--level L5 --dims-permute 20261024 --split test`; `--level L5 --withhold-title --split test`; L5-P died with 4 `api_errors` → needs retry/resume |
| A7 test seeds | E/S | `--replicate` samples on GPT-4.1(-mini); GPT-5 rejects temperature → on GPT-5.4 only `--shuffle-seed` makes a replicate |
| A8 E8v4 on GPT-5.4 family | E/S | both arms run today; ids-only arm and period-matched counterfactuals are new options in `llm_cf_forced_choice.py` |
| A9 `--k 10` vs `--k 30` + shuffle (M6 proxy) | E/S | `--k 10` exists; `--dims-permute` permutes dimensions, not positions — add `--shuffle-seed <int>` |
| A10 cost-matched SC | E/S | five `--replicate` runs + a 50-line vote script |
| A11 CLIP/SigLIP/DINOv2 (M8 part) | N | GPU, E16's local thumbnails, embedding script; $0 API |
| A12 datasheet / licences | N | documentation; seed = `release_validation` |
| M1 | E | L1/L5/L6 rows exist |
| M2 ids-only output | S | template + strict JSON parse (`--prompt-variant v2` already cut completions 105 → 59 tok) |
| M3 effort sweep | S | `reasoning_effort` hard-wired to `low`; expose `--reasoning-effort` |
| M4/M5 cascade | S→N | prototype: `llm_pointwise_rerank.py --from-run <mini L5 run>` (E) → offline band → flagship listwise on survivors (`--candidates-from <json>`, S); production driver N |
| M4′ prune, M6 adaptive K | S/N | S if shortlist files carry retriever scores, N if only ranks |
| M8 visual closed-book, same-holder negatives | N | new probe; shortlist-builder change |
| M9 grounding + checker | S | one short call per predicted member + literal field-presence check |
| M11 abstention | S | allow `[]` + confidence in prompt/parser; needs A3's no-gold stratum |
| M12 routing, M14 VoI gate | N | drivers; replay offline first from existing mini + flagship dev runs ($0) |
| M13 non-Western stratum | N | dataset work (≈$130) |
| M16 Pareto reporting | E | `tools/extract_real_runs.py` gives the cost column |

## (b) Hidden operational risks

1. **Relay rate limits.** GPT-4.1's family note — "relay rate 9 / 36: decisive jobs only" — means GPT-4.1 was rationed. Observed sequential request rates: 10.8/min (mini L1), 11.3 (GPT-4.1 L1), 14.2 (GPT-5.4), 22 (pointwise). Two GPT-4.1 stages under `max_parallel 2` double that; an 8-way pointwise client hits ≈180/min. Confirm the quota first; cap concurrency *per model*.
2. **`api_errors` and the failed L5-P campaign.** On 10-24 22:31–23:56 all three stages (Gemini 3 Pro, Claude Opus 4.6, GPT-5.4) ended rc = 1; GPT-5.4 made 4 calls, 4 errors, 505 s (126 s/attempt → timeouts) and aborted: a relay incident. The 00:20 restart is unverified (log ends 00:20:28; a lock file dated 00:37 may block the next start). E17 silently swallowed 2 errors in 211 steps. Needed: per-call retry with backoff + jitter, resume from the last completed query in `run_dir`, `api_errors > 0 → do not quote`.
3. **Unpinned aliases.** GPT-5.4 was served as `gpt-5.4-2026-03-05` *and* bare `gpt-5.4` in 4–31 % of calls (73/294 on L1 test); L6 dev and E17 were 100 % pinned — routing changed within 48 h. Request the dated snapshot, log `response.model` per call, stratify by served label.
4. **Cache hits are duplicate prompts of four kinds.** 3 hits on every 294-call L1 test run and 2 on every L3-H/L5 test run, model-independent → 2–3 test queries with byte-identical prompts. 8 hits in L3-H2 dev → removing the holder made 8 prompts collide → near-duplicate records differing only by holder (a ground-truth problem). 135/2,344 pointwise hits → duplicate (query, candidate) pairs. 47/295 harness hits → the agent loops. None is analysable: cache key and colliding call id are not logged.
5. **Sequential pointwise.** 29.3 × 2.70 s = 79 s/query; the test split is 8,614 requests = 6.5 h on one worker. Every cascade plan needs an async client (8 in flight → ≈50 min) and risk 1 settled. Put query + instructions first so provider prompt caching (`cached_tokens`) covers the 29 re-sends.
6. **Wall-time and thinking-model variance.** GPT-5.4-mini test ran at 14–15 s/call (L3-H, L5) vs 6.6 s at L1; GPT-5.4 L6 dev at 20 s/call vs 4.4 typical → 2–4× slack, flagship test jobs overnight. GPT-5.4-mini completion tokens swing 440–766/call and grow as evidence shrinks; the dev→test cost predictor holds for non-thinking models only.
7. **Redefinitions and accounting.** L2-T went from 5/17 to 32/91 queries between 10-23 and 10-24; `e10_regate` runs after every job; GPT-5.4 prices are "estimated"; failed calls show $0 but may be billed. Record detector/regate versions in `run_dir`; reserve 20 %.

## (c) The next $100 as a decision tree

Cost and wall time per node are sequential sums from the rates above; "noise" = replicate ΔF1 from N2; test MDD = 7–9 points (`sim/results/POWER.md`). Never run two GPT-4.1 stages in parallel.

- **N0 — $0, analysis; gates everything.** A1, A3, A4, A5; dedupe the duplicate test prompts; verify the 00:20 restart; per-query Jaccard of `L1_dev` vs `_rep1` and `_v1` vs `_v2`.
  - Jaccard > 0.9 → skip N9. Recall@30 at L5 < 0.8 → the retriever is the ceiling: K stays 30, go to N3, not "read less".
- **N1 — dilution + position, GPT-4.1-mini dev: $1.64, 53 min (27 min 2-parallel).** `--k 10` at L1 ($0.17, 778 tok/call) and L5 ($0.10); `--shuffle-seed` at K = 30, L1 ($0.33) and L5 ($0.20).
  - F1(k10) ≈ F1(k30) within noise and recall@10 ≈ recall@30 → β ≈ 0 → "read less" (M6/M4′ replayed offline, $0); skip N9; N3 only if the mini trails the flagship by > noise.
  - F1(k10) > F1(k30) → β > 0 → N3 mandatory. F1(k10) < F1(k30) with recall@10 < recall@30 → retriever-limited, K = 30, savings only via N3.
  - κ(shuffled, original) < 0.7 → every later test run needs two orders (doubles N6).
- **N2 — dev noise floor, GPT-4.1-mini: $0.72, 20 min, alongside N1.** L1 rep2 ($0.33), L5 rep1–2 ($0.39).
  - noise > 8 points → dev is uninterpretable; stop buying dev variants, compare on test (N6).
- **N3 — cascade prototype on dev: $1.07, 108 min (105 = sequential pointwise).** `llm_pointwise_rerank.py --from-run <mini L5 dev>` ($0.81, 2,344 requests) → reject-only band p̂ < 0.05 → GPT-4.1 `--level L1 --candidates-from` on ≈8 survivors for ≈40 % of queries ($0.26, 32 calls); paired against the existing GPT-4.1 L1 dev run.
  - cascade ≥ flagship − noise at ≤ 60 % cost → v2 reference → N7, N10. Else the saving is M1–M3; M4/M5 stay simulation.
- **N4 — ladder floor on test, GPT-5.4: $7.11, 45 min (≤ 2 h in a slow period).** L5-P rerun ($3.81) and L6 ($3.30), 294 calls each; needs retry/resume.
  - L5 − L5-P > MDD → dimensions carry the physical channel. L5 − L6 > MDD → title is the bottom leak (B4) → the $74 nested ladder is unavoidable before any ladder claim; L5 ≈ L6 → defer A2, report L6 as floor.
- **N5 — memorisation on the likeliest memorisers: core $12.49, ≈3.5 h (one GPT-5.4 stage at a time).** GPT-5.4 E8v4 both arms ($2.73 + $3.09) + ids-only arm ($2.07, A8); GPT-4.1 E8v4 L1 arm, never run ($2.73); E5 closed-book on test, GPT-4.1 ($0.82) + GPT-5.4 ($1.05). Optional +$9.55: GPT-5.4-mini arms, only if it survives N8.
  - ids-only > 60 % on GPT-5.4 → stratify every ladder number; N6's seeds go to L5/L6, not L1. ids-only ≈ 50 % but the 260-token arm ≫ 50 % → that arm was period matching (R03); say so.
- **N6 — test-split power: core $4.71, ≈2.2 h.** Mini L1 seeds 2–3 ($2.48, 588 calls), L5 seeds 1–3 ($2.23, 882 calls; no mini L5 test run exists). Conditional +$12 per flagship — two shuffled L1 test runs on GPT-4.1 ($12.15) or GPT-5.4 ($11.85) — headline model only, and only if κ < 0.7 or noise > 5 points.
- **N7 — v2 system on test (only if N3 passed): $3.95; 6.6 h sequential, ≈1 h async.** Mini pointwise @L5 ($2.98, 8,614 requests) + GPT-4.1 @L1 on the band ($0.97, 118 calls).
- **N8 — effort sweep, GPT-5.4-mini L5 dev: $3.01, 28 min (needs M3's flag).** `minimal` ($0.43), `medium` ($2.58, assuming 2× low's hidden tokens). Flat → drop GPT-5.4-mini, save N5's $9.55.
- **N9 — cost-matched SC, mini dev (only if Jaccard < 0.9 and β > 0): $1.57, 41 min.** Reps 3–5 at L1 ($0.98) and L5 ($0.59); vote vs one GPT-4.1 call ($0.0200 = 4.8 mini calls).
- **N10 — M9 grounding pilot on dev after N3: $0.14 (mini) / $0.70 (GPT-4.1), 13 min, ≈144 member calls. A11 CLIP baseline: $0 API, GPU minutes, any time.**

Totals: unconditional N0–N6 core = **$27.7**; every conditional branch (N5-ext, N6-ext both flagships, N7–N10) = **$70.6**; ≈$29 remains as the 20 % retry reserve. The $74 nested-ladder re-run does **not** fit and must wait for N4 and N5.

## (d) What to log per call that is not logged today

Today the suite JSON records per *run*: calls, tokens, cost, `cache_hits`, `api_errors`, a served-model histogram. Needed per *call*, one JSONL line in `run_dir`:

| field | enables |
| --- | --- |
| `query_id`, `level`, `schema_hash` (fields per rung), `prompt_template_version`, `regate_rule_hash`, `git_sha` | joins across rungs and days; A2, A4, M15 |
| `prompt_sha256` + `canonical_sha256` (ids/whitespace stripped) | duplicate analysis: which call collided; duplicate record vs duplicate shortlist |
| `cache` = {hit/miss, key, `source_call_id`} | separating the four kinds of hit; excluding cached calls from variance |
| `candidates[]` = ordered {id, position, retriever_score, retriever_rank, is_gold}, `shuffle_seed` | position bias (selection rate vs position), recall@K, offline replay of M6/M4′/M12 |
| `response_raw`, `parsed_ids[]`, `parse_status` | v1/v2 output-length effects; parse failures as their own class |
| `logprobs` (first-token P(yes); per-id logprobs where passed) | calibration, cascade band, risk–coverage, un-mixing weights |
| `usage` incl. `reasoning_tokens`, `cached_tokens` | reasoning tax per query; cache savings in pointwise |
| `requested_model`, `served_model`, `system_fingerprint`, `request_id` | stratify by served snapshot; relay audit trail |
| `attempts[]` = {t_start, t_end, http_status, error_class} | retries, timeouts, slow-relay periods |
| `sampling` = {temperature or "rejected", reasoning_effort, seed} | A7, N8 interpretability |
| `pre_regate_ids[]`, `post_regate_ids[]` | B6 in one place |

With these, the position-bias, duplicate and un-mixing analyses are offline joins on `query_id`; without them each needs a re-run.
