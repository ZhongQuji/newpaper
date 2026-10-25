# 02 · Related-work positioning map (2015–2026)

**Scope.** Closest prior work to the *digital reunion* project in `01_project_reconstruction.md`
(LLM/MLLM agents selecting dispersed ensemble members from Wikidata/Commons/NGA records + images;
ladder L1→L6; counterfactual forced choice; cost ledger over ~15 models). Searched 2026-10-25.
**Tags:** `[opened]` = full text fetched and inspected; `[snippet]` = seen only in search snippets/abstracts. Unverifiable items were dropped.

## A. Computational reassembly of dispersed / fragmented heritage

| work | venue / year | what it does | how this project differs | URL |
| --- | --- | --- | --- | --- |
| Fragmentarium (Univ. Fribourg) | platform, 2015– | IIIF lab to catalogue and *manually* assemble medieval leaves/cuttings across libraries | reunion done by scholars; we automate member selection from metadata and audit memorisation | https://fragmentarium.ms/pages/about/digital-laboratory `[snippet]` |
| Broken Books / Beauvais Missal (Davis) | *Digital Philology* 2024 | hand-traced reconstruction, 122 of 309 leaves in 25 states / 6 countries | expert, case-by-case; we evaluate machine selection over 374 queries | https://doi.org/10.1353/dph.2024.a926884 `[snippet]` |
| International Dunhuang Programme | BL platform, 1994–; relaunch 2024 | aggregates 35+ institutions' holdings; no automatic join finding | aggregated catalogues are our *input* | https://idp.bl.uk/about/ `[snippet]` |
| Reunion helper (Zheng, Li, Weng) | *Heritage Science* 2024 | CNN edge matcher for Dunhuang sibling-fragment identification; >97 % on in-house edge dataset | fracture-edge pixels; ours are *whole* objects matched by metadata + whole-image cues | https://www.nature.com/articles/s40494-024-01150-3 `[opened]` |
| LLMCO4MR (Zhang et al.) | ECCV 2024 | neural combinatorial solver picks Top-K fragments, then GPT-4V/LLaVA scores pairs + direction; synthetic shredding, grid layout, Dunhuang cases | closest LLM precedent: physical fragments of one collection, no catalogue text, no memorisation control, 2 MLLMs, no cost | https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09585.pdf `[opened]` |
| Oracle-bone rejoining: S3-Net/OB-Rejoin; SFF-Siam; DRM + OBFI | KDD 2022; IEEE CG&A 2023; *npj Heritage Science* 2025 | Siamese contour/texture matching, gallery retrieval; OBFI = 5,374 images, 138k patches | same retrieve-the-partner shape, geometric signal only | https://doi.org/10.1145/3534678.3539050 `[snippet]`; https://doi.org/10.1038/s40494-025-01651-9 `[opened]` |
| Papyrus / Genizah retrieval (Papy-S-Net, ViT-ED; feature-mixing; Genizah join retrieval) | ICDAR-HIP 2019, ICDAR 2024; HIP 2023; PRIMA 2026 | writer/page and join retrieval by deep metric learning on handwriting crops | palaeographic image signal; no LLM, no metadata | https://geshaem.huma-num.fr/wp3.html `[snippet]`; https://arxiv.org/html/2306.12939 `[snippet]`; https://beratkurar.github.io/papers/PRIMA2026Genizah.pdf `[snippet]` |
| RePAIR (Tsesmelis et al.) | NeurIPS 2024 D&B | 1,070 Pompeii fresco fragments, 117 solved groups; 2D/3D puzzle baselines | contiguous puzzles; our members are non-contiguous records in different museums | https://doi.org/10.48550/arxiv.2410.24010 `[opened]` |
| Polyptych reunions: Griffoni (Factum), Augustinian (Poldi Pezzoli 2024), Bandini Icon AR | 2012–2020; 2024; 2020s | curatorial/physical/AR reassembly of known panel sets | membership known a priori; we test its *discovery* | https://factumfoundation.org/our-projects/digitisation/the-polittico-griffoni/ `[snippet]` |
| Visual link discovery (Seguin et al.; ArtMiner) | ECCV-W 2016; CVPR 2019 | CNN retrieval of visual links / near-duplicate motifs (1,587 Brueghel works) | pattern reuse, not membership; no LLM | https://openaccess.thecvf.com/content_CVPR_2019/html/Shen_Discovering_Visual_Patterns_in_Art_Collections_With_Spatially-Consistent_Feature_Learning_CVPR_2019_paper.html `[snippet]` |

