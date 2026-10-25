# 04 · Method redesign (v2) — a measurement first, a frugal system second

> v2 supersedes the v1 of this document after a second, adversarial review round
> (`docs/reviews/redteam_*.md`). The main changes: the simulation now compares policies at
> matched operating points, which reverses one of v1's headline claims (two-model cascades no
> longer beat single-model "read less" policies) and surfaces a zero-cost mechanism v1 missed
> (fusing the retriever score into the LLM decision); the ladder measurement and the frugal
> system are kept strictly separate; prices are taken from the simulation's own outputs; the
> philosophical framing is reduced to two sentences whose sources are read correctly.

Numbers tagged **[real]** are from `data/real/runs.csv`; **[sim]** from `sim/results/` (synthetic
world, matched operating points, held-out seeds; absolute values do not transfer, orderings and
sensitivities are the deliverable within the swept assumptions — `sim/README.md`).

---

## 0. Framing — two sentences, used as description, not justification

The measurement follows a subtractive logic. The *Daodejing* (ch. 48) distinguishes learning, which
adds daily (為學日益), from the Way, which subtracts daily (為道日損 — 損之又損, "subtract, and
subtract again"); the information ladder is that procedure applied to a catalogue record: from the
full entry we remove, rung by rung, the title, the holder, the creator, and finally every word about
people and places, until only the physical object remains, measuring at each subtraction what the
model can still do. The system's output follows the *Analects*' rule for speaking under uncertainty
(2.17–18): say "I do not know" where you do not know, and set the doubtful aside (闕疑) rather than
speak about it — the agent returns an accepted set with calibrated confidence, a deferred set routed
to the curator with its evidence, and nothing else.

Everything below is motivated and evaluated on cost and accuracy alone. (v1 attached six further
traditions to mechanisms that exist for ordinary engineering reasons; the sinology review found two
misattributions — 無為而治 is *Analects* 15.5, not Laozi, and 大道至簡 is a modern slogan — and
recommended the cut. The mechanisms those labels decorated survive on their own merits or not at all.)

## 1. Two deliverables that must not be mixed

**(A) The measurement** — the paper's claim. A *fixed-rung* reference system is run at every rung of a
nested ladder on the test split; accuracy per rung, stratified by memorisation, with ensemble-level
CIs, is the result. Nothing about the system's own confidence may decide which rung a decision is
made at, or rung accuracy stops being an experimental manipulation (red-team AC, B.2).

**(B) The system** — the engineering deliverable. A frugal pipeline is evaluated end-to-end on its own
quality–cost point. It may use any rung internally; its internals are reported as cost and as a
"non-action rate", never pooled into (A).

v1's "evidence escalation" (screen at L5, escalate to L1) blurred A and B and, under the v1 memory
model, inverted its own story (memorised queries were the ones settled "from physical facts"). It is
retained below only as a system-side option, with the honest [sim] result.

## 2. The measurement (deliverable A)

### 2.1 Nested ladder with a monotonicity assertion
Rungs L1 ⊃ L2 (−title) ⊃ L3 (−holder, accession, credit line, image-URL host) ⊃ L4 (−creator /
workshop / Notname) ⊃ L5 (physical facts: dimensions, support, medium, technique, date band,
iconography keywords) ⊃ L5-P (dimensions permuted) ⊃ L6 (image only + dimensions). The harness
asserts `tokens(L_{k+1}) < tokens(L_k)` **per prompt**; today's L2-T (+357 tokens vs L1 **[real]**)
would fail it, which is the point. Field table = `docs/05` §2.2; the image-URL filename and the
iconography keywords are named there because both can carry the ensemble's name.

### 2.2 Which kind of memory? — the word-keyed vs record-keyed test
Memory of a reunion may be keyed to *words* (title, creator, holder) or to the *record as a whole*
(dates, dimensions, medium). The two hypotheses predict different ladders: **[sim]** under
record-keyed memory the memorised stratum stays flat to L6 (Fig. S5b); under word-keyed memory it
collapses at L5 (Fig. S5c), so that L5/L6 are *clean* even for famous objects. One cheap real
experiment separates them: an E8 forced-choice arm whose only evidence is the L5 physical facts
(≈ $2.4 on GPT-5.4, 600 calls **[real price class]**). If word-keyed, the nested L5 is the paper's
evidence rung; if record-keyed, every rung needs the stratification of §2.3.

### 2.3 Stratify, do not back out
Observed accuracy per rung is reported on three strata — closed-book-solved (E5 on **test**),
forced-choice-solved, neither — and by fame tercile (`commons_views`, `nga_views`). The mixture
formula (`eval_toolkit.unmix`) is reported only as a sensitivity analysis with the probe's
chance-level false-positive rate (25 % for "both orders correct" at chance) propagated, because with
a noisy probe the equation has more unknowns than it has data (red-team AC, B.6).

### 2.4 Counterfactuals that measure *dependence*, not availability
`--mask-creator` withholds a field; a **field-swap** (`--swap-creator <seed>`, `--swap-title`) puts a
period-matched *wrong* value in and measures the flip rate — the share of decisions that follow the
word against the physical evidence. One dev run per rung ≈ $0.33 on GPT-4.1-mini **[real rate]**.
Likewise L5-P (dimension permutation) is the existing dependence test for the physical channel.

### 2.5 Canaries
Each run injects ~10 known members and ~10 perturbed-gold non-members per 80 queries so that the
pipeline's false-accept and false-reject rates are measured in-band (≈ $0.10 per dev run on the mini
**[real rate]**). Canaries also catch the duplicate-prompt and parse-failure classes the ledger's
`cache_hits` hint at (docs/03 B6b).

