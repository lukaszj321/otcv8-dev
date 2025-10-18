#!/usr/bin/env python3
"""
Generate QA reports for documentation quality checks.
"""

import os
import csv
import re
from pathlib import Path
from datetime import datetime

def check_frontmatter(chapter_path, chapter_id):
    """Check if index.md has proper frontmatter."""
    index_path = Path(chapter_path) / "index.md"
    if not index_path.exists():
        return {"status": "FAIL", "details": "index.md not found"}
    
    content = index_path.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return {"status": "FAIL", "details": "No frontmatter"}
    
    # Check for required fields
    required = ['doc_id', 'source_path', 'doc_class', 'title']
    missing = [f for f in required if f not in content[:500]]
    
    if missing:
        return {"status": "WARN", "details": f"Missing: {','.join(missing)}"}
    
    return {"status": "PASS", "details": "Frontmatter present"}

def check_datasets(chapter_path):
    """Check datasets for schema compliance."""
    datasets_path = Path(chapter_path) / "datasets"
    if not datasets_path.exists():
        return {"status": "WARN", "details": "No datasets directory"}
    
    csv_files = list(datasets_path.glob("*.csv"))
    if not csv_files:
        return {"status": "WARN", "details": "No CSV files"}
    
    issues = []
    for csv_file in csv_files:
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
                if not header:
                    issues.append(f"{csv_file.name}: empty header")
                # Check for rows
                rows = list(reader)
                if not rows:
                    issues.append(f"{csv_file.name}: no data rows")
        except Exception as e:
            issues.append(f"{csv_file.name}: {str(e)}")
    
    if issues:
        return {"status": "WARN", "details": "; ".join(issues[:2])}
    
    return {"status": "PASS", "details": f"{len(csv_files)} CSVs validated"}

def check_diagrams(chapter_path):
    """Check Mermaid diagrams for init header."""
    diagrams_path = Path(chapter_path) / "diagrams"
    if not diagrams_path.exists():
        return {"status": "INFO", "details": "No diagrams directory"}
    
    mmd_files = list(diagrams_path.glob("*.mmd"))
    if not mmd_files:
        return {"status": "INFO", "details": "No Mermaid files"}
    
    issues = []
    for mmd_file in mmd_files:
        content = mmd_file.read_text(encoding='utf-8')
        if not content.startswith('%%{init:'):
            issues.append(f"{mmd_file.name}: missing init header")
    
    if issues:
        return {"status": "WARN", "details": "; ".join(issues[:2])}
    
    return {"status": "PASS", "details": f"{len(mmd_files)} diagrams validated"}

def check_links(chapter_path, chapter_id):
    """Basic link check in index.md."""
    index_path = Path(chapter_path) / "index.md"
    if not index_path.exists():
        return {"status": "FAIL", "details": "index.md not found"}
    
    content = index_path.read_text(encoding='utf-8')
    
    # Count relative links
    link_pattern = re.compile(r'\[([^\]]+)\]\(\.\.\/([^)]+)\)')
    links = link_pattern.findall(content)
    
    if len(links) < 3:
        return {"status": "WARN", "details": f"Only {len(links)} crosslinks (min: 3)"}
    
    return {"status": "PASS", "details": f"{len(links)} crosslinks found"}

def check_facets(chapter_path, chapter_id):
    """Check for facet anchors."""
    index_path = Path(chapter_path) / "index.md"
    if not index_path.exists():
        return {"status": "FAIL", "details": "index.md not found"}
    
    content = index_path.read_text(encoding='utf-8')
    
    # Check for facet anchor
    facet_pattern = re.compile(r'\(facet-' + re.escape(chapter_id) + r'\.[^)]+\)=')
    facets = facet_pattern.findall(content)
    
    if not facets:
        return {"status": "WARN", "details": "No facet anchors"}
    
    return {"status": "PASS", "details": f"{len(facets)} facet(s) found"}

