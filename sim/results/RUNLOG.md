# Simulation run log (v2 — matched operating points)

- started: 2026-10-25 10:53:34 UTC
- world: `{"Q": 3000, "K": 30, "member_probs": [0.15, 0.35, 0.25, 0.13, 0.08, 0.04], "retriever_dprime": 1.5, "belief_factor": 1.0, "p_mem": 0.3, "mem_share": [["mini", 0.6], ["flagship", 1.0], ["mini-thinking", 0.8]], "dprime_mem": [["mini", 3.0], ["flagship", 4.0], ["mini-thinking", 3.5]], "mem_keying": "record", "word_rungs": ["L1", "L3"], "dprime_level": [["L1", 2.4], ["L3", 2.0], ["L5", 1.3], ["L6", 1.0]], "model_quality": [["mini", 0.75], ["flagship", 1.0], ["mini-thinking", 0.9]], "beta_dilution": 0.06, "pointwise_threshold_jitter": 0.35, "rho_sc": 0.5, "rho_models": 0.5, "conf_noise": 0.0, "rho_retriever_llm": 0.0, "seed": 0}`
- seeds: 8 (threshold selected on the first 4, metrics on the remaining held-out seeds); queries per seed: 3000
- elapsed: 8.6 s

## Headline tables — each policy at its own F1-optimal threshold (chosen on selection seeds), evaluated on held-out seeds

F1 = micro pairwise F1 over (query, candidate) decisions; 'F1 non-mem' = same on the queries the flagship does NOT remember.

