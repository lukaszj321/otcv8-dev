#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Authoring Pipeline Generator (01-10)
Generates datasets, diagrams, MyST pages, xrefs, and analytics
for docs/authoring/** from _sources/ frontmatter metadata.
"""

import re
import csv
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime

# Paths
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AUTHORING = DOCS / "authoring"
SOURCES = AUTHORING / "_sources"
DATA_DIR = AUTHORING / "_data"
ANALYTICS_DIR = AUTHORING / "analytics"

# Constants
MAX_CSV_SIZE = 2 * 1024 * 1024  # 2MB
SAMPLE_ROWS = 200
MERMAID_INIT = "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%"

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}
    
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"[WARN] YAML parse error: {e}")
        return {}

def ensure_dirs(*dirs):
    """Create directories if they don't exist."""
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

def create_csv_stub(path: Path, headers: List[str]):
    """Create a CSV file with headers if it doesn't exist."""
    if path.exists():
        print(f"  [SKIP] {path.name} already exists")
        return
    
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
    print(f"  [CREATE] {path.name} with headers: {', '.join(headers)}")

def create_mermaid_stub(path: Path, facet_id: str, diagram_id: str):
    """Create a Mermaid diagram stub if it doesn't exist."""
    if path.exists():
        print(f"  [SKIP] {path.name} already exists")
        return
    
    stub = f"""{MERMAID_INIT}
graph TD
    A[{facet_id}] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-{facet_id}" "Open {diagram_id}"
"""
    path.write_text(stub, encoding='utf-8')
    print(f"  [CREATE] {path.name} stub for facet {facet_id}")

def ensure_mermaid_init(content: str) -> str:
    """Ensure Mermaid diagram has init block."""
    content = content.strip()
    if not content.startswith("%%{init:"):
        return MERMAID_INIT + "\n" + content
    return content

def get_csv_size(path: Path) -> int:
    """Get file size in bytes."""
    return path.stat().st_size if path.exists() else 0

def create_csv_sample(source: Path, sample: Path, max_rows: int = SAMPLE_ROWS):
    """Create a sample CSV with limited rows."""
    if not source.exists():
        return
    
    with source.open('r', encoding='utf-8') as f_in:
        reader = csv.reader(f_in)
        rows = [next(reader)]  # header
        rows.extend([row for i, row in enumerate(reader) if i < max_rows])
    
    with sample.open('w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        writer.writerows(rows)
    
    print(f"  [SAMPLE] Created {sample.name} with {len(rows)} rows")

def process_chapter_artifacts(chapter: str, metadata: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    """Process datasets and diagrams for a chapter."""
    chapter_dir = AUTHORING / chapter
    datasets_dir = chapter_dir / "datasets"
    diagrams_dir = chapter_dir / "diagrams"
    
    ensure_dirs(datasets_dir, diagrams_dir)
    
    datasets = []
    diagrams = []
    
    # Process datasets
    artifacts = metadata.get('artifacts', {})
    for ds in artifacts.get('datasets', []):
        ds_id = ds.get('id', '')
        ds_file = ds.get('file', '')
        ds_headers = ds.get('headers', [])
        ds_facet = ds.get('facet', f"{chapter}.{ds_id}")
        
        if not ds_file or not ds_headers:
            continue
        
        csv_path = datasets_dir / ds_file
        create_csv_stub(csv_path, ds_headers)
        datasets.append(ds_file)
        
        # Check if sample needed
        if get_csv_size(csv_path) > MAX_CSV_SIZE:
            sample_path = datasets_dir / ds_file.replace('.csv', '-sample.csv')
            create_csv_sample(csv_path, sample_path)
    
    # Process diagrams
    for diag in artifacts.get('diagrams', []):
        diag_id = diag.get('id', '')
        diag_file = diag.get('file', '')
        diag_facet = diag.get('facet', f"{chapter}.{diag_id}")
        
        if not diag_file:
            continue
        
        mmd_path = diagrams_dir / diag_file
        create_mermaid_stub(mmd_path, diag_facet, diag_id)
        diagrams.append(diag_file)
    
    return datasets, diagrams

def generate_chapter_page(chapter: str, metadata: Dict[str, Any], datasets: List[str], diagrams: List[str]):
    """Generate MyST page for a chapter."""
    chapter_dir = AUTHORING / chapter
    index_path = chapter_dir / "index.md"
    
    title = metadata.get('title', chapter.replace('_', ' ').title())
    slug = metadata.get('slug', chapter)
    
    # Intro section
    intro_lines = [
        f"# {title}\n",
        "```{contents} Table of contents",
        ":depth: 2",
        ":local:",
        "```\n",
    ]
    
    # Datasets section
    datasets_lines = ["## Datasets\n"]
    if datasets:
        datasets_dir = chapter_dir / "datasets"
        for ds_file in sorted(datasets):
            ds_path = datasets_dir / ds_file
            stem = ds_path.stem
            facet_id = f"{chapter}.{stem}"
            
            # Check if sample exists
            sample_path = datasets_dir / ds_file.replace('.csv', '-sample.csv')
            use_sample = sample_path.exists() and get_csv_size(ds_path) > MAX_CSV_SIZE
            display_file = sample_path.name if use_sample else ds_file
            
            datasets_lines.extend([
                f"### {stem}",
                f"*Facet:* [`{facet_id}`](#facet-{facet_id})",
                "",
                f"```{{csv-table}} {stem}",
                ":header-rows: 1",
                f":file: ./datasets/{display_file}",
                ":widths: auto",
                "```",
                "",
            ])
            
            if use_sample:
                datasets_lines.append(f"*Full dataset: [`{ds_file}`](./datasets/{ds_file})*\n")
    else:
        datasets_lines.append("_Brak datasets w tym rozdziale._\n")
    
    # Diagrams section
    diagrams_lines = ["## Diagrams\n"]
    if diagrams:
        diagrams_dir = chapter_dir / "diagrams"
        for diag_file in sorted(diagrams):
            diag_path = diagrams_dir / diag_file
            if not diag_path.exists():
                continue
            
            stem = diag_path.stem
            facet_id = f"{chapter}.{stem}"
            content = diag_path.read_text(encoding='utf-8')
            content = ensure_mermaid_init(content)
            
            diagrams_lines.extend([
                f"### {stem}",
                f"*Facet:* [`{facet_id}`](#facet-{facet_id})",
                "",
                "```{mermaid}",
                content,
                "```",
                "",
            ])
    else:
        diagrams_lines.append("_Brak diagrams w tym rozdziale._\n")
    
    # Facets appendix
    facets_lines = ["## Appendix / Facets\n"]
    all_items = [(ds.replace('.csv', ''), 'dataset') for ds in datasets] + \
                [(diag.replace('.mmd', ''), 'diagram') for diag in diagrams]
    
    for item_stem, item_type in sorted(all_items, key=lambda x: x[0]):
        facet_id = f"{chapter}.{item_stem}"
        facets_lines.extend([
            f"(facet-{facet_id})=",
            f"### Facet: `{facet_id}`",
            f"Type: {item_type}",
            "",
        ])
    
    # Cross-references section
    xrefs = metadata.get('xrefs', [])
    if xrefs:
        xrefs_lines = ["## Cross-References\n"]
        for xref in xrefs:
            to = xref.get('to', '')
            xref_type = xref.get('type', '')
            evidence = xref.get('evidence', '')
            xrefs_lines.append(f"- **{xref_type}** → `{to}` (evidence: `{evidence}`)")
        xrefs_lines.append("")
    else:
        xrefs_lines = []
    
    # Assemble page
    frontmatter = [
        "---",
        f"title: {title}",
        "---",
        "",
    ]
    
    page_content = "\n".join(
        frontmatter +
        intro_lines +
        datasets_lines +
        diagrams_lines +
        xrefs_lines +
        facets_lines
    )
    
    index_path.write_text(page_content, encoding='utf-8')
    print(f"[OK] Generated {index_path.relative_to(ROOT)}")

def generate_xref_data(all_chapters: Dict[str, Dict[str, Any]]):
    """Generate cross-reference CSV and JSON."""
    ensure_dirs(DATA_DIR)
    
    csv_path = DATA_DIR / "xref.csv"
    json_path = DATA_DIR / "xref.json"
    
    edges = []
    
    for chapter, metadata in all_chapters.items():
        xrefs = metadata.get('xrefs', [])
        for xref in xrefs:
            to = xref.get('to', '')
            xref_type = xref.get('type', '')
            evidence = xref.get('evidence', '')
            
            if not to:
                continue
            
            # Parse 'to' as 'chapter.facet'
            to_parts = to.split('.', 1)
            to_chapter = to_parts[0] if len(to_parts) > 0 else ''
            to_facet = to if len(to_parts) > 1 else ''
            
            edges.append({
                'from_chapter': chapter,
                'from_facet': chapter,
                'to_chapter': to_chapter,
                'to_facet': to,
                'type': xref_type,
                'evidence_path': evidence,
                'note': ''
            })
    
    # Write CSV
    with csv_path.open('w', newline='', encoding='utf-8') as f:
        if edges:
            writer = csv.DictWriter(f, fieldnames=[
                'from_chapter', 'from_facet', 'to_chapter', 'to_facet',
                'type', 'evidence_path', 'note'
            ])
            writer.writeheader()
            writer.writerows(edges)
    
    print(f"[OK] Generated {csv_path.relative_to(ROOT)} with {len(edges)} edges")
    
    # Write JSON
    json_data = [
        {
            'from': {'c': e['from_chapter'], 'f': e['from_facet']},
            'to': {'c': e['to_chapter'], 'f': e['to_facet']},
            'type': e['type'],
            'evidence': e['evidence_path']
        }
        for e in edges
    ]
    
    json_path.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"[OK] Generated {json_path.relative_to(ROOT)}")

def generate_analytics(all_chapters: Dict[str, Dict[str, Any]], stats: Dict[str, Any]):
    """Generate analytics report."""
    ensure_dirs(ANALYTICS_DIR)
    
    # Per-chapter statistics CSV
    stats_path = ANALYTICS_DIR / "chapter_stats.csv"
    with stats_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['chapter', 'datasets_count', 'diagrams_count', 'xrefs_count', 'facets_count'])
        
        for chapter in sorted(all_chapters.keys()):
            ch_stats = stats.get(chapter, {})
            writer.writerow([
                chapter,
                ch_stats.get('datasets', 0),
                ch_stats.get('diagrams', 0),
                ch_stats.get('xrefs', 0),
                ch_stats.get('facets', 0)
            ])
    
    print(f"[OK] Generated {stats_path.relative_to(ROOT)}")
    
    # Summary report
    report_path = ANALYTICS_DIR / "summary.md"
    total_datasets = sum(s.get('datasets', 0) for s in stats.values())
    total_diagrams = sum(s.get('diagrams', 0) for s in stats.values())
    total_xrefs = sum(s.get('xrefs', 0) for s in stats.values())
    total_facets = sum(s.get('facets', 0) for s in stats.values())
    
    report_content = f"""---
title: Analytics Summary
generated: {datetime.now().isoformat()}
---

# Authoring Pipeline Analytics

## Summary Statistics

- **Total Chapters:** {len(all_chapters)}
- **Total Datasets:** {total_datasets}
- **Total Diagrams:** {total_diagrams}
- **Total Cross-References:** {total_xrefs}
- **Total Facets:** {total_facets}

## Per-Chapter Breakdown

```{{csv-table}} Chapter Statistics
:header-rows: 1
:file: ./chapter_stats.csv
:widths: auto
```

## Coverage

- Chapters with datasets: {sum(1 for s in stats.values() if s.get('datasets', 0) > 0)} / {len(all_chapters)}
- Chapters with diagrams: {sum(1 for s in stats.values() if s.get('diagrams', 0) > 0)} / {len(all_chapters)}
- Chapters with xrefs: {sum(1 for s in stats.values() if s.get('xrefs', 0) > 0)} / {len(all_chapters)}

---
*Generated by `scripts/generate_authoring_pipeline.py`*
"""
    
    report_path.write_text(report_content, encoding='utf-8')
    print(f"[OK] Generated {report_path.relative_to(ROOT)}")

def generate_main_index(all_chapters: Dict[str, Dict[str, Any]]):
    """Generate main authoring/index.md."""
    index_path = AUTHORING / "index.md"
    
    # Grid cards
    cards_lines = [
        ":::{grid} 1 1 2 3",
        ":gutter: 2",
        ""
    ]
    
    for chapter in sorted(all_chapters.keys()):
        metadata = all_chapters[chapter]
        title = metadata.get('title', chapter.replace('_', ' ').title())
        
        cards_lines.extend([
            f":::{{grid-item-card}} {title}",
            f":link: {chapter}/index",
            ":link-type: doc",
            ":shadow: md",
            f"{title} - datasets and diagrams embedded.",
            ":::",
            ""
        ])
    
    cards_lines.append(":::")
    
    # Toctree
    toc_lines = [
        "```{toctree}",
        ":caption: Chapters",
        ":maxdepth: 1",
        ":titlesonly:",
        ""
    ]
    
    for chapter in sorted(all_chapters.keys()):
        toc_lines.append(f"{chapter}/index")
    
    toc_lines.extend([
        "",
        "analytics/summary",
        "```"
    ])
    
    # Assemble
    content = """---
title: Authoring (embedded)
---

# Authoring - Embedded Documentation

All chapters from `docs/authoring/**` rendered inline with datasets and diagrams.

"""
    
    content += "\n".join(cards_lines) + "\n\n"
    content += "\n".join(toc_lines) + "\n"
    
    index_path.write_text(content, encoding='utf-8')
    print(f"[OK] Generated {index_path.relative_to(ROOT)}")

def main():
    """Main pipeline execution."""
    print("=" * 60)
    print("Authoring Pipeline Generator (01-10)")
    print("=" * 60)
    
    if not SOURCES.exists():
        print(f"[ERROR] Sources directory not found: {SOURCES}")
        return 1
    
    # Discover and parse chapter sources
    all_chapters = {}
    stats = {}
    
    source_files = sorted(SOURCES.glob("chapter_*.md"))
    if not source_files:
        print(f"[ERROR] No chapter_*.md files found in {SOURCES}")
        return 1
    
    print(f"\n[INFO] Found {len(source_files)} chapter source files\n")
    
    for source_file in source_files:
        print(f"Processing: {source_file.name}")
        content = source_file.read_text(encoding='utf-8')
        metadata = parse_frontmatter(content)
        
        chapter = metadata.get('chapter', '') or metadata.get('slug', '')
        if not chapter:
            print(f"  [WARN] No chapter/slug in frontmatter, skipping")
            continue
        
        all_chapters[chapter] = metadata
        
        # Process artifacts
        datasets, diagrams = process_chapter_artifacts(chapter, metadata)
        
        # Generate page
        generate_chapter_page(chapter, metadata, datasets, diagrams)
        
        # Track stats
        xrefs_count = len(metadata.get('xrefs', []))
        facets_count = len(datasets) + len(diagrams)
        stats[chapter] = {
            'datasets': len(datasets),
            'diagrams': len(diagrams),
            'xrefs': xrefs_count,
            'facets': facets_count
        }
        
        print()
    
    # Generate cross-references
    print("\n[Phase 3] Generating cross-references...")
    generate_xref_data(all_chapters)
    
    # Generate analytics
    print("\n[Phase 4] Generating analytics...")
    generate_analytics(all_chapters, stats)
    
    # Generate main index
    print("\n[Phase 5] Generating main index...")
    generate_main_index(all_chapters)
    
    print("\n" + "=" * 60)
    print("Pipeline completed successfully!")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
