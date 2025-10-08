#!/usr/bin/env bash
set -euo pipefail

# keep-alive, żeby GH Actions nie ubił kroku za ciszę
( while true; do echo "[keep-alive] $(date -u +%H:%M:%S)"; sleep 30; done ) &
KEEPALIVE_PID=$!

# faktyczny build + timeout + pełny log do pliku
STATUS=0
set -o pipefail
timeout 15m mkdocs build --clean -v 2>&1 | tee build.log || STATUS=$?

# sprzątanie keep-alive
kill $KEEPALIVE_PID || true

# jeśli padło – pokaż ostatnie linie loga i wyjdź z kodem błędu
if [ "$STATUS" -ne 0 ]; then
  echo "::group::Last 200 lines of build.log"
  tail -n 200 build.log || true
  echo "::endgroup::"
  exit $STATUS
fi
