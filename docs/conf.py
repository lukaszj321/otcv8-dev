# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x, PyData >=0.16) ---------
from __future__ import annotations

import os
import sys
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

# ── Helpers ───────────────────────────────────────────────────────────────────
def _try_load(ext: str) -> bool:
    """Append an extension if importable; log result."""
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
        return True
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")
        return False

# ── Extensions (core) ─────────────────────────────────────────────────────────
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

for ext in extensions:
    print(f"[conf.py] ✓ loaded: {ext}")

# ── Extensions (optional / nice-to-have) ──────────────────────────────────────
# Te będą załadowane, jeśli są zainstalowane (nie wywalą buildu)
for ext in [
    "breathe",
    "exhale",
    "ablog",
    "sphinx_design",
    "sphinxcontrib.mermaid",
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
]:
    _try_load(ext)

# AutoAPI tylko na życzenie (np. ustaw w CI: AUTOAPI=1 i autoapi_dirs)
if os.environ.get("AUTOAPI", "0") == "1":
    if _try_load("autoapi.extension"):
        # Minimalna konfiguracja — dopasuj do repo
        autoapi_type = os.environ.get("AUTOAPI_TYPE", "python")  # python/cpp/etc.
        autoapi_dirs = [
            p for p in os.environ.get("AUTOAPI_DIRS", "").split(":") if p.strip()
        ] or []
        if not autoapi_dirs:
            print("[conf.py] ! AUTOAPI włączone, ale brak AUTOAPI_DIRS — wyłączam.")
            extensions.remove("autoapi.extension")

# Nie ładuj myst_parser obok myst_nb
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

# Ważne: wyłącz automatyczny HR dla przypisów (eliminuje część “transition”)
myst_footnote_transition = False

# Unikatowe kotwice per dokument
autosectionlabel_prefix_document = True

# ── Intersphinx (naprawione tuple) ────────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# ── Breathe / Exhale (C++) — tylko jeśli mamy Doxygen XML ────────────────────
if "breathe" in extensions and "exhale" in extensions:
    if DOXY_XML.exists() and (DOXY_XML / "index.xml").exists():
        breathe_projects = {"OTCv8 C++ API": str(DOXY_XML)}
        breathe_default_project = "OTCv8 C++ API"
        exhale_args = {
            "containmentFolder": "autoapi/cpp",
            "rootFileName": "index.rst",
            "rootFileTitle": "OTCv8 C++ API",
            "createTreeView": True,
            "exhaleExecutesDoxygen": False,         # Doxygen uruchamiany w CI
            "doxygenStripFromPath": str(REPO_ROOT),
            # "verboseBuild": True,
        }
        primary_domain = "cpp"
        highlight_language = "cpp"
    else:
        print("[conf.py] ! Brak Doxygen XML → pomijam Breathe/Exhale")
        extensions = [e for e in extensions if e not in {"breathe", "exhale"}]

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
    import pydata_sphinx_theme  # noqa: F401
    html_theme = "pydata_sphinx_theme"
    print("[conf.py] ✓ using theme: pydata_sphinx_theme")
except Exception:
    html_theme = "alabaster"
    print("[conf.py] ✗ pydata_sphinx_theme not found — using 'alabaster'")

html_title = "OTClient v8 — Authoring & API"

# CSS (ładuj tylko jeśli pliki istnieją; kolejność → nadpisywanie)
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

# JS (ładuj tylko jeśli pliki istnieją)
html_js_files: list[str] = []
def _add_js(rel: str) -> None:
    if (STATIC_DIR / rel).exists():
        html_js_files.append(rel)

for rel in [
    "custom.js",
    "css/canonical-fix.js",
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

html_baseurl = os.environ.get(
    "HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/"
)
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# ── Mermaid (client-side) ─────────────────────────────────────────────────────
mermaid_version = os.environ.get("MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.environ.get("MERMAID_OUTPUT", "raw")
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# ── OpenGraph / SEO ───────────────────────────────────────────────────────────
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"

# ── Copybutton ────────────────────────────────────────────────────────────────
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# ── Sitemap / Hoverxref (jeśli są) ────────────────────────────────────────────
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

# ── Linkcheck (jeśli użyjesz) ────────────────────────────────────────────────
linkcheck_ignore = [r"http://localhost:\d+/", r"https://placehold\.co/.*", r".*\.local"]
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── Opcjonalny snippet „Copilot” — bezpieczne środowisko ─────────────────────
_copilot_snippet = DOCS_DIR / "copilot" / "sphinx" / "conf_copilot_snippet.py"
if _copilot_snippet.exists():
    try:
        _ctx = {"extensions": extensions, "html_theme_options": html_theme_options}
        exec(_copilot_snippet.read_text(encoding="utf-8"), _ctx, _ctx)
        # przejmij ewentualne zmiany ze snippeta
        extensions = _ctx.get("extensions", extensions)
        html_theme_options = _ctx.get("html_theme_options", html_theme_options)
        print("[conf.py] ✓ Copilot snippet loaded")
    except Exception as e:
        print(f"[conf.py] ✗ Copilot snippet error: {e}")

# ── Tymczasowy detektor „transition” (poziome kreski) ────────────────────────
# Zgłosi WARNING dla każdej linii `---`/`***`/`___` i ERROR gdy plik kończy się taką linią.
import re
_HR_RE = re.compile(r'^\s*(?:-{3,}|\*{3,}|_{3,})\s*$')

def _scan_hr_nodes(app, docname, source):
    text = source[0]
    lines = text.splitlines()
    bad_end = bool(lines and _HR_RE.match(lines[-1]))
    for i, line in enumerate(lines, 1):
        if _HR_RE.match(line):
            app.logger.warning(f"[HR] {docname}:{i}: pozioma linia (możliwy 'transition')")
    if bad_end:
        # ERROR – zatrzyma build. Usuń poziomą linię na końcu pliku.
        from docutils.utils import SystemMessage
        raise SystemMessage(f"[HR-END] {docname}: plik KOŃCZY się poziomą linią — usuń ją.")

# ── Minimal setup hook ────────────────────────────────────────────────────────
def setup(app):  # noqa: D401
    """Lightweight Sphinx setup hook."""
    app.connect("source-read", _scan_hr_nodes)
    return
