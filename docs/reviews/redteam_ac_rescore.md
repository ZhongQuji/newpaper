# Red-team AC re-score — `docs/04` redesign against the `docs/03` blockers

Cross-checked against `sim/reunion_sim.py`, `RUNLOG.md`, `policies_raw.csv`, `POWER.md`. No accuracy number exists; every quality claim is conditional or simulated.

## A. Blocker-by-blocker

- **B1 under-powered rungs — (ii), trending (iv).** §4.2/§4.5 promise MDD reporting and ≥3 test seeds but add no queries; M7 relabels the rungs, so existing L2-T/L3/L3-H/L5 test runs fall off the ladder; expected effects (+0.03–0.06 F1 [sim]) sit below the test MDD (0.07–0.09).
- **B2 evaluation unit — (i) on paper.** §4.2 + Stage 4 (pairwise F1 / B-cubed / ARI, ensemble bootstrap); silently requires an ensemble-disjoint dev/test split, stated nowhere.
- **B3 shortlist black box — (ii), partly (iv).** §4.4 promises recall@K and the shortcut row (undone); M4′/M6 make the undocumented retriever's *calibrated scores* load-bearing (two new dev-tuned thresholds).
- **B4 non-nested ladder, title at L5 — (i) in design, (ii) in practice.** The M7 table is right, but M5/§3 price and simulate Stage 1 with the *old* L5 (1,208 tok, title shown); image-URL filenames survive to L3 and "iconography keywords" to L5.
- **B5 probes skipped the likeliest memorisers — (ii).** M10 specifies the right probe, unrun on GPT-5.4/5.4-mini; "ids only" is itself incoherent (B.6).
- **B6 `e10_regate` — (ii), prospective only.** M15 freezes the rule for future runs; the rule behind the 65 existing runs stays "unknown" (§1); no pre/post-regate report (docs/03 action 4).
- **B6b duplicate test prompts — (iii) ignored.**
- **B7 reproducibility — (iii) largely ignored.** Seeds (§4.5) help; nothing on the unpinned `gpt-5.4` alias split, the 4.4× relay (every §3 dollar is a relay absolute) or "estimated" GPT-5.4 prices.

## B. New weaknesses introduced by the redesign

1. **BLOCKER — The headline numbers contradict the authors' own simulation.** §3: $0.0075–0.0115/query (−40…−63 %), quality "equal or higher in 87–95 % of worlds". (a) Pricing assumes flagship calls on ≈40 % of queries (§2.2); the sim escalates 91–99 % (band 0.45: `strong_call_frac=0.96`, ≈9.5 candidates) at $0.0128 before M9 — all-in $0.014–0.018, −10…−31 %. (b) The §3 diagram's 0.1–0.9 band *is* the band-0.4 setting §2.2 and README §3b say loses 0.034 F1; non-losing settings fall outside the quoted range. (c) "87–95 %" is the share of worlds where *some* per-world-chosen policy beats today's design (README headline 1) — an oracle statistic, not a property of the fixed pipeline. (d) In the base world M5 is Pareto-dominated by the plain cascade M4 (F1 0.671 @ 1.28¢ vs 0.687 @ 1.12¢).

2. **BLOCKER — M5 inverts its own contamination story and makes the rung a dependent variable.** `llm_evidence` gives remembered queries d′=4.0 at every rung for every model, against 0.975 for the mini's non-memorised L5 evidence. Stage 1 therefore settles memorised queries and escalates evidence-driven ones: "decided from physical facts" ≈ "decided from memory", and the "needed the title" fraction measures 1−p_mem. The same assumption says memory survives title removal, contradicting M7's premise that the title is where memorisation lives; neither model is tested. Since the system's confidence picks the rung, v2's "accuracy at L5" is accuracy on self-selected candidates and cannot be pooled with the §4.1 ladder. As priced, Stage 1 is the old L5 (the only L5 with real tokens and a sim d′), which still shows the title: either the cheap stage leaks on the 31–40 % title-leak subset or every [real] number behind M5 describes a prompt that no longer exists.

3. **MAJOR — Per-candidate p̂, the cascade's engine, is unimplemented and conflicts with M2.** An ids-only listwise answer has no posterior; logprob P(yes) is documented only for GPT-4.1-mini (`family` note); verbalised scores cost ≈120 completion tokens at 4–6× prompt price, more than M2's 8 % saving; §5's "agreement proxy" doubles Stage 1.

4. **MAJOR — Validation below its own resolution.** All §2 validations run on dev (MDD 15–18 points) for expected effects of 3–6 points. M6's "never loses more than 0.01" and M1's "L5 within the CI of L1 ⇒ production prompt" are non-inferiority claims needing a pre-specified margin and far more paired queries; M1 turns a ±10-point CI into a deployment decision.

5. **MAJOR — M9 measures compliance, not causation.** A model told to cite shown fields does so whatever drove the decision; the literal checker penalises paraphrase and unit normalisation and rewards terseness; the metric is one-sided (unshown ⇒ leak, shown ⇒ nothing). Under the cascade "shown" is undefined (L5 at Stage 1, L1 at Stage 2): verify against L1 and the leak rate is zero by construction. R10's version (cite under L5-P: a dims-citing accept that still finds the true partner is memory caught in the act) was diagnostic; M9 dropped it.

