#!/usr/bin/env python3
"""
Script to fix trailing transition markers (---) in Markdown and RST files.
Reference commit: 84add321aea1031e8700b9a4db4b5025ef0b1396

This script removes trailing "---" that causes Sphinx build errors.
"""

import os
import sys
from pathlib import Path

# Known problematic files from build logs
KNOWN_PROBLEMATIC_FILES = [
    "docs/modules/structured/bot_tools/modul-game-bot-default-configs-cavebot-1.3-cavebot.md",
    "docs/modules/structured/bot_tools/modul-game-bot-default-configs-cavebot-1.3-targetbot.md",
    "docs/modules/structured/bot_tools/modul-game-bot-default-configs-vbot-4.7-cavebot.md",
    "docs/modules/structured/bot_tools/modul-game-bot-default-configs-vbot-4.7-targetbot.md",
    "docs/modules/structured/bot_tools/modul-game-bot-default-configs-vbot-4.8-cavebot.md",
    "docs/modules/structured/bot_tools/modul-game-bot-default-configs-vbot-4.8-targetbot.md",
    "docs/modules/structured/bot_tools/modul-game-bot-functions.md",
    "docs/modules/structured/dev_tools/modul-client-textedit.md",
    "docs/modules/structured/dev_tools/modul-corelib-ui.md",
    "docs/modules/structured/gameplay/modul-game-market.md",
]


def fix_trailing_transition(file_path: Path) -> bool:
    """
    Remove trailing '---' from a file if present.
    
    Returns:
        True if file was modified, False otherwise
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"ERROR reading {file_path}: {e}", file=sys.stderr)
        return False
    
    # Split into lines and check for trailing ---
    lines = content.splitlines(keepends=True)
    
    # Work backwards to find trailing ---
    modified = False
    while lines:
        last_line = lines[-1].rstrip('\r\n')
        
        # Check if last line is exactly "---" or only whitespace after it
        if last_line.strip() == "---":
            lines.pop()
            modified = True
        elif not last_line.strip():  # Empty line
            lines.pop()
            modified = True
        else:
            break
    
    if modified:
        # Write back without the trailing transition
        new_content = ''.join(lines)
        if new_content and not new_content.endswith('\n'):
            new_content += '\n'
        
        try:
            file_path.write_text(new_content, encoding='utf-8')
            return True
        except Exception as e:
            print(f"ERROR writing {file_path}: {e}", file=sys.stderr)
            return False
    
    return False


def find_files_with_trailing_transitions(root_dir: Path, extensions=('.md', '.rst')):
    """
    Find all files with specific extensions that end with '---'.
    
    Args:
        root_dir: Root directory to search
        extensions: Tuple of file extensions to check
    
    Yields:
        Path objects for files ending with '---'
    """
    for file_path in root_dir.rglob('*'):
        if file_path.is_file() and file_path.suffix in extensions:
            try:
                content = file_path.read_text(encoding='utf-8')
                lines = content.splitlines()
                
                # Check if file ends with --- (ignoring trailing whitespace)
                for line in reversed(lines):
                    stripped = line.strip()
                    if stripped:
                        if stripped == "---":
                            yield file_path
                        break
            except Exception:
                # Skip files we can't read
                pass


def main():
    """Main execution function."""
    repo_root = Path(__file__).parent.parent
    changed_files = []
    
    print("=== Fixing trailing transitions in documentation files ===")
    print(f"Repository root: {repo_root}")
    print()
    
    # Process known problematic files first
    print("Processing known problematic files...")
    for rel_path in KNOWN_PROBLEMATIC_FILES:
        file_path = repo_root / rel_path
        if file_path.exists():
            if fix_trailing_transition(file_path):
                changed_files.append(rel_path)
                print(f"✓ Fixed: {rel_path}")
            else:
                print(f"  Skipped (already OK): {rel_path}")
        else:
            print(f"  Not found: {rel_path}")
    
    print()
    print("Searching for other files with trailing transitions...")
    
    # Search for other problematic files
    docs_dir = repo_root / "docs"
    if docs_dir.exists():
        for file_path in find_files_with_trailing_transitions(docs_dir):
            rel_path = file_path.relative_to(repo_root)
            rel_path_str = str(rel_path)
            
            # Skip if already processed
            if rel_path_str in KNOWN_PROBLEMATIC_FILES:
                continue
            
            if fix_trailing_transition(file_path):
                changed_files.append(rel_path_str)
                print(f"✓ Fixed: {rel_path_str}")
    
    print()
    print("=== Summary ===")
    print(f"Total files fixed: {len(changed_files)}")
    
    if changed_files:
        print("\nChanged files:")
        for file in changed_files:
            print(f"  - {file}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
