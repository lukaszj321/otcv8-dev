#!/usr/bin/env python3
"""
Generate placeholder files for missing literalinclude references.

This script scans documentation files for literalinclude directives and creates
minimal placeholder files for any missing references. This prevents Sphinx build
failures when source files are not available.

Usage:
    python docs/scripts/generate_placeholders.py
"""

import re
from pathlib import Path
from typing import Set
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def find_literalinclude_paths(docs_dir: Path) -> Set[str]:
    """
    Scan all .rst and .md files for literalinclude directives and extract file paths.
    
    Returns:
        Set of strings representing files referenced in literalinclude directives
    """
    include_paths: Set[str] = set()
    
    # Patterns for both RST and MyST syntax
    rst_pattern = re.compile(r'^\s*\.\.\s+literalinclude::\s+(.+)$', re.MULTILINE)
    myst_pattern = re.compile(r'^\s*```\{literalinclude\}\s+(.+)$', re.MULTILINE)
    
    for doc_file in docs_dir.rglob('*.rst'):
        try:
            content = doc_file.read_text(encoding='utf-8', errors='replace')
            for match in rst_pattern.finditer(content):
                path_str = match.group(1).strip()
                include_paths.add(path_str)
        except Exception as e:
            logger.warning(f"Error reading {doc_file}: {e}")
    
    for doc_file in docs_dir.rglob('*.md'):
        try:
            content = doc_file.read_text(encoding='utf-8', errors='replace')
            for match in myst_pattern.finditer(content):
                path_str = match.group(1).strip()
                include_paths.add(path_str)
        except Exception as e:
            logger.warning(f"Error reading {doc_file}: {e}")
    
    return include_paths


def resolve_include_path(include_str: str, docs_dir: Path, repo_root: Path) -> Path:
    """
    Resolve a literalinclude path to an absolute file path.
    
    Handles:
    - Absolute paths from repo root (e.g., /src/file.cpp)
    - Relative paths from docs dir
    - Paths with special prefixes
    
    Args:
        include_str: The path string from literalinclude directive
        docs_dir: Path to docs directory
        repo_root: Path to repository root
        
    Returns:
        Absolute Path object
    """
    # Clean the path
    path_str = include_str.strip()
    
    # Remove any directive options (lines starting with :)
    path_str = path_str.split('\n')[0].strip()
    
    # Handle absolute paths from repo root
    if path_str.startswith('/'):
        return repo_root / path_str.lstrip('/')
    
    # Handle relative paths from docs dir
    return docs_dir / Path(path_str)


def create_placeholder_file(file_path: Path, file_type: str = 'unknown') -> bool:
    """
    Create a placeholder file with appropriate comment syntax.
    
    Args:
        file_path: Path where placeholder should be created
        file_type: File extension/type for appropriate comment syntax
        
    Returns:
        True if file was created, False if it already exists or creation failed
    """
    if file_path.exists():
        return False
    
    # Determine comment syntax based on file extension
    suffix = file_path.suffix.lower()
    comment_styles = {
        '.cpp': ('// ', ''),
        '.h': ('// ', ''),
        '.hpp': ('// ', ''),
        '.c': ('// ', ''),
        '.cc': ('// ', ''),
        '.cxx': ('// ', ''),
        '.py': ('# ', ''),
        '.lua': ('-- ', ''),
        '.sh': ('# ', ''),
        '.rs': ('// ', ''),
        '.java': ('// ', ''),
        '.js': ('// ', ''),
        '.ts': ('// ', ''),
        '.html': ('<!-- ', ' -->'),
        '.xml': ('<!-- ', ' -->'),
        '.css': ('/* ', ' */'),
    }
    
    comment_start, comment_end = comment_styles.get(suffix, ('# ', ''))
    
    # Calculate relative path for display in placeholder
    # Try to get path relative to repository root, fall back to parent if too deep
    try:
        # Assumes file_path is absolute and within a git repository
        # Walk up to find a reasonable base (max 5 levels to avoid going too far)
        for parent in list(file_path.parents)[:5]:
            if (parent / '.git').exists():
                rel_path = file_path.relative_to(parent)
                break
        else:
            # No .git found, use relative to immediate parent
            rel_path = file_path.name
    except (ValueError, IndexError):
        rel_path = file_path.name
    
    # Create placeholder content
    placeholder_content = f"""{comment_start}PLACEHOLDER FILE{comment_end}
{comment_start}This file was auto-generated as a placeholder for documentation builds.{comment_end}
{comment_start}Real implementation should replace this file.{comment_end}
{comment_start}Path: {rel_path}{comment_end}

"""
    
    try:
        # Create parent directories if needed
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write placeholder
        file_path.write_text(placeholder_content, encoding='utf-8')
        logger.info(f"Created placeholder: {file_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to create placeholder {file_path}: {e}")
        return False


def main():
    """Main entry point for the script."""
    # Determine paths
    script_dir = Path(__file__).resolve().parent
    docs_dir = script_dir.parent
    repo_root = docs_dir.parent
    
    logger.info(f"Scanning documentation in: {docs_dir}")
    logger.info(f"Repository root: {repo_root}")
    
    # Find all literalinclude references
    include_refs = find_literalinclude_paths(docs_dir)
    logger.info(f"Found {len(include_refs)} literalinclude references")
    
    # Check which files are missing and create placeholders
    created_count = 0
    missing_count = 0
    
    for include_str in sorted(include_refs):
        try:
            file_path = resolve_include_path(include_str, docs_dir, repo_root)
            
            if not file_path.exists():
                missing_count += 1
                if create_placeholder_file(file_path):
                    created_count += 1
        except Exception as e:
            logger.warning(f"Error processing include '{include_str}': {e}")
    
    logger.info(f"Summary: {missing_count} missing files, {created_count} placeholders created")
    
    # Create docs/images/.gitkeep if it doesn't exist
    images_dir = docs_dir / 'images'
    images_dir.mkdir(exist_ok=True)
    gitkeep = images_dir / '.gitkeep'
    if not gitkeep.exists():
        gitkeep.write_text('')
        logger.info(f"Created {gitkeep}")


if __name__ == '__main__':
    main()
