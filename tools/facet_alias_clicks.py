
#!/usr/bin/env python3
# Patch diagrams using alias->facet mapping from docs/authoring/_data/facet_aliases.csv

from pathlib import Path
import csv, re

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"
ALIASES = AUTHORING / "_data" / "facet_aliases.csv"

def main():
    if not ALIASES.exists():
        print("[ALIAS] no facet_aliases.csv, skipping")
        return 0
    mapping = {}
    with ALIASES.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            alias = (row.get("alias") or "").strip()
            fid = (row.get("facet_id") or "").strip()
            if alias and fid:
                mapping[alias] = fid
    if not mapping:
        print("[ALIAS] empty mapping")
        return 0

    patched = 0
    for mmd in AUTHORING.rglob("diagrams/*.mmd"):
        txt = mmd.read_text(encoding="utf-8")
        add = []
        for alias, fid in mapping.items():
            node_id = re.sub(r"[^A-Za-z0-9_]", "", alias.title().replace(" ", ""))
            anchor = "#facet-" + fid
            if not re.search(r"^\s*click\s+" + re.escape(node_id) + r"\b", txt, flags=re.MULTILINE):
                add.append('click ' + node_id + ' "./index.html' + anchor + '" "Open ' + fid + '"')
        if add:
            txt = txt.rstrip() + "\n" + "\n".join(add) + "\n"
            mmd.write_text(txt, encoding="utf-8")
            patched += 1
            print(f"[ALIAS] patched {mmd}")
    print(f"[ALIAS] patched files: {patched}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
