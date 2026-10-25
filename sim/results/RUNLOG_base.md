# Simulation run log (v2 — matched operating points)

- started: 2026-10-25 10:22:50 UTC
- world: `{"Q": 3000, "K": 30, "member_probs": [0.15, 0.35, 0.25, 0.13, 0.08, 0.04], "retriever_dprime": 1.5, "belief_factor": 1.0, "p_mem": 0.3, "mem_share": [["mini", 0.6], ["flagship", 1.0], ["mini-thinking", 0.8]], "dprime_mem": [["mini", 3.0], ["flagship", 4.0], ["mini-thinking", 3.5]], "mem_keying": "record", "word_rungs": ["L1", "L3"], "dprime_level": [["L1", 2.4], ["L3", 2.0], ["L5", 1.3], ["L6", 1.0]], "model_quality": [["mini", 0.75], ["flagship", 1.0], ["mini-thinking", 0.9]], "beta_dilution": 0.06, "pointwise_threshold_jitter": 0.35, "rho_sc": 0.5, "rho_models": 0.5, "conf_noise": 0.0, "seed": 0}`
- seeds: 8 (threshold selected on the first 4, metrics on the remaining held-out seeds); queries per seed: 3000
- elapsed: 8.5 s

## Headline tables — each policy at its own F1-optimal threshold (chosen on selection seeds), evaluated on held-out seeds

F1 = micro pairwise F1 over (query, candidate) decisions; 'F1 non-mem' = same on the queries the flagship does NOT remember.

