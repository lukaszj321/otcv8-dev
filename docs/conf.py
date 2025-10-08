# -- Project information -----------------------------------------------------
project = "OTCv8 — Dokumentacja"
author = "OTCv8"
language = "pl"

# Plik startowy (masz index.md)
root_doc = "index"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
]

# autosectionlabel: unikalne etykiety z prefiksem ścieżki pliku
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 10

templates_path = ["_templates"]

# Wyklucz śmieci/backupy z budowania (w tym __md_backup_YYYYMMDD_HHMMSS)
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    "**/__md_backup_*",
    "**/__md_backup_*/*",
]

# Obsługa .md i .rst
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# MyST: przydatne dodatki i kotwice H1–H6
myst_enable_extensions = [
    "attrs",
    "colon_fence",
    "deflist",
    "fieldlist",
    "linkify",
    "smartquotes",
    "substitution",
    "tasklist",
    "replacements",
]
myst_heading_anchors = 6

# Ucisz niekrytyczne ostrzeżenia (masz ich dużo w zewn. plikach)
suppress_warnings = [
    "myst.xref_missing",       # brakujące odnośniki/kotwice
    "misc.highlighting_failure",  # problemy z Pygments (np. strzałka → w kodzie)
    "autosectionlabel.*",      # duplikaty etykiet "Funkcje"/"Opis" itd.
]

# Fallback lexery, żeby nie warczało na nieznane języki bloków kodu
from sphinx.highlighting import lexers
from pygments.lexers.special import TextLexer
lexers["otui"] = TextLexer()
lexers["otml"] = TextLexer()
lexers["mermaid"] = TextLexer()

# -- HTML --------------------------------------------------------------------
html_theme = "alabaster"  # wbudowany, bez zależności
html_static_path = ["_static"]
html_title = "OTCv8 — Dokumentacja"
