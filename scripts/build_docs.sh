#!/usr/bin/env bash
set -euo pipefail
if [ -d "data" ]; then
  mkdir -p docs/_static/data
  rsync -a --delete data/ docs/_static/data/
fi
python -m pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
sphinx-build -b json docs docs/_build/json
echo "HTML → docs/_build/html"
echo "JSON → docs/_build/json"