### L1

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.22 | 0.391 ± 0.007 | 0.390 | 0.388 | 0.395 | 0.099 | 0.00 | 0.00 | no LLM call |
| L1 | mini | listwise K=10 | 0.15 | 0.592 ± 0.010 | 0.556 | 0.636 | 0.553 | 0.257 | 0.19 | 1.00 |  |
| L1 | mini | listwise K=10 + retriever prior | 0.32 | 0.642 ± 0.007 | 0.613 | 0.686 | 0.604 | 0.306 | 0.19 | 1.00 |  |
| L1 | mini | retriever-prune p≥0.02 | 0.18 | 0.567 ± 0.007 | 0.523 | 0.578 | 0.556 | 0.229 | 0.25 | 1.00 | mean_kept=15.8 |
| L1 | mini | retriever-prune p≥0.02 + retriever prior | 0.32 | 0.643 ± 0.006 | 0.608 | 0.666 | 0.622 | 0.302 | 0.25 | 1.00 | mean_kept=15.8 |
| L1 | mini | adaptive-K τ=0.05 | 0.18 | 0.526 ± 0.003 | 0.479 | 0.499 | 0.557 | 0.176 | 0.30 | 1.00 | mean_k=21.0 |
| L1 | mini | listwise K=30 + retriever prior | 0.32 | 0.630 ± 0.006 | 0.595 | 0.652 | 0.610 | 0.287 | 0.39 | 1.00 |  |
| L1 | mini | listwise K=30 | 0.22 | 0.473 ± 0.009 | 0.425 | 0.452 | 0.497 | 0.142 | 0.39 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.3 | 0.22 | 0.603 ± 0.015 | 0.529 | 0.802 | 0.484 | 0.331 | 0.86 | 1.87 | strong_call_frac=0.87 esc_cands=2.0 |
| L1 | flagship | listwise K=10 | 0.18 | 0.730 ± 0.005 | 0.675 | 0.808 | 0.666 | 0.427 | 0.94 | 1.00 |  |
| L1 | flagship | listwise K=10 + retriever prior | 0.38 | 0.754 ± 0.003 | 0.707 | 0.832 | 0.689 | 0.458 | 0.94 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.4 | 0.27 | 0.681 ± 0.015 | 0.612 | 0.786 | 0.600 | 0.383 | 1.03 | 1.98 | strong_call_frac=0.98 esc_cands=4.4 |
| L1 | mini+flagship | cascade reject-only p̂<0.05 | 0.27 | 0.708 ± 0.017 | 0.635 | 0.749 | 0.672 | 0.402 | 1.21 | 2.00 | strong_call_frac=1.00 esc_cands=7.8 |
| L1 | flagship | retriever-prune p≥0.02 + retriever prior | 0.44 | 0.774 ± 0.006 | 0.716 | 0.841 | 0.717 | 0.492 | 1.24 | 1.00 | mean_kept=15.8 |
| L1 | flagship | retriever-prune p≥0.02 | 0.22 | 0.732 ± 0.003 | 0.662 | 0.761 | 0.704 | 0.425 | 1.24 | 1.00 | mean_kept=15.8 |
| L1 | mini+flagship | evidence-cascade L5→L1 band=0.45 | 0.38 | 0.659 ± 0.025 | 0.567 | 0.765 | 0.579 | 0.371 | 1.27 | 2.00 | strong_call_frac=1.00 esc_cands=11.3 |
| L1 | mini-thinking | listwise K=10 | 0.15 | 0.675 ± 0.010 | 0.634 | 0.719 | 0.636 | 0.342 | 1.27 | 1.00 |  |
| L1 | mini-thinking | listwise K=10 + retriever prior | 0.38 | 0.711 ± 0.009 | 0.673 | 0.788 | 0.647 | 0.398 | 1.27 | 1.00 |  |
| L1 | mini+flagship | evidence-cascade L5→L1 reject-only | 0.38 | 0.660 ± 0.028 | 0.569 | 0.765 | 0.580 | 0.377 | 1.28 | 2.00 | strong_call_frac=1.00 esc_cands=11.4 |
| L1 | mini | pointwise ×30 | 0.27 | 0.531 ± 0.016 | 0.476 | 0.528 | 0.533 | 0.199 | 1.29 | 30.00 |  |
| L1 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.32 | 0.722 ± 0.009 | 0.677 | 0.736 | 0.709 | 0.396 | 1.38 | 1.00 | mean_kept=15.8 |
| L1 | mini-thinking | retriever-prune p≥0.02 | 0.18 | 0.658 ± 0.017 | 0.604 | 0.656 | 0.660 | 0.313 | 1.38 | 1.00 | mean_kept=15.8 |
| L1 | mini-thinking | adaptive-K τ=0.05 | 0.22 | 0.636 ± 0.014 | 0.574 | 0.633 | 0.639 | 0.291 | 1.49 | 1.00 | mean_k=21.0 |
| L1 | flagship | adaptive-K τ=0.05 | 0.27 | 0.709 ± 0.009 | 0.628 | 0.732 | 0.688 | 0.396 | 1.52 | 1.00 | mean_k=21.0 |
| L1 | mini-thinking | listwise K=30 + retriever prior | 0.38 | 0.709 ± 0.008 | 0.657 | 0.750 | 0.671 | 0.389 | 1.66 | 1.00 |  |
| L1 | mini-thinking | listwise K=30 | 0.27 | 0.587 ± 0.005 | 0.520 | 0.580 | 0.594 | 0.242 | 1.66 | 1.00 |  |
| L1 | mini+flagship | route θ=0.25 | 0.32 | 0.645 ± 0.011 | 0.552 | 0.711 | 0.591 | 0.343 | 1.93 | 1.77 | escalated=0.76 |
| L1 | mini | self-consistency n=5 | 0.02 | 0.543 ± 0.018 | 0.489 | 0.564 | 0.524 | 0.208 | 1.96 | 5.00 |  |
| L1 | flagship | listwise K=30 + retriever prior | 0.38 | 0.763 ± 0.007 | 0.698 | 0.790 | 0.738 | 0.464 | 1.99 | 1.00 |  |
| L1 | flagship | listwise K=30 | 0.32 | 0.670 ± 0.012 | 0.576 | 0.690 | 0.651 | 0.351 | 1.99 | 1.00 |  |
| L1 | mini+flagship | route θ=0.35 | 0.32 | 0.667 ± 0.013 | 0.576 | 0.694 | 0.641 | 0.347 | 2.27 | 1.94 | escalated=0.94 |
| L1 | flagship | pointwise ×30 | 0.38 | 0.730 ± 0.010 | 0.643 | 0.763 | 0.699 | 0.435 | 6.66 | 30.00 |  |
| L1 | mini-thinking | self-consistency n=5 | 0.22 | 0.666 ± 0.012 | 0.572 | 0.857 | 0.545 | 0.403 | 8.31 | 5.00 |  |
| L1 | flagship | self-consistency n=5 | 0.22 | 0.765 ± 0.014 | 0.668 | 0.881 | 0.676 | 0.509 | 9.96 | 5.00 |  |
| L1 | mini-thinking | pointwise ×30 | 0.32 | 0.655 ± 0.009 | 0.585 | 0.669 | 0.641 | 0.325 | 20.74 | 30.00 |  |

