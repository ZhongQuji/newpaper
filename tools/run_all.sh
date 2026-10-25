#!/usr/bin/env bash
# Rebuild every derived artefact from the raw export. Idempotent; ~12 minutes (sweep + power analysis dominate).
#   bash tools/run_all.sh            # full
#   bash tools/run_all.sh --fast     # skip the 5-minute power analysis and the 1-minute sweep
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
FAST=0; [ "${1:-}" = "--fast" ] && FAST=1
python3 -c "import matplotlib, numpy, pandas, scipy" 2>/dev/null || pip install --quiet --user -r requirements.txt

echo "[1/7] extract real ledger";          python3 tools/extract_real_runs.py > /dev/null
echo "[2/7] figures from real ledger";     python3 tools/plot_real_ledger.py > /dev/null 2>&1
echo "[3/7] paper schematics";             python3 tools/plot_paper_schematics.py > /dev/null 2>&1
echo "[4/7] evaluation toolkit self-test"; python3 tools/eval_toolkit.py --selftest | tail -1
if [ "$FAST" = 1 ]; then
  echo "[5/7] design-space simulation (base only)";  python3 sim/reunion_sim.py > /dev/null 2>&1
  echo "[6/7] measurement simulations";               python3 sim/measurement_sim.py > /dev/null 2>&1
  echo "[7/7] power analysis skipped (--fast)"
else
  echo "[5/7] design-space simulation + sweep";       python3 sim/reunion_sim.py --sweep > /dev/null 2>&1
  echo "[6/7] measurement simulations";               python3 sim/measurement_sim.py > /dev/null 2>&1
  echo "[7/7] power analysis";                        python3 sim/power_analysis.py > /dev/null 2>&1
fi
echo "done. Outputs: data/real/, figures/{real,sim,paper}/, sim/results/"
