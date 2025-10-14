# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 7.4.7, PyData 0.16.1) -----

import os
from pathlib import Path
from importlib import import_module

# -- Project -------------------------------------------------------------------
project = "OTClient v8 — Developer Documentation"
author = "OTClient v8 contributors"
language = "pl"

# -- Paths ---------------------------------------------------------------------
DOCS_DIR = Path(__file__).parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"

templates_path = ["_templates"] if TEMPLATES_DIR.exists() else []
html_static_path = ["_static"] if STATIC_DIR.exists() else []

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    ".venv",
    "venv",
]

# -- Extensions ----------------------------------------------------------------
# Uwaga: NIE ładujemy jednocześnie "myst_parser" i "myst_nb".
extensions = [
    "myst_nb",                      # MyST + notebooki (wykonanie wyłączone poniżej)
    "sphinx.ext.autosectionlabel",  # zamiast pip-owego "sphinx-autosectionlabel"
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
]

# Opcjonalne rozszerzenia — doładuj tylko jeśli są zainstalowane w CI
_optional_exts = [
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinxcontrib.mermaid",
    "sphinx_codeautolink",
    "sphinxcontrib.jquery",
    "sphinx_hoverxref",
]

for ext in list(_optional_exts):
    try:
        # import name == ext (kropki są poprawne, myślników nie używamy w nazwach)
        import_module(ext)
        extensions.append(ext)
    except Exception:
        print(f"[conf.py] optional extension skipped: {ext}")

# Bezpiecznik gdyby ktoś przez przypadek dodał myst_parser obok myst_nb
if "myst_nb" in extensions and "myst_parser" in extensions:
    extensions.remove("myst_parser")

# -- MyST / Notebooks ----------------------------------------------------------
nb_execution_mode = "off"          # nie wykonujemy komórek w CI
nb_execution_timeout = 300

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
    "linkify",
    "attrs_block",
    "attrs_inline",
    "tasklist",
    "smartquotes",
]
myst_heading_anchors = 3

# Labelowanie nagłówków bez kolizji
autosectionlabel_prefix_document = True

# -- HTML / Theme --------------------------------------------------------------
# Jeśli pydata-sphinx-theme nie jest zainstalowany, fallback do alabaster
try:
    import pydata_sphinx_theme  # noqa: F401
    html_theme = "pydata_sphinx_theme"
except Exception:
    print("[conf.py] pydata-sphinx-theme not available — falling back to 'alabaster'")
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"
html_css_files = []
if (STATIC_DIR / "tables-premium.css").exists():
    html_css_files.append("tables-premium.css")

html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_with_keys": True,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lukaszj321/otcv8-dev",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
}

# Publiczny URL dla sitemap/opengraph (zmień jeśli masz inny branch/URL)
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",  # zmień na "main" jeśli używasz main
    "doc_path": "docs",
}

# -- Mermaid (sphinxcontrib-mermaid) -------------------------------------------
mermaid_version = "10.9.0"
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'neutral'});"

# -- OpenGraph / SEO -----------------------------------------------------------
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"
# ogp_image = html_baseurl + "_static/og.png"

# -- Copybutton ----------------------------------------------------------------
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# -- Hoverxref -----------------------------------------------------------------
# (działa tylko jeśli zainstalowane; w przeciwnym razie zostanie pominięte powyżej)
hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"

# -- Sitemap -------------------------------------------------------------------
sitemap_url_scheme = "{link}"

# -- CodeAutolink --------------------------------------------------------------
codeautolink_autodoc_inject = False
codeautolink_concat = True

# -- Favicon -------------------------------------------------------------------
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# -- Warnings / porządek -------------------------------------------------------
suppress_warnings = [
    "myst.header",
    "myst.nb.render",
]

# -- Todo ----------------------------------------------------------------------
todo_include_todos = False

# -- Build hooks ---------------------------------------------------------------
def setup(app):
    pass
