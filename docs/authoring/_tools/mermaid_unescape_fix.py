#!/usr/bin/env python3
"""
Mermaid Unescape Fixer
Removes literal escape sequences (\n, \", etc.) from Mermaid blocks
that should be actual newlines and quotes.

This fixes the issue where Mermaid diagrams contain literal text like:
  \nclick LoggingFlow "./index.html#facet-09_logging.logging_flow" "Open logging_flow"\n

Should become actual newlines before/after the click directive.
"""

import re
import sys
from pathlib import Path
from typing import Tuple


def unescape_mermaid_content(content: str) -> Tuple[str, bool]:
    """
    Unescape literal escape sequences in Mermaid content.
    
    Returns:
        (unescaped_content, was_modified)
    """
    original = content
    
    # Fix literal \n sequences (but preserve them in actual strings)
    # Pattern: match \n at end of lines or standalone on lines
    # This is the pattern we see: ...something\n
    # We want to convert: \n at the end of line to actual newline
    
    # First, handle trailing \n patterns (literal backslash-n at end of line)
    content = re.sub(r'\\n\s*$', '', content, flags=re.MULTILINE)
    
    # Handle leading \n patterns (literal backslash-n at start of line)
    content = re.sub(r'^\s*\\n', '', content, flags=re.MULTILINE)
    
    # Fix literal \" to actual quotes (but be careful not to break strings)
    content = content.replace('\\"', '"')
    
    # Remove any double blank lines that might have been created
    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')
    
    return content, content != original


def fix_mermaid_file(filepath: Path) -> Tuple[bool, str]:
    """
    Fix escape sequences in a .mmd file.
    
    Returns:
        (modified, reason)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Check if file has escape issues
        if '\\n' not in content and '\\"' not in content:
            return False, 'no_escapes'
        
        fixed_content, was_modified = unescape_mermaid_content(content)
        
        if was_modified:
            filepath.write_text(fixed_content, encoding='utf-8')
            return True, 'unescaped'
        
        return False, 'no_changes'
        
    except Exception as e:
        return False, f"error: {e}"


def fix_mermaid_in_md(filepath: Path) -> Tuple[bool, int, str]:
    """
    Fix mermaid blocks in markdown files.
    
    Returns:
        (modified, blocks_fixed, reasons)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        
        # Find all mermaid blocks (both {mermaid} and ```mermaid forms)
        blocks_fixed = 0
        reasons = []
        
        def replace_block(match):
            nonlocal blocks_fixed, reasons
            header = match.group(1)
            block_content = match.group(2)
            closer = match.group(3)

            # If :file: is present in the header or block, skip unescape
            if ":file:" in header or ":file:" in block_content:
                return match.group(0)

            if '\\n' in block_content or '\\"' in block_content:
                fixed_content, was_modified = unescape_mermaid_content(block_content)
                if was_modified:
                    blocks_fixed += 1
                    reasons.append('unescaped')
                return f'{header}{fixed_content}{closer}'
            return match.group(0)

        # Handle both ```mermaid and directive-style fences, preserving header/options
        pattern = r'(```\{?mermaid[^\n]*\n)([\s\S]*?)(\n```)'  # header, body, closer
        new_content = re.sub(pattern, replace_block, content)
        
        if blocks_fixed > 0:
            filepath.write_text(new_content, encoding='utf-8')
            return True, blocks_fixed, '; '.join(set(reasons))
        
        return False, 0, ''
        
    except Exception as e:
        return False, 0, f"error: {e}"


def main():
    """Main entry point."""
    base_path = Path('docs/authoring')
    
    if not base_path.exists():
        print(f"Error: {base_path} does not exist", file=sys.stderr)
        sys.exit(1)
    
    total_files = 0
    total_blocks = 0
    modified_files = []
    
    # Process .mmd files
    for mmd_file in base_path.rglob('*.mmd'):
        # Skip _instructions and _tools
        if any(part.startswith('_') for part in mmd_file.parts):
            continue
        
        was_modified, reason = fix_mermaid_file(mmd_file)
        if was_modified:
            total_files += 1
            total_blocks += 1
            rel_path = mmd_file.relative_to(base_path)
            modified_files.append((str(rel_path), 1, reason))
    
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
    
    # Print summary
    print(f"Mermaid Unescape Fix Complete")
    print(f"  Files modified: {total_files}")
    print(f"  Blocks fixed: {total_blocks}")
    
    if modified_files:
        print("\nModified files:")
        for filepath, blocks, reasons in modified_files[:30]:  # Show first 30
            print(f"  - {filepath}: {blocks} block(s) - {reasons}")
        if len(modified_files) > 30:
            print(f"  ... and {len(modified_files) - 30} more")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