### L1

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.18 | 0.398 ± 0.012 | 0.398 | 0.348 | 0.465 | 0.077 | 0.00 | 0.00 | no LLM call |
| L1 | mini | listwise K=10 | 0.12 | 0.585 ± 0.010 | 0.550 | 0.588 | 0.581 | 0.232 | 0.19 | 1.00 |  |
| L1 | mini | listwise K=10 + retriever prior | 0.32 | 0.639 ± 0.008 | 0.608 | 0.685 | 0.600 | 0.307 | 0.19 | 1.00 |  |
| L1 | mini | retriever-prune p≥0.02 | 0.18 | 0.558 ± 0.006 | 0.509 | 0.569 | 0.546 | 0.220 | 0.25 | 1.00 | mean_kept=15.8 |
| L1 | mini | retriever-prune p≥0.02 + retriever prior | 0.32 | 0.643 ± 0.009 | 0.607 | 0.665 | 0.624 | 0.300 | 0.25 | 1.00 | mean_kept=15.8 |
| L1 | mini | adaptive-K τ=0.05 | 0.18 | 0.530 ± 0.010 | 0.483 | 0.504 | 0.558 | 0.177 | 0.30 | 1.00 | mean_k=20.9 |
| L1 | mini | listwise K=30 + retriever prior | 0.32 | 0.632 ± 0.006 | 0.594 | 0.653 | 0.612 | 0.288 | 0.39 | 1.00 |  |
| L1 | mini | listwise K=30 | 0.22 | 0.468 ± 0.012 | 0.418 | 0.446 | 0.493 | 0.140 | 0.39 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.3 | 0.22 | 0.596 ± 0.011 | 0.519 | 0.793 | 0.478 | 0.330 | 0.86 | 1.88 | strong_call_frac=0.87 esc_cands=2.0 |
| L1 | flagship | listwise K=10 | 0.15 | 0.724 ± 0.006 | 0.672 | 0.772 | 0.682 | 0.417 | 0.94 | 1.00 |  |
| L1 | flagship | listwise K=10 + retriever prior | 0.38 | 0.755 ± 0.006 | 0.709 | 0.833 | 0.690 | 0.460 | 0.94 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.4 | 0.27 | 0.674 ± 0.006 | 0.602 | 0.779 | 0.595 | 0.380 | 1.03 | 1.99 | strong_call_frac=0.98 esc_cands=4.4 |
| L1 | mini+flagship | cascade reject-only p̂<0.05 | 0.32 | 0.705 ± 0.009 | 0.624 | 0.779 | 0.645 | 0.412 | 1.22 | 2.00 | strong_call_frac=1.00 esc_cands=7.8 |
| L1 | flagship | retriever-prune p≥0.02 + retriever prior | 0.38 | 0.774 ± 0.009 | 0.720 | 0.813 | 0.739 | 0.482 | 1.24 | 1.00 | mean_kept=15.8 |
| L1 | flagship | retriever-prune p≥0.02 | 0.22 | 0.726 ± 0.006 | 0.655 | 0.753 | 0.701 | 0.415 | 1.24 | 1.00 | mean_kept=15.8 |
| L1 | mini+flagship | evidence-cascade L5→L1 band=0.45 | 0.38 | 0.655 ± 0.010 | 0.561 | 0.761 | 0.575 | 0.372 | 1.27 | 2.00 | strong_call_frac=1.00 esc_cands=11.3 |
| L1 | mini-thinking | listwise K=10 | 0.15 | 0.669 ± 0.006 | 0.626 | 0.710 | 0.632 | 0.338 | 1.27 | 1.00 |  |
| L1 | mini-thinking | listwise K=10 + retriever prior | 0.38 | 0.707 ± 0.008 | 0.670 | 0.787 | 0.642 | 0.404 | 1.27 | 1.00 |  |
| L1 | mini+flagship | evidence-cascade L5→L1 reject-only | 0.38 | 0.655 ± 0.014 | 0.562 | 0.762 | 0.574 | 0.370 | 1.28 | 2.00 | strong_call_frac=1.00 esc_cands=11.4 |
| L1 | mini | pointwise ×30 | 0.27 | 0.521 ± 0.008 | 0.463 | 0.519 | 0.523 | 0.188 | 1.29 | 30.00 |  |
| L1 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.38 | 0.722 ± 0.015 | 0.675 | 0.771 | 0.679 | 0.408 | 1.38 | 1.00 | mean_kept=15.8 |
| L1 | mini-thinking | retriever-prune p≥0.02 | 0.22 | 0.658 ± 0.011 | 0.599 | 0.700 | 0.620 | 0.335 | 1.38 | 1.00 | mean_kept=15.8 |
| L1 | mini-thinking | adaptive-K τ=0.05 | 0.22 | 0.638 ± 0.014 | 0.577 | 0.634 | 0.641 | 0.291 | 1.49 | 1.00 | mean_k=20.9 |
| L1 | flagship | adaptive-K τ=0.05 | 0.27 | 0.704 ± 0.005 | 0.622 | 0.728 | 0.682 | 0.387 | 1.52 | 1.00 | mean_k=20.9 |
| L1 | mini-thinking | listwise K=30 + retriever prior | 0.38 | 0.707 ± 0.010 | 0.656 | 0.751 | 0.668 | 0.388 | 1.66 | 1.00 |  |
| L1 | mini-thinking | listwise K=30 | 0.27 | 0.580 ± 0.011 | 0.509 | 0.574 | 0.585 | 0.239 | 1.66 | 1.00 |  |
| L1 | mini+flagship | route θ=0.25 | 0.27 | 0.639 ± 0.004 | 0.553 | 0.663 | 0.618 | 0.315 | 1.93 | 1.77 | escalated=0.78 |
| L1 | mini | self-consistency n=5 | 0.02 | 0.536 ± 0.010 | 0.479 | 0.553 | 0.521 | 0.196 | 1.96 | 5.00 |  |
| L1 | flagship | listwise K=30 + retriever prior | 0.38 | 0.761 ± 0.005 | 0.695 | 0.790 | 0.735 | 0.468 | 1.99 | 1.00 |  |
| L1 | flagship | listwise K=30 | 0.32 | 0.660 ± 0.006 | 0.563 | 0.682 | 0.640 | 0.344 | 1.99 | 1.00 |  |
| L1 | mini+flagship | route θ=0.35 | 0.32 | 0.662 ± 0.003 | 0.566 | 0.689 | 0.636 | 0.340 | 2.27 | 1.94 | escalated=0.95 |
| L1 | flagship | pointwise ×30 | 0.38 | 0.728 ± 0.009 | 0.640 | 0.762 | 0.698 | 0.435 | 6.66 | 30.00 |  |
| L1 | mini-thinking | self-consistency n=5 | 0.22 | 0.660 ± 0.006 | 0.563 | 0.854 | 0.538 | 0.393 | 8.31 | 5.00 |  |
| L1 | flagship | self-consistency n=5 | 0.22 | 0.759 ± 0.007 | 0.660 | 0.879 | 0.668 | 0.507 | 9.96 | 5.00 |  |
| L1 | mini-thinking | pointwise ×30 | 0.32 | 0.643 ± 0.010 | 0.571 | 0.657 | 0.630 | 0.314 | 20.74 | 30.00 |  |

