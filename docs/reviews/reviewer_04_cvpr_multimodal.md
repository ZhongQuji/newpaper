# Reviewer 04 — CVPR/ECCV (computer vision for cultural heritage)

## Summary of the submission as I understand it
The submission proposes LLM/MLLM agents that select, from a 30-candidate shortlist, the records belonging to the same dispersed ensemble as a query object. Vision enters in three places: E7, a pairwise MLLM verifier (`mllm_pair_verify.py --conditions V0,V4 --score-only`, first-token P(yes), 754 calls); E10c, a visual gate scored once on 229 selected pairs and replayed over three text runs; and E16, a "visual reunion" that re-scores the top-8 of a local Qwen3-VL-2B shortlist (160 calls per run, ~3.1k prompt tok/call). All visual runs are dev-only (80 queries), on GPT-4.1-mini and GPT-4.1. No accuracy numbers are available to me; the critique is conditional.

## Scores (1–10) with one-line justification each
- Novelty: 6 — the application (reunion across institutions) is new to vision venues; asking an MLLM "same ensemble?" is not.
- Technical soundness: 4 — no classical or embedding baseline, thumbnail-scale pixel budgets, a recall ceiling inherited from a 2B model.
- Evaluation rigour: 4 — visual experiments are dev-only, one model family, metric undefined.
- Clarity (of the design, as reconstructed): 5 — conditions V0/V4, the resize/detail setting and `media_usability` thresholds are opaque.
- Impact / significance: 7 — curators and conservators would use this if it works; the dataset may outlive the method.
- Overall: 4 — reject at a vision venue as it stands; 6–7 with the baselines and resolution study below.

## Strengths
- Vision is used as a verifier/gate over a text shortlist, the right place for an expensive MLLM, and E10c's score-once-replay-many design is economical.
- `--balance-source` in E7 shows awareness that data source (NGA vs Commons) is a photographic-style confound.
- Image hygiene exists upstream (`media_integrity`, `media_usability`, `near_duplicates` reports), rare in LLM papers.
- First-token P(yes) with one completion token yields a continuous score at $0.0017–0.0018 per pair.

## Weaknesses
1. **No vision baseline at all (BLOCKER).** No SIFT/ORB or edge-contour matching, no CLIP/SigLIP/DINOv2 retrieval, no colour/texture/craquelure statistics. Without a frozen-embedding cosine baseline on the same 30-candidate shortlists, nothing shows the MLLM's P(yes) adds anything over a 2023 self-supervised backbone.
2. **Pixel budget is thumbnail-scale (MAJOR).** E7/E10c spend 1,005–1,018 prompt tokens per image *pair* including instructions (≲ 450 per image); E16 spends ~3.1k for nine records' text plus, presumably, nine images (~270 per image). In OpenAI's accounting that is a single 512-px tile. Near-identical E16 prompt counts for GPT-4.1 and GPT-4.1-mini (3,032 vs 3,051 at L5; 3,195 vs 3,214 at L3), despite different image-token schemes, confirm images are a small, low-detail share. Punch marks, wood grain, ruling and craquelure are invisible at this scale.
3. **E16's recall ceiling is set by a 2B model (MAJOR).** `--from-run 20261013_*_Qwen3-VL-2B-Instruct --k 8`: the flagship re-scorer sees only the top-8 of a run of unknown quality — a 73 % cut before any strong model sees a pixel. Report oracle recall@8; below ~80 %, E16 demonstrates nothing about visual reasoning.
4. **No visual closed-book control (MAJOR).** Famous panels are recognisable from the image alone — these models have seen the Commons files. Nothing asks "name this work" from pixels, so a high visual P(yes) may be visual memorisation. Also: bytes, or Commons URLs/filenames (which contain the ensemble name)?
5. **Photographic-campaign shortcut (MAJOR).** Panels from one ensemble in one museum share photography (background, colour calibration, cropping). If E7 negatives are random, "same photo campaign" explains separability; if `--balance-source` balances only NGA vs Commons, holder-level style is uncontrolled.
6. **Set-valued metric undefined (MAJOR).** What `e10_regate` scores is invisible. Pairwise F1, exact-set match and ensemble-level ARI/B-cubed disagree sharply when ensembles have 2 vs 12 members; per-query scoring over-weights large ensembles and ignores transitivity (A→B, B↛A). 294 test queries span far fewer ensembles; cluster CIs by ensemble.
7. **The gate is precision-only and tiny (MINOR).** E10c touches 229 unique pairs across 3×80 query-runs (≈ 2.9 per query); it can only remove selections, never recover misses — report flip counts, not rates.
8. **`media_usability` is a black box (MINOR; MAJOR if it drives the subset).** No threshold, no pixel distribution, no fraction of gold pairs with usable images on both sides. If usability skews to famous, well-photographed works, visual results sit on the most memorised slice.
9. **Coverage (MINOR).** Vision runs exist only for GPT-4.1-mini (E7, E10c, E16) and GPT-4.1 (E16), dev only; `20261024_042813_e16_visual_L3_xj-gpt-4.1` failed (rc=1 after 9 calls); E16 makes 2 calls per query — say why.

