
#!/usr/bin/env python3
# Converts docs/authoring/_data/facets.csv -> facets.json for React tooling.

from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"
DATA = AUTHORING / "_data"

BASE_URL = "https://lukaszj321.github.io/otcv8-dev/authoring"

def main():
    csv_path = DATA / "facets.csv"
    out = DATA / "facets.json"
    if not csv_path.exists():
        out.write_text("[]", encoding="utf-8")
        print("[FACETS] facets.csv missing, wrote empty facets.json")
        return 0
    rows = []
    with csv_path.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            chapter = r.get("chapter","")
            facet_id = r.get("facet_id","")
            source_index = r.get("source_index_path","")
            url = f"{BASE_URL}/{source_index.replace('index.md','index.html')}#facet-{facet_id}"
            rows.append({
                "chapter": chapter,
                "facet_id": facet_id,
                "title": r.get("title",""),
                "url": url,
                "datasets": (r.get("datasets","") or "").split(";") if r.get("datasets") else [],
                "diagrams": (r.get("diagrams","") or "").split(";") if r.get("diagrams") else [],
                "has_csv": r.get("has_csv") == "1",
                "has_mmd": r.get("has_mmd") == "1",
            })
    with out.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f"[FACETS] wrote {out} ({len(rows)} facets)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
