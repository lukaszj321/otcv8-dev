#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QA Checker for Authoring Pipeline
Validates structure, schemas, anchors, CSV headers, and Mermaid diagrams.
"""

import re
import csv
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Any

# Paths
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AUTHORING = DOCS / "authoring"
SOURCES = AUTHORING / "_sources"
QA_DIR = AUTHORING / "qa"

def ensure_dirs(*dirs):
    """Create directories if they don't exist."""
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}
    
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        return {}

def check_csv_headers(chapter: str, metadata: Dict[str, Any]) -> List[Dict]:
    """Check that CSV files have correct headers as per frontmatter."""
    issues = []
    chapter_dir = AUTHORING / chapter
    datasets_dir = chapter_dir / "datasets"
    
    if not datasets_dir.exists():
        return issues
    
    artifacts = metadata.get('artifacts', {})
    for ds in artifacts.get('datasets', []):
        ds_file = ds.get('file', '')
        expected_headers = ds.get('headers', [])
        
        if not ds_file:
            continue
        
        csv_path = datasets_dir / ds_file
        if not csv_path.exists():
            issues.append({
                'chapter': chapter,
                'file': ds_file,
                'issue': 'CSV file not found',
                'expected': ', '.join(expected_headers),
                'actual': 'N/A'
            })
            continue
        
        # Read actual headers
        try:
            with csv_path.open('r', encoding='utf-8') as f:
                reader = csv.reader(f)
                actual_headers = next(reader)
            
            # Compare
            if actual_headers != expected_headers:
                issues.append({
                    'chapter': chapter,
                    'file': ds_file,
                    'issue': 'Header mismatch',
                    'expected': ', '.join(expected_headers),
                    'actual': ', '.join(actual_headers)
                })
        except Exception as e:
            issues.append({
                'chapter': chapter,
                'file': ds_file,
                'issue': f'Read error: {e}',
                'expected': ', '.join(expected_headers),
                'actual': 'N/A'
            })
    
    return issues

def check_mermaid_init(chapter: str) -> List[Dict]:
    """Check that Mermaid diagrams have proper init blocks."""
    issues = []
    chapter_dir = AUTHORING / chapter
    diagrams_dir = chapter_dir / "diagrams"
    
    if not diagrams_dir.exists():
        return issues
    
    expected_init = "%%{init:"
    
    for mmd_file in diagrams_dir.glob("*.mmd"):
        try:
            content = mmd_file.read_text(encoding='utf-8').strip()
            if not content.startswith(expected_init):
                issues.append({
                    'chapter': chapter,
                    'file': mmd_file.name,
                    'issue': 'Missing or incorrect Mermaid init block',
                    'line': 1
                })
        except Exception as e:
            issues.append({
                'chapter': chapter,
                'file': mmd_file.name,
                'issue': f'Read error: {e}',
                'line': 0
            })
    
    return issues

def check_facet_anchors(chapter: str, metadata: Dict[str, Any]) -> List[Dict]:
    """Check that facet anchors are present in index.md."""
    issues = []
    chapter_dir = AUTHORING / chapter
    index_path = chapter_dir / "index.md"
    
    if not index_path.exists():
        issues.append({
            'chapter': chapter,
            'facet': 'N/A',
            'issue': 'index.md not found'
        })
        return issues
    
    content = index_path.read_text(encoding='utf-8')
    
    # Expected facets from artifacts
    artifacts = metadata.get('artifacts', {})
    expected_facets = []
    
    for ds in artifacts.get('datasets', []):
        facet = ds.get('facet', '')
        if facet:
            expected_facets.append(facet)
    
    for diag in artifacts.get('diagrams', []):
        facet = diag.get('facet', '')
        if facet:
            expected_facets.append(facet)
    
    # Check for anchors
    for facet in expected_facets:
        anchor_pattern = f"(facet-{facet})="
        if anchor_pattern not in content:
            issues.append({
                'chapter': chapter,
                'facet': facet,
                'issue': f'Missing facet anchor: {anchor_pattern}'
            })
    
    return issues

def check_index_structure(chapter: str) -> List[Dict]:
    """Check that index.md has required sections."""
    issues = []
    chapter_dir = AUTHORING / chapter
    index_path = chapter_dir / "index.md"
    
    if not index_path.exists():
        return issues
    
    content = index_path.read_text(encoding='utf-8')
    
    required_sections = [
        '## Datasets',
        '## Diagrams',
        '## Appendix / Facets'
    ]
    
    for section in required_sections:
        if section not in content:
            issues.append({
                'chapter': chapter,
                'section': section,
                'issue': f'Missing required section: {section}'
            })
    
    # Check frontmatter
    if not content.startswith('---'):
        issues.append({
            'chapter': chapter,
            'section': 'frontmatter',
            'issue': 'Missing frontmatter'
        })
    
    return issues