### L5

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.22 | 0.391 ± 0.007 | 0.390 | 0.388 | 0.395 | 0.099 | 0.00 | 0.00 | no LLM call |
| L5 | mini | listwise K=10 | 0.10 | 0.431 ± 0.013 | 0.368 | 0.409 | 0.457 | 0.131 | 0.14 | 1.00 |  |
| L5 | mini | listwise K=10 + retriever prior | 0.27 | 0.527 ± 0.005 | 0.470 | 0.548 | 0.508 | 0.209 | 0.14 | 1.00 |  |
| L5 | mini | retriever-prune p≥0.02 | 0.12 | 0.395 ± 0.016 | 0.317 | 0.374 | 0.419 | 0.124 | 0.18 | 1.00 | mean_kept=15.8 |
| L5 | mini | retriever-prune p≥0.02 + retriever prior | 0.27 | 0.529 ± 0.005 | 0.466 | 0.544 | 0.515 | 0.212 | 0.18 | 1.00 | mean_kept=15.8 |
| L5 | mini | adaptive-K τ=0.05 | 0.12 | 0.356 ± 0.007 | 0.281 | 0.309 | 0.421 | 0.083 | 0.21 | 1.00 | mean_k=21.0 |
| L5 | mini | listwise K=30 + retriever prior | 0.27 | 0.521 ± 0.008 | 0.459 | 0.534 | 0.509 | 0.197 | 0.26 | 1.00 |  |
| L5 | mini | listwise K=30 | 0.15 | 0.307 ± 0.019 | 0.216 | 0.286 | 0.331 | 0.076 | 0.26 | 1.00 |  |
| L5 | mini+flagship | cascade band=0.3 | 0.18 | 0.334 ± 0.020 | 0.174 | 0.550 | 0.240 | 0.205 | 0.53 | 1.60 | strong_call_frac=0.61 esc_cands=1.0 |
| L5 | flagship | listwise K=10 | 0.12 | 0.558 ± 0.010 | 0.436 | 0.580 | 0.538 | 0.272 | 0.71 | 1.00 |  |
| L5 | flagship | listwise K=10 + retriever prior | 0.32 | 0.626 ± 0.010 | 0.524 | 0.691 | 0.573 | 0.337 | 0.71 | 1.00 |  |
| L5 | mini+flagship | route θ=0.25 | 0.18 | 0.378 ± 0.023 | 0.220 | 0.443 | 0.330 | 0.180 | 0.77 | 1.38 | escalated=0.39 |
| L5 | mini+flagship | cascade band=0.4 | 0.18 | 0.434 ± 0.011 | 0.285 | 0.550 | 0.359 | 0.236 | 0.79 | 1.98 | strong_call_frac=0.98 esc_cands=4.3 |
| L5 | flagship | retriever-prune p≥0.02 + retriever prior | 0.32 | 0.638 ± 0.018 | 0.514 | 0.685 | 0.597 | 0.352 | 0.88 | 1.00 | mean_kept=15.8 |
| L5 | flagship | retriever-prune p≥0.02 | 0.15 | 0.541 ± 0.015 | 0.391 | 0.543 | 0.539 | 0.273 | 0.88 | 1.00 | mean_kept=15.8 |
| L5 | mini+flagship | cascade reject-only p̂<0.05 | 0.22 | 0.482 ± 0.017 | 0.301 | 0.555 | 0.426 | 0.260 | 1.01 | 2.00 | strong_call_frac=1.00 esc_cands=11.4 |
| L5 | mini | pointwise ×30 | 0.18 | 0.334 ± 0.014 | 0.229 | 0.330 | 0.337 | 0.110 | 1.04 | 30.00 |  |
| L5 | flagship | adaptive-K τ=0.05 | 0.18 | 0.516 ± 0.021 | 0.337 | 0.543 | 0.492 | 0.268 | 1.04 | 1.00 | mean_k=21.0 |
| L5 | mini-thinking | listwise K=10 + retriever prior | 0.32 | 0.581 ± 0.009 | 0.500 | 0.651 | 0.525 | 0.288 | 1.19 | 1.00 |  |
| L5 | mini-thinking | listwise K=10 | 0.10 | 0.500 ± 0.005 | 0.416 | 0.472 | 0.532 | 0.188 | 1.19 | 1.00 |  |
| L5 | mini-thinking | retriever-prune p≥0.02 | 0.15 | 0.473 ± 0.016 | 0.352 | 0.492 | 0.455 | 0.211 | 1.25 | 1.00 | mean_kept=15.8 |
| L5 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.27 | 0.587 ± 0.010 | 0.501 | 0.593 | 0.582 | 0.270 | 1.25 | 1.00 | mean_kept=15.8 |
| L5 | mini-thinking | adaptive-K τ=0.05 | 0.15 | 0.444 ± 0.012 | 0.322 | 0.426 | 0.465 | 0.171 | 1.31 | 1.00 | mean_k=21.0 |
| L5 | mini | self-consistency n=5 | 0.02 | 0.263 ± 0.019 | 0.021 | 0.606 | 0.168 | 0.176 | 1.32 | 5.00 |  |
| L5 | flagship | listwise K=30 + retriever prior | 0.32 | 0.634 ± 0.013 | 0.503 | 0.679 | 0.595 | 0.351 | 1.33 | 1.00 |  |
| L5 | flagship | listwise K=30 | 0.27 | 0.478 ± 0.024 | 0.234 | 0.613 | 0.392 | 0.273 | 1.33 | 1.00 |  |
| L5 | mini+flagship | route θ=0.35 | 0.22 | 0.459 ± 0.018 | 0.254 | 0.539 | 0.400 | 0.243 | 1.39 | 1.85 | escalated=0.84 |
| L5 | mini-thinking | listwise K=30 + retriever prior | 0.32 | 0.580 ± 0.014 | 0.482 | 0.639 | 0.531 | 0.284 | 1.41 | 1.00 |  |
| L5 | mini-thinking | listwise K=30 | 0.22 | 0.398 ± 0.019 | 0.229 | 0.486 | 0.337 | 0.187 | 1.41 | 1.00 |  |
| L5 | flagship | pointwise ×30 | 0.32 | 0.513 ± 0.021 | 0.269 | 0.660 | 0.420 | 0.322 | 5.37 | 30.00 |  |
| L5 | flagship | self-consistency n=5 | 0.02 | 0.490 ± 0.025 | 0.196 | 0.682 | 0.382 | 0.266 | 6.63 | 5.00 |  |
| L5 | mini-thinking | self-consistency n=5 | 0.02 | 0.383 ± 0.020 | 0.107 | 0.639 | 0.274 | 0.211 | 7.07 | 5.00 |  |
| L5 | mini-thinking | pointwise ×30 | 0.22 | 0.426 ± 0.014 | 0.270 | 0.452 | 0.403 | 0.200 | 20.26 | 30.00 |  |

