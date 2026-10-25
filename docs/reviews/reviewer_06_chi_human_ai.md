# Reviewer 06 — CHI / CSCW (human–AI collaboration, expert decision support)

## Summary of the submission as I understand it

Given one museum record and a shortlist of 30 candidate records, LLM/MLLM agents select the candidates that belong to the same dispersed ensemble; an information ladder (L1 full record → L6 physical facts only) and per-channel scrubs separate memorisation from evidence use. Variants: listwise agent (E10), pointwise scoring (E10e), visual gates (E10c/E16), forced choice (E8v4), tool-using harnesses (E15, E17 open pool). The material contains no users, no interface and no human evaluation; the ledger gives cost and latency per configuration but no accuracy. I review it as a candidate decision-support component and ask what would make it one.

## Scores (1–10) with one-line justification each

- Novelty: 5 — a new domain for the memorisation-versus-evidence question; nothing new on the human–AI side.
- Technical soundness: 6 — careful ablation grid; 41–110 completion tokens per query cannot carry the explanation the task requires.
- Evaluation rigour: 4 — no abstention condition, no calibration, no human study, no operating point chosen for the real error costs.
- Clarity (of the design, as reconstructed): 6 — the pipeline reconstructs cleanly; the user and the decision are never named.
- Impact / significance: 5 — large for provenance research if reframed as evidence triage with abstention; limited as "agent picks members".
- Overall: 4 — reject for CHI in this form (a sound measurement paper elsewhere); artefacts 1–3 below would move me to 6.

## Strengths

- Honest cost and latency accounting per configuration (`runs.csv`) — rare, and exactly what a deployment decision needs.
- Pointwise scoring (`20261023_014051_e10e_pointwise_L1_xj-gpt-4.1-mini`: 1 completion token per candidate, 2,344 records for 80 queries) already yields the per-candidate scores calibration needs.
- Replicate and prompt-variant runs at L1 acknowledge stochastic output; v2 halves completion length against v1 (59.4 vs 105.4 tok/call), which matters for any interface.
- The leakage ladder maps directly onto the explanation requirement "what evidence did the system actually use".

## Weaknesses

1. **[BLOCKER] No user, no decision.** Is the user a curator deciding whether to publish a reconstruction, a registrar vetting a loan, a catalogue-raisonné author, or a Wikidata editor? Error costs differ by an order of magnitude between them. Without this, "select members from 30" is a benchmark, not decision support.
2. **[BLOCKER] A shortlist with picks is the wrong artefact.** Non-thinking models emit 41–110 completion tokens per query in every E10 run (GPT-4.1 L2-T dev 41.3; GPT-4.1 L1 dev 64.8; GPT-5.4 L1 test 86.6): an ID list with at most a clause of justification. The over-reliance literature (Bansal et al. 2021; Buçinca et al. 2021) shows that recommendations plus thin explanations raise acceptance of wrong answers. Experts need an evidence dossier — side-by-side fields, matched and conflicting facts, what is missing — not a pick.
3. **[MAJOR] Abstention is unmeasured and possibly impossible.** If every shortlist contains ≥1 true member, the agent is never tested on "none of these", the curator's modal case. Report the share of queries with zero gold in the shortlist (if zero, add negatives), the no-answer rate and no-answer precision; if `e10_regate` is the acceptance rule, it is the abstention mechanism and must be specified.
4. **[MAJOR] Calibration is not reported.** With pointwise P(yes) logged, show reliability diagrams, ECE and risk–coverage curves per level. A tool at 90 % precision and 40 % coverage with honest abstention is useful; the same model at 70 % precision and 100 % coverage is a liability.
5. **[MAJOR] Verifiability of cited evidence.** When the agent says "same dimensions" or "both from the X collection", is the fact in the shown record? At L5/L6 citing an unshown fact is a memorisation leak made visible. Measure the evidence-grounding rate (cited atoms ⊂ input) per level; it is a string match and doubles as a leakage metric.
6. **[MAJOR] Asymmetric error costs are ignored.** A false reunion claim is reputational and sticky (press release, catalogue entry, Wikidata write-back); a miss preserves the status quo. Report precision at ≥95 % and the recall achieved there, not F1, and separate "plausible wrong" (replica, pendant) from "absurd wrong" — experts accept the former.
7. **[MAJOR] The latency profile is not interactive where the system is most likely to be right.** Listwise: 3–8 s/call (GPT-5.4 L1 dev 4.24 s; GPT-4.1 L5 dev 7.99 s), acceptable with progress feedback. GPT-5.4-mini on test: 14.3–15.2 s. GPT-5.4 at L6: 20.08 s/call. Pointwise 79 s/query, E17 53 s/query. Above ~10 s this is a precomputed batch presented as a dossier, which changes the system design, not just the UI. Robustness: the L5-P test run died on 4 API errors (`20261024_234820_e10_agent_L5-P_xj-gpt-5.4`).
8. **[MINOR] Stochasticity is user-visible.** rep1 and the base L1 run have identical prompts (156,708 tokens) but 6,844 vs 7,271 completion tokens; if picks differ, the tool must show it or average over seeds.
9. **[MINOR] Ground truth may not be inter-annotator reliable** (see the art-history concerns); a human study will expose this and should plan for it.

