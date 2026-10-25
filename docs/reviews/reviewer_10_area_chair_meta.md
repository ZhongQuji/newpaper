# Reviewer 10 — Senior Area Chair (meta-review drafted before reading the other reviews)

## Summary of the submission as I understand it
A benchmark-plus-agent study of "digital reunion": an LLM agent picks, from a 30-candidate shortlist, the other members of a dispersed ensemble, evaluated along an information ladder (L1 full record → L6 physical facts minus title) with one ablation per leakage channel, memory-only probes (E5, E8v4) and costlier alternatives (pointwise rerank, deep research, open pool, MLLM visual gates). Four OpenAI-family models have complete ledgers (65 runs, 9,178 calls, $100.07, 17.7 h); eleven others ran without ledgers. The grid aims to separate evidence-driven from memory-driven performance; the ledger adds a cost finding (a thinking-class "mini" model costs as much per call as the flagships). No accuracy numbers are available to me, so this meta-review is about decision risk and what to run next.

## Scores (1–10) with one-line justification each
- Novelty: 6 — the leakage ladder for CH reunion is a fresh measurement design; the agent is a standard listwise selector.
- Technical soundness: 5 — the right controls, run too thinly (one model, dev only) to license their conclusions.
- Evaluation rigour: 4 — test ladder is L1/L3-H/L5 for two models, L1/L2-T for the others; L5-P, L6, L3-H2 are 80-query one-model runs; E6/E10e/E15 baselines only on GPT-4.1-mini.
- Clarity (of the design, as reconstructed): 6 — recoverable from flags; metric, `e10_regate` rule, shortlist generation and ground truth are not.
- Impact / significance: 7 — a well-powered result interests CH and LLM-evaluation audiences whichever way the ladder falls.
- Overall: 5 — borderline until the central table exists on test with paired CIs; the $300 plan should reach 6–7.

## Strengths
- Right question, right instruments: ladder, per-channel ablations, both-orders forced choice, closed-book baseline, temporal ladder, prompt variants, a replicate.
- Operational hygiene: served-model audit (0/9,178 mismatches), per-call cost and latency, cheap replay of the visual gate.
- Quotable cost findings: GPT-5.4-mini $0.016–0.023/call vs GPT-4.1-mini $0.004; pointwise 3× cost, 14× wall; open-pool $0.22/query ≈ 11× the shortlist agent.
- Dataset audits (near-duplicates, media integrity, release validation) most CH benchmarks lack.

## Weaknesses
1. **BLOCKER — Unpowered where it matters.** n = 294 gives a 95 % CI of ≈ ±5.7 pts (±11 on 80 dev, ±10 on the 91-query L2-T subset). The decisive rungs — L5-P (`20261024_164053`), L6 (`20261024_165325`), L3-H2 — exist only on dev, only for GPT-5.4; the L5-P test run died with 4 `api_errors` (`20261024_234820`) and the 10-25 restart is unresolved. A dev L1→L6 drop < 10 pts proves nothing; one > 25 pts still needs test confirmation on ≥ 2 models with a paired bootstrap.
2. **BLOCKER — Agent value over trivial baselines unmeasured on any flagship.** The K = 30 shortlist generator and its recall are unknown; `shortlist_shortcuts` (same holder/creator/title stem) may already solve most queries; single-shot rerank E6 exists only for GPT-4.1-mini on 40 dev queries, as do pointwise E10e and the E15 harness. If agent minus (E6 + shortcuts) sits inside the CI, this is a benchmark paper.
3. **MAJOR — Memorisation probes skip the likeliest memorisers.** E8v4 ran on GPT-4.1-mini and GPT-4.1 only, the with-evidence arm only on GPT-4.1-mini; none on GPT-5.4 or GPT-5.4-mini; E5 closed-book is dev-only. The with-evidence prompt is only 76 tokens longer than the no-evidence one (335 vs 260 tok/call), so both arms may measure memory.
4. **MAJOR — Ladder construct validity.** L1→L3 removes 9 % of tokens, L3→L3-H 49; holders may still leak via accession formats, credit lines or image URLs; L2-T was redefined between 10-23 (5/17 queries, 1,730 tok) and 10-24 (32/91, 2,316 tok); `cache_hits=3` on all four L1 test rows suggests duplicate test prompts. Print field sets per level and the `e10_regate` rule.
5. **MAJOR — Reproducibility and generality.** Paid relay throughout; 25–31 % of GPT-5.4 test calls served under an unpinned alias; GPT-5.4 prices estimated; reasoning model without temperature control; one replicate in total (GPT-4.1-mini, dev, L1); eleven non-OpenAI models without ledgers; release blocked by image/text licensing and a Western-canon pool.

## Experiments or artefacts that would change my score
**Build the paper around one claim: the memory-vs-evidence ladder measurement.** Not the agent (risk 2), not the benchmark alone (release blockers, 374 queries, Western canon), not the cost table (a section, not a paper). The ladder is the only claim publishable in either direction — a large L1→L6 drop is a contamination result, a small one a reasoning-over-physical-facts result — and 74 % of spend already sits on it. The agent becomes the reference system, the dataset the vehicle, the cost table the appendix. Costs use ledger per-call rates.

