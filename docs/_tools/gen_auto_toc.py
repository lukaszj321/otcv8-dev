#!/usr/bin/env python3
"""
Auto-generuje `index.md` z blokami MyST `toctree` bez ręcznego pisania plików.

Nowości:
- **Automatyczne odkrywanie katalogów** na podstawie baz przekazanych jako
  argumenty CLI, wzorców glob (np. "docs/**/code") albo zmiennej `AUTO_TOC_BASES`.
- **Filtry**: pomija `_build`, `_static`, `_templates`, `_extra`, `.git`, itp.
- **Tworzy indeks tylko tam, gdzie są realne treści** (`.md`/`.rst`) lub podkatalogi
  z takimi treściami — nie zaśmieca pustych folderów.
- **Nie nadpisuje** istniejących `index.md` (chyba że ustawisz `AUTO_TOC_FORCE=1`).

Użycie (CI):
  python docs/_tools/gen_auto_toc.py docs/copilot/sphinx/code
  # albo z wieloma bazami
  python docs/_tools/gen_auto_toc.py docs/copilot/sphinx/code docs/autoapi
  # albo przez zmienną środowiskową (separator ścieżek jak w PATH — ':' na Linuksie)
  AUTO_TOC_BASES="docs/copilot/sphinx/code:docs/autoapi" python docs/_tools/gen_auto_toc.py
  # lub wzorce glob
  python docs/_tools/gen_auto_toc.py "docs/**/code"
"""
from __future__ import annotations
from pathlib import Path
import os
import sys
import glob
from typing import Iterable

INDEX_NAME = "index.md"
FILE_EXTS = {".md", ".rst"}
EXCLUDE_DIRNAMES = {
    "_build", "_static", "_templates", "_extra",
    ".git", ".github", "venv", ".venv", "node_modules", "__pycache__",
}
FORCE = os.getenv("AUTO_TOC_FORCE", "0") == "1"

TEMPLATE_ROOT = """# {title}

```{{toctree}}
:maxdepth: 2
:glob:
:titlesonly:

*/index
*
```
"""

TEMPLATE_SUB = """# {title}

```{{toctree}}
:hidden:
:glob:

*/index
*
```
"""

def is_excluded(p: Path) -> bool:
    # Wyklucz, jeśli którakolwiek część ścieżki jest na liście
    return any(part in EXCLUDE_DIRNAMES for part in p.parts)


def has_doc_files(d: Path) -> bool:
    """Czy katalog zawiera treść wartą indeksowania?"""
    try:
        for f in d.iterdir():
            if f.is_file() and f.suffix.lower() in FILE_EXTS and f.name.lower() != INDEX_NAME:
                return True
        # jeśli nie ma plików, sprawdź bezpośrednie podkatalogi
        for sub in d.iterdir():
            if sub.is_dir() and not is_excluded(sub):
                for f in sub.iterdir():
                    if f.is_file() and f.suffix.lower() in FILE_EXTS:
                        return True
    except Exception:
        pass
    return False


def should_write(idx: Path, root: bool) -> bool:
    if not FORCE and idx.exists():
        return False
    # Dla podkatalogów nie twórz bez treści
    if not root and not has_doc_files(idx.parent):
        return False
    return True


def ensure_index(dirpath: Path, root: bool) -> bool:
    idx = dirpath / INDEX_NAME
    if not should_write(idx, root):
        return False
    title = (dirpath.name or dirpath.resolve().name).strip() or "Index"
    content = (TEMPLATE_ROOT if root else TEMPLATE_SUB).format(title=title)
    idx.write_text(content, encoding="utf-8")
    return True


def expand_bases(argv: list[str]) -> list[Path]:
    candidates: list[str] = []
    env = os.getenv("AUTO_TOC_BASES", "").strip()
    if env:
        # PATH-like: ':' (Linux/macOS) lub ';' (Windows). Obsłuż oba.
        sep = ";" if ";" in env and os.pathsep == ";" else ":"
        for part in env.split(sep):
            if part:
                candidates.append(part)
    # argumenty CLI
    if len(argv) > 1:
        candidates.extend(argv[1:])
    # domyślna baza (jeśli nic nie podano)
    if not candidates:
        candidates = ["docs/copilot/sphinx/code"]

    bases: list[Path] = []
    for c in candidates:
        # obsługa globów
        matches = glob.glob(c, recursive=True) or [c]
        for m in matches:
            p = Path(m).resolve()
            if p.is_dir() and not is_excluded(p):
                bases.append(p)
    # deduplikacja, zachowaj kolejność
    seen = set()
    unique: list[Path] = []
    for b in bases:
        if b not in seen:
            unique.append(b)
            seen.add(b)
    return unique