## B. Entity resolution / record linkage for museum & library records

| work | venue / year | what it does | how this project differs | URL |
| --- | --- | --- | --- | --- |
| Heritage Connector (Dutia & Stack) | *Applied AI Letters* 2021 | ML record linkage of Science Museum Group catalogue to Wikidata, 85 %+ precision, laptop-scale models | identity links (same object/person); ours is *part-of* membership across institutions | https://doi.org/10.1002/ail2.23 `[snippet]` |
| Polley et al.; AIC provenance linking; LLM-in-the-loop provenance (Chinese art) | ASIS&T 2021; *Zbornik* 2024; JCDL 2026 | NED of archival/provenance actors to Wikidata/ULAN; LLM extraction + reconciliation of 1,829 AIC records | people linking, not object reunion; LLM used for extraction, not matching | https://asistdl.onlinelibrary.wiley.com/doi/10.1002/pra2.490 `[snippet]`; https://doi.org/10.1145/3805696.3846493 `[snippet]` |
| Using ChatGPT for EM; Entity Matching using LLMs (Peeters, Steiner, Bizer) | arXiv 2023; EDBT 2025 | zero/few-shot LLM matchers on WDC Products etc.; cost table: 0.006¢/prompt GPT-mini zero-shot vs 0.474¢ GPT-4; few-shot/rules 1.5–470× cost | binary pairwise identity on product data, ≤3 hosted models, pre-reasoning-model era; no memorisation concern | https://doi.org/10.48786/edbt.2025.42 `[opened]` |
| Match, Compare, or Select? (ComEM, Wang et al.) | COLING 2025 | matching vs comparing vs *selecting* from a candidate list; selecting is cheapest but shows position bias; medium LLM filters → strong LLM selects | our listwise agent ≈ "selecting"; we add set-valued output, evidence ablations, 15 models | https://aclanthology.org/2025.coling-main.8.pdf `[opened]` |
| BATCHER (Fan et al.) | ICDE 2024 | cost-effective in-context learning for ER via batched demonstrations | cost lever is prompt packing; ours is information shown | https://paperswithcode.com/task/entity-resolution/latest `[snippet]` |

## C. Contamination / memorisation detection; knowledge vs evidence

| work | venue / year | what it does | how this project differs | URL |
| --- | --- | --- | --- | --- |
| Min-K% Prob + WikiMIA (Shi et al.) | ICLR 2024 | reference-free MIA from low-probability tokens; time-split benchmark | needs logprobs; our ladder is behavioural, works on closed APIs | https://proceedings.iclr.cc/paper_files/paper/2024/file/e32ad85fa27be4a9868d55703f01323e-Paper-Conference.pdf `[opened]` |
| Time Travel in LLMs (Golchin & Surdeanu) | ICLR 2024 spotlight | guided-instruction completion flags contaminated instances | recitation test; we measure *task performance* as evidence is removed | https://arxiv.org/abs/2308.08493 `[snippet]` |
| Proving Test Set Contamination (Oren et al.) | ICLR 2024 oral | exchangeability test, canonical vs shuffled order | needs logprobs over the whole benchmark | https://arxiv.org/abs/2310.17623 `[snippet]` |
| Surveys: Deng et al.; Fu et al. | arXiv 2024/25; NAACL Findings 2025 | 50+ methods; Fu et al.: MIA ≈ random on pretraining data, works only with time-split negatives | motivates our temporal ladder + behavioural probes over MIA | https://arxiv.org/html/2404.00699v5 `[snippet]`; https://arxiv.org/html/2410.18966v3 `[opened]` |
| Dated Data (Cheng et al.); LiveBench | COLM 2024; ICLR 2025 | effective cut-offs differ from reported; monthly-refreshed benchmark | we date-stratify records rather than refresh questions | https://arxiv.org/html/2403.12958v2 `[opened]`; https://arxiv.org/abs/2406.19314 `[snippet]` |
| Reasoning or Reciting? (Wu et al.) | NAACL 2024 | counterfactual task variants separate skill from recitation | closest analogue to `--dims-permute`; ours on real records, relational | https://aclanthology.org/2024.naacl-long.102/ `[snippet]` |
| ClashEval; FaithEval; ConflictBank; WikiContradict | NeurIPS 2024 D&B; arXiv 2024 (×3) | prior-vs-context conflicts (GPT-4o overrides correct prior >60 %; counterfactual context drops GPT-4o 96→47 %) | synthetic/perturbed passages; we *remove* real evidence channels and see what survives | https://proceedings.neurips.cc/paper_files/paper/2024/file/3aa291abc426d7a29fb08418c1244177-Paper-Datasets_and_Benchmarks_Track.pdf `[opened]`; https://arxiv.org/html/2410.03727v1 `[opened]` |
| PopQA (Mallen et al.) | ACL 2023 | memorisation scales with entity popularity (page views) | the famous-vs-obscure axis our ablations should be stratified by | https://aclanthology.org/2023.acl-long.546/ `[snippet]` |
| MM-Detect (Song et al.) | EMNLP Findings 2025 | unimodal vs cross-modal contamination in 12 MLLMs | benchmark-level; ours is task-level in heritage | https://aclanthology.org/2025.findings-emnlp.556.pdf `[opened]` |