def generate_qa_report(authoring_root, output_path):
    """Generate comprehensive QA report."""
    chapters = [
        "01_core", "01_runtime", "02_events", "03_modules", "04_ui",
        "05_network", "06_assets", "07_settings_crypto", "08_audio",
        "09_logging", "10_game_runtime", "11_data", "12_otmod",
        "13_layouts", "14_android", "15_vc16"
    ]
    
    rows = []
    
    for chapter in chapters:
        chapter_path = Path(authoring_root) / chapter
        if not chapter_path.exists():
            continue
        
        # Run checks
        checks = {
            "frontmatter": check_frontmatter(chapter_path, chapter),
            "datasets": check_datasets(chapter_path),
            "diagrams": check_diagrams(chapter_path),
            "links": check_links(chapter_path, chapter),
            "facets": check_facets(chapter_path, chapter)
        }
        
        for check_name, result in checks.items():
            rows.append({
                "chapter": chapter,
                "check": check_name,
                "status": result["status"],
                "details": result["details"]
            })
    
    # Write CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["chapter", "check", "status", "details"])
        writer.writeheader()
        writer.writerows(rows)
    
    return rows

def generate_qa_summary(qa_rows, output_path):
    """Generate QA summary markdown."""
    content = """# QA Summary Report

Generated: """ + datetime.utcnow().isoformat() + """Z

## Overall Status

"""
    
    # Count by status
    fail_count = sum(1 for r in qa_rows if r['status'] == 'FAIL')
    warn_count = sum(1 for r in qa_rows if r['status'] == 'WARN')
    pass_count = sum(1 for r in qa_rows if r['status'] == 'PASS')
    info_count = sum(1 for r in qa_rows if r['status'] == 'INFO')
    
    content += f"""- ✅ PASS: {pass_count} checks
- ⚠️ WARN: {warn_count} checks
- ❌ FAIL: {fail_count} checks
- ℹ️ INFO: {info_count} checks

## Checks by Type

"""
    
    # Group by check type
    by_check = {}
    for row in qa_rows:
        check = row['check']
        if check not in by_check:
            by_check[check] = []
        by_check[check].append(row)
    
    for check_name, checks in sorted(by_check.items()):
        content += f"\n### {check_name.title()}\n\n"
        
        fail = [c for c in checks if c['status'] == 'FAIL']
        warn = [c for c in checks if c['status'] == 'WARN']
        
        if fail:
            content += f"**FAIL ({len(fail)}):**\n"
            for c in fail[:5]:
                content += f"- {c['chapter']}: {c['details']}\n"
        
        if warn:
            content += f"\n**WARN ({len(warn)}):**\n"
            for c in warn[:5]:
                content += f"- {c['chapter']}: {c['details']}\n"
    
    content += """

## Recommendations

1. Address all FAIL status checks immediately
2. Review WARN status checks and improve where possible
3. Ensure all chapters have:
   - Proper frontmatter with required fields
   - At least 3 datasets with valid schemas
   - Mermaid diagrams with init headers
   - At least 3 crosslinks to related chapters
   - Facet anchors for key sections

## Next Steps

- Run link-lint to verify all relative links
- Validate CSV schemas for compliance
- Check diagram rendering
- Verify facet anchor targets exist
"""
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    authoring_root = "/home/runner/work/otcv8-dev/otcv8-dev/docs/authoring"
    
    print("Running QA checks...")
    qa_rows = generate_qa_report(
        authoring_root,
        os.path.join(authoring_root, "qa", "qa_report.csv")
    )
    print(f"  - Completed {len(qa_rows)} checks across all chapters")
    
    print("Generating QA summary...")
    generate_qa_summary(
        qa_rows,
        os.path.join(authoring_root, "qa", "qa_summary.md")
    )
    
    # Count issues
    fail_count = sum(1 for r in qa_rows if r['status'] == 'FAIL')
    warn_count = sum(1 for r in qa_rows if r['status'] == 'WARN')
    
    print(f"\nQA Report: {fail_count} FAIL, {warn_count} WARN")
    
    if fail_count > 0:
        print("\n⚠️  Critical issues found - review qa/qa_report.csv")
    else:
        print("\n✅ No critical failures")

if __name__ == "__main__":
    main()
