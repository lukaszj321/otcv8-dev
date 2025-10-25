# -- OTClient v8 Dev Docs — Sphinx config -------------------------------------
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
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"    # powinno zawierać index.xml

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
    # MyST + notebooki
    "myst_nb",
    # core
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
    # C++ API
    "breathe",
    "exhale",
    # UI/SEO
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_sitemap",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "sphinxcontrib.jquery",
    "hoverxref.extension",
    "sphinx_last_updated_by_git",
    "sphinxext.rediraffe",
    # blog (opcjonalnie)
    "ablog",
]

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

# ── Intersphinx (ważne: None, nie {}) ────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# ── Breathe / Exhale (C++) ────────────────────────────────────────────────────
breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
breathe_default_project = "OTCv8 C++ API"

exhale_args = {
    "containmentFolder": "autoapi/cpp",
    "rootFileName": "index.rst",
    "rootFileTitle": "OTCv8 C++ API",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,          # Doxygen odpalasz w CI
    "doxygenStripFromPath": str(REPO_ROOT),  # krótsze ścieżki w output
}
primary_domain = "cpp"
highlight_language = "cpp"

# ── HTML / Theme ──────────────────────────────────────────────────────────────
try:
    import pydata_sphinx_theme  # noqa:F401
    html_theme = "pydata_sphinx_theme"
except Exception:
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"

html_css_files: list[str] = []
for rel in [
    "tables.css",
    "tables-premium.css",
    "custom-dark-mermaid.css",
    "css/custom.css",
    "css/layout.css",
]:
    if (STATIC_DIR / rel).exists():
        html_css_files.append(rel)

html_js_files: list[str] = []
for rel in [
    "custom.js",
    "css/canonical-fix.js",
]:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)

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
    "navbar_links": [
        {"name": "Copilot Docs", "url": "dokumentacja%20copilot/index.html", "internal": True}
    ],
}

html_baseurl = os.environ.get("SPHINX_HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/")
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# ── Mermaid (client-side) ─────────────────────────────────────────────────────
mermaid_version = os.environ.get("SPHINX_MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.environ.get("SPHINX_MERMAID_OUT", "raw")
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# ── OpenGraph / SEO ───────────────────────────────────────────────────────────
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"

# ── Copybutton ────────────────────────────────────────────────────────────────
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# ── Sitemap / Hoverxref ───────────────────────────────────────────────────────
sitemap_url_scheme = "{link}"

hoverxref_default_type = "tooltip"
hoverxref_auto_ref = True
hoverxref_domains = ["std", "py", "cpp"]
hoverxref_role_types = {
    # std
    "ref": "tooltip",
    "doc": "tooltip",
    "term": "tooltip",
    "download": "tooltip",
    "numref": "tooltip",
    # python
    "mod": "tooltip",
    "class": "tooltip",
    "meth": "tooltip",
    "func": "tooltip",
    "attr": "tooltip",
    "exc": "tooltip",
    "obj": "tooltip",
    # cpp
    "t": "tooltip",
}

# ── Favicons ──────────────────────────────────────────────────────────────────
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# ── Warnings / Hygiene ────────────────────────────────────────────────────────
suppress_warnings = ["myst.header", "myst.nb.render", "design.grid"]
nitpicky = False

# ── Todo ──────────────────────────────────────────────────────────────────────
todo_include_todos = False

# ── Linkcheck (opcjonalnie) ──────────────────────────────────────────────────
linkcheck_ignore = [r"http://localhost:\d+/", r"https://placehold\.co/.*", r".*\.local"]
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── sphinx-last-updated-by-git ────────────────────────────────────────────────
git_last_updated_timezone = "UTC"
git_last_updated_fallback = True

# ── Code autolink ─────────────────────────────────────────────────────────────
codeautolink_autodoc_inject = False

# ── Optional: Copilot snippet (load) ─────────────────────────────────────────
_copilot_snippet = DOCS_DIR / "copilot" / "sphinx" / "conf_copilot_snippet.py"
if _copilot_snippet.exists():
    try:
        # wczytujemy w osobnej przestrzeni nazw, żeby łatwiej kontrolować efekty
        _ns: dict = {}
        exec(_copilot_snippet.read_text(encoding="utf-8"), _ns, _ns)
        # przenieś tylko jawnie do globals jeśli potrzeba
        for k, v in _ns.items():
            if k in ("extensions", "html_theme_options", "intersphinx_mapping"):
                globals()[k] = v
        print("[conf.py] ✓ Copilot snippet loaded")
    except Exception as e:
        print(f"[conf.py] ✗ Copilot snippet error: {e}")

# ── TWARDY FIX po snippecie: {} → None w intersphinx ─────────────────────────
try:
    _imap = globals().get("intersphinx_mapping", {})
    if isinstance(_imap, dict):
        fixed = False
        for k, v in list(_imap.items()):
            if isinstance(v, (list, tuple)) and len(v) >= 2:
                url, inv = v[0], v[1]
                if inv in ({}, "", [], ()):
                    _imap[k] = (url, None)
                    fixed = True
        if fixed:
            print("[conf.py] ✎ normalized intersphinx_mapping ({} → None)")
    globals()["intersphinx_mapping"] = _imap
except Exception as e:
    print(f"[conf.py] ✗ intersphinx normalize error: {e}")

# ── Minimal setup hook ────────────────────────────────────────────────────────
def setup(app):  # noqa: D401
    """Lightweight Sphinx setup (no custom events)."""
    return
