# Power of the ladder comparison (synthetic; paired exact-set outcomes)

| n | ICC (ensemble clustering) | ρ_pair (same-query correlation across levels) | MDD @80 % power, McNemar | MDD @80 % power, cluster bootstrap |
| ---: | ---: | ---: | ---: | ---: |
| 80 | 0.0 | 0.3 | 0.183 | 0.176 |
| 80 | 0.0 | 0.7 | 0.149 | 0.140 |
| 80 | 0.3 | 0.3 | 0.183 | 0.169 |
| 80 | 0.3 | 0.7 | 0.150 | 0.139 |
| 294 | 0.0 | 0.3 | 0.091 | 0.089 |
| 294 | 0.0 | 0.7 | 0.074 | 0.070 |
| 294 | 0.3 | 0.3 | 0.092 | 0.089 |
| 294 | 0.3 | 0.7 | 0.073 | 0.072 |

95 % CI half-width of one level's absolute accuracy (base 0.60, cluster bootstrap over ensembles):

| n | ICC | ± |
| ---: | ---: | ---: |
| 80 | 0.0 | 0.103 |
| 80 | 0.3 | 0.110 |
| 294 | 0.0 | 0.055 |
| 294 | 0.3 | 0.058 |

- reps per cell: 1500 (McNemar), 300 (bootstrap, B=400); base accuracy 0.60; λ=1.0
- elapsed 282 s

Reading (computed from the table above): on the 80-query dev split a true drop must be about 0.15–0.18 (i.e. 15–18 accuracy points) before a paired McNemar test detects it with 80 % power; on the 294-query test split about 0.07–0.09. Pairing cancels the shared ensemble effect, so ICC barely changes the power of a *difference*; it does widen the CI of each level's *absolute* accuracy (second table), so leaderboard numbers must be bootstrapped over ensembles, not queries. Lower same-query correlation (ρ_pair) — i.e. noisier LLM sampling — costs power: report replicate runs.