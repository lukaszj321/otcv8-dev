
#!/usr/bin/env python3
# Convert docs/authoring/_data/xref.csv -> xref.json for React graph rendering

from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "authoring" / "_data"

def main():
    xref = DATA / "xref.csv"
    out = DATA / "xref.json"
    if not xref.exists():
        out.write_text("[]", encoding="utf-8")
        print("[XREF] no xref.csv; wrote empty xref.json")
        return 0
    edges = []
    with xref.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            edges.append({
                "from_chapter": row.get("from_chapter",""),
                "from_facet": row.get("from_facet",""),
                "to_chapter": row.get("to_chapter",""),
                "to_facet": row.get("to_facet",""),
                "type": row.get("type",""),
                "evidence_path": row.get("evidence_path","") or row.get("evidence",""),
                "note": row.get("note",""),
            })
    out.write_text(json.dumps(edges, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[XREF] wrote {out} ({len(edges)} edges)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
