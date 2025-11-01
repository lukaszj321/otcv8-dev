
#!/usr/bin/env python3
# Validates/repairs Mermaid diagrams under docs/authoring/**/diagrams/*.mmd
# - Ensures first line has Mermaid init
# - Ensures at least one click anchor towards #facet-<chapter>.<stem>

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"

INIT = "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%"

def chapter_of(p: Path) -> str:
    for part in p.parts:
        if re.match(r"^\d{2}_", part):
            return part
    return "00_misc"

def camel(stem: str) -> str:
    parts = re.split(r"[_\-\s]+", stem.strip())
    return "".join(s.capitalize() for s in parts if s)

def main():
    if not AUTHORING.exists():
        print("[WARN] docs/authoring not found")
        return 0
    patched = 0
    for mmd in AUTHORING.rglob("diagrams/*.mmd"):
        ch = chapter_of(mmd)
        stem = mmd.stem
        txt = mmd.read_text(encoding="utf-8", errors="ignore")
        lines = [l for l in txt.splitlines() if l.strip() != ""]
        if not lines:
            continue
        changed = False
        # Ensure init
        if not lines[0].lstrip().startswith("%%{init:"):
            txt = INIT + "\\n" + txt
            changed = True
        # Ensure click anchor exists
        node_id = camel(stem)
        if not re.search(rf"^\\s*click\\s+{re.escape(node_id)}\\b", txt, flags=re.MULTILINE):
            click = f'click {node_id} "./index.html#facet-{ch}.{stem}" "Open {stem}"'
            if not txt.endswith("\\n"):
                txt += "\\n"
            txt += click + "\\n"
            changed = True
        if changed:
            mmd.write_text(txt, encoding="utf-8")
            patched += 1
            print(f"[OK] patched {mmd}")
    print(f"[SUMMARY] patched={patched}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
