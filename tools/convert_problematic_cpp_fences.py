#!/usr/bin/env python3
"""
convert_problematic_cpp_fences.py

Detects problematic ```cpp blocks containing unicode arrows, @, backslash sequences
that might break Sphinx/MyST parsing, and optionally converts them to ```text blocks.

Usage:
    python3 tools/convert_problematic_cpp_fences.py              # dry-run (detect problems)
    python3 tools/convert_problematic_cpp_fences.py --apply      # apply conversions (creates .bak backups)
"""

import sys
import re
import shutil
from pathlib import Path
from typing import List, Tuple, Dict


def find_docs_root() -> Path:
    """Find the docs directory."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    return repo_root / "docs"


def find_md_files(docs_root: Path) -> List[Path]:
    """Find all markdown files in docs directory."""
    return list(docs_root.rglob("*.md"))


def is_problematic_cpp(content: str) -> Tuple[bool, List[str]]:
    """
    Check if cpp code block contains problematic characters.
    
    Returns:
        (is_problematic, list_of_issues)
    """
    issues = []
    
    # Unicode arrows (→, ←, ↔, etc.)
    if re.search(r'[→←↔↑↓⇒⇐⇔⇑⇓➜➞➡➠]', content):
        issues.append("unicode_arrows")
    
    # Problematic @ symbols (common in Doxygen)
    if re.search(r'@\w+', content):
        issues.append("doxygen_tags")
    
    # Problematic backslash sequences that aren't standard C++ escapes
    if re.search(r'\\[^nrtabfv0\'"\\]', content):
        issues.append("unusual_backslashes")
    
    # Complex template syntax that might confuse parsers
    if content.count('<') > 5 and content.count('>') > 5:
        # Check for deeply nested templates
        depth = 0
        max_depth = 0
        for char in content:
            if char == '<':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == '>':
                depth -= 1
        if max_depth > 3:
            issues.append("deep_templates")
    
    return (len(issues) > 0, issues)


def find_cpp_fences(content: str) -> List[Dict]:
    """
    Find cpp code fences in content and check if they're problematic.
    
    Returns:
        List of dicts with fence info: {start_line, end_line, content, is_problematic, issues}
    """
    fences = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for cpp code fence start
        if line.startswith('```cpp') or line.startswith('````cpp'):
            start_line = i
            fence_type = '````' if line.startswith('````') else '```'
            fence_content_lines = []
            i += 1
            
            # Find the closing fence
            while i < len(lines):
                if lines[i].strip().startswith(fence_type) and not lines[i].strip().startswith(fence_type + fence_type[0]):
                    # Found closing fence
                    fence_content = '\n'.join(fence_content_lines)
                    is_prob, issues = is_problematic_cpp(fence_content)
                    
                    if is_prob:
                        fences.append({
                            'start_line': start_line,
                            'end_line': i,
                            'content': fence_content,
                            'fence_type': fence_type,
                            'is_problematic': True,
                            'issues': issues
                        })
                    break
                else:
                    fence_content_lines.append(lines[i])
                i += 1
        
        i += 1
    
    return fences


def convert_problematic_fences(content: str, fences: List[Dict]) -> str:
    """Convert problematic cpp fences to text fences."""
    lines = content.split('\n')
    
    # Process in reverse order to maintain line numbers
    for fence in reversed(fences):
        start = fence['start_line']
        end = fence['end_line']
        fence_type = fence['fence_type']
        
        # Replace opening fence marker
        lines[start] = lines[start].replace(f'{fence_type}cpp', f'{fence_type}text')
    
    return '\n'.join(lines)


def process_file(file_path: Path, apply: bool = False) -> Tuple[int, List[str]]:
    """
    Process a single file.
    
    Returns:
        (num_problematic_fences, list_of_issue_types)
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f"⚠️  Skipping {file_path} (encoding issue)")
        return 0, []
    
    fences = find_cpp_fences(content)
    
    if not fences:
        return 0, []
    
    # Collect unique issue types
    all_issues = set()
    for fence in fences:
        all_issues.update(fence['issues'])
    
    print(f"\n📄 {file_path.relative_to(find_docs_root())}")
    print(f"   Found {len(fences)} problematic cpp fence(s)")
    for fence in fences:
        print(f"   - Lines {fence['start_line']+1}-{fence['end_line']+1}: {', '.join(fence['issues'])}")
    
    if apply:
        # Create backup
        backup_path = file_path.with_suffix(file_path.suffix + '.bak')
        shutil.copy2(file_path, backup_path)
        
        # Convert fences
        new_content = convert_problematic_fences(content, fences)
        file_path.write_text(new_content, encoding='utf-8')
        
        print(f"   ✅ Converted and backed up to {backup_path.name}")
    
    return len(fences), list(all_issues)


def main():
    apply = '--apply' in sys.argv
    
    print("=" * 60)
    print("Convert Problematic C++ Fences")
    print("=" * 60)
    print(f"Mode: {'APPLY (with backups)' if apply else 'DRY RUN'}")
    print()
    
    docs_root = find_docs_root()
    if not docs_root.exists():
        print(f"❌ Docs directory not found: {docs_root}")
        sys.exit(1)
    
    md_files = find_md_files(docs_root)
    print(f"Scanning {len(md_files)} markdown files...\n")
    
    total_fences = 0
    total_files = 0
    all_issue_types = set()
    
    for md_file in md_files:
        num_fences, issues = process_file(md_file, apply)
        if num_fences > 0:
            total_fences += num_fences
            total_files += 1
            all_issue_types.update(issues)
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Files with problematic cpp fences: {total_files}")
    print(f"Total problematic fences: {total_fences}")
    if all_issue_types:
        print(f"Issue types found: {', '.join(sorted(all_issue_types))}")
    
    if not apply and total_fences > 0:
        print("\n💡 Run with --apply to convert problematic fences (creates .bak files)")
    elif apply and total_fences > 0:
        print("\n✅ Conversions complete! Backup files (.bak) created.")
    else:
        print("\n✅ No problematic cpp fences found!")
    
    return 0 if total_fences == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
