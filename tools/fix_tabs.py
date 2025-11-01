#!/usr/bin/env python3
"""
fix_tabs.py

Detects and fixes tab-item closure issues in Sphinx MyST documentation.
Ensures that tab-set/tab-item directives are properly closed.

Usage:
    python3 tools/fix_tabs.py              # dry-run (detect issues)
    python3 tools/fix_tabs.py --apply      # apply fixes (creates .bak backups)
"""

import sys
import re
import shutil
from pathlib import Path
from typing import List, Tuple


def find_docs_root() -> Path:
    """Find the docs directory."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    return repo_root / "docs"


def find_md_files(docs_root: Path) -> List[Path]:
    """Find all markdown files in docs directory."""
    return list(docs_root.rglob("*.md"))


def check_tab_directives(content: str, filepath: Path) -> List[Tuple[int, str]]:
    """
    Check for tab-item directive issues.
    
    Returns:
        List of (line_number, issue_description) tuples
    """
    issues = []
    lines = content.split('\n')
    
    # Track tab-set and tab-item nesting
    tab_set_stack = []
    tab_item_stack = []
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Detect tab-set start
        if stripped.startswith('```{tab-set}') or stripped.startswith('````{tab-set}'):
            tab_set_stack.append(i)
        
        # Detect tab-item start
        elif stripped.startswith('```{tab-item}') or stripped.startswith('````{tab-item}'):
            if not tab_set_stack:
                issues.append((i, "tab-item without parent tab-set"))
            else:
                tab_item_stack.append(i)
        
        # Detect code fence closures
        elif stripped == '```' or stripped == '````':
            # Close tab-item if open
            if tab_item_stack:
                tab_item_stack.pop()
            # Close tab-set if no more tab-items and tab-set is open
            elif tab_set_stack:
                tab_set_stack.pop()
        
        # Check for unclosed directives at end of nested blocks
        elif stripped and not stripped.startswith('#') and not stripped.startswith('```'):
            # If we have open tab-items but see content that suggests end of block
            if tab_item_stack and stripped.startswith('(') and ')=' in stripped:
                # This is a new anchor - possible missing closure
                issues.append((i, f"Possible unclosed tab-item (opened at line {tab_item_stack[-1]})"))
    
    # Check for unclosed directives at end of file
    if tab_item_stack:
        for line_num in tab_item_stack:
            issues.append((line_num, "Unclosed tab-item directive"))
    if tab_set_stack:
        for line_num in tab_set_stack:
            issues.append((line_num, "Unclosed tab-set directive"))
    
    return issues


def fix_tab_directives(content: str) -> str:
    """
    Fix tab-item directive issues by ensuring proper closures.
    
    This function:
    - Ensures tab-item directives are properly closed
    - Ensures tab-set directives are properly closed
    - Adds missing closing fences
    """
    lines = content.split('\n')
    fixed_lines = []
    
    tab_set_stack = []
    tab_item_stack = []
    indent_stack = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())
        
        # Detect tab-set start
        if stripped.startswith('```{tab-set}') or stripped.startswith('````{tab-set}'):
            tab_set_stack.append(i)
            indent_stack.append(indent)
            fixed_lines.append(line)
        
        # Detect tab-item start
        elif stripped.startswith('```{tab-item}') or stripped.startswith('````{tab-item}'):
            tab_item_stack.append((i, indent))
            fixed_lines.append(line)
        
        # Detect fence closures
        elif stripped in ('```', '````'):
            # Close tab-item if open
            if tab_item_stack:
                tab_item_stack.pop()
            # Close tab-set if no more tab-items
            elif tab_set_stack:
                tab_set_stack.pop()
                if indent_stack:
                    indent_stack.pop()
            fixed_lines.append(line)
        
        # Check for new section/anchor that might need closure
        elif stripped and (stripped.startswith('#') or (stripped.startswith('(') and ')=' in stripped)):
            # Close any open tab-items
            while tab_item_stack:
                _, tab_indent = tab_item_stack.pop()
                fixed_lines.append(' ' * tab_indent + '```')
            
            # Close any open tab-sets
            while tab_set_stack:
                tab_set_stack.pop()
                base_indent = indent_stack.pop() if indent_stack else 0
                fixed_lines.append(' ' * base_indent + '```')
            
            fixed_lines.append(line)
        
        else:
            fixed_lines.append(line)
    
    # Close any remaining open directives at end of file
    while tab_item_stack:
        _, tab_indent = tab_item_stack.pop()
        fixed_lines.append(' ' * tab_indent + '```')
    
    while tab_set_stack:
        tab_set_stack.pop()
        base_indent = indent_stack.pop() if indent_stack else 0
        fixed_lines.append(' ' * base_indent + '```')
    
    return '\n'.join(fixed_lines)


def process_file(filepath: Path, apply_fix: bool = False) -> Tuple[bool, List[str]]:
    """
    Process a single markdown file.
    
    Returns:
        (has_issues, messages)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return False, [f"Error reading {filepath}: {e}"]
    
    issues = check_tab_directives(content, filepath)
    
    if not issues:
        return False, []
    
    messages = [f"\n{filepath}:"]
    for line_num, issue in issues:
        messages.append(f"  Line {line_num}: {issue}")
    
    if apply_fix:
        # Create backup
        backup_path = filepath.with_suffix(filepath.suffix + '.bak')
        shutil.copy2(filepath, backup_path)
        messages.append(f"  Created backup: {backup_path}")
        
        # Apply fix
        fixed_content = fix_tab_directives(content)
        filepath.write_text(fixed_content, encoding='utf-8')
        messages.append(f"  ✓ Fixed tab directive issues")
    
    return True, messages


def main():
    """Main entry point."""
    apply_fix = '--apply' in sys.argv
    
    docs_root = find_docs_root()
    if not docs_root.exists():
        print(f"Error: docs directory not found: {docs_root}", file=sys.stderr)
        return 1
    
    print(f"Scanning markdown files in: {docs_root}")
    if apply_fix:
        print("Mode: APPLY (will create .bak backups)")
    else:
        print("Mode: DRY-RUN (use --apply to fix)")
    print()
    
    md_files = find_md_files(docs_root)
    print(f"Found {len(md_files)} markdown files")
    
    files_with_issues = 0
    total_issues = 0
    
    for md_file in sorted(md_files):
        has_issues, messages = process_file(md_file, apply_fix)
        if has_issues:
            files_with_issues += 1
            for msg in messages:
                print(msg)
            # Count actual issues (exclude file path and backup messages)
            total_issues += sum(1 for m in messages if 'Line' in m)
    
    print()
    print("=" * 60)
    print(f"Summary:")
    print(f"  Files scanned: {len(md_files)}")
    print(f"  Files with issues: {files_with_issues}")
    print(f"  Total issues found: {total_issues}")
    
    if files_with_issues > 0 and not apply_fix:
        print()
        print("Run with --apply to fix these issues")
        return 1
    elif files_with_issues > 0 and apply_fix:
        print()
        print("✓ Issues fixed. Backup files created with .bak extension")
    else:
        print()
        print("✓ No issues found")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
