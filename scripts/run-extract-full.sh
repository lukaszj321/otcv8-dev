#!/usr/bin/env bash
# Orchestrator: prepares env, generates compile_commands.json, runs local-extract.sh
# and performs simple validation/reporting including optional regression check.
#
# Usage:
#   ./scripts/run-extract-full.sh [--install-deps] [--skip-libclang] [--no-venv] [--regression-threshold <percent>]
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

INSTALL_DEPS=false
SKIP_LIBCLANG=false
SKIP_NODE=false
USE_VENV=true
PYTHON=python3
REGRESSION_THRESHOLD=0  # percentage, 0 -> disabled

while [[ $# -gt 0 ]]; do
  case "$1" in
    --install-deps) INSTALL_DEPS=true; shift ;;
    --skip-libclang) SKIP_LIBCLANG=true; shift ;;
    --skip-node) SKIP_NODE=true; shift ;;
    --no-venv) USE_VENV=false; shift ;;
    --python) PYTHON="$2"; shift 2 ;;
    --regression-threshold) REGRESSION_THRESHOLD="$2"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

mkdir -p tmp
REPORT=tmp/extract_report.txt
echo "Run started: $(date -u)" > "$REPORT"

echo "Preflight: checking tools..." | tee -a "$REPORT"
command -v cmake >/dev/null 2>&1 && echo "cmake: $(cmake --version | head -n1)" | tee -a "$REPORT" || echo "cmake: MISSING" | tee -a "$REPORT"
command -v node >/dev/null 2>&1 && echo "node: $(node --version)" | tee -a "$REPORT" || echo "node: MISSING" | tee -a "$REPORT"
command -v "$PYTHON" >/dev/null 2>&1 && echo "python: $($PYTHON --version 2>&1)" | tee -a "$REPORT" || echo "python: MISSING" | tee -a "$REPORT"
command -v jq >/dev/null 2>&1 || echo "jq: MISSING (optional)" | tee -a "$REPORT"
command -v git >/dev/null 2>&1 || echo "git: MISSING (optional)" | tee -a "$REPORT"

# optional venv and pip deps for libclang
if [ "$USE_VENV" = true ] && [ "$SKIP_LIBCLANG" = false ]; then
  echo "Setting up Python venv" | tee -a "$REPORT"
  if ! command -v "$PYTHON" >/dev/null 2>&1; then
    echo "Python not found; cannot setup venv; libclang step will be skipped" | tee -a "$REPORT"
    SKIP_LIBCLANG=true
  else
    python_venv_dir="$ROOT_DIR/.venv-extract"
    if [ ! -d "$python_venv_dir" ]; then
      "$PYTHON" -m venv "$python_venv_dir"
    fi
    # shellcheck disable=SC1090
    source "$python_venv_dir/bin/activate"
    pip install --upgrade pip >/dev/null 2>&1 || true
    pip install clang >/dev/null 2>&1 || {
      echo "pip install clang failed; libclang extraction may not work" | tee -a "$REPORT"
    }
    echo "Activated venv: $python_venv_dir" | tee -a "$REPORT"
  fi
fi

# optional npm install for tree-sitter
if [ "$INSTALL_DEPS" = true ]; then
  echo "Installing npm deps (tree-sitter)..." | tee -a "$REPORT"
  npm install --no-audit --no-fund tree-sitter tree-sitter-cpp tree-sitter-lua tree-sitter-java || {
    echo "npm install (tree-sitter) failed; continuing" | tee -a "$REPORT"
  }
fi

# 1) generate compile_commands.json (only needed for libclang)
if [ "$SKIP_LIBCLANG" = false ]; then
  echo "Generating compile_commands.json..." | tee -a "$REPORT"
  if ./scripts/generate-compile-commands.sh build >> tmp/generate-compile-commands.log 2>&1; then
    echo "compile_commands.json generation: OK" | tee -a "$REPORT"
  else
    echo "compile_commands.json generation: FAILED (see tmp/generate-compile-commands.log)" | tee -a "$REPORT"
    echo "Skipping libclang extraction." | tee -a "$REPORT"
    SKIP_LIBCLANG=true
  fi
