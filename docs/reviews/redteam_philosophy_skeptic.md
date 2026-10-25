# Red-team review — philosophy of science / sinology

Scope: the principle → mechanism mappings in `docs/04_method_redesign.md` §2 — (a) is the source read accurately, (b) does the mechanism follow or is the principle a label, (c) what the text actually suggests, (d) what a referee who knows the texts will do.

Verdict first: the engineering in M1–M16 is mostly sound and mostly standard; the philosophy was attached afterwards. The tell is structural — one idea, *thresholded escalation*, wears three banners (M4 as 無為, M12 as Marx, M14 as value of information; §2.8 says M14 "is M4 generalised"). A principle that yields the same mechanism as two others is a caption, not a premise.

## 1. 大道至簡 → M1–M3 (evidence-minimal prompts, ids-only output, thinking tax)

(a) Not a classical text. 大道至簡 is a modern slogan of management prose; it is in neither the Daodejing nor the Zhuangzi. The nearest canonical sources are the Yijing *Xici* (易簡而天下之理得矣) and Daodejing ch. 48: 為學日益，為道日損。損之又損，以至於無為. Ch. 48's 損 is a discipline of *unlearning* — shedding knowledge and desire to reach 無為 — not Occam's razor.
(b) M1–M3 follow from the fitted relay prices (completion 4–6× prompt) and the token fingerprint, not from Laozi.
(c) Ch. 48 does describe something the authors have and do not name: the *ladder* is 損之又損 — subtract a field, measure, subtract again. Make it operational: a nested schema with a monotonicity assertion in the harness (`tokens(L_k+1) < tokens(L_k)` per prompt), which L2-T (+357 tokens) violates.
(d) Cut the slogan. Cite ch. 48 once, for the ladder, never for prompt compression.

## 2. 無為而治 → M4, M4′, M5 (cascade, retriever prune, evidence escalation)

(a) Misattributed. 無為而治 is Confucius on Shun, *Analects* 15.5: 無為而治者，其舜也與？夫何為哉？恭己正南面而已矣. The Daodejing has 無為 (ch. 37 道常無為而無不為; ch. 57 我無為而民自化; ch. 3 為無為，則無不治) but never 無為而治. Worse, Laozi's 無為 rejects purposive intervention as such (ch. 29, 64: 為者敗之，執者失之); it is not a triage rule.
(b) A cascade that detects uncertainty and escalates to a flagship is paradigmatically 有為. It is Viola–Jones (2001) and FrugalGPT (Chen, Zaharia, Zou 2023); cite those.
(c) The text does suggest a mechanism, and it is not M4. Ch. 57: 法令滋彰，盜賊多有 — the more edicts, the more thieves. Every added control (holder scrub, title substitution, `e10_regate`) opens a new leak path — R03's finding. The 無為 mechanism is the **no-intervention null**: (i) a zero-LLM-call policy (retriever threshold only) as the row every mechanism must beat at equal cost; (ii) the **non-action rate** — queries decided with no LLM call — as a first-class number; (iii) *drop* `e10_regate` rather than freeze it. M15's "do not tune" is the 無為 move; the cascade is not.
(d) Cut. A referee who knows the *Analects* catches the attribution in one line and distrusts the rest.

## 3. 知止 → M6 (adaptive K)

(a) Ch. 44: 知足不辱，知止不殆 — a chapter on fame, goods and hoarding (甚愛必大費，多藏必厚亡). Ch. 32: 始制有名，名亦既有，夫亦將知止 — stop once names proliferate. Neither argues from diminishing marginal returns; both from the danger of excess.
(b) Adaptive K from a calibrated retriever tail is early-exit ranking (Cambazoglu et al., WSDM 2010) — engineering.
(c) Two honest readings. 多藏必厚亡 is a fair gloss on list dilution β (hoard 30 candidates, lose discrimination) *if* the $1 `--k 10` run shows β > 0; do not write it before then. Ch. 32's 知止 about *names* indicts the campaign: L2-T, L3-H, L3-H2, inV2, v1/v2 — rungs multiplied mid-campaign. The missed mechanism is a **stopping rule for the experiment itself**: a pre-registered rung set and a group-sequential plan on the test split (one seed; stop when the paired CI clears the MDD, else add a seed). 知止 for the authors.
(d) One sentence at most, conditional on β.

## 4. 禪 不立文字 / 初心 → M7, M8 (ladder reorder, visual rung)

(a) 教外別傳，不立文字，直指人心，見性成佛 is Song-dynasty Chan (祖庭事苑, 五燈會元), ascribed to Bodhidharma. The *Platform Sutra*'s own formula is 諸佛妙理，非關文字 (機緣品), and it explicitly rejects the crude reading used here: 執空之人有謗經，直言不用文字。既云不用文字，人亦不合語言……又云直道不立文字，即此不立兩字，亦是文字 (付囑品). What is pointed at is 人心／自性, not a physical object; a dimension field is 文字 exactly as a title is. 初心 as "beginner's mind" is Shunryu Suzuki (1970); in Chinese Buddhist usage it is 初發心, the first arousal of bodhicitta (華嚴經: 初發心時，便成正覺).
(b) M7 repairs construct validity (blocker B4); M8 is a standard vision baseline. Neither owes anything to Chan.
(c) 初心 does suggest a missing test: not *masking* the prior but *contradicting* it. A **field-swap counterfactual** — replace creator or title with a period-matched wrong value and measure the flip rate — measures reliance on words, not mere availability. `--mask-creator` withholds; `--swap-creator <seed>` would measure dependence (one dev run per rung, ≈$0.33 on the mini).
(d) Cut both. A sinologist referee will quote the 付囑品 back at you.

