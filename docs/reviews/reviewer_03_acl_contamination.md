# Reviewer 03 — ACL/EMNLP (LLM evaluation, data contamination & memorisation)

## Summary of the submission as I understand it
The project asks whether LLM/MLLM agents can reassemble dispersed cultural-heritage ensembles from catalogue records, and how much of that skill is memorisation of famous cases. The core method is a listwise agent (`llm_reunion_agent.py`, K=30) evaluated along an information ladder L1→L2-T→L3→L3-H→L5→L5-P→L6 (prompt sizes 1,959→1,064 tok/call). Memorisation is probed by a closed-book baseline (E5), a counterfactual forced choice with evidence withheld and creator masked (E8v4), per-channel ablations and a temporal-ladder report. Splits are dev=80 / test=294. No accuracy numbers are available to me, so every judgement below is conditional.

## Scores (1–10) with one-line justification each
- Novelty: 7 — the task and the per-channel leakage ladder are fresh for NLP; the probes themselves are standard.
- Technical soundness: 5 — well-chosen controls that, as instantiated, do not isolate the channels they are named after.
- Evaluation rigour: 5 — one model carries the variant/replicate/P(yes) evidence; most ablations are dev-only, single-run.
- Clarity (of the design, as reconstructed): 6 — the ladder is legible from flags; field sets per level and E8 item construction are not.
- Impact / significance: 6 — a real digital-humanities problem and a reusable contamination methodology, if the leak accounting holds.
- Overall: 5 — borderline; 7 if artefacts 1–4 below come out as the authors hope.

## Strengths
- Every leakage channel has its own flag (`--withhold-title`, `--holder-scrub v2`, `--mask-creator`, `--dims-permute`, `--withhold-evidence`), and prompt-token fingerprints confirm each changes the input.
- Both-orders presentation in E8 and a served-model audit (0 mismatches / 9,178 calls).
- Prompt variants and a replicate exist (`E10_agent_L1_dev_v1/_v2/_rep1`), so wording and sampling variance can be bounded.
- The closed-book ceiling (E5) is cheap ($0.05–$0.59 per model) and aimed at the right question.

## Weaknesses
1. **Title shown at every level except L6 (BLOCKER).** L6 is `--level L5 --withhold-title` (`E10_agent_L6_dev`), so L5 — the "austere" level — still shows the title; on the title-leak subset (32/80 dev, 91/294 test: 40 %/31 % of queries) that title names the ensemble. The L1→L5 drop therefore excludes the strongest leak. L6 ran once (GPT-5.4, dev).
2. **E8v4 "memory-only" still shows ~260 tokens of item content (MAJOR).** `--withhold-evidence --mask-creator` removes 76 tok/call (335.4→259.5; `E8v4_L1_both_orders` vs `E8v4_noevidence_maskcreator`). What remains (titles, dates, dimensions, holders) is Wikidata/Commons content these models have seen. Unidentifiable both ways: high accuracy may be honest inference from period/medium/height, low accuracy may hide title-keyed memorisation.
3. **E8 item construction undocumented (MAJOR).** 600 calls for `--n 100 --both-orders` implies three items per query; a random counterfactual is solvable by period matching alone. 42–45 completion tok/call means answers are parsed from prose, not logprobs; report parse-failure and order-flip rates.
4. **L2-T is a subset-and-substitution, not an ablation (MAJOR).** L2-T prompts are *longer* than L1 (2,316 vs 1,959 tok/call): the withheld title is replaced by ~350 extra tokens — if a description from the same sources, it names the ensemble. The subset changed between 10-23 (5/17 calls) and 10-24 (32/91); state the leak detector and its recall on oblique titles ("left wing", "predella panel").
5. **Holder scrub and title leak interact (MAJOR).** L3-H removes ~49 tokens over 31 records (1,784→1,735), v2 another 30 — the holder name only. Accession formats, credit lines and `custody_events` also identify holders. With the title still present, the scrub measures nothing on 40 % of queries.
6. **Closed-book ceiling is dev-only and prompt-dependent (MAJOR).** E5 ran on 80 dev queries, never on test; its 137-token prompt must carry title/creator/holder, so on the leak subset it is a copying task.
7. **First-token P(yes) and reasoning models (MAJOR).** E7/E10c (1 completion token, logprob-based) ran only on GPT-4.1-mini, the one model with a logprob-passthrough preflight. For a thinking model the first *visible* token is a post-deliberation verdict, not a calibrated score. GPT-5.4-mini's reasoning also grows as evidence shrinks (475 tok/call at L1 → 694 at L5 → 766 at L2-T; 343 tokens for a 137-token closed-book query): the hidden channel works hardest where the prompt says least.
8. **Position bias and self-consistency unmeasured for the 30-item list (MAJOR if the shortlist is retriever-ordered).** Both-orders exists only for the 2-item E8. One replicate on one model/level cannot bound variance; v1/v2 change output length (105 vs 59 tok/call), i.e. probably selection count, which moves F1 by itself.
9. **Temporal ladder is weak here (MINOR).** Reunion scholarship is decades old; Wikidata timestamps measure editing recency; GPT-5.4 (served `gpt-5.4-2026-03-05`) leaves almost no post-cutoff stratum.
10. **Power (MINOR).** L5-P, L6, L3-H v2, v1/v2 and rep1 are dev-only (n=80), where a 5-point gap is noise and ensembles contribute correlated queries; `E10_agent_L5P_test` failed (rc=1), rerun unconfirmed.

