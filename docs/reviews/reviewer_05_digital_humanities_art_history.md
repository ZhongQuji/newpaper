# Reviewer 05 — Digital Humanities / art history (DH, JCDL, museum-informatics journal)

## Summary of the submission as I understand it

The authors assemble dispersed ensembles (altarpiece panels, album and manuscript leaves, cut scrolls, print series) from Wikidata, Commons, NGA open data, Wikipedia and OA literature, and ask LLM/MLLM agents to pick the true members of a query object's ensemble from a 30-candidate shortlist (dev 80 / test 294). An information ladder (L1 full record → L6 physical facts without title) with one scrub per leakage channel is meant to separate evidence use from memorisation. Side probes: closed-book recall (E5), forced choice (E8v4), pointwise/visual re-scoring (E10e, E10c, E16), a 20-query open-pool run (E17). I have the ledger ($100.07, 9,178 calls) but no accuracy numbers, so every judgement is conditional.

## Scores (1–10) with one-line justification each

- Novelty: 6 — the leakage ladder is useful; reunion from catalogue metadata is an established DH task (Fragmentarium, Broken Books).
- Technical soundness: 5 — careful controls on two undocumented foundations: what "member" means and how the 30 candidates are chosen.
- Evaluation rigour: 5 — many ablations, but the practitioner task (open pool) got 20 queries at L1 on one model, and closed-book never ran on test.
- Clarity (of the design, as reconstructed): 6 — flags reconstruct well; field sets per level, the `e10_regate` rule and the GT source are unknown.
- Impact / significance: 5 — high if L5/L6 and open-pool results hold; if gains sit at L1 on famous ensembles, this measures Wikipedia recall.
- Overall: 5 — conditional; 7 with artefacts 1–4 below.

## Strengths

- One ablation per leakage channel (`--holder-scrub v2`, `--mask-creator`, `--withhold-title`, `--dims-permute 20261024`) — the discipline the "AI rediscovers famous reunions" genre lacks.
- Temporal ladder, near-duplicate, `commons_identity` and media-integrity audits, a release gate, 0 served-model mismatches over 9,178 calls.
- Both-orders forced choice with evidence withheld and creator masked is a clean memory-only probe.
- Prompt-token fingerprints per level are near-identical across models (L1 1,959, L3 1,784, L3-H 1,735, L5 1,208, L6 1,064), so the ladder is actually controlled.

## Weaknesses

1. **[BLOCKER] "Part of" is one reading, not ground truth.** If membership comes from Wikidata P361/P527 (`wikidata_deep`, `membership_evidence` suggest so), it inherits one editor's adoption of one reconstruction. Typical corpus members have incompatible published reconstructions (Sassetta's Borgo San Sepolcro altarpiece, the Laudario of Sant'Agnese leaves), and master / workshop / "circle of" boundaries differ between owning institutions. Returning the majority reconstruction is "correct" against Wikidata and may be wrong. Needed: membership tiers (physically proven / literature consensus / single source / contested) with scores per tier.
2. **[BLOCKER] Published reunions are memorisable and useless to curators.** Anything with a Wikidata item and a Commons category is already reunited in print. The case a provenance researcher brings is the orphan with no published partner — the open-pool setting. E17 ran 20 dev queries, one model, L1 (`20261024_203938_harness_open_L1_xj-gpt-5.4`: $0.22/query, 53 s/query, 2 API errors). At L1 the query record may name the ensemble, so E17 measures lookup, not discovery.
3. **[MAJOR] Shortlist construction is the task.** If candidates are blocked on creator / date / type, recall@30 is the real number and `shortlist_shortcuts` presumably shows how far "same creator ∧ similar height" already goes. Report gold-in-shortlist rate and a zero-token baseline per level.
4. **[MAJOR] Title withholding substituted something longer; creator masking meets Notnamen.** L2-T prompts are 2,316 tok/call against 1,959 at L1 (`20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini`); withholding should shorten. If a Wikidata description replaced the title ("predella panel of the X altarpiece"), the leak moved. Candidate titles presumably still name the ensemble (half a control), and the subset changed between 10-23 (5 / 17 queries) and 10-24 (32 / 91). For "Master of the Osservanza Triptych" the creator string *is* the ensemble name.
5. **[MAJOR] Holder-scrub completeness is unverified.** v2 removes ≈30 tokens per prompt beyond v1 (1,704.6 vs 1,733.8 tok/call) — one token per record, consistent with accession prefixes ("NG", "1939.1."), credit lines ("Samuel H. Kress Collection") or Commons categories. Train a cheap holder classifier on scrubbed records; above chance means L3-H is not holder-blind.
6. **[MAJOR] The discipline's failure modes are not enumerated.** Autograph replicas and workshop copies share creator, medium, subject, date and often dimensions; prints after paintings and dealer pastiches share provenance; pendants are pairs, series are sets, polyptychs are structures; an Otto Ege leaf is "part of" both its manuscript and a modern portfolio. State which relations count and count each class among the errors.
7. **[MINOR] `custody_events` as evidence.** If derived from Wikidata owned-by / donated-by qualifiers, events are sparse and often entered *because* the reunion was published (reverse causation). A curator wants a chain — sale catalogue, lot, Lugt mark, photo-archive negative — with citation and uncertainty per link; none fits in the 60–90 completion tokens per query the ledger shows.
8. **[MINOR] Multilingual records** (Italian, German, French titles and labels) confound title-stem heuristics and language competence with reasoning; report by record language.
9. **[MINOR] Ethics of "reunion".** A membership claim can attach an object to a looted or contested ensemble, or to a dealer's dismemberment a donor would rather not see named; written back to Wikidata it contaminates the next model's training data. Label claims (hypothesis vs established); no write-back without review.

