#!/usr/bin/env python3
"""
Fix malformed MyST/sphinx-design tab directives across the repository.

This script addresses common tab formatting issues:
1. Missing blank lines after ```{tab} Label headers
2. Empty tab bodies (adds placeholder content)
3. Improper code fence nesting inside tabs
4. Normalizes backtick usage (````{tabs} to ```{tabs})

Usage:
    python scripts/fix_myst_tabs.py [--dry-run] [--verbose]
    
Options:
    --dry-run    Show what would be changed without modifying files
    --verbose    Print detailed change information
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Tuple
import shutil


class TabFixer:
    """Fix MyST tab directive formatting issues."""
    
    def __init__(self, dry_run: bool = False, verbose: bool = False):
        self.dry_run = dry_run
        self.verbose = verbose
        self.stats = {
            'files_scanned': 0,
            'files_modified': 0,
            'blank_lines_added': 0,
            'placeholders_added': 0,
            'code_blocks_fixed': 0,
            'backticks_normalized': 0,
        }
    
    def find_markdown_files(self, root_dir: Path) -> List[Path]:
        """Find all markdown files in the repository."""
        extensions = ['.md', '.rst', '.mkd']
        exclude_dirs = {'.git', 'node_modules', '__md_backup_*', '_build', 'build', 
                       'dist', '.cache', 'venv', '.venv'}
        
        markdown_files = []
        for ext in extensions:
            for path in root_dir.rglob(f'*{ext}'):
                # Skip excluded directories
                if any(excluded in path.parts for excluded in exclude_dirs):
                    continue
                # Skip backup files
                if path.suffix == '.bak' or '.bak' in path.suffixes:
                    continue
                markdown_files.append(path)
        
        return sorted(markdown_files)
    
    def backup_file(self, filepath: Path) -> None:
        """Create a backup of the file before modification."""
        if not self.dry_run:
            backup_path = Path(str(filepath) + '.bak')
            shutil.copy2(filepath, backup_path)
            if self.verbose:
                print(f"  Created backup: {backup_path}")
    
    def fix_tab_blank_lines(self, lines: List[str]) -> Tuple[List[str], int]:
        """Ensure blank line after each ```{tab} Label header."""
        fixed_lines = []
        changes = 0
        i = 0
        
        while i < len(lines):
            line = lines[i]
            fixed_lines.append(line)
            
            # Check if this is a tab directive line
            if re.match(r'^```{tab}\s+.+', line):
                # Check if next line exists and is not blank
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    # If next line is not blank and not a closing fence, add blank line
                    if next_line.strip() and not next_line.strip().startswith('```'):
                        fixed_lines.append('')
                        changes += 1
                        if self.verbose:
                            print(f"    Added blank line after: {line.strip()}")
                elif i + 1 >= len(lines):
                    # Tab at end of file, add blank line
                    fixed_lines.append('')
                    changes += 1
            
            i += 1
        
        return fixed_lines, changes
    
    def fix_empty_tabs(self, lines: List[str]) -> Tuple[List[str], int]:
        """Add placeholder content to empty tabs."""
        fixed_lines = []
        changes = 0
        i = 0
        
        while i < len(lines):
            line = lines[i]
            fixed_lines.append(line)
            
            # Check if this is a tab directive
            if re.match(r'^```{tab}\s+.+', line):
                # Look ahead to find the content
                j = i + 1
                
                # Skip blank lines after tab header
                while j < len(lines) and not lines[j].strip():
                    fixed_lines.append(lines[j])
                    j += 1
                
                # Check if immediately followed by closing ``` or another tab/directive
                if j < len(lines):
                    next_content = lines[j].strip()
                    if next_content.startswith('```') and not next_content.startswith('```{'):
                        # Empty tab - add placeholder
                        fixed_lines.append('TODO: add content')
                        fixed_lines.append('')
                        changes += 1
                        if self.verbose:
                            print(f"    Added placeholder to empty tab: {line.strip()}")
                    elif next_content.startswith('```{tab}') or next_content.startswith('````'):
                        # Another tab follows - this tab is empty
                        fixed_lines.append('TODO: add content')
                        fixed_lines.append('')
                        changes += 1
                        if self.verbose:
                            print(f"    Added placeholder to empty tab: {line.strip()}")
                elif j >= len(lines):
                    # Tab at EOF with no content
                    fixed_lines.append('TODO: add content')
                    changes += 1
                
                # Continue from where we left off
                i = j - 1
            
            i += 1
        
        return fixed_lines, changes
    
    def fix_nested_code_blocks(self, lines: List[str]) -> Tuple[List[str], int]:
        """Convert improperly nested code fences to MyST code-block directives."""
        fixed_lines = []
        changes = 0
        i = 0
        in_tab = False
        
        while i < len(lines):
            line = lines[i]
            
            # Track if we're inside a tab
            if re.match(r'^```{tab}\s+.+', line):
                in_tab = True
                fixed_lines.append(line)
            elif line.strip().startswith('````') and in_tab:
                # End of tabs block
                in_tab = False
                fixed_lines.append(line)
            elif in_tab and re.match(r'^```(\w+)\s*$', line):
                # Found a code fence inside a tab - convert to code-block
                lang_match = re.match(r'^```(\w+)\s*$', line)
                if lang_match:
                    lang = lang_match.group(1)
                    fixed_lines.append(f'```{{code-block}} {lang}')
                    changes += 1
                    if self.verbose:
                        print(f"    Converted code fence to code-block: {lang}")
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
            
            i += 1
        
        return fixed_lines, changes
    
    def normalize_backticks(self, lines: List[str]) -> Tuple[List[str], int]:
        """Normalize multi-backtick usage for tabs directives."""
        fixed_lines = []
        changes = 0
        
        for line in lines:
            # Convert ````{tabs} to ```{tabs}
            if re.match(r'^````\{tabs\}', line):
                fixed_lines.append(line.replace('````{tabs}', '```{tabs}'))
                changes += 1
                if self.verbose:
                    print(f"    Normalized backticks: {line.strip()}")
            # Convert ```` closing to ``` when it's at the right nesting level
            # This is tricky - we need to track nesting, so we'll be conservative
            else:
                fixed_lines.append(line)
        
        return fixed_lines, changes
    
    def fix_file(self, filepath: Path) -> bool:
        """Fix all tab issues in a single file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            
            # Apply all fixes
            lines, blank_changes = self.fix_tab_blank_lines(lines)
            lines, placeholder_changes = self.fix_empty_tabs(lines)
            lines, code_changes = self.fix_nested_code_blocks(lines)
            lines, backtick_changes = self.normalize_backticks(lines)
            
            total_changes = blank_changes + placeholder_changes + code_changes + backtick_changes
            
            if total_changes > 0:
                self.stats['files_modified'] += 1
                self.stats['blank_lines_added'] += blank_changes
                self.stats['placeholders_added'] += placeholder_changes
                self.stats['code_blocks_fixed'] += code_changes
                self.stats['backticks_normalized'] += backtick_changes
                
                print(f"✓ {filepath.relative_to(Path.cwd())}: {total_changes} fix(es)")
                
                if not self.dry_run:
                    # Backup original
                    self.backup_file(filepath)
                    
                    # Write fixed content
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write('\n'.join(lines))
                
                return True
            
            return False
            
        except Exception as e:
            print(f"✗ Error processing {filepath}: {e}", file=sys.stderr)
            return False
    
    def process_repository(self, root_dir: Path) -> None:
        """Process all markdown files in the repository."""
        markdown_files = self.find_markdown_files(root_dir)
        self.stats['files_scanned'] = len(markdown_files)
        
        print(f"Scanning {len(markdown_files)} markdown files...")
        if self.dry_run:
            print("DRY RUN MODE - No files will be modified\n")
        
        for filepath in markdown_files:
            self.fix_file(filepath)
        
        self.print_summary()
    
    def print_summary(self) -> None:
        """Print summary of changes."""
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Files scanned:          {self.stats['files_scanned']}")
        print(f"Files modified:         {self.stats['files_modified']}")
        print(f"Blank lines added:      {self.stats['blank_lines_added']}")
        print(f"Placeholders added:     {self.stats['placeholders_added']}")
        print(f"Code blocks fixed:      {self.stats['code_blocks_fixed']}")
        print(f"Backticks normalized:   {self.stats['backticks_normalized']}")
        
        if self.dry_run:
            print("\nDRY RUN - No files were actually modified")
            print("Run without --dry-run to apply changes")
        else:
            print(f"\nBackup files created with .bak extension")
            print("To restore: rm *.bak (to remove backups) or restore from backups if needed")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Fix malformed MyST tab directives',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Print detailed change information'
    )
    
    args = parser.parse_args()
    
    root_dir = Path.cwd()
    fixer = TabFixer(dry_run=args.dry_run, verbose=args.verbose)
    
    try:
        fixer.process_repository(root_dir)
        return 0
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        return 130
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
