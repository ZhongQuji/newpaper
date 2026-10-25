# Adapters: local run outputs → `tools/eval_toolkit.py` schema

The toolkit needs one row per (run, query, candidate) decision with these columns
(`run_id, query_id, query_ens, cand_id, cand_ens, pred` required; `score, pos, memorised, stratum`
optional). The export we worked from contains only the **names** of the per-run report files
(`reports/<date>_llm_reunion_agent_<level>_<model>.json`, `reports/<date>_e10_regate_<level>_<model>.json`,
`reports/<date>_e10_shortlist_controls_<run>.json`), not their contents, so the field mapping below
has to be completed on the machine that holds them.

## Template

```python
#!/usr/bin/env python3
"""adapt_e10.py — build decisions.csv from one or more E10 run directories."""
import json, sys, pathlib, pandas as pd

def rows_from_run(run_dir: pathlib.Path, run_id: str):
    # TODO 1: locate the per-query record file written by scripts/llm_reunion_agent.py
    #         (candidates shown, their order, the agent's selected ids, optional P(yes)/scores)
    # TODO 2: locate the gold membership (ensemble id per object id) — probably the dataset
    #         builder's output that `membership_evidence` / `wikidata_deep` reports summarise
    for rec in json.load(open(run_dir / "per_query.json")):          # TODO: real file name
        q = rec["query_id"]; q_ens = GOLD[q]
        for pos, cand in enumerate(rec["shortlist"]):               # TODO: preserve shown order
            yield dict(run_id=run_id, query_id=q, query_ens=q_ens,
                       cand_id=cand, cand_ens=GOLD.get(cand, f"unk:{cand}"),
                       pred=int(cand in rec["selected"]),
                       score=rec.get("scores", {}).get(cand),       # None if the run has no scores
                       pos=pos,
                       memorised=MEM.get(q),                        # from the E8 forced-choice probe, if run
                       stratum=FAME.get(q))                         # e.g. commons_views tercile

GOLD = {}   # object_id -> ensemble_id
MEM  = {}   # query_id  -> 0/1
FAME = {}   # query_id  -> "low" | "mid" | "high"
out = pd.DataFrame(r for run in sys.argv[1:] for r in rows_from_run(pathlib.Path(run), pathlib.Path(run).name))
out.to_csv("decisions.csv", index=False)
```

## Then

```bash
python3 tools/eval_toolkit.py --input decisions.csv --summary               # metrics + ensemble-bootstrap CIs per run
python3 tools/eval_toolkit.py --input decisions.csv --compare <L1 run> <L5 run>   # paired Δ with CI, McNemar
python3 tools/eval_toolkit.py --input decisions.csv --unmix <run>           # memorised / non-memorised strata
python3 tools/eval_toolkit.py --input decisions.csv --position-bias <run>   # FPR & recall by shortlist position
```

## Two things to check while writing the adapter

1. **Candidates with unknown gold.** If a shortlist contains objects that are not in the gold
   membership table, give them a unique pseudo-ensemble (`unk:<id>`) so they count as negatives;
   report how many there are.
2. **Pre- vs post-regate.** Build two `run_id`s per run (`…_raw`, `…_regate`) so the effect of
   `e10_regate.py` is a paired comparison, not a silent replacement (blocker B6).
