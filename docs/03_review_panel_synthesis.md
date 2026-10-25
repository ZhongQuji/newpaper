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
| B6b | **Possible duplicate test prompts.** The harness cache logs exactly 3 hits on every 294-call L1 test run across all four models, 2 on every L3-H / L5 test run — the same prompt recurring within a run points to 2–3 duplicate or near-duplicate query records (or identical shortlists) in the test split. Small, but it must be resolved before CIs are quoted. | R09 | ✔ `cache_hits` column, model-independent |
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
| compute-matched comparison of policies (cascade, adaptive K, routing, SC, abstention) | `sim/reunion_sim.py` → `sim/results/RUNLOG.md`, `figures/sim/S1–S3, S8` |
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
