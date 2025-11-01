#!/usr/bin/env python3
"""
convert_problematic_cpp_fences.py

Detects and converts problematic ```cpp fences that contain:
- Unicode arrow characters (→)
- @ tags (Doxygen/JavaDoc style)
- Backslash/tab sequences that break rendering

Converts offending fences to ```text on --apply.

Usage:
    python3 tools/convert_problematic_cpp_fences.py              # dry-run (detect issues)
    python3 tools/convert_problematic_cpp_fences.py --apply      # apply fixes (creates .bak backups)
"""

import sys
import re
import shutil
from pathlib import Path
from typing import List, Tuple, Optional


def find_docs_root() -> Path:
    """Find the docs directory."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    return repo_root / "docs"


def find_md_files(docs_root: Path) -> List[Path]:
    """Find all markdown files in docs directory."""
    return list(docs_root.rglob("*.md"))


def has_problematic_content(content: str) -> Tuple[bool, List[str]]:
    """
    Check if fence content has problematic characters/patterns.
    
    Returns:
        (is_problematic, list_of_reasons)
    """
    reasons = []
    
    # Check for unicode arrow
    if '→' in content:
        reasons.append("contains unicode arrow (→)")
    
    # Check for @ tags (common in Doxygen/JavaDoc)
    if re.search(r'@\w+', content):
        reasons.append("contains @ tags")
    
    # Check for problematic backslash sequences
    if re.search(r'\\\w', content):
        reasons.append("contains backslash sequences")
    
    # Check for tab characters in code
    if '\t' in content:
        reasons.append("contains tab characters")
    
    return (len(reasons) > 0, reasons)


def find_cpp_fences(content: str) -> List[Tuple[int, int, str, List[str]]]:
    """
    Find ```cpp code fences and check if they're problematic.
    
    Returns:
        List of (start_line, end_line, fence_content, reasons) tuples for problematic fences
    """
    problematic = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for cpp code fence start
        if re.match(r'^```+cpp\s*$', line.strip()):
            start_line = i
            fence_type = re.match(r'^(```+)cpp', line.strip()).group(1)
            fence_content = []
            i += 1
            
            # Collect fence content until closing
            while i < len(lines):
                if lines[i].strip() == fence_type:
                    # Found closing fence
                    full_content = '\n'.join(fence_content)
                    is_prob, reasons = has_problematic_content(full_content)
                    
                    if is_prob:
                        problematic.append((start_line, i, full_content, reasons))
                    break
                fence_content.append(lines[i])
                i += 1
        
        i += 1
    
    return problematic


def convert_cpp_to_text(content: str, problematic_fences: List[Tuple[int, int, str, List[str]]]) -> str:
    """
    Convert problematic ```cpp fences to ```text.
    """
    if not problematic_fences:
        return content
    
    lines = content.split('\n')
    
    # Process fences in reverse order to maintain line numbers
    for start_line, end_line, fence_content, reasons in reversed(problematic_fences):
        # Replace ```cpp with ```text
        lines[start_line] = lines[start_line].replace('```cpp', '```text')
    
    return '\n'.join(lines)


def process_file(filepath: Path, apply_fix: bool = False) -> Tuple[int, List[str]]:
    """
    Process a single markdown file.
    
    Returns:
        (number_of_issues, list_of_issue_descriptions)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        return 0, []
    
    problematic = find_cpp_fences(content)
    
    if not problematic:
        return 0, []
    
    issues = []
    for start_line, end_line, fence_content, reasons in problematic:
        reason_str = ", ".join(reasons)
        issues.append(f"  Lines {start_line+1}-{end_line+1}: {reason_str}")
    
    if apply_fix:
        # Create backup
        backup_path = filepath.with_suffix(filepath.suffix + '.bak')
        shutil.copy2(filepath, backup_path)
        
        # Apply conversion
        fixed_content = convert_cpp_to_text(content, problematic)
        filepath.write_text(fixed_content, encoding='utf-8')
        print(f"✓ Fixed {filepath} (backup: {backup_path.name})")
    
    return len(problematic), issues


def main():
    apply_fix = '--apply' in sys.argv
    
    docs_root = find_docs_root()
    if not docs_root.exists():
        print(f"Error: docs directory not found at {docs_root}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning markdown files in {docs_root}")
    md_files = find_md_files(docs_root)
    print(f"Found {len(md_files)} markdown files")
    
    if apply_fix:
        print("\n⚠️  APPLY MODE: Will convert problematic ```cpp fences to ```text")
        print("Creating .bak backups for modified files\n")
    else:
        print("\n🔍 DRY-RUN MODE: Detecting problematic fences (use --apply to fix)\n")
    
    total_issues = 0
    files_with_issues = 0
    
    for filepath in sorted(md_files):
        num_issues, issue_list = process_file(filepath, apply_fix)
        
        if num_issues > 0:
            files_with_issues += 1
            total_issues += num_issues
            rel_path = filepath.relative_to(docs_root.parent)
            print(f"\n{rel_path}:")
            for issue in issue_list:
                print(issue)
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files with problematic cpp fences: {files_with_issues}")
    print(f"  Total problematic fences: {total_issues}")
    
    if not apply_fix and total_issues > 0:
        print(f"\nRun with --apply to convert problematic ```cpp fences to ```text")
    elif apply_fix and total_issues > 0:
        print(f"\n✓ All problematic fences converted (backups created with .bak extension)")
    
    return 0 if total_issues == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