### L5

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.18 | 0.398 ± 0.012 | 0.398 | 0.348 | 0.465 | 0.077 | 0.00 | 0.00 | no LLM call |
| L5 | mini | listwise K=10 | 0.10 | 0.430 ± 0.005 | 0.366 | 0.408 | 0.454 | 0.131 | 0.14 | 1.00 |  |
| L5 | mini | listwise K=10 + retriever prior | 0.27 | 0.529 ± 0.008 | 0.476 | 0.553 | 0.508 | 0.220 | 0.14 | 1.00 |  |
| L5 | mini | retriever-prune p≥0.02 | 0.12 | 0.390 ± 0.010 | 0.311 | 0.369 | 0.413 | 0.122 | 0.18 | 1.00 | mean_kept=15.8 |
| L5 | mini | retriever-prune p≥0.02 + retriever prior | 0.27 | 0.528 ± 0.003 | 0.467 | 0.544 | 0.513 | 0.212 | 0.18 | 1.00 | mean_kept=15.8 |
| L5 | mini | adaptive-K τ=0.05 | 0.12 | 0.358 ± 0.006 | 0.280 | 0.309 | 0.424 | 0.084 | 0.21 | 1.00 | mean_k=20.9 |
| L5 | mini | listwise K=30 + retriever prior | 0.27 | 0.524 ± 0.007 | 0.462 | 0.539 | 0.510 | 0.210 | 0.26 | 1.00 |  |
| L5 | mini | listwise K=30 | 0.15 | 0.304 ± 0.004 | 0.211 | 0.284 | 0.328 | 0.077 | 0.26 | 1.00 |  |
| L5 | mini+flagship | cascade band=0.3 | 0.15 | 0.330 ± 0.013 | 0.213 | 0.352 | 0.312 | 0.136 | 0.54 | 1.61 | strong_call_frac=0.62 esc_cands=1.0 |
| L5 | flagship | listwise K=10 | 0.12 | 0.552 ± 0.009 | 0.431 | 0.577 | 0.529 | 0.262 | 0.71 | 1.00 |  |
| L5 | flagship | listwise K=10 + retriever prior | 0.32 | 0.623 ± 0.007 | 0.521 | 0.692 | 0.567 | 0.334 | 0.71 | 1.00 |  |
| L5 | mini+flagship | route θ=0.25 | 0.18 | 0.374 ± 0.006 | 0.212 | 0.437 | 0.327 | 0.179 | 0.77 | 1.38 | escalated=0.39 |
| L5 | mini+flagship | cascade band=0.4 | 0.18 | 0.436 ± 0.009 | 0.283 | 0.549 | 0.361 | 0.236 | 0.79 | 1.98 | strong_call_frac=0.99 esc_cands=4.3 |
| L5 | flagship | retriever-prune p≥0.02 + retriever prior | 0.32 | 0.639 ± 0.008 | 0.519 | 0.691 | 0.595 | 0.354 | 0.88 | 1.00 | mean_kept=15.8 |
| L5 | flagship | retriever-prune p≥0.02 | 0.15 | 0.536 ± 0.013 | 0.386 | 0.540 | 0.532 | 0.272 | 0.88 | 1.00 | mean_kept=15.8 |
| L5 | mini+flagship | cascade reject-only p̂<0.05 | 0.22 | 0.475 ± 0.011 | 0.292 | 0.550 | 0.418 | 0.257 | 1.01 | 2.00 | strong_call_frac=1.00 esc_cands=11.4 |
| L5 | mini | pointwise ×30 | 0.18 | 0.331 ± 0.011 | 0.223 | 0.329 | 0.333 | 0.112 | 1.04 | 30.00 |  |
| L5 | flagship | adaptive-K τ=0.05 | 0.18 | 0.517 ± 0.012 | 0.340 | 0.544 | 0.493 | 0.267 | 1.04 | 1.00 | mean_k=20.9 |
| L5 | mini-thinking | listwise K=10 + retriever prior | 0.32 | 0.577 ± 0.007 | 0.495 | 0.650 | 0.518 | 0.281 | 1.19 | 1.00 |  |
| L5 | mini-thinking | listwise K=10 | 0.10 | 0.493 ± 0.009 | 0.410 | 0.467 | 0.523 | 0.183 | 1.19 | 1.00 |  |
| L5 | mini-thinking | retriever-prune p≥0.02 | 0.15 | 0.469 ± 0.006 | 0.348 | 0.490 | 0.450 | 0.203 | 1.25 | 1.00 | mean_kept=15.8 |
| L5 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.32 | 0.582 ± 0.007 | 0.487 | 0.641 | 0.534 | 0.288 | 1.25 | 1.00 | mean_kept=15.8 |
| L5 | mini-thinking | adaptive-K τ=0.05 | 0.15 | 0.435 ± 0.005 | 0.314 | 0.416 | 0.456 | 0.165 | 1.31 | 1.00 | mean_k=20.9 |
| L5 | mini | self-consistency n=5 | 0.02 | 0.266 ± 0.014 | 0.023 | 0.597 | 0.171 | 0.173 | 1.32 | 5.00 |  |
| L5 | flagship | listwise K=30 + retriever prior | 0.32 | 0.631 ± 0.013 | 0.500 | 0.676 | 0.591 | 0.346 | 1.33 | 1.00 |  |
| L5 | flagship | listwise K=30 | 0.22 | 0.475 ± 0.012 | 0.268 | 0.526 | 0.434 | 0.243 | 1.33 | 1.00 |  |
| L5 | mini+flagship | route θ=0.35 | 0.22 | 0.463 ± 0.010 | 0.260 | 0.541 | 0.405 | 0.244 | 1.39 | 1.85 | escalated=0.86 |
| L5 | mini-thinking | listwise K=30 + retriever prior | 0.27 | 0.579 ± 0.013 | 0.489 | 0.584 | 0.575 | 0.260 | 1.41 | 1.00 |  |
| L5 | mini-thinking | listwise K=30 | 0.18 | 0.391 ± 0.007 | 0.247 | 0.396 | 0.386 | 0.148 | 1.41 | 1.00 |  |
| L5 | flagship | pointwise ×30 | 0.27 | 0.506 ± 0.013 | 0.290 | 0.579 | 0.450 | 0.293 | 5.37 | 30.00 |  |
| L5 | flagship | self-consistency n=5 | 0.02 | 0.488 ± 0.013 | 0.194 | 0.680 | 0.381 | 0.269 | 6.63 | 5.00 |  |
| L5 | mini-thinking | self-consistency n=5 | 0.02 | 0.379 ± 0.010 | 0.100 | 0.635 | 0.270 | 0.208 | 7.07 | 5.00 |  |
| L5 | mini-thinking | pointwise ×30 | 0.22 | 0.421 ± 0.013 | 0.265 | 0.447 | 0.398 | 0.199 | 20.26 | 30.00 |  |

