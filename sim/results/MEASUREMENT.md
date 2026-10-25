# Measurement-protocol simulations (synthetic)

## S9 · evaluation unit (70 ensembles of size 2–12, every member a query, K=30, 1,500-object distractor pool; 12 reps)

| system                    |   pair_F1 |   macro_F1_ens |   b3_F1 |   ARI |   exact_set |   contradiction_rate |   ci_w_ens |   ci_w_query |
|:--------------------------|----------:|---------------:|--------:|------:|------------:|---------------------:|-----------:|-------------:|
| A uniform                 |     0.503 |          0.419 |   0.94  | 0.375 |       0.078 |                0.075 |      0.081 |        0.069 |
| B big-ensemble specialist |     0.7   |          0.43  |   0.942 | 0.373 |       0.093 |                0.048 |      0.185 |        0.073 |

Which system 'wins' depends on the metric: pair_F1: 100% of reps B > A; macro_F1_ens: 58% of reps B > A; b3_F1: 75% of reps B > A; ARI: 67% of reps B > A; exact_set: 58% of reps B > A

- query-level bootstrap CI is 0.65× as wide as the ensemble-level one on average → it understates uncertainty by ~35 %.
- 7.5% of explicit negative decisions are overturned by transitive closure of the positives (system A), i.e. the per-query output is not a consistent clustering.
- Dense-reuse regime (no distractor pool, every object reused as a distractor ~28×): pair F1 0.463 but B³ F1 0.265, ARI 0.008, contradiction rate 75.6% — naive transitive closure collapses into giant components at a ~2 % pairwise FPR. Stage 4 of the v2 design must use a proper clustering rule (e.g. correlation clustering), not closure.

## S10 · forking paths of a post-hoc rule (k variants tried, best reported; 150 reps)

| family              | split      |   k |   f1_optimism |   exact_optimism |   f1_honest_gain |
|:--------------------|:-----------|----:|--------------:|-----------------:|-----------------:|
| heterogeneous rules | dev n=80   |   1 |         0.003 |            0.004 |           -0.003 |
| heterogeneous rules | dev n=80   |   3 |         0.007 |            0.013 |            0.068 |
| heterogeneous rules | dev n=80   |   5 |         0.009 |            0.019 |            0.068 |
| heterogeneous rules | dev n=80   |  10 |         0.011 |            0.023 |            0.068 |
| heterogeneous rules | dev n=80   |  20 |         0.018 |            0.032 |            0.066 |
| heterogeneous rules | test n=294 |   1 |         0.001 |            0     |           -0.001 |
| heterogeneous rules | test n=294 |   3 |         0.002 |            0.001 |            0.073 |
| heterogeneous rules | test n=294 |   5 |         0.002 |            0.009 |            0.073 |
| heterogeneous rules | test n=294 |  10 |         0.004 |            0.01  |            0.072 |
| heterogeneous rules | test n=294 |  20 |         0.006 |            0.015 |            0.072 |
| threshold only      | dev n=80   |   1 |         0.003 |            0.004 |           -0.003 |
| threshold only      | dev n=80   |   3 |         0.007 |            0.013 |            0.113 |
| threshold only      | dev n=80   |   5 |         0.009 |            0.018 |            0.112 |
| threshold only      | dev n=80   |  10 |         0.01  |            0.021 |            0.111 |
| threshold only      | dev n=80   |  20 |         0.011 |            0.024 |            0.111 |
| threshold only      | test n=294 |   1 |         0.001 |            0     |           -0.001 |
| threshold only      | test n=294 |   3 |         0.001 |            0.005 |            0.119 |
| threshold only      | test n=294 |   5 |         0.001 |            0.006 |            0.119 |
| threshold only      | test n=294 |  10 |         0.001 |            0.007 |            0.119 |
| threshold only      | test n=294 |  20 |         0.001 |            0.008 |            0.118 |

- 'optimism' = metric reported after picking the best variant on the split being reported − the same variant's metric on a fresh draw of the same queries (what a frozen rule would have scored).
- 'threshold only': variants differ only in the posterior threshold (highly correlated → small optimism). 'heterogeneous rules': each variant re-scores a different 20 % of candidates (what a hand-written regate rule family looks like).
- 'f1_honest_gain' = what tuning buys once the choice is frozen on another split (threshold tuning is genuinely useful; the problem is only where it is chosen).

## S11 · position bias and the shuffled-order control (15 reps)

|                    |   pair_F1 |   pair_R |   recall_first_third |   recall_last_third |
|:-------------------|----------:|---------:|---------------------:|--------------------:|
| (0.0, 'retriever') |     0.404 |    0.28  |                0.283 |               0.258 |
| (0.0, 'shuffled')  |     0.409 |    0.284 |                0.285 |               0.292 |
| (1.5, 'retriever') |     0.367 |    0.232 |                0.258 |               0.093 |
| (1.5, 'shuffled')  |     0.269 |    0.161 |                0.241 |               0.09  |
| (3.0, 'retriever') |     0.31  |    0.187 |                0.222 |               0.038 |
| (3.0, 'shuffled')  |     0.177 |    0.099 |                0.204 |               0.019 |

- With a retriever-ordered list a primacy-biased selector loses little in aggregate F1 (gold sits early), so the ordered-list number flatters the selector by up to ~13 F1 points at primacy 3.0; the shuffled replicate reveals the loss that a weaker retriever or a different candidate order would expose.
- The diagnostic recall(first third) − recall(last third) detects the bias under BOTH orderings here (recall is conditional on gold, so where gold sits does not bias it), but on the ordered list it rests on the few gold items that land late and is correspondingly noisier; FPR-by-position IS confounded on an ordered list because retriever score and similarity co-vary. Run one shuffled-order replicate per headline condition and report both numbers.

- elapsed 49 s