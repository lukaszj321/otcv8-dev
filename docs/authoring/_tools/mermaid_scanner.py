#!/usr/bin/env python3
"""
Mermaid Syntax Scanner
Scans all markdown and .mmd files for Mermaid syntax issues:
- sequenceDiagram with click directive (unsupported)
- Missing init block
- Parse errors
"""

import re
import csv
from pathlib import Path
from typing import List, Dict


def scan_mermaid_blocks(filepath: Path) -> List[Dict[str, str]]:
    """
    Scan a file for Mermaid syntax issues.
    
    Returns:
        List of issues found
    """
    issues = []
    
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        
        # Find all mermaid blocks in markdown
        if filepath.suffix == '.md':
            # Match ```mermaid blocks
            block_matches = list(re.finditer(r'```mermaid\n([\s\S]*?)\n```', content))
            for block_num, match in enumerate(block_matches, 1):
                block_content = match.group(1)
                scan_block(filepath, block_num, block_content, issues)
        else:
            # .mmd files are pure mermaid
            if content.strip():
                scan_block(filepath, 1, content, issues)
        
        return issues
        
    except Exception as e:
        issues.append({
            'file': str(filepath.relative_to('docs/authoring')),
            'block': 0,
            'issue': 'scan_error',
            'details': str(e)
        })
    
    return issues


def scan_block(filepath: Path, block_num: int, block_content: str, issues: List[Dict[str, str]]):
    """Scan a single mermaid block for issues."""
    # Check for missing init
    if '%%{init:' not in block_content:
        issues.append({
            'file': str(filepath.relative_to('docs/authoring')),
            'block': block_num,
            'issue': 'missing_init',
            'details': 'Missing %%{init: ...}%% at start of block'
        })
    
    # Check for sequenceDiagram with click
    if 'sequenceDiagram' in block_content and 'click' in block_content:
        # Find the click line
        for line_num, line in enumerate(block_content.split('\n'), 1):
            if 'click' in line and not line.strip().startswith('%'):
                issues.append({
                    'file': str(filepath.relative_to('docs/authoring')),
                    'block': block_num,
                    'issue': 'sequence_with_click',
                    'details': f'sequenceDiagram does not support click directive: {line.strip()[:60]}'
                })
    
    # Check for invalid syntax patterns
    # Unicode arrows (should be ASCII)
    if '→' in block_content or '←' in block_content or '↔' in block_content:
        issues.append({
            'file': str(filepath.relative_to('docs/authoring')),
            'block': block_num,
            'issue': 'unicode_arrows',
            'details': 'Use ASCII arrows (-->, <--, <-->) instead of Unicode'
        })
    
    # Check for stray backticks inside block
    if '```' in block_content:
        issues.append({
            'file': str(filepath.relative_to('docs/authoring')),
            'block': block_num,
            'issue': 'stray_backticks',
            'details': 'Backticks found inside Mermaid block'
        })


def main():
    """Main entry point."""
    base_path = Path('docs/authoring')
    qa_path = Path('docs/authoring/qa')
    qa_path.mkdir(parents=True, exist_ok=True)
    
    output_file = qa_path / 'mermaid_parse_issues.csv'
    
    all_issues = []
    
    # Scan all markdown and .mmd files
    for pattern in ['*.md', '*.mmd']:
        for file in base_path.rglob(pattern):
            # Skip _instructions and _tools
            if any(part.startswith('_') for part in file.parts):
                continue
            
            issues = scan_mermaid_blocks(file)
            all_issues.extend(issues)
    
    # Write CSV report
    with output_file.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['file', 'block', 'issue', 'details'])
        writer.writeheader()
        writer.writerows(all_issues)
    
    print(f"Mermaid scan complete")
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
