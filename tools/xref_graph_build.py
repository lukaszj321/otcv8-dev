
#!/usr/bin/env python3
# Builds a Mermaid graph from docs/authoring/_data/xref.csv (if present)
# Outputs docs/authoring/_data/xref_graph.mmd

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "authoring" / "_data"

HEADER = "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%\\n"

def sanitize(label: str) -> str:
    return label.replace(".", "_").replace("-", "_").replace("/", "_")

def main():
    xref = DATA / "xref.csv"
    out = DATA / "xref_graph.mmd"
    if not xref.exists():
        out.write_text(HEADER + "graph TD\\n  A[No xref.csv] --> B[Run xref_builder]\\n", encoding="utf-8")
        print("[XREF] no xref.csv found, wrote placeholder graph")
        return 0
    edges = []
    with xref.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            a = row.get("from_facet") or row.get("from_facet".upper()) or ""
            b = row.get("to_facet") or row.get("to_facet".upper()) or ""
            if not a or not b:
                # try combination of columns used earlier
                a = (row.get("from_chapter","") + "." + row.get("from_facet","")).strip(".")
                b = (row.get("to_chapter","") + "." + row.get("to_facet","")).strip(".")
            if not a or not b:
                continue
            A = sanitize(a)
            B = sanitize(b)
            edges.append(f"  {A}[{a}] --> {B}[{b}]")
    if not edges:
        out.write_text(HEADER + "graph TD\\n  A[No edges]\\n", encoding="utf-8")
        print("[XREF] no edges found, wrote empty graph")
        return 0
    body = "graph TD\\n" + "\\n".join(edges) + "\\n"
    out.write_text(HEADER + body, encoding="utf-8")
    print(f"[XREF] wrote graph with {len(edges)} edges to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
