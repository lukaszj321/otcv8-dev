#!/usr/bin/env python3
# coding: utf-8
"""
Generator stron Authoring -> z docs/reposzablony/** do docs/authoring/**
- Renderuje CSV (summary.csv, entities.csv) i Mermaid (flow.mmd, architecture.mmd) na JEDNEJ stronie
- Nie linkuje do GitHuba; ładuje pliki lokalnie z docs/reposzablony
- Dokłada toctree do wszystkich *.md w rozdziale, aby menu widziało pełną zawartość
"""

import os
import pathlib
from pathlib import Path

DOCS = Path("docs")
SRC  = DOCS / "reposzablony"
DST  = DOCS / "authoring"

def as_docname(md_path: Path) -> str:
    """Zwraca ścieżkę dokumentu względem docs/, bez rozszerzenia .md (tak lubi Sphinx)."""
    p = md_path.as_posix()
    if p.startswith("docs/"):
        p = p[5:]
    if p.endswith(".md"):
        p = p[:-3]
    return p

def write(dst: Path, text: str):
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")

def discover_chapters(base: Path):
    """Zwraca listę katalogów (rozdziałów) bez ukrytych, posortowaną."""
    if not base.exists():
        return []
    items = []
    for p in sorted(base.iterdir()):
        if p.is_dir() and not p.name.startswith("."):
            items.append(p)
    return items

def discover_md_list(chapter_dir: Path):
    """Zwraca listę ścieżek *.md w rozdziale (względem docs/), posortowane."""
    md_files = []
    for root, _, files in os.walk(chapter_dir):
        for f in files:
            if f.lower().endswith(".md"):
                full = Path(root) / f
                md_files.append(full)
    md_files = sorted(md_files)
    # Zamień na docnames względem docs/
    docnames = [as_docname(p) for p in md_files]
    return docnames

def page_for_chapter(chapter: Path) -> str:
    """Generuje treść index.md dla pojedynczego rozdziału."""
    name = chapter.name  # np. 01_core
    # Ścieżki do danych i diagramów
    s_summary = chapter / "datasets" / "summary.csv"
    s_entities = chapter / "datasets" / "entities.csv"
    d_flow = chapter / "diagrams" / "flow.mmd"
    d_arch = chapter / "diagrams" / "architecture.mmd"

    # Relatywne ścieżki od docs/authoring/<name>/index.md do plików źródłowych:
    rel_summary = f"../../reposzablony/{name}/datasets/summary.csv"
    rel_entities = f"../../reposzablony/{name}/datasets/entities.csv"
    rel_flow     = f"../../reposzablony/{name}/diagrams/flow.mmd"
    rel_arch     = f"../../reposzablony/{name}/diagrams/architecture.mmd"

    lines = []
    lines.append(f"---\ntitle: {name} — Authoring\n---\n")
    lines.append(f"# {name}\n")

    # Datasets
    lines.append("## Datasets")
    if s_summary.exists():
        lines.append("::::{dropdown} Summary (`datasets/summary.csv`)")
        lines.append("```{csv-table}")
        lines.append(':header: "Key","Value","Notes"')
        lines.append(f":file: {rel_summary}")
        lines.append(":widths: 30, 30, 40")
        lines.append("```")
        lines.append("::::\n")
    else:
        lines.append("> _Brak_ `datasets/summary.csv`\n")

    if s_entities.exists():
        lines.append("::::{dropdown} Entities (`datasets/entities.csv`)")
        lines.append("```{csv-table}")
        lines.append(':header: "Entity","Count","Meta"')
        lines.append(f":file: {rel_entities}")
        lines.append(":widths: 40, 20, 40")
        lines.append("```")
        lines.append("::::\n")
    else:
        lines.append("> _Brak_ `datasets/entities.csv`\n")

    # Diagrams
    lines.append("## Diagrams")
    if d_flow.exists():
        lines.append("::::{dropdown} Flow (`diagrams/flow.mmd`)")
        lines.append("```{mermaid}")
        lines.append(f"{{include}} {rel_flow}")
        lines.append("```")
        lines.append("::::\n")
    else:
        lines.append("> _Brak_ `diagrams/flow.mmd`\n")

    if d_arch.exists():
        lines.append("::::{dropdown} Architecture (`diagrams/architecture.mmd`)")
        lines.append("```{mermaid}")
        lines.append(f"{{include}} {rel_arch}")
        lines.append("```")
        lines.append("::::\n")
    else:
        lines.append("> _Brak_ `diagrams/architecture.mmd`\n")

    # ToC z całej zawartości rozdziału (wszystkie .md)
    docnames = [d for d in discover_md_list(chapter) if not d.startswith("authoring/")]
    if docnames:
        lines.append("\n## Powiązane dokumenty\n")
        lines.append("```{toctree}")
        lines.append(":maxdepth: 2")
        lines.append(":titlesonly:\n")
        for d in docnames:
            # Pokaż tylko w obrębie reposzablony/<name>/...
            if d.startswith(f"reposzablony/{name}/"):
                lines.append(d)
        lines.append("```")
    return "\n".join(lines).strip() + "\n"

def build_authoring():
    chapters = discover_chapters(SRC)
    # Strona główna Authoring z listą rozdziałów:
    index_lines = []
    index_lines.append("---\ntitle: Authoring – rozdziały (AUTO)\n---\n")
    index_lines.append("# Authoring (AUTO)\n")
    index_lines.append("```{toctree}\n:caption: Rozdziały\n:maxdepth: 1\n")
    for ch in chapters:
        index_lines.append(f"{ch.name}/index")
    index_lines.append("```\n")
    write(DST / "index.md", "\n".join(index_lines))

    # Każdy rozdział
    for ch in chapters:
        out = page_for_chapter(ch)
        write(DST / ch.name / "index.md", out)

if __name__ == "__main__":
    build_authoring()
    print("OK: generated docs/authoring/* from docs/reposzablony/*")
