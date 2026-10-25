# 03 · Ten-reviewer panel — synthesis and action list

Ten simulated programme-committee members (five parallel sessions, two personas each) reviewed
the project from `docs/01_project_reconstruction.md` and the real ledger under the contract in
`docs/reviews/_briefing.md`. Individual reviews: `docs/reviews/reviewer_01…10.md`
(≈1,000 words each). A web-grounded positioning scan is in `docs/02_related_work_positioning.md`.

Reminder: the panel saw **no accuracy numbers** (none exist in the export), so every verdict is
conditional. That is also why their consensus is unusually sharp: it is about *design*, not results.

## 1. Scores

| reviewer | Nov | Sound | Eval | Clar | Impact | **Overall** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| R01 NeurIPS D&B, statistics | 6 | 5 | 4 | 6 | 7 | **5** |
| R02 ICLR, benchmark/agent novelty | 5 | 6 | 5 | 6 | 7 | **5** |
| R03 ACL/EMNLP, contamination | 7 | 5 | 5 | 6 | 6 | **5** |
| R04 CVPR/ECCV, CV for heritage | 6 | 4 | 4 | 5 | 7 | **4** |
| R05 Digital humanities / art history | 6 | 5 | 5 | 6 | 5 | **5** |
| R06 CHI/CSCW, human–AI | 5 | 6 | 4 | 6 | 5 | **4** |
| R07 SIGIR/KDD, IR & entity resolution | 6 | 5 | 4 | 6 | 6 | **5** |
| R08 AAAI/ICML, agents & cost | 5 | 5 | 4 | 6 | 5 | **5** |
| R09 FAccT / D&B ethics & release | 6 | 5 | 4 | 6 | 6 | **4** |
| R10 Senior Area Chair (meta) | 6 | 5 | 4 | 6 | 7 | **5** |
| **mean** | 5.8 | 5.1 | **4.3** | 5.9 | 6.1 | **4.7** |

Reading: *impact* (6.1) and *novelty* (5.8) are the strengths; *evaluation rigour* (4.3) is the
weakness every reviewer converges on. Nobody doubts the question; everybody doubts that the current
grid can answer it with the statistics it will need.

## 2. Consensus blockers (named by ≥ 4 reviewers)

Items marked ✔ were **re-verified by me against `data/real/runs.csv`**; items marked ◌ are design
inferences the authors must confirm against the local repository.

