#!/usr/bin/env python3
"""
Normalize a label into a safe Mermaid node-id.

Usage:
  python3 scripts/diagram-tools/node_id_normalizer.py "Game Engine v2"
  python3 scripts/diagram-tools/node_id_normalizer.py --dir docs/authoring --report mapping.json

Behavior:
- lowercase
- spaces -> underscore
- remove characters not in [a-z0-9_-:]
- optionally prefix with doc_id (not automatic; generator can add)
Outputs a mapping if --dir is provided: prints JSON {"original":"normalized",...}
"""
import re
import sys
import json
from pathlib import Path

def normalize(label: str) -> str:
    s = label.strip().lower()
    s = re.sub(r'\s+', '_', s)
    s = re.sub(r'[^a-z0-9_\-:]', '', s)
    # collapse multiple underscores
    s = re.sub(r'__+', '_', s)
    s = s.strip('_')
    if not s:
        s = "node"
    return s

def process_dir(root: Path):
    mapping = {}
    for p in root.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        # find Mermaid node labels like A["Label"] or A("Label") or A{ "Label" }
        for m in re.finditer(r'\w+\s*\[\s*"([^"]+)"\s*\]|\w+\s*\(\s*"([^"]+)"\s*\)|\w+\s*\{\s*"([^"]+)"\s*\}', text):
            label = next(g for g in m.groups() if g)
            nid = normalize(label)
            mapping.setdefault(label, nid)
    return mapping

def main():
    if len(sys.argv) == 2 and sys.argv[1] != "--dir":
        print(normalize(sys.argv[1]))
        return
    if "--dir" in sys.argv:
        i = sys.argv.index("--dir")
        root = Path(sys.argv[i+1]) if i+1 < len(sys.argv) else Path("docs")
        mapping = process_dir(Path(root))
        out = mapping
        if "--report" in sys.argv:
            j = sys.argv.index("--report")
            if j+1 < len(sys.argv):
                Path(sys.argv[j+1]).write_text(json.dumps(mapping, indent=2), encoding="utf-8")
        print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
