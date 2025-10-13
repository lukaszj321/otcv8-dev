#!/usr/bin/env python3
# coding: utf-8
"""
Authoring generator (FIXED):
- Źródło: docs/reposzablony/** (01_core, 01_runtime, 02_events, ...)
- Cel:    docs/authoring/** 
Renderuje NA STRONIE:
  • CSV -> csv-table (summary.csv, entities.csv)
  • Mermaid -> inline (flow.mmd, architecture.mmd)
  • ToC do wszystkich *.md z rozdziału (żeby nawigacja łapała zawartość)
Czyści docs/authoring przed generowaniem (hard reset).
"""

from pathlib import Path
import shutil

DOCS = Path("docs")
SRC  = DOCS / "reposzablony"
DST  = DOCS / "authoring"

def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""

def safe_rel(from_file: Path, to_file: Path) -> str:
    """Zwróć ścieżkę względną (as_posix), z punktu widzenia from_file.parent."""
    try:
        return to_file.resolve().relative_to(from_file.parent.resolve()).as_posix()
    except Exception:
        # fallback – względna po prostu po segmentach
        return str(Path(*([".."] * (len(from_file.parent.parts))) ) / to_file).replace("\\", "/")

def discover_chapters(base: Path):
    if not base.exists():
        return []
    return [p for p in sorted(base.iterdir()) if p.is_dir() and not p.name.startswith(".")]

def discover_md(chapter_dir: Path):
    files = []
    for p in chapter_dir.rglob("*.md"):
        # pomijamy naszą sekcję outputową:
        if "/authoring/" in p.as_posix():
            continue
        files.append(p)
    return sorted(files)

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def build_chapter_page(chapter: Path):
    """
    Tworzy docs/authoring/<name>/index.md z:
    - CSV (summary.csv, entities.csv) osadzone jako csv-table
    - Mermaid (flow.mmd, architecture.mmd) osadzone inline (czytamy plik i wklejamy do ```{mermaid} ... ```)
    - ToC do wszystkich .md z tego rozdziału (z wykluczeniem docs/authoring)
    """
    name = chapter.name  # np. 01_core
    out_file = DST / name / "index.md"

    # Lokacje danych
    p_summary = chapter / "datasets" / "summary.csv"
    p_entities = chapter / "datasets" / "entities.csv"
    p_flow = chapter / "diagrams" / "flow.mmd"
    p_arch = chapter / "diagrams" / "architecture.mmd"

    # Czytamy mermaid jako tekst, wklejamy inline (bez include) -> zawsze renderuje.
    flow_txt = read_text(p_flow).strip()
    arch_txt = read_text(p_arch).strip()

    # Zbierz wszystkie md z rozdziału dla toctree
    md_files = discover_md(chapter)
    # Sphinx chce ścieżki względem docs/, bez rozszerzenia
    def to_docname(p: Path) -> str:
        ap = p.as_posix()
        if ap.startswith("docs/"):
            ap = ap[5:]
        if ap.endswith(".md"):
            ap = ap[:-3]
        return ap

    related_docs = [to_docname(p) for p in md_files if p.exists()]

    # Budujemy stronę
    lines = []
    lines.append(f"---\ntitle: {name} — Authoring\n---\n")
    lines.append(f"# {name}\n")

    # Kafelki z sekcjami
    lines.append(":::{grid} 1 1 2 2\n:gutter: 2\n")

    # Datasets (CSV)
    lines.append(":::{grid-item-card} Datasets")
    lines.append(":shadow: md\n")
    if p_summary.exists():
        rel_summary = Path("../../") / (p_summary.relative_to(DOCS))
        lines.append("**Summary**")
        lines.append("```{csv-table}")
        lines.append(':header: "Key","Value","Notes"')
        lines.append(f":file: {rel_summary.as_posix()}")
        lines.append(":widths: 30, 30, 40")
        lines.append("```")
        lines.append("")
    else:
        lines.append("_Brak_ `datasets/summary.csv`\n")

    if p_entities.exists():
        rel_entities = Path("../../") / (p_entities.relative_to(DOCS))
        lines.append("**Entities**")
        lines.append("```{csv-table}")
        lines.append(':header: "Entity","Count","Meta"')
        lines.append(f":file: {rel_entities.as_posix()}")
        lines.append(":widths: 40, 20, 40")
        lines.append("```")
        lines.append("")
    else:
        lines.append("_Brak_ `datasets/entities.csv`\n")
    lines.append(":::\n")  # /grid-item-card

    # Diagrams (Mermaid)
    lines.append(":::{grid-item-card} Diagrams")
    lines.append(":shadow: md\n")
    if flow_txt:
        lines.append("**Flow (Mermaid)**")
        lines.append("```{mermaid}")
        lines.append(flow_txt)
        lines.append("```")
        lines.append("")
    else:
        lines.append("_Brak_ `diagrams/flow.mmd`\n")

    if arch_txt:
        lines.append("**Architecture (Mermaid)**")
        lines.append("```{mermaid}")
        lines.append(arch_txt)
        lines.append("```")
        lines.append("")
    else:
        lines.append("_Brak_ `diagrams/architecture.mmd`\n")
    lines.append(":::\n")  # /grid-item-card

    lines.append(":::\n")  # /grid

    # ToC do wszystkich md w rozdziale
    if related_docs:
        lines.append("\n## Powiązane dokumenty\n")
        lines.append("```{toctree}")
        lines.append(":maxdepth: 2")
        lines.append(":titlesonly:\n")
        for d in related_docs:
            # tylko z bieżącego rozdziału
            if d.startswith(f"reposzablony/{name}/"):
                lines.append(d)
        lines.append("```")

    write(out_file, "\n".join(lines) + "\n")

def build_index(chapters):
    out = []
    out.append("---\ntitle: Authoring — AUTO\n---\n")
    out.append("# Authoring (auto)\n")
    out.append(":::{admonition} Źródło\nTe strony są generowane z `docs/reposzablony/**` i osadzają CSV/diagramy inline.\n:::")
    out.append("\n```{toctree}\n:caption: Rozdziały\n:maxdepth: 1\n")
    for ch in chapters:
        out.append(f"{ch.name}/index")
    out.append("```\n")
    write(DST / "index.md", "\n".join(out))

def main():
    # HARD RESET outputu (na Twoje życzenie: „wolę hard reset”)
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True, exist_ok=True)

    # Odkryj rozdziały w reposzablony
    chapters = discover_chapters(SRC)

    # Zbuduj stronę główną Authoring
    build_index(chapters)

    # Zbuduj każdą stronę rozdziału
    for ch in chapters:
        build_chapter_page(ch)

    print("OK: generated docs/authoring/* from docs/reposzablony/* (inline CSV + Mermaid + TOC)")

if __name__ == "__main__":
    main()
