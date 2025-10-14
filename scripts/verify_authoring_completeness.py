#!/usr/bin/env python3
"""
Verify completeness of authoring documentation for chapters 01-10.

This script checks that all required sections and elements are present:
- Datasets section with CSV tables and facet links
- Diagrams section with Mermaid diagrams and clickable nodes
- Podkatalogi section with toctree (where applicable)
- Crosslinks section (where source metadata exists)
- Appendix/Facets section with proper anchors
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"

def check_chapter(chapter_dir):
    """Check a single chapter for completeness."""
    chapter = chapter_dir.name
    index_file = chapter_dir / "index.md"
    
    if not index_file.exists():
        return {
            "chapter": chapter,
            "status": "MISSING",
            "errors": ["index.md file not found"]
        }
    
    content = index_file.read_text(encoding="utf-8")
    errors = []
    warnings = []
    
    # Check required sections
    required_sections = [
        "## Datasets",
        "## Diagrams",
        "## Appendix / Facets"
    ]
    
    for section in required_sections:
        if section not in content:
            errors.append(f"Missing required section: {section}")
    
    # Check for CSV tables with facet links
    csv_tables = re.findall(r'\{csv-table\}', content)
    facet_links = re.findall(r'\*Facet:\*.*\[`([^`]+)`\]', content)
    
    if not csv_tables and "## Datasets" in content:
        warnings.append("Datasets section has no CSV tables")
    
    # Check for Mermaid diagrams with init
    mermaid_blocks = re.findall(r'\{mermaid\}', content)
    mermaid_inits = re.findall(r'%%\{init:', content)
    
    if mermaid_blocks and len(mermaid_inits) < len(mermaid_blocks):
        warnings.append(f"Some Mermaid diagrams missing init block ({len(mermaid_inits)}/{len(mermaid_blocks)})")
    
    # Check for clickable nodes in diagrams
    click_nodes = re.findall(r'click\s+\w+', content)
    if mermaid_blocks and not click_nodes:
        warnings.append("Mermaid diagrams have no clickable nodes")
    
    # Check for subdirectories section (optional)
    has_subdirs = len([d for d in chapter_dir.iterdir() 
                       if d.is_dir() and d.name not in ["datasets", "diagrams"] 
                       and not d.name.startswith(".")]) > 0
    has_podkatalogi = "## Podkatalogi" in content
    
    if has_subdirs and not has_podkatalogi:
        warnings.append("Chapter has subdirectories but no Podkatalogi section")
    
    # Check for crosslinks (optional, depends on source metadata)
    has_crosslinks = "## Crosslinks" in content or "## Cross-References" in content
    
    # Check facet anchors
    facet_anchors = re.findall(r'\(facet-([^)]+)\)=', content)
    
    if not facet_anchors:
        warnings.append("No facet anchors found")
    
    status = "ERROR" if errors else ("WARNING" if warnings else "OK")
    
    return {
        "chapter": chapter,
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "stats": {
            "csv_tables": len(csv_tables),
            "facet_links": len(facet_links),
            "mermaid_diagrams": len(mermaid_blocks),
            "clickable_nodes": len(click_nodes),
            "facet_anchors": len(facet_anchors),
            "has_podkatalogi": has_podkatalogi,
            "has_crosslinks": has_crosslinks
        }
    }

def main():
    """Check all chapters 01-10."""
    chapter_pattern = re.compile(r'^(0[1-9]|1[0-2])_.*$')
    
    chapters = []
    for d in sorted(AUTHORING.iterdir()):
        if d.is_dir() and chapter_pattern.match(d.name):
            chapters.append(d)
    
    if not chapters:
        print("ERROR: No chapters found!")
        return 1
    
    print(f"Checking {len(chapters)} chapters...\n")
    
    results = []
    for chapter_dir in chapters:
        result = check_chapter(chapter_dir)
        results.append(result)
    
    # Print summary
    ok_count = sum(1 for r in results if r["status"] == "OK")
    warning_count = sum(1 for r in results if r["status"] == "WARNING")
    error_count = sum(1 for r in results if r["status"] == "ERROR")
    
    print("=" * 80)
    print(f"SUMMARY: {ok_count} OK, {warning_count} warnings, {error_count} errors")
    print("=" * 80)
    
    # Print details
    for result in results:
        status_symbol = {
            "OK": "✓",
            "WARNING": "⚠",
            "ERROR": "✗",
            "MISSING": "✗"
        }.get(result["status"], "?")
        
        print(f"\n{status_symbol} {result['chapter']:30s} [{result['status']}]")
        
        stats = result.get("stats", {})
        if stats:
            print(f"  Stats: {stats['csv_tables']} CSV, {stats['mermaid_diagrams']} diagrams, "
                  f"{stats['facet_anchors']} facets")
            features = []
            if stats.get('has_podkatalogi'):
                features.append("Podkatalogi")
            if stats.get('has_crosslinks'):
                features.append("Crosslinks")
            if features:
                print(f"  Features: {', '.join(features)}")
        
        for error in result.get("errors", []):
            print(f"  ERROR: {error}")
        
        for warning in result.get("warnings", []):
            print(f"  WARNING: {warning}")
    
    print("\n" + "=" * 80)
    
    return 0 if error_count == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
