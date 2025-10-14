
#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
AUTHORING = ROOT / "docs" / "authoring"

def camel(stem: str) -> str:
    parts = re.split(r"[_\-\s]+", stem.strip())
    return "".join(p.capitalize() for p in parts if p)

def chapter_of(p: Path) -> str:
    for part in p.parts:
        if re.match(r"^\d{2}_", part):
            return part
    return "00_misc"

def main():
    if not AUTHORING.exists():
        print(f"[WARN] Missing {AUTHORING}")
        return 0
    patched = 0
    for mmd in AUTHORING.rglob("diagrams/*.mmd"):
        stem = mmd.stem
        ch = chapter_of(mmd)
        node_id = camel(stem)
        txt = mmd.read_text(encoding="utf-8")
        if not re.search(rf"(^|\W){re.escape(node_id)}\s*[\[\(\{{]", txt):
            continue
        if re.search(rf"^\s*click\s+{re.escape(node_id)}\b", txt, flags=re.MULTILINE):
            continue
        click = f'click {node_id} "./index.html#facet-{ch}.{stem}" "Open {stem}"'
        new_txt = txt.rstrip() + "\n" + click + "\n"
        mmd.write_text(new_txt, encoding="utf-8")
        patched += 1
        print(f"[OK] patched: {mmd}")
    print(f"[SUMMARY] patched={patched}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
