#!/usr/bin/env python3
"""
YAML Front-matter Scanner
Scans all markdown files for front-matter issues:
- Single-line YAML (should be multiline)
- Invalid tags format (should be YAML list)
- Missing/duplicate --- delimiters
- Invalid dates
"""

import re
import csv
from pathlib import Path
from typing import List, Dict


def scan_frontmatter(filepath: Path) -> List[Dict[str, str]]:
    """
    Scan a markdown file for front-matter issues.
    
    Returns:
        List of issues found
    """
    issues = []
    
    try:
        content = filepath.read_text(encoding='utf-8')
        lines = content.splitlines()
        
        if not lines:
            return issues
        
        # Check if file starts with ---
        if not lines[0].startswith('---'):
            issues.append({
                'file': str(filepath.relative_to('docs/authoring')),
                'line': 1,
                'issue': 'missing_frontmatter',
                'details': 'No front-matter block found'
            })
            return issues
        
        # Find the front-matter block
        end_idx = -1
        for i in range(1, min(len(lines), 50)):  # Look in first 50 lines
            if lines[i].startswith('---'):
                end_idx = i
                break
        
        if end_idx == -1:
            issues.append({
                'file': str(filepath.relative_to('docs/authoring')),
                'line': 1,
                'issue': 'unclosed_frontmatter',
                'details': 'Front-matter block not closed'
            })
            return issues
        
        frontmatter = '\n'.join(lines[1:end_idx])
        
        # Check if front-matter is single-line (all on line 2)
        if end_idx == 2:
            # Single line between --- markers
            issues.append({
                'file': str(filepath.relative_to('docs/authoring')),
                'line': 2,
                'issue': 'single_line_yaml',
                'details': 'Front-matter is single-line (should be multiline)'
            })
        
        # Check for tags format
        tags_match = re.search(r'tags:\s*([^\n]+)', frontmatter)
        if tags_match:
            tags_value = tags_match.group(1).strip()
            # If tags contains commas but not brackets, it's wrong format
            if ',' in tags_value and not (tags_value.startswith('[') or tags_value.startswith('-')):
                issues.append({
                    'file': str(filepath.relative_to('docs/authoring')),
                    'line': 2,
                    'issue': 'invalid_tags_format',
                    'details': f'tags should be YAML list, got: {tags_value[:50]}'
                })
        
        # Check for invalid date format
        date_match = re.search(r'last_sync_iso:\s*([^\n,]+)', frontmatter)
        if date_match:
            date_value = date_match.group(1).strip()
            # Basic ISO date check
            if not re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', date_value):
                issues.append({
                    'file': str(filepath.relative_to('docs/authoring')),
                    'line': 2,
                    'issue': 'invalid_date_format',
                    'details': f'Invalid ISO date: {date_value[:30]}'
                })
        
        # Check for duplicate --- in frontmatter (shouldn't happen but let's check)
        if frontmatter.count('---') > 0:
            issues.append({
                'file': str(filepath.relative_to('docs/authoring')),
                'line': 2,
                'issue': 'duplicate_delimiter',
                'details': 'Extra --- found inside front-matter'
            })
            
    except Exception as e:
        issues.append({
            'file': str(filepath.relative_to('docs/authoring')),
            'line': 0,
            'issue': 'scan_error',
            'details': str(e)
        })
    
    return issues


def main():
    """Main entry point."""
    base_path = Path('docs/authoring')
    qa_path = Path('docs/authoring/qa')
    qa_path.mkdir(parents=True, exist_ok=True)
    
    output_file = qa_path / 'frontmatter_issues.csv'
    
    all_issues = []
    
    # Scan all markdown files
    for md_file in base_path.rglob('*.md'):
        # Skip _instructions and _tools
        if any(part.startswith('_') for part in md_file.parts):
            continue
        
        issues = scan_frontmatter(md_file)
        all_issues.extend(issues)
    
    # Write CSV report
    with output_file.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['file', 'line', 'issue', 'details'])
        writer.writeheader()
        writer.writerows(all_issues)
    
    print(f"Front-matter scan complete")
    print(f"  Files scanned: {len(list(base_path.rglob('*.md')))}")
    print(f"  Issues found: {len(all_issues)}")
    print(f"  Report: {output_file}")
    
    if all_issues:
        print("\nIssue summary:")
        issue_types = {}
        for issue in all_issues:
            issue_type = issue['issue']
            issue_types[issue_type] = issue_types.get(issue_type, 0) + 1
        
        for issue_type, count in sorted(issue_types.items()):
            print(f"  - {issue_type}: {count}")


if __name__ == '__main__':
    main()
