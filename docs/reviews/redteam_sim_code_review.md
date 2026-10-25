# Red-team code review — `sim/reunion_sim.py`, `sim/power_analysis.py`

Adversarial review (statistics / simulation methodology). Both scripts were read line by line and
probed with scratch experiments against the committed code (scripts in `/tmp/rt/`, not in the
repo). The base run reproduces bit-exactly (`run_all(World(Q=3000), 8)` vs
`policies_summary.csv`: max |ΔF1| = 0, max |Δ$| = 0) and all 64 single-model cost rows satisfy
`usd = prompt·p_in + completion·p_out` to 1e-18.

## Verdict (3 sentences)

The code is clean and reproducible; I found no indexing, broadcasting or ground-truth-leak bug
that silently corrupts a result. The *comparison* is not fair: every policy is scored at a fixed
posterior threshold of 0.5 under a 5.8 % prior (different operating points), the retriever
posterior and the cheap model's confidence are oracles, and in the base world the L5 evidence
channel is dead (non-memorised F1 = 0.06), so the L5 ranking is a ranking of how policies treat
memorised queries. The headline orderings (cascade wins, adaptive-K "never loses", 87 %/95 % of
worlds) therefore do not "transfer" as claimed, and the M5 price in `docs/04` ("$0.0065, −67 %")
contradicts the sim's own output ($0.0132, −34 %).

## Bugs found

1. **`sim/reunion_sim.py:64,197-198` — pointwise cost is level- and model-blind.** 240 prompt
   tok/candidate at L5 as at L1 (E10e was measured at L1 only) and 5 completion tok/call for every
   model, including the thinking mini (ledger: 475–694). RUNLOG prices mini-thinking pointwise at
   2.67 ¢; with 500 tok/call it is 32.9 ¢. Pointwise/listwise cost is 3.5× at L1 but 5.2× at L5,
   while README says "3.5×" and RUNLOG "3×". Fix: per-call prompt = overhead +
   `per_cand_tokens(level)`, model-specific completion. Changes the S1/S2 Pareto frontier
   (mini-thinking pointwise sits on it) and the "3.5×" text; not the winner counts.
2. **`sim/reunion_sim.py:145,310` — self-consistency correlation is 0.75, not the documented 0.5.**
   Inter-sample correlation is ρ_sc + (1−ρ_sc)·ρ_models = 0.75 (measured 0.751; 0.65/0.85 in the
   sweep). With a true 0.5 the SC gain rises from +0.023 to +0.037 (L1 flagship). Headline 5
   survives (5× cost) but README's "ρ_sc = .5" is false. Fix: solve the shared weight for the
   total correlation.
3. **`sim/reunion_sim.py:294-295` — route uses the min margin over all 30 candidates**, not the
   "candidates in play" of the comment; one noisy irrelevant candidate escalates the whole query
   (escalation 0.44–0.86 at L1). M12's "routing is weaker (19/432)" rests on this definition.
4. **`sim/reunion_sim.py:635` — "beats today's design" is gain > 0.005 on 2 seeds × 1,500
   queries**, below the Monte-Carlo noise (sd of pointwise−listwise at β=0 is 0.007). At gain > 0.02
   the share is 66 % (L1) / 70 % (L5), not 87/95. Select-on-seeds-A / evaluate-on-B over 12 cells:
   every "gain" ≤ 0.006 vanishes on fresh seeds. Fix: hold-out seeds, threshold 0.02.
5. **`docs/04_method_redesign.md:86-88` (M5 price) — not derivable from the sim.** It assumes the
   flagship is called on 40 % of queries over ≈8 candidates; the sim's reject-only policy calls it
   on 99 % of queries over 9.6 (`policies_raw.csv` extra, calls/query 1.99) → $0.0132 = 66 % of
   today, which README itself quotes. "$0.0065, −67 %" and §3's "−40 … −63 %" are off by ~2×.
6. **`sim/power_analysis.py:59` — fine.** Continuity-corrected McNemar: MDD 0.152 (n=80) vs exact
   binomial 0.149 vs uncorrected 0.139 — the right conservative choice. The percentile cluster
   bootstrap is anti-conservative at n=80 (Type I 0.043–0.090 in `power_curves.csv`), so its
   smaller MDD column is partly inflated α.