| # | blocker | who | evidence |
| --- | --- | --- | --- |
| B1 | **The decisive rungs are under-powered.** L5-P, L6, L3-H2 exist only on 80 dev queries of one model (GPT-5.4); L3 has no test run for any model; the test ladder is complete for no model. Dev detects only ≥ 15–18-point drops (`sim/results/POWER.md`). | R01 R03 R05 R07 R09 R10 | ✔ ledger; ✔ power simulation |
| B2 | **Queries are not independent units.** "Same ensemble" is an equivalence relation; queries from one ensemble share the memorised fact and overlapping shortlists. Bootstrap over queries overstates precision; per-query scoring over-weights big polyptychs and hides A→B, B→C, C↛A inconsistencies. Need ensemble-level bootstrap and a cluster metric (pairwise F1 / B-cubed / ARI). | R01 R04 R07 R10 | ◌ (metric unknown) |
| B3 | **The first-stage shortlist is a black box.** Recall@30 is the ceiling of every E10 number and is not reported; `shortlist_shortcuts` (same holder / creator / title stem) may already solve much of the task; "different holder than the query" is itself a shortcut for a cross-institution task. | R02 R05 R07 R10 | ◌ |
| B4 | **The ladder is not nested, and L5 still shows the title.** L2-T prompts are *longer* than L1 (2,316 vs 1,959 tok/call — something ~350 tokens long was substituted for the title); only L6 (`--level L5 --withhold-title`) removes the title, so the "austere" L5 keeps the single most leaking field on the 31–40 % title-leak subset. L1→L3 removes only 9 % of tokens; holder scrub v2 removes one token per record. | R01 R02 R03 R05 R09 R10 | ✔ token fingerprints |
| B5 | **Memorisation probes skipped the likeliest memorisers.** E8v4 ran only on GPT-4.1-mini (both arms) and GPT-4.1 (no-evidence arm); never on GPT-5.4 / GPT-5.4-mini; E5 closed-book is dev-only. The "no-evidence" arm still shows ≈260 tokens of item content (titles, dates, dimensions, holders) — a period-matching task, not a memory-only probe. | R03 R05 R10 | ✔ ledger (259.5 vs 335.4 tok/call) |
| B6 | **`e10_regate` is an undisclosed post-hoc degree of freedom** run after every E10 job; if its rule was tuned on outcomes, all headline numbers are optimistic. | R01 R04 R07 R10 | ✔ follow_up column; ◌ rule |
| B6b | **Duplicate prompts of four kinds.** The harness cache logs exactly 3 hits on every 294-call L1 test run across all four models and 2 on every L3-H / L5 test run (2–3 duplicate test queries or identical shortlists); 8 hits in the L3-H2 dev run (records that differ *only* by holder → near-duplicate records in the ground truth); 135/2,344 in the pointwise run (duplicate query–candidate pairs); 47/295 in the deep-research harness (the agent loops). None is analysable from the export because the cache key is not logged. Small in count, but it must be resolved before CIs are quoted. | R09, red-team practitioner | ✔ `cache_hits` column, model-independent |
| B7 | **Reproducibility.** All calls via a paid relay at ≈4.4× list prices; GPT-5.4 was served under two labels on every GPT-5.4 run (pinned `gpt-5.4-2026-03-05` plus 4–31 % of calls under the unpinned alias `gpt-5.4`; e.g. 73/294 on the L1 test run); GPT-5.4 prices "estimated"; one replicate in the whole grid (GPT-4.1-mini, L1, dev). | R08 R09 R10 | ✔ served_as field |

## 3. Major issues by theme (each named by 2–3 reviewers)

- **"Agent" is one listwise call** (80/80 and 294/294 calls, 40–110 completion tokens); the agentic
  road (E15/E17) ran on 40 / 20 queries of one model each and is not compute-matched. Either rename
  ("listwise selector") or make the multi-step system the method. (R02 R08)
- **No cost-adaptive mechanism in 65 runs** — no cascade, early exit, adaptive K, routing, abstention —
  the central omission for a paper that talks about cost. The natural compute-matched test
  (5 × GPT-4.1-mini = 1 × GPT-4.1 at $0.02) was never run. (R08; addressed in simulation, §5)
- **Reasoning tax observed, not controlled**: GPT-5.4-mini ran only at `reasoning_effort=low`; its
  completion tokens *grow* as evidence shrinks (475 → 617 → 660 → 694 from L1 to L5), so ≈60 % of its
  spend is hidden reasoning. Sweep effort, or report accuracy-per-dollar curves. (R08 R03)
- **Position bias uncontrolled** in the 30-item list: `--both-orders` exists only for 2-item E8;
  no shuffle seed on any E10 run. (R03 R07)
- **No vision baseline at all** (SIFT / CLIP / DINOv2 / SigLIP embedding cosine on the same
  shortlists); images at thumbnail scale (≲450 tokens per image); E16's recall ceiling set by a 2B
  model's top-8; no visual closed-book ("name this panel from pixels") control; photographic-campaign
  shortcut unaddressed. (R04)
- **Ground truth and practitioner value**: Wikidata `part of` encodes one editor's reconstruction;
  published reunions are both memorisable and useless to curators — the orphan case is the open-pool
  setting (E17), which got 20 queries. Discipline failure modes (autograph replicas, workshop copies,
  prints after paintings, pendants vs series, Notnamen) are not enumerated as hard negatives. (R05 R07)
- **No user, no decision, no abstention**: who acts on the output and at what error cost? False
  reunions are sticky (catalogue entries, Wikidata write-backs); report precision at ≥95 % and the
  recall achieved there, risk–coverage curves, and evidence-grounding rate (is the cited fact in the
  shown record?). (R06)
