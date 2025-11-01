#!/usr/bin/env python3
"""
convert_mermaid_fences.py

Converts mermaid code fences (```mermaid) to MyST directive format ({mermaid}).
This ensures compatibility with Sphinx MyST parser.

Usage:
    python3 tools/convert_mermaid_fences.py              # dry-run (detect conversions)
    python3 tools/convert_mermaid_fences.py --apply      # apply conversions (creates .bak backups)
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


def find_mermaid_fences(content: str) -> List[Tuple[int, int, str]]:
    """
    Find mermaid code fences in content.
    
    Returns:
        List of (start_line, end_line, mermaid_content) tuples
    """
    fences = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for mermaid code fence start
        if line.startswith('```mermaid') or line.startswith('````mermaid'):
            start_line = i
            fence_type = '````' if line.startswith('````') else '```'
            
            # Find the closing fence
            i += 1
            mermaid_lines = []
            while i < len(lines):
                if lines[i].strip() == fence_type:
                    # Found closing fence
                    end_line = i
                    mermaid_content = '\n'.join(mermaid_lines)
                    fences.append((start_line, end_line, mermaid_content))
                    break
                else:
                    mermaid_lines.append(lines[i])
                i += 1
        
        i += 1
    
    return fences


def convert_mermaid_fence_to_directive(content: str) -> Tuple[str, int]:
    """
    Convert mermaid code fences to MyST directive format.
    
    Returns:
        (converted_content, number_of_conversions)
    """
    lines = content.split('\n')
    converted_lines = []
    conversions = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Check for mermaid code fence start
        if stripped.startswith('```mermaid') or stripped.startswith('````mermaid'):
            fence_type = '````' if stripped.startswith('````') else '```'
            indent = len(line) - len(line.lstrip())
            indent_str = ' ' * indent
            
            # Collect mermaid content
            i += 1
            mermaid_lines = []
            while i < len(lines):
                if lines[i].strip() == fence_type:
                    # Found closing fence - convert to MyST directive
                    converted_lines.append(indent_str + '```{mermaid}')
                    for mermaid_line in mermaid_lines:
                        converted_lines.append(mermaid_line)
                    converted_lines.append(indent_str + '```')
                    conversions += 1
                    i += 1
                    break
                else:
                    mermaid_lines.append(lines[i])
                    i += 1
        else:
            converted_lines.append(line)
            i += 1
    
    return '\n'.join(converted_lines), conversions


def process_file(filepath: Path, apply_fix: bool = False) -> Tuple[bool, List[str], int]:
    """
    Process a single markdown file.
    
    Returns:
        (has_fences, messages, conversion_count)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return False, [f"Error reading {filepath}: {e}"], 0
    
    fences = find_mermaid_fences(content)
    
    if not fences:
        return False, [], 0
    
    messages = [f"\n{filepath}:"]
    messages.append(f"  Found {len(fences)} mermaid code fence(s)")
    
    if apply_fix:
        # Create backup
        backup_path = filepath.with_suffix(filepath.suffix + '.bak')
        shutil.copy2(filepath, backup_path)
        messages.append(f"  Created backup: {backup_path}")
        
        # Apply conversion
        converted_content, conversions = convert_mermaid_fence_to_directive(content)
        filepath.write_text(converted_content, encoding='utf-8')
        messages.append(f"  ✓ Converted {conversions} fence(s) to MyST directive format")
        return True, messages, conversions
    else:
        for start, end, _ in fences:
            messages.append(f"    Lines {start + 1}-{end + 1}: mermaid fence")
        return True, messages, len(fences)


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
        print("Mode: DRY-RUN (use --apply to convert)")
    print()
    
    md_files = find_md_files(docs_root)
    print(f"Found {len(md_files)} markdown files")
    
    files_with_fences = 0
    total_conversions = 0
    
    for md_file in sorted(md_files):
        has_fences, messages, conversions = process_file(md_file, apply_fix)
        if has_fences:
            files_with_fences += 1
            total_conversions += conversions
            for msg in messages:
                print(msg)
    
    print()
    print("=" * 60)
    print(f"Summary:")
    print(f"  Files scanned: {len(md_files)}")
    print(f"  Files with mermaid fences: {files_with_fences}")
    print(f"  Total fences {'converted' if apply_fix else 'found'}: {total_conversions}")
    
    if files_with_fences > 0 and not apply_fix:
        print()
        print("Run with --apply to convert these fences to MyST directive format")
        return 0  # Not an error, just informational
    elif files_with_fences > 0 and apply_fix:
        print()
        print("✓ Fences converted. Backup files created with .bak extension")
    else:
        print()
        print("✓ No mermaid code fences found")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
