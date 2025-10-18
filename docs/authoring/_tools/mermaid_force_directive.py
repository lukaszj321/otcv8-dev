#!/usr/bin/env python3
"""
Mermaid Force Directive Converter (idempotent)
Converts ```mermaid to ```{mermaid} in all markdown files.
Skips files that already have the correct syntax.
"""

import re
from pathlib import Path

# Repository root
REPO_ROOT = Path(__file__).resolve().parents[3]
AUTHORING_DIR = REPO_ROOT / "docs" / "authoring"

def convert_mermaid_fences(content: str) -> tuple[str, int]:
    """
    Convert ```mermaid to ```{mermaid}
    Returns: (converted_content, change_count)
    """
    # Pattern to match ```mermaid (without braces) at start of line
    # But NOT ```{mermaid} (already correct)
    pattern = r'^(```)(mermaid)(\s*)$'
    
    changes = 0
    lines = content.split('\n')
    result_lines = []
    
    for line in lines:
        # Check if this is a fence opener
        match = re.match(pattern, line)
        if match and '{mermaid}' not in line:
            # Convert to directive syntax
            result_lines.append('```{mermaid}')
            changes += 1
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines), changes

def process_file(filepath: Path) -> bool:
    """Process a single markdown file. Returns True if changes were made."""
    try:
        content = filepath.read_text(encoding='utf-8')
        new_content, changes = convert_mermaid_fences(content)
        
        if changes > 0:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"✓ {filepath.relative_to(REPO_ROOT)}: {changes} fence(s) converted")
            return True
        return False
    except Exception as e:
        print(f"✗ {filepath.relative_to(REPO_ROOT)}: {e}")
        return False

def main():
    """Main entry point"""
    print("Mermaid Force Directive Converter")
    print("=" * 60)
    print(f"Scanning: {AUTHORING_DIR}")
    print()
    
    # Find all markdown files in authoring directory
    md_files = list(AUTHORING_DIR.rglob("*.md"))
    
    if not md_files:
        print("No markdown files found.")
        return
    
    print(f"Found {len(md_files)} markdown files")
    print()
    
    total_changed = 0
    for md_file in md_files:
        if process_file(md_file):
            total_changed += 1
    
    print()
    print("=" * 60)
    print(f"Summary: {total_changed} file(s) modified")
    
    if total_changed == 0:
        print("✓ All files already use correct syntax!")

if __name__ == "__main__":
    main()
