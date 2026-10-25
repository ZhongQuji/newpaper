# 07 · Paper outline and figure plan

Built around the one claim the panel converged on (docs/03 §4): **a leakage-controlled measurement of
how much of LLM "reunion" skill is evidence and how much is memory**, with the agent as reference
system, the dataset as vehicle, and cost as a first-class axis. Target: NeurIPS Datasets &
Benchmarks / ICLR (benchmark + diagnostic methodology); fallback: a DH venue with the same content.

Working title options (pick after the ladder result is in):
- *Reciting or Reasoning? A leakage-controlled benchmark for reuniting dispersed cultural-heritage ensembles with LLMs*
- *What the catalogue tells and what the model remembers: an information-ladder study of LLM reunion agents*

Each figure below is tagged **[have]** (exists in this repo, real data), **[have·sim]** (exists,
synthetic — use only as a methods illustration or move to appendix), **[needs real]** (template or
analysis exists, needs the local outcome data), or **[new]**.

## 1. Introduction (1 page)
- The problem: ensembles dismembered and dispersed across institutions; reunion is a set-valued
  record-linkage task over catalogue evidence (cite Fragmentarium, Broken Books, IDP; docs/02 bucket A).
- The confound: these records are in every pretraining corpus; an LLM may *recite* the reunion.
- Contributions (4 bullets): (i) benchmark + nested information ladder; (ii) evidence-free
  memorisation probe and the un-mixing estimator; (iii) a cost-tracked study of ~15 models with a
  frugal reference system; (iv) a measurement protocol (ensemble unit, paired CIs, pre-registration).
- **Fig. 1 [have → polish]** `figures/paper/P2_nested_ladder_v2` with one real example record walked
  down the rungs (needs one record from the local data to replace the abstract field names).

## 2. Related work (0.75 page) — docs/02 buckets A–F; must-cite list there (25 items).

## 3. Task and benchmark (1.5 pages)
- Sources, construction, ground-truth tiers, splits by ensemble, near-duplicate audit, licence audit.
- **Table 1 [needs real]** datasheet summary: ensembles, members, holders, countries, periods, types,
  fame terciles, licence histogram. **Fig. 2 [needs real]** map/period/type composition (small multiples).
- The ladder schema (Table 2 = docs/05 §2.2) and its token fingerprint **[have]** `figures/real/R1`.
- Shortlist construction and recall@K **[needs real]** (one line plot: recall vs K, with the
  prompt-token cost on the second axis — template `figures/sim/S4` **[have·sim]**).

## 4. Memorisation probes (0.75 page)
- Closed-book, evidence-free forced choice (both orders, matched counterfactuals), probe error.
- **Fig. 3 [needs real]** p_mem per model vs fame tercile; probe agreement with closed-book.

## 5. Systems (0.75 page)
- Reference listwise selector; frugal variants (retriever-prune, reject-only cascade); abstention.
- **Fig. 4 [have → adapt]** `figures/paper/P1_pipeline_today_vs_v2` (keep (b) only, as the system figure).

## 6. Results (3 pages)
- **Fig. 5 — the headline [needs real]**: ladder plot per model, test split, pairwise F1 with
  ensemble-bootstrap CIs, **stratified** memorised / non-memorised (schematic: `figures/paper/P3`
  **[have]**; synthetic version `figures/sim/S5` **[have·sim]**). Hypotheses H1–H3 of docs/05.
- **Table 3 [needs real]**: full test table — recall@30 row, shortcut-heuristic row, closed-book row,
  each rung × model, pre/post-regate, USD and tokens per query, seeds, shuffled-order replicate.
- **Fig. 6 [have·real]** cost structure: `figures/real/R2` (reasoning tax) + `R3` (cost of each road)
  — these are already final; add the quality axis once real F1 exists → becomes the Pareto plot
  (template `figures/sim/S1`/`S2` **[have·sim]**).
- **Fig. 7 [needs real]** risk–coverage / precision at ≥95 % (template `figures/sim/S6` **[have·sim]**).
- **Fig. 8 [needs real]** position-bias diagnostic (recall by shortlist third, ordered vs shuffled;
  template `figures/sim/S11` **[have·sim]**).
- Visual rung: MLLM vs CLIP/SigLIP/DINOv2 cosine baseline **[new; needs GPU minutes]**.

## 7. Measurement protocol and statistical notes (0.5 page + appendix)
- Ensemble as unit, paired comparisons, MDD **[have·sim]** `figures/sim/S7`; evaluation-unit
  divergence and transitivity **[have·sim]** `figures/sim/S9`; forking-paths optimism of the post-hoc
  rule **[have·sim]** `figures/sim/S10`; pre-registration hash.

## 8. Limitations, ethics, release (0.5 page)
- Western-canon pool; Wikidata `part of` as one reconstruction; provenance sensitivity; relay prices
  ≈ 4.4× list; non-pinned served labels; what is not released and why (docs/reviews/reviewer_09).

## Appendix
- A. Ledger of all runs **[have]** `data/real/runs_summary.md`, campaign timeline `figures/real/R6`,
  dev→test cost predictability `R7`, latency `R5`, budget breakdown `R4`.
- B. Design-space simulation (what it assumes, what it found, which real experiment decides it)
  **[have·sim]** `sim/README.md`, `figures/sim/S1–S3, S8`.
- C. Prompts per rung, regate rule, adapter and toolkit **[have]** `tools/eval_toolkit.py`.
- D. Datasheet and licence audit **[needs real]**.

## Figure style
All figures through `tools/figstyle.py` (Okabe–Ito palette, 3.4 / 7.0 in widths, Type-42 PDF). Model
colours are fixed across the paper (GPT-4.1 mini sky, GPT-4.1 blue, GPT-5.4 mini orange, GPT-5.4
vermilion); rung colours run dark-blue → orange along the ladder (`figstyle.LEVEL_COLORS`).

## What must come from the local machine before any results section can be written
decisions.csv for every run (tools/adapters), gold membership with tiers, retriever scores,
prompt hashes, served-model labels, images' pixel sizes. Everything else in this repo is ready.
