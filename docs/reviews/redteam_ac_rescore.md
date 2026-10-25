# Red-team AC re-score — the redesign (`docs/04`) against the round-1 blockers (`docs/03`)

Read in order: `docs/03` → `docs/04` → `sim/README.md` → `docs/01`; cross-checked against `sim/reunion_sim.py`, `sim/results/RUNLOG.md`, `policies_raw.csv`, `POWER.md`. No accuracy number exists anywhere; every quality claim is conditional or simulated and is scored as such.

## A. Blocker-by-blocker

- **B1 under-powered rungs — (ii), trending (iv).** §4.2/§4.5 promise MDD reporting and ≥3 test seeds but add no queries; M7 relabels the rungs so the existing L2-T/L3/L3-H/L5 test runs fall off the ladder; the mechanisms' own expected effects (+0.03–0.06 F1 [sim]) sit below the test MDD (0.07–0.09, `POWER.md`).
- **B2 evaluation unit — (i) on paper.** §4.2 + Stage 4 (pairwise F1 / B-cubed / ARI, ensemble bootstrap) is the right free fix; it silently requires an ensemble-disjoint dev/test split, which no document states.
- **B3 shortlist black box — (ii), partly (iv).** §4.4 promises recall@K and the shortcut row (free, not done); M4′/M6 then make the undocumented retriever's *calibrated scores* load-bearing, with two new thresholds (0.02, τ=0.05) tuned on 80 dev queries.
- **B4 non-nested ladder, title at L5 — (i) in design, (ii) in practice.** The M7 table is right, but M5/§3 price and simulate Stage 1 with the *old* L5 (1,208 tok, title shown), and the schema keeps image-URL filenames to L3 and "iconography keywords" at L5 — both word channels.
- **B5 probes skipped the likeliest memorisers — (ii).** M10 specifies the right probe (ids-only, period-matched, both orders) and has not run it on GPT-5.4/5.4-mini; "ids only" is itself incoherent (B.6).
- **B6 `e10_regate` — (ii), prospective only.** M15 freezes the rule for future runs; the rule applied to all 65 existing runs is still "unknown" (§1) and the pre/post-regate report (docs/03 action 4) is absent.
- **B6b duplicate test prompts — (iii) ignored.** Not mentioned.
- **B7 reproducibility — (iii) largely ignored.** Seeds (§4.5) help; nothing on the unpinned `gpt-5.4` alias split, the 4.4× relay (every §3 dollar is a relay-fitted absolute), "estimated" GPT-5.4 prices or temperature control.

## B. New weaknesses introduced by the redesign

1. **BLOCKER — The headline numbers contradict the authors' own simulation.** §3 claims $0.0075–0.0115/query (−40…−63 %) and "quality equal or higher in 87–95 % of worlds". (a) The price assumes flagship calls on ≈40 % of queries (§2.2); the sim's evidence cascade escalates on 91–99 % (band 0.45: `strong_call_frac=0.96`, ≈9.5 candidates) and costs $0.0128 before M9 — all-in $0.014–0.018, i.e. −10…−31 %. (b) The §3 diagram's 0.1–0.9 band *is* the band-0.4 setting that §2.2 and sim README §3b say loses 0.034 F1; the settings that do not lose are priced outside the quoted range. (c) "87–95 %" is the share of worlds in which *some* per-world-chosen policy beats today's design (README headline 1) — an oracle statistic, not a property of the fixed pipeline. (d) In the base world M5 is Pareto-dominated by the plain cascade M4 (F1 0.671 @ 1.28¢ vs 0.687 @ 1.12¢, RUNLOG L1).