def main(argv: list[str]) -> int:
    bases = expand_bases(argv)
    if not bases:
        print("! No bases found — nothing to do.")
        return 0

    created = 0
    for base in bases:
        # indeks dla bazy (root)
        if ensure_index(base, True):
            created += 1
            print(f"+ {base/INDEX_NAME}")
        # indeksy dla wszystkich podkatalogów
        for d in base.rglob("*"):
            if not d.is_dir() or is_excluded(d):
                continue
            if ensure_index(d, False):
                created += 1
                print(f"+ {d/INDEX_NAME}")

    print(
        f"Done. Created/updated {created} index files.
"
        f"Bases: {', '.join(str(b) for b in bases)}
"
        f"FORCE={FORCE} (set AUTO_TOC_FORCE=1 to overwrite)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
#!/usr/bin/env python3
"""
Auto-generuje `index.md` z blokami MyST `toctree` bez ręcznego pisania plików.

Nowości:
- **Automatyczne odkrywanie katalogów** na podstawie baz przekazanych jako
  argumenty CLI, wzorców glob (np. "docs/**/code") albo zmiennej `AUTO_TOC_BASES`.
- **Filtry**: pomija `_build`, `_static`, `_templates`, `_extra`, `.git`, itp.
- **Tworzy indeks tylko tam, gdzie są realne treści** (`.md`/`.rst`) lub podkatalogi
  z takimi treściami — nie zaśmieca pustych folderów.
- **Nie nadpisuje** istniejących `index.md` (chyba że ustawisz `AUTO_TOC_FORCE=1`).

Użycie (CI):
  python docs/_tools/gen_auto_toc.py docs/copilot/sphinx/code
  # albo z wieloma bazami
  python docs/_tools/gen_auto_toc.py docs/copilot/sphinx/code docs/autoapi
  # albo przez zmienną środowiskową (separator ścieżek jak w PATH — ':' na Linuksie)
  AUTO_TOC_BASES="docs/copilot/sphinx/code:docs/autoapi" python docs/_tools/gen_auto_toc.py
  # lub wzorce glob
  python docs/_tools/gen_auto_toc.py "docs/**/code"
"""
from __future__ import annotations
from pathlib import Path
import os
import sys
import glob
from typing import Iterable

INDEX_NAME = "index.md"
FILE_EXTS = {".md", ".rst"}
EXCLUDE_DIRNAMES = {
    "_build", "_static", "_templates", "_extra",
    ".git", ".github", "venv", ".venv", "node_modules", "__pycache__",
}
FORCE = os.getenv("AUTO_TOC_FORCE", "0") == "1"

TEMPLATE_ROOT = """# {title}

```{{toctree}}
:maxdepth: 2
:glob:
:titlesonly:

*/index
*
```
"""

TEMPLATE_SUB = """# {title}

```{{toctree}}
:hidden:
:glob:

*/index
*
```
"""

def is_excluded(p: Path) -> bool:
    # Wyklucz, jeśli którakolwiek część ścieżki jest na liście
    return any(part in EXCLUDE_DIRNAMES for part in p.parts)


def has_doc_files(d: Path) -> bool:
    """Czy katalog zawiera treść wartą indeksowania?"""
    try:
        for f in d.iterdir():
            if f.is_file() and f.suffix.lower() in FILE_EXTS and f.name.lower() != INDEX_NAME:
                return True
        # jeśli nie ma plików, sprawdź bezpośrednie podkatalogi
        for sub in d.iterdir():
            if sub.is_dir() and not is_excluded(sub):
                for f in sub.iterdir():
                    if f.is_file() and f.suffix.lower() in FILE_EXTS:
                        return True
    except Exception:
        pass
    return False


def should_write(idx: Path, root: bool) -> bool:
    if not FORCE and idx.exists():
        return False
    # Dla podkatalogów nie twórz bez treści
    if not root and not has_doc_files(idx.parent):
        return False
    return True


def ensure_index(dirpath: Path, root: bool) -> bool:
    idx = dirpath / INDEX_NAME
    if not should_write(idx, root):
        return False
    title = (dirpath.name or dirpath.resolve().name).strip() or "Index"
    content = (TEMPLATE_ROOT if root else TEMPLATE_SUB).format(title=title)
    idx.write_text(content, encoding="utf-8")
    return True


def expand_bases(argv: list[str]) -> list[Path]:
    candidates: list[str] = []
    env = os.getenv("AUTO_TOC_BASES", "").strip()
    if env:
        # PATH-like: ':' (Linux/macOS) lub ';' (Windows). Obsłuż oba.
        sep = ";" if ";" in env and os.pathsep == ";" else ":"
        for part in env.split(sep):
            if part:
                candidates.append(part)
    # argumenty CLI
    if len(argv) > 1:
        candidates.extend(argv[1:])
    # domyślna baza (jeśli nic nie podano)
    if not candidates:
        candidates = ["docs/copilot/sphinx/code"]

    bases: list[Path] = []
    for c in candidates:
        # obsługa globów
        matches = glob.glob(c, recursive=True) or [c]
        for m in matches:
            p = Path(m).resolve()
            if p.is_dir() and not is_excluded(p):
                bases.append(p)
    # deduplikacja, zachowaj kolejność
    seen = set()
    unique: list[Path] = []
    for b in bases:
        if b not in seen:
            unique.append(b)
            seen.add(b)
    return unique


def main(argv: list[str]) -> int:
    bases = expand_bases(argv)
    if not bases:
        print("! No bases found — nothing to do.")
        return 0

    created = 0
    for base in bases:
        # indeks dla bazy (root)
        if ensure_index(base, True):
            created += 1
            print(f"+ {base/INDEX_NAME}")
        # indeksy dla wszystkich podkatalogów
        for d in base.rglob("*"):
            if not d.is_dir() or is_excluded(d):
                continue
            if ensure_index(d, False):
                created += 1
                print(f"+ {d/INDEX_NAME}")

    print(
        f"Done. Created/updated {created} index files.
"
        f"Bases: {', '.join(str(b) for b in bases)}
"
        f"FORCE={FORCE} (set AUTO_TOC_FORCE=1 to overwrite)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
