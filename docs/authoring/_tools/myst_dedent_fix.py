#!/usr/bin/env python3
"""
MyST Directive Dedent Fixer
Fixes indented MyST directives (```{mermaid}, ```{csv-table}, etc.) 
so they render properly in Sphinx instead of appearing as literal text.

Fixes:
1. Dedents directive openers (```{mermaid}, etc.) to column 0
2. Dedents directive closers (```) to column 0
3. Dedents *Facet:* lines to column 0
4. Ensures blank line before directives
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple


def process_file(filepath: Path) -> Tuple[bool, int]:
    """
    Process a single markdown file to fix indentation issues.
    
    Returns:
        (modified, fixes_applied)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        lines = content.splitlines(keepends=True)
        
        modified = False
        fixes = 0
        new_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            original_line = line
            
            # Fix 1: Dedent *Facet:* lines
            if re.match(r'^\s+\*Facet:\*', line):
                dedented = line.lstrip()
                if dedented != line:
                    line = dedented
                    modified = True
                    fixes += 1
            
            # Fix 2: Dedent directive openers and ensure blank line before
            elif re.match(r'^\s+```{(mermaid|csv-table)', line):
                dedented = line.lstrip()
                if dedented != line:
                    # Check if previous line is blank
                    if new_lines and new_lines[-1].strip():
                        new_lines.append('\n')
                        fixes += 1
                    line = dedented
                    modified = True
                    fixes += 1
            
            # Fix 3: Dedent directive closers (only if they match indented pattern)
            elif re.match(r'^\s+```\s*$', line):
                # Only dedent if it's actually indented (not just column 0)
                if line[0] in (' ', '\t'):
                    dedented = line.lstrip()
                    line = dedented if dedented else '```\n'
                    modified = True
                    fixes += 1
            
            new_lines.append(line)
            i += 1
        
        if modified:
            # Write back
            new_content = ''.join(new_lines)
            filepath.write_text(new_content, encoding='utf-8')
            return True, fixes
        
        return False, 0
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}", file=sys.stderr)
        return False, 0


def main():
    """Main entry point."""
    base_path = Path('docs/authoring')
    
    if not base_path.exists():
        print(f"Error: {base_path} does not exist", file=sys.stderr)
        sys.exit(1)
    
    total_files = 0
    total_fixes = 0
    modified_files = []
    
    # Process all markdown files in docs/authoring
    for md_file in base_path.rglob('*.md'):
        # Skip _instructions directory
        if '_instructions' in str(md_file):
            continue
        
        was_modified, fixes = process_file(md_file)
        if was_modified:
            total_files += 1
            total_fixes += fixes
            rel_path = md_file.relative_to(base_path)
            modified_files.append((str(rel_path), fixes))
    
    # Print summary
    print(f"MyST Dedent Fix Complete")
    print(f"  Files modified: {total_files}")
    print(f"  Total fixes: {total_fixes}")
    
    if modified_files:
        print("\nModified files:")
        for filepath, fixes in modified_files:
            print(f"  - {filepath}: {fixes} fixes")
    
    return 0 if total_files == 0 else 0


if __name__ == '__main__':
    sys.exit(main())
