# -- Project information -----------------------------------------------------
project = "OTCv8 — Dokumentacja"
author = "OTCv8"
language = "pl"

# Sphinx 7+: root dokumentu
root_doc = "index"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
]

# autosectionlabel: unikalne etykiety poprzedzone ścieżką pliku
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 10

templates_path = ["_templates"]

# WYKLUCZ backupy i śmieci z budowania
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

# MyST – przydatne rozszerzenia i kotwice do nagłówków
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

# Wycisz głośne, „niekrytyczne” warningi
suppress_warnings = [
    "myst.xref_missing",   # brakujące #kotwice (masz ich dużo w zewn. treściach)
    "autosectionlabel.*",  # duplikaty etykiet przy powtarzających się nagłówkach
]

# Zarejestruj fallback lexery, żeby nie krzyczało, że nie zna 'otui'/'otml'/'mermaid'
from sphinx.highlighting import lexers
from pygments.lexers.special import TextLexer
lexers["otui"] = TextLexer()
lexers["otml"] = TextLexer()
lexers["mermaid"] = TextLexer()

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"  # bezpieczny, dostępny out-of-the-box
html_static_path = ["_static"]
html_title = "OTCv8 — Dokumentacja"
