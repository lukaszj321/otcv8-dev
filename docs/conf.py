# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x, PyData >=0.16) ---------
from __future__ import annotations

import os
from pathlib import Path
from importlib import import_module

# ── Projekt ───────────────────────────────────────────────────────────────────
project = "OTClient v8 — Developer Documentation"
author = "Dildo"
language = "pl"

# ── Ścieżki ───────────────────────────────────────────────────────────────────
DOCS_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_DIR.parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"
EXTRA_DIR = DOCS_DIR / "_extra"                        # np. mirror LDoc HTML
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"     # musi zawierać index.xml

templates_path = ["_templates"] if TEMPLATES_DIR.exists() else []
html_static_path = ["_static"] if STATIC_DIR.exists() else []
html_extra_path = ["_extra"] if EXTRA_DIR.exists() else []

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    ".venv",
    "venv",
]

# ── Helper do bezpiecznego ładowania rozszerzeń ───────────────────────────────
extensions: list[str] = []

def _try_load(ext: str, strict: bool = False) -> None:
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
    except Exception as e:
        msg = f"[conf.py] ✗ missing: {ext} ({e})"
        if strict:
            raise
        print(msg)

# ── Rdzeń/standard ────────────────────────────────────────────────────────────
_try_load("myst_nb", strict=True)  # MyST + notebooki
_try_load("sphinx.ext.autosectionlabel")
_try_load("sphinx.ext.githubpages")
_try_load("sphinx.ext.todo")
_try_load("sphinx.ext.ifconfig")
_try_load("sphinx.ext.duration")
_try_load("sphinx.ext.graphviz")
_try_load("sphinx.ext.napoleon")
_try_load("sphinx.ext.viewcode")
_try_load("sphinx.ext.intersphinx")
_try_load("sphinx.ext.mathjax")

# ── Doxygen / C++ API ─────────────────────────────────────────────────────────
_try_load("breathe")
_try_load("exhale")

# ── Blog / UX / SEO / extras ─────────────────────────────────────────────────
_try_load("ablog")
_try_load("sphinx_design")
_try_load("sphinxcontrib.mermaid")
_try_load("sphinx_copybutton")
_try_load("sphinxext.opengraph")
_try_load("sphinx_sitemap")
_try_load("sphinx_favicon")
_try_load("sphinx_codeautolink")
_try_load("hoverxref.extension")           # hoverxref
_try_load("sphinx_last_updated_by_git")
_try_load("sphinxcontrib.bibtex")
_try_load("sphinxext.rediraffe")
_try_load("sphinxcontrib.luadomain")
_try_load("sphinxcontrib.jquery")          # nie zaszkodzi, przydaje się z ablog
_try_load("autoapi.extension")             # tylko jeśli chcesz AutoAPI (Python)

# Nie ładuj myst_parser obok myst_nb
if "myst_nb" in extensions and "myst_parser" in extensions:
    extensions.remove("myst_parser")

# ── MyST / Notebooki ──────────────────────────────────────────────────────────
nb_execution_mode = "off"          # szybkie buildy; zmień na "auto" gdy potrzeba
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
    "dollarmath",
    "fieldlist",
]
myst_heading_anchors = 6
myst_fence_as_directive = ["mermaid"]  # ```mermaid → {mermaid}
myst_url_schemes = ["http", "https", "mailto", "tel"]

# Unikalne kotwice nagłówków (eliminuje duplikaty)
autosectionlabel_prefix_document = True

# ── Breathe / Exhale (C++) ────────────────────────────────────────────────────
# Doxygen XML produkowany w CI do docs/_build/doxygen/xml
breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
breathe_default_project = "OTCv8 C++ API"

# Exhale generuje drzewo RST w docs/autoapi/cpp/
exhale_args = {
    "containmentFolder": "autoapi/cpp",
    "rootFileName": "index.rst",
    "rootFileTitle": "OTCv8 C++ API",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,              # Doxygen uruchamiasz w CI
    "doxygenStripFromPath": str(REPO_ROOT),
    # "verboseBuild": True,
}
primary_domain = "cpp"
highlight_language = "cpp"

# ── Własne lexery (ciche fallbacki) ───────────────────────────────────────────
try:
    from sphinx.highlighting import lexers
    from pygments.lexers import get_lexer_by_name
    lexers["otui"] = get_lexer_by_name("yaml")
    lexers["otmod"] = get_lexer_by_name("ini")
