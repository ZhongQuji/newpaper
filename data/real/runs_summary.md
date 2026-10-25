# Real experiment ledger (extracted verbatim from the export)

- suite JSON dumps parsed: **53**
- distinct runs (unique `run_dir`): **65** — rc=0: 62, rc≠0: 3
- pending / never-started job entries: 226
- total API calls: **9,178**; prompt tokens: **15,151,717**; completion tokens: **1,457,088**
- total relay cost: **$100.07**; total wall time: **17.7 h**

## Per-model totals

| model | runs | calls | prompt tok | completion tok | cost USD | wall h |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| xj-gpt-4.1 | 13 | 1,746 | 2,620,011 | 100,388 | 26.77 | 3.0 |
| xj-gpt-4.1-mini | 26 | 4,027 | 5,933,188 | 218,829 | 12.09 | 7.1 |
| xj-gpt-5.4 | 13 | 1,546 | 2,851,962 | 113,761 | 28.02 | 2.8 |
| xj-gpt-5.4-mini | 13 | 1,859 | 3,746,556 | 1,024,110 | 33.19 | 4.8 |

## Failed runs (rc≠0)

- `20261024_042813_e16_visual_L3_xj-gpt-4.1` (xj-gpt-4.1, E16_visual_L3_dev): rc=1, calls=9, api_errors=0, 93.6 s
- `20261024_042949_e8v2_cf_forced_choice_xj-gpt-4.1v4_noevidence_maskcreator` (xj-gpt-4.1, E8v4_noevidence_maskcreator): rc=1, calls=0, api_errors=0, 13.6 s
- `20261024_234820_e10_agent_L5-P_xj-gpt-5.4` (xj-gpt-5.4, E10_agent_L5P_test): rc=1, calls=4, api_errors=4, 504.9 s

## Served-model audit

- runs where the relay served a different model than requested: **0**
