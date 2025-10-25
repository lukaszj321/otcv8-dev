# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x) ------------------------
from __future__ import annotations

import os
from pathlib import Path
from importlib import import_module

# ── Flags (czytane z env) ─────────────────────────────────────────────────────
OTC_SKIP_CPP = os.getenv("OTC_SKIP_CPP") == "1"   # pomiń C++ API (breathe/exhale)
OTC_LIGHT    = os.getenv("OTC_LIGHT") == "1"      # pomiń wolne rozszerzenia

# ── Project ───────────────────────────────────────────────────────────────────
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
if OTC_SKIP_CPP:
    exclude_patterns += ["autoapi/cpp/**"]

# ── Helpers ───────────────────────────────────────────────────────────────────
def _load(ext: str) -> bool:
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
        return True
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")
        return False

extensions: list[str] = []

# ── Core ──────────────────────────────────────────────────────────────────────
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
    "sphinxcontrib.jquery",
]:
    _load(ext)

# ── C++ toolchain (warunkowo) ─────────────────────────────────────────────────
if not OTC_SKIP_CPP:
    _loaded_breathe = _load("breathe")
    _loaded_exhale  = _load("exhale")
else:
    _loaded_breathe = _loaded_exhale = False
    print("[conf.py] ⇢ OTC_SKIP_CPP=1 → pomijam breathe/exhale i autoapi/cpp")

# ── UI/SEO dodatki (LIGHT pomija wolne) ───────────────────────────────────────
if not OTC_LIGHT:
    for ext in [
        "ablog",
        "sphinxext.opengraph",
        "sphinx_sitemap",
        "sphinx_favicon",
        "hoverxref.extension",
    ]:
        _load(ext)
else:
    print("[conf.py] ⇢ OTC_LIGHT=1 → pomijam ablog/ogp/sitemap/hoverxref/favicons")

# Zawsze przydatne, umiarkowanie lekkie
for ext in [
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinx_codeautolink",
    "sphinxext.rediraffe",
]:
    _load(ext)

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
myst_fence_as_directive = ["mermaid"]
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
        "exhaleExecutesDoxygen": False,                 # Doxygen w CI
        "doxygenStripFromPath": str(REPO_ROOT),
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

# ── Theme ─────────────────────────────────────────────────────────────────────
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

# CSS/JS ładowane tylko jeśli istnieją
html_css_files: list[str] = []
for rel in ["tables.css", "tables-premium.css", "custom-dark-mermaid.css", "css/custom.css", "css/layout.css"]:
    if (STATIC_DIR / rel).exists():
        html_css_files.append(rel)

html_js_files: list[str] = []
for rel in ["custom.js", "css/canonical-fix.js"]:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)

# ── Mermaid ───────────────────────────────────────────────────────────────────
mermaid_version = "10.9.1"
mermaid_output_format = "raw"
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# ── OpenGraph/Sitemap/Hoverxref (część może być pominięta w LIGHT) ───────────
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"
sitemap_url_scheme = "{link}"

# ── Copybutton ────────────────────────────────────────────────────────────────
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# ── Warnings / Todo ───────────────────────────────────────────────────────────
suppress_warnings = ["myst.header", "myst.nb.render"]
todo_include_todos = False

# ── Navbar: dodaj „Copilot Docs” (bez duplikatów) ────────────────────────────
def _on_config_inited(app, config):
    opts = dict(config.html_theme_options or {})
    links = list(opts.get("navbar_links", []))
    if not any(isinstance(x, dict) and x.get("url") in ("copilot/index.html", "dokumentacja%20copilot/index.html") for x in links):
        links.append({"name": "Copilot Docs", "url": "copilot/index.html", "internal": True})
    opts["navbar_links"] = links
    config.html_theme_options = opts

# ── Sanityzacja dependencies (naprawa git timestamps crash) ───────────────────
def _sanitize_dependencies(app, env, *args, **kwargs):
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
            p2 = (base_dir / dep)
            if p2.is_file():
                new_items.append(str(p2.relative_to(root)))
                continue
            removed += 1  # katalog / brak pliku
        deps[docname] = sorted(new_items)
    if removed:
        print(f"[conf.py] sanitized dependencies: removed {removed} non-files")

# ── setup() ───────────────────────────────────────────────────────────────────
def setup(app):
    # alias eventu, którego może szukać stare rozszerzenie
    try:
        app.add_event("env-after-read-docs")
    except Exception:
        pass

    app.connect("config-inited", _on_config_inited, priority=200)
    app.connect("env-check-consistency", _sanitize_dependencies, priority=100)
    app.connect("env-updated", _sanitize_dependencies, priority=100)
