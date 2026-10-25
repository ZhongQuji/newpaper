#!/usr/bin/env bash
# Rebuild every derived artefact from the raw export. Idempotent; ~7 minutes (power analysis dominates).
#   bash tools/run_all.sh            # full
#   bash tools/run_all.sh --fast     # skip the 5-minute power analysis and the 1-minute sweep
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
FAST=0; [ "${1:-}" = "--fast" ] && FAST=1
python3 -c "import matplotlib, numpy, pandas, scipy" 2>/dev/null || pip install --quiet --user -r requirements.txt

echo "[1/5] extract real ledger";          python3 tools/extract_real_runs.py > /dev/null
echo "[2/5] figures from real ledger";     python3 tools/plot_real_ledger.py > /dev/null 2>&1
echo "[3/5] paper schematics";             python3 tools/plot_paper_schematics.py > /dev/null 2>&1
if [ "$FAST" = 1 ]; then
  echo "[4/5] simulation (base only)";     python3 sim/reunion_sim.py > /dev/null 2>&1
  echo "[5/5] power analysis skipped (--fast)"
else
  echo "[4/5] simulation + sweep";         python3 sim/reunion_sim.py --sweep > /dev/null 2>&1
  echo "[5/5] power analysis";             python3 sim/power_analysis.py > /dev/null 2>&1
fi
echo "done. Outputs: data/real/, figures/{real,sim,paper}/, sim/results/"
