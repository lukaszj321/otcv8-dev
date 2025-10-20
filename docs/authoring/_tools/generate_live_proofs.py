#!/usr/bin/env python3
"""
Generate LIVE proofs for documentation build
- Saves _sources/ diffs
- Documents verification steps
"""

import random
from pathlib import Path
from typing import List

# Repository root
REPO_ROOT = Path(__file__).resolve().parents[3]
BUILD_DIR = REPO_ROOT / "docs" / "_build" / "html"
AUTHORING_DIR = REPO_ROOT / "docs" / "authoring"
PROOFS_DIR = AUTHORING_DIR / "_proofs"
ANALYTICS_DIR = AUTHORING_DIR / "analytics"

# All chapter directories (01-15 plus special ones)
CHAPTERS = [
    "01_core", "01_runtime", "02_events", "03_modules", "04_ui", "05_events",
    "05_network", "06_assets", "07_settings_crypto", "08_audio", "09_logging",
    "10_game_runtime", "11_data", "12_otmod", "13_layouts", "14_android", "15_vc16"
]

def save_source_diff(chapter: str) -> bool:
    """
    Save _sources diff for a chapter
    Returns True if successful
    """
    # Path to built _sources file
    sources_file = BUILD_DIR / "_sources" / "authoring" / chapter / "index.md.txt"
    
    if not sources_file.exists():
        print(f"  ✗ Sources file not found: {sources_file}")
        return False
    
    # Path to original markdown
    original_file = AUTHORING_DIR / chapter / "index.md"
    
    if not original_file.exists():
        print(f"  ✗ Original file not found: {original_file}")
        return False
    
    # Create proof directory for chapter
    chapter_proof_dir = PROOFS_DIR / chapter
    chapter_proof_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy _sources file
    sources_content = sources_file.read_text(encoding='utf-8')
    output_file = chapter_proof_dir / "index.md.txt"
    output_file.write_text(sources_content, encoding='utf-8')
    
    # Generate diff report
    original_content = original_file.read_text(encoding='utf-8')
    
    diff_file = ANALYTICS_DIR / f"index_diff_{chapter}.md"
    ANALYTICS_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(diff_file, 'w', encoding='utf-8') as f:
        f.write(f"# Source Diff: {chapter}\n\n")
        f.write(f"**Chapter:** `{chapter}`\n")
        f.write(f"**Original:** `docs/authoring/{chapter}/index.md`\n")
        f.write(f"**Built Source:** `_sources/authoring/{chapter}/index.md.txt`\n\n")
        
        # Check for key differences
        orig_has_mermaid_directive = '```{mermaid}' in original_content
        sources_has_mermaid_directive = '```{mermaid}' in sources_content
        
        orig_has_mermaid_backtick = '```mermaid' in original_content and '```{mermaid}' not in original_content
        
        f.write("## Key Checks\n\n")
        f.write(f"- Original uses `{{mermaid}}` directive: **{orig_has_mermaid_directive}**\n")
        f.write(f"- Built source has `{{mermaid}}` directive: **{sources_has_mermaid_directive}**\n")
        f.write(f"- Original has plain ```mermaid: **{orig_has_mermaid_backtick}**\n\n")
        
        if orig_has_mermaid_directive and sources_has_mermaid_directive:
            f.write("✓ **PASS**: Mermaid directive syntax preserved in build\n\n")
        elif orig_has_mermaid_backtick:
            f.write("✗ **FAIL**: Original still uses plain ```mermaid (should be converted)\n\n")
        else:
            f.write("⚠ **INFO**: No Mermaid diagrams in this chapter\n\n")
        
        # Count mermaid blocks
        orig_count = original_content.count('```{mermaid}')
        sources_count = sources_content.count('```{mermaid}')
        
        f.write(f"## Mermaid Block Counts\n\n")
        f.write(f"- Original: {orig_count}\n")
        f.write(f"- Built: {sources_count}\n\n")
        
        if orig_count == sources_count:
            f.write("✓ Counts match\n")
        else:
            f.write(f"⚠ Count mismatch (diff: {abs(orig_count - sources_count)})\n")
    
    print(f"  ✓ Diff saved: {diff_file.relative_to(REPO_ROOT)}")
    return True

def generate_proof_readme():
    """Generate README for proofs directory"""
    PROOFS_DIR.mkdir(parents=True, exist_ok=True)
    
    readme = PROOFS_DIR / "README.md"
    with open(readme, 'w', encoding='utf-8') as f:
        f.write("# LIVE Proofs Directory\n\n")
        f.write("This directory contains proof artifacts from the documentation build.\n\n")
        f.write("## Contents\n\n")
        f.write("- `<chapter>/index.md.txt` - Built _sources files from Sphinx\n")
        f.write("- `<chapter>/screenshot.png` - Screenshots of rendered pages (manual)\n\n")
        f.write("## Verification\n\n")
        f.write("Compare these files with:\n")
        f.write("- Original: `docs/authoring/<chapter>/index.md`\n")
        f.write("- Diff reports: `docs/authoring/analytics/index_diff_<chapter>.md`\n\n")
        f.write("## Screenshots\n\n")
        f.write("Screenshots should show:\n")
        f.write("1. Mermaid diagrams rendered as visual diagrams (not code)\n")
        f.write("2. Grid/card layouts from sphinx-design working\n")
        f.write("3. No raw fence blocks or unprocessed directives\n")

def select_random_chapters(count: int = 5) -> List[str]:
    """Select random chapters for diff verification"""
    available = [ch for ch in CHAPTERS if (AUTHORING_DIR / ch / "index.md").exists()]
    
    if len(available) <= count:
        return available
    
    return random.sample(available, count)

def main():
    """Main entry point"""
    print("LIVE Proofs Generator")
    print("=" * 60)
    
    # Generate README
    generate_proof_readme()
    
    # Select chapters for verification
    selected = select_random_chapters(5)
    
    print(f"\nGenerating proofs for {len(selected)} chapters:")
    for ch in selected:
        print(f"  - {ch}")
    print()
    
    success_count = 0
    for chapter in selected:
        print(f"Processing {chapter}...")
        if save_source_diff(chapter):
            success_count += 1
    
    print()
    print("=" * 60)
    print(f"Generated {success_count}/{len(selected)} proof diffs")
    
    if success_count < len(selected):
        print("\n⚠ Some chapters failed. Build may be incomplete.")
    else:
        print("\n✓ All selected chapters processed successfully")
    
    print(f"\n📁 Proofs saved to: {PROOFS_DIR.relative_to(REPO_ROOT)}")
    print(f"📊 Diff reports in: {ANALYTICS_DIR.relative_to(REPO_ROOT)}")
    print("\n📸 Note: Screenshots must be captured manually from the live site")
    print("    Save as: docs/authoring/_proofs/<chapter>/screenshot.png")

if __name__ == "__main__":
    main()
