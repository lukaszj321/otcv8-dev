# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x) ------------------------
from __future__ import annotations

import os
import subprocess
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
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"   # musi zawierać index.xml

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

# ── Extensions ────────────────────────────────────────────────────────────────
def _load(ext: str) -> bool:
    """Spróbuj załadować rozszerzenie; wypisz status."""
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
        return True
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")
        return False

extensions: list[str] = []
# Core
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
    _load(ext)

# C++ toolchain
_loaded_breathe = _load("breathe")
_loaded_exhale = _load("exhale")

# Dodatki UI/SEO
_load("ablog")
_load("sphinx_design")
_load("sphinxcontrib.mermaid")
_load("sphinx_copybutton")
_load("sphinxext.opengraph")
_load("sphinx_sitemap")
_load("sphinx_favicon")
_load("sphinx_codeautolink")
_load("hoverxref.extension")
_load("sphinx_last_updated_by_git")
_load("sphinxext.rediraffe")
_load("sphinxcontrib.jquery")

# Uwaga: celowo NIE ładuję 'sphinxcontrib.bibtex' i 'autoapi.extension'
#       (oba wcześniej powodowały obowiązkowe ustawienia).

# ── Intersphinx ───────────────────────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

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
autosectionlabel_prefix_document = True

# ── Breathe / Exhale (C++) ────────────────────────────────────────────────────
if _loaded_breathe:
    breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
    breathe_default_project = "OTCv8 C++ API"

if _loaded_exhale:
    exhale_args = {
        "containmentFolder": "autoapi/cpp",
        "rootFileName": "index.rst",
        "rootFileTitle": "OTCv8 C++ API",
        "createTreeView": True,
        "exhaleExecutesDoxygen": False,         # Doxygen odpalany w CI
        "doxygenStripFromPath": str(REPO_ROOT), # ładniejsze ścieżki
        # "verboseBuild": True,
    }
primary_domain = "cpp"
highlight_language = "cpp"

# ── Custom lexers (fallback) ──────────────────────────────────────────────────
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
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

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

html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# CSS — załaduj tylko istniejące
html_css_files: list[str] = []
def _add_css(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_css_files.append(rel)
for rel in ["tables.css", "tables-premium.css", "custom-dark-mermaid.css", "css/custom.css", "css/layout.css"]:
    _add_css(rel)

# JS — załaduj tylko istniejące
html_js_files: list[str] = []
def _add_js(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)
for rel in ["custom.js", "css/canonical-fix.js"]:
    _add_js(rel)

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

# ── Sitemap / Hoverxref (bezpieczne minimum) ─────────────────────────────────
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"

# ── Warnings / Hygiene ────────────────────────────────────────────────────────
suppress_warnings = ["myst.header", "myst.nb.render"]

# ── Todo ──────────────────────────────────────────────────────────────────────
todo_include_todos = False

# ── Linkcheck (jeśli kiedyś użyjesz -b linkcheck) ────────────────────────────
linkcheck_ignore = [r"http://localhost:\d+/", r"https://placehold\.co/.*", r".*\.local"]
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── Navbar: dodaj „Copilot Docs” (bez duplikatów) ────────────────────────────
def _on_config_inited(app, config):
    opts = dict(config.html_theme_options or {})
    links = list(opts.get("navbar_links", []))
    if not any(isinstance(x, dict) and x.get("url") in ("copilot/index.html", "dokumentacja%20copilot/index.html") for x in links):
        links.append({"name": "Copilot Docs", "url": "copilot/index.html", "internal": True})
    opts["navbar_links"] = links
    config.html_theme_options = opts

# ── KRYTYCZNE: sanitizacja dependencies zanim ruszy sphinx_last_updated_by_git
def _sanitize_dependencies(app, env, *args, **kwargs):
    """
    Usuń z dependencies wpisy, które nie są plikami (np. 'copilot/diagrams').
    Dzięki temu 'git log <dep>' nie poleci na katalogach / nieistniejących ścieżkach.
    """
    deps = getattr(env, "dependencies", None) or getattr(env, "_dependencies", None)
    if not deps:
        return
    root = Path(env.srcdir)
    removed = 0
    for docname, items in list(deps.items()):
        base_dir = root / docname.rsplit("/", 1)[0] if "/" in docname else root
        new_items: list[str] = []
        for dep in set(items):
            p = (root / dep)
            if p.is_file():
                new_items.append(dep)
                continue
            # spróbuj zinterpretować relatywnie do katalogu dokumentu
            p2 = (base_dir / dep)
            if p2.is_file():
                new_items.append(str(p2.relative_to(root)))
                continue
            # jeśli to katalog / nie istnieje — wywal
            removed += 1
        deps[docname] = sorted(new_items)
    if removed:
        print(f"[conf.py] sanitized dependencies: removed {removed} non-files")

def setup(app):
    # dodaj link do navbaru wcześnie
    app.connect("config-inited", _on_config_inited, priority=200)
    # posprzątaj dependencies PRZED „last_updated_by_git”
    app.connect("env-check-consistency", _sanitize_dependencies, priority=100)
    app.connect("env-updated", _sanitize_dependencies, priority=100)

# ── KONIEC --------------------------------------------------------------------
