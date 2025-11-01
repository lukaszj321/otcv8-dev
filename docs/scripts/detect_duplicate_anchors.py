#!/usr/bin/env python3
"""
detect_duplicate_anchors.py

Scans docs/copilot/sphinx/anchors.rst for duplicate explicit targets and prints duplicates.

Usage:
    python3 docs/scripts/detect_duplicate_anchors.py
"""

import sys
from pathlib import Path
from collections import defaultdict


def find_anchors_file() -> Path:
    """Find the anchors.rst file."""
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent
    anchors_file = docs_dir / "copilot" / "sphinx" / "anchors.rst"
    
    # Fallback to current working directory
    if not anchors_file.exists():
        anchors_file = Path.cwd() / "docs" / "copilot" / "sphinx" / "anchors.rst"
    
    return anchors_file


def parse_anchors(file_path: Path) -> dict:
    """
    Parse anchors.rst file and extract explicit targets.
    
    Returns:
        dict mapping anchor_name -> list of line numbers where it appears
    """
    if not file_path.exists():
        return {}
    
    anchors = defaultdict(list)
    
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, start=1):
            # Match explicit target pattern: .. _anchor-name:
            if line.strip().startswith('.. _') and line.strip().endswith(':'):
                # Extract anchor name
                anchor_name = line.strip()[4:-1].strip()
                if anchor_name:
                    anchors[anchor_name].append(line_num)
        
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return {}
    
    return anchors


def main():
    anchors_file = find_anchors_file()
    
    if not anchors_file.exists():
        print(f"Error: anchors.rst not found at: {anchors_file}", file=sys.stderr)
        print("Expected location: docs/copilot/sphinx/anchors.rst", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning: {anchors_file}\n")
    
    anchors = parse_anchors(anchors_file)
    
    # Find duplicates
    duplicates = {name: lines for name, lines in anchors.items() if len(lines) > 1}
    
    if not duplicates:
        print("No duplicate anchors found! ✓")
        sys.exit(0)
    
    # Print report
    print("="*70)
    print("DUPLICATE ANCHORS REPORT")
    print("="*70 + "\n")
    
    for anchor_name in sorted(duplicates.keys()):
        line_nums = duplicates[anchor_name]
        print(f"Anchor: '{anchor_name}'")
        print(f"  Found at lines: {', '.join(map(str, line_nums))}")
        print(f"  Occurrences: {len(line_nums)}")
        print()
    
    print(f"Total duplicate anchors: {len(duplicates)}")
    print(f"Total duplicate entries: {sum(len(lines) - 1 for lines in duplicates.values())}")
    print("\n" + "="*70)
    print("\nRun dedupe_anchors.py to automatically remove duplicates.")


if __name__ == '__main__':
    main()