- **Release**: Commons per-file licences (PD-Art contested outside the US), no datasheet, provenance
  sensitivity (suppression sales, colonial removal, 1933–45 forced sales), Western-canon pool. (R09)

## 4. The one claim to build the paper around (R10, endorsed by R02 R03)

> *The memory-versus-evidence ladder measurement.* It is publishable in either direction (a large
> L1→L6 drop is a contamination result; a small one is a reasoning-over-physical-facts result), it is
> where 74 % of the spend already sits, and it is the only part all ten reviewers rate as novel.
> The agent becomes the reference system, the dataset the vehicle, the cost table an appendix section.

The related-work scan (`docs/02_related_work_positioning.md`) agrees: catalogue-level,
cross-institution reunion with per-channel leakage ablations has no located precedent; the closest
work (LLMCO4MR, ECCV 2024) is pixel-level fragment matching on Dunhuang, and GalleryGPT / TAM already
name memorisation of famous artworks as a confound — so claim the *measurement design*, not the
discovery of the confound.

## 5. What this repository already answers

| reviewer request | artefact here |
| --- | --- |
| power / minimum detectable difference for n = 80 / 294, clustering | `sim/power_analysis.py` → `sim/results/POWER.md`, `figures/sim/S7` |
| compute-matched comparison of policies at matched operating points (fusion, read-less, cascade, routing, SC, abstention; no-LLM null) | `sim/reunion_sim.py` (v2) → `sim/results/RUNLOG.md`, `figures/sim/S1–S3, S8`, decision table in `sim/README.md` |
| ensemble-level metrics, cluster bootstrap, paired tests, un-mixing, risk–coverage, position bias — as code | `tools/eval_toolkit.py` (self-tested), `tools/adapters/README.md` |
| evaluation-unit divergence, forking-paths optimism, shuffled-order control | `sim/measurement_sim.py` → `figures/sim/S9–S11`, `sim/results/MEASUREMENT.md` |
| pre-registration (with disclosure of seen comparisons), runbook, paper outline | `docs/05`, `docs/06`, `docs/07` |
| memorised queries flatten the ladder → stratify by the forced-choice probe | `figures/sim/S5` |
| risk–coverage / abstention | `figures/sim/S6` |
| reasoning tax, cost of each road, dev→test cost prediction | `figures/real/R2, R3, R7` |
| served-model label split, failed runs, campaign timeline | `data/real/runs.csv` (`served_as`), `figures/real/R6` |

## 6. Prioritised action list for the local repository (cheapest first)

Costs use the real per-call rates (`figures/real/R3`). "Free" = no API calls.

1. **Free — fix the evaluation unit.** Report pairwise P/R/F1 and B-cubed/ARI per *ensemble*; bootstrap
   over ensembles; paired tests between rungs (McNemar on exact-set, paired bootstrap on F1).
2. **Free — publish the ladder schema.** A table of which fields each rung shows; make it nested
   (L1 ⊃ L2 ⊃ … ⊃ L6); explain the +357-token substitution in L2-T or drop the substitution; move
   title withholding *below* L5 so that L5 = physical facts without title.
3. **Free — report recall@30 of the shortlist and the shortcut-heuristic baseline row** in the main
   table; add a "no gold in shortlist" stratum (if it is empty, inject negatives so abstention is tested).
4. **Free — disclose `e10_regate`**; freeze its rule before any test run; report pre- and post-regate.
5. **Free — stratify every ladder plot by fame tercile** (`commons_views` / `nga_views`) and by the
   E8 forced-choice outcome (memorised vs not) — the un-mixing in `figures/sim/S5`.
6. **~$4 — GPT-5.4 L5-P and L6 on test** (the failed 10-24 campaign; `data/real/campaign_log_tail.txt`).
7. **~$6 — three seeds of L1 and L5 test on GPT-4.1-mini**; **~$12 — two L1 test replicates on each flagship**.
8. **~$19 — E8v4 both arms on GPT-5.4 and GPT-5.4-mini**, with the no-evidence arm *truly* evidence-free
   (ids only) and a period-matched counterfactual.
