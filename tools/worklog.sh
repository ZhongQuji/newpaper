#!/usr/bin/env bash
# Append one timestamped entry to logs/worklog.md (Asia/Shanghai time).
# Usage: tools/worklog.sh <STATUS> <message>
#   STATUS in: START | DONE | NOTE | CHECK | FAIL | TODO
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="$ROOT/logs/worklog.md"
STATUS="${1:?status}"; shift
MSG="$*"
TS="$(TZ=Asia/Shanghai date '+%Y-%m-%d %H:%M:%S %Z')"
mkdir -p "$(dirname "$LOG")"
if [ ! -f "$LOG" ]; then
  printf '# Work log\n\nAll times are Asia/Shanghai (UTC+8). One line per unit of work.\n\n| time | status | entry |\n| --- | --- | --- |\n' > "$LOG"
fi
printf '| %s | %s | %s |\n' "$TS" "$STATUS" "$MSG" >> "$LOG"
echo "[$TS] $STATUS $MSG"