## Same policies at a fixed threshold of 0.5 (the v1 comparison; different operating points — for reference only)

### L1

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.50 | 0.223 ± 0.005 | 0.223 | 0.640 | 0.135 | 0.178 | 0.00 | 0.00 | no LLM call |
| L1 | mini | listwise K=10 | 0.50 | 0.414 ± 0.009 | 0.329 | 0.884 | 0.270 | 0.262 | 0.19 | 1.00 |  |
| L1 | mini | listwise K=10 + retriever prior | 0.50 | 0.618 ± 0.005 | 0.578 | 0.797 | 0.504 | 0.336 | 0.19 | 1.00 |  |
| L1 | mini | retriever-prune p≥0.02 | 0.50 | 0.415 ± 0.010 | 0.322 | 0.836 | 0.276 | 0.257 | 0.25 | 1.00 | mean_kept=15.7 |
| L1 | mini | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.618 ± 0.005 | 0.572 | 0.786 | 0.509 | 0.333 | 0.25 | 1.00 | mean_kept=15.7 |
| L1 | mini | adaptive-K τ=0.05 | 0.50 | 0.403 ± 0.009 | 0.308 | 0.788 | 0.271 | 0.246 | 0.30 | 1.00 | mean_k=20.9 |
| L1 | mini | listwise K=30 + retriever prior | 0.50 | 0.595 ± 0.005 | 0.546 | 0.774 | 0.483 | 0.319 | 0.39 | 1.00 |  |
| L1 | mini | listwise K=30 | 0.50 | 0.368 ± 0.009 | 0.270 | 0.713 | 0.248 | 0.222 | 0.39 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.3 | 0.50 | 0.575 ± 0.007 | 0.477 | 0.893 | 0.424 | 0.341 | 0.86 | 1.87 | strong_call_frac=0.86 esc_cands=2.0 |
| L1 | flagship | listwise K=10 | 0.50 | 0.662 ± 0.005 | 0.567 | 0.933 | 0.513 | 0.414 | 0.94 | 1.00 |  |
| L1 | flagship | listwise K=10 + retriever prior | 0.50 | 0.748 ± 0.003 | 0.696 | 0.877 | 0.652 | 0.471 | 0.94 | 1.00 |  |
| L1 | mini+flagship | cascade band=0.4 | 0.50 | 0.653 ± 0.007 | 0.562 | 0.881 | 0.518 | 0.393 | 1.03 | 1.98 | strong_call_frac=0.98 esc_cands=4.2 |
| L1 | mini+flagship | cascade reject-only p̂<0.05 | 0.50 | 0.685 ± 0.005 | 0.587 | 0.861 | 0.569 | 0.422 | 1.21 | 2.00 | strong_call_frac=1.00 esc_cands=7.6 |
| L1 | flagship | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.768 ± 0.003 | 0.705 | 0.864 | 0.691 | 0.495 | 1.24 | 1.00 | mean_kept=15.7 |
| L1 | flagship | retriever-prune p≥0.02 | 0.50 | 0.680 ± 0.005 | 0.571 | 0.897 | 0.547 | 0.428 | 1.24 | 1.00 | mean_kept=15.7 |
| L1 | mini+flagship | evidence-cascade L5→L1 band=0.45 | 0.50 | 0.646 ± 0.009 | 0.539 | 0.830 | 0.529 | 0.385 | 1.27 | 2.00 | strong_call_frac=1.00 esc_cands=11.1 |
| L1 | mini+flagship | evidence-cascade L5→L1 reject-only | 0.50 | 0.648 ± 0.011 | 0.542 | 0.834 | 0.530 | 0.390 | 1.27 | 2.00 | strong_call_frac=1.00 esc_cands=11.1 |
| L1 | mini-thinking | listwise K=10 | 0.50 | 0.568 ± 0.007 | 0.480 | 0.915 | 0.412 | 0.340 | 1.27 | 1.00 |  |
| L1 | mini-thinking | listwise K=10 + retriever prior | 0.50 | 0.699 ± 0.005 | 0.656 | 0.844 | 0.597 | 0.413 | 1.27 | 1.00 |  |
| L1 | mini | pointwise ×30 | 0.50 | 0.468 ± 0.011 | 0.381 | 0.726 | 0.346 | 0.257 | 1.29 | 30.00 |  |
| L1 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.710 ± 0.004 | 0.656 | 0.834 | 0.617 | 0.419 | 1.38 | 1.00 | mean_kept=15.7 |
| L1 | mini-thinking | retriever-prune p≥0.02 | 0.50 | 0.582 ± 0.007 | 0.484 | 0.871 | 0.437 | 0.346 | 1.38 | 1.00 | mean_kept=15.7 |
| L1 | mini-thinking | adaptive-K τ=0.05 | 0.50 | 0.569 ± 0.005 | 0.466 | 0.833 | 0.432 | 0.327 | 1.49 | 1.00 | mean_k=20.9 |
| L1 | flagship | adaptive-K τ=0.05 | 0.50 | 0.674 ± 0.005 | 0.558 | 0.867 | 0.551 | 0.421 | 1.52 | 1.00 | mean_k=20.9 |
| L1 | mini-thinking | listwise K=30 + retriever prior | 0.50 | 0.691 ± 0.006 | 0.631 | 0.817 | 0.599 | 0.402 | 1.66 | 1.00 |  |
| L1 | mini-thinking | listwise K=30 | 0.50 | 0.538 ± 0.006 | 0.430 | 0.767 | 0.414 | 0.295 | 1.66 | 1.00 |  |
| L1 | mini+flagship | route θ=0.25 | 0.50 | 0.617 ± 0.009 | 0.497 | 0.825 | 0.493 | 0.363 | 1.92 | 1.77 | escalated=0.77 |
| L1 | mini | self-consistency n=5 | 0.50 | 0.346 ± 0.008 | 0.212 | 0.936 | 0.212 | 0.249 | 1.96 | 5.00 |  |
| L1 | flagship | listwise K=30 + retriever prior | 0.50 | 0.756 ± 0.005 | 0.682 | 0.852 | 0.680 | 0.484 | 1.99 | 1.00 |  |
| L1 | flagship | listwise K=30 | 0.50 | 0.649 ± 0.005 | 0.527 | 0.813 | 0.540 | 0.387 | 1.99 | 1.00 |  |
| L1 | mini+flagship | route θ=0.35 | 0.50 | 0.642 ± 0.006 | 0.522 | 0.815 | 0.530 | 0.378 | 2.27 | 1.94 | escalated=0.94 |
| L1 | flagship | pointwise ×30 | 0.50 | 0.721 ± 0.006 | 0.621 | 0.833 | 0.636 | 0.454 | 6.66 | 30.00 |  |
| L1 | mini-thinking | self-consistency n=5 | 0.50 | 0.560 ± 0.006 | 0.419 | 0.949 | 0.397 | 0.359 | 8.31 | 5.00 |  |
| L1 | flagship | self-consistency n=5 | 0.50 | 0.689 ± 0.006 | 0.542 | 0.961 | 0.537 | 0.465 | 9.96 | 5.00 |  |
| L1 | mini-thinking | pointwise ×30 | 0.50 | 0.629 ± 0.007 | 0.537 | 0.792 | 0.522 | 0.359 | 20.74 | 30.00 |  |

