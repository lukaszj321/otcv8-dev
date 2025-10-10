#!/usr/bin/env bash
set -euo pipefail
if [ -d "data" ]; then
  mkdir -p docs/_static/data
  rsync -a --delete data/ docs/_static/data/
fi
python -m pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
echo "HTML → docs/_build/html"

# JSON build currently has issues with PyData theme
# Attempting JSON build (non-fatal)
echo "Attempting JSON build for RAG..."
sphinx-build -b json docs docs/_build/json || {
  echo "WARNING: JSON build failed (known issue with PyData theme)"
  echo "HTML documentation is still available"
}
echo "JSON → docs/_build/json (if successful)"
