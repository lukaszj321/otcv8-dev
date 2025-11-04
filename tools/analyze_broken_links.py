#!/usr/bin/env python3
import csv
import re
from pathlib import Path

AUTHORING = Path('docs/authoring')
REPORT = AUTHORING / 'qa' / 'link_lint.csv'
OUT = AUTHORING / 'qa' / 'link_triage.csv'

def classify(md_rel: Path, link: str):
    """Return (classification, suggestion_path or '')."""
    md_abs = (AUTHORING / md_rel).resolve()
    base = md_abs.parent
    # Directory links
    if link.endswith('/'):
        target = (base / link).resolve()
        return ('missing_dir', '')
    # Patterns considered obsolete/no-op in docs
    if str(md_rel).startswith('_sources/'):
        return ('obsolete_source_draft', '')
    if link == 'obj' or link.endswith('/obj'):
        return ('garbage_obj', '')
    if re.search(r'^\./sections/.*\.md$', link):
        return ('obsolete_sections', '')
    if re.search(r'^\./(datasets|stats|analysis)/', link):
        return ('obsolete_artifacts', '')
    if re.search(r'\.(json|schema\.json|dataset\.csv|dataset\.jsonl)$', link):
        return ('obsolete_schema_or_dataset', '')
    # Suggestion: if link points to chapter-level sibling diagrams, check existence
    # e.g. md: 04_ui/otui/game_battle/battle.md, link: ../diagrams/battle.mmd
    if link.startswith('../diagrams/'):
        parts = md_rel.parts
        if len(parts) >= 2:
            chapter_root = AUTHORING / parts[0] / 'diagrams' / Path(link).name
            if chapter_root.exists():
                return ('suggest_fix', str(Path('../diagrams') / Path(link).name))
    # analytics/execution_report.md → prefer execution_report_prev.md if exists
    if link == 'analytics/execution_report.md':
        alt = AUTHORING / 'analytics' / 'execution_report_prev.md'
        if alt.exists():
            return ('suggest_fix', 'analytics/execution_report_prev.md')
        return ('needed_missing', '')
    # Default: needed but missing
    return ('needed_missing', '')

def main():
    broken = []
    with REPORT.open('r', encoding='utf-8', newline='') as f:
        r = csv.DictReader(f)
        for row in r:
            if row['status'] == 'BROKEN':
                broken.append((row['file'], row['link']))

    rows = []
    counts = {}
    for file_rel, link in broken:
        cls, sugg = classify(Path(file_rel), link)
        counts[cls] = counts.get(cls, 0) + 1
        rows.append([file_rel, link, cls, sugg])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['file', 'link', 'classification', 'suggestion'])
        w.writerows(rows)

    print('Broken links triaged:', len(rows))
    for k in sorted(counts):
        print(f'  {k}: {counts[k]}')
    print('Report:', OUT)

if __name__ == '__main__':
    main()