### L5

| level | model | policy | thr | F1 ± CI95 | F1 non-mem | P | R | exact-set | ¢/query | calls/query | note |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| — | none | retriever-only (no LLM) | 0.50 | 0.223 ± 0.005 | 0.223 | 0.640 | 0.135 | 0.178 | 0.00 | 0.00 | no LLM call |
| L5 | mini | listwise K=10 | 0.50 | 0.195 ± 0.009 | 0.012 | 0.927 | 0.109 | 0.208 | 0.14 | 1.00 |  |
| L5 | mini | listwise K=10 + retriever prior | 0.50 | 0.458 ± 0.006 | 0.365 | 0.752 | 0.329 | 0.262 | 0.14 | 1.00 |  |
| L5 | mini | retriever-prune p≥0.02 | 0.50 | 0.205 ± 0.008 | 0.010 | 0.895 | 0.116 | 0.209 | 0.18 | 1.00 | mean_kept=15.7 |
| L5 | mini | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.461 ± 0.008 | 0.358 | 0.750 | 0.333 | 0.265 | 0.18 | 1.00 | mean_kept=15.7 |
| L5 | mini | adaptive-K τ=0.05 | 0.50 | 0.201 ± 0.007 | 0.007 | 0.855 | 0.114 | 0.203 | 0.21 | 1.00 | mean_k=20.9 |
| L5 | mini | listwise K=30 + retriever prior | 0.50 | 0.444 ± 0.005 | 0.341 | 0.736 | 0.318 | 0.254 | 0.26 | 1.00 |  |
| L5 | mini | listwise K=30 | 0.50 | 0.195 ± 0.009 | 0.005 | 0.804 | 0.111 | 0.196 | 0.26 | 1.00 |  |
| L5 | mini+flagship | cascade band=0.3 | 0.50 | 0.286 ± 0.008 | 0.053 | 0.899 | 0.170 | 0.242 | 0.53 | 1.59 | strong_call_frac=0.59 esc_cands=0.9 |
| L5 | flagship | listwise K=10 | 0.50 | 0.411 ± 0.010 | 0.097 | 0.949 | 0.262 | 0.303 | 0.71 | 1.00 |  |
| L5 | flagship | listwise K=10 + retriever prior | 0.50 | 0.598 ± 0.004 | 0.457 | 0.819 | 0.471 | 0.362 | 0.71 | 1.00 |  |
| L5 | mini+flagship | route θ=0.25 | 0.50 | 0.314 ± 0.008 | 0.033 | 0.880 | 0.191 | 0.255 | 0.76 | 1.38 | escalated=0.37 |
| L5 | mini+flagship | cascade band=0.4 | 0.50 | 0.369 ± 0.011 | 0.105 | 0.880 | 0.234 | 0.273 | 0.78 | 1.98 | strong_call_frac=0.98 esc_cands=4.2 |
| L5 | flagship | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.609 ± 0.007 | 0.441 | 0.819 | 0.485 | 0.380 | 0.88 | 1.00 | mean_kept=15.7 |
| L5 | flagship | retriever-prune p≥0.02 | 0.50 | 0.431 ± 0.010 | 0.088 | 0.930 | 0.280 | 0.322 | 0.88 | 1.00 | mean_kept=15.7 |
| L5 | mini+flagship | cascade reject-only p̂<0.05 | 0.50 | 0.418 ± 0.009 | 0.096 | 0.886 | 0.274 | 0.306 | 1.01 | 2.00 | strong_call_frac=1.00 esc_cands=11.2 |
| L5 | mini | pointwise ×30 | 0.50 | 0.236 ± 0.011 | 0.025 | 0.804 | 0.138 | 0.213 | 1.04 | 30.00 |  |
| L5 | flagship | adaptive-K τ=0.05 | 0.50 | 0.430 ± 0.010 | 0.077 | 0.908 | 0.282 | 0.320 | 1.04 | 1.00 | mean_k=20.9 |
| L5 | mini-thinking | listwise K=10 + retriever prior | 0.50 | 0.536 ± 0.005 | 0.420 | 0.790 | 0.406 | 0.315 | 1.19 | 1.00 |  |
| L5 | mini-thinking | listwise K=10 | 0.50 | 0.308 ± 0.008 | 0.055 | 0.940 | 0.184 | 0.253 | 1.19 | 1.00 |  |
| L5 | mini-thinking | retriever-prune p≥0.02 | 0.50 | 0.320 ± 0.008 | 0.042 | 0.910 | 0.194 | 0.259 | 1.25 | 1.00 | mean_kept=15.7 |
| L5 | mini-thinking | retriever-prune p≥0.02 + retriever prior | 0.50 | 0.544 ± 0.007 | 0.409 | 0.789 | 0.415 | 0.320 | 1.25 | 1.00 | mean_kept=15.7 |
| L5 | mini-thinking | adaptive-K τ=0.05 | 0.50 | 0.319 ± 0.008 | 0.038 | 0.883 | 0.195 | 0.256 | 1.31 | 1.00 | mean_k=20.9 |
| L5 | mini | self-consistency n=5 | 0.50 | 0.205 ± 0.011 | 0.001 | 0.958 | 0.115 | 0.217 | 1.32 | 5.00 |  |
| L5 | flagship | listwise K=30 + retriever prior | 0.50 | 0.602 ± 0.008 | 0.423 | 0.811 | 0.479 | 0.374 | 1.33 | 1.00 |  |
| L5 | flagship | listwise K=30 | 0.50 | 0.424 ± 0.011 | 0.064 | 0.871 | 0.280 | 0.307 | 1.33 | 1.00 |  |
| L5 | mini+flagship | route θ=0.35 | 0.50 | 0.401 ± 0.010 | 0.059 | 0.876 | 0.260 | 0.295 | 1.39 | 1.85 | escalated=0.86 |
| L5 | mini-thinking | listwise K=30 + retriever prior | 0.50 | 0.531 ± 0.008 | 0.391 | 0.780 | 0.402 | 0.313 | 1.41 | 1.00 |  |
| L5 | mini-thinking | listwise K=30 | 0.50 | 0.309 ± 0.011 | 0.031 | 0.835 | 0.190 | 0.240 | 1.41 | 1.00 |  |
| L5 | flagship | pointwise ×30 | 0.50 | 0.473 ± 0.009 | 0.135 | 0.845 | 0.328 | 0.343 | 5.37 | 30.00 |  |
| L5 | flagship | self-consistency n=5 | 0.50 | 0.434 ± 0.012 | 0.022 | 0.983 | 0.278 | 0.355 | 6.63 | 5.00 |  |
| L5 | mini-thinking | self-consistency n=5 | 0.50 | 0.322 ± 0.008 | 0.008 | 0.974 | 0.193 | 0.277 | 7.07 | 5.00 |  |
| L5 | mini-thinking | pointwise ×30 | 0.50 | 0.362 ± 0.008 | 0.080 | 0.822 | 0.233 | 0.272 | 20.26 | 30.00 |  |