## Experiments or artefacts that would change my score
1. Verbatim prompts (one query, 30 candidates) at every level, plus E5 and E8v4. Convinces me if nothing in the L6/E8v4 prompts resolves to the ensemble via a Wikidata label search.
2. L6 on all four models, dev and test, plus a full-dev "L1 minus title" run. Convinces me if L6 retains ≥ 70 % of L5's score on the leak subset *and* its complement.
3. E8v4 by distractor type, with matched counterfactuals (same period ±15 y, same medium, height within 5 %). Convinces me if matched-distractor accuracy without evidence is within 5 points of 50 %.
4. E5 on test, split leak subset vs complement, and used as a per-query covariate for E10 at L5/L6. Convinces me if the L5–L6 gap is near zero on queries E5 gets wrong.
5. Two shuffled-shortlist permutations at L1 and L5, histogram of selected vs gold positions. Convinces me if selection rate is flat in position and κ between permutations is ≥ 0.7.
6. Three replicates at L1 and L5 on one model; v1/v2 with mean selections per query. Convinces me if every claimed level gap exceeds the replicate-to-replicate gap.
7. GPT-5.4-mini correctness vs reasoning-token count per level. Convinces me if L5/L6 accuracy does not rise with reasoning length.
8. Popularity ladder from the existing `commons_views`/`nga_views` reports: L1–L6 gap per pageview decile. Convinces me if the gap shrinks monotonically with fame.

## Token-efficiency / cost critique
The listwise agent is 54 % of calls but 74 % of cost ($74.5), while the two load-bearing numbers — ceiling (E5, $1.15 total) and floor (L6, $0.89) — were under-run. GPT-5.4-mini's 7–10× completion-token tax makes it as dear as the flagships at L1 ($0.0162/call vs $0.0200/$0.0196) and *dearer* at L5 ($0.0181 vs $0.0130/$0.0127), with no ledger evidence it buys accuracy (GPT-5.4 prices are flagged "estimated"). Cheap and missing: E5 on test (~$0.8 on GPT-4.1), L6 on three more models (~$0.9 dev / ~$3.3 test each), matched-distractor E8v4 (~$2.4), shuffled-order replicates (~$1.6), E8 on the GPT-5.4 family (never run).

## One idea the authors have not tried
Make memorisation a per-item covariate rather than a corpus-level verdict. For every query, one closed-book call: given the title+creator E5 already shows, list all surviving members of the ensemble with holders; overlap with ground truth gives m_q ∈ [0,1] (~$1.5 for all 374 queries on GPT-4.1). Per level, fit a logistic regression of E10 per-query correctness on m_q, pageview decile (`commons_views`/`nga_views`) and leak-subset membership. The intercept at m_q = 0 is evidence-driven skill; the slope is memorisation. This turns "accuracy drops by X along the ladder" into "accuracy at L5 on unmemorised items is Y".

## Confidence (1–5) and what I could not assess
4 on the design critique, 2 on outcomes. I could not see field sets per level, the shortlist generator, the ground-truth source, E8 distractor sampling, `e10_regate`'s rule, or any non-OpenAI run. If the paper already reports leak-subset-stratified results, weaknesses 1, 5 and 6 downgrade to MINOR.