## Same policies at a fixed threshold of 0.5 (the v1 comparison; different operating points — for reference only)

### L1

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.50 | 0.225 ± 0.009 | 0.225 | 0.646 | 0.136 | 0.179 | 0.00 | 0.00 | no LLM call |
| L1 | mini | listwise K=10 | 0.50 | 0.408 ± 0.009 | 0.321 | 0.878 | 0.266 | 0.258 | 0.19 | 1.00 |  |
| L1 | mini | listwise K=10 + retriever prior | 0.50 | 0.618 ± 0.005 | 0.577 | 0.797 | 0.504 | 0.336 | 0.19 | 1.00 |  |
| L1 | mini | retriever-prune p≥0.02 | 0.50 | 0.410 ± 0.008 | 0.315 | 0.829 | 0.273 | 0.254 | 0.25 | 1.00 | mean_kept=15.7 |
| L1 | mini | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.616 ± 0.005 | 0.571 | 0.785 | 0.507 | 0.334 | 0.25 | 1.00 | mean_kept=15.7 |
| L1 | mini | adaptive-K τ=0.05 | 0.50 | 0.397 ± 0.006 | 0.298 | 0.790 | 0.265 | 0.247 | 0.30 | 1.00 | mean_k=20.9 |
| L1 | mini | listwise K=30 + retriever prior | 0.50 | 0.597 ± 0.006 | 0.551 | 0.773 | 0.486 | 0.318 | 0.39 | 1.00 |  |
| L1 | mini | listwise K=30 | 0.50 | 0.366 ± 0.009 | 0.268 | 0.713 | 0.247 | 0.222 | 0.39 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.3 | 0.50 | 0.570 ± 0.005 | 0.472 | 0.890 | 0.419 | 0.338 | 0.86 | 1.87 | strong_call_frac=0.87 esc_cands=2.0 |
| L1 | flagship | listwise K=10 | 0.50 | 0.656 ± 0.006 | 0.562 | 0.931 | 0.506 | 0.410 | 0.94 | 1.00 |  |
| L1 | flagship | listwise K=10 + retriever prior | 0.50 | 0.748 ± 0.004 | 0.696 | 0.878 | 0.651 | 0.473 | 0.94 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.4 | 0.50 | 0.650 ± 0.005 | 0.556 | 0.879 | 0.516 | 0.393 | 1.03 | 1.99 | strong_call_frac=0.98 esc_cands=4.2 |
| L1 | mini+flagship | cascade reject-only p̂<0.05 | 0.50 | 0.681 ± 0.005 | 0.581 | 0.856 | 0.565 | 0.418 | 1.21 | 2.00 | strong_call_frac=1.00 esc_cands=7.6 |
| L1 | flagship | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.766 ± 0.006 | 0.703 | 0.864 | 0.687 | 0.493 | 1.24 | 1.00 | mean_kept=15.7 |
| L1 | flagship | retriever-prune p≥0.02 | 0.50 | 0.677 ± 0.004 | 0.569 | 0.897 | 0.544 | 0.426 | 1.24 | 1.00 | mean_kept=15.7 |
| L1 | mini+flagship | evidence-cascade L5→L1 band=0.45 | 0.50 | 0.643 ± 0.005 | 0.534 | 0.832 | 0.524 | 0.387 | 1.27 | 2.00 | strong_call_frac=1.00 esc_cands=11.1 |
| L1 | mini-thinking | listwise K=10 | 0.50 | 0.566 ± 0.004 | 0.478 | 0.908 | 0.411 | 0.343 | 1.27 | 1.00 |  |
| L1 | mini-thinking | listwise K=10 + retriever prior | 0.50 | 0.697 ± 0.004 | 0.654 | 0.845 | 0.594 | 0.413 | 1.27 | 1.00 |  |
| L1 | mini+flagship | evidence-cascade L5→L1 reject-only | 0.50 | 0.641 ± 0.005 | 0.535 | 0.832 | 0.522 | 0.384 | 1.27 | 2.00 | strong_call_frac=1.00 esc_cands=11.1 |
| L1 | mini | pointwise ×30 | 0.50 | 0.463 ± 0.007 | 0.373 | 0.722 | 0.340 | 0.256 | 1.29 | 30.00 |  |
| L1 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.708 ± 0.007 | 0.655 | 0.831 | 0.617 | 0.420 | 1.38 | 1.00 | mean_kept=15.7 |
| L1 | mini-thinking | retriever-prune p≥0.02 | 0.50 | 0.575 ± 0.007 | 0.476 | 0.869 | 0.430 | 0.341 | 1.38 | 1.00 | mean_kept=15.7 |
| L1 | mini-thinking | adaptive-K τ=0.05 | 0.50 | 0.567 ± 0.005 | 0.467 | 0.833 | 0.429 | 0.330 | 1.48 | 1.00 | mean_k=20.9 |
| L1 | flagship | adaptive-K τ=0.05 | 0.50 | 0.666 ± 0.004 | 0.550 | 0.863 | 0.542 | 0.410 | 1.52 | 1.00 | mean_k=20.9 |
| L1 | mini-thinking | listwise K=30 + retriever prior | 0.50 | 0.690 ± 0.006 | 0.631 | 0.819 | 0.597 | 0.401 | 1.66 | 1.00 |  |
| L1 | mini-thinking | listwise K=30 | 0.50 | 0.531 ± 0.005 | 0.425 | 0.764 | 0.407 | 0.293 | 1.66 | 1.00 |  |
| L1 | mini+flagship | route θ=0.25 | 0.50 | 0.609 ± 0.004 | 0.490 | 0.816 | 0.486 | 0.353 | 1.92 | 1.77 | escalated=0.78 |
| L1 | mini | self-consistency n=5 | 0.50 | 0.345 ± 0.008 | 0.213 | 0.936 | 0.211 | 0.253 | 1.96 | 5.00 |  |
| L1 | flagship | listwise K=30 + retriever prior | 0.50 | 0.754 ± 0.002 | 0.679 | 0.850 | 0.677 | 0.482 | 1.99 | 1.00 |  |
| L1 | flagship | listwise K=30 | 0.50 | 0.638 ± 0.004 | 0.515 | 0.804 | 0.530 | 0.377 | 1.99 | 1.00 |  |
| L1 | mini+flagship | route θ=0.35 | 0.50 | 0.637 ± 0.006 | 0.515 | 0.809 | 0.526 | 0.372 | 2.27 | 1.94 | escalated=0.95 |
| L1 | flagship | pointwise ×30 | 0.50 | 0.719 ± 0.005 | 0.619 | 0.830 | 0.635 | 0.450 | 6.66 | 30.00 |  |
| L1 | mini-thinking | self-consistency n=5 | 0.50 | 0.553 ± 0.006 | 0.410 | 0.945 | 0.391 | 0.352 | 8.31 | 5.00 |  |
| L1 | flagship | self-consistency n=5 | 0.50 | 0.681 ± 0.004 | 0.535 | 0.962 | 0.528 | 0.459 | 9.96 | 5.00 |  |
| L1 | mini-thinking | pointwise ×30 | 0.50 | 0.622 ± 0.005 | 0.532 | 0.785 | 0.515 | 0.352 | 20.74 | 30.00 |  |

