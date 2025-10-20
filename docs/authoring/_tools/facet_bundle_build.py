
#!/usr/bin/env python3
# Generate per-facet bundle pages: docs/authoring/<chapter>/facets/<stem>.md

from pathlib import Path
import csv, os

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"
PREV = AUTHORING / "_data" / "previews"
PREV.mkdir(parents=True, exist_ok=True)

CSV_PREVIEW_ROWS = int(os.environ.get("CSV_PREVIEW_ROWS", "100"))

def write_file(p: Path, content: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def csv_head_to(p_csv: Path, out_csv: Path, n: int):
    try:
        with p_csv.open(encoding="utf-8", newline="") as f_in:
            r = csv.reader(f_in)
            rows = []
            for i, row in enumerate(r):
                rows.append(row)
                if i >= n:
                    break
        with out_csv.open("w", encoding="utf-8", newline="") as f_out:
            w = csv.writer(f_out)
            w.writerows(rows)
        return True
    except Exception as e:
        print(f"[WARN] preview skip {p_csv}: {e}")
        return False

def make_bundle_md(chapter: str, stem: str, csv_rel: str|None, mmd_rel: str|None) -> str:
    title = f"{chapter}.{stem}"
    dl_parts = []
    if csv_rel:
        dl_parts.append(f":download:`Download CSV <{csv_rel}>`")
    if mmd_rel:
        dl_parts.append(f":download:`Download diagram (.mmd) <{mmd_rel}>`")
    dl = " | ".join(dl_parts) if dl_parts else "_no files_"
    csv_block = ""
    if csv_rel:
        csv_block = f"""
```{{csv-table}} {stem}
:file: ../{csv_rel}
:header-rows: 1
:widths: auto
```"""
    mermaid_block = ""
    if mmd_rel:
        mermaid_block = f"""
```{{literalinclude}} ../{mmd_rel}
:language: mermaid
:caption: {stem}
```"""
    return f"""---
title: {title}
---

# {title}

{dl}

## Preview
{csv_block}

## Diagram
{mermaid_block}

## Notes
- Short description, context and usage.
- Links: see index and Relations for neighbors.
"""

def main():
    if not AUTHORING.exists():
        print("[WARN] docs/authoring missing")
        return 0

    count = 0
    for ch_dir in sorted([p for p in AUTHORING.iterdir() if p.is_dir() and p.name[:2].isdigit()], key=lambda p: p.name):
        chapter = ch_dir.name
        ds_dir = ch_dir / "datasets"
        dg_dir = ch_dir / "diagrams"
        facets_dir = ch_dir / "facets"

        stems = set()
        if ds_dir.exists():
            stems.update([p.stem for p in ds_dir.glob("*.csv")])
        if dg_dir.exists():
            stems.update([p.stem for p in dg_dir.glob("*.mmd")])

        for stem in sorted(stems):
            csv_rel = None
            mmd_rel = None

            if ds_dir.exists():
                src_csv = ds_dir / f"{stem}.csv"
                if src_csv.exists():
                    prev_out = PREV / chapter / f"{stem}.head.csv"
                    prev_out.parent.mkdir(parents=True, exist_ok=True)
                    if not prev_out.exists():
                        csv_head_to(src_csv, prev_out, CSV_PREVIEW_ROWS)
                    rel_from_facet = Path("..") / "_data" / "previews" / chapter / f"{stem}.head.csv"
                    csv_rel = str(rel_from_facet).replace("\\", "/")

            if dg_dir.exists():
                src_mmd = dg_dir / f"{stem}.mmd"
                if src_mmd.exists():
                    mmd_rel = f"../diagrams/{stem}.mmd"

            md_path = facets_dir / f"{stem}.md"
            write_file(md_path, make_bundle_md(chapter, stem, csv_rel, mmd_rel))
            count += 1
    print(f"[BUNDLES] generated {count} facet bundle pages")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