### 2.6 Statistics (frozen in `docs/05`)
Ensemble is the unit (B2); paired ensemble-bootstrap between rungs; McNemar on exact-set; Holm over
H1–H4; MDD on test ≈ 7–9 points, on dev 15–18 **[sim, S7]** — so dev is for tuning only. Report the
**no-LLM null** (retriever threshold alone) as the first row of every table: **[sim]** F1 0.40 at $0
in the base world, which several LLM configurations do not beat by much. Report pre- *and*
post-`e10_regate` numbers for every existing run; for new runs, prefer *dropping* the post-hoc rule
to freezing it — **[sim, S10]** the forking-paths optimism of a best-of-k rule is modest (≤ 1.8 F1 /
≤ 3.2 exact-set points at n = 80, k = 20), so the issue is disclosure, not magnitude, and disclosure is
simplest when there is nothing to disclose. One shuffled-order replicate per headline cell
(**[sim, S11]**: an ordered list can flatter a primacy-biased selector by ~13 F1 points).

### 2.7 Pre-registration after exposure
L1 / L2-T / L3-H / L5 test runs already exist for 2–4 models, so the pre-registration (`docs/05`)
must list the comparisons already seen, give a value for every tunable (K, prune threshold, abstention
margin, memorised criterion, fame cut-points, clustering rule), and register MDDs and equivalence
margins rather than a direction — the ladder is publishable either way. A **stopping rule for the
experiment itself** (one seed per cell; add a seed only while the paired CI straddles the MDD) replaces
the v1 habit of multiplying rungs mid-campaign.

## 3. The system (deliverable B) — what the matched-operating-point simulation says

All v1 orderings were artefacts of comparing policies at a fixed posterior threshold of 0.5 under a
5.8 % prior (different operating points). With each policy at its own F1-optimal threshold, chosen on
selection seeds and evaluated on held-out seeds (`sim/results/RUNLOG.md`), the **base world** —
retriever errors independent of the LLM's (ρ = 0), record-keyed memory — gives:

