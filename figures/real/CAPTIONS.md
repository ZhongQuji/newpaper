# Captions and provenance for figures/real

All data: `data/real/runs.csv` (rc = 0 rows unless stated). Derived columns are per-call ratios of verbatim totals.

**R1_ladder_prompt_tokens** — mean prompt tokens per call of `llm_reunion_agent.py` dev runs grouped by ladder level (L1, L1 v2 inputs, L2-T, L3, L3-H, L3-H2 holder-scrub v2, L5, L5-P dims-permute, L6 withhold-title). Circles: per-model means — identical to within ±2 tokens, proving all models saw the same prompts.

**R2_reasoning_tax** — (a) mean completion tokens per call by model and level (dev agent runs). GPT-5.4 mini (reasoning_effort=low, hidden reasoning billed as completion) emits 475–766 tokens/query vs 41–91 for the non-thinking models. (b) Resulting relay cost per query at L1: the 'mini' thinking model (1.62¢) is within 20 % of GPT-4.1 (2.00¢) and GPT-5.4 (1.96¢) and 3.9× GPT-4.1 mini (0.42¢).

**R3_cost_per_query_roads** — relay USD per query for each experimental 'road', one dot per model run (dev split). Per-query = cost_usd / calls, except E15/E17 (cost_usd / --limit queries) and E16 (2 calls per query). Grey annotations: ratio of the most expensive dot on each row to the GPT-4.1 mini agent at L1 ($0.0042/query). The open-pool deep-research road (GPT-5.4, $0.22/query) is ~53× the cheapest shortlist agent and ~11× the same model's shortlist agent at L1 ($0.0196).

**R4_budget_breakdown** — totals by experiment family over all 65 runs (including the 3 failed ones). The listwise agent is 54 % of calls but 74 % of spend.

**R5_latency** — mean (dot) and min–max (bars) of seconds per call across dev and test agent runs per level. Interactive use would need <5 s; GPT-5.4 mini's test runs at L3-H/L5 took 14–15 s per query.

**R6_campaign_timeline** — each bar is one run (start from `run_dir` timestamp, length = `seconds`). Three failed runs (red outline): E16 visual L3 on GPT-4.1 (10-24 04:28), E8v4 no-evidence on GPT-4.1 (10-24 04:29, 0 calls), and the L5-P test on GPT-5.4 (10-24 23:48, 4 API errors).

**R7_dev_to_test_cost** — for levels run on both splits, total cost of the dev run vs the test run. Full-ladder points lie on the 294/80 line and L2-T points on the 91/32 line, so a dev run predicts a full test run's cost to within a few percent — a useful planning fact for budgeting the remaining models.
