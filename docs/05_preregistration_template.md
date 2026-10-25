# 05 · Pre-registration — the memory-vs-evidence ladder for dispersed-heritage reunion

> Fill in every `⟨ ⟩`, commit this file, and record the commit hash **before** the first test-split
> run of the pre-registered conditions. Anything decided after that hash is exploratory and is
> reported in a separate "exploratory" section of the paper. This closes blocker B6 (undisclosed
> post-hoc rule), pre-empts B1/B2 (unpowered, wrong unit) and makes the ladder claim falsifiable in
> either direction (the Area Chair's advice, docs/03 §4).

## 0. Administrative

- Pre-registration commit: `⟨hash⟩`, date `⟨YYYY-MM-DD⟩`, authors `⟨…⟩`.
- Status of the test split at this commit: the test split has been run at **L1, L2-T, L3-H, L5**
  for some models already (ledger `data/real/runs.csv`); those runs are **not** covered by this
  pre-registration and will be reported as "pilot/exploratory". All conditions listed in §3 will be
  **re-run** with the frozen pipeline of §2 so that every pre-registered number comes from a run
  made after this commit.

## 1. Hypotheses (state direction and a minimum effect that would matter)

H1 (ladder). Mean pairwise F1 on the **non-memorised stratum** decreases monotonically along the
nested rungs L1 ⊃ L2 ⊃ L3 ⊃ L4 ⊃ L5; the L1→L5 drop is ≥ `⟨δ₁ = 0.10⟩` for every model in §3.
  *Falsifier:* drop < δ₁ with the 95 % CI excluding δ₁ → the models reason over physical facts and
  the catalogue words are not needed — a result we commit to reporting as the headline if it occurs.

H2 (memorisation). The share of test queries solved by the evidence-free forced-choice probe
(§2.4) is ≥ `⟨π₀ = 0.20⟩` for at least one flagship model, and accuracy on that stratum is
level-independent (|slope| across rungs < `⟨0.03⟩` per rung).

H3 (physical channel). L5 − L5-P (dimensions permuted) ≥ `⟨δ₃ = 0.05⟩` on the non-memorised stratum
(the model uses dimensions when that is all it has). *Falsifier:* no difference → L5 performance is
not evidence-driven and must be attributed to residual leakage or memory.

H4 (cost). At equal relay cost, the pre-registered frugal policy (§2.3) is within `⟨0.02⟩` F1 of the
flagship listwise K=30 baseline at ≤ `⟨70⟩` % of its cost. *Falsifier:* worse by more than 0.02.

## 2. Frozen pipeline (no change after the commit)

### 2.1 Data
- Dataset snapshot id / git hash of the builder: `⟨…⟩`; crawl dates: Wikidata `⟨…⟩`, Commons `⟨…⟩`, NGA `⟨…⟩`.
- Ground truth: "same ensemble" = `⟨Wikidata P361/P527 chain | curated literature | both⟩`; confidence
  tiers `⟨A: literature-attested; B: Wikidata only; C: contested⟩` are recorded per ensemble and
  results are reported per tier.
- Splits: dev = 80 queries / `⟨n_ens⟩` ensembles; test = 294 queries / `⟨n_ens⟩` ensembles; split made
  **by ensemble** (no ensemble spans both splits). Duplicate / near-duplicate queries removed
  (`near_duplicates` report, threshold `⟨…⟩`); the model-independent cache hits on test
  (3 on every L1 test run, docs/03 B6b) have been traced to `⟨…⟩` and resolved by `⟨…⟩`.
- Shortlist: first-stage retriever = `⟨method⟩`, K = 30, candidates presented in **random order**
  (seeded per query); recall@30 of gold on test = `⟨…⟩` (reported in the main table).
  "No gold in shortlist" cases: `⟨n⟩` test queries (if 0, `⟨m⟩` negative-only shortlists are injected).

### 2.2 Rungs (field schema; each a strict subset of the rung above)
| rung | fields shown | fields removed vs rung above |
| --- | --- | --- |
| L1 | `⟨…⟩` | — |
| L2 | `⟨…⟩` | title |
| L3 | `⟨…⟩` | holder, accession number, credit line, image-URL host |
| L4 | `⟨…⟩` | creator / workshop / Notname |
| L5 | dimensions, support, medium, technique, date band, iconography keywords | all remaining person/place words |
| L5-P | L5 with dimensions permuted across candidates (seed `⟨…⟩`) | the physical channel (control) |
| L6 | images only (+ dimensions) | all text |
Prompt-token fingerprint of each rung on dev (mean tokens/query) will be reported as a sanity check.

### 2.3 Systems
- Reference: `scripts/llm_reunion_agent.py --k 30 --level ⟨rung⟩`, temperature `⟨0⟩`, prompt
  version `⟨hash⟩`, output = JSON id list. **`e10_regate.py` is frozen at rule `⟨rule text⟩`,
  chosen on dev only; both pre- and post-regate numbers are reported.**
- Frugal policy (H4): retriever-prune p ≥ `⟨0.02⟩` → flagship listwise, *or* mini@L5 reject-only
  screen (p̂ < `⟨0.05⟩`) → flagship@L1 on survivors — exactly one of these two, chosen on dev: `⟨…⟩`.
- Models: `⟨xj-gpt-4.1-mini, xj-gpt-4.1, xj-gpt-5.4, xj-gpt-5.4-mini (reasoning_effort=low)⟩`;
  served-model label pinned to `⟨…⟩`; runs with any unpinned/served-other call are flagged.
- Seeds: `⟨3⟩` independent runs per headline cell (L1, L5, L5-P on test); one **shuffled-order**
  replicate per headline cell.

### 2.4 Memorisation probe
- Evidence-free forced choice: query shown as `⟨id only | id + one neutral field⟩`; options = true
  partner vs a counterfactual matched on `⟨period, object type, size class⟩`; both orders; a query is
  "memorised" if both orders are correct with P(yes) margin ≥ `⟨…⟩`. Probe error rates (fpr, fnr)
  estimated on `⟨n⟩` hand-labelled queries and propagated via `eval_toolkit.unmix`.
- Closed-book baseline (E5) run on **test** for every model.

## 3. Pre-registered conditions and budget (ledger-based estimates; `docs/06_runbook…`)

| condition | models | split | seeds | est. USD |
| --- | --- | --- | --- | ---: |
| L1, L2, L3, L4, L5, L5-P | 4 | test | 1 | `≈ 85` |
| L1, L5, L5-P extra seeds | 4 | test | +2 | `≈ 60` |
| shuffled-order replicate at L1, L5 | 4 | test | 1 | `≈ 40` |
| forced-choice probe, both arms | 4 | test | 1 | `≈ 20` |
| closed-book | 4 | test | 1 | `≈ 5` |
| frugal policy (H4) | 2 | test | 2 | `≈ 10` |
| **total** | | | | **≈ 220** |

## 4. Analysis plan (frozen)

- **Unit:** ensemble. Metrics: pairwise P/R/F1 (primary), exact-set accuracy, B-cubed F1 and ARI on
  correlation-clustered output (secondary); contradiction rate reported.
- **Uncertainty:** 95 % CIs by ensemble-level bootstrap (B = 2,000); all rung-vs-rung comparisons are
  **paired** (same queries) via paired ensemble-bootstrap on F1 and McNemar on exact-set.
- **Multiplicity:** H1–H4 are 4 primary tests → Holm at α = 0.05 within each model; the per-rung
  monotonicity check is descriptive.
- **Power:** MDD at n = 294, 80 % power ≈ 7–9 accuracy points (`sim/results/POWER.md`); dev is for
  tuning and pilots only — no dev number appears in a claim.
- **Stratification:** every ladder figure shows memorised / non-memorised strata and fame terciles
  (`commons_views`, `nga_views`) side by side; the un-mixed evidence-only accuracy with CI is the
  headline number for H1.
- **Cost:** every table row carries relay USD/query and prompt+completion tokens/query; the headline
  figure is F1 vs cost with CIs.
- **Exclusions:** runs with `api_errors > 0` are re-run, not patched; served-model mismatches are
  excluded and counted.

## 5. What we will report regardless of outcome
The full ladder table for every model on test with CIs; recall@30; the shortcut-heuristic baseline
row; pre- and post-regate numbers; the probe's p_mem per model; failed/excluded runs; total spend.

## 6. Deviations
Any change to §2–§4 after the commit is logged here with date, reason and a diff, and the affected
result moves to the exploratory section.

| date | section | change | reason |
| --- | --- | --- | --- |
| | | | |
