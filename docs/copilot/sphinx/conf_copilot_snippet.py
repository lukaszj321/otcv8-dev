# --- Copilot Docs snippet (append to your conf.py) ---
from pathlib import Path

# 1) Upewnij się, że mamy wymagane rozszerzenia/opsje motywu
extensions = list(sorted(set(globals().get("extensions", []) + ["sphinx.ext.graphviz"])))
html_theme_options = dict(globals().get("html_theme_options", {}) or {})

# 2) Link w nawigacji PyData (używamy external_links – wspierane przez pydata-sphinx-theme)
ext_links = list(html_theme_options.get("external_links", []))
copilot_link = {"name": "Copilot Docs", "url": "copilot/index.html"}  # poprawna ścieżka
if not any(x.get("url") == copilot_link["url"] for x in ext_links):
    ext_links.append(copilot_link)
html_theme_options["external_links"] = ext_links

# 3) KLUCZOWE: rejestruj pliki (nie katalog) jako zależności dla sekcji "copilot"
DOCS_DIR = Path(__file__).parent.resolve()
DIAGRAMS_DIR = DOCS_DIR / "copilot" / "diagrams"

# Jeśli chcesz filtrować typy plików, ustaw suffixy, np. {".md", ".mmd", ".mermaid", ".dot", ".gv", ".png", ".svg"}
_ACCEPT_SUFFIXES = None  # None = bierz wszystkie pliki

def _iter_diagram_files():
    if not DIAGRAMS_DIR.exists():
        return
    for p in DIAGRAMS_DIR.rglob("*"):
        if p.is_file():
            if _ACCEPT_SUFFIXES is None or p.suffix.lower() in _ACCEPT_SUFFIXES:
                yield p

def _add_copilot_diagram_deps(app, docname, source):
    # Podpina zależności do wszystkich stron zaczynających się od "copilot"
    if not docname.startswith("copilot"):
        return
    for p in _iter_diagram_files():
        rel = p.relative_to(DOCS_DIR)
        # WAŻNE: przekazujemy ŚCIEŻKĘ DO PLIKU, nie katalog
        app.env.note_dependency(str(rel))

def setup(app):
    app.connect("source-read", _add_copilot_diagram_deps)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
# --- end ---