## D. LLM reranking, cost-aware inference, routing, abstention

| work | venue / year | what it does | how this project differs | URL |
| --- | --- | --- | --- | --- |
| RankGPT (Sun et al.) | EMNLP 2023 | listwise sliding-window reranking; NovelEval against contamination | single ranking; we output a variable-size member set with "none" | https://aclanthology.org/2023.emnlp-main.923/ `[snippet]` |
| PRP (Qin et al.) | NAACL Findings 2024 | pairwise prompting; O(N²)/O(N log N)/O(N) variants | our pair-verify (E7) is pairwise but *visual* | https://aclanthology.org/2024.findings-naacl.97.pdf `[snippet]` |
| Setwise (Zhuang et al.) | SIGIR 2024 | unified efficiency study; GPT-4-priced run cost: pointwise $0.48, setwise-heapsort $1.28, pairwise-heapsort $3.39, all-pairs $90.6 | our E10e pointwise = 3× listwise cost, 14× wall time; same direction, new domain | https://arxiv.org/html/2310.09497v1 `[opened]` |
| FIRST (Gangi Reddy et al.) | EMNLP 2024 | first-identifier logits for listwise ranking, −50 % latency | analogous to our first-token P(yes) in E7 | https://aclanthology.org/2024.emnlp-main.491/ `[opened]` |
| FrugalGPT; RouteLLM; early-abstention cascades; routing surveys | arXiv 2023; ICLR 2025; arXiv 2025 (×2) | cascades save 59–98 %; routers >2×; early abstention cuts cost 13 %, error 5 % | we *measure* cost but do not route/cascade; the "reasoning tax" of mini thinking models is absent here | https://ar5iv.labs.arxiv.org/html/2305.05176 `[opened]`; https://arxiv.org/html/2502.09054 `[opened]`; https://arxiv.org/html/2502.00409v3 `[snippet]` |
| Conformal LM (Quach et al.); Conformal abstention; Know Your Limits | ICLR 2024; NeurIPS-W 2024; TACL 2025 | distribution-free prediction sets / abstention guarantees | `e10_regate` is a heuristic gate without coverage guarantee | https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf `[opened]`; https://aclanthology.org/2025.tacl-1.26/ `[snippet]` |

## E. Multimodal LLM evaluation for art & cultural heritage

