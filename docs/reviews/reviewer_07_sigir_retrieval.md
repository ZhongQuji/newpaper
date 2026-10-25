# Reviewer 07 — SIGIR/WSDM/KDD persona (information retrieval & entity resolution)

## Summary of the submission as I understand it
The task is query-centric "digital reunion": given one museum record, select from a K=30 shortlist the records of the other surviving members of its original ensemble (altarpiece, album, manuscript). The main method (E10, `llm_reunion_agent.py`) is one listwise LLM call over the 30 candidates, run at seven information levels (L1 → L6) whose per-channel ablations (holder scrub, creator mask, title withheld, dimensions permuted) are meant to separate evidence use from memorisation. Alternatives are a pointwise reranker (E10e), MLLM visual gates (E10c/E16) and a tool-using harness (E15/E17); four OpenAI-family models have full ledgers (9,178 calls, $100). From an IR/ER standpoint this is two-stage entity resolution (blocking → matching) over 80 dev / 294 test queries, but the first stage and every effectiveness number are absent from what I was given, so all judgements below are conditional.

## Scores (1–10) with one-line justification each
- Novelty: 6 — the information ladder with per-channel leakage ablations is a genuinely good protocol; the matcher itself (listwise LLM rerank of a fixed shortlist) is standard RankGPT-style practice.
- Technical soundness: 5 — matcher is fine; the first stage is unspecified and the evaluation unit (independent queries) is wrong for an equivalence relation.
- Evaluation rigour: 4 — no recall ceiling, no shuffled-order control, no classic ER baselines, no cluster-level metric, no CIs clustered by ensemble; the L2-T subset was redefined mid-campaign.
- Clarity (of the design, as reconstructed): 6 — flags and levels are legible from the ledger; field sets per level and the `e10_regate` acceptance rule are not.
- Impact / significance: 6 — a real GLAM problem and a reusable benchmark if retriever, gold and shortlists are released.
- Overall: 5 — borderline / weak reject pending the artefacts listed below.

## Strengths
- Per-channel leakage controls (holder, creator, title, dimensions) plus both-order forced choice (E8 `--both-orders`) and a served-model audit (0 mismatches) — more careful than most LLM-ranking papers.
- The prompt-token fingerprint makes the ladder monotone and auditable: 1,959 → 1,784 → 1,735 → 1,208 → 1,064 tok/call, identical across models.
- Prompt-variant and replicate runs exist at L1 (`E10_agent_L1_dev_v1`, `_v2`, `_rep1`), so prompt sensitivity and sampling variance can be reported rather than hand-waved.
- `e10_shortlist_controls` / `shortlist_shortcuts` show the authors already suspect trivial heuristics solve part of the shortlist.
- Open-data provenance (Wikidata, Commons, NGA) with near-duplicate and media-integrity audits before release.

## Weaknesses
1. **BLOCKER** — The first-stage retriever is a black box. No ledger row says how the K=30 shortlist is built (lexical? dense? metadata blocking? gold injection?), and recall@30 is not reported. If the gold partner is absent the agent cannot win, so every E10 number is conditional on an unknown ceiling. Worse: if the shortlist is built once from full records (titles, holders) and reused at L5/L6, the leak the ladder removes from the prompt re-enters through the candidate set, and the L6 "floor" is not a floor.
2. **MAJOR** — Position bias is uncontrolled in the main method. E8 has `--both-orders`; no E10 row carries a shuffle/seed flag analogous to `--dims-permute 20261024`. If candidates appear in retriever-score order, LLM primacy bias and retriever quality are confounded.
3. **MAJOR** — Wrong evaluation unit. "Same ensemble" is an equivalence relation. Scoring 294 member-queries independently over-weights large polyptychs, ignores transitivity, and hides inconsistent predictions (A→B, B→C, C↛A). No pairwise/B-cubed/ARI/exact-cluster metric and no transitive-closure step is visible.
4. **MAJOR** — No classic ER baselines. Blocking on creator/date/medium plus a Fellegi–Sunter or logistic matcher over string and dimension similarities; Dedupe; Magellan; a DITTO-style fine-tuned PLM matcher; a dense-embedding threshold. These cost ≈ $0/query and may match the LLM at L5, where the evidence is essentially numeric.
5. **MAJOR** — Hard-negative composition unknown. Same-workshop panels, other series by the same master with identical predella heights, replicas/versions and near-duplicates (a `near_duplicates` report exists) are what make this task hard; their count per shortlist is not reported.
6. **MAJOR** — The pointwise-vs-listwise comparison is confounded by implementation. E10e = 29.3 requests/query × 246 prompt tokens, 1 completion token (P(yes)), executed sequentially at 2.7 s/request; the "14× wall time" is serialisation and the 3× cost is the query record re-sent 29 times (135/2,344 cache hits). Pairwise and setwise variants are absent.
7. **MINOR** — L2-T was redefined mid-campaign: 10-23 rows have 5 dev / 17 test queries at 1,730/1,930 tok/call; 10-24 rows have 32/91 at 2,316/2,471. Which definition is in the paper, and were the earlier runs dropped post hoc?
8. **MINOR** — Gold from Wikidata `part of` (inferred) is incomplete; some "false positives" are probably unlabelled true links.

