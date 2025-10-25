# OTClient v8 — Developer Documentation (Sphinx 8.x)

from __future__ import annotations
import os
import re
from importlib import import_module
from pathlib import Path

# ── Podstawy ────────────────────────────────────────────────────────────────
project = "OTClient v8 — Developer Documentation"
author = "Dildo"
language = "pl"

DOCS_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_DIR.parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"   # ma zawierać index.xml

templates_path = ["_templates"] if TEMPLATES_DIR.exists() else []
html_static_path = ["_static"] if STATIC_DIR.exists() else []
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "**/.ipynb_checkpoints", ".venv", "venv"
]

# ── MyST / Markdown ─────────────────────────────────────────────────────────
# GASI: "Source parser for markdown not registered"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst",
}

# myst-nb (bez wykonywania notebooków w CI)
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
myst_fence_as_directive = ["mermaid"]  # ```mermaid -> {mermaid}

# ── Rozszerzenia ────────────────────────────────────────────────────────────
extensions = [
    # Markdown / notebooks
    "myst_nb",

    # core
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",

    # C++ API
    "breathe",
    "exhale",

    # UI / dodatki
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_sitemap",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "sphinxcontrib.jquery",
    "sphinx_last_updated_by_git",
]

autosectionlabel_prefix_document = True

# ── Breathe / Exhale (C++) ──────────────────────────────────────────────────
breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
breathe_default_project = "OTCv8 C++ API"

exhale_args = {
    "containmentFolder": "autoapi/cpp",
    "rootFileName": "index.rst",
    "rootFileTitle": "OTCv8 C++ API",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,
    "doxygenStripFromPath": str(REPO_ROOT),
}
primary_domain = "cpp"
highlight_language = "cpp"

# ── Motyw / HTML ────────────────────────────────────────────────────────────
try:
    import_module("pydata_sphinx_theme")
    html_theme = "pydata_sphinx_theme"
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

html_baseurl = os.environ.get("SPHINX_HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/")
sitemap_url_scheme = "{link}"

# ── Mermaid (klient) ────────────────────────────────────────────────────────
mermaid_version = os.environ.get("SPHINX_MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.environ.get("SPHINX_MERMAID_OUT", "raw")
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# ── Copybutton ──────────────────────────────────────────────────────────────
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# ── Favicons (opcjonalnie) ─────────────────────────────────────────────────
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# ── Ostrzeżenia ─────────────────────────────────────────────────────────────
suppress_warnings = ["myst.header", "myst.nb.render"]

# ── HOTFIX Exhale: puste dyrektywy zabijają build ───────────────────────────
_EMPTY_DOXY = re.compile(
    r"(?m)^\.\.\s+(doxygenenum|doxygenfunction|doxygenclass|doxygenstruct|"
    r"doxygenvariable|doxygenunion)\s*::\s*$"
)

def _fix_exhale_blank_directives(app, env, docnames):
    """Podmień puste dyrektywy Exhale zanim Sphinx zacznie je czytać."""
    base = DOCS_DIR / "autoapi" / "cpp"
    if not base.exists():
        return
    for p in base.rglob("*.rst"):
        txt = p.read_text(encoding="utf-8")
        if not _EMPTY_DOXY.search(txt):
            continue
        fixed = _EMPTY_DOXY.sub(
            ".. note:: (pominięto pustą dyrektywę wygenerowaną przez Exhale)", txt
        )
        if fixed != txt:
            p.write_text(fixed, encoding="utf-8")

def setup(app):
    # Upewnij się, że Exhale zdążył wygenerować RST → wtedy patchujemy
    app.connect("env-before-read-docs", _fix_exhale_blank_directives)