7. Trivia: `summarize:386` uses 1.96 with 8 seeds (t₇ = 2.36); `run_all:349` `conf` is dead;
   `prior = np.mean(y)` leaks realised prevalence (0.0582 vs 0.0587), uniformly, harmless.
   `pol_adaptive_k`'s tail logic and `pred[:, k:]` are correct (checked by hand). RNG is seeded
   everywhere; adding a policy reshuffles the stream for later ones (fragile, not wrong).

## Unfair or misleading modelling choices

1. **HIGH — fixed 0.5 threshold ⇒ different operating points.** Under prior 0.058 the rule sits
   high on the precision axis (L1 flagship P 0.81 / R 0.53). Scoring each policy at its own
   F1-optimal threshold (same oracle for all) reorders the table: L1 — prune 0.730, pointwise 0.725,
   K=10 0.723, cascade 0.712, LW30 0.665; L5 — K=10 goes from −0.009 to **+0.087** vs LW30, prune
   +0.064, cascade +0.032. "Same decision rule" ≠ "same operating point".
2. **HIGH — at L5 the evidence channel is dead; the mini is memory-only.** Non-memorised queries,
   base world: flagship LW30 F1 0.060 (recall 0.03), mini 0.006; memorised 0.85–0.93. All L5
   differences (headline 1's "95 %", the cascade's 99 L5 wins) concern the 30 % memorised queries.
   `p_mem` is query-level, shared by both models with the same d'_mem = 4, so the mini "remembers"
   exactly what the flagship does and the cascade gets two d'=4 looks (memorised F1 0.93 vs 0.88).
3. **HIGH — oracle retriever posterior** (`retriever_posterior:126-131` uses the true d'_r and
   member distribution). Believe d'_r = 2.0 when the truth is 1.0: prune −0.063, adaptive-K −0.020,
   so "never loses more than 0.01" is an oracle-only statement; the sweep never mis-specifies it.
   Worse: the same posterior used as the per-candidate prior *inside* the plain listwise decision
   (zero extra cost) gives **+0.116 (L1) / +0.189 (L5)** — more than any policy in the table. The
   omitted baseline dominates the frontier, and a real system with logprob P(yes) can do it.
4. **HIGH — cascade/route/abstain consume perfectly calibrated confidence.** Over-confidence ×1.4
   is monotone and keeps the confidence ranking intact. Same escalation fraction (12 %) but random
   candidates: cascade 0.538 at L1, *below* LW30 0.640. "Two models beat one" is a bet on
   confidence informativeness, which the sweep never probes and `docs/04 §5` admits is the weak spot.
5. **MED — "every assumption swept" is false.** Fixed: member_probs, d'_mem, per-level d' values,
   ρ_sc, pointwise jitter 0.35, FIXED_PROMPT = 400 (contradicted by the 240-token pointwise call),
   the thinking-mini multiplier, base_acc 0.6 and λ in the power model.
6. **MED — README claims not matching the sweep.** Cascade "is *not* the winner when β = 0": it is
   best-at-budget in 44/144 β=0 cells (second to adaptive-K 57; K=10 wins 0) by noise-level margins
   (−0.012 L1 / +0.011 L5). "Survives ρ = 0.7 with a smaller margin": it wins *more* often (96 vs
   74) with a *larger* mean gain. "+0.036 at 67 %" for retriever-prune is L1 only (L5 +0.011, 74 %).
7. **MED — power labels overstate what is simulated.** "ICC = 0.3" is latent-scale; outcome ICC is
   0.09 with mean cluster size 1.9 (design effect 1.08). ICC "barely matters" because clusters are
   tiny and the level effect is a pure intercept shift; the Reading then demands ensemble bootstraps
   on the strength of 0.103 → 0.110. Realised outcome correlation is φ = 0.45/0.65 (0.33 even at
   ρ_pair = 0), not "ρ_pair".
8. **LOW** — "pairwise F1" is micro-F1 over query × candidate cells; `docs/04 §3` credits the
   never-simulated v2 pipeline with "quality equal or higher in 87–95 % of worlds" (that is
   best-of-~20 policies per world).