## Experiments or artefacts that would change my score

1. Membership tiers with per-tier accuracy — convinces me if the L1→L5 drop sits in the "contested" tier and L5 is within 5 points of L1 on "physically proven".
2. E5 closed-book on the 294 test queries (the 80-call dev run cost $0.05–0.59), accuracy split recalled / not recalled — convinces me if L5 on the not-recalled subset beats the zero-token baseline by ≥15 points.
3. E17 at L5/L6 on ≥60 queries including ≥20 curator-vetted orphans — convinces me if precision is reported with explicit abstention on the orphans.
4. Recall@30 and the `shortlist_shortcuts` table — convinces me if the agent beats the best heuristic by ≥10 points at L3-H.
5. Error typology (derivative / pendant / pastiche share of false positives) — convinces me if reported rather than folded into "errors".
6. Holder-classifier audit on L3-H v2 — convinces me at chance.
7. One full prompt and output per failure class, annotated by an art historian — convinces me if stated reasons cite shown fields.

## Token-efficiency / cost critique

Wasteful: E16 spends $4.70 per run (GPT-4.1, 160 calls) re-scoring the top-8 of a 2B local model's shortlist, whose recall caps the result. The L1 "v2 inputs" variant adds 1.7× tokens (3,391/call); if the added fields come from `literature_enrich` / `oa_fulltext`, the prompt contains the article that published the reunion. E7's `--balance-source` hints that image source (NGA studio photography vs Commons uploads) is a confound; a same-source split costs nothing. Cheap and missing: closed-book on test; a zero-token metadata baseline; fame stratification from view counts already computed; a GT-provenance column per ensemble. $4.40 on 20 open-pool queries against $74.5 on the listwise family is the wrong allocation for practitioners.

## One idea the authors have not tried

Build a *derivative-distractor* set from Wikidata: for each true member, pull items linked by P144 "based on", P4969 "derivative work", "after X" Commons captions and workshop replicas (`wikidata_deep` already walks these edges), and insert one per query into the shortlist with its real record. Score the rate at which the agent prefers the derivative over the original, and whether its stated reason names a field that actually distinguishes them (support, dimensions, date, medium). This is the mistake connoisseurship exists to avoid and the one catalogue metadata is worst at exposing; it also turns "false positive" from a count into a typology (replica, print, pendant, pastiche) a curator can read.

## Confidence (1–5) and what I could not assess

4 — I know the reconstruction literature and cataloguing practice. I could not assess field sets per level, the GT source, the shortlist builder, the `e10_regate` rule, the content of `custody_events`, or any accuracy figure.
