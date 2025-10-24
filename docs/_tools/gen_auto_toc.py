#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generyczny auto-index (TOC) po katalogach.
Użycie (w CI):
  python docs/_tools/gen_auto_toc.py docs/copilot/sphinx/code/modules/modules  docs/inny/korzen
Domyślnie NIE nadpisuje istniejących index.md (ustaw AUTO_TOC_FORCE=1 aby wymusić).
"""

from __future__ import annotations
import os, sys, textwrap
from pathlib import Path

HEADER = """---
title: Auto TOC
---

# Autoindeks

Poniżej automatycznie wygenerowany spis treści dla podkatalogów.
"""

TOC_TMPL = """```{{toctree}}
:maxdepth: 2
:hidden:

{entries}
```"""

def rel_entries(dir_path: Path):
    items = []
    for p in sorted(dir_path.iterdir()):
        if p.name.startswith("_") or p.name.startswith("."):
            continue
        if p.is_dir():
            # prefer index.md / index.rst
            idx = None
            for cand in (p / "index.md", p / "index.rst"):
                if cand.exists():
                    idx = cand
                    break
            if idx:
                items.append(str(idx.relative_to(dir_path).as_posix()))
    return items

def write_index(dir_path: Path, force: bool = False):
    md = dir_path / "index.md"
    if md.exists() and not force:
        return False
    entries = rel_entries(dir_path)
    content = HEADER + "\n" + TOC_TMPL.format(entries="\n".join(entries)) + "\n"
    md.write_text(content, encoding="utf-8")
    return True

def main(argv: list[str]) -> int:
    roots = argv[1:]
    if not roots:
        roots = ["docs/copilot/sphinx/code/modules/modules"]
    force = os.environ.get("AUTO_TOC_FORCE", "0") == "1"
    wrote_any = False
    for r in roots:
        rp = Path(r).resolve()
        if rp.is_dir():
            if write_index(rp, force=force):
                print(f"[auto-toc] wrote: {rp/'index.md'}")
                wrote_any = True
            else:
                print(f"[auto-toc] skipped (exists): {rp/'index.md'}")
        else:
            print(f"[auto-toc] not a dir: {rp}")
    return 0 if wrote_any else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
