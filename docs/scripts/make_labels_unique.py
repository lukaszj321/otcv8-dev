#!/usr/bin/env python3
"""Post-process generated MyST markdown files to ensure label names are unique per file.

Usage: python docs/scripts/make_labels_unique.py

This script:
- finds label definitions like (label)= at the start of a line
- renames definitions to append a file-specific slug
- updates references to unique labels when unambiguous
- reports ambiguous references for manual review
"""
import re
import sys
from pathlib import Path

DOCS_DIR = Path('docs')
LABEL_DEF_RE = re.compile(r'^\(([A-Za-z0-9_:-]+)\)=\s*$', re.MULTILINE)


def file_slug(path: Path) -> str:
    """Generate a file-specific slug based on relative path to docs with non-alnum replaced by '_'."""
    rel = path.relative_to(DOCS_DIR)
    s = str(rel).replace('/', '_').replace('\\', '_')
    s = re.sub(r'[^A-Za-z0-9_]', '_', s)
    # drop extension
    if s.endswith('_md'):
        s = s[:-3]
    return s


def collect_label_defs():
    """Collect all label definitions and their files."""
    defs = {}  # label -> list of files
    md_files = list(DOCS_DIR.rglob('*.md'))
    print(f"Scanning {len(md_files)} markdown files for label definitions...")
    for i, p in enumerate(md_files):
        if (i + 1) % 200 == 0:
            print(f"  Processed {i + 1}/{len(md_files)} files...")
        try:
            txt = p.read_text(encoding='utf-8')
            for m in LABEL_DEF_RE.finditer(txt):
                label = m.group(1)
                defs.setdefault(label, []).append(p)
        except Exception as e:
            print(f"Warning: Could not read {p}: {e}", file=sys.stderr)
    return defs


def make_replacements(defs):
    """Create mapping from (original label, file) to new_label."""
    mapping = {}
    for label, files in defs.items():
        for f in files:
            mapping[(label, f)] = f"{label}__{file_slug(f)}"
    return mapping


def build_ref_pattern(label):
    """Build a combined regex pattern for all reference types for a given label."""
    escaped_label = re.escape(label)
    # Match :ref:`label`, {ref}`label`, or :any:`label`
    return re.compile(
        r'(:ref:`' + escaped_label + r'`|'
        r'\{ref\}`' + escaped_label + r'`|'
        r':any:`' + escaped_label + r'`)'
    )


def replace_defs_and_local_refs(mapping):
    """Replace definitions in files and local references that refer to own labels."""
    # Build a reverse mapping: file -> list of (label, new_label)
    file_labels = {}
    for (label, f), new_label in mapping.items():
        if f not in file_labels:
            file_labels[f] = []
        file_labels[f].append((label, new_label))
    
    print(f"Updating definitions and local references in {len(file_labels)} files...")
    for i, (p, labels_in_file) in enumerate(file_labels.items()):
        if (i + 1) % 100 == 0:
            print(f"  Processed {i + 1}/{len(file_labels)} files...")
        try:
            txt = p.read_text(encoding='utf-8')
            changed = False
            
            # replace label defs if present
            def def_sub_func(m):
                label = m.group(1)
                if (label, p) in mapping:
                    return f"({mapping[(label, p)]})="
                return m.group(0)
            
            txt_new = LABEL_DEF_RE.sub(def_sub_func, txt)
            if txt_new != txt:
                changed = True
                txt = txt_new
            
            # replace references that point to labels defined in this same file
            for label, new_label in labels_in_file:
                # Build pattern for this label
                pattern = build_ref_pattern(label)
                # Replace all reference types at once
                def ref_sub_func(m):
                    matched = m.group(1)
                    if matched.startswith(':ref:'):
                        return f':ref:`{new_label}`'
                    elif matched.startswith('{ref}'):
                        return f'{{ref}}`{new_label}`'
                    elif matched.startswith(':any:'):
                        return f':any:`{new_label}`'
                    return matched
                
                txt2 = pattern.sub(ref_sub_func, txt)
                if txt2 != txt:
                    changed = True
                    txt = txt2
            
            if changed:
                # Write to temp file then replace (safe write)
                temp_path = p.with_suffix('.md.tmp')
                temp_path.write_text(txt, encoding='utf-8')
                temp_path.replace(p)
        except Exception as e:
            print(f"Warning: Could not process {p}: {e}", file=sys.stderr)


