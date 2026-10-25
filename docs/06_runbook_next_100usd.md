# 06 · Runbook — the next $100 of API spend, as a decision tree

Every command below uses **only flags that already appear in the ledger** (`data/real/runs.csv`,
column `argv`), so each one is known to run on the authors' machine as-is. Costs and wall times are
projected from the real per-call rates of the same model × level (ledger medians; dev→test scaling
validated in `figures/real/R7`). Where a step needs a flag that does **not** exist yet, it says so.

Follow-ups `scripts/e10_regate.py --run <run_dir>` and `scripts/e10_shortlist_controls.py --run <run_dir>`
run automatically after each E10 job in the campaign runner; keep that, but also export the
**pre-regate** decisions (see `tools/adapters/README.md`).

Legend: 💲 relay USD · ⏱ wall time (sequential) · ▶ what the result decides.

> **Decide the ladder schema before spending (red-team AC, B.8).** Nodes 1–4 and 6 are schema-neutral
> (they measure β, position bias, memory and cost-matching on existing rungs). Node 5 buys *old-schema*
> rungs (L5 with title, `--withhold-title` as L6). If the nested v2 schema of `docs/05` §2.2 is adopted,
> replace Node 5 by the v2 test ladder — same price class (≈ $74 for 5 rungs × 4 models at test, by the
> ledger's per-call rates) — rather than paying for both.

> **Node 0 cannot be skipped.** Three of its outputs gate everything after it: recall@30 (if < 0.6 the
> retriever is the bottleneck and "read less" is the wrong direction), the duplicate-prompt count on the
> test split, and whether the 10-25 00:20 restart of the L5-P campaign actually completed
> (`records/queue/api_campaign_pt.log`; a lock file dated 00:37 may block the next start).

---

## Node 0 — free, before any call (≈ 1 h of work, $0)

```bash
python3 tools/eval_toolkit.py --selftest                       # toolkit is sane on this machine
# write the adapter (tools/adapters/README.md) and rebuild ALL existing runs as decisions.csv:
python3 tools/eval_toolkit.py --input decisions.csv --summary  # ensemble-level CIs for every existing run
```
▶ Produces the first honest table (B1, B2). Also answers: recall@30 of the shortlist (needs gold in
the adapter), the "no gold in shortlist" count, and the duplicate-prompt question (B6b). The ledger's
`cache_hits` point to four different kinds of collision — 3 hits on every 294-call L1 test run (duplicate
test queries), 8 hits in the L3-H2 dev run (records that differ *only* by holder → near-duplicates in
the ground truth), 135/2,344 in the pointwise run (duplicate query–candidate pairs), 47/295 in the
deep-research harness (the agent loops). Hash prompts per call to tell them apart.
Also check **whether the relay returns logprobs** for each alias (it did for GPT-4.1-mini **[real]**):
mechanism M1 of `docs/04` (retriever-score prior fused with P(yes)) — the largest simulated gain — needs a
per-candidate score. If no logprobs, plan a verbalised 0–100 score (≈ +120 completion tokens/call).

**Stop rule:** if recall@30 < 0.6 on test, the retriever — not the LLM — is the paper's bottleneck;
re-order the tree to spend on the retriever first.

## Node 1 — the dilution test · 💲 0.6–0.9 · ⏱ ≈ 17 min

```bash
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1-mini --split dev --limit 0 --k 10 --level L1
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1-mini --split dev --limit 0 --k 10 --level L5
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1-mini --split dev --limit 0 --k 30 --level L1 --replicate 2
```
(`--k 10` reuses the existing `--k` flag; the third line is a fresh K=30 seed for a paired comparison.)
Compare with `tools/eval_toolkit.py --compare <k10 run> <k30 run>` restricted to candidates at
positions < 10 in both.

Also, at $0: if the K=30 runs carry per-candidate scores (logprobs) and the shortlist files carry
retriever scores, fit the fused decision `logit P = logit P_llm + logit P_retriever − logit π` on dev
and evaluate it offline — this is M1 (`docs/04` §3), the policy the simulation ranks first.

▶ **Measures list dilution β** — the parameter that decides the whole design space (`figures/sim/S8`):
- if K=10 ≥ K=30 on the top-10 candidates (β > 0): go to **Node 2a** (cascade / adaptive-K will pay);
- if K=10 ≈ K=30 (β ≈ 0): go to **Node 2b** (skip cascades; "read less" via retriever-prune is the only saving; pointwise is never worth it).

## Node 2a — cheap two-model cascade, dev · 💲 1.8 · ⏱ ≈ 13 min  *(needs one small code change for the real thing)*

The cascade needs "re-judge only these candidate ids with the flagship". Smallest change: add
`--only-candidates <json>` to `llm_reunion_agent.py` (or run `llm_pointwise_rerank.py --from-run`
on the uncertain band, which already exists but is pointwise). Until then, the *reject-only* variant
can be approximated with existing flags:

```bash
# cheap screen at L5 (exists):
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1-mini --split dev --limit 0 --k 30 --level L5
# strong judge at L1 on all 30 (exists) — then combine offline: accept only where BOTH say yes,
# or where the mini said "uncertain" and the flagship says yes:
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1 --split dev --limit 0 --k 30 --level L1
```
This upper-bounds the cascade's quality (the flagship sees everything) and its cost is known
exactly from the band fraction you observe. ▶ If offline-combined F1 ≥ flagship-alone F1 − 0.02 with
the mini rejecting ≥ 40 % of candidates, implement the real cascade (`docs/04` M4/M5).

## Node 2b — read less with no second model · 💲 1.7 · ⏱ ≈ 14 min

```bash
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1 --split dev --limit 0 --k 10 --level L1
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1 --split dev --limit 0 --k 15 --level L1
```
▶ F1 vs K on the flagship; pick the smallest K within 0.01 of K=30 → that is the production K
(`docs/04` M6). Retriever-prune (M4′) needs retriever scores in the adapter; if available, evaluate
offline on the K=30 run by masking candidates below the threshold — $0.

## Node 3 — position bias · 💲 1.9 · ⏱ ≈ 13 min  *(needs a `--shuffle-seed` flag — ≈ 5 lines)*

```bash
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1-mini --split dev --limit 0 --k 30 --level L1 --shuffle-seed 1
scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1 --split dev --limit 0 --k 30 --level L1 --shuffle-seed 1
```
then `tools/eval_toolkit.py --position-bias <run>` on both the ordered and shuffled runs.
▶ If recall(first third) − recall(last third) > 0.1 on the shuffled run: randomise order in every
future run and report the shuffled number (`figures/sim/S11`). Without the flag, `--dims-permute`'s
seed mechanism is the closest existing template for implementing it.

## Node 4 — close the memory probes on the models most likely to remember · 💲 15–19 · ⏱ ≈ 3.5–4 h

```bash
scripts/llm_cf_forced_choice.py --backend api --model xj-gpt-5.4      --n 100 --both-orders --tag v5
scripts/llm_cf_forced_choice.py --backend api --model xj-gpt-5.4      --n 100 --withhold-evidence --mask-creator --both-orders --tag v5
scripts/llm_cf_forced_choice.py --backend api --model xj-gpt-5.4-mini --n 100 --both-orders --tag v5
scripts/llm_cf_forced_choice.py --backend api --model xj-gpt-5.4-mini --n 100 --withhold-evidence --mask-creator --both-orders --tag v5
scripts/llm_eval_harness.py --task t0_closedbook --backend api --model xj-gpt-4.1-mini --split test --limit 0
scripts/llm_eval_harness.py --task t0_closedbook --backend api --model xj-gpt-5.4      --split test --limit 0
```
(GPT-4.1 no-evidence arm: 600 calls cost $2.36 and 49 min on 10-24; the with-evidence arm is ≈ 1.3× that;
GPT-5.4 is priced like GPT-4.1; GPT-5.4-mini ≈ $4 per arm if it reasons ≈ 300 tokens per answer as it did
in closed-book. Closed-book on test ≈ $0.17 (mini) / $1.05 (GPT-5.4).)
▶ p_mem per model for the un-mixing (`figures/sim/S5`, `eval_toolkit.unmix`). **Before running**, make
the `--withhold-evidence` arm truly evidence-free (today it still shows ≈260 tokens of item content;
docs/03 B5) — that is a prompt-template change, not a flag.

## Node 5 — complete the test ladder where the claim lives · 💲 ≈ 41 · ⏱ ≈ 5.3 h

Priority order (cost from the ledger's dev→test ratio, `figures/real/R7`):

| run | 💲 | ⏱ | why first |
| --- | ---: | ---: | --- |
| `--model xj-gpt-5.4 --split test --k 30 --level L5 --dims-permute 20261024` (retry of the failed 10-24 job) | 3.9 | 25 min | H3: is L5 using dimensions? |
| `--model xj-gpt-5.4 --split test --k 30 --level L5 --withhold-title` | 3.5 | 25 min | the only title-free rung, never run on test |
| `--model xj-gpt-4.1-mini --split test --k 30 --level {L3,L3-H,L5}` + `L5 --dims-permute` + `L5 --withhold-title` | 4.6 | 1.7 h | full ladder on the cheapest model |
| `--model xj-gpt-4.1 --split test --k 30 --level {L3-H,L5}` + `L5 --dims-permute` + `L5 --withhold-title` | 16.8 | 1.8 h | second flagship agrees on ladder shape? |
| `--model xj-gpt-5.4 --split test --k 30 --level L1 --shuffle-seed 1` and `… --level L5 --shuffle-seed 1` | 9.7 | 50 min | second run on the two headline rungs — the GPT-5 family rejects `temperature`, so `--replicate` would not sample; a shuffled order is the only independent run (needs the Node 3 flag) |
| `--model xj-gpt-4.1-mini --split test --k 30 --level L1 --replicate {1,2}` | 2.5 | 60 min | 3 seeds on the cheapest model |

▶ With Node 0's toolkit this yields the first ladder table with paired, ensemble-level CIs
(`figures/sim/S7`: n = 294 resolves ≥ 7–9-point drops). Note the GPT-5.4 L5-P job died with 4
`api_errors` after 505 s on 10-24 — check the relay's error before retrying; rate limits for GPT-4.1
were noted as "9/36" in the ledger's `family` field.

## Node 6 — cost-matched self-consistency (only if Node 1 found β ≈ 0) · 💲 0.8 · ⏱ ≈ 22 min

```bash
for r in 1 2 3 4; do scripts/llm_reunion_agent.py --backend api --model xj-gpt-4.1-mini --split dev --limit 0 --k 30 --level L5 --replicate $r; done
```
5 × GPT-4.1-mini at L5 ($0.0025 × 5 = $0.0127/query) = 1 × GPT-5.4 at L5 ($0.0127/call). Majority
vote offline. ▶ `figures/sim` predicts a median gain of only +0.01 F1; if the real gain is < 0.03,
drop self-consistency from the paper's method space.

## Running total

| node | 💲 | cumulative |
| --- | ---: | ---: |
| 0 | 0 | 0 |
| 1 | 0.9 | 0.9 |
| 2a or 2b | 1.8 / 1.7 | ≤ 2.7 |
| 3 | 1.9 | ≤ 4.6 |
| 4 | 15–19 | ≤ 24 |
| 5 | 41 | ≤ 65 |
| 6 | 0.8 | ≤ 66 |

≈ $34 of the $100 is left for relay failures (the ledger shows 3 failed jobs in 65) and for the first
pre-registration re-runs (`docs/05`). Wall time ≈ 10 h sequential; the campaign runner's
`max_parallel 2` roughly halves it, but watch the GPT-4.1 relay rate limit. All costs are projections
from `data/real/runs.csv` per-call medians (dev→test scaling verified in `figures/real/R7`); the
projection error on the existing dev→test pairs was < 5 %.

## What to log per call from now on (none of this is in the export today)

One JSONL line per call in `run_dir` (spec from `docs/reviews/redteam_practitioner.md` §d):

| field | enables |
| --- | --- |
| `query_id`, `level`, `schema_hash` (fields per rung), `prompt_template_version`, `regate_rule_hash`, `git_sha` | joins across rungs and days; the nested schema; pre-registration |
| `prompt_sha256` + `canonical_sha256` (ids/whitespace stripped) | which call collided; duplicate record vs duplicate shortlist |
| `cache` = {hit/miss, key, `source_call_id`} | separating the four kinds of hit; excluding cached calls from variance |
| `candidates[]` = ordered {id, position, retriever_score, retriever_rank, is_gold}, `shuffle_seed` | position bias, recall@K, offline replay of M1/M2 |
| `response_raw`, `parsed_ids[]`, `parse_status` | output-length effects; parse failures as their own class |
| `logprobs` (first-token P(yes); per-id where passed) | calibration, M1 fusion, risk–coverage, stratification weights |
| `usage` incl. `reasoning_tokens`, `cached_tokens` | reasoning tax per query; provider cache savings |
| `requested_model`, `served_model`, `system_fingerprint`, `request_id` | stratify by served snapshot; relay audit |
| `attempts[]` = {t_start, t_end, http_status, error_class} | retries, timeouts, slow-relay periods |
| `sampling` = {temperature or "rejected", reasoning_effort, seed} | replicate interpretability |
| `pre_regate_ids[]`, `post_regate_ids[]` | blocker B6 in one place |

With these, position-bias, duplicate-prompt, stratification and risk–coverage analyses are offline
joins on `query_id`; without them each needs a re-run. Operational: cap concurrency **per model**
(GPT-4.1 was rationed "9/36" on the relay **[real]**), add per-call retry with backoff + resume from the
last completed query (the L5-P job died after 4 timeouts of ~126 s), and never quote a run with
`api_errors > 0`.
