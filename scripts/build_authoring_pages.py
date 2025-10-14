
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

def generate_crossref_section(chapter: str) -> str:
    """Generate cross-references section from source metadata"""
    sources_dir = AUTHORING / "_sources"
    if not sources_dir.exists():
        return ""
    
    # Try to find matching source file by checking frontmatter
    source_file = None
    for f in sources_dir.glob("*.md"):
        content = f.read_text(encoding="utf-8")
        # Check if this file has the matching chapter in frontmatter
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if i > 20:  # Only check first 20 lines for frontmatter
                break
            if f'chapter: "{chapter}"' in line or f"chapter: '{chapter}'" in line or f"slug: '{chapter}'" in line or f'slug: "{chapter}"' in line:
                source_file = f
                break
        if source_file:
            break
    
    if not source_file or not source_file.exists():
        return ""
    
    # Parse xrefs from frontmatter
    content = source_file.read_text(encoding="utf-8")
    lines = []
    in_xrefs = False
    xrefs = []
    
    for line in content.split("\n"):
        line_stripped = line.strip()
        if line_stripped == "xrefs:":
            in_xrefs = True
            continue
        if in_xrefs:
            if line_stripped.startswith("- to:"):
                to = line_stripped.replace("- to:", "").strip().strip('"')
                xrefs.append({"to": to, "type": "", "evidence": ""})
            elif line_stripped.startswith("type:") and xrefs:
                xrefs[-1]["type"] = line_stripped.replace("type:", "").strip().strip('"')
            elif line_stripped.startswith("evidence:") and xrefs:
                xrefs[-1]["evidence"] = line_stripped.replace("evidence:", "").strip().strip('"')
            elif line_stripped and not line_stripped.startswith(" ") and ":" in line_stripped and not line.startswith("  "):
                in_xrefs = False
    
    if not xrefs:
        return ""
    
    lines = ["## Crosslinks\n"]
    for xref in xrefs:
        to = xref.get("to", "")
        xtype = xref.get("type", "")
        evidence = xref.get("evidence", "")
        if to:
            lines.append(f"- **{xtype}** → `{to}` (evidence: `{evidence}`)")
    
    return "\n".join(lines)

def write_chapter(chapter: str):
    ch_dir = AUTHORING / chapter
    dst = ch_dir / "index.md"
    datasets = ch_dir / "datasets"
    diagrams = ch_dir / "diagrams"
    csvs = sorted(datasets.glob("*.csv")) if datasets.exists() else []
    mmds = sorted(diagrams.glob("*.mmd")) if diagrams.exists() else []

    # Find subdirectories (excluding datasets and diagrams)
    subdirs = []
    if ch_dir.exists():
        for item in sorted(ch_dir.iterdir()):
            if item.is_dir() and not item.name.startswith(".") and item.name not in ["datasets", "diagrams"]:
                subdirs.append(item.name)

    def csv_block(p: pathlib.Path):
        fid = f"{chapter}.{p.stem}"
        return textwrap.dedent(f"""
        ### {p.stem}
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
        ### {p.stem}
        *Facet:* [`{fid}`](#facet-{fid})

        ```{{mermaid}}
        {content}
        ```
        """).strip()

    csv_section = "\n\n".join(csv_block(c) for c in csvs) if csvs else "_Brak CSV w tym rozdziale._"
    mmd_section = "\n\n".join(mmd_block(m) for m in mmds) if mmds else "_Brak diagramow w tym rozdziale._"

    # Podkatalogi section
    podkatalogi_section = ""
    if subdirs:
        toc_lines = ["```{toctree}", ":maxdepth: 1", ":titlesonly:"]
        for subdir in subdirs:
            toc_lines.append(f"{subdir}/index")
        toc_lines.append("```")
        podkatalogi_section = f"## Podkatalogi\n\n{chr(10).join(toc_lines)}"

    # Cross-references from source files
    xref_section = generate_crossref_section(chapter)

    stems = sorted({p.stem for p in csvs + mmds})
    appendix_md = ""
    if stems:
        facets = []
        for stem in stems:
            facet_type = "dataset" if any(c.stem == stem for c in csvs) else "diagram"
            facets.append(f"(facet-{chapter}.{stem})=")
            facets.append(f"### Facet: `{chapter}.{stem}`")
            facets.append(f"Type: {facet_type}")
            facets.append("")
        appendix_md = "## Appendix / Facets\n\n" + "\n".join(facets)

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

{podkatalogi_section}

{xref_section}

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
    
    # Build toctree with all chapters
    toc = ["```{toctree}", ":caption: Rozdzialy", ":maxdepth: 1", ":titlesonly:"]
    toc.extend([f"{ch}/index" for ch in chapters])
    toc.append("")
    toc.append("analytics/summary")
    toc.append("qa/summary")
    toc.append("```")
    
    dst.write_text(f"""---
title: Authoring (embedded)
---

# Authoring - embedded

Wszystkie rozdzialy z `docs/authoring/**` renderowane inline.

{os.linesep.join(cards)}

{os.linesep.join(toc)}

## Narzedzia

Zobacz: [Tools Documentation](../tools/index)

## RAG Manifest

Zobacz: [Datasets](./datasets/index)
""", encoding="utf-8")
    print(f"[OK] Wrote {dst}")

def ensure_subdirectory_indexes(chapter: str):
    """Ensure all subdirectories have index.md files"""
    ch_dir = AUTHORING / chapter
    if not ch_dir.exists():
        return
    
    for item in ch_dir.iterdir():
        if item.is_dir() and not item.name.startswith(".") and item.name not in ["datasets", "diagrams"]:
            index_file = item / "index.md"
            if not index_file.exists():
                # Create a simple index
                title = item.name.replace("_", " ").title()
                # Find any subdirectories
                subdirs = [d.name for d in item.iterdir() if d.is_dir() and not d.name.startswith(".")]
                
                toc_section = ""
                if subdirs:
                    toc_lines = ["```{toctree}", ":maxdepth: 2", ":titlesonly:", ""]
                    for subdir in sorted(subdirs):
                        toc_lines.append(f"{subdir}/index")
                    toc_lines.append("```")
                    toc_section = "\n\n" + "\n".join(toc_lines)
                
                content = f"""# {title}

Dokumentacja dla `{chapter}/{item.name}/`.
{toc_section}
"""
                index_file.write_text(content, encoding="utf-8")
                print(f"[OK] Created {index_file}")

def main():
    chapters = find_chapters()
    if not chapters:
        print("[WARN] No chapters found under docs/authoring/**")
        return 0
    for ch in chapters:
        ensure_subdirectory_indexes(ch)
        write_chapter(ch)
    write_index(chapters)
    print("[DONE] authoring pages generated.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
