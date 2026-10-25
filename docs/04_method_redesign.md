# 04 · Method redesign — from "one flagship call over 30 candidates" to a frugal, evidence-first reunion system

This document does three things. (1) It states what the current method is and where it is weak,
using only facts from the ledger and the panel. (2) It turns a set of philosophical principles the
user asked us to draw on — Daoist *大道至简* and *无为而治*, the Zen stance toward words and
things, Confucian honesty about not-knowing, the Christian injunction to *test everything*,
need-based allocation, and the economics of information — into **concrete mechanisms**, each with
the evidence we have (real ledger or calibrated simulation) and the cheap real experiment that would
confirm or kill it. (3) It proposes a v2 system and a v2 measurement protocol and prices both.

Numbers tagged **[real]** come from `data/real/runs.csv`; numbers tagged **[sim]** come from
`sim/results/` and are *synthetic-world* results whose absolute values do not transfer — only their
ordering and sensitivities do (`sim/README.md`).

---

## 1. What the current method is (and is not)

- One listwise call per query: a flagship model reads the query record plus 30 candidate records at a
  chosen information level and returns the ids it believes belong to the same ensemble
  (80/80 and 294/294 calls per run, 40–110 completion tokens on non-thinking models) **[real]**.
- Cost per query: $0.0042 (GPT-4.1 mini) … $0.020 (GPT-4.1 / GPT-5.4) at L1; $0.0025 … $0.013 at L5 **[real]**.
- No cascade, no early exit, no adaptive K, no routing, no abstention, no verification step in
  65 runs **[real]**. The "deep research" harness (E15/E17) is a separate road costing 4–53× more
  per query **[real]**.
- The post-processor `e10_regate` runs after every job with an unknown rule **[real, rule unknown]**.

The method is therefore a *RankGPT-style listwise selector with a set-valued output*. The panel's
view (R02, R07, R10) is that this is fine as a reference system but is not a contribution; the
contribution is the measurement design around it. The redesign below keeps that priority: every
mechanism is chosen because it either **saves tokens at equal quality**, **improves quality at equal
tokens**, or **makes the memory-vs-evidence measurement cleaner** — ideally all three.

## 2. Principles → mechanisms

### 2.1 大道至简 — "the great way is simple": strip the prompt to the evidence that decides

*Principle.* Remove everything that does not change the decision; what remains is both cheaper
and harder to fake.

*Mechanism M1 — evidence-minimal prompts.* The ladder already measures what each field is worth.
If, on **non-memorised** queries, L5 (physical facts) performs within the CI of L1, then L5 is the
production prompt: 1,208 vs 1,959 prompt tokens, **−38 % cost at the same decision quality**
**[real token counts]**. If L1 is better only on memorised queries, the extra 750 tokens buy
recall of Wikipedia, not evidence — and the paper should say so.

*Mechanism M2 — ids-only output.* Completion tokens are priced 4–6× prompt tokens **[real: fitted
relay prices]**; the 70-token answers of the flagships are 12 % of a GPT-4.1 call **[real]**.
A strict "return ids as a JSON array" format with the justification requested *only* in the
verification stage (§2.5) saves ≈8 % with no information loss.

*Mechanism M3 — turn the thinking tax off unless it buys accuracy.* GPT-5.4 mini at
`reasoning_effort=low` spends 60 % (L1) to 78 % (L5) of its cost on hidden reasoning tokens and its
reasoning *grows as evidence shrinks* (475 → 694 tokens/query from L1 to L5) **[real]**. Either sweep
effort {none/minimal/low} and plot accuracy-per-dollar, or use the non-thinking mini.

*Validation (≈ $1, GPT-4.1 mini, dev):* already in the ledger as L1 vs L5 — only the stratification
by the forced-choice outcome is missing (free).

### 2.2 无为而治 — "govern by not acting": act only where action is needed

*Principle.* The system's default is *no* intervention; the expensive model is invoked only where
a cheap signal says the decision is genuinely open. The sage "does nothing, yet nothing is left
undone".

*Mechanism M4 — two-model cascade with an uncertainty band.* A cheap model judges all 30
candidates; only candidates whose posterior lies within ±0.4 of 0.5 go to the flagship, in one short
listwise call. **[sim]**: the most frequent equal-budget winner across 216 worlds (170/432 cells),
typically delivering +0.03…0.06 F1 at 55–70 % of the flagship's cost; it keeps winning under
correlated model errors (ρ = 0.7) and over-confidence (×1.4), but *not* when long lists do not
dilute the model (β = 0) — then it ties and the single-model "read less" policies win (Fig. S8c).

