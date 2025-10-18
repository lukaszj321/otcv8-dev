#!/usr/bin/env python3
"""
Diagram Lint & Fix Tool for OTClient v8 Documentation

Fixes common Mermaid diagram issues:
1. Adds init header if missing
2. Removes stray backticks inside blocks
3. Extracts blocks from quotes
4. Ensures proper formatting

Generates: docs/authoring/qa/diagram_lint.csv
"""

import re
import csv
from pathlib import Path
from typing import List, Tuple

INIT_HEADER = "%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%"

def fix_mmd_file(path: Path) -> Tuple[bool, str]:
    """Fix a .mmd file by ensuring it has the init header."""
    try:
        content = path.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
        
        # Check if first line already has init
        if lines and '%%{init:' in lines[0]:
            return (False, 'Already has init header')
        
        # Add init header at the beginning
        fixed_content = INIT_HEADER + '\n' + content
        path.write_text(fixed_content, encoding='utf-8')
        return (True, 'Added init header')
    except Exception as e:
        return (False, f'Error: {str(e)}')

def fix_mermaid_blocks_in_md(path: Path) -> List[Tuple[int, str, str]]:
    """Fix Mermaid blocks in markdown files."""
    try:
        content = path.read_text(encoding='utf-8', errors='ignore')
        original_content = content
        fixes = []
        
        # Find all mermaid blocks
        pattern = r'```mermaid\n([\s\S]*?)\n```'
        matches = list(re.finditer(pattern, content))
        
        for idx, match in enumerate(matches):
            block_content = match.group(1)
            block_start = match.start()
            fixed = False
            actions = []
            
            # Check for init header
            has_init = '%%{init:' in block_content
            if not has_init:
                # Add init header
                block_content = INIT_HEADER + '\n' + block_content
                fixed = True
                actions.append('added_init')
            
            # Check for stray backticks
            if '```' in block_content:
                # Remove stray backticks
                block_content = block_content.replace('```', '')
                fixed = True
                actions.append('removed_stray_backticks')
            
            if fixed:
                # Replace the block
                new_block = f'```mermaid\n{block_content}\n```'
                content = content[:match.start()] + new_block + content[match.end():]
                # Adjust for length change
                offset = len(new_block) - len(match.group(0))
                for future_match in matches[idx+1:]:
                    future_match.regs = tuple((start + offset, end + offset) for start, end in future_match.regs)
                
                line_num = original_content[:block_start].count('\n') + 1
                fixes.append((line_num, ', '.join(actions), 'FIXED'))
        
        if content != original_content:
            path.write_text(content, encoding='utf-8')
        
        return fixes
    except Exception as e:
        return [(0, f'Error: {str(e)}', 'ERROR')]

def main():
    """Main entry point."""
    base_path = Path('docs/authoring')
    if not base_path.exists():
        print(f"Error: {base_path} does not exist")
        return 1
    
    results = []
    
    # Fix .mmd files
    print("Fixing .mmd files...")
    for mmd_file in base_path.rglob('*.mmd'):
        rel_path = mmd_file.relative_to(base_path)
        fixed, action = fix_mmd_file(mmd_file)
        status = 'FIXED' if fixed else 'OK'
        results.append([str(rel_path), 1, status, action])
        if fixed:
            print(f"  Fixed: {rel_path}")
    
    # Fix embedded mermaid blocks in .md files
    print("\nFixing embedded Mermaid blocks in .md files...")
    for md_file in base_path.rglob('*.md'):
        rel_path = md_file.relative_to(base_path)
        fixes = fix_mermaid_blocks_in_md(md_file)
        if fixes:
            for line_num, action, status in fixes:
                results.append([str(rel_path), line_num, status, action])
                if status == 'FIXED':
                    print(f"  Fixed: {rel_path}:{line_num} - {action}")
    
    # Write report
    qa_dir = base_path / 'qa'
    qa_dir.mkdir(parents=True, exist_ok=True)
    
    report_path = qa_dir / 'diagram_lint.csv'
    with open(report_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['file', 'line', 'status', 'problem'])
        writer.writerows(results)
    
    print(f"\nReport written to: {report_path}")
    print(f"Total fixes: {sum(1 for r in results if r[2] == 'FIXED')}")
    print(f"Total OK: {sum(1 for r in results if r[2] == 'OK')}")
    print(f"Total errors: {sum(1 for r in results if r[2] == 'ERROR')}")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
