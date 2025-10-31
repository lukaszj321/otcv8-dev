#!/usr/bin/env python3
"""
cleanup_scripts_tools.py

Scans scripts/ and tools/ directories and moves unreferenced and older-than-2-years files
into scripts/legacy/ (conservative; do not delete).

References are gathered from: Makefile, .github, docs, package.json, conf.py

Usage:
    python3 docs/scripts/cleanup_scripts_tools.py           # dry-run (report only)
    python3 docs/scripts/cleanup_scripts_tools.py --apply   # move files to legacy/
"""

import os
import sys
import shutil
import re
from pathlib import Path
from datetime import datetime, timedelta
from typing import Set, List


def find_repo_root() -> Path:
    """Find repository root (contains .git directory)."""
    current = Path(__file__).parent
    while current != current.parent:
        if (current / ".git").exists():
            return current
        current = current.parent
    
    # Fallback to current working directory
    return Path.cwd()


def gather_references(repo_root: Path) -> Set[str]:
    """
    Gather all referenced file paths from various sources.
    
    Returns:
        Set of referenced file basenames (without directories)
    """
    references = set()
    
    # Files to scan for references
    scan_files = [
        repo_root / "Makefile",
        repo_root / "package.json",
        repo_root / "docs" / "conf.py",
    ]
    
    # Add all files in .github directory
    github_dir = repo_root / ".github"
    if github_dir.exists():
        for file in github_dir.rglob("*"):
            if file.is_file():
                scan_files.append(file)
    
    # Add all doc files
    docs_dir = repo_root / "docs"
    if docs_dir.exists():
        for ext in ["*.md", "*.rst", "*.py"]:
            for file in docs_dir.rglob(ext):
                scan_files.append(file)
    
    # Pattern to match script/tool references
    # Matches: script.py, tool.sh, anything.mjs, etc.
    script_pattern = re.compile(r'[\w\-\.]+\.(py|sh|js|mjs|ts|ps1|bash|rb|pl)')
    
    for scan_file in scan_files:
        if not scan_file.exists() or not scan_file.is_file():
            continue
        
        try:
            content = scan_file.read_text(encoding='utf-8', errors='ignore')
            
            # Find all script references
            matches = script_pattern.findall(content)
            for match in matches:
                references.add(match)
            
            # Also extract full paths (e.g., scripts/something.py)
            path_pattern = re.compile(r'(?:scripts|tools)/[\w\-\./]+\.(py|sh|js|mjs|ts|ps1|bash|rb|pl)')
            for match in path_pattern.finditer(content):
                path = match.group(0)
                basename = Path(path).name
                references.add(basename)
                
        except Exception as e:
            print(f"Warning: Could not read {scan_file}: {e}", file=sys.stderr)
    
    return references


def is_old_file(file_path: Path, age_years: int = 2) -> bool:
    """Check if file is older than specified years based on modification time."""
    try:
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        cutoff = datetime.now() - timedelta(days=age_years * 365)
        return mtime < cutoff
    except Exception:
        return False


def find_unreferenced_files(repo_root: Path, references: Set[str]) -> List[tuple]:
    """
    Find unreferenced and old files in scripts/ and tools/ directories.
    
    Returns:
        List of tuples: (file_path, reason)
        reason can be: 'unreferenced', 'old', 'unreferenced_and_old'
    """
    candidates = []
    
    for directory in ["scripts", "tools"]:
        dir_path = repo_root / directory
        if not dir_path.exists():
            continue
        
        for file in dir_path.iterdir():
            if not file.is_file():
                continue
            
            # Skip certain files
            if file.name in [".gitkeep", "README.md", "README.txt", "__init__.py"]:
                continue
            
            basename = file.name
            is_referenced = basename in references
            is_old = is_old_file(file, age_years=2)
            
            # Determine if this file should be moved
            if not is_referenced and is_old:
                reason = "unreferenced_and_old"
            elif not is_referenced:
                # Only suggest if truly looks unused (conservative)
                if file.suffix in ['.bak', '.tmp', '.old', '.backup']:
                    reason = "unreferenced"
                else:
                    # Too risky - skip files that might be used but not explicitly referenced
                    continue
            elif is_old:
                # Only move old files if they have certain extensions that suggest they're outdated
                if file.suffix in ['.bak', '.tmp', '.old', '.backup']:
                    reason = "old"
                else:
                    continue
            else:
                continue
            
            candidates.append((file, reason))
    
    return candidates


def move_to_legacy(files: List[tuple], apply: bool = False) -> int:
    """
    Move files to legacy directory.
    
    Returns:
        Number of files moved
    """
    if not files:
        print("\nNo files to move.")
        return 0
    
    if not apply:
        print("\n=== DRY RUN: No files will be moved ===")
        print("Run with --apply to move files to legacy/\n")
        return 0
    
    repo_root = find_repo_root()
    legacy_dir = repo_root / "scripts" / "legacy"
    legacy_dir.mkdir(parents=True, exist_ok=True)
    
    moved_count = 0
    print("\n=== Moving files to legacy/ ===\n")
    
    for file_path, reason in files:
        try:
            # Determine source directory name
            parent_name = file_path.parent.name
            
            # Create subdirectory in legacy if needed
            if parent_name == "tools":
                dest_dir = legacy_dir / "from_tools"
                dest_dir.mkdir(exist_ok=True)
                dest = dest_dir / file_path.name
            else:
                dest = legacy_dir / file_path.name
            
            # Move file
            shutil.move(str(file_path), str(dest))
            print(f"  Moved: {file_path} -> {dest}")
            print(f"    Reason: {reason}")
            moved_count += 1
            
        except Exception as e:
            print(f"  Error moving {file_path}: {e}", file=sys.stderr)
    
    print(f"\nMoved {moved_count} file(s) to {legacy_dir}")
    return moved_count


def main():
    apply = '--apply' in sys.argv
    
    repo_root = find_repo_root()
    print(f"Repository root: {repo_root}\n")
    
    print("Gathering references from Makefile, .github, docs, package.json, conf.py...")
    references = gather_references(repo_root)
    print(f"Found {len(references)} referenced script/tool name(s)\n")
    
    print("Scanning scripts/ and tools/ for unreferenced and old files...")
    candidates = find_unreferenced_files(repo_root, references)
    
    # Print report
    print("\n" + "="*70)
    print("CLEANUP CANDIDATES REPORT")
    print("="*70 + "\n")
    
    if not candidates:
        print("No files need to be moved! ✓")
        return
    
    print(f"Found {len(candidates)} file(s) to move:\n")
    
    for file_path, reason in sorted(candidates, key=lambda x: (x[1], str(x[0]))):
        print(f"  {file_path}")
        print(f"    Reason: {reason}")
        print()
    
    print("="*70)
    
    move_to_legacy(candidates, apply)


if __name__ == '__main__':
    main()