else
  echo "Skipping compile_commands generation (libclang skipped)" | tee -a "$REPORT"
fi

# 2) run local-extract.sh with selected flags
EXTRACT_FLAGS=()
$INSTALL_DEPS && EXTRACT_FLAGS+=("--install-deps")
$SKIP_LIBCLANG && EXTRACT_FLAGS+=("--no-libclang")

if [ "$SKIP_NODE" = true ] && [ "$SKIP_LIBCLANG" = true ]; then
  echo "Both node and libclang extraction skipped; nothing to run." | tee -a "$REPORT"
  echo "Aborting." | tee -a "$REPORT"
  exit 1
fi

echo "Running local-extract.sh with flags: ${EXTRACT_FLAGS[*]}" | tee -a "$REPORT"
if ./scripts/local-extract.sh "${EXTRACT_FLAGS[@]}" 2>&1 | tee tmp/local-extract.log; then
  echo "local-extract.sh: finished (check tmp/extract-api.log and tmp/clang_entities.json)" | tee -a "$REPORT"
else
  echo "local-extract.sh: finished with errors; check tmp/local-extract.log" | tee -a "$REPORT"
fi

# 3) simple validation: compare counts to manifest if present
echo "Validation:" | tee -a "$REPORT"
if [ -f docs/_data/_api_manifest.json ] && command -v jq >/dev/null 2>&1; then
  echo "Manifest counts (raw):" | tee -a "$REPORT"
  jq '.counts' docs/_data/_api_manifest.json | tee -a "$REPORT"
else
  echo "Manifest not present or jq missing; skipping manifest checks" | tee -a "$REPORT"
fi

