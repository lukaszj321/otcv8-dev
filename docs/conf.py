# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x) ------------------------
from __future__ import annotations

import os
from pathlib import Path
from importlib import import_module

# ── Project ────────────────────────────────────────────────────────────────────
project = "OTClient v8 — Developer Documentation"
author = "Dildo"
language = "pl"

# ── Root doc / parsers / intersphinx / hoverxref ──────────────────────────────
# (naprawia błędy z master doc + intersphinx)
root_doc = "index"       # Sphinx 8+
master_doc = root_doc    # dla zgodności z rozszerzeniami

# Obsługuj .rst i .md
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Stabilne, niepuste inventory (ważne: drugi element to None, nie {})
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# hoverxref – zdefiniowane style dla :ref: itd., żeby nie pluło ostrzeżeniami
hoverxref_role_types = {
    "ref": "tooltip",
    "doc": "tooltip",
    "mod": "tooltip",
}

# ── Paths ─────────────────────────────────────────────────────────────────────
DOCS_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_DIR.parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"
EXTRA_DIR = DOCS_DIR / "_extra"                        # np. mirror LDoc
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

# ── Extensions ────────────────────────────────────────────────────────────────
extensions: list[str] = [
    # Podstawowe
    "myst_nb",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
]

# “Best-effort” doładowanie rozszerzeń: ładowane tylko jeśli są zainstalowane
def _try(ext: str, as_name: str | None = None) -> None:
    try:
        import_module(ext)
        extensions.append(as_name or ext)
        print(f"[conf.py] ✓ loaded: {as_name or ext}")
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")

# Krytyczne dla layoutu / C++
for ext in ["breathe", "exhale", "sphinx_design", "sphinxcontrib.mermaid"]:
    _try(ext)

# Dodatkowe (jeśli są w reqs, to się załadują)
for ext in [
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_sitemap",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "hoverxref.extension",
    "sphinxext.rediraffe",
    "sphinxcontrib.jquery",
    # NIE ładujemy bibtex bez skonfigurowanych plików .bib
    # "sphinxcontrib.bibtex",
]:
    _try(ext)

# ── MyST / notebooks ──────────────────────────────────────────────────────────
nb_execution_mode = "off"
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
myst_fence_as_directive = ["mermaid"]  # ```mermaid → {mermaid}

# Unikalne anchory per dokument
autosectionlabel_prefix_document = True

# ── Breathe / Exhale (C++) ────────────────────────────────────────────────────
breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
breathe_default_project = "OTCv8 C++ API"

exhale_args = {
    "containmentFolder": "autoapi/cpp",
    "rootFileName": "index.rst",
    "rootFileTitle": "OTCv8 C++ API",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,      # doxygen uruchamiany w CI
    "doxygenStripFromPath": str(REPO_ROOT),
}

primary_domain = "cpp"
highlight_language = "cpp"

# ── Custom lexers (fallback na wbudowane) ─────────────────────────────────────
try:
    from sphinx.highlighting import lexers
    from pygments.lexers import get_lexer_by_name
    lexers["otui"] = get_lexer_by_name("yaml")
    lexers["otmod"] = get_lexer_by_name("ini")
except Exception as e:
    print(f"[conf.py] (warn) custom lexers not set: {e}")

# ── HTML / Theme ──────────────────────────────────────────────────────────────
try:
    import pydata_sphinx_theme  # noqa
    html_theme = "pydata_sphinx_theme"
    print("[conf.py] ✓ using theme: pydata_sphinx_theme")
except Exception:
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"

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

html_baseurl = os.getenv("SPHINX_HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/")
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# CSS (ładuj tylko jeśli istnieją — kolejność: późniejsze nadpisują wcześniejsze)
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

# JS (ładuj tylko jeśli istnieją)
html_js_files: list[str] = []
def _add_js(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)

for rel in [
    "custom.js",
    "css/canonical-fix.js",
]:
    _add_js(rel)

# ── Mermaid (client-side) ─────────────────────────────────────────────────────
mermaid_version = os.getenv("SPHINX_MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.getenv("SPHINX_MERMAID_OUT", "raw")  # raw/svg
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# ── OpenGraph / SEO ───────────────────────────────────────────────────────────
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"

# ── Copybutton ────────────────────────────────────────────────────────────────
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# ── Sitemap / Hoverxref (jeśli załadowane) ────────────────────────────────────
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"

# ── Favicons ──────────────────────────────────────────────────────────────────
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# ── Warnings / Hygiene ────────────────────────────────────────────────────────
suppress_warnings = ["myst.header", "myst.nb.render"]

# ── Todo ──────────────────────────────────────────────────────────────────────
todo_include_todos = False

# ── Linkcheck ─────────────────────────────────────────────────────────────────
linkcheck_ignore = [r'http://localhost:\d+/', r'https://placehold\.co/.*', r'.*\.local']
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── Minimal setup hook (nic nie podpinamy do eventów Sphinxa) ────────────────
def setup(app):  # noqa: D401
    """Lightweight Sphinx setup hook (no custom events)."""
    print("[conf.py] ✓ conf loaded")
    return
