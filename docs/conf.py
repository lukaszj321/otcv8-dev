<<<<<<< HEAD
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
=======
# --- podstawy ---
project = "otcv8-dev"
author = "otcv8-dev"
language = "pl"

# --- rozszerzenia ---
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinxcontrib.mermaid",
    "sphinx_codeautolink",
    "hoverxref.extension",
]

myst_enable_extensions = ["colon_fence", "linkify", "attrs_block", "deflist", "tasklist"]
myst_heading_anchors = 3
source_suffix = {".md": "myst", ".rst": "restructuredtext"}

# --- HTML / Furo ---
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
pygments_dark_style = "native"

html_title = "OTCv8 — Dokumentacja"
html_theme_options = {
    "light_logo": "img/logo-light.svg",
    "dark_logo": "img/logo-dark.svg",
    "sidebar_hide_name": True,
    "announcement": "📣 Dev build dokumentacji (auto z CI).",
}

# --- sitemap / ogp / favicon ---
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
ogp_site_url = "https://lukaszj321.github.io/otcv8-dev/"
ogp_image = "https://lukaszj321.github.io/otcv8-dev/_static/cover.png"

favicons = [
    {"rel": "icon", "href": "favicon.svg"},
]
>>>>>>> a68ef8f068e3a76726d61ab5d4d6927f4a2d0ccb