| policy (flagship class unless stated) | L1 F1 | L1 ¢/query | L5 F1 | L5 ¢/query |
| --- | ---: | ---: | ---: | ---: |
| today: listwise K=30 | 0.67 | 1.99 | 0.48 | 1.33 |
| **listwise K=30 + retriever prior** (same prompt, same cost) | **0.76** | 1.99 | **0.63** | 1.33 |
| listwise K=10 + retriever prior | 0.75 | 0.94 | 0.63 | 0.71 |
| retriever-prune p≥0.02 + retriever prior | 0.77 | 1.24 | 0.64 | 0.88 |
| listwise K=10 | 0.73 | 0.94 | 0.56 | 0.71 |
| retriever-prune p≥0.02 | 0.73 | 1.24 | 0.54 | 0.88 |
| cascade mini→flagship band 0.4 | 0.68 | 1.03 | 0.43 | 0.79 |
| cascade reject-only | 0.71 | 1.21 | 0.48 | 1.01 |
| evidence-cascade L5→L1 (reject-only) | 0.66 | 1.28 | — | — |
| pointwise ×30 | 0.73 | 6.66 | 0.51 | 5.37 |
| self-consistency n=5 | 0.76 | 9.96 | 0.49 | 6.63 |
| mini: listwise K=10 + retriever prior | 0.64 | 0.19 | 0.53 | 0.14 |
| no LLM: retriever score alone | 0.39 | 0 | 0.39 | 0 |

Two decimals on purpose: re-running with a different random stream moves most cells by ≤ 0.01 and
the L5 pointwise / self-consistency cells by up to 0.05 (their tuned thresholds are unstable), so
the third decimal is noise. Costs are exact given the token model.

### M1 — fuse the retriever score into the decision (zero extra cost; the largest gain *if* the retriever's errors are not the LLM's) **[sim]**
Give the LLM's per-candidate P(member) a per-candidate prior from the calibrated retriever score
instead of a flat prevalence prior. Base world: +0.09 F1 at L1 and +0.16 at L5 for the flagship at
identical cost; the *mini* with the prior (0.63) nearly matches today's flagship (0.67) at a fifth of
the price; the gain holds on the non-memorised stratum (0.58 → 0.70 at L1). **But the gain is a bet on
error independence:** when the retriever's noise is the same item difficulty the LLM sees (ρ = 0.5),
the L1 gain vanishes; at ρ = 0.8 it turns negative unless the retriever is strong (Fig. S8b). A lexical
or embedding retriever over the *same* metadata the LLM reads is probably ρ > 0; an image-embedding or
provenance-graph retriever is probably ρ ≈ 0 — which argues for making the first stage *complementary*
to the LLM's evidence rather than a cheaper version of it. Real-world requirements: a per-candidate
score from the LLM (first-token P(yes) where the relay passes logprobs — documented for GPT-4.1-mini
**[real]** — or a verbalised 0–100 score, ≈ +120 completion tokens per call) and a retriever score
calibrated on dev; the test is a $0 offline fit on logged scores (`docs/06` Node 1).

### M2 — read less **[sim]**
K = 10 (47 % of cost) or retriever-prune at p ≥ 0.02 (62–66 %) are *better* than K = 30 at matched
thresholds whenever list dilution β > 0, and lose < 0.01 when β = 0 and the retriever is well
calibrated; a badly calibrated retriever makes them lose (Fig. S8b). The $1 real experiment that
measures β — `--k 10` vs `--k 30` on the same dev queries — is Node 1 of `docs/06`.

### M3 — a second model only in one corner (demoted from v1)
Under matched operating points no cascade or routing policy beats the single-model M1/M2 policies at
equal cost in the base world (cascade band 0.4: 0.68 @ 1.03¢ vs K=10 0.73 @ 0.94¢), and routing
escalates 78–94 % of queries once the margin is measured on candidates in play. In the sweep the
*reject-only* cascade (mini screens, flagship judges survivors) is the best choice at budget only where
ρ > 0 **and** β > 0 — correlated errors make the prior fusion useless and dilution makes a cheap screen
worth having (Fig. S8c). And in the ρ > 0, β = 0 corner (15 % of L1 worlds) **today's design is already
the best policy at its budget**. So: measure ρ (fusion test) and β (`--k 10`) first; the second model
is the answer only if the first comes back null and the second positive.