**Next $100** — complete and power the test ladder, close the memory probes:
1. GPT-5.4 L5-P test retry ($3.75) and L6 test ($3.30). *Convinces:* L5 ≈ L5-P inside the CI (dimensions unused) or not; whether L6 falls to the shortcut-heuristic floor.
2. GPT-4.1-mini test L3/L3-H/L5/L5-P/L6 ($4.40), E6 rerank test L1/L5 ($2.80), three extra seeds of L1/L5 test ($6). *Convinces:* seed SD < 2 pts; monotone ladder; agent − E6 > CI.
3. E8v4 both arms on GPT-5.4 and GPT-5.4-mini, with-evidence arm on GPT-4.1 (≈ $19). *Convinces:* flagship no-evidence accuracy > 70 % means a memorised pool that must be fame-stratified.
4. E5 closed-book on test, four models ($4.20). *Convinces:* closed-book correctness as a per-query covariate.
5. GPT-4.1 test L3-H/L5/L5-P/L6 ($16.40); two L1 test replicates each on GPT-5.4 ($5.91) and GPT-4.1 ($6.07). *Convinces:* two flagships agree on ladder shape.
6. Free: paired bootstrap; shortcut heuristics as a baseline row; fame terciles from `commons_views`/`nga_views`; duplicate check; field table per level. ≈ $16 for `api_error` retries.

**Next $300** (cumulative) — generality and cost-matched comparison:
7. GPT-5.4-mini test L3/L5-P/L6 ($14.30), two L1 replicates ($10). *Convinces:* reasoning tokens buy accuracy at L5/L6, or not.
8. E6 rerank on GPT-5.4 test, L1/L5 (≈ $13). *Convinces:* agent beats single-shot rerank on a flagship.
9. Cost-matched self-consistency: 5 × GPT-4.1-mini at L5 ($0.0127/query) vs 1 × GPT-5.4 ($0.0127/call), also at L1 (≈ $10). *Convinces:* the cost finding becomes prescriptive.
10. E16 visual on GPT-5.4 at L5/L6 (≈ $10); E7 pair-verify on GPT-4.1 (≈ $7). *Convinces:* images rescue ≥ 5 pts at L6, or not.
11. E15 closed-pool on GPT-5.4 test L5 (≈ $18); E17 open-pool on 80 dev at L5/L6 (≈ $35). *Convinces:* open-world retrieval from physical facts — the realistic deployment — against the shortlist condition.
12. E8v4 both arms, full test, GPT-5.4 ($14); rerun the failed Gemini 3 Pro / Claude Opus 4.6 L5-P test jobs (≈ $15); two more seeds of GPT-5.4 L5/L5-P/L6 test ($22). ≈ $31 contingency.

**Next $1,000** (cumulative) — the generalisation paper:
13. Three-seed full test ladders, four OpenAI models (≈ $250 net). *Convinces:* every difference carries a seed-aware CI.
14. Non-Western extension (≥ 100 queries: Dunhuang, Chinese albums, Shahnama/muraqqaʿ leaves, sutras), full ladder × 4 models × 3 seeds (≈ $130). *Convinces:* ladder shape transfers, or the title gains a scope qualifier.
15. E17 full test at L5/L6 (≈ $130); E10e pointwise on GPT-5.4 test L1/L5 (≈ $34). *Convinces:* the shortlist is not doing the work.
16. Two non-OpenAI flagships, L1/L5/L6 test, three seeds (≈ $100); hard-negative distractors (same workshop, matched dimensions) at L5, four models (≈ $12). ≈ $44 contingency. A human-expert audit of 100 decisions is time, not API spend, and should happen regardless.

## Token-efficiency / cost critique
- Wasteful: $33.19 on GPT-5.4-mini (70 % of all completion tokens) before knowing whether L1 needs reasoning; E17 at L1 ($0.22/query, 25k tok) at the leakiest level; E16 on GPT-4.1 ($4.70/run) over a 2B-model shortlist; a 505 s failed L5-P test run with zero usable calls.
- Cheap and missing: the whole GPT-4.1-mini test ladder (< $5); closed-book on test (< $5); E8v4 on GPT-5.4 (≈ $2.40/arm); flagship replicates ($5.91 each); every free re-analysis in item 6.

## One idea the authors have not tried
Citation-grounded decisions: require the agent to emit, for every accepted candidate, the field it relied on (`dims`, `medium`, `date`, `title`, `holder`, `creator`) and the quoted value; parse and verify the quote against the record shown. Under L5-P the quoted dimensions are known to be permuted, so an accept that cites dimensions yet lands on the true partner is memory caught in the act, per query. This turns the ladder from an aggregate difference into per-decision attribution for ~20 extra completion tokens per call (≈ +$0.0001 on GPT-4.1-mini, +$0.0002 on GPT-5.4) and yields the evidence trail an ethics reviewer will demand.

## Confidence (1–5) and what I could not assess
3. I have the ledger, flags and campaign log, not the paper, data, metric, regate rule, shortlist generator or any accuracy number; the budget assumes ledger prices hold and non-OpenAI relays price comparably. I have not read the other reviews.
