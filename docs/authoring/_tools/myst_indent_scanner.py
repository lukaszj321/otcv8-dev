#!/usr/bin/env python3
"""
MyST Indent Scanner
Scans all markdown files for indented MyST directives that render as text.
"""

import re
import csv
from pathlib import Path
from typing import List, Dict


def scan_indentation(filepath: Path) -> List[Dict[str, str]]:
    """
    Scan a markdown file for indentation issues.
    
    Returns:
        List of issues found
    """
    issues = []
    
    try:
        content = filepath.read_text(encoding='utf-8')
        lines = content.splitlines()
        
        for line_num, line in enumerate(lines, 1):
            # Check for indented directive openers
            if re.match(r'^\s+```{(mermaid|csv-table)', line):
                indent = len(line) - len(line.lstrip())
                issues.append({
                    'file': str(filepath.relative_to('docs/authoring')),
                    'line': line_num,
                    'issue': 'indented_directive_opener',
                    'details': f'Directive indented by {indent} spaces: {line.strip()[:50]}'
                })
            
            # Check for indented directive closers (only if truly indented)
            elif re.match(r'^\s+```\s*$', line):
                indent = len(line) - len(line.lstrip())
                issues.append({
                    'file': str(filepath.relative_to('docs/authoring')),
                    'line': line_num,
                    'issue': 'indented_directive_closer',
                    'details': f'Closer indented by {indent} spaces'
                })
            
            # Check for indented Facet lines
            elif re.match(r'^\s+\*Facet:\*', line):
                indent = len(line) - len(line.lstrip())
                issues.append({
                    'file': str(filepath.relative_to('docs/authoring')),
                    'line': line_num,
                    'issue': 'indented_facet',
                    'details': f'Facet line indented by {indent} spaces: {line.strip()[:50]}'
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
    
    output_file = qa_path / 'myst_indent_report.csv'
    
    all_issues = []
    
    # Scan all markdown files
    for md_file in base_path.rglob('*.md'):
        # Skip _instructions and _tools
        if any(part.startswith('_') for part in md_file.parts):
            continue
        
        issues = scan_indentation(md_file)
        all_issues.extend(issues)
    
    # Write CSV report
    with output_file.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['file', 'line', 'issue', 'details'])
        writer.writeheader()
        writer.writerows(all_issues)
    
    print(f"MyST indent scan complete")
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
