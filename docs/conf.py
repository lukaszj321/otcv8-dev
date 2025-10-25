# -- OTClient v8 Dev Docs — conf.py ------------------------------------------------
from __future__ import annotations
import os, re
from pathlib import Path

# --- Project ---
project = "OTClient v8 — Developer Documentation"
author = "Dildo"
language = "pl"

# --- Paths ---
DOCS_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_DIR.parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"   # musi zawierać index.xml

templates_path = ["_templates"] if TEMPLATES_DIR.exists() else []
html_static_path = ["_static"] if STATIC_DIR.exists() else []

exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "**/.ipynb_checkpoints", ".venv", "venv"
]

# --- Extensions (BEZ myst_nb) ---
extensions = [
    "myst_parser",
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
]

# --- MyST ---
source_suffix = {".rst": "restructuredtext", ".md": "myst"}
myst_enable_extensions = [
    "colon_fence", "deflist", "substitution", "linkify",
    "attrs_block", "attrs_inline", "tasklist", "smartquotes",
]
myst_heading_anchors = 3

# --- Intersphinx (pewne wartości, żadnych {}!) ---
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# --- Breathe / Exhale ---
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

# --- Theme / HTML ---
html_theme = "pydata_sphinx_theme"
html_title = "OTClient v8 — Authoring & API"
html_baseurl = os.environ.get("SPHINX_HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/")

html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_with_keys": True,
    "show_prev_next": True,
    "secondary_sidebar_items": ["page-toc", "sourcelink", "edit-this-page"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {"name": "GitHub", "url": "https://github.com/lukaszj321/otcv8-dev",
         "icon": "fa-brands fa-github", "type": "fontawesome"},
    ],
}
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# --- Mermaid ---
mermaid_version = os.environ.get("SPHINX_MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.environ.get("SPHINX_MERMAID_OUT", "raw")
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# --- Sitemap / OGP ---
sitemap_url_scheme = "{link}"
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"

# --- Copybutton ---
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# --- Hygiene ---
suppress_warnings = ["myst.header"]

# --- SAFE fix: usuń *puste* dyrektywy od Exhale (np. '.. doxygenenum::' bez argumentu) ---
_DOXY_BLANK_RE = re.compile(
    r"(?ms)^\.\.\s+doxygen(?:enum|function|typedef|define|var|class|struct|union|namespace|file)::\s*\n\s*:project:[^\n]+\n"
)

# --- fix for sphinx_last_updated_by_git + Sphinx 8 ---
# Upewnij się, że MyST jest zarejestrowany jako parser .md
extensions = list(dict.fromkeys(globals().get("extensions", []) + [
    "myst_parser",
    "sphinx_last_updated_by_git",
]))

# Parsery źródeł: .rst i .md (MyST)
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst",
}

# Minimalny zestaw rozszerzeń MyST używany w Twoich plikach
myst_enable_extensions = list(dict.fromkeys(
    globals().get("myst_enable_extensions", []) + [
        "colon_fence", "deflist", "attrs_block", "attrs_inline",
        "linkify", "tasklist", "substitution",
    ]
))

# 1) Nie chodź po zależnościach, jeśli dany plik nie jest śledzony przez Gita
git_untracked_check_dependencies = False

# 2) Wyklucz katalog z diagramami z obliczania timestampów (źródła i dependency)
git_exclude_patterns = list(dict.fromkeys(
    globals().get("git_exclude_patterns", []) + [
        "copilot/diagrams", "copilot/diagrams/**"
    ]
))

# (Bezpiecznik, tylko ostrzeżenia – nie błąd – jeśli Sphinx poda brakujące dependency)
suppress_warnings = list(dict.fromkeys(
    globals().get("suppress_warnings", []) + [
        "git.dependency_not_found",
    ]
))
# --- end fix ---

def _strip_exhale_blanks(app, docname, source):
    # tylko autoapi/cpp (tam Exhale wrzuca RST)
    if not docname.startswith("autoapi/"):
        return
    text = source[0]
    new = _DOXY_BLANK_RE.sub(".. note:: (pominięto pustą dyrektywę wygenerowaną automatycznie)\n", text)
    if new != text:
        source[0] = new

def setup(app):
    app.connect("source-read", _strip_exhale_blanks)