## Experiments or artefacts that would change my score
1. Retriever card: method, fields used per level, recall@{5,10,20,30} on dev and test per level, rank-of-gold histogram, and confirmation the retriever only sees the fields of the current level. *Convince me:* recall@30 reported for every level, and the matcher's conditional and unconditional F1 both shown.
2. Shuffled-order replicate per model on dev ($0.33–$1.60 each): selection rate by shortlist position and ΔF1. *Convince me:* |ΔF1| < 2 points and a flat position curve.
3. Cluster-level evaluation: union all predicted links on test, take connected components, report pairwise P/R/F1, B-cubed, ARI, exact-cluster match, with bootstrap CIs resampled by ensemble. *Convince me:* B-cubed F1 within 5 points of per-query F1.
4. Baseline table: random-from-shortlist, the `shortlist_shortcuts` heuristics (same holder / same creator / title stem), FS or logistic matcher with ±2 cm dimension tolerance, DITTO-style matcher trained on dev pairs. *Convince me:* LLM at L5 beats the dimension-rule baseline by > 10 F1 points; otherwise the claim must change.
5. Hard-negative audit: per shortlist, count same-creator, same-series, replica and near-duplicate candidates; F1 stratified by stratum. *Convince me:* same-creator precision reported separately and not collapsing.
6. P–R curve from E10e P(yes) against the listwise single operating point, plus a setwise run (3 groups of 10). *Convince me:* comparison at matched precision, not at each method's default threshold.
7. Precision audit: hand-label 100 predicted-not-gold test pairs. *Convince me:* < 20 % turn out to be true links.
8. The L2-T definition history and the fate of the 10-23 runs.

## Token-efficiency / cost critique
- Listwise is already the cheap road: $0.004/query (GPT-4.1-mini) to $0.020 (GPT-4.1 / GPT-5.4). E10e burns 7.2k tokens/query re-sending the query 29 times; place query + instructions first and use prompt caching, or score candidates setwise in batches of 10 (~3 calls, ~2.5k tokens/query).
- Wasteful: fixed K=30 at every level. Prompt tokens are roughly linear in K (≈ 30 tok/candidate at L6, ≈ 60 at L1); if recall@10 ≈ recall@30, K=10 halves cost with no loss.
- Wasteful: E16 is 12 % of the budget ($12.4) to re-score a 2B model's top-8 on 80 dev queries for two models, with that shortlist's recall@8 unknown.
- Cheap-and-missing: shuffled-order run; random-selection and heuristic baselines (free); classic ER baselines (CPU only); a dense-retriever recall curve. Everything in this list costs < $5 on this relay.

## One idea the authors have not tried
Level-consistent blocking + transitive-closure decoding. Build the shortlist with a blocker that sees only the current level's fields (at L5: same medium ∧ |Δheight| ≤ 2 cm or |Δwidth| ≤ 2 cm ∧ overlapping date range), so the recall ceiling is honest per level. Then, instead of 294 independent set decisions, obtain pointwise P(yes) for each (query, candidate) pair (E10e-style, batched setwise to cut cost), symmetrise by averaging P(a,b) and P(b,a), and run correlation clustering or average-linkage agglomerative clustering with a threshold tuned on dev to emit ensembles directly. Report B-cubed and pairwise F1 against gold ensembles. This reuses existing scripts, removes order effects by construction, enforces transitivity, and delivers the actual object of interest — reassembled ensembles — rather than per-query lists.

## Confidence (1–5) and what I could not assess
Confidence 4 on the methodological critique, 2 on effectiveness: I saw no accuracy numbers, no per-level field definitions, no retriever description, no gold-source specification, no shortlist files, and no non-OpenAI results. If the retriever card (item 1) and cluster-level metrics (item 3) exist in the paper and hold up, my Overall rises to 7.