## Experiments or artefacts that would change my score
1. DINOv2-L/14 and SigLIP cosine between query and all 30 candidates: recall@k of the embedding ranking and AUROC on the E7 pairs. Convinces me if MLLM P(yes) beats the best embedding AUROC by ≥ 0.05 and a fusion beats both.
2. Resolution ablation for E7: 256 / 512 / 1024 / 2048-px long side (or `detail: high`), same pairs. Convinces me either way: rising AUROC makes current numbers a lower bound; flat AUROC means surface detail is not being read.
3. Oracle recall@8/@30 of the Qwen3-VL-2B and main shortlists, per level. Convinces me if recall@8 ≥ 85 %; otherwise rerun E16 on a DINOv2 top-8.
4. Image-only closed-book on the 80 dev query images ("name the work and its ensemble"). Convinces me if visual gains at L5/L6 survive on the subset the model cannot name.
5. Hard-negative E7 with same-holder, same-creator and same-period negatives, AUROC per negative type. Convinces me if same-holder AUROC is within 0.05 of random-negative AUROC.
6. Metric definition plus pairwise F1, exact-set match and ARI after transitive closure on the same runs, with ensemble-clustered bootstrap CIs. Convinces me if conclusions are stable across all three.
7. `media_usability` spec, histogram of long-side pixels, results by resolution tercile. Convinces me if the visual gain survives in the lowest tercile.
8. Error gallery: 20 E7 false positives and 20 false negatives with images, separating workshop copies and re-photographed plates from genuine confusions.

## Token-efficiency / cost critique
E16 is the dearest non-agentic run: $4.70 per 80 queries on GPT-4.1 ($0.059/query, 2 calls × 3.1k tokens) to re-score 8 candidates — 3–5× the per-query tokens of the 30-candidate text agent. Nine ~270-token thumbnails per call is the worst of both worlds: too few pixels to see material evidence, too many images to afford `detail: high`. E7 and E10c, at one completion token and ~$0.0018/pair, are cheap and under-used: scoring all 80×30 = 2,400 dev pairs costs ~$4.4 and would turn the gate into a reranker. Cheap and missing: a one-time DINOv2/SigLIP embedding pass over every image (minutes on the GPU that ran Qwen3-VL-2B, $0 per query).

## One idea the authors have not tried
Late-fuse the free signal with the expensive one. (1) Embed every image once with DINOv2-L/14: CLS plus a 4×4 grid of patch-pooled descriptors; store cosine s_glob and max-over-cells s_loc for every (query, candidate) pair. (2) Add dimension compatibility d = |h_q − h_c| / max(h_q, h_c) from the L5 fields. (3) Fit on dev a 4-feature logistic model on [P(yes)_MLLM, s_glob, s_loc, d]; report test AUROC/F1 against each single feature. (4) Route only pairs with |logit| < τ to a second MLLM call at `detail: high` on two crops (top/bottom edges for predella and wing panels, margins for leaves) to test edge and ruling continuity. Cost: one GPU pass plus ≤ 20 % of current E7 calls at higher resolution — and it tells a conservator which cue drove the match.

## Confidence (1–5) and what I could not assess
4 on the methodological critique, 2 on outcomes. I could not see conditions V0/V4, resize/detail settings, any image, `media_usability` thresholds, the ground truth, the metric, or the Gemini/Claude/Qwen3-VL runs. If the paper already includes an embedding baseline and a resolution study, weaknesses 1–2 drop to MINOR and my overall rises to 6.
