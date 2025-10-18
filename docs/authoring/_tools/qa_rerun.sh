#!/bin/bash
# QA Rerun Script for OTClient v8 Documentation
# Runs diagram fix, link-lint, and csv-sanity checks

set -e

echo "=== QA Rerun Started ==="
echo "Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo ""

# Change to repo root
cd "$(dirname "$0")/../../.."

# 1. Diagram Lint & Fix
echo "==> Running diagram lint & fix..."
python3 docs/authoring/_tools/diagram_lint_fix.py
echo ""

# 2. Link Lint (simple relative link checker)
echo "==> Running link lint..."
python3 - <<'PYLINT'
import re, os, csv
from pathlib import Path

OUT = Path('docs/authoring/qa/link_lint.csv')
OUT.parent.mkdir(parents=True, exist_ok=True)

results = []
for md in Path('docs/authoring').rglob('*.md'):
    txt = md.read_text(encoding='utf-8', errors='ignore')
    for m in re.finditer(r"\]\(([^)#]+)\)", txt):
        link = m.group(1)
        if link.startswith(('http', 'mailto', '#')):
            continue
        tgt = (md.parent / link).resolve()
        status = 'OK' if tgt.exists() else 'BROKEN'
        results.append([str(md.relative_to('docs/authoring')), status, link])

with OUT.open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['file', 'status', 'link'])
    w.writerows(results)

print(f"Link lint complete: {len(results)} links checked")
broken = sum(1 for r in results if r[1] == 'BROKEN')
print(f"  Broken links: {broken}")
PYLINT
echo ""

# 3. CSV Sanity
echo "==> Running CSV sanity check..."
python3 docs/authoring/_tools/csv_sanity.py \
  --in docs/authoring/datasets \
  --out docs/authoring/qa/dataset_sanity.csv || true
echo ""

# 4. Optional: Mermaid block sanity
echo "==> Running Mermaid block sanity check..."
python3 - <<'PYMERMAID'
import re, csv
from pathlib import Path

rows = []
for md in Path('docs/authoring').rglob('*.md'):
    txt = md.read_text(encoding='utf-8', errors='ignore')
    blocks = re.findall(r"```mermaid\n([\s\S]*?)\n```", txt)
    for i, block in enumerate(blocks):
        has_init = '%%{init:' in block
        bad_bt = '```' in block
        status = 'OK' if (has_init and not bad_bt) else 'FAIL'
        problem = []
        if not has_init:
            problem.append('missing init')
        if bad_bt:
            problem.append('stray backticks')
        rows.append([str(md.relative_to('docs/authoring')), i+1, status, '; '.join(problem) if problem else ''])

Path('docs/authoring/qa').mkdir(parents=True, exist_ok=True)
with open('docs/authoring/qa/mermaid_sanity.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['file', 'blockNo', 'status', 'problem'])
    w.writerows(rows)

print(f"Mermaid sanity complete: {len(rows)} blocks checked")
failed = sum(1 for r in rows if r[2] == 'FAIL')
print(f"  Failed blocks: {failed}")
PYMERMAID
echo ""

echo "=== QA Rerun Complete ==="
echo ""
echo "Reports generated:"
echo "  - docs/authoring/qa/diagram_lint.csv"
echo "  - docs/authoring/qa/link_lint.csv"
echo "  - docs/authoring/qa/dataset_sanity.csv"
echo "  - docs/authoring/qa/mermaid_sanity.csv"
