# Simulation run log

- started: 2026-10-25 09:14:41 UTC
- world: `{"Q": 3000, "K": 30, "member_probs": [0.15, 0.35, 0.25, 0.13, 0.08, 0.04], "retriever_dprime": 1.5, "p_mem": 0.3, "dprime_mem": 4.0, "dprime_level": [["L1", 2.4], ["L3", 2.0], ["L5", 1.3], ["L6", 1.0]], "model_quality": [["mini", 0.75], ["flagship", 1.0], ["mini-thinking", 0.9]], "beta_dilution": 0.06, "pointwise_threshold_jitter": 0.35, "rho_sc": 0.5, "rho_models": 0.5, "overconfidence": 1.0, "seed": 0}`
- seeds: 8, queries per seed: 3000
- elapsed: 5.2 s

## Headline table (mean over seeds; coverage = 1 policies)

### L1

| model | policy | F1 ± CI95 | P | R | exact-set | ¢/query | calls/query |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| mini | listwise K=10 | 0.520 ± 0.005 | 0.922 | 0.362 | 0.338 | 0.21 | 1.00 |
| mini | adaptive-K τ=0.1 | 0.533 ± 0.006 | 0.876 | 0.384 | 0.346 | 0.28 | 1.00 |
| mini | adaptive-K τ=0.05 | 0.529 ± 0.006 | 0.862 | 0.382 | 0.349 | 0.31 | 1.00 |
| mini | adaptive-K τ=0.02 | 0.522 ± 0.006 | 0.837 | 0.379 | 0.337 | 0.34 | 1.00 |
| mini | listwise K=30 | 0.506 ± 0.008 | 0.808 | 0.369 | 0.326 | 0.39 | 1.00 |
| mini+flagship | cascade mini→flagship band=0.2 | 0.588 ± 0.003 | 0.898 | 0.437 | 0.381 | 0.78 | 1.57 |
| mini+flagship | cascade mini→flagship band=0.3 | 0.637 ± 0.004 | 0.907 | 0.491 | 0.414 | 0.94 | 1.78 |
| flagship | listwise K=10 | 0.655 ± 0.003 | 0.929 | 0.506 | 0.407 | 1.07 | 1.00 |
| mini+flagship | cascade mini→flagship band=0.4 | 0.687 ± 0.004 | 0.890 | 0.560 | 0.447 | 1.12 | 1.92 |
| mini+flagship | route mini→flagship θ=0.15 | 0.602 ± 0.003 | 0.844 | 0.467 | 0.371 | 1.28 | 1.45 |
| mini-thinking | listwise K=10 | 0.605 ± 0.005 | 0.925 | 0.450 | 0.380 | 1.32 | 1.00 |
| mini | pointwise ×30 | 0.577 ± 0.006 | 0.801 | 0.451 | 0.370 | 1.35 | 30.00 |
| flagship | adaptive-K τ=0.1 | 0.672 ± 0.004 | 0.887 | 0.541 | 0.420 | 1.41 | 1.00 |
| mini-thinking | adaptive-K τ=0.1 | 0.622 ± 0.005 | 0.880 | 0.481 | 0.391 | 1.45 | 1.00 |
| mini-thinking | adaptive-K τ=0.05 | 0.614 ± 0.004 | 0.857 | 0.479 | 0.382 | 1.51 | 1.00 |
| mini-thinking | adaptive-K τ=0.02 | 0.607 ± 0.004 | 0.833 | 0.478 | 0.373 | 1.57 | 1.00 |
| flagship | adaptive-K τ=0.05 | 0.669 ± 0.006 | 0.864 | 0.546 | 0.415 | 1.57 | 1.00 |
| mini-thinking | listwise K=30 | 0.587 ± 0.003 | 0.800 | 0.464 | 0.349 | 1.66 | 1.00 |
| flagship | adaptive-K τ=0.02 | 0.661 ± 0.005 | 0.842 | 0.545 | 0.401 | 1.74 | 1.00 |
| mini+flagship | route mini→flagship θ=0.25 | 0.630 ± 0.003 | 0.828 | 0.509 | 0.384 | 1.74 | 1.68 |
| mini | self-consistency n=5 | 0.515 ± 0.005 | 0.898 | 0.361 | 0.357 | 1.96 | 5.00 |
| flagship | listwise K=30 | 0.641 ± 0.004 | 0.805 | 0.533 | 0.381 | 1.99 | 1.00 |
| mini+flagship | route mini→flagship θ=0.35 | 0.645 ± 0.004 | 0.819 | 0.532 | 0.389 | 2.10 | 1.86 |
| mini-thinking | pointwise ×30 | 0.663 ± 0.004 | 0.814 | 0.560 | 0.410 | 2.67 | 30.00 |
| flagship | pointwise ×30 | 0.717 ± 0.003 | 0.831 | 0.630 | 0.452 | 6.93 | 30.00 |
| mini-thinking | self-consistency n=5 | 0.612 ± 0.004 | 0.896 | 0.465 | 0.396 | 8.31 | 5.00 |
| flagship | self-consistency n=5 | 0.669 ± 0.004 | 0.900 | 0.532 | 0.429 | 9.96 | 5.00 |

### L5

