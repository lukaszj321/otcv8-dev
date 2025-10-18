#!/usr/bin/env python3
"""
Mermaid Lint & Fixer
Fixes common Mermaid syntax issues:
- Removes click directives from sequenceDiagram (unsupported)
- Removes stray backticks
- Adds init block if missing (optional)
"""

import re
import sys
from pathlib import Path
from typing import Tuple


def fix_mermaid_block(block_content: str) -> Tuple[str, bool, str]:
    """
    Fix a single mermaid block.
    
    Returns:
        (fixed_content, was_modified, reason)
    """
    original = block_content
    modified = False
    reasons = []
    
    # Fix 1: Remove click from sequenceDiagram
    if 'sequenceDiagram' in block_content and 'click' in block_content:
        lines = block_content.split('\n')
        new_lines = []
        for line in lines:
            # Remove or comment out click lines in sequence diagrams
            if 'click' in line and not line.strip().startswith('%'):
                # Comment it out instead of removing completely
                new_lines.append('    %% ' + line.strip() + ' %% REMOVED: click not supported in sequenceDiagram')
                modified = True
                reasons.append('removed_sequence_click')
            else:
                new_lines.append(line)
        block_content = '\n'.join(new_lines)
    
    # Fix 2: Remove stray backticks (shouldn't be in mermaid blocks)
    if '```' in block_content:
        # This is likely an error - remove them
        block_content = block_content.replace('```', '')
        modified = True
        reasons.append('removed_stray_backticks')
    
    return block_content, modified, ', '.join(reasons) if reasons else ''


def fix_mermaid_in_md(filepath: Path) -> Tuple[bool, int, str]:
    """
    Fix mermaid blocks in a markdown file.
    
    Returns:
        (modified, blocks_fixed, reasons)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Find and fix all mermaid blocks
        blocks_fixed = 0
        reasons = []
        
        def replace_block(match):
            nonlocal blocks_fixed, reasons
            block_content = match.group(1)
            fixed_content, was_modified, reason = fix_mermaid_block(block_content)
            if was_modified:
                blocks_fixed += 1
                if reason:
                    reasons.append(reason)
            return f'```mermaid\n{fixed_content}\n```'
        
        new_content = re.sub(r'```mermaid\n([\s\S]*?)\n```', replace_block, content)
        
        if blocks_fixed > 0:
            filepath.write_text(new_content, encoding='utf-8')
            return True, blocks_fixed, '; '.join(set(reasons))
        
        return False, 0, ''
        
    except Exception as e:
        return False, 0, f"error: {e}"


def fix_mermaid_in_mmd(filepath: Path) -> Tuple[bool, str]:
    """
    Fix mermaid syntax in .mmd file.
    
    Returns:
        (modified, reason)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        fixed_content, was_modified, reason = fix_mermaid_block(content)
        
        if was_modified:
            filepath.write_text(fixed_content, encoding='utf-8')
            return True, reason
        
        return False, ''
        
    except Exception as e:
        return False, f"error: {e}"


def main():
    """Main entry point."""
    base_path = Path('docs/authoring')
    
    if not base_path.exists():
        print(f"Error: {base_path} does not exist", file=sys.stderr)
        sys.exit(1)
    
    total_files = 0
    total_blocks = 0
    modified_files = []
    
    # Process markdown files
    for md_file in base_path.rglob('*.md'):
        # Skip _instructions and _tools
        if any(part.startswith('_') for part in md_file.parts):
            continue
        
        was_modified, blocks_fixed, reasons = fix_mermaid_in_md(md_file)
        if was_modified:
            total_files += 1
            total_blocks += blocks_fixed
            rel_path = md_file.relative_to(base_path)
            modified_files.append((str(rel_path), blocks_fixed, reasons))
    
    # Process .mmd files
    for mmd_file in base_path.rglob('*.mmd'):
        # Skip _instructions and _tools
        if any(part.startswith('_') for part in mmd_file.parts):
            continue
        
        was_modified, reason = fix_mermaid_in_mmd(mmd_file)
        if was_modified:
            total_files += 1
            total_blocks += 1
            rel_path = mmd_file.relative_to(base_path)
            modified_files.append((str(rel_path), 1, reason))
    
    # Print summary
    print(f"Mermaid Lint & Fix Complete")
    print(f"  Files modified: {total_files}")
    print(f"  Blocks fixed: {total_blocks}")
    
    if modified_files:
        print("\nModified files:")
        for filepath, blocks, reasons in modified_files:
            print(f"  - {filepath}: {blocks} block(s) - {reasons}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
