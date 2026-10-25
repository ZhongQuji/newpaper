# Work log

All times are Asia/Shanghai (UTC+8). One line per unit of work.

| time | status | entry |
| --- | --- | --- |
| 2026-10-25 16:49:18 CST | START | Session opened. Inputs: user export of newpaper tool-call outputs (284 KB, 8285 lines, 55 suite JSON dumps) copied to data/raw/. Constraint: local MFMCP server unreachable (3 auth timeouts across two days) → working in GitHub repo ZhongQuji/newpaper on branch cursor/reunion-paper-review-sim-b15e. No LLM API keys in this VM → all new experiments are calibrated simulations, clearly labelled; all token/cost/latency numbers come from the real export. |
| 2026-10-25 16:49:18 CST | NOTE | Repo skeleton created: data/{raw,real} docs figures/{real,paper} sim/results logs tools. Python 3.12 + matplotlib 3.11 / numpy 2.5 / pandas 3.1 / scipy 1.18 / seaborn 0.13 installed (user site). |
| 2026-10-25 16:49:18 CST | CHECK | Secret scan of raw export (sk-*, api_key, password, token=) → 0 hits; safe to commit to public repo. |
| 2026-10-25 16:50:25 CST | DONE | tools/extract_real_runs.py → data/real/runs.csv|json|runs_summary.md|campaign_log_tail.txt. 53 suite dumps → 65 distinct runs (62 rc=0, 3 rc≠0), 9,178 calls, 15.15M prompt / 1.46M completion tokens, $100.07 relay cost, 17.7 h wall. Served-model audit: 0 mismatches. |
| 2026-10-25 16:50:25 CST | NOTE | Operational finding from campaign log: the L5-P (dims-permute) TEST campaign failed on all 3 models on 10-24 22:31 (gemini-3-pro rc=1 after 77 min, claude-opus-4.6 rc=1, gpt-5.4 rc=1 with 4 api_errors / 0 usage) and was restarted 10-25 00:20 — result unknown in export. Flagged in STATUS as something to re-check locally. |
| 2026-10-25 16:54:44 CST | DONE | docs/01_project_reconstruction.md written (task, info-level ladder fingerprinted by prompt tokens/call, E5–E17 map, controls, real cost structure, unknowns). |
| 2026-10-25 16:54:44 CST | START | Spawned 6 background subagents in parallel: 5 reviewer pairs (NeurIPS-stats+ICLR-novelty, ACL-contamination+CVPR-multimodal, DH-art-history+CHI-HCI, SIGIR-retrieval+AAAI-agents/cost, FAccT-ethics+Area-Chair meta) → docs/reviews/reviewer_01..10.md, and 1 related-work scout with web search → docs/02_related_work_positioning.md. Briefing/contract: docs/reviews/_briefing.md. |
| 2026-10-25 16:54:44 CST | START | Figures from REAL ledger: tools/plot_real_ledger.py → figures/real/*.pdf|png |
| 2026-10-25 16:59:55 CST | DONE | figures/real/R1–R7 (PDF+PNG) + CAPTIONS.md rendered from real ledger; visually inspected each PNG; fixed: L2-T pilot runs (5/17 calls, 10-23) excluded from ladder, legend/title overlaps, date axis, L2-T 91/32 scaling line. Caught and corrected my own wrong caption ('~1,000×' → verified 53× for E17 vs GPT-4.1-mini L1 agent). |
