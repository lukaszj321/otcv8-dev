#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
attach_unused_artifacts.py

Idempotent helper for OTClient authoring docs:
- attaches any missing CSVs (datasets/*.csv) and MMDs (diagrams/*.mmd) to chapter pages
- appends subdirectory toctrees (excluding datasets/, diagrams/)
- ensures facet anchors for all datasets/diagrams
- writes a concise report with per-chapter stats

Markers this script manages (do not edit manually):
  <!-- AUTO:DATASETS START/END -->
  <!-- AUTO:DIAGRAMS START/END -->
  <!-- AUTO:APPENDIX START/END -->
  <!-- AUTO:TOCTREE START/END -->
"""

from __future__ import annotations
import re
from pathlib import Path
from typing import List

DOCS_ROOT = Path("docs")
AUTHORING = DOCS_ROOT / "authoring"
EXCLUDE_SUBDIRS = {"datasets", "diagrams", "_assets", "_includes"}

MARK_DATASETS = ("<!-- AUTO:DATASETS START -->", "<!-- AUTO:DATASETS END -->")
MARK_DIAGRAMS  = ("<!-- AUTO:DIAGRAMS START -->", "<!-- AUTO:DIAGRAMS END -->")
MARK_APPX      = ("<!-- AUTO:APPENDIX START -->", "<!-- AUTO:APPENDIX END -->")
MARK_TOCTREE   = ("<!-- AUTO:TOCTREE START -->", "<!-- AUTO:TOCTREE END -->")

INIT_MERMAID = "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%"

def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""

def write_text(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")

def between_markers(text: str, start: str, end: str, new_body: str) -> str:
    # insert/replace a block between markers; if absent, append at the end
    if start in text and end in text and text.index(start) < text.index(end):
        pre = text.split(start)[0]
        post = text.split(end)[-1]
        return f"{pre}{start}\n{new_body}\n{end}{post}"
    return text.rstrip() + f"\n\n{start}\n{new_body}\n{end}\n"

def ensure_section_heading(text: str, heading: str) -> str:
    if re.search(rf"^##\s+{re.escape(heading)}\s*$", text, flags=re.MULTILINE):
        return text
    return text.rstrip() + f"\n\n## {heading}\n"

def ensure_title_frontmatter(text: str, chapter_slug: str) -> str:
    lines = text.splitlines()
    if lines and (lines[0].startswith('---') or lines[0].startswith('# ')):
        return text
    title = f"# {chapter_slug} — Authoring"
    return f"{title}\n\n" + text

def md_has_reference(md: str, rel_path: str, basename: str) -> bool:
    return (basename in md) or (rel_path in md) or (('./' + rel_path) in md)

def make_csv_block(chapter: str, rel_csv: str) -> str:
    stem = Path(rel_csv).stem
    facet = f"{chapter}.{stem}"
    return (
f"""#### `{stem}`
*Facet:* [`{facet}`](#facet-{facet})

```{{csv-table}} {stem}
:header-rows: 1
:file: ./{rel_csv}
:widths: auto
```
""".strip()
    )

def make_mermaid_block(chapter: str, rel_mmd: str, content: str) -> str:
    stem = Path(rel_mmd).stem
    facet = f"{chapter}.{stem}"
    click_hint = f'click Root "./index.html#facet-{facet}" "Open {stem}"'
    hint = ""
    if "click " not in content:
        hint = f"\n{click_hint}"
    return (
f"""#### `{stem}`
*Facet:* [`{facet}`](#facet-{facet})

```{{mermaid}}
{INIT_MERMAID}
{content}{hint}
```
""".strip()
    )

def make_appendix_block(chapter: str, csv_stems: List[str], mmd_stems: List[str]) -> str:
    lines = []
    lines.append("### Facets")
    for s in sorted(csv_stems):
        facet = f"{chapter}.{s}"
        lines.append(f"(facet-{facet})=\n#### Facet: `{facet}`\nType: dataset\n")
    for s in sorted(mmd_stems):
        facet = f"{chapter}.{s}"
        lines.append(f"(facet-{facet})=\n#### Facet: `{facet}`\nType: diagram\n")
    return "\n".join(lines).strip()

def make_toctree_block(chapter_dir: Path, current_md: str) -> str:
    subdirs = [p.name for p in chapter_dir.iterdir() if p.is_dir() and p.name not in EXCLUDE_SUBDIRS]
    subdirs = sorted(subdirs)
    if not subdirs:
        return "_(no subdirectories)_"
    block = ["```{toctree}", ":titlesonly:", ":maxdepth: 1", ""]
    for s in subdirs:
        block.append(f"{s}/index")
    block.append("```")
    return "\n".join(block)

def main() -> None:
    assert AUTHORING.exists(), f"Missing directory: {AUTHORING}"
    report_lines = []
    total_added_csv = 0
    total_added_mmd = 0
    chapters_processed = 0
    chapters_with_subdirs = 0

    for chapter_dir in sorted([p for p in AUTHORING.iterdir() if p.is_dir()]):
        chapter = chapter_dir.name
        index_md = chapter_dir / "index.md"
        if not index_md.exists():
            write_text(index_md, f"# {chapter}\n\n")
        content = read_text(index_md)
        content = ensure_title_frontmatter(content, chapter)

        csvs = sorted((chapter_dir / "datasets").glob("*.csv")) if (chapter_dir / "datasets").exists() else []
        mmds = sorted((chapter_dir / "diagrams").glob("*.mmd")) if (chapter_dir / "diagrams").exists() else []

        missing_csv_blocks = []
        csv_stems_in_appendix = []
        for csv in csvs:
            rel = csv.relative_to(chapter_dir).as_posix()
            if not md_has_reference(content, rel, csv.name):
                missing_csv_blocks.append(make_csv_block(chapter, rel))
                total_added_csv += 1
            csv_stems_in_appendix.append(csv.stem)

        missing_mmd_blocks = []
        mmd_stems_in_appendix = []
        for mmd in mmds:
            rel = mmd.relative_to(chapter_dir).as_posix()
            diagram_src = read_text(mmd).strip()
            if not md_has_reference(content, rel, mmd.name):
                missing_mmd_blocks.append(make_mermaid_block(chapter, rel, diagram_src))
                total_added_mmd += 1
            mmd_stems_in_appendix.append(mmd.stem)

        content = ensure_section_heading(content, "Datasets")
        datasets_body = "\n\n".join(missing_csv_blocks) if missing_csv_blocks else "_(all CSV already attached)_"
        content = between_markers(content, MARK_DATASETS[0], MARK_DATASETS[1], datasets_body)

        content = ensure_section_heading(content, "Diagrams")
        diagrams_body = "\n\n".join(missing_mmd_blocks) if missing_mmd_blocks else "_(all diagrams already attached)_"
        content = between_markers(content, MARK_DIAGRAMS[0], MARK_DIAGRAMS[1], diagrams_body)

        content = ensure_section_heading(content, "Appendix / Facets")
        appendix_body = make_appendix_block(chapter, csv_stems_in_appendix, mmd_stems_in_appendix)
        content = between_markers(content, MARK_APPX[0], MARK_APPX[1], appendix_body)

        subdirs = [p.name for p in chapter_dir.iterdir() if p.is_dir() and p.name not in EXCLUDE_SUBDIRS]
        if subdirs:
            chapters_with_subdirs += 1
            content = ensure_section_heading(content, "Podkatalogi")
            toctree_body = make_toctree_block(chapter_dir, content)
            content = between_markers(content, MARK_TOCTREE[0], MARK_TOCTREE[1], toctree_body)

        write_text(index_md, content)
        chapters_processed += 1

        report_lines.append(
            f"- {chapter}: +CSV={len(missing_csv_blocks)}, +MMD={len(missing_mmd_blocks)}, subdirs={len(subdirs)}"
        )

    rpt = [
        "# Authoring — auto-attach report",
        "",
        f"- Chapters processed: **{chapters_processed}**",
        f"- CSV blocks added: **{total_added_csv}**",
        f"- Mermaid blocks added: **{total_added_mmd}**",
        f"- Chapters with subdirs updated: **{chapters_with_subdirs}**",
        "",
        "## Per chapter",
        *report_lines
    ]
    write_text(AUTHORING / "_reports" / "auto_attach_report.md", "\n".join(rpt))
    print("OK: attach_unused_artifacts finished.")
    print(f"Chapters: {chapters_processed}, CSV added: {total_added_csv}, MMD added: {total_added_mmd}")
    print(f"Report: {AUTHORING / '_reports' / 'auto_attach_report.md'}")

if __name__ == "__main__":
    main()