def replace_global_refs_for_unambiguous(defs, mapping):
    """For labels that have a single defining file, replace global refs across all docs."""
    single_defs = {label: files[0] for label, files in defs.items() if len(files) == 1}
    if not single_defs:
        print("No unambiguous labels to update globally.")
        return
    
    print(f"Updating global references for {len(single_defs)} unambiguous labels...")
    
    # Create a mapping from old to new labels
    label_to_new = {label: mapping[(label, f)] for label, f in single_defs.items()}
    
    # Simple pattern to find any reference
    ref_pattern = re.compile(r'(:ref:`([^`]+)`|\{ref\}`([^`]+)`|:any:`([^`]+)`)')
    
    md_files = list(DOCS_DIR.rglob('*.md'))
    files_updated = 0
    for i, p in enumerate(md_files):
        if (i + 1) % 200 == 0:
            print(f"  Processed {i + 1}/{len(md_files)} files... ({files_updated} updated)")
        try:
            txt = p.read_text(encoding='utf-8')
            
            # Replace all references in one pass
            def ref_sub_func(m):
                full_match = m.group(0)
                # Extract the label from whichever group matched
                label = m.group(2) or m.group(3) or m.group(4)
                
                # Only replace if this is an unambiguous label
                if label in label_to_new:
                    new_label = label_to_new[label]
                    if full_match.startswith(':ref:'):
                        return f':ref:`{new_label}`'
                    elif full_match.startswith('{ref}'):
                        return f'{{ref}}`{new_label}`'
                    elif full_match.startswith(':any:'):
                        return f':any:`{new_label}`'
                
                return full_match
            
            txt_new = ref_pattern.sub(ref_sub_func, txt)
            
            if txt_new != txt:
                # Write to temp file then replace (safe write)
                temp_path = p.with_suffix('.md.tmp')
                temp_path.write_text(txt_new, encoding='utf-8')
                temp_path.replace(p)
                files_updated += 1
        except Exception as e:
            print(f"Warning: Could not process {p}: {e}", file=sys.stderr)
    
    print(f"  Updated {files_updated} files with global reference changes.")


def main():
    """Main entry point."""
    print("MyST Label Uniqueness Processor")
    print("=" * 70)
    
    defs = collect_label_defs()
    if not defs:
        print('No label definitions found under docs/; nothing to do.')
        return 0
    
    print(f"Found {len(defs)} distinct labels.")
    
    mapping = make_replacements(defs)
    replace_defs_and_local_refs(mapping)
    replace_global_refs_for_unambiguous(defs, mapping)

    # Report summary
    dupes = {k: v for k, v in defs.items() if len(v) > 1}
    print("\n" + "=" * 70)
    print('Label processing complete.')
    print(f'Total distinct labels found: {len(defs)}')
    print(f'Duplicated labels (count >1): {len(dupes)}')
    if dupes:
        print('\nDuplicated labels (showing first 10):')
        for i, (label, files) in enumerate(sorted(dupes.items(), key=lambda x: len(x[1]), reverse=True)[:10]):
            print(f' - {label}: ({len(files)} occurrences)')
        if len(dupes) > 10:
            print(f'\n... and {len(dupes) - 10} more duplicated labels.')
        print('\nNote: For duplicated labels, the script renamed definitions per file and updated local references.')
        print('External references (from other files) that point to these duplicated labels were NOT')
        print('automatically changed and should be reviewed manually.')
    print("=" * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