except Exception as e:
    print(f"[conf.py] (warn) custom lexers not set: {e}")

# ── Motyw / HTML ──────────────────────────────────────────────────────────────
try:
    import pydata_sphinx_theme  # noqa: F401
    html_theme = "pydata_sphinx_theme"
except Exception:
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"

# Dodatkowe CSS/JS (ładuj tylko, jeśli pliki istnieją)
html_css_files: list[str] = []
def _add_css(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_css_files.append(rel)

for rel in [
    "tables.css",
    "tables-premium.css",
    "custom-dark-mermaid.css",
    "css/custom.css",
    "css/layout.css",
]:
    _add_css(rel)

html_js_files: list[str] = []
def _add_js(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)

for rel in [
    "custom.js",
    "css/canonical-fix.js",  # u Ciebie ten plik jest w _static/css/
]:
    _add_js(rel)

html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_with_keys": True,
    "show_prev_next": True,
    "secondary_sidebar_items": ["page-toc", "sourcelink", "edit-this-page"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lukaszj321/otcv8-dev",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
}

html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# ── Mermaid (client-side) ─────────────────────────────────────────────────────
mermaid_version = "10.9.1"
mermaid_output_format = "raw"
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# ── OpenGraph / SEO / Sitemap ────────────────────────────────────────────────
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"
sitemap_url_scheme = "{link}"

# ── ABlog (odblokowuje .. post::) ────────────────────────────────────────────
blog_title = "Blog"
blog_baseurl = html_baseurl
blog_path = "posts"
blog_post_pattern = "posts/*"
blog_feed_fulltext = True
blog_feed_archives = True
post_auto_excerpt = 1

# Dodatkowe sidebary ABlog (jeśli chcesz)
html_sidebars = {
    "posts/**": [
        "ablog/categories.html",
        "ablog/tagcloud.html",
        "ablog/archives.html",
        "ablog/recentposts.html",
        "ablog/postcard.html",
    ],
    "blog/**": [
        "ablog/categories.html",
        "ablog/tagcloud.html",
        "ablog/archives.html",
        "ablog/recentposts.html",
    ],
}

# ── Copybutton ────────────────────────────────────────────────────────────────
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# ── Hoverxref ─────────────────────────────────────────────────────────────────
hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"

# ── Favicons ──────────────────────────────────────────────────────────────────
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# ── BibTeX (ładuj tylko, gdy pliki istnieją) ─────────────────────────────────
if (DOCS_DIR / "refs.bib").exists():
    bibtex_bibfiles = ["refs.bib"]
else:
    bibtex_bibfiles = []

# ── Intersphinx ───────────────────────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
}

# ── Codeautolink ──────────────────────────────────────────────────────────────
codeautolink_concat_default = True

# ── Graphviz ──────────────────────────────────────────────────────────────────
graphviz_output_format = "svg"

# ── Podświetlanie / Pygments ─────────────────────────────────────────────────
pygments_style = "default"
pygments_dark_style = "native"

# ── Todo ──────────────────────────────────────────────────────────────────────
todo_include_todos = False

# ── Linkcheck (jeśli używasz) ────────────────────────────────────────────────
linkcheck_ignore = [
    r"http://localhost:\d+/",
    r"https://placehold\.co/.*",
    r".*\.local",
]
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── Rediraffe (przekierowania) ────────────────────────────────────────────────
rediraffe_redirects = {
    # "stary/plik.rst": "nowy/plik.rst",
}

# ── Ostrzeżenia / Higiena builda ─────────────────────────────────────────────
suppress_warnings = [
    "myst.header",
    "myst.nb.render",
    "toc.not_readable",
    "design.grid",   # wycisza 'The parent of a "grid-item" should be a "grid-row"'
]

# ── Domeny / języki ──────────────────────────────────────────────────────────
primary_domain = "cpp"
highlight_language = "cpp"

# ── AutoAPI (domyślnie nie skanuje nic) ──────────────────────────────────────
autoapi_type = "python"
autoapi_dirs: list[str] = []  # dodaj ścieżki gdy zechcesz generować API z Pythona

# ── Minimalny setup hook ──────────────────────────────────────────────────────
def setup(app):  # noqa: D401
    """Lekki hook Sphinx."""
    return
