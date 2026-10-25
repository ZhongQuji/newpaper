# STATUS — what is done, what is not, what needs the local machine

Updated 2026-10-25 17:40 CST. Full timestamped trail: `logs/worklog.md`.

## Done in this repository (all reproducible with `bash tools/run_all.sh`, ≈6 min)

| # | deliverable | where | evidence type |
| --- | --- | --- | --- |
| 1 | Real experiment ledger parsed from the export: 65 runs, 9,178 calls, 15.15 M + 1.46 M tokens, $100.07, 17.7 h; served-model audit; failed runs; campaign log | `data/real/runs.csv`, `runs_summary.md`, `campaign_log_tail.txt` | **real** |
| 2 | Project reconstruction with confidence tags (task, ladder fingerprint, E5–E17 map, controls, unknowns) | `docs/01_project_reconstruction.md` | real + inference |
| 3 | Seven publication-style figures from the real ledger (ladder fingerprint, reasoning tax, cost of each road, budget breakdown, latency, campaign timeline, dev→test cost) | `figures/real/R1–R7.{pdf,png}` + `CAPTIONS.md` | **real** |
| 4 | Web-grounded related-work positioning (6 buckets, novelty verdict, must-cite list, scoop risks) | `docs/02_related_work_positioning.md` | literature |
| 5 | Ten-reviewer panel (NeurIPS stats, ICLR novelty, ACL contamination, CVPR multimodal, DH art history, CHI, SIGIR, AAAI cost, FAccT, Area Chair) + synthesis with 7 consensus blockers and a 12-step priced action list | `docs/reviews/`, `docs/03_review_panel_synthesis.md` | simulated reviewers; 5 factual claims re-verified against the ledger |
| 6 | Calibrated design-space simulation: 11 policy families × 3 model classes × L1/L5, real token prices, 216-world sensitivity sweep | `sim/reunion_sim.py`, `sim/results/`, `figures/sim/S1–S6, S8` | **synthetic** (labelled) |
| 7 | Statistical power of the ladder for n = 80 / 294 with ensemble clustering | `sim/power_analysis.py`, `sim/results/POWER.md`, `figures/sim/S7` | synthetic |
| 8 | Method redesign: 16 mechanisms from stated principles → priced, testable designs; v2 system; v2 measurement protocol; self-declared defects | `docs/04_method_redesign.md` | real prices + sim |
| 9 | Paper schematics (pipeline today vs v2, nested ladder, un-mixing) | `figures/paper/P1–P3` | design |
| 10 | Clean-room rebuild check: deleting all derived outputs and re-running reproduces `runs_summary.md`, `RUNLOG.md`, `POWER.md` byte-for-byte (modulo timestamps) | `tools/run_all.sh` | verification |

## Not done — cannot be done from this VM

| item | why | what to do locally |
| --- | --- | --- |
| Any **accuracy / F1 / MRR** analysis of the real runs | the export holds no outcome numbers (only `.out` / `reports/*.json` *names*) | run `tools/extract_real_runs.py`-style parsing on `records/queue/*_suite.json` **plus** the `reports/*.json`; join on `run_dir` |
| Any **new LLM run** (the $1 `--k 10` vs `--k 30` dilution test, cost-matched self-consistency, E8 on GPT-5.4…) | no API key / relay access here | §6 of `docs/03_review_panel_synthesis.md` lists them cheapest-first with real per-call prices |
| Confirming the **ladder field schema**, the `e10_regate` rule, the retriever and the ground-truth source | not in the export | read `scripts/llm_reunion_agent.py`, `scripts/e10_regate.py`, the dataset builder |
| Outcome of the **10-25 00:20 restart** of the L5-P test campaign (Gemini 3 Pro / Claude Opus 4.6 / GPT-5.4 all failed at 22:31 on 10-24) | export ends before it finished | check `records/queue/api_campaign_pt.log` |
| Writing into the user's local project | MFMCP server unreachable for two days (auth timeouts) | pull this branch, or re-open the MFMCP tunnel |

## Open questions the user should decide

1. Build the paper around the **ladder measurement** (panel's unanimous advice) or around the agent?
2. Adopt the **nested v2 ladder** (title removed above the physical-facts rung) — this changes every level's meaning and requires re-running the test ladder (≈ $40 for the four OpenAI models, by the dev→test cost predictor).
3. Pre-register the analysis plan (metric, regate rule, test-split comparisons) before the next test run?

## Caveats on this work

- Every number tagged **[real]** is a verbatim relay ledger value; the relay prices are ≈4.4× OpenAI list, so only ratios transfer to other providers.
- Every number tagged **[sim]** is from a synthetic world; use orderings and sensitivities, never absolute F1.
- Reviewer personas are simulations, not people; they are useful because they are adversarial and specific, not because they are authoritative.