### L5

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.50 | 0.225 ± 0.009 | 0.225 | 0.646 | 0.136 | 0.179 | 0.00 | 0.00 | no LLM call |
| L5 | mini | listwise K=10 | 0.50 | 0.194 ± 0.007 | 0.012 | 0.934 | 0.108 | 0.210 | 0.14 | 1.00 |  |
| L5 | mini | listwise K=10 + retriever prior | 0.50 | 0.464 ± 0.006 | 0.373 | 0.758 | 0.334 | 0.267 | 0.14 | 1.00 |  |
| L5 | mini | retriever-prune p≥0.02 | 0.50 | 0.199 ± 0.007 | 0.010 | 0.884 | 0.112 | 0.207 | 0.18 | 1.00 | mean_kept=15.7 |
| L5 | mini | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.460 ± 0.010 | 0.361 | 0.746 | 0.333 | 0.263 | 0.18 | 1.00 | mean_kept=15.7 |
| L5 | mini | adaptive-K τ=0.05 | 0.50 | 0.202 ± 0.008 | 0.008 | 0.856 | 0.114 | 0.205 | 0.21 | 1.00 | mean_k=20.9 |
| L5 | mini | listwise K=30 + retriever prior | 0.50 | 0.446 ± 0.010 | 0.346 | 0.742 | 0.319 | 0.257 | 0.26 | 1.00 |  |
| L5 | mini | listwise K=30 | 0.50 | 0.194 ± 0.009 | 0.005 | 0.792 | 0.110 | 0.194 | 0.26 | 1.00 |  |
| L5 | mini+flagship | cascade band=0.3 | 0.50 | 0.282 ± 0.008 | 0.054 | 0.894 | 0.168 | 0.241 | 0.53 | 1.60 | strong_call_frac=0.60 esc_cands=0.9 |
| L5 | flagship | listwise K=10 | 0.50 | 0.402 ± 0.008 | 0.095 | 0.946 | 0.255 | 0.300 | 0.71 | 1.00 |  |
| L5 | flagship | listwise K=10 + retriever prior | 0.50 | 0.595 ± 0.007 | 0.454 | 0.822 | 0.466 | 0.358 | 0.71 | 1.00 |  |
| L5 | mini+flagship | route θ=0.25 | 0.50 | 0.309 ± 0.010 | 0.034 | 0.881 | 0.188 | 0.253 | 0.76 | 1.37 | escalated=0.38 |
| L5 | mini+flagship | cascade band=0.4 | 0.50 | 0.363 ± 0.008 | 0.097 | 0.875 | 0.229 | 0.273 | 0.78 | 1.98 | strong_call_frac=0.98 esc_cands=4.1 |
| L5 | flagship | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.609 ± 0.009 | 0.444 | 0.823 | 0.483 | 0.381 | 0.88 | 1.00 | mean_kept=15.7 |
| L5 | flagship | retriever-prune p≥0.02 | 0.50 | 0.421 ± 0.008 | 0.083 | 0.930 | 0.272 | 0.317 | 0.88 | 1.00 | mean_kept=15.7 |
| L5 | mini+flagship | cascade reject-only p̂<0.05 | 0.50 | 0.413 ± 0.009 | 0.096 | 0.880 | 0.270 | 0.305 | 1.01 | 2.00 | strong_call_frac=1.00 esc_cands=11.1 |
| L5 | mini | pointwise ×30 | 0.50 | 0.235 ± 0.009 | 0.025 | 0.806 | 0.138 | 0.213 | 1.04 | 30.00 |  |
| L5 | flagship | adaptive-K τ=0.05 | 0.50 | 0.425 ± 0.008 | 0.073 | 0.905 | 0.278 | 0.318 | 1.04 | 1.00 | mean_k=20.9 |
| L5 | mini-thinking | listwise K=10 + retriever prior | 0.50 | 0.536 ± 0.009 | 0.421 | 0.790 | 0.406 | 0.309 | 1.19 | 1.00 |  |
| L5 | mini-thinking | listwise K=10 | 0.50 | 0.302 ± 0.009 | 0.050 | 0.940 | 0.180 | 0.251 | 1.19 | 1.00 |  |
| L5 | mini-thinking | retriever-prune p≥0.02 | 0.50 | 0.314 ± 0.010 | 0.042 | 0.905 | 0.190 | 0.254 | 1.25 | 1.00 | mean_kept=15.7 |
| L5 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.539 ± 0.007 | 0.406 | 0.784 | 0.411 | 0.314 | 1.25 | 1.00 | mean_kept=15.7 |
| L5 | mini-thinking | adaptive-K τ=0.05 | 0.50 | 0.317 ± 0.008 | 0.041 | 0.883 | 0.193 | 0.255 | 1.31 | 1.00 | mean_k=20.9 |
| L5 | mini | self-consistency n=5 | 0.50 | 0.203 ± 0.009 | 0.001 | 0.960 | 0.113 | 0.216 | 1.32 | 5.00 |  |
| L5 | flagship | listwise K=30 + retriever prior | 0.50 | 0.599 ± 0.009 | 0.421 | 0.814 | 0.474 | 0.372 | 1.33 | 1.00 |  |
| L5 | flagship | listwise K=30 | 0.50 | 0.414 ± 0.009 | 0.061 | 0.867 | 0.272 | 0.303 | 1.33 | 1.00 |  |
| L5 | mini+flagship | route θ=0.35 | 0.50 | 0.397 ± 0.009 | 0.058 | 0.872 | 0.257 | 0.293 | 1.38 | 1.85 | escalated=0.85 |
| L5 | mini-thinking | listwise K=30 + retriever prior | 0.50 | 0.531 ± 0.009 | 0.391 | 0.780 | 0.403 | 0.313 | 1.41 | 1.00 |  |
| L5 | mini-thinking | listwise K=30 | 0.50 | 0.306 ± 0.012 | 0.028 | 0.837 | 0.187 | 0.241 | 1.41 | 1.00 |  |
| L5 | flagship | pointwise ×30 | 0.50 | 0.465 ± 0.009 | 0.131 | 0.845 | 0.321 | 0.337 | 5.37 | 30.00 |  |
| L5 | flagship | self-consistency n=5 | 0.50 | 0.427 ± 0.009 | 0.022 | 0.983 | 0.273 | 0.350 | 6.63 | 5.00 |  |
| L5 | mini-thinking | self-consistency n=5 | 0.50 | 0.318 ± 0.012 | 0.006 | 0.972 | 0.190 | 0.277 | 7.07 | 5.00 |  |
| L5 | mini-thinking | pointwise ×30 | 0.50 | 0.354 ± 0.011 | 0.076 | 0.819 | 0.226 | 0.267 | 20.26 | 30.00 |  |
