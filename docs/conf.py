# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x, PyData >=0.16) ---------

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
EXTRA_DIR = DOCS_DIR / "_extra"                       # LDoc HTML mirror
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"    # must contain index.xml

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
extensions = [
    "myst_nb",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
]

# Critical (load if installed)
for ext in ["sphinxcontrib.mermaid", "sphinx_design", "breathe", "exhale"]:
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")

# Optional
for ext in [
    "sphinx_copybutton",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "sphinxcontrib.jquery",
]:
    try:
        import_module(ext)
        extensions.append(ext)
    except Exception:
        pass

# Don’t load myst_parser alongside myst_nb
if "myst_nb" in extensions and "myst_parser" in extensions:
    extensions.remove("myst_parser")

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

# Unique anchors per document
autosectionlabel_prefix_document = True

# ── Breathe (C++) ─────────────────────────────────────────────────────────────
# Doxygen XML is produced in CI into docs/_build/doxygen/xml
breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
breathe_default_project = "OTCv8 C++ API"

# ── Exhale (C++ tree generator) ───────────────────────────────────────────────
# Exhale writes RST into docs/autoapi/cpp/ at build time
exhale_args = {
    "containmentFolder": "autoapi/cpp",
    "rootFileName": "index.rst",
    "rootFileTitle": "OTCv8 C++ API",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,                 # Doxygen runs in CI
    "doxygenStripFromPath": str(REPO_ROOT),         # nicer paths in output
    # "verboseBuild": True,
}
primary_domain = "cpp"
highlight_language = "cpp"

# ── Custom lexers (quiet fallback) ────────────────────────────────────────────
try:
    from sphinx.highlighting import lexers
    # Good-enough stand-ins; avoid hard dependency on specific Pygments classes
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

# CSS (load if files exist, order matters: later overrides earlier)
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

# JS (load if files exist)
html_js_files: list[str] = []
def _add_js(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)

for rel in [
    "custom.js",
    "css/canonical-fix.js",  # u Ciebie ten plik leży w _static/css/
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
# Render raw in browser (no mmdc/puppeteer)
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

# ── Sitemap / Hoverxref (if installed) ────────────────────────────────────────
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

# ── Linkcheck (if used) ───────────────────────────────────────────────────────
linkcheck_ignore = [r'http://localhost:\d+/', r'https://placehold\.co/.*', r'.*\.local']
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── Optional: Copilot snippet (no fail) ───────────────────────────────────────
_copilot_snippet = DOCS_DIR / "copilot" / "sphinx" / "conf_copilot_snippet.py"
if _copilot_snippet.exists():
    try:
        exec(_copilot_snippet.read_text(encoding="utf-8"), {}, {})
        print(f"[conf.py] ✓ Copilot snippet loaded")
    except Exception as e:
        print(f"[conf.py] ✗ Copilot snippet error: {e}")

# ── Minimal setup hook (kept simple on purpose) ───────────────────────────────
def setup(app):  # noqa: D401
    """Lightweight Sphinx setup hook."""
    return