2. **BLOCKER — M5 inverts its own contamination story and makes the rung a dependent variable.** `llm_evidence` gives remembered queries d′=4.0 at every rung for every model; the mini's non-memorised L5 d′ is 0.975. Stage 1's confident decisions are therefore the memorised ones and the evidence-driven ones escalate: "decided from physical facts" ≈ "decided from memory", and the per-query "needed the title" fraction measures 1−p_mem. The same assumption says memory survives title removal, contradicting M7's premise that the title is where memorisation lives — two incompatible memory models, neither tested (one $2 E8 arm with L5-only evidence would). Independently, the rung of decision is chosen by the system's confidence, so v2's "accuracy at L5" is accuracy on self-selected candidates — a descriptive statistic that must never be pooled with the §4.1 ladder (§5 bullet 3 half-admits this). And as priced, Stage 1 is the *old* L5: the only L5 with a real token count (1,208) and a sim d′ (1.3) still shows the title, so either the cheap stage leaks on the 31–40 % title-leak subset or every [real] number attached to M5 describes a prompt that no longer exists.

3. **MAJOR — The cascade's engine, per-candidate p̂, is unimplemented and conflicts with M2.** An ids-only listwise answer has no posterior; logprob P(yes) is documented only for GPT-4.1-mini (`family` note), not the GPT-5.4 family; verbalised scores cost ≈120 completion tokens at 4–6× prompt price, more than M2's 8 % saving; §5's "two-sample agreement proxy" doubles Stage 1. The sim gets p̂ free and calibrated.

4. **MAJOR — Validation below its own resolution.** Every §2 validation runs on dev (MDD 15–18 points) for expected effects of 3–6 points. M6's "never loses more than 0.01" and M1's "L5 within the CI of L1 ⇒ production prompt" are non-inferiority claims needing a pre-specified margin and thousands of paired queries; as written M1 turns a ±10-point CI into a deployment decision.

5. **MAJOR — M9 measures compliance, not causation.** A model told to cite shown fields does so whatever drove the decision; the literal checker penalises unit normalisation and paraphrase and rewards terse answers; the metric is one-sided (unshown ⇒ leak, shown ⇒ nothing). Under the cascade "shown" is undefined (L5 at Stage 1, L1 at Stage 2): verify against L1 and the leak rate is zero by construction. R10's version — cite under L5-P, where a dims-citing accept that still lands on the true partner is memory caught in the act — was diagnostic; M9 dropped that lever and adds $0.001–0.005/query.

6. **MAJOR — The un-mixing estimator is not identifiable with a noisy probe.** One equation, three unknowns per rung. Under correct-in-both-orders scoring a chance-level model is tagged "memorised" 25 % of the time, so the evidence stratum contains memorised queries at an unknown rate and acc_evid has no bound; E8 answers are parsed from prose (R03). "Ids only" is either chance-level (Q-ids, accession numbers) or leaky (any text): a forced choice cannot be evidence-free — closed-book naming (E5 on test) is the coherent instrument. Strata are model-specific, so cross-model ladders compare different query sets, and the top fame tercile leaves ~10–30 dev queries in the evidence stratum. Report strata; drop the formula.

7. **MAJOR — Pre-registration after exposure, with eight new knobs.** L1/L2-T/L3-H/L5 test runs already exist for 2–4 models, so M15 registers an analysis of seen data; disclose what has been seen. The redesign adds band, prune threshold, τ, K, abstention margin, memorised criterion, fame cut-points and clustering rule, all set on the same 80 dev queries — B6's one hidden degree of freedom becomes eight unless each value is in the file. A ladder "publishable either way" cannot register a direction; register the MDD and equivalence margins.

8. **MAJOR — Scope drift and orphaned data.** docs/03 §4 says build the paper around the ladder; docs/04 spends §2.2–2.3, §2.7–2.8 and §3 on a four-stage system with zero real runs, reopening R02/R08 in a new form. Because M7 relabels the rungs, the docs/03 §6 "$100" buys old-schema rungs (L5-P, `--withhold-title` L6) while `STATUS.md` prices the v2 test ladder at ≈$40 more: choose the schema before spending or pay twice.

9. **MINOR — Opposed mechanisms and split leakage.** M4′/M6 prune low-score candidates — the orphans' members that M12 says "need the flagship" — and lower the ceiling from recall@30 to recall@16 (B3). Stage 4 closure propagates decisions across queries, hence across splits if ensembles straddle them; no document says they do not.

