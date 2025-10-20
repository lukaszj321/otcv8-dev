#!/usr/bin/env python3
"""
Generate analytics reports for documentation coverage and gaps.
"""

import os
import csv
from pathlib import Path
from datetime import datetime

def count_md_files(chapter_path):
    """Count markdown files in a chapter."""
    return len(list(Path(chapter_path).rglob("*.md")))

def get_chapter_size(chapter_path):
    """Get total size of chapter in bytes."""
    total = 0
    for f in Path(chapter_path).rglob("*"):
        if f.is_file():
            total += f.stat().st_size
    return total

def count_datasets(chapter_path):
    """Count CSV/NDJSON datasets in a chapter."""
    datasets_path = Path(chapter_path) / "datasets"
    if not datasets_path.exists():
        return 0
    return len([f for f in datasets_path.iterdir() 
                if f.suffix in ['.csv', '.ndjson'] and f.name != 'index.md'])

def count_diagrams(chapter_path):
    """Count Mermaid diagrams in a chapter."""
    diagrams_path = Path(chapter_path) / "diagrams"
    if not diagrams_path.exists():
        return 0
    return len([f for f in diagrams_path.iterdir() if f.suffix == '.mmd'])

def generate_coverage_csv(authoring_root, output_path):
    """Generate coverage.csv with chapter statistics."""
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
        
        md_count = count_md_files(chapter_path)
        size_bytes = get_chapter_size(chapter_path)
        size_kb = size_bytes / 1024
        datasets = count_datasets(chapter_path)
        diagrams = count_diagrams(chapter_path)
        
        # Determine status
        status = "PASS" if size_kb >= 18 and datasets >= 3 else "WARN"
        if datasets < 1:
            status = "FAIL"
        
        rows.append({
            "chapter": chapter,
            "md_files": md_count,
            "size_kb": f"{size_kb:.1f}",
            "datasets": datasets,
            "diagrams": diagrams,
            "status": status,
            "notes": ""
        })
    
    # Write CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "chapter", "md_files", "size_kb", "datasets", "diagrams", "status", "notes"
        ])
        writer.writeheader()
        writer.writerows(rows)
    
    return rows

def generate_gaps_md(coverage_rows, output_path):
    """Generate gaps.md with identified issues."""
    content = """# Documentation Gaps and Issues

Generated: """ + datetime.utcnow().isoformat() + """Z

## Summary

"""
    
    fail_count = sum(1 for r in coverage_rows if r['status'] == 'FAIL')
    warn_count = sum(1 for r in coverage_rows if r['status'] == 'WARN')
    pass_count = sum(1 for r in coverage_rows if r['status'] == 'PASS')
    
    content += f"""- ✅ PASS: {pass_count} chapters
- ⚠️ WARN: {warn_count} chapters
- ❌ FAIL: {fail_count} chapters

## Gaps by Chapter

"""
    
    for row in coverage_rows:
        if row['status'] != 'PASS':
            content += f"""### {row['chapter']} - {row['status']}

- **Size:** {row['size_kb']} KB (target: ≥18 KB)
- **Datasets:** {row['datasets']} (minimum: 3)
- **Diagrams:** {row['diagrams']}

**Actionable Steps:**
"""
            if float(row['size_kb']) < 18:
                content += "1. Add more content sections and examples\n"
            if int(row['datasets']) < 3:
                content += f"2. Generate {3 - int(row['datasets'])} additional dataset(s)\n"
            if int(row['diagrams']) == 0:
                content += "3. Create at least 1 Mermaid diagram\n"
            content += "\n"
    
    # Write file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_xref_stats(authoring_root, output_path):
    """Generate xref_stats.csv from relations data."""
    relations_path = Path(authoring_root) / "relations" / "relations.csv"
    
    if not relations_path.exists():
        # Create empty stats
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                "chapter", "outgoing_links", "incoming_links", "total_relations"
            ])
            writer.writeheader()
        return
    
    # Would parse relations.csv and count links per chapter
    # For now, create placeholder
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "chapter", "outgoing_links", "incoming_links", "total_relations"
        ])
        writer.writeheader()

def generate_run_summary(coverage_rows, output_path):
    """Generate run_summary.json with overall statistics."""
    import json
    
    summary = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "chapters_total": len(coverage_rows),
        "chapters_pass": sum(1 for r in coverage_rows if r['status'] == 'PASS'),
        "chapters_warn": sum(1 for r in coverage_rows if r['status'] == 'WARN'),
        "chapters_fail": sum(1 for r in coverage_rows if r['status'] == 'FAIL'),
        "total_md_files": sum(int(r['md_files']) for r in coverage_rows),
        "total_datasets": sum(int(r['datasets']) for r in coverage_rows),
        "total_diagrams": sum(int(r['diagrams']) for r in coverage_rows),
        "total_size_kb": sum(float(r['size_kb']) for r in coverage_rows)
    }
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

def main():
    authoring_root = "/home/runner/work/otcv8-dev/otcv8-dev/docs/authoring"
    
    print("Generating coverage.csv...")
    coverage_rows = generate_coverage_csv(
        authoring_root,
        os.path.join(authoring_root, "analytics", "coverage.csv")
    )
    print(f"  - Analyzed {len(coverage_rows)} chapters")
    
    print("Generating gaps.md...")
    generate_gaps_md(
        coverage_rows,
        os.path.join(authoring_root, "analytics", "gaps.md")
    )
    
    print("Generating xref_stats.csv...")
    generate_xref_stats(
        authoring_root,
        os.path.join(authoring_root, "analytics", "xref_stats.csv")
    )
    
    print("Generating run_summary.json...")
    generate_run_summary(
        coverage_rows,
        os.path.join(authoring_root, "analytics", "run_summary.json")
    )
    
    print("\nAnalytics generated successfully!")
    
    # Print summary
    pass_count = sum(1 for r in coverage_rows if r['status'] == 'PASS')
    warn_count = sum(1 for r in coverage_rows if r['status'] == 'WARN')
    fail_count = sum(1 for r in coverage_rows if r['status'] == 'FAIL')
    
    print(f"\nSummary: {pass_count} PASS, {warn_count} WARN, {fail_count} FAIL")

if __name__ == "__main__":
    main()
