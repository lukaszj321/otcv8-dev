#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enrich chapter index.md files with intro text from _sources/*.md
Extracts 2-4 sentence intros and adds them after the title.
"""

import re
import yaml
from pathlib import Path
from typing import Dict, Optional

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"
SOURCES = AUTHORING / "_sources"

# Mapping of chapter numbers to directories

def parse_source_file(source_path: Path) -> Dict[str, str]:
    """Extract metadata and intro from source file."""
    content = source_path.read_text(encoding='utf-8')
    
    # Parse frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return {}
    
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"[WARN] YAML parse error in {source_path}: {e}")
        return {}
    
    body = match.group(2).strip()
    
    # Extract a concise intro (first meaningful paragraph or executive summary)
    intro = extract_intro(body, meta)
    
    return {
        "chapter": meta.get("chapter", ""),
        "title": meta.get("title", ""),
        "intro": intro
    }

def extract_intro(body: str, meta: Dict) -> str:
    """Extract 2-4 sentence intro from body text."""
    # Strategy 1: Look for executive summary section
    exec_match = re.search(r'### 0\) Executive summary\s*\n\s*\n(.*?)(?=\n###|\n---|\Z)', body, re.DOTALL)
    if exec_match:
        exec_text = exec_match.group(1).strip()
        # Get first bullet point or paragraph
        lines = [l.strip() for l in exec_text.split('\n') if l.strip()]
        if lines:
            first_item = lines[0]
            # Clean up bullet points
            first_item = re.sub(r'^[-*]\s+', '', first_item)
            # Extract just the "Co:" part if it exists
            if 'Co:' in first_item:
                first_item = first_item.split('Co:', 1)[1].strip()
            # Limit to first sentence or two
            sentences = re.split(r'[.;]\s+', first_item)
            intro = '. '.join(sentences[:2]) + '.'
            intro = intro.replace('..', '.')
            return intro
    
    # Strategy 2: Look for first paragraph after first heading
    para_match = re.search(r'#[^#].*?\n\s*\n([^#\n][^\n]*(?:\n[^#\n][^\n]*){0,2})', body)
    if para_match:
        para = para_match.group(1).strip()
        # Clean up
        para = re.sub(r'\(facet-[^)]+\)=', '', para)
        para = re.sub(r'##[^\n]*\n', '', para)
        para = para.strip()
        if len(para) > 20 and not para.startswith('-'):
            sentences = re.split(r'[.;]\s+', para)
            intro = '. '.join(sentences[:2]) + '.'
            intro = intro.replace('..', '.')
            return intro
    
    # Strategy 3: Use title as description
    title = meta.get("title", "")
    if title:
        return f"Ten rozdział dokumentuje {title.lower()}."
    
    return ""

def add_intro_to_index(chapter_dir: Path, intro: str):
    """Add intro text to chapter index.md file."""
    index_path = chapter_dir / "index.md"
    if not index_path.exists():
        print(f"[SKIP] {index_path} not found")
        return False
    
    content = index_path.read_text(encoding='utf-8')
    
    # Check if intro already exists (look for text between title and TOC)
    # Pattern to check: title, then directly ```{contents} with only blank line between
    if not re.search(r'# \d+_\w+[^\n]*\n\n```\{contents\}', content):
        print(f"[SKIP] {chapter_dir.name} already has intro content")
        return False
    
    if not intro:
        print(f"[SKIP] {chapter_dir.name} - no intro text extracted")
        return False
    
    # Find the position to insert (after title, before TOC)
    # Pattern: title line, blank line, then ```{contents}
    pattern = r'(# \d+_\w+[^\n]*\n)(\n)(```\{contents\})'
    
    # Create intro block
    intro_block = f"\n{intro}\n"
    
    # Replace
    new_content = re.sub(pattern, r'\1' + intro_block + r'\n\3', content, count=1)
    
    if new_content == content:
        print(f"[SKIP] {chapter_dir.name} - pattern not matched")
        return False
    
    index_path.write_text(new_content, encoding='utf-8')
    print(f"[OK] Added intro to {chapter_dir.name}")
    return True

def main():
    """Main execution."""
    print("Enriching chapter intros from _sources...")
    
    # Process each source file
    updated = 0
    for source_file in sorted(SOURCES.glob("chapter_*.md")):
        print(f"\n[PROCESS] {source_file.name}")
        
        # Parse source
        data = parse_source_file(source_file)
        if not data or not data.get("chapter"):
            print(f"[WARN] Could not extract metadata from {source_file.name}")
            continue
        
        chapter = data["chapter"]
        intro = data["intro"]
        
        print(f"  Chapter: {chapter}")
        print(f"  Title: {data['title']}")
        print(f"  Intro: {intro[:80]}..." if intro else "  No intro extracted")
        
        # Find corresponding chapter directory
        chapter_dir = AUTHORING / chapter
        if not chapter_dir.exists():
            print(f"[WARN] Chapter directory not found: {chapter_dir}")
            continue
        
        # Add intro to index
        if add_intro_to_index(chapter_dir, intro):
            updated += 1
    
    print(f"\n[SUMMARY] Updated {updated} chapters")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
