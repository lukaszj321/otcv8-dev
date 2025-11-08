#!/usr/bin/env bash
# Orchestrator: prepares env, generates compile_commands.json, runs local-extract.sh
# and performs simple validation/reporting.
#
# Usage:
#   ./scripts/run-extract-full.sh [--install-deps] [--skip-libclang] [--skip-node] [--no-venv]
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

INSTALL_DEPS=false
SKIP_LIBCLANG=false
SKIP_NODE=false
USE_VENV=true
PYTHON=python3

while [[ $# -gt 0 ]]; do
  case "$1" in
    --install-deps) INSTALL_DEPS=true; shift ;;
    --skip-libclang) SKIP_LIBCLANG=true; shift ;;
    --skip-node) SKIP_NODE=true; shift ;;
    --no-venv) USE_VENV=false; shift ;;
    --python) PYTHON="$2"; shift 2 ;;
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
command -v jq >/dev/null 2>&1 || echo "jq: MISSING (optional, used for JSON checks)" | tee -a "$REPORT"
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
$SKIP_LIBCLANG || EXTRACT_FLAGS+=("--use-libclang")
$SKIP_LIBCLANG && EXTRACT_FLAGS+=("--no-libclang")
$SKIP_NODE || true

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
  echo "Manifest counts:" | tee -a "$REPORT"
  jq '.counts' docs/_data/_api_manifest.json | tee -a "$REPORT"
else
  echo "Manifest not present or jq missing; skipping manifest checks" | tee -a "$REPORT"
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