## 5. 1 Thess 5:21 → M9, M10

(a) πάντα δὲ δοκιμάζετε, τὸ καλὸν κατέχετε. δοκιμάζω is the assayer's verb — test a metal for genuineness; the context (5:19–22) is testing *prophecies* in the assembly.
(b) Reading the agent's claim as an utterance to be assayed before it is held is honest and close to the text; M9 follows. M10 (mixture un-mixing) does not, and 5:22 ἀπέχεσθε → "abstain" (M11) is a pun.
(c) An assayer tests against a standard. Missed mechanism: **canaries** — known members and known non-members (perturbed gold records) injected into each run, so the verifier's own false-accept and false-reject rates are measured in-band (`--canaries 10`, ≈$0.10 per dev run on the mini).
(d) Could survive as an epigraph to the verification section; nothing more.

## 6. 知之為知之，不知為不知 → M11

(a) *Analects* 2.17, accurately read. The better verse is 2.18: 多聞闕疑，慎言其餘，則寡尤 — hear much, set aside the doubtful (闕疑), speak cautiously of the rest, and you will err little. Selective prediction, c. 500 BCE.
(b) M11 is Chow (1957) and Geifman & El-Yaniv (2017); the risk–coverage curve follows from a loss function, not from Confucius. But the mapping is faithful.
(c) 闕疑 means *set aside*, not *discard*. Output three sets — accepted (with calibrated confidence), **deferred to the curator with its evidence dossier**, rejected — and report deferral rate against error among the non-deferred.
(d) Survives as one sentence; over-familiar, so keep it short and cite 2.18.

## 7. 各盡所能、按需分配 → M12, M13

(a) Marx, *Critique of the Gotha Programme* (1875), Part I: the principle of the *higher phase*, after "all the springs of co-operative wealth flow more abundantly"; in the lower phase, Marx insists, equal right remains "bourgeois right", unequal for unequal persons. The slogan predates him (Louis Blanc 1839/1851; ultimately Acts 4:35).
(b) A budget-constrained routing rule is the scarcity case Marx says the principle does *not* govern; the mapping inverts the text. Routing is Pareto economics.
(c) The passage's real claim — equal treatment of unequal units is unequal — is blocker B2: per-query scoring over-weights large polyptychs. The ensemble-level metric is the fix; it needs no Marx.
(d) Cut. Political noise on top of a misreading.

## 8. Economics of information → M14

(a) Howard (1966), Raiffa & Schlaifer (1961): EVSI/EVPI. Decision theory, not philosophy.
(b) Follows exactly — given a loss function and a prior, and the paper has neither.
(c) Upstream mechanism: **elicit the loss ratio** λ = cost(false reunion)/cost(missed reunion) from curators (R06), then *derive* the cascade band (M4), the abstention threshold (M11) and the image/open-pool gate (M14) from λ by the Bayes rule. One elicited number replaces three tuned hyperparameters.
(d) Keep, as the paper's theoretical backbone, under its own name.

## Verdict table

| pairing | fate |
| --- | --- |
| 大道至簡 → M1–M3 | cut the slogan; ch. 48 once, for the ladder |
| 無為而治 → M4/M4′/M5 | cut (*Analects* 15.5, not Laozi; a cascade is 有為) |
| 知止 → M6 | one sentence, only if β > 0 is measured |
| 不立文字 / 初心 → M7/M8 | cut |
| 1 Thess 5:21 → M9 | epigraph at most |
| *Analects* 2.17 → M11 | one sentence; prefer 2.18 闕疑 |
| Marx → M12/M13 | cut |
| value of information → M14 | keep, as decision theory |

## Recommended one-paragraph framing

> Our measurement follows a subtractive logic. The *Daodejing* (ch. 48) distinguishes learning, which adds daily (為學日益), from the Way, which subtracts daily (為道日損) — 損之又損, "subtract, and subtract again". The information ladder is that procedure applied to a catalogue record: from the full entry we remove, rung by rung, the title, the holder, the creator, and finally every word about people and places, until only the physical object remains, and at each subtraction we measure what the model can still do. What survives the last subtraction is evidence; what vanished with the words was, at least in part, memory. The system's output follows the *Analects*' rule for speaking under uncertainty (2.17–18): say "I do not know" where you do not know, and set the doubtful aside (闕疑) rather than speak about it. Concretely, the agent returns an accepted set with calibrated confidence, a deferred set routed to the curator with its evidence, and nothing else. We use these two texts as descriptions of the design, not as its justification; every mechanism below is motivated and evaluated on cost and accuracy alone.

## Present purely on engineering grounds

M2, M3 (token economics); M4, M4′, M5 (cascades — Viola–Jones 2001, FrugalGPT 2023); M6 (early-exit ranking); M8 (vision baselines); M9 (attribution checking); M10 (mixture estimation); M12 (routing); M13 (stratified reporting); M14 (EVSI, Howard 1966); M15 (pre-registration); M16 (Pareto reporting). Only the ladder (M1/M7) and the three-way output (M11) carry the two framing sentences above.