## Sanity experiments I ran (command + result)

- `python3 /tmp/rt/exp1.py` — d'=0, p_mem=0: every policy predicts nothing, F1 = 0 ✓; d'=0,
  p_mem=0.3: F1 0.39 (memory floor ≈ base-world mini L5 0.393); p_mem=1: ladder flat 0.868–0.881 ✓,
  mini = flagship; SC inter-sample corr 0.751; pointwise cost identical at L1/L5.
- `python3 /tmp/rt/exp2.py` — F1 at 0.5 vs F1-optimal threshold, 8 policies (item 1); listwise +
  retriever prior +0.116/+0.189 at equal cost.
- `python3 /tmp/rt/exp3.py` — random-escalation cascade 0.538 vs calibrated 0.689 vs LW30 0.640;
  mis-calibrated d'_r grid; β=0 cascade −0.012/+0.011; split-sample winner's curse (mean gain
  0.031 → 0.029; near-ties → 0).
- `python3 /tmp/rt/exp4.py`, `exp4b.py` — every MDD in `POWER.md` recomputed from
  `power_curves.csv` (match to 3 dp); Type I at Δ=0 McNemar 0.017–0.041, bootstrap 0.030–0.090;
  CC/exact/uncorrected MDD 0.152/0.149/0.139; outcome ICC 0.09; binomial half-widths 0.107/0.056 ≈
  table; ensemble × level interaction (sd 0.8) leaves McNemar at 0.045–0.058.
- Inline pandas on the CSVs: 87/95 % ✓ (66/70 % at 0.02); mean gain 0.058/0.049 at 63/77 % ✓;
  170, 146, 19, 17 /432 ✓; aK min −0.008, cost 66–92 % (README "70–90") ~✓; d'_r=2 → +0.044 at
  70 % ✓; mini pointwise 45/144 at β=0.12 ✓; abstain 18.5 % → P 0.918 ✓; memory ratio 0.49 ✓.

## Numbers quoted in README/docs that I could not reproduce

- `docs/04` M5: "$0.0065/query, −67 %", "≈40 % of queries over ≈8 candidates" → sim $0.0132,
  −34 %, 99 % of queries over 9.6; §3 "−40 … −63 %" inherits it.
- `docs/04 §3`: v2 "equal or higher in 87–95 % of worlds" — v2 is not simulated.
- README/RUNLOG: pointwise "3.5×"/"3×" (3.5× L1, 5.2× L5); mini-thinking pointwise 2.67 ¢ (≈33 ¢).
- README: "ρ_sc = .5" (0.75); cascade "not the winner when β=0" (44/144); "smaller margin at
  ρ=0.7" (larger); "every one swept" (nine fixed knobs); "+0.036 at 67 %" is L1-only.
- Everything else in README "Headline findings" and `POWER.md` reproduces from the CSVs.

## Recommended changes (prioritised)

1. Compare at matched operating points: tune the threshold per policy on held-out seeds (or report
   best-F1 / PR-AUC and F1 at equal precision); re-derive every ordering claim.
2. Add the zero-cost baseline "listwise with retriever-informed prior"; if it dominates, say so and
   demote the cascade. Sweep mis-calibrated retriever posteriors (believed ≠ true d'_r).
3. Replace the over-confidence knob with a confidence-*informativeness* knob (noise on the
   confidence used for routing, not on the decision) and re-run cascade/route/abstain.
4. Make memorisation model-specific (lower p_mem and d'_mem for the mini); stratify every headline by
   memorised/non-memorised; state that base-world L5 is a memory-only regime.
5. Fix pointwise cost, the SC correlation composition, the route margin, the M5 price; regenerate
   S1/S2 and RUNLOG.
6. ≥ 4 held-out seeds in the sweep; report "beats" at gain > 0.02; drop "87 %/95 %".
7. Power: report outcome-scale ICC and realised φ; sweep base accuracy and cluster sizes (real
   ensembles may exceed 4); keep the McNemar continuity correction.
8. Rewrite "what transfers": with 1–4 open, neither orderings nor curve shapes are shown robust;
   what honestly transfers is the list of cheap real experiments (`--k 10` vs `--k 30`, logprob
   calibration, memorised stratification), not the verdicts.