### M4 — thinking tax and output economy **[real]**
GPT-5.4-mini at `reasoning_effort=low` spends 60–78 % of its cost on hidden reasoning that *grows* as
evidence shrinks (475 → 694 tokens/query from L1 to L5); expose the effort knob and plot accuracy per
dollar, or use the non-thinking mini. Ids-only JSON output saves ≈ 8 % on the flagships (completion
priced 4–6× prompt) — unless M1 needs a verbalised score, in which case the score *is* the output.

### M5 — three-way output with an elicited loss ratio
Accepted (calibrated confidence) / **deferred to the curator with the evidence dossier** / rejected.
Elicit λ = cost(false reunion) / cost(missed reunion) from 2–3 curators (R06); derive the acceptance
threshold and the deferral band from λ by the Bayes rule instead of tuning them — one elicited number
replaces three hyper-parameters. **[sim]** refusing the ~20 % least-confident queries lifts precision
0.87 → 0.92 at zero extra calls (Fig. S6; threshold-0.5 regime).

### M6 — grounded verification, diagnostic version
A second call cites the shown fields supporting each accepted member; a checker verifies literal
presence. Run it **under L5-P**: an accept that cites the (permuted, hence wrong) dimensions and still
finds the true partner is memory caught in the act. Under L1 the leak rate is zero by construction and
the metric measures compliance only (red-team AC, B.5). ≈ $0.001–0.005 per predicted member **[real rates]**.

### M7 — ensemble closure needs a clustering rule, not transitive closure **[sim, S9]**
At a ~2 % pairwise false-positive rate, naive closure over a dense candidate universe collapses into
giant components (B³ F1 0.27, ARI 0.01); with a realistic distractor pool 7.5 % of explicit "no"
decisions are still overturned. Use correlation clustering (or at least degree-capped closure) and
report the contradiction rate.

### System price, from the simulation's own outputs
Recommended v2 reference = flagship, K = 10 or prune, + retriever prior: **≈ 0.94–1.24 ¢/query**
versus 1.99 ¢ today (−38 … −53 %) **[sim cost, real token prices]**, with F1 +0.08 … +0.10 in the base world **[sim]**.
Cheap variant = mini, K = 10, + retriever prior: ≈ 0.19 ¢ (−90 %) at F1 ≈ today's (0.64 vs 0.67). v1's
"$0.0075–0.0115, quality higher in 87–95 % of worlds" is withdrawn: the price assumed a 40 % escalation
fraction the simulation never produced, and the percentage was an oracle statistic.

## 4. What transfers, honestly
Not the F1 values. Not even the orderings, unless the real system has (i) a per-candidate score,
(ii) a calibrated retriever whose errors are measurably independent of the LLM's, (iii) a measured β.
What transfers is the decision table (`sim/README.md`): fusion test on dev ($0) → `--k 10` vs `--k 30`
($1) → if both null, keep today's design and spend on the measurement; plus one striking null to check
first — in half of the swept worlds the retriever score alone beats the flagship at L5. The measurement
protocol of §2 does not depend on the simulation at all.

## 5. Known defects of v2 (so the next reviewer does not have to find them)
- The retriever prior's gain assumes the retriever score is informative *given* the LLM's evidence;
  if the LLM already saw everything the retriever saw, the gain shrinks. The real test is M1 on dev.
- Memory is still a two-parameter toy (share, sharpness) with a binary keying switch; real memory is
  graded by fame and by field. The fame-tercile stratification is the empirical substitute.
- Costs are relay prices (≈ 4.4× list **[real]**); ratios transfer, dollars do not.
- The simulation has no images, no open pool, no abstention under tuned thresholds, no clustering
  stage; S9 only quantifies why the last is needed.
- Nothing here fixes ground truth; the confidence tiers of `docs/05` §2.1 and a 100-decision expert
  audit (time, not API spend) are the remedy.
