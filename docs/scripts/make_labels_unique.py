#!/usr/bin/env python3
"""
Post-process generated MyST markdown files to ensure label names are unique per file.

Usage:
  python docs/scripts/make_labels_unique.py
"""
from pathlib import Path
import re
import sys
import tempfile
import shutil

DOCS_DIR = Path('docs')
LABEL_DEF_RE = re.compile(r'^\(([A-Za-z0-9_:-]+)\)=\s*$', re.MULTILINE)
# Pattern templates for references - will be formatted with specific label
REF_PATTERNS = [
    (r':ref:`{}`', ':ref:`{}`'),
    (r'\{{ref\}}`{}`', '{{ref}}`{}`'),
    (r':any:`{}`', ':any:`{}`'),
]

def file_slug(path: Path) -> str:
    rel = path.relative_to(DOCS_DIR)
    s = str(rel).replace('/', '_').replace('\\', '_')
    s = re.sub(r'[^A-Za-z0-9_]', '_', s)
    if s.endswith('.md'):
        s = s[:-3]
    return s

def safe_write(path: Path, text: str):
    tmp = Path(tempfile.mktemp(dir=path.parent))
    tmp.write_text(text, encoding='utf-8')
    shutil.move(str(tmp), str(path))

def collect_label_defs():
    defs = {}
    md_files = list(DOCS_DIR.rglob('*.md'))
    for p in md_files:
        try:
            txt = p.read_text(encoding='utf-8')
        except Exception:
            txt = p.read_text(encoding='latin-1')
        for m in LABEL_DEF_RE.finditer(txt):
            label = m.group(1)
            defs.setdefault(label, []).append(p)
    return defs

def make_mapping(defs):
    mapping = {}
    for label, files in defs.items():
        for f in files:
            mapping[(label, f)] = f"{label}__{file_slug(f)}"
    return mapping

def replace_defs_and_local_refs(mapping):
    md_files = list(DOCS_DIR.rglob('*.md'))
    for p in md_files:
        try:
            txt = p.read_text(encoding='utf-8')
        except Exception:
            txt = p.read_text(encoding='latin-1')
        changed = False
        def replacer(m):
            label = m.group(1)
            key = (label, p)
            if key in mapping:
                return f"({mapping[key]})="
            return m.group(0)
        txt_new = LABEL_DEF_RE.sub(replacer, txt)
        if txt_new != txt:
            txt = txt_new
            changed = True
        for (label, f), new_label in mapping.items():
            if f == p:
                for pat_template, fmt_template in REF_PATTERNS:
                    pat_str = pat_template.format(re.escape(label))
                    pat_full = re.compile(pat_str)
                    txt2 = pat_full.sub(fmt_template.format(new_label), txt)
                    if txt2 != txt:
                        txt = txt2
                        changed = True
        if changed:
            safe_write(p, txt)

def replace_global_refs_for_unambiguous(defs, mapping):
    single_defs = {label: files[0] for label, files in defs.items() if len(files) == 1}
    if not single_defs:
        return
    md_files = list(DOCS_DIR.rglob('*.md'))
    for p in md_files:
        try:
            txt = p.read_text(encoding='utf-8')
        except Exception:
            txt = p.read_text(encoding='latin-1')
        changed = False
        for label, f in single_defs.items():
            new_label = mapping[(label, f)]
            for pat_template, fmt_template in REF_PATTERNS:
                pat_str = pat_template.format(re.escape(label))
                pat_full = re.compile(pat_str)
                txt2 = pat_full.sub(fmt_template.format(new_label), txt)
                if txt2 != txt:
                    txt = txt2
                    changed = True
        if changed:
            safe_write(p, txt)

def find_ambiguous_external_refs(defs):
    dupes = {label: files for label, files in defs.items() if len(files) > 1}
    if not dupes:
        return {}
    md_files = list(DOCS_DIR.rglob('*.md'))
    report = {}
    for label, defs_files in dupes.items():
        refs = []
        for p in md_files:
            try:
                txt = p.read_text(encoding='utf-8')
            except Exception:
                txt = p.read_text(encoding='latin-1')
            if p in defs_files:
                continue
            for pat_template, _ in REF_PATTERNS:
                pat_str = pat_template.format(re.escape(label))
                pat_full = re.compile(pat_str)
                if pat_full.search(txt):
                    refs.append(p)
                    break
        if refs:
            report[label] = {'defs': defs_files, 'refs': refs}
    return report

def main():
    if not DOCS_DIR.exists():
        print("docs/ directory not found. Nothing to do.")
        return 0
    defs = collect_label_defs()
    if not defs:
        print("No label definitions found under docs/.")
        return 0
    mapping = make_mapping(defs)
    replace_defs_and_local_refs(mapping)
    replace_global_refs_for_unambiguous(defs, mapping)
    ambig = find_ambiguous_external_refs(defs)
    print("Label processing complete.")
    print(f"Total distinct labels found: {len(defs)}")
    dup_count = sum(1 for v in defs.values() if len(v) > 1)
    print(f"Labels duplicated across files: {dup_count}")
    if ambig:
        print("\nAmbiguous labels with external references (manual review required):")
        for label, info in ambig.items():
            print(f" - {label}:")
            for d in info['defs']:
                print(f"    def: {d}")
            for r in info['refs']:
                print(f"    external ref: {r}")
    else:
        print("No ambiguous external references found.")
    print("Note: script renames definitions and updates local refs. For labels defined in exactly one file, global refs were updated automatically.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
