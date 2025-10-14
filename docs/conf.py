# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 7.4.7, PyData 0.16.1) -----------------

import os
from pathlib import Path

# -- Project -------------------------------------------------------------------
project = "OTClient v8 — Developer Documentation"
author = "Dildo"
language = "pl"  # możesz zmienić na 'en' jeśli wolisz

# -- Paths ---------------------------------------------------------------------
DOCS_DIR = Path(__file__).parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"

templates_path = ["_templates"] if TEMPLATES_DIR.exists() else []
html_static_path = ["_static"] if STATIC_DIR.exists() else []
html_css_files = []
if (STATIC_DIR / "tables-premium.css").exists():
    html_css_files.append("tables-premium.css")

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
    "myst_nb",                      # MyST + notebooki (ale wykonanie wyłączone poniżej)
    "sphinx.ext.autosectionlabel",  # zastępuje nieistniejący pip-pakiet "sphinx-autosectionlabel"
    "sphinx.ext.githubpages",       # .nojekyll
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",

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

# -- MyST / Notebooks ----------------------------------------------------------
# Wyłączamy wykonywanie komórek (bezpiecznie dla CI, szybkie buildy)
nb_execution_mode = "off"
nb_execution_timeout = 300

# Rozszerzenia MyST
myst_enable_extensions = [
    "colon_fence",     # ```{admonition} / {toctree} / {csv-table} itp.
    "deflist",
    "substitution",
    "linkify",
    "attrs_block",
    "attrs_inline",
    "tasklist",
    "smartquotes",
]
myst_heading_anchors = 3  # automatyczne kotwice H1..H3

# Autosectionlabel — prefiksuj dokumentem, żeby uniknąć kolizji nagłówków
autosectionlabel_prefix_document = True

# -- HTML ----------------------------------------------------------------------
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "logo": {
        # Dodaj jeśli masz logo w _static
        # "text": "OTClient v8",
    },
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

html_title = "OTClient v8 — Authoring & API"
# Dla sitemap i ogp musisz podać publiczny URL
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",   # lub "main" jeśli używasz main
    "doc_path": "docs",
}

# -- Mermaid (sphinxcontrib-mermaid) -------------------------------------------
# Neutralny motyw — dobrze czytelny w light/dark
mermaid_version = "10.9.0"
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'neutral'});"

# -- OpenGraph / SEO -----------------------------------------------------------
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"
# ogp_image = "https://lukaszj321.github.io/otcv8-dev/_static/og.png"  # jeśli posiadasz

# -- Copybutton ----------------------------------------------------------------
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# -- Hoverxref -----------------------------------------------------------------
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

# -- Warnings / czyszczenie szumu ---------------------------------------------
suppress_warnings = [
    # Przydatne, gdy mieszamy MyST i duże zbiory
    "myst.header",
    "myst.nb.render",
]

# -- Todo ----------------------------------------------------------------------
todo_include_todos = False  # ustaw True, jeśli chcesz renderować .. todo::

# -- Build hooks (opcjonalne) --------------------------------------------------
def setup(app):
    # Jeżeli masz własne CSS/JS do wstrzyknięcia warunkowo — zrób to tutaj
    pass
