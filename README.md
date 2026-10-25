# newpaper — review, redesign and simulation workbench for the dispersed-heritage reunion project

This branch turns one artefact — the exported run ledger of the `newpaper` experiment campaign
(65 LLM runs, 9,178 API calls, $100 of relay charges, 22–25 Oct 2026) — into a critique, a redesign
and a set of calibrated simulations for the paper *"Can LLM agents reunite dispersed cultural-heritage
ensembles from catalogue evidence, and how much of that is memory?"*

Start here:

1. `STATUS.md` — what is done, what is not, what needs the local machine.
2. `docs/01_project_reconstruction.md` — the project as reconstructed from the ledger, with confidence tags.
3. `docs/03_review_panel_synthesis.md` — ten simulated top-venue reviewers, consensus blockers, priced action list, and the round-2 red-team of this repository's own work.
4. `docs/04_method_redesign.md` — v2: the measurement (nested ladder, memory-keying test, stratification, counterfactuals, canaries, statistics) kept separate from the frugal system (retriever-score fusion, read less, three-way output, diagnostic verification).
5. `docs/05_preregistration_template.md`, `docs/06_runbook_next_100usd.md`, `docs/07_paper_outline_and_figure_plan.md` — what to commit before the next test run, what to run for the next $100 (exact commands, ledger-derived costs), and how the paper is laid out.
6. `sim/README.md` — what the simulations assume, what they found after the red-team corrections, and which real $1–$5 experiments decide them.
7. `tools/eval_toolkit.py` — ensemble-level metrics, cluster bootstrap, paired tests, un-mixing, risk–coverage, position bias (`--selftest`).
8. `logs/worklog.md` — timestamped record of every step (Asia/Shanghai time).

Figures: `figures/real/` (from real data), `figures/sim/` (synthetic, labelled), `figures/paper/` (schematics).
Rebuild everything: `bash tools/run_all.sh` (≈12 min; `--fast` ≈ 1 min).

Raw input: `data/raw/newpaper_tool_output_export_20261025.md` (secret-scanned, no credentials).
