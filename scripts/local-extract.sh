#!/usr/bin/env bash
# Local extraction wrapper:
#  - optionally installs tree-sitter packages (npm) if --install-deps passed
#  - generates compile_commands.json via CMake
#  - runs libclang extractor (python) to get precise C++ entities
#  - runs Node extractor
#
# Usage:
#   ./scripts/local-extract.sh [--install-deps] [--run-lua-bindgen] [--no-libclang]
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

INSTALL_DEPS=false
RUN_LUA_BINDGEN=false
USE_LIBCLANG=true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --install-deps) INSTALL_DEPS=true; shift ;;
    --run-lua-bindgen) RUN_LUA_BINDGEN=true; shift ;;
    --no-libclang) USE_LIBCLANG=false; shift ;;
    *) echo "Unknown arg: $1"; exit 1 ;;
  esac
done

# Optional npm install (tree-sitter) - can be heavy; skip unless requested
if [ "$INSTALL_DEPS" = true ]; then
  echo "Installing tree-sitter packages (npm)..."
  npm install --no-audit --no-fund tree-sitter tree-sitter-cpp tree-sitter-lua tree-sitter-java || {
    echo "npm install failed; continue but tree-sitter unavailable"
  }
fi

# 1) Generate compile_commands.json
echo "Generating compile_commands.json (CMake)..."
./scripts/generate-compile-commands.sh build

# 2) Collect headers list for libclang helper (avoid ARG_MAX by writing to tmp file)
echo "Collecting header files..."
HEADERS=()
for dir in src include modules data vc16; do
  if [ -d "$dir" ]; then
    while IFS= read -r header; do
      HEADERS+=("$header")
    done < <(find "$dir" -type f \( -iname '*.h' -o -iname '*.hpp' -o -iname '*.hxx' \) -print)
  fi
done
if [ ${#HEADERS[@]} -eq 0 ]; then
  echo "No headers found with default globs. Please adjust the find paths."
else
  echo "Found ${#HEADERS[@]} headers (sample): ${HEADERS[@]:0:5}"
fi

# 3) Run libclang helper (python)
if [ "$USE_LIBCLANG" = true ]; then
  echo "Running libclang helper..."
  PY=python3
  if ! command -v $PY >/dev/null 2>&1; then
    echo "Python3 not found in PATH. Install python3 and clang python bindings (pip install clang)."
    echo "Skipping libclang extraction."
  else
    # create tmp dir
    mkdir -p tmp
    # Write header list to file to avoid ARG_MAX issues
    printf '%s\n' "${HEADERS[@]}" > tmp/headers.txt
    # Ensure clang_extract script exists
    if [ ! -f tools/clang-extract/clang_extract.py ]; then
      echo "tools/clang-extract/clang_extract.py not found; skipping libclang extraction."
    elif [ ! -f compile_commands.json ]; then
      echo "compile_commands.json not found in repo root; abort libclang step."
    else
      if ! "$PY" tools/clang-extract/clang_extract.py compile_commands.json tmp/headers.txt > tmp/clang_entities.json; then
        echo "clang_extract.py failed (check python clang.cindex / libclang). See tmp/clang_entities.json (partial or empty)."
      else
        echo "libclang output -> tmp/clang_entities.json"
      fi
    fi
  fi
else
  echo "Skipping libclang helper (disabled)."
fi

# 4) Run Node extractor
echo "Running Node extractor (scripts/extract-api.mjs)..."
NODE_CMD=node
if ! command -v $NODE_CMD >/dev/null 2>&1; then
  echo "node not found in PATH; install Node.js v18+"
  exit 2
fi

EXTRACT_ARGS=()
if [ "$RUN_LUA_BINDGEN" = true ]; then EXTRACT_ARGS+=("--run-lua-bindgen"); fi
# NOTE: ensure scripts/extract-api.mjs supports --use-libclang; if not, remove this flag or update extractor.
EXTRACT_ARGS+=("--use-libclang")

# Run extractor and capture stdout/stderr to log
mkdir -p tmp
"$NODE_CMD" scripts/extract-api.mjs "${EXTRACT_ARGS[@]}" 2>&1 | tee tmp/extract-api.log || {
  echo "Node extractor failed; see tmp/extract-api.log"
}
echo "Extractor finished. Logs -> tmp/extract-api.log"

# 5) Quick sanity checks (counts)
echo "Running quick sanity checks..."
if ! command -v jq >/dev/null 2>&1; then
  echo "jq not found; skipping JSON sanity checks. Install jq for better output (apt/brew install jq)."
else
  if [ -f docs/_data/_api_manifest.json ]; then
    echo "Manifest exists: docs/_data/_api_manifest.json"
    jq '.counts' docs/_data/_api_manifest.json || true
  fi
  if [ -f tmp/clang_entities.json ]; then
    echo "Libclang entities count: $(jq '.entities | length' tmp/clang_entities.json || echo '?')"
  fi
  if [ -f docs/_data/_api_entities.json ]; then
    echo "All entities (final) count: $(jq 'length' docs/_data/_api_entities.json || echo '?')"
  fi
fi

echo "Done. Inspect docs/ and tmp/ for outputs. Use CSV datasets in docs/authoring/datasets/ to validate content samples."