## Sensitivity sweep (648 worlds × 2 levels; 4 seeds: thresholds on seeds 0–1, policy selection on seed 2, evaluation on seed 3)

- elapsed: 635.3 s
- share of worlds where the policy selected at ≤105 % of today's budget beats today's design by > 0.02 F1 on the held-out seed: L1 76%, L5 86% (mean held-out gain +0.070 / +0.130)
- listwise + retriever prior − listwise (flagship, same cost): median +0.046, 10–90 % [-0.041, +0.206]
- retriever-prune − listwise (flagship): median +0.024, 10–90 % [-0.008, +0.122] at median 67% of cost
- retriever-prune + retriever prior − listwise (flagship): median +0.061, 10–90 % [-0.033, +0.214] at median 67% of cost
- K=10 + retriever prior − listwise K=30 (flagship): median +0.067, 10–90 % [-0.066, +0.223] at ≈ 47 % of cost
- MINI listwise + retriever prior − FLAGSHIP listwise (≈ 20 % of cost): median -0.047, 10–90 % [-0.210, +0.174]
- adaptive-K − listwise (flagship): median +0.017, 10–90 % [-0.003, +0.106] at median 80% of cost
- K=10 − K=30 (flagship): median +0.045, 10–90 % [-0.056, +0.145]
- cascade band 0.4 − listwise (flagship): median -0.015, 10–90 % [-0.061, +0.039] at median 57% of cost
- pointwise − listwise (flagship): median +0.048, 10–90 % [-0.016, +0.136] at 3.5–5× cost
- self-consistency n=5 − single (flagship): median +0.069, 10–90 % [-0.167, +0.101] at 5× cost
- retriever-only (no LLM) − flagship listwise: median -0.128, 10–90 % [-0.411, +0.197]

