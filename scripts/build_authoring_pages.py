#!/usr/bin/env python3
# Build Authoring pages from docs/reposzablony/**
# - For each chapter folder (e.g., 01_core), generate docs/authoring/<chapter>/index.md
# - Embed CSV via csv-table; embed Mermaid via mermaid + include; show code via literalinclude
# - Update docs/authoring/index.md with cards and toctree
import os, sys, pathlib, textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPO = DOCS / "reposzablony"
AUTHORING = DOCS / "authoring"

def find_chapters():
    if not REPO.exists():
        print(f"[WARN] Missing {REPO}")
        return []
    items = []
    for p in sorted(REPO.iterdir()):
        if not p.is_dir():
            continue
        if p.name.startswith("."):
            continue
        items.append(p.name)
    return items

def chapter_title(slug: str) -> str:
    clean = slug.replace("_", " ").strip()
    parts = clean.split(" ", 1)
    if len(parts) == 2 and parts[0].isdigit():
        return f"{slug} — {parts[1].capitalize()}"
    return clean.title()

def rel(path: pathlib.Path) -> str:
    return str(path.as_posix())

def write_chapter(chapter: str):
    src = REPO / chapter
    dst_dir = AUTHORING / chapter
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / "index.md"

    datasets = src / "datasets"
    diagrams = src / "diagrams"

    csvs = sorted(datasets.glob("*.csv")) if datasets.exists() else []
    mmds = sorted(diagrams.glob("*.mmd")) if diagrams.exists() else []

    title = chapter_title(chapter)
    base_rel = pathlib.Path("../../reposzablony") / chapter

    def csv_block(p: pathlib.Path):
        return textwrap.dedent(f"""
        ```{{admonition}} {p.name} (CSV)
        :class: dropdown
        Lokalizacja: `{rel(base_rel / 'datasets' / p.name)}`
        ```

        ```{{csv-table}} {p.stem}
        :header-rows: 1
        :file: {rel(base_rel / 'datasets' / p.name)}
        :widths: 50,50
        ```
        """).strip()

    def mmd_block(p: pathlib.Path):
        return textwrap.dedent(f"""
        ```{{admonition}} {p.name} (Mermaid)
        :class: tip
        Lokalizacja: `{rel(base_rel / 'diagrams' / p.name)}`
        ```

        ````{{mermaid}}
        :caption: {p.stem}
        ```{{include}} {rel(base_rel / 'diagrams' / p.name)}
        ```
        ````

        ```{{admonition}} Kod źródłowy ({p.name})
        :class: dropdown
        ```{{literalinclude}} {rel(base_rel / 'diagrams' / p.name)}
        :language: mermaid
        ```
        ```
        """).strip()

    if len(csvs) >= 2:
        csv_grid = [":::{grid} 1 1 2 2", ":gutter: 2"]
        for c in csvs:
            csv_grid.append(":::{grid-item}")
            csv_grid.append(csv_block(c))
            csv_grid.append(":::")
        csv_grid.append(":::")
        csv_section = "\n\n".join(csv_grid)
    elif len(csvs) == 1:
        csv_section = csv_block(csvs[0])
    else:
        csv_section = "_Brak CSV w tym rozdziale._"

    if mmds:
        mmd_section = "\n\n".join(mmd_block(m) for m in mmds)
    else:
        mmd_section = "_Brak diagramów w tym rozdziale._"

    # Build the body with proper string concatenation to avoid escaping issues
    admonition_part = """:::{admonition} Co jest na tej stronie?
:class: tip
- **Datasets** — CSV z `datasets/` osadzone jako tabele
- **Diagrams** — Mermaid z `diagrams/` + podgląd kodu w dropdown
:::"""
    
    body = f"""---
title: {title}
---

# {title}

> Źródła: `docs/reposzablony/{chapter}/`

{admonition_part}

## Datasets
{csv_section}

## Diagrams
{mmd_section}
"""

    dst.write_text(body, encoding="utf-8")
    print(f"[OK] Wrote {dst}")

def write_index(chapters):
    dst = AUTHORING / "index.md"
    cards = [":::{grid} 1 1 2 3", ":gutter: 2"]
    for ch in chapters:
        title = chapter_title(ch)
        link = f"{ch}/index"
        cards += [
            ":::{grid-item-card} " + title,
            f":link: {link}",
            ":link-type: doc",
            ":shadow: md",
            f"{title} — wbudowany podgląd CSV i diagramów.",
            ":::",
        ]
    cards.append(":::")

    toc = ["```{toctree}", ":caption: Rozdziały", ":maxdepth: 1", ":titlesonly:"]
    toc += [f"{ch}/index" for ch in chapters]
    toc.append("```")

    body = textwrap.dedent(f"""---
title: Authoring Kit (embedded)
---

# Authoring Kit — embedded

Poniżej **wbudowane** strony dla rozdziałów z `docs/reposzablony/**`.
Wszystkie dane są osadzane inline, bez wychodzenia poza sekcję **authoring**.

{os.linesep.join(cards)}

{os.linesep.join(toc)}
""")
    dst.write_text(body, encoding="utf-8")
    print(f"[OK] Wrote {dst}")

def main():
    chapters = find_chapters()
    if not chapters:
        print("[WARN] No chapters found under docs/reposzablony/**")
        return 0
    for ch in chapters:
        write_chapter(ch)
    write_index(chapters)
    print("[DONE] authoring pages generated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