## Experiments or artefacts that would change my score

1. A one-page user, decision and error-cost table — convinces me if the operating point is derived from it.
2. A negative-shortlist condition (≥25 % of queries without gold) with abstention metrics — convinces me if no-answer precision ≥80 % at L3-H.
3. Calibration from the existing pointwise scores (zero new spend) — convinces me if ECE <0.1 and the risk–coverage curve dominates the listwise agent.
4. An evidence-grounding audit — convinces me if ≥95 % of cited facts are present in the shown record at L1, with the L5/L6 rate reported as a leakage statistic.
5. A budgeted human-in-the-loop study: 3 curators × 40 cases (25 with a true member, 15 without; stratified by fame via `commons_views`/`nga_views` and by level), within-subjects, counterbalanced over three conditions — records only; records plus agent picks; records plus evidence dossier with the pick hidden until the curator commits. ~15 min per case, ~30 expert-hours, $2–3k honoraria, API <$5. Measures: accuracy against Wikidata gold and against curator consensus; over-reliance (accepting wrong picks) and under-reliance; time per case; confidence; Krippendorff's α among curators in the no-AI condition (α <0.6 means the gold is contested); time saved counted only on correctly decided cases — convinces me if the dossier condition cuts time ≥25 % without raising over-reliance above the picks condition.
6. A latency-bucketed configuration table (best accuracy at ≤8 s, ≤20 s, batch) — convinces me if the recommended deployment is honest about its bucket.

## Token-efficiency / cost critique

The listwise family took 74 % of spend ($74.5) to produce outputs too short to be explanations, while a structured, field-cited justification of ~300 tokens would add ≈$0.002–0.003 per query at GPT-4.1 output prices. GPT-5.4-mini costs as much per call as the flagships at L1 ($0.016 vs $0.020) and more at L5 ($0.018 vs $0.013), and its extra 475–766 tokens per call are hidden reasoning — zero explanation value per dollar; drop it or expose a summary. Pointwise E10e on GPT-4.1-mini ($0.012/query) is cheaper than listwise on a flagship ($0.020) and yields per-candidate scores; its 79 s is a batch problem, not a cost problem. Missing and cheap: calibration from logged scores, evidence-grounding string match, negative shortlists. The real budget line is human time: the study above costs 20–30× the entire API ledger and is the only thing that would make this a CHI paper.

## One idea the authors have not tried

A *commit-then-reveal dossier protocol*. The agent outputs JSON per candidate: verdict ∈ {member, non-member, cannot tell}; evidence as verbatim quotes from the shown records; conflicts; what is missing that would settle it. A validator rejects any quote not found in the input, so grounding is enforced rather than measured. The interface shows both records side by side with quoted spans highlighted; the curator records judgement and confidence before the verdict is revealed, then may revise. Pre/post logs give, per case, whether updates move toward truth and where "cannot tell" coincides with curator uncertainty. Pilot on 10 dev cases with one curator; ~300 completion tokens per candidate stays inside the ledger's cost envelope.

## Confidence (1–5) and what I could not assess

4 — confident on the human–AI design and evaluation points. I could not assess accuracy, the real output format (whether justifications exist beyond IDs), the `e10_regate` acceptance rule, or whether any shortlist lacks a gold member.