| work | venue / year | what it does | how this project differs | URL |
| --- | --- | --- | --- | --- |
| Have VLMs Mastered Art History? (Strafforello et al.) | arXiv 2024 / ICIAP-W 2025 | zero-shot style/author/period; GPT-4o 53 % style, 6.7 % author on WikiArt | single-image attributes; ours is relational (pair/set membership) | https://arxiv.org/html/2409.03521v2 `[opened]` |
| GalleryGPT (Bin et al.) | ACM MM 2024 | formal analysis LMM; names "LLM-biased visual hallucination" — recognise-then-recall on famous paintings; one nameless painting as control | anecdotal control; we systematise it as a ladder + forced choice | https://arxiv.org/html/2408.00491 `[opened]` |
| Towards Artwork Explanation in LVLMs | ACL 2024 short | image-only vs image+title to split vision- vs language-based knowledge | title-withholding on *one* object; our L2-T/L6 withhold title across candidate sets | https://aclanthology.org/2024.acl-short.65.pdf `[snippet]` |
| Museum-65; VQArt-Bench; VaseVQA | ICCV 2025; ICCVW 2025; arXiv 2025 | 65M images / 200M QA on exhibits; 14k semantic VQA items, 14 MLLMs; Greek pottery agent | attribute QA, no pairing, no memorisation control, no $ | https://openaccess.thecvf.com/content/ICCV2025/papers/Balauca_Understanding_Museum_Exhibits_using_Vision-Language_Reasoning_ICCV_2025_paper.pdf `[opened]`; https://arxiv.org/abs/2510.12750 `[snippet]` |
| TAM grounding of art descriptions (Fanelli et al.) | ICPR-W 2026 | artist right 82 % vs title 28 %; wrong predictions more text-driven | supports our title-leak and creator-mask channels | https://icpr2026orgteam.github.io/WSpapers/pdfs/paper_0104.pdf `[opened]` |

## F. Agentic "deep research" baselines and cost per query

| work | venue / year | what it does | how this project differs | URL |
| --- | --- | --- | --- | --- |
| BrowseComp / OpenAI Deep Research | OpenAI, Apr 2025 | 1,266 hard browsing questions; Deep Research 51.5 % | open web; our E17 pool is a closed catalogue | https://openai.com/index/browsecomp/ `[snippet]` |
| Mind2Web 2 | arXiv 2025 | 130 long-horizon tasks, Agent-as-a-Judge; reports minutes, not $ | we report $ and tokens per query | https://arxiv.org/html/2506.21506v2 `[opened]` |
| DeepResearch Bench (Du et al.) | arXiv 2025 | 100 PhD-level tasks; judge cost $0.04–0.47/query | agent cost not isolated | https://arxiv.org/html/2506.11763 `[opened]` |
| Deep Research Bench (FutureSearch) | arXiv 2025 | RetroSearch offline web; cost explicitly deferred | our ledger fills that gap for one domain | https://arxiv.org/html/2506.06287 `[opened]` |
| DR Tulu (Shao et al.) | arXiv Nov 2025 | OpenAI Deep Research ≈ $1.80/query (ScholarQA-CSv2); DR Tulu-8B $0.0019 | same order as our E17 $0.22 vs shortlist $0.020 | https://arxiv.org/pdf/2511.19399 `[opened]` |
| Parallel.ai price-performance study | vendor blog, Aug 2025 | BrowseComp cost $100–$5,194 per 1,000 requests | vendor-reported; ours is relay-metered per call | https://parallel.ai/blog/deep-research-benchmarks `[opened]` |
| WebThinker; HF Open Deep Research; DeepResearchGym | arXiv 2025; blog 2025; arXiv 2025 | open agents; Gym: 640k search calls = $640 (Serper) / $5,000 (Tavily) | fixed pool, so search-API cost is zero | https://arxiv.org/html/2504.21776v2 `[snippet]`; https://arxiv.org/html/2505.19253 `[snippet]` |

## Novelty verdict