*Mechanism M4′ — the simplest version: prune by the retriever, no cheap model at all.* Drop every
candidate whose calibrated retriever posterior is below 0.02 and give the flagship only the
survivors (≈16 of 30). **[sim]**: +0.036 F1 at 67 % of today's cost, with zero extra calls — as good
as the two-model cascade in the base world. This is 大道至简 in its purest form and should be the
first thing tried.

*Mechanism M5 — evidence escalation, not just model escalation.* Run the cheap screen at **L5**
and escalate to **L1**. Easy decisions are then made from physical facts (memory-poor), hard ones
get the full record. This fuses the cost argument with the contamination argument: the fraction of
decisions that *needed* the title/creator/holder becomes a measured quantity, per query.
**[sim] caveat**: the screen must be allowed to *reject* but not to *accept* confidently — a
symmetric band of 0.4 at L5 loses 0.034 F1 (true members confidently dismissed at the austere level
never reach the flagship); a reject-only screen (p̂ < 0.05) or a band of 0.45 gives +0.026…+0.030 F1
at 64–66 % of today's cost. Price **[real token counts, GPT-4.1 mini + GPT-4.1]**: mini@L5 all
(1,208 prompt + 70 completion tok → $0.0026) + flagship@L1 on ≈40 % of queries over ≈8 candidates
(≈816 prompt + 70 completion tok → $0.0098 × 0.4 = $0.0039) ≈ **$0.0065/query, −67 % vs today's $0.020**.

*Validation (≈ $5, dev):* mini@L5 → flagship@L1 cascade vs flagship@L1, paired, 80 queries, 3 seeds.

### 2.3 知止 — "know when to stop": read only as much of the shortlist as the retriever justifies

*Principle.* Diminishing marginal returns; the retriever already ranked the candidates.

