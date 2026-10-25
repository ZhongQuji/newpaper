# Briefing for the simulated programme committee

You are reviewing a research project on **LLM / MLLM agents for the digital reunion of
dispersed cultural-heritage objects** (panels of dismembered altarpieces, leaves of broken-up
albums and manuscripts, fragments now held by different museums). Read, in this order:

1. `docs/01_project_reconstruction.md` — what the project is, its information-level ladder,
   its experiment grid (E5–E17), its leakage controls, and what is *unknown*.
2. `data/real/runs_summary.md` — real totals (calls, tokens, cost, wall time) per model.
3. `data/real/runs.csv` — the per-run ledger (65 runs). Columns `prompt_tok_per_call`,
   `completion_tok_per_call`, `cost_per_call_usd`, `sec_per_call` are derived from verbatim counts.

Hard facts you must respect:

- **No accuracy numbers exist in the material you have.** Do not invent any. Write your
  critique conditionally ("if the L1→L5 drop is < X, then …") and name the exact number or
  artefact the authors must show to resolve each concern.
- Cost/token/latency numbers in the ledger are real and may be quoted.
- Dev split = 80 queries, test split = 294 queries, shortlist K = 30. Levels: L1 (full record)
  → L2-T (title-leak subset, title withheld) → L3 → L3-H (holder scrubbed) → L5 (physical facts)
  → L5-P (dimensions permuted) → L6 (L5 minus title).
- Models with ledgers: GPT-4.1, GPT-4.1-mini, GPT-5.4, GPT-5.4-mini (thinking-class small model).
  Others were run in other sessions (Gemini 2.5/3, Claude 4.5/4.6, Qwen3.5, MiMo, Qwen3-VL-2B).

## Output contract (strict)

Write **one Markdown file per reviewer** at the path you are given. Each file has exactly
these sections, in this order, and is at most ~1,200 words:

```
# Reviewer <id> — <venue persona>
## Summary of the submission as I understand it            (≤ 5 sentences)
## Scores (1–10) with one-line justification each
- Novelty:
- Technical soundness:
- Evaluation rigour:
- Clarity (of the design, as reconstructed):
- Impact / significance:
- Overall:
## Strengths                                                 (3–5 bullets)
## Weaknesses                                                (numbered; each with a Severity tag: BLOCKER / MAJOR / MINOR)
## Experiments or artefacts that would change my score      (numbered, concrete, each with a one-line "what result would convince me")
## Token-efficiency / cost critique                          (what is wasteful, what is cheap-and-missing)
## One idea the authors have not tried                       (≤ 150 words, concrete enough to implement)
## Confidence (1–5) and what I could not assess
```

Rules: be specific, be adversarial but fair, cite the artefact (`runs.csv` row / level / flag)
you are reacting to, prefer numbered concrete requests over general advice, do not pad.
Do not edit any file other than the one(s) you were asked to write.