- **New task framing.** Reunion of dispersed ensembles as set-valued membership selection from cross-institution catalogue records (Wikidata/Commons/NGA). All located reassembly work is pixel/edge/puzzle-level (Dunhuang, oracle bones, papyri, RePAIR) or manual (Fragmentarium, Broken Books, IDP); no LLM-agent benchmark for this exists.
- **New diagnostic: the information-level ladder.** Per-channel ablations (title withheld, holder scrubbed, creator masked, dimensions permuted) on real records form a black-box, behavioural memorisation probe needing no logprobs. Closest analogues (Reasoning or Reciting; FaithEval/ClashEval; image-only vs image+title) are domain-general, synthetic, or single-object.
- **New combination of memorisation controls.** Closed-book baseline + both-order counterfactual forced choice with evidence withheld + date-stratified temporal ladder + served-model audit. Each piece exists separately (guided prompting, time splits, PopQA popularity); the joint use on one heritage dataset is new and should be stratified by entity popularity.
- **Relational MLLM evaluation is new.** Pair verification via first-token P(yes) with source-balanced negatives plus shortlist re-scoring; existing art MLLM benchmarks are single-image attribute QA.
- **Cost ledger across ~15 current models, including reasoning-mode "mini" models, is new evidence**; EM and reranking cost studies (Peeters/Bizer, ComEM, Setwise) cover ≤3 hosted models and pre-date reasoning models. The "reasoning tax" is a contribution.
- **Incremental:** listwise-beats-pointwise on cost replicates Setwise (SIGIR 2024) and ComEM (COLING 2025); report as domain confirmation and cite both.
- **Incremental:** the ~11× open-pool-vs-shortlist cost gap is expected from BrowseComp/DR Tulu cost reports; the value is the controlled same-model, same-query comparison.
- **At risk / must differentiate:** MLLM scoring of fragment pairs has a direct precedent in LLMCO4MR (ECCV 2024). Differentiate on object type (whole catalogued objects vs shredded fragments), evidence (text metadata), scale (15 models), and controls.
- **Gap, not novelty:** no learned router/cascade and no conformal set-size guarantee is in the grid; `e10_regate` is heuristic. Add one bucket-D baseline or avoid "cost-aware method" claims.
- **Overall:** position as a benchmark + diagnostic-methodology paper; dataset, ladder and probes are the defensible core, the agent itself is standard.

## Must-cite list

1. Fragmentarium (2015–) · 2. Davis, *Digital Philology* 2024 · 3. International Dunhuang Programme · 4. Zheng et al., *Heritage Science* 2024 · 5. Zhang et al., LLMCO4MR, ECCV 2024 · 6. Zhang et al., OB-Rejoin/S3-Net, KDD 2022 · 7. Tsesmelis et al., RePAIR, NeurIPS 2024 · 8. Shen, Efros, Aubry, CVPR 2019 · 9. Dutia & Stack, Heritage Connector, 2021 · 10. Peeters, Steiner, Bizer, EDBT 2025 · 11. Wang et al., ComEM, COLING 2025 · 12. Shi et al., Min-K% Prob, ICLR 2024 · 13. Golchin & Surdeanu, ICLR 2024 · 14. Oren et al., ICLR 2024 · 15. Fu et al., NAACL Findings 2025 · 16. Cheng et al., Dated Data, COLM 2024 · 17. Wu et al., Reasoning or Reciting, NAACL 2024 · 18. Wu, Wu, Zou, ClashEval, NeurIPS 2024 · 19. Mallen et al., PopQA, ACL 2023 · 20. Sun et al., RankGPT, EMNLP 2023 · 21. Zhuang et al., Setwise, SIGIR 2024 · 22. Chen, Zaharia, Zou, FrugalGPT, 2023 · 23. Quach et al., Conformal LM, ICLR 2024 · 24. Strafforello et al., 2024/2025 · 25. Bin et al., GalleryGPT, ACM MM 2024.

## Risks of being scooped / overlapping claims

- **LLMCO4MR (ECCV 2024)** is the only located 2024–26 work combining (M)LLMs with heritage fragment reunion (GPT-4V pairwise matching on Dunhuang). Do not claim "first (M)LLM for heritage reassembly"; claim first for *catalogue-level, cross-institution* reunion.
- **GalleryGPT (ACM MM 2024)**, **Towards Artwork Explanation (ACL 2024)** and the **TAM study (ICPR-W 2026)** already name memorisation of famous artworks as a confound (nameless images, title withholding, title hallucination vs artist recall). Cite; do not claim discovery of the confound.
- **MM-Detect (EMNLP Findings 2025)** owns "multimodal contamination detection"; qualify ours as a *heritage-specific, task-level, relational* probe.
- **Museum-65 (ICCV 2025), VQArt-Bench (ICCVW 2025), VaseVQA (2025)**: active groups with large heritage MLLM benchmarks; a pairing or memorisation-controlled extension is a short step for them.
- **MuseKG (Nov 2025), Getty Provenance RAG (2025/26), LLM-in-the-loop provenance (JCDL 2026)**: LLMs over museum metadata/Wikidata; adjacent data, different task — watch for "part-of" link-prediction follow-ups.
- **Genizah join retrieval (PRIMA 2026) + GenizahSearch Joins Lab**: human+AI join finding; an LLM reranker there would be close manuscript prior art.
- **EM community (Bizer group; ComEM)** already established "selecting is cheapest; position bias" — do not re-claim.
