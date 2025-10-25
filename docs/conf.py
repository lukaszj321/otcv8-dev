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
EXTRA_DIR = DOCS_DIR / "_extra"                      # opcjonalne (np. mirror LDoc)
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"   # index.xml tu musi trafić

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

for ext in ["breathe", "exhale", "sphinx_design", "sphinxcontrib.mermaid"]:
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")

for ext in [
    "ablog",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_sitemap",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "hoverxref.extension",
    "sphinx_last_updated_by_git",
    "sphinxext.rediraffe",
    "sphinxcontrib.jquery",
]:
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
    except Exception:
        pass

# nie ładujemy bibtex/autoapi, bo wymagają dodatkowych ustawień
for maybe in ("autoapi.extension", "sphinxcontrib.bibtex"):
    if maybe in extensions:
        extensions.remove(maybe)

if "myst_nb" in extensions and "myst_parser" in extensions:
    extensions.remove("myst_parser")

# ── InterSphinx ───────────────────────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# ── MyST / notebooks ──────────────────────────────────────────────────────────
nb_execution_mode = "off"
nb_execution_timeout = 300
myst_enable_extensions = [
    "colon_fence", "deflist", "substitution", "linkify",
    "attrs_block", "attrs_inline", "tasklist", "smartquotes",
]
myst_heading_anchors = 3
myst_fence_as_directive = ["mermaid"]
autosectionlabel_prefix_document = True

# ── Breathe / Exhale ─────────────────────────────────────────────────────────
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

# ── Pygments fallback lexers ──────────────────────────────────────────────────
try:
    from sphinx.highlighting import lexers
    from pygments.lexers import get_lexer_by_name
    lexers["otui"] = get_lexer_by_name("yaml")
    lexers["otmod"] = get_lexer_by_name("ini")
except Exception as e:
    print(f"[conf.py] (warn) custom lexers not set: {e}")

# ── Theme / HTML ──────────────────────────────────────────────────────────────
try:
    import pydata_sphinx_theme  # noqa
    html_theme = "pydata_sphinx_theme"
    print("[conf.py] ✓ using theme: pydata_sphinx_theme")
except Exception:
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"

html_css_files: list[str] = []
def _add_css(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_css_files.append(rel)
for rel in ["tables.css","tables-premium.css","custom-dark-mermaid.css","css/custom.css","css/layout.css"]:
    _add_css(rel)

html_js_files: list[str] = []
def _add_js(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)
for rel in ["custom.js", "css/canonical-fix.js"]:
    _add_js(rel)

html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_with_keys": True,
    "show_prev_next": True,
    "secondary_sidebar_items": ["page-toc", "sourcelink", "edit-this-page"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {"name": "GitHub", "url": "https://github.com/lukaszj321/otcv8-dev", "icon": "fa-brands fa-github", "type": "fontawesome"},
    ],
    "navbar_links": [],
}

html_baseurl = os.getenv("HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/")
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# ── Mermaid ──────────────────────────────────────────────────────────────────
mermaid_version = os.getenv("MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.getenv("MERMAID_OUTPUT", "raw")
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# ── OpenGraph / Copybutton / Sitemap / Hoverxref ─────────────────────────────
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"

favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

suppress_warnings = ["myst.header", "myst.nb.render"]
todo_include_todos = False

linkcheck_ignore = [r'http://localhost:\d+/', r'https://placehold\.co/.*', r'.*\.local']
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── (opcjonalne) Copilot snippet ─────────────────────────────────────────────
_copilot_snippet = DOCS_DIR / "copilot" / "sphinx" / "conf_copilot_snippet.py"
if _copilot_snippet.exists():
    try:
        exec(_copilot_snippet.read_text(encoding="utf-8"), {}, {})
        print(f"[conf.py] ✓ Copilot snippet loaded")
    except Exception as e:
        print(f"[conf.py] ✗ Copilot snippet error: {e}")

# ── HOT-FIX: przyspieszenie sphinx_last_updated_by_git bez wyłączania go ─────
# cel: ograniczyć/wyczyścić dependencies ZANIM plugin zacznie liczyć czasy Gita
GIT_DEPS_MAX = int(os.getenv("OTC_GIT_DEPS_MAX", "64"))
# katalogi, których nie dodajemy jako „dependencies” (strony nadal się budują!)
GIT_DEPS_EXCLUDE = (
    "copilot/diagrams",
    "copilot/sphinx/src_code",
    "autoapi/cpp",
    "_images", "_static", "_build",
)

def _patch_env_dependency_filter(app, docnames):
    """Uruchamia się PRZED czytaniem źródeł. Podmieniamy note_dependency,
    żeby nie rejestrować ciężkich ścieżek w env.dependencies."""
    env = app.builder.env
    orig = env.note_dependency

    def _filtered(dep):
        # normalizacja względna
        dep = dep.replace("\\", "/").lstrip("./")
        for p in GIT_DEPS_EXCLUDE:
            if dep == p or dep.startswith(p + "/"):
                return  # pomijamy
        return orig(dep)

    env.note_dependency = _filtered
    print("[conf.py] patched env.note_dependency (filter heavy deps)")

def _sanitize_dependencies(app, env, *args, **kwargs):
    """Dodatkowe sprzątanie PO wczytaniu, ale PRZED wyliczeniem timestampów."""
    deps = getattr(env, "dependencies", None) or getattr(env, "_dependencies", None)
    if not deps:
        return
    root = Path(env.srcdir).resolve()
    removed, trimmed = 0, 0
    for docname, items in list(deps.items()):
        cleaned = []
        for dep in set(items):
            if not dep:
                removed += 1
                continue
            dep_n = dep.replace("\\", "/").lstrip("./")
            if any(dep_n == p or dep_n.startswith(p + "/") for p in GIT_DEPS_EXCLUDE):
                removed += 1
                continue
            p_abs = (root / dep_n).resolve()
            if p_abs.is_file():
                try:
                    cleaned.append(str(p_abs.relative_to(root)))
                except Exception:
                    cleaned.append(dep_n)
            else:
                removed += 1
        if len(cleaned) > GIT_DEPS_MAX:
            cleaned = sorted(cleaned)[:GIT_DEPS_MAX]
            trimmed += 1
        deps[docname] = sorted(cleaned)
    msg = f"[conf.py] deps sanitized: removed={removed}"
    if trimmed:
        msg += f", trimmed_docs={trimmed} (max={GIT_DEPS_MAX})"
    print(msg)

def _add_nav_link(app, config):
    opts = dict(config.html_theme_options or {})
    nav = list(opts.get("navbar_links", []))
    if not any(isinstance(x, dict) and x.get("url") in ("copilot/index.html","dokumentacja%20copilot/index.html") for x in nav):
        nav.append({"name": "Copilot Docs", "url": "copilot/index.html", "internal": True})
    opts["navbar_links"] = nav
    config.html_theme_options = opts

def setup(app):
    # 1) PRZED czytaniem źródeł — patch note_dependency (ważne: bardzo niski priorytet ⇒ wcześniej)
    app.connect("env-before-read-docs", _patch_env_dependency_filter, priority=0)
    # 2) PO wczytaniu — dodatkowe czyszczenie dependencies, ciągle PRZED pluginem (priority 0 < 500)
    app.connect("env-updated", _sanitize_dependencies, priority=0)
    # 3) link do Copilota w navbarze
    app.connect("config-inited", _add_nav_link, priority=200)
