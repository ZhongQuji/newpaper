# Reviewer 05 — Digital Humanities / art history (DH, JCDL, museum-informatics journal)

## Summary of the submission as I understand it

The authors assemble a corpus of dispersed ensembles (altarpiece panels, album and manuscript leaves, cut scrolls, print series) from Wikidata, Wikimedia Commons, NGA open data, Wikipedia and OA literature, and ask LLM/MLLM agents to pick the true members of a query object's ensemble from a 30-candidate shortlist (dev 80 / test 294 queries). The central manipulation is an information ladder (L1 full record → L6 physical facts without title) with one scrub per leakage channel (holder, creator, title, permuted dimensions) meant to separate evidence use from memorisation. Side probes cover closed-book recall (E5), counterfactual forced choice (E8v4), pointwise and visual re-scoring (E10e, E10c, E16) and a 20-query open-pool deep-research run (E17). I have the run ledger ($100.07, 9,178 calls) but no accuracy numbers, so every judgement below is conditional.

## Scores (1–10) with one-line justification each

- Novelty: 6 — the leakage ladder is genuinely useful for our field; "reunion from catalogue metadata" itself is an established DH task (Fragmentarium, Broken Books, altarpiece-reconstruction projects) and Wikidata-derived membership is not new.
- Technical soundness: 5 — careful controls on top of two undocumented foundations: what "member" means and how the 30 candidates are chosen.
- Evaluation rigour: 5 — many ablations, but the practitioner task (open pool, unpublished case) got 20 queries at L1 on one model, and the closed-book probe never ran on test.
- Clarity (of the design, as reconstructed): 6 — flags reconstruct well; field sets per level, the `e10_regate` acceptance rule and the GT source are unknown.
- Impact / significance: 5 — high if L5/L6 and open-pool results hold; if gains concentrate at L1 on Wikipedia-famous ensembles, this measures Wikipedia recall.
- Overall: 5 — conditional; moves to 7 with artefacts 1–4 below.

## Strengths

- One ablation per leakage channel (`--holder-scrub v2`, `--mask-creator`, `--withhold-title`, `--dims-permute 20261024`) is the discipline the "AI rediscovers famous reunions" genre lacks.
- Temporal ladder, near-duplicate, `commons_identity` and media-integrity audits plus a release-validation gate; served-model audit with 0 mismatches over 9,178 calls.
- Both-orders forced choice with evidence withheld and creator masked is a clean memory-only probe.
- Prompt-token fingerprints per level are identical across the four models (1,959 / 1,784 / 1,735 / 1,208 / 1,064), so the ladder is actually controlled.
- The expensive question was asked at least once: E17 open pool exists.

## Weaknesses

1. **[BLOCKER] "Part of" is one reading, not ground truth.** If membership comes from Wikidata P361/P527 (the `wikidata_deep` and `membership_evidence` reports suggest so), it inherits one editor's adoption of one reconstruction. For ensembles typical of such a corpus the literature holds incompatible reconstructions (Sassetta's Borgo San Sepolcro altarpiece has been re-laid out repeatedly; Ugolino di Nerio's Santa Croce polyptych; the Laudario of Sant'Agnese leaves; Mughal albums that were themselves re-bound), and master / workshop / "circle of" boundaries differ between owning institutions. A model that returns the majority published reconstruction is "correct" against Wikidata and may be wrong. Needed: per-ensemble membership tiers (physically proven / literature consensus / single source / contested) and scores per tier.
2. **[BLOCKER] Published reunions are memorisable and useless to curators.** Anything with a Wikidata item and a Commons category is, by construction, already reunited in print. The case a provenance researcher brings is the orphan panel with no published partner, i.e. the open-pool setting. E17 ran 20 dev queries on one model at L1 (`20261024_203938_harness_open_L1_xj-gpt-5.4`: $0.22/query, 53 s/query, 2 API errors). At L1 the query record may literally name the ensemble, so E17 as run measures lookup, not discovery. `commons_views` / `nga_views` give you a fame covariate; nothing in the grid is stratified by it.
3. **[MAJOR] Shortlist construction is the task.** If candidates are blocked on creator / date / object type, recall@30 of true members is the real number and the `shortlist_shortcuts` report presumably shows how far "same creator ∧ similar height" already goes. Report gold-in-shortlist rate and a zero-token baseline per level.
4. **[MAJOR] Title withholding substituted something longer.** L2-T prompts are 2,316 tok/call against 1,959 at L1 (`20261024_113936_e10_agent_L2-T_xj-gpt-4.1-mini`); withholding a title should shorten the prompt. If a Wikidata description or depicts list replaced it ("predella panel of the X altarpiece" is a typical description), the leak moved rather than closed. Candidate titles presumably still name the ensemble, so withholding only the query title is half a control. The subset also changed between 10-23 (5 dev / 17 test) and 10-24 (32 / 91): state which definition is reported.
5. **[MAJOR] Creator mask versus Notnamen.** "Master of the Osservanza Triptych", "Master of the Saint Bartholomew Altarpiece": the creator string *is* the ensemble name, and anonymous masters are over-represented among dismembered Trecento/Quattrocento works. Masking creator but not title (or the reverse) still leaks.
6. **[MAJOR] Holder-scrub completeness is unverified.** v2 removes ≈30 tokens per prompt beyond v1 (1,704.6 vs 1,733.8 tok/call) — about one token per record, consistent with accession prefixes ("NG", "1939.1.", "Inv. 1890 n."), credit lines ("Samuel H. Kress Collection"), Commons category strings or simply the cataloguing language. Train a cheap holder classifier on scrubbed records; if it beats chance, L3-H is not holder-blind.
7. **[MAJOR] The failure modes that define the discipline are not enumerated.** Autograph replicas and workshop copies share creator, medium, subject, date and often dimensions; prints after paintings and nineteenth-century dealer pastiches share provenance; pendants are pairs, series (Months, Apostles) are sets, polyptychs are structures; a leaf in an Otto Ege portfolio is "part of" both its manuscript and a modern album; a panel sawn in two is one object or two members; re-used panels belonged to two ensembles over time. Which relations count must be stated and each class counted among the errors.
8. **[MINOR] `custody_events` as evidence.** If events derive from Wikidata owned-by / donated-by qualifiers they are sparse and often entered *because* the reunion was published (reverse causation). A curator wants a chain — sale catalogue, lot, Lugt mark, photo-archive negative — each with a citation and an uncertainty flag; none fits in the 60–90 completion tokens per query the ledger shows.
9. **[MINOR] Multilingual records.** Italian, German and French titles and labels confound "title stem" heuristics and model language competence with reasoning; report by record language.
10. **[MINOR] Ethics of "reunion".** An automated membership claim can attach an object to a looted or contested ensemble, a restitution file, or a dealer's dismemberment a donor would rather not see named; written back to Wikidata it also contaminates the next model's training data. Say how claims are labelled (hypothesis vs established) and that nothing is written back without review.

