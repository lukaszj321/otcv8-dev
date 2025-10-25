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

# ── Markdown (MyST) ────────────────────────────────────────────────────────
# Wymuś myst_parser i usuń myst_nb, jeśli pojawił się wcześniej
extensions: list[str] = []

def _ensure(ext: str):
    try:
        import_module(ext.replace("-", "_"))
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")

# Parser Markdown
_ensure("myst_parser")

# Rejestracja rozszerzeń
for ext in [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "breathe",
    "exhale",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_sitemap",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "sphinxcontrib.jquery",
    "sphinx_last_updated_by_git",
    "sphinxext.rediraffe",
]:
    _ensure(ext)

# jeśli ktoś dodał myst_nb gdzieś indziej – usuń, żeby nie mieszał parserów
if "myst_nb" in extensions:
    extensions.remove("myst_nb")
    print("[conf.py] – removed myst_nb to avoid parser conflicts")

# Rejestracja sufiksów źródeł (ustaw tylko, gdy myst_parser jest dostępny)
try:
    import myst_parser  # noqa: F401
    source_suffix = {".rst": "restructuredtext", ".md": "myst"}
except Exception:
    source_suffix = {".rst": "restructuredtext"}
    print("[conf.py] ! myst_parser not installed; .md will be ignored")

# MyST konfiguracja (bez notebooków)
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

html_baseurl = os.environ.get(
    "SPHINX_HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/"
)
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

# ── InterSphinx ─────────────────────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# ── Ostrzeżenia ─────────────────────────────────────────────────────────────
suppress_warnings = ["myst.header"]

# ── HOTFIX: usuń *całe* puste bloki .. doxygen*:: łącznie z opcjami ─────────
# Przykład do usunięcia:
#   .. doxygenenum::
#      :project: OTCv8 C++ API
#      :no-link:
# (bez żadnego argumentu po ::)
_RE_EMPTY_DOXY_BLOCK = re.compile(
    r"""
    (?mxs)                                  # flags: multiline, verbose, dotall
    ^[ \t]*\.\.\s+doxygen(?:enum|function|class|struct|variable|union)\s*::\s*  # dyrektywa bez argumentu
    (?:\n[ \t]*:[^\n]*?)*                    # 0+ wierszy opcji typu ':option: value'
    (?:\n[ \t]*)?                            # opcjonalny pusty wiersz końcowy
    """,
)

def _strip_blank_doxygen(app, docname, source):
    if not docname.startswith("autoapi/cpp/"):
        return
    txt = source[0]
    new = _RE_EMPTY_DOXY_BLOCK.sub("", txt)
    if new != txt:
        source[0] = new

def setup(app):
    app.connect("source-read", _strip_blank_doxygen)
