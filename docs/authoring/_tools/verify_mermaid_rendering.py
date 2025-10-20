#!/usr/bin/env python3
"""
Mermaid Rendering Verification Tool
Scans HTML output to verify Mermaid diagrams are properly rendered.
"""

import csv
import re
from pathlib import Path
from typing import List, Tuple

# Repository root
REPO_ROOT = Path(__file__).resolve().parents[3]
BUILD_DIR = REPO_ROOT / "docs" / "_build" / "html" / "authoring"
QA_DIR = REPO_ROOT / "docs" / "authoring" / "qa"
ANALYTICS_DIR = REPO_ROOT / "docs" / "authoring" / "analytics"

def check_mermaid_rendering(html_file: Path) -> Tuple[bool, str]:
    """
    Check if an HTML file has properly rendered Mermaid diagrams.
    Returns: (found_mermaid: bool, notes: str)
    """
    try:
        content = html_file.read_text(encoding='utf-8', errors='ignore')
        
        # Look for multiple patterns that indicate successful Mermaid rendering:
        # 1. <div class="mermaid"> or <pre class="mermaid">
        # 2. <svg ...> elements with mermaid-related classes/attributes
        # 3. Mermaid-generated SVG content
        
        patterns = [
            r'<div[^>]*class="[^"]*mermaid[^"]*"',
            r'<pre[^>]*class="[^"]*mermaid[^"]*"',
            r'<svg[^>]*class="[^"]*mermaid[^"]*"',
            r'<svg[^>]*id="[^"]*mermaid[^"]*"',
            # Look for SVG with typical Mermaid structure
            r'<svg[^>]*><defs[^>]*>.*?</defs>.*?<g[^>]*class="[^"]*output[^"]*"',
        ]
        
        found = False
        matched_patterns = []
        
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
                found = True
                matched_patterns.append(pattern[:50])
        
        # Also check if there are code blocks that should have been Mermaid
        # but weren't rendered (e.g., <pre><code class="language-mermaid">)
        code_block_pattern = r'<pre[^>]*><code[^>]*class="[^"]*language-mermaid[^"]*"'
        unrendered = re.search(code_block_pattern, content, re.IGNORECASE)
        
        if unrendered and not found:
            return False, "Found unrendered mermaid code blocks"
        elif found:
            count = len(re.findall(r'<(?:div|pre|svg)[^>]*(?:class|id)="[^"]*mermaid[^"]*"', content, re.IGNORECASE))
            return True, f"Found {count} rendered mermaid diagram(s)"
        else:
            # Check if file has any mermaid references at all
            if 'mermaid' in content.lower():
                return False, "Has 'mermaid' text but no rendered diagrams"
            else:
                return True, "No mermaid diagrams expected"
                
    except Exception as e:
        return False, f"Error reading file: {e}"

def scan_html_output() -> List[Tuple[str, bool, str]]:
    """
    Scan all index.html files in the authoring build output.
    Returns: List of (page_path, found_mermaid, notes)
    """
    results = []
    
    if not BUILD_DIR.exists():
        print(f"✗ Build directory not found: {BUILD_DIR}")
        return results
    
    # Find all index.html files
    for html_file in BUILD_DIR.rglob("index.html"):
        rel_path = html_file.relative_to(BUILD_DIR)
        found, notes = check_mermaid_rendering(html_file)
        results.append((str(rel_path), found, notes))
    
    return results

def generate_report(results: List[Tuple[str, bool, str]]):
    """Generate CSV report of Mermaid rendering status"""
    QA_DIR.mkdir(parents=True, exist_ok=True)
    
    output_file = QA_DIR / "mermaid_render_matrix.csv"
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['page', 'found_mermaid', 'notes'])
        
        for page, found, notes in results:
            writer.writerow([page, str(found).lower(), notes])
    
    print(f"✓ Report written to: {output_file.relative_to(REPO_ROOT)}")
    
    # Generate summary
    total = len(results)
    passed = sum(1 for _, found, _ in results if found)
    failed = total - passed
    
    print(f"\n=== Summary ===")
    print(f"Total pages: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        print(f"\n✗ {failed} page(s) failed Mermaid rendering check:")
        for page, found, notes in results:
            if not found:
                print(f"  - {page}: {notes}")
        return False
    else:
        print("\n✓ All pages passed Mermaid rendering check!")
        return True

def generate_gaps_report(results: List[Tuple[str, bool, str]]):
    """Generate gaps report for failed pages"""
    ANALYTICS_DIR.mkdir(parents=True, exist_ok=True)
    
    failed = [(page, notes) for page, found, notes in results if not found]
    
    if not failed:
        return
    
    output_file = ANALYTICS_DIR / "gaps.md"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Mermaid Rendering Gaps\n\n")
        f.write(f"**Generated:** {Path(__file__).name}\n\n")
        f.write(f"**Total Failed Pages:** {len(failed)}\n\n")
        f.write("## Failed Pages\n\n")
        
        for page, notes in failed:
            f.write(f"- **{page}**\n")
            f.write(f"  - Reason: {notes}\n\n")
    
    print(f"✓ Gaps report written to: {output_file.relative_to(REPO_ROOT)}")

def main():
    """Main entry point"""
    print("Mermaid Rendering Verification Tool")
    print("=" * 60)
    print(f"Scanning: {BUILD_DIR}")
    print()
    
    if not BUILD_DIR.exists():
        print(f"✗ Build directory not found: {BUILD_DIR}")
        print("  Please build the documentation first with: sphinx-build -b html docs docs/_build/html")
        return False
    
    results = scan_html_output()
    
    if not results:
        print("✗ No HTML files found in build directory")
        return False
    
    print(f"Found {len(results)} HTML pages to check\n")
    
    success = generate_report(results)
    generate_gaps_report(results)
    
    return success

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
