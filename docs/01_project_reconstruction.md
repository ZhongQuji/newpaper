# 01 · Project reconstruction from the exported run ledger

**Source of truth.** Everything in this document is inferred from one artefact: the
tool-call export of the `newpaper` window (`data/raw/newpaper_tool_output_export_20261025.md`,
8,285 lines, 53 suite-state JSON dumps written by the local campaign runner between
2026-10-22 11:07 and 2026-10-25 00:20 CST). The export contains **script names, CLI flags,
run directories, report file names, API call counts, token counts, relay costs and wall times**.
It does **not** contain the paper text, the data files, or any accuracy numbers (the `.out`
files and the `reports/*.json` are listed by name only). Every statement below is therefore
tagged with a confidence level:

- **[verbatim]** copied from the export;
- **[inferred-high]** the only reasonable reading of several consistent file/flag names;
- **[inferred-medium]** plausible reading, one or two alternatives exist;
- **[unknown]** cannot be determined from the export — must be checked against the local repo.

The companion machine-readable ledger is `data/real/runs.csv` (65 distinct runs) and the
aggregate summary is `data/real/runs_summary.md`.

---

## 1. What the paper is about

**Task [inferred-high].** *Digital reunion of dispersed cultural-heritage objects.* A query
object (a panel, leaf, fragment or sheet that is now a separate museum record) must be
matched with the other surviving members of the ensemble it originally belonged to
(polyptych / altarpiece, album, manuscript, cut-up scroll, print series …), which today sit
in **different holding institutions**. Evidence for this reading:

| clue in export | reading |
| --- | --- |
| `llm_reunion_agent.py`, `e16_visual_reunion.py` | the core verb is *reunion* |
| `--holder-scrub v2`, level `L3-H` | the *holder* (owning museum) is a metadata field that can leak membership and is scrubbed |
| `--mask-creator` | the *creator* (artist / workshop) is a metadata field whose memorised associations must be controlled |
| `--withhold-title`, level `L2-T` | the *title* often spells out the ensemble ("… from the X Altarpiece") |
| `--dims-permute` (level `L5-P`) | physical *dimensions* are an evidence channel at the most austere level |
| reports `custody_events`, `commons_identity`, `commons_views`, `nga_views`, `wikidata_deep`, `wikipedia_dump`, `oa_fulltext`, `membership_evidence`, `fact_cards`, `near_duplicates`, `media_integrity`, `media_usability`, `temporal_ladder`, `text_screen`, `quality_audit`, `literature_enrich`, `release_validation` | the dataset was assembled from Wikidata + Wikimedia Commons + National Gallery of Art open data + Wikipedia + open-access literature, with provenance ("custody") events, image integrity/usability audits, near-duplicate screening, a temporal ladder (date-stratified leakage probe) and a release-validation gate |
| `mllm_pair_verify.py --conditions V0,V4 --score-only` | a multimodal pair-verification probe (images of two fragments → first-token P(yes)) |

**Research question [inferred-high].** *Can LLM / MLLM agents reassemble dispersed ensembles
from catalogue evidence, and how much of their apparent skill is memorisation of famous
cases rather than reasoning over the evidence shown?* The experiment grid is built almost
entirely around separating **evidence-driven** from **memory-driven** performance.

## 2. The information-level ladder (the paper's central manipulation)

[inferred-high for the ordering; the exact field sets per level are **unknown**.]
Prompt tokens per call are a near-perfect fingerprint of how much metadata each level shows
(identical across the four OpenAI-family models, `data/real/runs.csv`):

| level | flags | prompt tok / call (dev) | reading |
| --- | --- | ---: | --- |
| **L1** | `--level L1` | 1,959 | full catalogue record for query + 30 candidates |
| **L1 v2 inputs** | `--inputs v2` | 3,391 | richer record (adds enrichment fields; ~1.7× tokens) |
| **L2-T** | `--level L2-T` | 2,316 (only 32/80 dev, 91/294 test queries) | *title-leak subset*: queries whose title names the ensemble; title withheld, something longer substituted (description?) [inferred-medium] |
| **L3** | `--level L3` | 1,784 | reduced record (creator/date kept, free text dropped?) |
| **L3-H** | `--level L3-H` | 1,735 | L3 with **holder** scrubbed; `--holder-scrub v2` → 1,705 (stronger scrub) |
| **L5** | `--level L5` | 1,208 | austere record: physical facts (dimensions, medium, date) |
| **L5-P** | `--level L5 --dims-permute 20261024` | 1,219 | L5 with dimensions permuted across candidates → if accuracy survives, the model is not using dimensions |
| **L6** | `--level L5 --withhold-title` | 1,064 | L5 minus title: the floor of the ladder |

