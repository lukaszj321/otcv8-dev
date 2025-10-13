#!/usr/bin/env python3
# coding: utf-8
"""
Authoring generator (FINAL):
Źródło: docs/reposzablony/** (01_core, 01_runtime, 02_events, ...)
Cel:    docs/authoring/** 

FUNKCJE:
- HARD RESET outputu (usuwa docs/authoring/*).
- Dla każdego rozdziału:
  • CSV -> csv-table (WSZYSTKIE *.csv z datasets/**)
  • Mermaid -> osadzone inline (WSZYSTKIE *.mmd, *.mermaid)
  • Graphviz -> osadzone inline (WSZYSTKIE *.dot, *.gv)
  • Intro -> jeżeli istnieje chapter_XX_*.md
  • ToC -> do wszystkich *.md w rozdziale (z podkatalogami)
- Buduje docs/authoring/index.md (kafelki rozdziałów).

UWAGA: brak include – wszystko inline, więc render jest stabilny.
"""

from pathlib import Path
import shutil
import re

DOCS = Path("docs")
SRC  = DOCS / "reposzablony"
DST  = DOCS / "authoring"

def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""

def write_text(p: Path, content: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def discover_chapters(base: Path):
    if not base.exists():
        return []
    # 01_*, 02_* ...
    return [p for p in sorted(base.iterdir()) if p.is_dir() and re.match(r"^\d{2}_", p.name)]

def discover_files(root: Path, exts):
    out = []
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in exts:
            # pomijamy nasz output
            if "/authoring/" in p.as_posix():
                continue
            out.append(p)
    return sorted(out)

def md_docname(p: Path) -> str:
    """Ścieżka dokumentu dla Sphinxa (bez rozszerzenia, bez prefixu docs/)."""
    ap = p.as_posix()
    if ap.startswith("docs/"):
        ap = ap[5:]
    if ap.endswith(".md"):
        ap = ap[:-3]
    return ap

def find_intro_for_chapter(chapter: Path):
    """
    Szuka pliku typu: chapter_XX_*.md w repo (np. docs/chapter_01_*.md),
    gdzie XX to prefix rozdziału (np. '01').
    """
    prefix = chapter.name.split("_", 1)[0]  # '01'
    # szukamy wszędzie pod docs/, najpierw w katalogu głównym:
    candidates = list(DOCS.glob(f"chapter_{prefix}_*.md"))
    return candidates[0] if candidates else None

def build_chapter_page(chapter: Path):
    name = chapter.name  # np. 01_core
    out_file = DST / name / "index.md"

    # 1) INTRO (opcjonalnie)
    intro_path = find_intro_for_chapter(chapter)
    intro_md = read_text(intro_path) if intro_path else ""

    # 2) CSV
    csv_files = discover_files(chapter / "datasets", {".csv"})

    # 3) DIAGRAMY
    mermaid_files = discover_files(chapter / "diagrams", {".mmd", ".mermaid"})
    graphviz_files = discover_files(chapter / "diagrams", {".dot", ".gv"})

    # 4) POWIĄZANE MD (wszystko z rozdziału i podkatalogów)
    md_files = discover_files(chapter, {".md"})
    # wykluczamy bieżący index (gdy istnieje) i nasz output
    md_files = [p for p in md_files if p.name.lower() != "index.md" and "/authoring/" not in p.as_posix()]

    # BUDOWA STRONY
    lines = []
    lines.append(f"---\ntitle: {name} — Authoring\n---\n")
    lines.append(f"# {name}\n")

    # Intro
    if intro_md.strip():
        lines.append(":::{admonition} Intro (z pliku chapter_XX_*)")
        lines.append(":class: note\n")
        lines.append(intro_md.strip())
        lines.append(":::\n")

    # GRID: datasets + diagrams (dwukolumnowo)
    lines.append(":::{grid} 1 1 2 2\n:gutter: 2\n")

    # Datasets
    lines.append(":::{grid-item-card} Datasets")
    lines.append(":shadow: md\n")
    if csv_files:
        for csv in csv_files:
            title = csv.stem.replace("_", " ").title()
            rel = csv.relative_to(DOCS).as_posix()
            lines.append(f"**{title}**")
            lines.append("```{csv-table}")
            lines.append(':header: "Col 1","Col 2","Col 3"')
            lines.append(f":file: ../../{rel}")
            lines.append(":widths: 33, 33, 34")
            lines.append("```")
            lines.append("")
    else:
        lines.append("_Brak danych CSV w `datasets/`_\n")
    lines.append(":::\n")

    # Diagrams
    lines.append(":::{grid-item-card} Diagrams")
    lines.append(":shadow: md\n")
    if mermaid_files or graphviz_files:
        for m in mermaid_files:
            title = m.stem.replace("_", " ").title()
            lines.append(f"**{title}**")
            lines.append("```{mermaid}")
            lines.append(read_text(m).strip())
            lines.append("```")
            lines.append("")
        for g in graphviz_files:
            title = g.stem.replace("_", " ").title()
            lines.append(f"**{title}**")
            lines.append("```{graphviz}")
            lines.append(read_text(g).strip())
            lines.append("```")
            lines.append("")
    else:
        lines.append("_Brak diagramów w `diagrams/`_\n")
    lines.append(":::\n")

    lines.append(":::\n")  # /grid

    # ToC (powiązane md z całego rozdziału)
    if md_files:
        lines.append("\n## Powiązane dokumenty\n")
        lines.append("```{toctree}")
        lines.append(":maxdepth: 2")
        lines.append(":titlesonly:\n")
        for p in md_files:
            docname = md_docname(p)
            lines.append(docname)
        lines.append("```")

    write_text(out_file, "\n".join(lines) + "\n")

def build_authoring_index(chapters):
    out = []
    out.append("---\ntitle: Authoring — AUTO\n---\n")
    out.append("# Authoring (auto)\n")
    out.append(":::{admonition} Skąd to jest?\nTe strony są generowane z `docs/reposzablony/**` i osadzają CSV/diagramy **inline**.\n:::")
    out.append("\n:::{grid} 1 1 2 3\n:gutter: 2\n")
    for ch in chapters:
        out.append(":::{grid-item-card} " + ch.name.replace("_", " ").title())
        out.append(f":link: {ch.name}/index")
        out.append(":link-type: doc")
        out.append(":shadow: md\n")
        # teaser: pokaż, czy są datasets/diagrams
        has_csv = (ch / "datasets").exists()
        has_dia = (ch / "diagrams").exists()
        badges = []
        if has_csv: badges.append("**datasets**")
        if has_dia: badges.append("**diagrams**")
        if badges:
            out.append("Zawiera: " + ", ".join(badges))
        else:
            out.append("Brak datasets/diagrams")
        out.append("\n:::\n")
    out.append(":::\n")

    # też toctree
    out.append("\n```{toctree}\n:caption: Rozdziały\n:maxdepth: 1\n")
    for ch in chapters:
        out.append(f"{ch.name}/index")
    out.append("```\n")

    write_text(DST / "index.md", "\n".join(out))

def main():
    # HARD RESET
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True, exist_ok=True)

    chapters = discover_chapters(SRC)
    build_authoring_index(chapters)
    for ch in chapters:
        build_chapter_page(ch)

    print("OK: generated docs/authoring/* from docs/reposzablony/* (inline CSV/Mermaid/Graphviz + TOC)")

if __name__ == "__main__":
    main()