6. **MAJOR — The un-mixing estimator is unidentified with a noisy probe.** One equation, three unknowns per rung. Under correct-in-both-orders scoring a chance-level model is tagged "memorised" 25 % of the time, so the evidence stratum holds memorised queries at an unknown rate and acc_evid has no bound. "Ids only" is either chance-level (Q-ids, accession numbers) or leaky (any text): a forced choice cannot be evidence-free — closed-book naming (E5 on test) is the coherent instrument.

7. **MAJOR — Pre-registration after exposure, with eight new knobs.** L1/L2-T/L3-H/L5 test runs exist for 2–4 models, so M15 registers an analysis of seen data; disclose it. Eight new tunables (band, prune threshold, τ, K, abstention margin, memorised criterion, fame cut-points, clustering rule) are set on the same 80 dev queries; each value must be in the file. A ladder "publishable either way" cannot register a direction; register the MDD and equivalence margins.

8. **MAJOR — Scope drift and orphaned data.** docs/03 §4 says build the paper around the ladder; docs/04 spends §2.2–2.3, §2.7–2.8 and §3 on a four-stage system with zero real runs, reopening R02/R08. Because M7 relabels the rungs, the docs/03 §6 "$100" buys old-schema rungs (L5-P, `--withhold-title` L6) while `STATUS.md` prices the v2 test ladder at ≈$40 more: choose the schema before spending or pay twice.

9. **MINOR — Opposed mechanisms.** M4′/M6 prune low-score candidates — the orphans' members M12 says "need the flagship" — and lower the ceiling to recall@16.

10. **MINOR — Framing.** Standing alone: M1–M4, M6–M11, M15–M16 (round-1 requests or standard techniques: FrugalGPT cascades, selective prediction, attribution, pre-registration). Existing only for the framing: M5 (dominated by M4, B.1d), M12 (19/432 sim wins; kept for 按需分配), M13 (a reviewer concern re-badged; no source or ground truth for the $130 stratum), M14 (no sim, price or experiment). Eight tradition headers read as decoration and invite an R05/R09 ornament objection; keep one epigraph.

## C. Re-scores (S1 / S2)

Round-1 means: Nov 5.8 · Sound 5.1 · Eval 4.3 · Clar 5.9 · Impact 6.1 · Overall 4.7.

**S1 — nothing new is run; `docs/04` is the method section.**

| axis | S1 | justification |
| --- | ---: | --- |
| Novelty | 6 | sharper measurement design (nested ladder, grounding, stratification); the cascade is FrugalGPT. |
| Technical soundness | 4 | contradictions (B.1–B.2), two memory models, unidentified estimator, nothing run. |
| Evaluation rigour | 3 | all quality numbers simulated; the v2 schema orphans the old rungs — less evidence than round 1. |
| Clarity | 5 | [real]/[sim] tagging undone by eight headers, overlapping M4/M5/M12/M14, three prices for one pipeline. |
| Impact | 6 | same question; a protocol without data is a promise. |
| **Overall** | **4** | a design document, not a method section; weaker than round 1 on soundness. |

**S2 — the `docs/03` §6 list is run and comes out as hoped (monotone test ladder with CIs, β>0, small seed SD, probes stratify, recall@30 and regate disclosed, duplicates resolved).**

| axis | S2 | justification |
| --- | ---: | --- |
| Novelty | 7 | first powered per-channel leakage ladder for catalogue-level reunion, probes on the likeliest memorisers. |
| Technical soundness | 6 | ladder sound (ensemble unit, disclosed regate, registered analysis); system claims stay simulated, in an appendix. |
| Evaluation rigour | 6 | ladder on ≥2 models with seeds, ceilings and floors; still n=294, one Western pool, old-schema rungs unless ≈$40 more. |
| Clarity | 6 | unchanged by the list; 7 if the framing shrinks to an epigraph and M5/M12/M14 leave the main text. |
| Impact | 7 | publishable in either direction with real CIs; reusable grounding/stratification protocol. |
| **Overall** | **6** | weak accept as a measurement paper; the system stays future work. |

## D. Must-do before resubmission

Build the paper around the ladder measurement; the v2 system goes to an appendix unless it is run. Freeze the nested schema first — a published field table naming the image-URL and iconography fields — then run it on test for ≥2 models × ≥2 seeds (≈$40) with ensemble-level bootstrap, recall@K, the shortcut-heuristic row, the served-as split per run, and the duplicate test prompts removed. Pre-register the `e10_regate` rule with pre/post-regate numbers for all existing runs, which test comparisons have already been seen, a value for every new tunable, and the MDD plus an equivalence margin rather than a direction. Run E8 on GPT-5.4 and GPT-5.4-mini as closed-book naming plus a period-matched counterfactual, report the probe's chance-level false-positive rate, stratify every ladder plot by that outcome and fame tercile rather than backing out acc_evid by formula, and add one E8 arm at L5-only evidence to decide whether memory is word-keyed or record-keyed. Re-price §3 with the simulation's own 0.96 escalation fraction or a measured one, set the §3 band to the §2.2 recommendation, delete the oracle "87–95 % of worlds" sentence, and either run the $5 paired mini@L5→flagship@L1 dev cascade or drop the M4–M6/M11–M12 quality claims from the main text. Implement M9 under L5-P so it is diagnostic, and confirm the dev/test split is ensemble-disjoint.
