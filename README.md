# newpaper — review, redesign and simulation workbench for the dispersed-heritage reunion project

This branch turns one artefact — the exported run ledger of the `newpaper` experiment campaign
(65 LLM runs, 9,178 API calls, $100 of relay charges, 22–25 Oct 2026) — into a critique, a redesign
and a set of calibrated simulations for the paper *"Can LLM agents reunite dispersed cultural-heritage
ensembles from catalogue evidence, and how much of that is memory?"*

Start here:

1. `STATUS.md` — what is done, what is not, what needs the local machine.
2. `docs/01_project_reconstruction.md` — the project as reconstructed from the ledger, with confidence tags.
3. `docs/03_review_panel_synthesis.md` — ten simulated top-venue reviewers, consensus blockers, priced action list.
4. `docs/04_method_redesign.md` — principles → mechanisms → priced, testable v2 design and measurement protocol.
5. `sim/README.md` — what the simulations assume, what they found, and which real $1–$5 experiments decide them.
6. `logs/worklog.md` — timestamped record of every step (Asia/Shanghai time).

Figures: `figures/real/` (from real data), `figures/sim/` (synthetic, labelled), `figures/paper/` (schematics).
Rebuild everything: `bash tools/run_all.sh` (≈6 min; `--fast` ≈ 30 s).

Raw input: `data/raw/newpaper_tool_output_export_20261025.md` (secret-scanned, no credentials).
