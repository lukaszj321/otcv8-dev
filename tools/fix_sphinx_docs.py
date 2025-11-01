#!/usr/bin/env python3
"""
Fix Sphinx documentation build errors by:
1. Removing trailing transitions (---, ***, ===) from doc files
2. Replacing csv-table directives with missing files with warning admonitions

Usage:
    python3 tools/fix_sphinx_docs.py           # Dry-run mode (shows what would be changed)
    python3 tools/fix_sphinx_docs.py --apply   # Apply changes to files
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Tuple, Set


def find_doc_files(docs_root: Path) -> List[Path]:
    """Find all documentation files in the docs/ directory."""
    extensions = ["*.md", "*.rst", "*.mdx"]
    files = []
    for ext in extensions:
        files.extend(docs_root.rglob(ext))
    return sorted(files)


def remove_trailing_transitions(content: str) -> Tuple[str, bool]:
    """
    Remove trailing transition lines from content.
    Transitions are lines with 3+ hyphens, asterisks, or equals.
    
    Returns: (modified_content, was_modified)
    """
    lines = content.splitlines(keepends=True)
    
    # Pattern for transition lines (3+ hyphens, asterisks, or equals)
    transition_pattern = re.compile(r'^\s*([-*=]{3,})\s*$')
    
    # Remove trailing transitions by checking from end
    modified = False
    while lines:
        # Check last non-empty line
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i].rstrip('\r\n')
            if line.strip():  # Found last non-blank line
                if transition_pattern.match(line):
                    # Remove this transition line
                    lines.pop(i)
                    modified = True
                    break
                else:
                    # Last non-blank line is not a transition, done
                    return ''.join(lines), modified
            # Continue to previous line if current is blank
        else:
            # All lines checked, none were non-blank transitions
            break
    
    return ''.join(lines), modified


def find_csv_table_directives(content: str, doc_path: Path) -> List[dict]:
    """
    Find csv-table directives and check if referenced files exist.
    
    Returns list of dicts with:
        - start_line: line number where directive starts (0-indexed)
        - end_line: line number where directive block ends (0-indexed)
        - csv_path: the referenced CSV path
        - exists: whether the file exists
        - directive_text: the full directive text
    """
    lines = content.splitlines()
    directives = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Look for csv-table directives (both MyST and reST)
        # MyST: ```{csv-table} or {csv-table}
        # reST: .. csv-table::
        myst_match = re.search(r'```?\{csv-table\}', line)
        rest_match = re.search(r'^\.\.\s+csv-table::', line)
        
        if myst_match or rest_match:
            start_line = i
            end_line = i
            csv_path = None
            
            # Look for :file: option in following indented lines
            j = i + 1
            indent_level = None
            
            while j < len(lines):
                next_line = lines[j]
                
                # Determine indent level from first option line
                if indent_level is None and next_line.strip() and next_line[0] in ' \t:':
                    indent_level = len(next_line) - len(next_line.lstrip())
                
                # Check if still in directive block
                if next_line.strip():
                    current_indent = len(next_line) - len(next_line.lstrip())
                    
                    # MyST fenced block ends with ```
                    if myst_match and next_line.strip().startswith('```'):
                        end_line = j
                        break
                    
                    # reST block ends when indent decreases
                    if rest_match and indent_level is not None:
                        if current_indent < indent_level and not next_line.strip().startswith(':'):
                            end_line = j - 1
                            break
                    
                    # Look for :file: option
                    file_match = re.search(r':file:\s*(.+)', next_line)
                    if file_match:
                        csv_path = file_match.group(1).strip()
                
                j += 1
                end_line = j - 1
            
            # Check if CSV file exists
            if csv_path:
                doc_dir = doc_path.parent
                # Resolve the path relative to document
                try:
                    full_path = (doc_dir / csv_path).resolve()
                    exists = full_path.exists()
                except Exception:
                    exists = False
                
                directive_text = '\n'.join(lines[start_line:end_line + 1])
                
                directives.append({
                    'start_line': start_line,
                    'end_line': end_line,
                    'csv_path': csv_path,
                    'exists': exists,
                    'directive_text': directive_text
                })
        
        i += 1
    
    return directives


def replace_missing_csv_tables(content: str, doc_path: Path) -> Tuple[str, List[str]]:
    """
    Replace csv-table directives referencing missing files with warning admonitions.
    
    Returns: (modified_content, list_of_replaced_paths)
    """
    directives = find_csv_table_directives(content, doc_path)
    
    # Filter to only missing files
    missing_directives = [d for d in directives if not d['exists']]
    
    if not missing_directives:
        return content, []
    
    lines = content.splitlines(keepends=True)
    replacements = []
    
    # Process in reverse order to maintain line numbers
    for directive in reversed(missing_directives):
        start = directive['start_line']
        end = directive['end_line']
        csv_path = directive['csv_path']
        
        # Determine if it's MyST or reST based on directive text
        directive_line = lines[start].rstrip('\r\n')
        is_myst = '```{csv-table}' in directive_line or '{csv-table}' in directive_line
        
        # Create replacement warning
        if is_myst:
            # MyST warning
            replacement = [
                '```{warning}\n',
                f'Missing CSV file: `{csv_path}`\n',
                '\n',
                'Either add the dataset or update the directive.\n',
                '```\n'
            ]
        else:
            # reST warning
            replacement = [
                '.. warning::\n',
                '\n',
                f'   Missing CSV file: ``{csv_path}``\n',
                '\n',
                '   Either add the dataset or update the directive.\n'
            ]
        
        # Replace the directive block
        lines[start:end + 1] = replacement
        replacements.append(csv_path)
    
    return ''.join(lines), replacements


def process_file(file_path: Path, apply: bool = False) -> dict:
    """
    Process a single documentation file.
    
    Returns dict with:
        - modified: whether file was modified
        - transitions_removed: whether transitions were removed
        - csv_replaced: list of CSV paths that were replaced
    """
    try:
        # Read file with UTF-8 encoding
        content = file_path.read_text(encoding='utf-8')
        original_content = content
        
        # Remove trailing transitions
        content, transitions_removed = remove_trailing_transitions(content)
        
        # Replace missing csv-table directives
        content, csv_replaced = replace_missing_csv_tables(content, file_path)
        
        modified = content != original_content
        
        # Write back if applying changes
        if apply and modified:
            file_path.write_text(content, encoding='utf-8')
        
        return {
            'modified': modified,
            'transitions_removed': transitions_removed,
            'csv_replaced': csv_replaced
        }
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return {
            'modified': False,
            'transitions_removed': False,
            'csv_replaced': []
        }


def main():
    parser = argparse.ArgumentParser(
        description='Fix Sphinx documentation build errors'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply changes to files (default is dry-run)'
    )
    parser.add_argument(
        '--docs-root',
        type=Path,
        default=Path('docs'),
        help='Root directory of documentation (default: docs/)'
    )
    
    args = parser.parse_args()
    
    docs_root = args.docs_root
    if not docs_root.exists():
        print(f"Error: Documentation root '{docs_root}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning documentation in: {docs_root}")
    print(f"Mode: {'APPLY CHANGES' if args.apply else 'DRY-RUN'}")
    print()
    
    # Find all documentation files
    doc_files = find_doc_files(docs_root)
    print(f"Found {len(doc_files)} documentation files")
    print()
    
    # Process each file
    stats = {
        'total_files': len(doc_files),
        'files_modified': 0,
        'transitions_removed': 0,
        'csv_tables_replaced': 0,
        'modified_files': []
    }
    
    for file_path in doc_files:
        result = process_file(file_path, apply=args.apply)
        
        if result['modified']:
            stats['files_modified'] += 1
            stats['modified_files'].append(file_path)
            
            if result['transitions_removed']:
                stats['transitions_removed'] += 1
            
            if result['csv_replaced']:
                stats['csv_tables_replaced'] += len(result['csv_replaced'])
                
                # Show details
                rel_path = file_path.relative_to(docs_root)
                print(f"Modified: {rel_path}")
                if result['transitions_removed']:
                    print(f"  - Removed trailing transitions")
                if result['csv_replaced']:
                    for csv_path in result['csv_replaced']:
                        print(f"  - Replaced missing CSV: {csv_path}")
    
    # Print summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files scanned:         {stats['total_files']}")
    print(f"Files modified:              {stats['files_modified']}")
    print(f"Files with transitions fixed: {stats['transitions_removed']}")
    print(f"CSV tables replaced:         {stats['csv_tables_replaced']}")
    print()
    
    if not args.apply and stats['files_modified'] > 0:
        print("This was a DRY-RUN. Use --apply to actually modify files.")
    elif args.apply and stats['files_modified'] > 0:
        print("Changes have been applied to the files.")
    else:
        print("No changes needed.")
    
    print()


if __name__ == '__main__':
    main()
