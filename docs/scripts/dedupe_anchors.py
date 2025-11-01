#!/usr/bin/env python3
"""
dedupe_anchors.py

Deduplicates explicit targets in docs/copilot/sphinx/anchors.rst.
Dry-run by default, --apply to write changes and create anchors.rst.bak.

Usage:
    python3 docs/scripts/dedupe_anchors.py           # dry-run (show what would change)
    python3 docs/scripts/dedupe_anchors.py --apply   # apply changes and create backup
"""

import sys
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def find_anchors_file() -> Path:
    """Find the anchors.rst file."""
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent
    anchors_file = docs_dir / "copilot" / "sphinx" / "anchors.rst"
    
    # Fallback to current working directory
    if not anchors_file.exists():
        anchors_file = Path.cwd() / "docs" / "copilot" / "sphinx" / "anchors.rst"
    
    return anchors_file


def parse_and_dedupe(content: str) -> tuple[str, dict]:
    """
    Parse content and remove duplicate anchors, keeping only the first occurrence.
    
    Returns:
        (deduplicated_content, stats_dict)
    """
    lines = content.split('\n')
    seen_anchors = set()
    output_lines = []
    stats = defaultdict(int)
    removed_lines = []
    
    for line_num, line in enumerate(lines, start=1):
        # Check if this is an explicit target
        if line.strip().startswith('.. _') and line.strip().endswith(':'):
            anchor_name = line.strip()[4:-1].strip()
            
            if anchor_name in seen_anchors:
                # Duplicate - skip this line
                stats['duplicates_removed'] += 1
                removed_lines.append((line_num, anchor_name, line))
                continue
            else:
                # First occurrence - keep it
                seen_anchors.add(anchor_name)
                stats['unique_anchors'] += 1
        
        output_lines.append(line)
    
    stats['total_lines_original'] = len(lines)
    stats['total_lines_deduplicated'] = len(output_lines)
    stats['removed_lines'] = removed_lines
    
    return '\n'.join(output_lines), stats


def main():
    apply = '--apply' in sys.argv
    
    anchors_file = find_anchors_file()
    
    if not anchors_file.exists():
        print(f"Error: anchors.rst not found at: {anchors_file}", file=sys.stderr)
        print("Expected location: docs/copilot/sphinx/anchors.rst", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing: {anchors_file}\n")
    
    # Read original content
    try:
        original_content = anchors_file.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Deduplicate
    deduplicated_content, stats = parse_and_dedupe(original_content)
    
    # Print report
    print("="*70)
    print("DEDUPLICATION REPORT")
    print("="*70 + "\n")
    
    print(f"Original lines: {stats['total_lines_original']}")
    print(f"Deduplicated lines: {stats['total_lines_deduplicated']}")
    print(f"Unique anchors kept: {stats['unique_anchors']}")
    print(f"Duplicate anchors removed: {stats['duplicates_removed']}")
    
    if stats['removed_lines']:
        print("\nRemoved duplicates:")
        for line_num, anchor_name, line in stats['removed_lines']:
            print(f"  Line {line_num}: {anchor_name}")
    else:
        print("\nNo duplicates found! ✓")
    
    print("\n" + "="*70)
    
    if stats['duplicates_removed'] == 0:
        print("\nNothing to do.")
        return
    
    if not apply:
        print("\n=== DRY RUN ===")
        print("Run with --apply to apply changes and create backup.")
        return
    
    # Apply changes
    print("\n=== Applying changes ===")
    
    # Create backup
    backup_file = anchors_file.with_suffix('.rst.bak')
    try:
        shutil.copy2(anchors_file, backup_file)
        print(f"Backup created: {backup_file}")
    except Exception as e:
        print(f"Error creating backup: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Write deduplicated content
    try:
        anchors_file.write_text(deduplicated_content, encoding='utf-8')
        print(f"Updated: {anchors_file}")
        print(f"\n✓ Successfully removed {stats['duplicates_removed']} duplicate anchor(s)")
    except Exception as e:
        print(f"Error writing file: {e}", file=sys.stderr)
        # Try to restore backup
        try:
            shutil.copy2(backup_file, anchors_file)
            print("Restored from backup due to error.", file=sys.stderr)
        except:
            pass
        sys.exit(1)


if __name__ == '__main__':
    main()
