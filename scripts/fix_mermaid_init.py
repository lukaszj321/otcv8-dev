#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Mermaid Init Blocks
Add proper init blocks to all Mermaid diagrams that are missing them.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AUTHORING = DOCS / "authoring"

MERMAID_INIT = "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%"

def fix_mermaid_file(mmd_path: Path):
    """Add init block if missing."""
    content = mmd_path.read_text(encoding='utf-8').strip()
    
    if content.startswith("%%{init:"):
        return False  # Already has init
    
    new_content = MERMAID_INIT + "\n" + content + "\n"
    mmd_path.write_text(new_content, encoding='utf-8')
    return True

def main():
    """Main execution."""
    print("Fixing Mermaid init blocks...")
    
    fixed_count = 0
    total_count = 0
    
    for mmd_file in AUTHORING.rglob("*.mmd"):
        if mmd_file.parent.name == "diagrams" or "diagram" in mmd_file.parent.name:
            total_count += 1
            if fix_mermaid_file(mmd_file):
                print(f"  [FIXED] {mmd_file.relative_to(ROOT)}")
                fixed_count += 1
    
    print(f"\nFixed {fixed_count} out of {total_count} Mermaid files.")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