9. **~$1 — listwise `--k 10` vs `--k 30` on the same dev queries (GPT-4.1-mini) and a shuffled-order
   seed**: this single experiment measures list dilution β and position bias, which decide whether
   pointwise / cascade / adaptive-K pay off (`figures/sim/S8`).
10. **~$3 — cost-matched self-consistency**: 5 × GPT-4.1-mini vs 1 × GPT-4.1 at L1 and L5.
11. **~$0 + GPU minutes — CLIP/SigLIP/DINOv2 cosine baseline on the E16 shortlists**; report oracle recall@8.
12. **Datasheet + licence audit per Commons file + sensitivity statement** before any release.


## 7. Round 2 — red-team of this repository's own deliverables (`docs/reviews/redteam_*.md`)

Four adversarial reports were commissioned against round 1's outputs. Their findings changed the
simulation and the redesign materially; the headline corrections are recorded here so that the
history is visible.

| report | key finding | what changed |
| --- | --- | --- |
| `redteam_sim_code_review.md` | The v1 comparison was at a fixed posterior threshold under a 5.8 % prior — different operating points per policy; the retriever posterior and the controller's confidence were oracles; a zero-extra-cost baseline (listwise + retriever-informed prior) was missing and, when added, dominates; pointwise cost was level-blind; SC correlation was 0.75 not 0.5; "87 %/95 % of worlds" was a winner's-curse statistic; M5's price was ~2× too optimistic. | `sim/reunion_sim.py` rewritten (v2): matched operating points on held-out seeds, model-specific and word/record-keyed memory, retriever mis-calibration and confidence-noise knobs, new baselines, fixed costs, three-way seed split in the sweep, t-quantile CIs. **Result: fusing the retriever score into the LLM decision is the dominant mechanism when retriever and LLM errors are independent, and worthless or harmful when they are correlated; "read less" is a smaller, more robust gain; two-model cascades win only where errors are correlated *and* lists dilute; in 15 % of worlds today's design is already optimal; at L5 the retriever alone beats the flagship in half the worlds.** |
| `redteam_ac_rescore.md` | The redesign mixed the measurement with the system (evidence escalation makes the rung a dependent variable); under the v1 memory model the L5 screen settled *memorised* queries; the un-mixing estimator is unidentified with a noisy probe; pre-registration after exposure needs disclosure; the $100 runbook bought old-schema rungs. S1 (nothing new run) Overall 4; S2 (next $100 run as hoped) Overall 6. | `docs/04` v2 separates deliverables A and B; adds the word- vs record-keyed memory test (E8 arm at L5-only evidence); stratify-don't-back-out; `docs/05` gains a disclosure section, equivalence margins, a stopping rule; `docs/06` gains a schema-decision gate. |
| `redteam_philosophy_skeptic.md` | 無為而治 is *Analects* 15.5, not Laozi; 大道至簡 is not classical; most pairings were post-hoc labels. Concrete additions: monotonicity assertion per prompt, the no-LLM null as first table row, a stopping rule for the experiment, field-swap counterfactuals, canaries, three-way output with an elicited loss ratio. | `docs/04` §0 keeps two sentences (Daodejing 48 for the ladder; *Analects* 2.17–18 for the output); all mechanisms presented on engineering grounds; the six suggested mechanisms adopted (§2.1, §2.4, §2.5, §2.6, §2.7, M5). |
| `redteam_practitioner.md` | GPT-5 rejects temperature (no sampling replicates); `--dims-permute` permutes dimensions not positions; four kinds of cache hit; relay rationing; an N0–N10 decision tree with per-node costs; a per-call logging spec. | `docs/06` updated (schema gate, Node 0 checks, `--shuffle-seed` for GPT-5.4 replicates, logging table); B6b above expanded. |

Round-2 scoring of the revised package (red-team AC): **S1 = 4/10** if nothing new is run and the
redesign is submitted as the method section; **S2 = 6/10** (weak accept as a measurement paper) if the
next-$100 list is run and comes out as hoped. Both are below the round-1 "7 if …" conditionals because
the AC counts the v2 schema as orphaning the existing test rungs until they are re-run (≈ $74).
