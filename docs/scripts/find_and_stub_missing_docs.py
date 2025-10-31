#!/usr/bin/env python3
"""
find_and_stub_missing_docs.py

Scans docs for missing includes/literalinclude/:file: references and .mmd references.
Prints report and creates safe placeholders when run with --apply.

Usage:
    python3 docs/scripts/find_and_stub_missing_docs.py        # dry-run (report only)
    python3 docs/scripts/find_and_stub_missing_docs.py --apply # create placeholders
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Set


def find_docs_root() -> Path:
    """Find docs directory relative to script location."""
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent
    if not docs_dir.name == "docs":
        # Fallback: try current working directory
        docs_dir = Path.cwd() / "docs"
    return docs_dir


def scan_for_references(docs_dir: Path) -> Dict[str, List[str]]:
    """
    Scan all .md and .rst files for references to external files.
    
    Returns:
        dict with keys 'include', 'literalinclude', 'file', 'mermaid'
        Each value is a list of referenced file paths.
    """
    references = {
        'include': [],
        'literalinclude': [],
        'file': [],
        'mermaid': []
    }
    
    # Patterns to match
    include_pattern = re.compile(r'```\{include\}\s+([^\s]+)')
    literalinclude_pattern = re.compile(r'```\{literalinclude\}\s+([^\s]+)')
    file_pattern = re.compile(r':file:`([^`]+)`')
    mermaid_file_pattern = re.compile(r'```\{mermaid\}\s+:file:\s*([^\s]+)')
    
    for ext in ['*.md', '*.rst']:
        for doc_file in docs_dir.rglob(ext):
            try:
                content = doc_file.read_text(encoding='utf-8')
                
                # Find includes
                for match in include_pattern.finditer(content):
                    ref_path = match.group(1)
                    references['include'].append((str(doc_file), ref_path))
                
                # Find literalincludes
                for match in literalinclude_pattern.finditer(content):
                    ref_path = match.group(1)
                    references['literalinclude'].append((str(doc_file), ref_path))
                
                # Find :file: references
                for match in file_pattern.finditer(content):
                    ref_path = match.group(1)
                    references['file'].append((str(doc_file), ref_path))
                
                # Find mermaid file references
                for match in mermaid_file_pattern.finditer(content):
                    ref_path = match.group(1)
                    references['mermaid'].append((str(doc_file), ref_path))
                    
            except Exception as e:
                print(f"Warning: Could not read {doc_file}: {e}", file=sys.stderr)
    
    return references


def check_missing_files(docs_dir: Path, references: Dict[str, List[str]]) -> Dict[str, List[tuple]]:
    """
    Check which referenced files are missing.
    
    Returns:
        dict with same keys as references, containing only missing file tuples
    """
    missing = {k: [] for k in references.keys()}
    
    for ref_type, ref_list in references.items():
        for source_file, ref_path in ref_list:
            # Resolve relative path
            source_path = Path(source_file)
            if ref_path.startswith('/'):
                # Absolute path from docs root
                target = docs_dir / ref_path.lstrip('/')
            else:
                # Relative to source file
                target = (source_path.parent / ref_path).resolve()
            
            if not target.exists():
                missing[ref_type].append((source_file, ref_path, str(target)))
    
    return missing


def create_placeholder_mmd(path: Path):
    """Create a minimal Mermaid diagram placeholder."""
    content = """%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Placeholder] --> B[TODO: Add diagram content]
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    print(f"  Created: {path}")


def create_placeholder_csv(path: Path):
    """Create a minimal CSV placeholder."""
    # Try to infer header from filename
    stem = path.stem
    if 'module' in stem:
        header = "module,function,params,returns,notes"
    elif 'ui' in stem or 'widget' in stem:
        header = "widget,type,id,file,notes"
    elif 'event' in stem:
        header = "event,source,handler,payload,notes"
    else:
        header = "id,name,type,value,notes"
    
    content = f"{header}\n# Placeholder row - edit this file\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    print(f"  Created: {path}")


def create_placeholder_md(path: Path):
    """Create a minimal Markdown placeholder."""
    title = path.stem.replace('_', ' ').replace('-', ' ').title()
    content = f"""# {title}

> **TODO**: Add content for this document.

This is a placeholder file generated by the documentation maintenance script.
Please replace this content with actual documentation.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    print(f"  Created: {path}")


def create_placeholder_rst(path: Path):
    """Create a minimal reStructuredText placeholder."""
    title = path.stem.replace('_', ' ').replace('-', ' ').title()
    content = f"""{title}
{'=' * len(title)}

.. note::
   
   **TODO**: Add content for this document.

This is a placeholder file generated by the documentation maintenance script.
Please replace this content with actual documentation.
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    print(f"  Created: {path}")


def create_placeholders(missing: Dict[str, List[tuple]], apply: bool = False):
    """Create placeholder files for missing references."""
    if not apply:
        print("\n=== DRY RUN: No files will be created ===")
        print("Run with --apply to create placeholder files.\n")
        return
    
    print("\n=== Creating placeholder files ===\n")
    
    created_count = 0
    for ref_type, items in missing.items():
        for source_file, ref_path, target_path in items:
            target = Path(target_path)
            
            # Skip if already exists (race condition protection)
            if target.exists():
                continue
            
            try:
                # Create appropriate placeholder based on extension
                if target.suffix == '.mmd':
                    create_placeholder_mmd(target)
                    created_count += 1
                elif target.suffix == '.csv':
                    create_placeholder_csv(target)
                    created_count += 1
                elif target.suffix == '.md':
                    create_placeholder_md(target)
                    created_count += 1
                elif target.suffix == '.rst':
                    create_placeholder_rst(target)
                    created_count += 1
                else:
                    print(f"  Skipped (unsupported type): {target}")
            except Exception as e:
                print(f"  Error creating {target}: {e}", file=sys.stderr)
    
    print(f"\nCreated {created_count} placeholder file(s).")


def main():
    apply = '--apply' in sys.argv
    
    docs_dir = find_docs_root()
    print(f"Scanning docs directory: {docs_dir}\n")
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found: {docs_dir}", file=sys.stderr)
        sys.exit(1)
    
    print("Scanning for file references...")
    references = scan_for_references(docs_dir)
    
    total_refs = sum(len(v) for v in references.values())
    print(f"Found {total_refs} file reference(s)\n")
    
    print("Checking for missing files...")
    missing = check_missing_files(docs_dir, references)
    
    # Print report
    print("\n" + "="*70)
    print("MISSING FILES REPORT")
    print("="*70 + "\n")
    
    total_missing = 0
    for ref_type, items in missing.items():
        if items:
            print(f"\n{ref_type.upper()} references ({len(items)}):")
            for source_file, ref_path, target_path in items:
                print(f"  - Referenced in: {source_file}")
                print(f"    Path: {ref_path}")
                print(f"    Resolved to: {target_path}")
                print()
            total_missing += len(items)
    
    if total_missing == 0:
        print("No missing files found! ✓")
    else:
        print(f"\nTotal missing: {total_missing} file(s)")
        create_placeholders(missing, apply)
    
    print("\n" + "="*70)


if __name__ == '__main__':
    main()
