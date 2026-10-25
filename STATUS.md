# STATUS — what is done, what is not, what needs the local machine

Updated 2026-10-25 18:50 CST (round 2). Full timestamped trail: `logs/worklog.md`.

## Round 2 in one paragraph
Round 1's deliverables were red-teamed by four independent adversarial reviews
(`docs/reviews/redteam_*.md`). They found that the round-1 simulation compared policies at
different operating points, used oracle confidence, and lacked a zero-cost baseline that turns out to
dominate; that the redesign mixed the paper's measurement with the engineering system; that two of the
philosophical attributions were wrong; and that the runbook bought old-schema rungs. All of this was
fixed: the simulation was rewritten (matched operating points on held-out seeds, model-specific and
word/record-keyed memory, retriever–LLM error correlation, new baselines), the redesign was rewritten
around two separated deliverables, and an evaluation toolkit, a pre-registration template (with
disclosure of already-seen comparisons), a priced decision-tree runbook and a paper outline were added.
**The headline simulation result changed sign:** two-model cascades do *not* beat single-model
"read less" policies at equal cost; fusing the retriever score into the LLM decision is the dominant
zero-cost mechanism — if, and only if, the retriever's errors are not the LLM's errors (Fig. S8b).

## Done in this repository (`bash tools/run_all.sh` rebuilds everything, ≈ 12 min)

| # | deliverable | where | evidence |
| --- | --- | --- | --- |
| 1 | Real experiment ledger: 65 runs, 9,178 calls, $100.07, served-model audit, failed runs, campaign log | `data/real/` | **real** |
| 2 | Project reconstruction with confidence tags | `docs/01` | real + inference |
| 3 | Seven figures from the real ledger | `figures/real/R1–R7` | **real** |
| 4 | Related-work positioning (web-grounded) | `docs/02` | literature |
| 5 | Ten-reviewer panel + synthesis (7 blockers, 12 actions) + **round-2 red-team section** | `docs/reviews/`, `docs/03` | simulated reviewers; factual claims re-verified |
| 6 | Design-space simulation **v2** (matched operating points, held-out seeds, 648-world sweep) | `sim/reunion_sim.py`, `sim/results/RUNLOG.md`, `figures/sim/S1–S6, S8` | **synthetic** |
| 7 | Power analysis (MDD for n = 80 / 294) | `sim/power_analysis.py`, `sim/results/POWER.md`, `S7` | synthetic |
| 8 | Measurement-protocol simulations: evaluation unit, forking paths, position bias | `sim/measurement_sim.py`, `sim/results/MEASUREMENT.md`, `S9–S11` | synthetic |
| 9 | **Evaluation toolkit** (ensemble-level metrics, cluster bootstrap, paired tests, un-mixing, risk–coverage, position bias) with a 12-check self-test | `tools/eval_toolkit.py`, `tools/adapters/README.md` | code, tested |
| 10 | Method redesign **v2** (measurement vs system separated; 7 mechanisms; honest prices) | `docs/04` | real prices + sim |
| 11 | Pre-registration template (disclosure, equivalence margins, stopping rule, frozen analysis) | `docs/05` | protocol |
| 12 | Runbook: next $100 as a decision tree with exact argv and ledger-derived costs; per-call logging spec | `docs/06` | **real** rates |
| 13 | Paper outline + figure-by-figure plan | `docs/07` | plan |
| 14 | Paper schematics | `figures/paper/P1–P3` | design |

## Not done — cannot be done from this VM

| item | why | what to do locally |
| --- | --- | --- |
| Any **accuracy / F1** analysis of the real runs | the export holds no outcome numbers | write the adapter (`tools/adapters/README.md`), then `tools/eval_toolkit.py --summary` |
| Any **new LLM run** (the $1 dilution test, M1 fusion check, L5-only E8 arm, …) | no API access here | `docs/06` Nodes 0–6, cheapest first |
| The **ladder field schema**, `e10_regate` rule, retriever, ground-truth source | not in the export | read `scripts/llm_reunion_agent.py`, `scripts/e10_regate.py`, the dataset builder |
| Whether the relay returns **logprobs** for GPT-4.1 / GPT-5.4 (M1 depends on it) | not in the export (documented only for GPT-4.1-mini) | one probe call per alias |
| **Duplicate prompts** of four kinds (test queries; records differing only by holder; query–candidate pairs; harness loops) | cache key not logged | hash prompts per call; dedupe before CIs |
| Outcome of the **10-25 00:20 restart** of the L5-P test campaign | export ends before it finished | `records/queue/api_campaign_pt.log`; a lock file dated 00:37 may block the next start |
| Writing into the user's local project | MFMCP unreachable for two days | pull this branch, or re-open the MFMCP tunnel |

## Decisions the user must make (in this order)

1. **Ladder schema:** keep the old rungs (and spend the next $100 on them) or adopt the nested v2 schema
   (`docs/05` §2.2; re-running the test ladder ≈ $74)? The runbook is schema-neutral up to Node 4.
2. **Paper claim:** the ladder measurement (panel's unanimous advice) with the system in an appendix?
3. **Pre-registration:** commit `docs/05` with the disclosure section filled in before the next test run?

## Caveats
- **[real]** numbers are verbatim relay values at ≈ 4.4× list prices; ratios transfer, dollars do not.
- **[sim]** numbers are synthetic; what transfers is the list of cheap real experiments, not the verdicts
  (`docs/04` §4). In ≥ 10 % of simulated worlds the retriever score alone beats the flagship LLM at L5.
- Reviewer personas (round 1 and red team) are simulations: adversarial and specific, not authoritative.
