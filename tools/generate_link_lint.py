#!/usr/bin/env python3
import re, csv
from pathlib import Path

OUT = Path('docs/authoring/qa/link_lint.csv')
ROOT = Path('docs/authoring')

rows = []
for md in ROOT.rglob('*.md'):
    try:
        txt = md.read_text(encoding='utf-8')
    except Exception:
        continue
    for m in re.finditer(r"\]\(([^)#]+)\)", txt):
        link = m.group(1)
        if link.startswith(('http', 'mailto:', '#')):
            continue
        tgt = (md.parent / link).resolve()
        status = 'OK' if tgt.exists() else 'BROKEN'
        rows.append([str(md.relative_to(ROOT)), status, link])

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['file','status','link'])
    w.writerows(rows)

print(f'Link lint regenerated. Total: {len(rows)}')