*Mechanism M6 — adaptive K from the retriever posterior tail.* Before calling, choose the smallest
K such that the expected number of unread members (from the retriever's calibrated scores) is < τ.
**[sim]**: τ = 0.05 costs 70–90 % of K = 30 and never loses more than 0.01 F1; with a good retriever
(d' = 2) it gains +0.04 while costing 70 % (Fig. S8b). Together with K = 10 and retriever-prune (M4′),
"read less" is the best single-model choice in 146/432 sweep cells. Requires only calibrated
retriever scores — zero extra calls.

*Validation (≈ $1, dev):* `--k 10` vs `--k 30` on the same queries, GPT-4.1 mini, 2 seeds. This also
measures **list dilution β**, the parameter that decides whether pointwise, cascade or adaptive-K
pays (Fig. S8a). It is the highest-information cheap experiment available.

### 2.4 禅 — "not founded on words; point directly at the thing"

*Principle.* 不立文字: the catalogue *words* (title, attribution, credit line) are where
memorisation and cataloguing conventions live; the *thing* (dimensions, support, medium, image,
ground, tool marks) is where evidence lives. 初心: approach each query with beginner's mind — no
prior about who made it or where it hangs.

*Mechanism M7 — reorder the ladder so that "things" sit below "words".* Today L5 still shows the
title and only L6 withholds it **[real: `--withhold-title` exists only on top of L5]**; the panel
(R03, R05, R10) calls this the ladder's main construct-validity flaw. v2 ladder (nested, each rung a
strict subset of the one above):

| rung | shows | removes vs rung above |
| --- | --- | --- |
| L1 | full record | — |
| L2 | L1 − title | the field that most often *names* the ensemble |
| L3 | L2 − holder / accession / credit line / image-URL host | institutional fingerprints |
| L4 | L3 − creator / workshop / Notname | the memorised association |
| L5 | physical facts only: dimensions, support, medium, technique, date band, iconography keywords | all words about people and places |
| L5-P | L5 with dimensions permuted across candidates | the physical channel itself (control) |
| L6 | images only (+ dimensions) | all text — the MLLM "direct pointing" rung |

*Mechanism M8 — a visual rung with a visual closed-book control.* E7/E16 ask the MLLM "same
ensemble?" from thumbnails (≲450 tokens per image) without asking "name this panel" **[real]**.
Add (a) a frozen CLIP/SigLIP/DINOv2 cosine baseline on the same shortlists (GPU minutes, $0),
(b) a visual closed-book probe (fame recognition from pixels), (c) a photographic-campaign control
(negatives from the *same* holder). R04's blocker.

### 2.5 "Test everything; hold fast what is good" (1 Thess 5:21) — verify before you claim

*Principle.* A claim of reunion is sticky (catalogue entries, Wikidata write-backs, press). It must
survive an adversarial check and carry its evidence.

*Mechanism M9 — grounded verification call.* For each predicted member, a second, short call must
cite the *fields in the shown record* that support the match; a deterministic checker then verifies
that every cited value is literally present. The fraction of predictions whose justification cites
an **unshown** fact is the *memory-leak rate made visible* — a new, cheap, per-decision
memorisation metric (R06's "evidence-grounding rate"). Price: ≈300 tokens per predicted member ×
≈1.8 members/query ≈ $0.005/query on GPT-4.1, $0.001 on the mini.

*Mechanism M10 — "render unto memory what is memory's": the un-mixing estimator.* Observed accuracy
at a rung is a mixture: acc_obs = p_mem · acc_mem + (1 − p_mem) · acc_evid. **[sim]** With
p_mem = 0.3 the observed L1→L6 drop is roughly half the evidence-only drop (Fig. S5). Estimate p_mem
per query with a *truly* evidence-free forced choice (ids only; today's "no-evidence" arm still shows
≈260 tokens of item content **[real]**), then report acc_evid = (acc_obs − p_mem·acc_mem)/(1 − p_mem)
with an ensemble-bootstrap CI, and stratify every ladder plot by memorised / non-memorised and by fame
tercile (`commons_views`, `nga_views`).

### 2.6 知之为知之，不知为不知 — honest not-knowing: abstain and calibrate

*Mechanism M11 — selective prediction.* Let the agent output the empty set with a confidence; report
risk–coverage curves and precision at ≥ 95 %. **[sim]** Refusing the 20 % least-confident queries
lifts precision 0.87 → 0.92 with no extra calls (Fig. S6). Requires that some shortlists contain
*no* gold member (if none do today, inject them) — the curator's modal case (R06).

### 2.7 各尽所能、按需分配 — from each according to ability, to each according to need

*Mechanism M12 — need-based budget per query (routing).* Equal spend per query is the wrong
allocation; famous, easy queries need a mini, orphans need the flagship plus images plus the open
pool. Route on the cheap model's confidence. **[sim]** routing is a weaker instrument than the
candidate-level cascade (wins in 19/432 cells vs 170) because it escalates whole queries; combine
both: candidate band first, query escalation only for the residual.

*Mechanism M13 — fairness of the pool.* Western-canon dominance (NGA + English Wikidata) makes the
benchmark measure Wikipedia recall for the famous and nothing for the rest (R05, R09). Stratified
reporting by fame tercile and by region; a non-Western extension (Dunhuang leaves across
London/Paris/Beijing/St Petersburg, dismembered Chinese albums, Persian *muraqqaʿ*, sutra scrolls)
priced at ≈$130 for a full ladder × 4 models × 3 seeds (R10's $1,000 plan).

### 2.8 Economics of information — buy evidence only when its expected value exceeds its price

*Mechanism M14 — value-of-information gate for images and open-pool search.* An image call
(≈$0.012 on the mini, $0.06 on GPT-4.1) or an open-pool step (≈$0.02 per step on GPT-5.4) is bought
for a query only if the current posterior is in the open band and the expected change in decision
value exceeds the price. This is M4 generalised to heterogeneous evidence sources; the cascade band
is the VoI gate's simplest instance.

*Mechanism M15 — commitment device against hidden degrees of freedom.* Fix `e10_regate`'s rule,
the ladder schema, the metric and the test-split analysis plan in a pre-registration file *before*
the next test run (principal–agent: the author is agent for the reader). Costs nothing; converts
B6 from blocker to footnote.

*Mechanism M16 — Pareto reporting.* Every table gets a cost column; the headline figure is
quality-vs-$/query with CIs (Fig. S1/S2 template), not a single number. Dev→test cost is predictable
to a few percent (Fig. R7), so the plan can be budgeted exactly.

## 3. The v2 system in one picture

```
query q ──► retriever ──► shortlist (scores) ──► K_q = adaptive cut (M6)
                                                     │
                       ┌─────────────────────────────┴──────────────────────────────┐
                       │ Stage 1  cheap screen · mini · L5 physical facts (M1, M5)   │  ≈ $0.0026
                       │   per candidate: p̂(member)                                 │
                       └───────────────┬─────────────────────┬──────────────────────┘
                   p̂ < 0.1 ─► reject   │  0.1 ≤ p̂ ≤ 0.9      │   p̂ > 0.9 ─► accept (provisional)
                                       ▼
                       ┌──────────────────────────────────────────────────────────────┐
                       │ Stage 2  strong judge · flagship · L1 full record, only the  │  ≈ $0.0098 × 40 %
                       │   uncertain candidates (M4) · images / open pool only if the  │
                       │   VoI gate opens (M14)                                        │
                       └───────────────────────────────┬──────────────────────────────┘
                                                       ▼
                       ┌──────────────────────────────────────────────────────────────┐
                       │ Stage 3  verify & ground (M9): cite shown fields; checker    │  ≈ $0.001–0.005
                       │   flags unshown facts ("memory claim"); calibrated confidence │
                       │   → answer set, or abstain (M11), + evidence dossier          │
                       └───────────────────────────────┬──────────────────────────────┘
                                                       ▼
                       Stage 4  ensemble closure: pairwise decisions across queries → clusters;
                                 evaluate pairwise F1 / B-cubed / ARI per ensemble (B2)
```

Expected price **[real token counts and fitted relay prices, GPT-4.1 mini + GPT-4.1]**: ≈ $0.0075–0.0115 per
query all-in versus $0.020 today, i.e. **−40 … −63 %**, while **[sim]** quality is equal or higher in
87–95 % of worlds.
The one real experiment that de-risks the whole design is the $1 `--k 10` vs `--k 30` run (§2.3).

## 4. The v2 measurement protocol (the paper's actual contribution)

1. **Nested ladder** (§2.4 table) with a published field schema; prompt-token fingerprint per rung
   as a sanity check (Fig. R1 style).
2. **Units and statistics.** Ensemble is the unit: pairwise P/R/F1 and B-cubed/ARI; bootstrap over
   ensembles; paired tests between rungs; report the MDD (dev ≥ 15–18 pts, test ≥ 7–9 pts **[sim]**)
   and only make rung-vs-rung claims on the test split.
3. **Stratification** by memorised/non-memorised (true evidence-free forced choice, period-matched
   counterfactuals, both orders) and by fame tercile; un-mixing estimator with CI (§2.5).
4. **Ceilings and floors in the main table**: recall@K of the shortlist; shortcut-heuristic row
   (same holder / creator / title stem / dimension match); a classic ER baseline (blocking +
   logistic matcher); a CLIP/SigLIP cosine row for the visual rung.
5. **Position and sampling controls**: shuffled-order seed on every E10 run; ≥ 3 seeds on test for the
   headline rungs (the dev→test cost predictor prices this exactly: ≈ $6 per 3 seeds of GPT-4.1 mini).
6. **Cost column everywhere**; one Pareto figure as the headline; reasoning-effort sweep for the
   thinking model.
7. **Pre-registration file** committed before the next test run (M15).
8. **Release hygiene**: datasheet, per-file Commons licence audit, provenance-sensitivity statement,
   non-Western stratum (R09, R05).

## 5. Known defects of this redesign (so the next reviewer does not have to find them)

- All quality claims for M4–M6, M11–M12 are **simulated**; the sweep says *which* assumption each
  verdict hinges on (β, retriever d', ρ_models, over-confidence) — those are what the $1–$5
  experiments in §2 measure. If β ≈ 0 and the retriever is weak, the cascade degenerates to
  "flagship on everything" and saves nothing; the design then still saves via M1–M3.
- The cascade's uncertainty band assumes the cheap model's posterior is informative; verbalised
  confidences of LLMs are poorly calibrated. Use logprob P(yes) where the relay passes logprobs
  (GPT-4.1 mini did **[real: `family` note]**), otherwise a two-sample agreement proxy.
- Evidence escalation (M5) changes the *evidence* between stages; a candidate accepted at L5 and a
  candidate accepted at L1 are not the same kind of decision. Report them separately — that is a
  feature for the contamination analysis, but it complicates a single F1.
- The grounding checker (M9) verifies literal presence, not inferential validity; a model can cite
  a shown dimension and still be wrong. It bounds *memory leaks*, not *reasoning errors*.
- Stage 4 closure needs a clustering rule (connected components over confident pairs is the simplest;
  correlation clustering is better); the metric choice changes rankings when ensembles are large.
- Nothing here fixes ground truth. Wikidata `part of` encodes one reconstruction; a small expert audit
  (100 decisions) is time, not API spend, and should happen regardless (R05, R10).