def check_xref_evidence(xref_path: Path) -> List[Dict]:
    """Check that xref evidence paths exist."""
    issues = []
    
    if not xref_path.exists():
        return [{'issue': 'xref.csv not found', 'path': str(xref_path)}]
    
    with xref_path.open('r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            evidence = row.get('evidence_path', '')
            if evidence and not evidence.startswith('docs/'):
                continue  # relative path
            
            evidence_full = ROOT / evidence if evidence else None
            if evidence_full and not evidence_full.exists():
                issues.append({
                    'from': row.get('from_chapter', ''),
                    'to': row.get('to_chapter', ''),
                    'evidence': evidence,
                    'issue': 'Evidence file not found'
                })
    
    return issues

def generate_qa_report(all_issues: Dict[str, List[Dict]]):
    """Generate QA report."""
    ensure_dirs(QA_DIR)
    
    # CSV reports for each check
    for check_name, issues in all_issues.items():
        if not issues:
            continue
        
        csv_path = QA_DIR / f"{check_name}.csv"
        
        if issues:
            keys = list(issues[0].keys())
            with csv_path.open('w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(issues)
            
            print(f"  [WARN] {len(issues)} issues in {check_name}")
        else:
            # Write OK marker
            with csv_path.open('w', newline='', encoding='utf-8') as f:
                f.write('status\nOK\n')
    
    # Summary markdown
    summary_path = QA_DIR / "summary.md"
    
    total_issues = sum(len(issues) for issues in all_issues.values())
    
    lines = [
        "---",
        "title: QA Summary",
        "---",
        "",
        "# QA Checks Summary",
        "",
        f"**Total Issues Found:** {total_issues}",
        "",
        "## Checks Performed",
        ""
    ]
    
    for check_name, issues in all_issues.items():
        status = "✅ PASS" if len(issues) == 0 else f"❌ FAIL ({len(issues)} issues)"
        lines.append(f"- **{check_name}**: {status}")
    
    lines.extend([
        "",
        "## Details",
        "",
        "See individual CSV files in this directory for detailed issue reports.",
        ""
    ])
    
    summary_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"\n[OK] QA report generated in {QA_DIR.relative_to(ROOT)}")

def main():
    """Main QA execution."""
    print("=" * 60)
    print("QA Checker for Authoring Pipeline")
    print("=" * 60)
    
    if not SOURCES.exists():
        print(f"[ERROR] Sources directory not found: {SOURCES}")
        return 1
    
    all_issues = {
        'csv_headers': [],
        'mermaid_init': [],
        'facet_anchors': [],
        'index_structure': [],
        'xref_evidence': []
    }
    
    # Process chapters
    source_files = sorted(SOURCES.glob("chapter_*.md"))
    
    print(f"\n[INFO] Checking {len(source_files)} chapters...\n")
    
    for source_file in source_files:
        content = source_file.read_text(encoding='utf-8')
        metadata = parse_frontmatter(content)
        
        chapter = metadata.get('chapter', '') or metadata.get('slug', '')
        if not chapter:
            continue
        
        print(f"Checking: {chapter}")
        
        # Run checks
        all_issues['csv_headers'].extend(check_csv_headers(chapter, metadata))
        all_issues['mermaid_init'].extend(check_mermaid_init(chapter))
        all_issues['facet_anchors'].extend(check_facet_anchors(chapter, metadata))
        all_issues['index_structure'].extend(check_index_structure(chapter))
    
    # Check xref evidence
    print("\nChecking cross-references...")
    xref_path = AUTHORING / "_data" / "xref.csv"
    all_issues['xref_evidence'].extend(check_xref_evidence(xref_path))
    
    # Generate report
    print("\n[Phase: Generating QA report]")
    generate_qa_report(all_issues)
    
    total_issues = sum(len(issues) for issues in all_issues.values())
    
    print("\n" + "=" * 60)
    if total_issues == 0:
        print("✅ All QA checks passed!")
    else:
        print(f"⚠️  Found {total_issues} issues. See {QA_DIR} for details.")
    print("=" * 60)
    
    return 0 if total_issues == 0 else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