# Regression check: compare new count vs committed baseline docs/_data/_api_entities.json (if present)
if [ "$REGRESSION_THRESHOLD" != "0" ]; then
  echo "Regression check enabled (threshold=${REGRESSION_THRESHOLD}%)" | tee -a "$REPORT"
  if ! command -v jq >/dev/null 2>&1; then
    echo "jq required for regression check but is missing; skipping regression check" | tee -a "$REPORT"
  else
    # baseline: committed file if present
    if [ -f docs/_data/_api_entities.json ]; then
      baseline_count=$(jq 'length' docs/_data/_api_entities.json)
    else
      baseline_count=0
    fi

    # new: prefer tmp/clang_entities.json, fallback to docs/_data/_api_entities.json generated earlier
    if [ -f tmp/clang_entities.json ]; then
      # try to count entities array, fallback to 0
      new_count=$(jq '.entities | length // 0' tmp/clang_entities.json)
    elif [ -f docs/_data/_api_entities.json ]; then
      new_count=$(jq 'length' docs/_data/_api_entities.json)
    else
      new_count=0
    fi

    echo "Baseline count: $baseline_count" | tee -a "$REPORT"
    echo "New count: $new_count" | tee -a "$REPORT"

    # compute absolute delta and percent (guard division by zero)
    delta=$(( new_count - baseline_count ))
    abs_delta=${delta#-}
    pct=0
    if [ "$baseline_count" -gt 0 ]; then
      pct=$(awk "BEGIN {printf \"%.0f\", ($abs_delta / $baseline_count) * 100}")
    else
      pct=$abs_delta
    fi

    echo "Absolute delta: $abs_delta" | tee -a "$REPORT"
    echo "Percent delta: ${pct}%" | tee -a "$REPORT"

    # fail if percent delta > threshold
    if [ "$pct" -gt "$REGRESSION_THRESHOLD" ]; then
      echo "REGRESSION: delta ${pct}% exceeds threshold ${REGRESSION_THRESHOLD}% - failing run" | tee -a "$REPORT"
      echo "Run artifacts available in tmp/" | tee -a "$REPORT"
      exit 2
    else
      echo "Regression check passed (delta ${pct}% <= ${REGRESSION_THRESHOLD}%)" | tee -a "$REPORT"
    fi
  fi
else
  echo "Regression check disabled (REGRESSION_THRESHOLD=0)" | tee -a "$REPORT"
fi

if [ -f tmp/clang_entities.json ] && command -v jq >/dev/null 2>&1; then
  ent_count=$(jq '.entities | length // 0' tmp/clang_entities.json)
  echo "Libclang entities: $ent_count" | tee -a "$REPORT"
else
  echo "No tmp/clang_entities.json or jq missing; skip libclang count" | tee -a "$REPORT"
fi

if [ -f docs/_data/_api_entities.json ] && command -v jq >/dev/null 2>&1; then
  final_count=$(jq 'length' docs/_data/_api_entities.json)
  echo "Final api_entities.json count: $final_count" | tee -a "$REPORT"
fi

echo "Report saved to $REPORT"
echo "Run finished: $(date -u)" >> "$REPORT"

# Generate markdown summary for easy reading
SUMMARY=tmp/full-extract-summary.md
echo "# Full Extract Summary" > "$SUMMARY"
echo "" >> "$SUMMARY"
echo "**Run Date:** $(date -u)" >> "$SUMMARY"
echo "" >> "$SUMMARY"

echo "## Environment" >> "$SUMMARY"
echo "" >> "$SUMMARY"
echo "- **CMake:** $(command -v cmake >/dev/null 2>&1 && cmake --version | head -n1 || echo 'NOT FOUND')" >> "$SUMMARY"
echo "- **Node:** $(command -v node >/dev/null 2>&1 && node --version || echo 'NOT FOUND')" >> "$SUMMARY"
echo "- **Python:** $(command -v "$PYTHON" >/dev/null 2>&1 && "$PYTHON" --version 2>&1 || echo 'NOT FOUND')" >> "$SUMMARY"
echo "- **jq:** $(command -v jq >/dev/null 2>&1 && echo "$(jq --version 2>&1)" || echo 'NOT FOUND')" >> "$SUMMARY"
echo "" >> "$SUMMARY"

echo "## Extraction Results" >> "$SUMMARY"
echo "" >> "$SUMMARY"

if [ -f tmp/clang_entities.json ] && command -v jq >/dev/null 2>&1; then
  ent_count=$(jq '.entities | length // 0' tmp/clang_entities.json)
  echo "- **Libclang entities:** $ent_count" >> "$SUMMARY"
else
  echo "- **Libclang entities:** N/A (file not found or jq missing)" >> "$SUMMARY"
fi

if [ -f docs/_data/_api_entities.json ] && command -v jq >/dev/null 2>&1; then
  final_count=$(jq 'length' docs/_data/_api_entities.json)
  echo "- **Final API entities:** $final_count" >> "$SUMMARY"
else
  echo "- **Final API entities:** N/A" >> "$SUMMARY"
fi
echo "" >> "$SUMMARY"

# Regression check results
if [ "$REGRESSION_THRESHOLD" != "0" ]; then
  echo "## Regression Check" >> "$SUMMARY"
  echo "" >> "$SUMMARY"
  if command -v jq >/dev/null 2>&1; then
    if [ -f docs/_data/_api_entities.json ]; then
      baseline_count=$(jq 'length' docs/_data/_api_entities.json 2>/dev/null || echo 0)
    else
      baseline_count=0
    fi

    if [ -f tmp/clang_entities.json ]; then
      new_count=$(jq '.entities | length // 0' tmp/clang_entities.json)
    elif [ -f docs/_data/_api_entities.json ]; then
      new_count=$(jq 'length' docs/_data/_api_entities.json)
    else
      new_count=0
    fi

    delta=$(( new_count - baseline_count ))
    abs_delta=${delta#-}
    pct=0
    if [ "$baseline_count" -gt 0 ]; then
      pct=$(awk "BEGIN {printf \"%.0f\", ($abs_delta / $baseline_count) * 100}")
    else
      pct="N/A"
    fi

    echo "- **Baseline count:** $baseline_count" >> "$SUMMARY"
    echo "- **New count:** $new_count" >> "$SUMMARY"
    echo "- **Delta:** $delta" >> "$SUMMARY"
    if [ "$pct" = "N/A" ]; then
      echo "- **Percent change:** N/A (baseline is zero)" >> "$SUMMARY"
      echo "- **Threshold:** ${REGRESSION_THRESHOLD}%" >> "$SUMMARY"
      echo "- **Status:** ⚠️ SKIPPED (cannot compute percent change when baseline is zero)" >> "$SUMMARY"
    else
      echo "- **Percent change:** ${pct}%" >> "$SUMMARY"
      echo "- **Threshold:** ${REGRESSION_THRESHOLD}%" >> "$SUMMARY"
      if [ "$pct" -gt "$REGRESSION_THRESHOLD" ]; then
        echo "- **Status:** ❌ FAILED (delta ${pct}% exceeds threshold)" >> "$SUMMARY"
      else
        echo "- **Status:** ✅ PASSED" >> "$SUMMARY"
      fi
    fi
  else
    echo "- **Status:** SKIPPED (jq not available)" >> "$SUMMARY"
  fi
else
  echo "## Regression Check" >> "$SUMMARY"
  echo "" >> "$SUMMARY"
  echo "- **Status:** DISABLED (threshold=0)" >> "$SUMMARY"
fi
echo "" >> "$SUMMARY"

echo "## Artifacts" >> "$SUMMARY"
echo "" >> "$SUMMARY"
echo "The following files are available in the \`tmp/\` directory:" >> "$SUMMARY"
echo "" >> "$SUMMARY"
for artifact in extract_report.txt extract-api.log clang_entities.json local-extract.log generate-compile-commands.log; do
  if [ -f "tmp/$artifact" ]; then
    size=$(du -h "tmp/$artifact" | cut -f1)
    echo "- ✅ \`tmp/$artifact\` (${size})" >> "$SUMMARY"
  else
    echo "- ❌ \`tmp/$artifact\` (not found)" >> "$SUMMARY"
  fi
done
echo "" >> "$SUMMARY"

echo "## Next Steps" >> "$SUMMARY"
echo "" >> "$SUMMARY"
echo "1. Review the full report in \`tmp/extract_report.txt\`" >> "$SUMMARY"
echo "2. Check for errors in \`tmp/extract-api.log\`" >> "$SUMMARY"
if [ "$REGRESSION_THRESHOLD" != "0" ] && command -v jq >/dev/null 2>&1; then
  if [ -f tmp/clang_entities.json ]; then
    new_count=$(jq '.entities | length // 0' tmp/clang_entities.json)
    if [ -f docs/_data/_api_entities.json ]; then
      baseline_count=$(jq 'length' docs/_data/_api_entities.json 2>/dev/null || echo 0)
      delta=$(( new_count - baseline_count ))
      if [ "$delta" -ne 0 ]; then
        echo "3. **If API changes are intentional:** Update baseline with \`cp tmp/clang_entities.json docs/_data/_api_entities.json\`" >> "$SUMMARY"
        echo "4. **If changes are unintentional:** Review and fix the code, then re-run extraction" >> "$SUMMARY"
      else
        echo "3. No baseline update needed (counts match)" >> "$SUMMARY"
      fi
    fi
  fi
fi
echo "" >> "$SUMMARY"

echo "---" >> "$SUMMARY"
echo "" >> "$SUMMARY"
echo "*Generated by run-extract-full.sh*" >> "$SUMMARY"

echo "Summary saved to $SUMMARY"