Each level is paired with two automatic follow-ups [verbatim]: `e10_regate.py` (re-gates
the agent's shortlist decisions, probably with a stricter/independent acceptance rule) and
`e10_shortlist_controls.py` (shortlist-level controls; the `shortlist_shortcuts` report
suggests it measures how far trivial heuristics — same holder, same creator, same title stem —
already solve the shortlist).

## 3. Experiment map (E-numbers as used by the campaign runner)

| E | script | what it measures [inference] | real scale per run |
| --- | --- | --- | --- |
| **E5** closed-book | `llm_eval_harness.py --task t0_closedbook` | memory-only baseline: can the model name the ensemble with no candidates? | 80 calls, 137 prompt tok/call |
| **E6** rerank | `llm_eval_harness.py --task t1_rerank --k 30` | single-shot listwise rerank of a 30-candidate shortlist at L1 / L5 | 40 calls, 2.0k / 1.2k tok/call |
| **E7** pair verify | `mllm_pair_verify.py --conditions V0,V4 --score-only --balance-source` | MLLM image-pair verification, first-token P(yes), balanced over source | 754 calls, 1 completion token each |
| **E8v4** counterfactual forced choice | `llm_cf_forced_choice.py --n 100 --both-orders [--withhold-evidence --mask-creator]` | memorisation probe: forced choice between the true partner and a counterfactual; both presentation orders; with evidence withheld and creator masked the only remaining signal is memory | 600 calls |
| **E9** T5 profile | `llm_t5_profile.py --level L1 --n 80` | per-query profile / attribute prediction (task "T5") [inferred-medium] | 80 calls |
| **E10** reunion agent | `llm_reunion_agent.py --k 30 --level …` | **main method**: agent selects members from a 30-candidate shortlist at a given level | 80 (dev) / 294 (test) calls |
| **E10c** visual gate | `e10_visual_gate.py --score … --replay` | MLLM visual gate scored once, then replayed over several E10 runs (cheap re-use) | 229 calls |
| **E10e** pointwise rerank | `llm_pointwise_rerank.py --from-run …` | pointwise alternative to the listwise agent | 80 calls, **7.2k tok/call, 79 s/call** |
| **E15** deep-research harness | `deep_research_harness.py --policy llm --max-steps 30 --max-tokens 200` | tool-using agentic baseline over a closed pool | 40 queries, 8.3k tok/query |
| **E16** visual reunion | `e16_visual_reunion.py --from-run <Qwen3-VL-2B run> --k 8` | multimodal re-scoring of a local Qwen3-VL-2B shortlist, top-8 | 160 calls, 3.1k tok/call |
| **E17** open pool | `deep_research_harness.py --pool open --stride 4 --max-steps 14` | open-world retrieval (no shortlist) | 20 queries, **25k tok/query, $0.22/query** |

Model roster seen in report names [verbatim]: GPT-4.1, GPT-4.1-mini, GPT-5.4, GPT-5.4-mini,
Gemini 2.5 Flash / Flash-thinking / Pro, Gemini 3 Pro, Claude Haiku 4.5 / Sonnet 4.6 / Opus 4.6,
Qwen3.5 27B / 122B / 397B, MiMo v2.6 Flash / Pro, local Qwen3-VL-2B-Instruct. Only the four
OpenAI-family models have usage ledgers in this export; the others ran in other windows.

Splits [verbatim]: dev = 80 queries, test = 294 queries; L2-T subset = 32 dev / 91 test.

## 4. Controls already in place (a strength of the project)

1. Served-model audit on every call (0 mismatches across 9,178 calls) [verbatim].
2. Prompt-variant (`v1`, `v2`) and replicate (`--replicate 1`) runs at L1 for prompt-sensitivity and sampling variance [verbatim].
3. Both-orders presentation in forced choice [verbatim].
4. Holder scrub, creator mask, title withholding, dimension permutation — one ablation per leakage channel [verbatim flags].
5. Temporal ladder report → date-stratified contamination probe [inferred-high].
6. Near-duplicate and media-integrity audits before release [inferred-high].

## 5. Real cost structure (verbatim totals, `data/real/runs_summary.md`)

- 65 runs, 9,178 calls, 15.15 M prompt + 1.46 M completion tokens, **$100.07**, 17.7 h wall.
- The listwise agent (E10 family) is 54 % of calls but **74 % of cost** ($74.5).
- **Reasoning tax:** GPT-5.4-mini emits 475–766 completion tokens per call where GPT-4.1 /
  GPT-5.4 emit 60–90; its cost per call ($0.016–0.023) equals the two flagships' ($0.018–0.024)
  and is 4–5× GPT-4.1-mini's ($0.004). A "mini" thinking model is *not* the cheap option here.
- **Pointwise is the expensive road:** E10e costs 3.0× the listwise L1 run and 14× its wall time.
- **Deep research is the very expensive road:** E17 open-pool costs ≈ 11× per query what the
  shortlist agent costs at L1 on the same model (GPT-5.4: $0.22 vs $0.020).

## 6. What is unknown and must be verified against the local repository

- The exact metadata fields shown at each level, and the acceptance rule of `e10_regate`.
- All accuracy / F1 / MRR numbers (none are in the export).
- How the 30-candidate shortlist is produced (lexical? embedding? metadata blocking?).
- The ground-truth source for "same ensemble" (Wikidata `part of`? curated literature?).
- Whether the 10-25 00:20 restart of the L5-P test campaign (Gemini 3 Pro, Claude Opus 4.6,
  GPT-5.4) succeeded — the 10-24 22:31 attempt failed on all three (`data/real/campaign_log_tail.txt`).
