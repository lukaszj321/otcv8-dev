
#!/usr/bin/env python3
# Scans docs/authoring/** for facet anchors in index pages and presence of datasets/diagrams.
# Writes docs/authoring/_data/facets.csv for navigation and React tooling.

from pathlib import Path
import re, csv

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"
DATA = AUTHORING / "_data"
DATA.mkdir(parents=True, exist_ok=True)

ANCHOR_RE = re.compile(r"\(facet-([0-9]{2}_[a-z0-9_]+)\.([a-z0-9_\-]+)\)=", re.IGNORECASE)

def list_chapters():
    if not AUTHORING.exists():
        return []
    return [p for p in AUTHORING.iterdir() if p.is_dir() and p.name[:2].isdigit()]

def scan_chapter(ch_dir: Path):
    index = ch_dir / "index.md"
    if not index.exists():
        return []
    text = index.read_text(encoding="utf-8", errors="ignore")
    facets = []
    for m in ANCHOR_RE.finditer(text):
        chapter = m.group(1)  # e.g., 01_core
        stem = m.group(2)     # e.g., summary
        facet_id = f"{chapter}.{stem}"
        # datasets / diagrams presence (same stem if present)
        ds_dir = ch_dir / "datasets"
        dg_dir = ch_dir / "diagrams"
        datasets = sorted([p.name for p in ds_dir.glob(f"{stem}*.csv")]) if ds_dir.exists() else []
        diagrams = sorted([p.name for p in dg_dir.glob(f"{stem}*.mmd")]) if dg_dir.exists() else []
        has_csv = "1" if datasets else "0"
        has_mmd = "1" if diagrams else "0"
        facets.append({
            "chapter": chapter,
            "facet_id": facet_id,
            "title": f"{chapter}.{stem}",
            "source_index_path": str(index.relative_to(AUTHORING)).replace("\\", "/"),
            "datasets": ";".join(datasets),
            "diagrams": ";".join(diagrams),
            "has_csv": has_csv,
            "has_mmd": has_mmd,
        })
    return facets

def main():
    rows = []
    for ch in sorted(list_chapters(), key=lambda p: p.name):
        rows.extend(scan_chapter(ch))
    out = DATA / "facets.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["chapter","facet_id","title","source_index_path","datasets","diagrams","has_csv","has_mmd"])
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"[FACETS] wrote {out} with {len(rows)} entries")

if __name__ == "__main__":
    raise SystemExit(main())