| model | policy | F1 ± CI95 | P | R | exact-set | ¢/query | calls/query |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| mini | listwise K=10 | 0.364 ± 0.006 | 0.971 | 0.224 | 0.290 | 0.17 | 1.00 |
| mini | adaptive-K τ=0.1 | 0.394 ± 0.008 | 0.944 | 0.249 | 0.311 | 0.20 | 1.00 |
| mini | adaptive-K τ=0.05 | 0.399 ± 0.008 | 0.940 | 0.253 | 0.315 | 0.22 | 1.00 |
| mini | adaptive-K τ=0.02 | 0.399 ± 0.009 | 0.929 | 0.254 | 0.311 | 0.24 | 1.00 |
| mini | listwise K=30 | 0.396 ± 0.008 | 0.903 | 0.253 | 0.302 | 0.26 | 1.00 |
| mini+flagship | cascade mini→flagship band=0.2 | 0.417 ± 0.009 | 0.940 | 0.268 | 0.329 | 0.40 | 1.22 |
| mini+flagship | route mini→flagship θ=0.15 | 0.403 ± 0.008 | 0.920 | 0.258 | 0.312 | 0.44 | 1.13 |
| mini+flagship | cascade mini→flagship band=0.3 | 0.433 ± 0.008 | 0.933 | 0.282 | 0.340 | 0.61 | 1.55 |
| mini+flagship | route mini→flagship θ=0.25 | 0.413 ± 0.008 | 0.914 | 0.266 | 0.318 | 0.72 | 1.34 |
| flagship | listwise K=10 | 0.400 ± 0.007 | 0.948 | 0.253 | 0.300 | 0.85 | 1.00 |
| mini+flagship | cascade mini→flagship band=0.4 | 0.458 ± 0.007 | 0.911 | 0.306 | 0.349 | 0.90 | 1.91 |
| flagship | adaptive-K τ=0.1 | 0.424 ± 0.007 | 0.915 | 0.276 | 0.318 | 1.02 | 1.00 |
| flagship | adaptive-K τ=0.05 | 0.425 ± 0.007 | 0.902 | 0.278 | 0.316 | 1.11 | 1.00 |
| flagship | adaptive-K τ=0.02 | 0.424 ± 0.007 | 0.894 | 0.278 | 0.315 | 1.19 | 1.00 |
| mini-thinking | listwise K=10 | 0.382 ± 0.007 | 0.957 | 0.239 | 0.295 | 1.24 | 1.00 |
| mini+flagship | route mini→flagship θ=0.35 | 0.418 ± 0.006 | 0.885 | 0.273 | 0.313 | 1.29 | 1.78 |
| mini-thinking | adaptive-K τ=0.1 | 0.406 ± 0.008 | 0.934 | 0.259 | 0.314 | 1.30 | 1.00 |
| mini | self-consistency n=5 | 0.405 ± 0.009 | 0.953 | 0.257 | 0.324 | 1.32 | 5.00 |
| flagship | listwise K=30 | 0.416 ± 0.007 | 0.870 | 0.273 | 0.302 | 1.33 | 1.00 |
| mini-thinking | adaptive-K τ=0.05 | 0.408 ± 0.008 | 0.923 | 0.262 | 0.314 | 1.33 | 1.00 |
| mini | pointwise ×30 | 0.426 ± 0.008 | 0.912 | 0.278 | 0.333 | 1.35 | 30.00 |
| mini-thinking | adaptive-K τ=0.02 | 0.408 ± 0.007 | 0.913 | 0.263 | 0.312 | 1.37 | 1.00 |
| mini-thinking | listwise K=30 | 0.403 ± 0.008 | 0.882 | 0.261 | 0.299 | 1.41 | 1.00 |
| mini-thinking | pointwise ×30 | 0.446 ± 0.006 | 0.876 | 0.299 | 0.337 | 2.67 | 30.00 |
| flagship | self-consistency n=5 | 0.421 ± 0.007 | 0.941 | 0.271 | 0.329 | 6.63 | 5.00 |
| flagship | pointwise ×30 | 0.465 ± 0.007 | 0.849 | 0.320 | 0.340 | 6.93 | 30.00 |
| mini-thinking | self-consistency n=5 | 0.411 ± 0.009 | 0.950 | 0.262 | 0.327 | 7.07 | 5.00 |

## Sensitivity sweep (216 worlds × 2 levels)

- elapsed: 48.0 s
- share of worlds where some policy beats today's design at ≤105 % of its budget: L1 86%, L5 97%
- pointwise − listwise (flagship) F1: median +0.060, range [-0.012, +0.218] at 3× the cost
- self-consistency n=5 − single (flagship): median +0.009, range [-0.034, +0.041] at 5× the cost
- adaptive-K τ=0.05 − K=30 (flagship): median +0.014, range [-0.010, +0.136] at median 81% of the cost

Best policy at budget, by world:

level  best_policy_at_budget                         
L1     flagship · adaptive-K τ=0.02                       15
       flagship · adaptive-K τ=0.05                       27
       flagship · adaptive-K τ=0.1                         6
       flagship · listwise K=10                           42
       flagship · listwise K=30                           13
       mini · pointwise ×30                               11
       mini+flagship · cascade mini→flagship band=0.4     92
       mini+flagship · route mini→flagship θ=0.35         10
L5     flagship · adaptive-K τ=0.02                       16
       flagship · adaptive-K τ=0.05                        9
       flagship · adaptive-K τ=0.1                         3
       flagship · listwise K=10                           32
       flagship · listwise K=30                            3
       mini · pointwise ×30                               29
       mini+flagship · cascade mini→flagship band=0.4    100
       mini+flagship · route mini→flagship θ=0.25          1
       mini+flagship · route mini→flagship θ=0.35         23
