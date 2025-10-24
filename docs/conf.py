# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x, PyData) ---------------

from __future__ import annotations

import os
from pathlib import Path
from importlib import import_module

# ── Project ────────────────────────────────────────────────────────────────────
project = "OTClient v8 — Developer Documentation"
author = "Dildo"
language = "pl"

# ── Paths ─────────────────────────────────────────────────────────────────────
DOCS_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_DIR.parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"
EXTRA_DIR = DOCS_DIR / "_extra"                       # np. mirror LDoc
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"    # ma zawierać index.xml

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

# Gdy masz jednocześnie index.md i index.rst w tym samym miejscu — wycisz warning:
if (DOCS_DIR / "copilot" / "sphinx" / "index.rst").exists() and (DOCS_DIR / "copilot" / "sphinx" / "index.md").exists():
    exclude_patterns.append("copilot/sphinx/index.rst")

# ── Helpers ───────────────────────────────────────────────────────────────────
extensions: list[str] = []

def _add_ext(name: str) -> None:
    try:
        import_module(name.replace(":", "."))  # np. hoverxref.extension
        extensions.append(name)
        print(f"[conf.py] ✓ loaded: {name}")
    except Exception as e:
        print(f"[conf.py] ✗ missing: {name} ({e})")

# ── Core / std extensions ─────────────────────────────────────────────────────
for ext in [
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
]:
    _add_ext(ext)

# ── Key addons ────────────────────────────────────────────────────────────────
for ext in [
    "breathe",
    "exhale",
    "ablog",
    "sphinx_design",
    "sphinxcontrib.mermaid",
]:
    _add_ext(ext)

# ── Optional addons (load if present) ─────────────────────────────────────────
for ext in [
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_sitemap",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "hoverxref.extension",
    "sphinx_last_updated_by_git",
    "sphinxcontrib.bibtex",
    "sphinxext.rediraffe",
    "sphinxcontrib.luadomain",
    "sphinxcontrib.jquery",
    # UWAGA: autoapi dodamy warunkowo niżej, gdy mamy skonfigurowane katalogi
]:
    _add_ext(ext)

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

# Unikalne kotwice na dokument
autosectionlabel_prefix_document = True

# ── Intersphinx ───────────────────────────────────────────────────────────────
# W Sphinx 8 drugi element krotki to None (nie puste {})
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
intersphinx_timeout = 5

# ── Breathe / Exhale (C++) ────────────────────────────────────────────────────
breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
breathe_default_project = "OTCv8 C++ API"

exhale_args = {
    "containmentFolder": "autoapi/cpp",
    "rootFileName": "index.rst",
    "rootFileTitle": "OTCv8 C++ API",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,         # Doxygen uruchamiany w CI
    "doxygenStripFromPath": str(REPO_ROOT), # ładniejsze ścieżki
    # "verboseBuild": True,
}
primary_domain = "cpp"
highlight_language = "cpp"

# ── Custom lexers (fallback cicho) ────────────────────────────────────────────
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
except Exception:
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"

# CSS — ładuj tylko istniejące
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

# JS — ładuj tylko istniejące
html_js_files: list[str] = []
def _add_js(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)

for rel in [
    "custom.js",
    "css/canonical-fix.js",  # jeśli plik leży w _static/css/
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

# ── OpenGraph / SEO ───────────────────────────────────────────────────────────
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"

# ── Copybutton ────────────────────────────────────────────────────────────────
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# ── Sitemap / Hoverxref / BibTeX (jeśli zainstalowane) ───────────────────────
sitemap_url_scheme = "{link}"

hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"
# hoverxref_tooltip_api_host = "https://readthedocs.org"  # opcjonalnie

bibtex_bibfiles = []  # dodaj pliki .bib jeśli używasz

# ── Favicons ──────────────────────────────────────────────────────────────────
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# ── Warnings / Hygiene ────────────────────────────────────────────────────────
suppress_warnings = ["myst.header", "myst.nb.render"]

# ── Todo ──────────────────────────────────────────────────────────────────────
todo_include_todos = False

# ── Linkcheck (jeśli używasz) ─────────────────────────────────────────────────
linkcheck_ignore = [r'http://localhost:\d+/', r'https://placehold\.co/.*', r'.*\.local']
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── AutoAPI (ładuj TYLKO gdy skonfigurowane) ──────────────────────────────────
# Ustaw w CI: AUTOAPI_DIRS="src:more_src" aby włączyć
_AUTOAPI_DIRS_ENV = os.getenv("AUTOAPI_DIRS", "").strip()
if _AUTOAPI_DIRS_ENV:
    _dirs = [d for d in (p.strip() for p in _AUTOAPI_DIRS_ENV.split(":")) if d]
    if _dirs:
        _add_ext("autoapi.extension")
        autoapi_type = "python"
        autoapi_dirs = _dirs
        autoapi_add_toctree_entry = False  # opcjonalnie
        # autoapi_generate_api_docs = True
        # autoapi_keep_files = False

# ── Optional: Copilot snippet (bez fail; przekazujemy potrzebne zmienne) ─────
def _exec_copilot_snippet(snippet_path: Path) -> None:
    try:
        code = snippet_path.read_text(encoding="utf-8")
        ns = {
            # to, co snippet może chcieć modyfikować / czytać:
            "extensions": extensions,
            "html_theme_options": html_theme_options,
            "html_css_files": html_css_files,
            "html_js_files": html_js_files,
            "html_context": html_context,
            "html_title": html_title,
            "html_theme": html_theme,
        }
        exec(compile(code, str(snippet_path), "exec"), ns, ns)
        # synchronizacja zmian z conf.py:
        for key in ["extensions", "html_theme_options", "html_css_files", "html_js_files", "html_context", "html_title", "html_theme"]:
            if key in ns:
                globals()[key] = ns[key]
        print("[conf.py] ✓ Copilot snippet loaded")
    except Exception as e:
        print(f"[conf.py] ✗ Copilot snippet error: {e}")

_copilot_snippet = DOCS_DIR / "copilot" / "sphinx" / "conf_copilot_snippet.py"
if _copilot_snippet.exists():
    _exec_copilot_snippet(_copilot_snippet)

# ── Minimal setup hook ────────────────────────────────────────────────────────
def setup(app):  # noqa: D401
    """Lightweight Sphinx setup hook."""
    return
