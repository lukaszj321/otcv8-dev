#!/usr/bin/env python3
import csv
import re
from pathlib import Path

AUTHORING = Path('docs/authoring')
TRIAGE = AUTHORING / 'qa' / 'link_triage.csv'

SUGGEST_CLASSES = {'suggest_fix'}
DELETE_CLASSES = {
    'obsolete_sections',
    'obsolete_artifacts',
    'obsolete_schema_or_dataset',
    'garbage_obj',
    'missing_dir',
}

def replace_link(text: str, old: str, new: str) -> str:
    # Replace target only: ](old) -> ](new)
    # Escape regex special chars in old; use function repl to avoid \ escapes
    old_esc = re.escape(old)
    pattern = re.compile(r"\]\(" + old_esc + r"\)")
    return pattern.sub(lambda m: "](" + new + ")", text)

def strip_link(text: str, old: str) -> str:
    # Turn [label](old) into label
    old_esc = re.escape(old)
    return re.sub(r"\[([^\]]+)\]\(" + old_esc + r"\)", r"\1", text)

def main():
    edits_by_file = {}
    with TRIAGE.open('r', encoding='utf-8', newline='') as f:
        r = csv.DictReader(f)
        for row in r:
            file_rel = row['file']
            link = row['link']
            cls = row['classification']
            sugg = row.get('suggestion', '')
            edits_by_file.setdefault(file_rel, []).append((cls, link, sugg))

    changed_files = 0
    for file_rel, ops in edits_by_file.items():
        md_path = AUTHORING / file_rel
        if not md_path.exists():
            continue
        original = md_path.read_text(encoding='utf-8')
        updated = original
        for cls, link, sugg in ops:
            if cls in SUGGEST_CLASSES and sugg:
                updated = replace_link(updated, link, sugg)
            elif cls in DELETE_CLASSES:
                updated = strip_link(updated, link)
        if updated != original:
            md_path.write_text(updated, encoding='utf-8')
            changed_files += 1

    print(f"Applied triage to {changed_files} files.")

if __name__ == '__main__':
    main()