## Experiments or artefacts that would change my score

1. Membership-confidence tiers with per-tier accuracy — convinces me if the L1→L5 drop is concentrated in the "contested" tier and L5 is within 5 points of L1 on the "physically proven" tier.
2. E5 closed-book on the 294 test queries (the 80-call dev run cost $0.05–0.59) and accuracy split by recalled / not recalled — convinces me if L5 accuracy on the not-recalled subset exceeds the zero-token baseline by ≥15 points.
3. E17 open pool at L5/L6 on ≥60 queries including ≥20 curator-vetted orphans with no Wikidata partner — convinces me if precision is reported with an explicit abstention on the orphans.
4. Recall@30 of the shortlist and the `shortlist_shortcuts` table — convinces me if the agent beats the best heuristic by ≥10 points at L3-H.
5. Error typology: fraction of false positives that are known derivatives, pendants or pastiches — convinces me if it is reported rather than folded into "errors".
6. Holder-classifier audit on L3-H v2 records — convinces me if holder prediction is at chance.
7. One full prompt and output per failure class, annotated by an art historian — convinces me if the agent's stated reasons use shown fields.

## Token-efficiency / cost critique

Wasteful: E16 spends $4.70 per run (GPT-4.1, 160 calls, 3.0k tok/call) re-scoring the top-8 of a 2B local model's shortlist, whose recall caps the result. The L1 "v2 inputs" variant adds 1.7× tokens (3,391/call); if the added fields come from `literature_enrich` / `oa_fulltext` / `fact_cards`, the prompt contains the article that published the reunion. E7's `--balance-source` hints that image source (NGA studio photography vs Commons uploads) is a confound; a same-source split costs nothing. Cheap and missing: closed-book on test; a zero-token metadata baseline; fame stratification from view counts already computed; a GT-provenance column per ensemble. Spending $4.40 on 20 open-pool queries while the listwise family absorbed $74.5 is the wrong allocation for a practitioner audience.

## One idea the authors have not tried

Build a *derivative-distractor* set from Wikidata: for each true member, pull items linked by P144 "based on", P4969 "derivative work", "after X" Commons captions and workshop replicas (`wikidata_deep` already walks these edges), and insert one per query into the shortlist with its real record. Score two things: the rate at which the agent prefers the derivative over the original, and whether its stated reason names a field that actually distinguishes them (support, dimensions, date, medium). This is the mistake connoisseurship exists to avoid and the one catalogue metadata is worst at exposing; it also turns "false positive" from a count into a typology (replica, print, pendant, pastiche) a curator can read.

## Confidence (1–5) and what I could not assess

4 — I know the reconstruction literature and cataloguing practice well. I could not assess the field sets per level, the GT source, the shortlist builder, the `e10_regate` acceptance rule, the content of `custody_events`, or any accuracy figure; none is in the material.