Best policy at budget (selected on seed 2), by world:

level  best_policy_at_budget                              
L1     flagship · adaptive-K τ=0.05                            18
       flagship · listwise K=10                                58
       flagship · listwise K=10 + retriever prior             156
       flagship · listwise K=30                                96
       flagship · listwise K=30 + retriever prior              88
       flagship · retriever-prune p≥0.02                       28
       flagship · retriever-prune p≥0.02 + retriever prior     46
       mini+flagship · cascade reject-only p̂<0.05            158
L5     flagship · adaptive-K τ=0.05                            22
       flagship · listwise K=10                                48
       flagship · listwise K=10 + retriever prior             239
       flagship · listwise K=30                                33
       flagship · listwise K=30 + retriever prior              99
       flagship · retriever-prune p≥0.02                        2
       flagship · retriever-prune p≥0.02 + retriever prior    125
       mini+flagship · cascade reject-only p̂<0.05              8
       none · retriever-only (no LLM)                          72

By assumption — mean held-out gain of the selected policy, and the fusion gain (LW+prior − LW, flagship):

                                    gain_heldout  rp_minus_lw  prune_minus_lw  k10_minus_lw
level rho_retriever_llm mem_keying                                                         
L1    0.0               record             0.108        0.092           0.053         0.056
                        word               0.108        0.092           0.053         0.056
      0.5               record             0.053       -0.004           0.026         0.020
                        word               0.053       -0.004           0.026         0.020
      0.8               record             0.050       -0.026           0.023         0.016
                        word               0.050       -0.026           0.023         0.016
L5    0.0               record             0.151        0.142           0.063         0.071
                        word               0.215        0.198           0.104         0.134
      0.5               record             0.080        0.063           0.024         0.019
                        word               0.134        0.115           0.053         0.066
      0.8               record             0.074        0.046           0.018         0.013
                        word               0.129        0.098           0.041         0.051

Fusion gain by retriever strength and error correlation:

rho_retriever_llm    0.0    0.5    0.8
retriever_dprime                      
1.0                0.057 -0.015 -0.034
1.5                0.128  0.034  0.015
2.0                0.208  0.108  0.088

Share of worlds where the retriever alone (no LLM) beats the flagship listwise K=30, by level: L1 4%, L5 51%