10. **MINOR — Framing.** Standing on their own: M1–M4, M6–M11, M15–M16 (each a round-1 request or a standard technique: FrugalGPT cascades, selective prediction, attribution, pre-registration). Existing only for the framing: M5 (dominated by M4; justified by fusing two slogans), M12 (19/432 sim wins; kept for 按需分配), M13 (a reviewer concern re-badged, no source or ground truth for the $130 stratum), M14 (no sim, no price, no experiment). Eight tradition headers in a method section read as decoration and invite an R05/R09 objection about ornament; keep one epigraph.

## C. Re-scores (S1 / S2)

Round-1 means: Nov 5.8 · Sound 5.1 · Eval 4.3 · Clar 5.9 · Impact 6.1 · Overall 4.7.

**S1 — nothing new is run; `docs/04` is the method section.**

| axis | S1 | justification |
| --- | ---: | --- |
| Novelty | 6 | nested ladder + per-decision grounding + stratification sharpen the measurement; the cascade is FrugalGPT. |
| Technical soundness | 4 | internal contradictions (B.1–B.2), two memory models, unidentified estimator, no mechanism run. |
| Evaluation rigour | 3 | all quality numbers simulated; the v2 schema orphans the old rungs, so less usable evidence than round 1; B1/B6b/B7 untouched. |
| Clarity | 5 | good [real]/[sim] tagging, undone by eight headers, M4/M5/M12/M14 overlap and three prices for one pipeline. |
| Impact | 6 | the question is unchanged; a protocol without data is a promise. |
| **Overall** | **4** | a design document, not a method section; weaker than round 1 on soundness. |

**S2 — the `docs/03` §6 list is run and comes out as hoped (monotone test ladder with CIs, β>0, small seed SD, probes stratify, recall@30 and regate disclosed, duplicates resolved).**

| axis | S2 | justification |
| --- | ---: | --- |
| Novelty | 7 | first powered, nested, per-channel leakage ladder for catalogue-level reunion with probes on the likeliest memorisers. |
| Technical soundness | 6 | the ladder measurement becomes sound (ensemble unit, disclosed regate, registered test analysis); system claims stay simulated and move to an appendix. |
| Evaluation rigour | 6 | test ladder on ≥2 models with seeds, ceilings and floors in the table; still n=294 (MDD 7–9), one Western pool, old-schema rungs unless ≈$40 more is spent. |
| Clarity | 6 | the list does not fix the writing; 7 if the framing shrinks to an epigraph and M5/M12/M14 leave the main text. |
| Impact | 7 | publishable in either direction with real CIs; the grounding and stratification protocol is reusable. |
| **Overall** | **6** | weak accept as a measurement paper; the frugal system is future work until the $5 cascade run exists. |

## D. Must-do before resubmission

Build the paper around the ladder measurement and demote the v2 system to an appendix unless it is actually run. Freeze the nested schema first — a published field table that names the image-URL and iconography fields — then run that schema on test for ≥2 models × ≥2 seeds (≈$40 by your own predictor) with ensemble-level bootstrap, recall@K, the shortcut-heuristic row, the served-as split per run, and the 2–3 duplicate test prompts removed. Commit a pre-registration that states the `e10_regate` rule with pre/post-regate numbers for all existing runs, discloses which test comparisons have already been seen, lists a value for every new tunable, and registers the MDD and an equivalence margin rather than a direction. Run E8 on GPT-5.4 and GPT-5.4-mini as closed-book naming plus a period-matched counterfactual, report the probe's chance-level false-positive rate, and stratify every ladder plot by that outcome and by fame tercile instead of backing out acc_evid by formula. State which memory model you hold (word-keyed or record-keyed) and test it with one E8 arm at L5-only evidence. Re-price §3 with the simulation's own 0.96 escalation fraction or a measured one, set the §3 band to the configuration §2.2 recommends, delete the oracle "87–95 % of worlds" sentence, and either run the $5 paired mini@L5→flagship@L1 dev cascade or remove the M4–M6/M11–M12 quality claims from the main text. Implement M9 under L5-P so that it is diagnostic, and confirm the dev/test split is ensemble-disjoint.
