
#!/usr/bin/env python3
import os, sys, pathlib, textwrap, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AUTHORING = DOCS / "authoring"

def find_chapters():
    if not AUTHORING.exists():
        print(f"[WARN] Missing {AUTHORING}")
        return []
    items = []
    chapter_pattern = re.compile(r'^(0[1-9]|1[0-2])_.*$')
    for p in sorted(AUTHORING.iterdir(), key=lambda q: q.name):
        if p.is_dir() and not p.name.startswith(".") and chapter_pattern.match(p.name):
            items.append(p.name)
    return items

def chapter_title(slug: str) -> str:
    clean = slug.replace("_", " ").strip()
    parts = clean.split(" ", 1)
    if len(parts) == 2 and parts[0].isdigit():
        return f"{slug} - {parts[1].capitalize()}"
    return clean.title()

def ensure_mermaid_init(text: str) -> str:
    init = "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%"
    t = text.strip()
    if not t.startswith("%%{init:"):
        return init + "\n" + t
    return t

def write_chapter(chapter: str):
    ch_dir = AUTHORING / chapter
    dst = ch_dir / "index.md"
    datasets = ch_dir / "datasets"
    diagrams = ch_dir / "diagrams"
    csvs = sorted(datasets.glob("*.csv")) if datasets.exists() else []
    mmds = sorted(diagrams.glob("*.mmd")) if diagrams.exists() else []

    def csv_block(p: pathlib.Path):
        fid = f"{chapter}.{p.stem}"
        return textwrap.dedent(f"""
        #### `{p.name}`
        *Facet:* [`{fid}`](#facet-{fid})

        ```{{csv-table}} {p.stem}
        :header-rows: 1
        :file: ./datasets/{p.name}
        :widths: auto
        ```
        """).strip()

    def mmd_block(p: pathlib.Path):
        content = (diagrams / p.name).read_text(encoding="utf-8") if (diagrams / p.name).exists() else "graph TD\n  A[Error]"
        content = ensure_mermaid_init(content)
        fid = f"{chapter}.{p.stem}"
        return textwrap.dedent(f"""
        #### `{p.name}`
        *Facet:* [`{fid}`](#facet-{fid})

        ```{{mermaid}}
        {content}
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

    mmd_section = "\n\n".join(mmd_block(m) for m in mmds) if mmds else "_Brak diagramow w tym rozdziale._"

    stems = sorted({p.stem for p in csvs + mmds})
    appendix_md = ""
    if stems:
        appendix_md = "## Appendix / Facets\n" + "\n".join([f"(facet-{chapter}.{s})=\n### Facet: `{chapter}.{s}`" for s in stems])

    body = f"""---
title: {chapter_title(chapter)}
---

# {chapter_title(chapter)}

```{{contents}} Table of contents
:depth: 2
:local:
```

## Datasets
{csv_section}

## Diagrams
{mmd_section}

{appendix_md}
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
            f"{title} - wbudowany podglad CSV i diagramow.",
            ":::",
        ]
    cards.append(":::")
    toc = ["```{toctree}", ":caption: Rozdzialy", ":maxdepth: 1", ":titlesonly:"] + [f"{ch}/index" for ch in chapters] + ["```"]
    dst.write_text(f"""---
title: Authoring (embedded)
---

# Authoring - embedded

Wszystkie rozdzialy z `docs/authoring/**` renderowane inline.

{os.linesep.join(cards)}

{os.linesep.join(toc)}
""", encoding="utf-8")
    print(f"[OK] Wrote {dst}")

def main():
    chapters = find_chapters()
    if not chapters:
        print("[WARN] No chapters found under docs/authoring/**")
        return 0
    for ch in chapters:
        write_chapter(ch)
    write_index(chapters)
    print("[DONE] authoring pages generated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
