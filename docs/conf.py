# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 8.x, PyData) ----------------
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

# ── Helpers ───────────────────────────────────────────────────────────────────
def _try_load(ext: str) -> bool:
    try:
        import_module(ext)
        print(f"[conf.py] ✓ loaded: {ext}")
        return True
    except Exception as e:
        print(f"[conf.py] ✗ missing: {ext} ({e})")
        return False

# ── Extensions (core) ─────────────────────────────────────────────────────────
extensions = []
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
    if _try_load(ext):
        extensions.append(ext)

# ── Extensions (optional, bezpieczne) ─────────────────────────────────────────
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
    # "autoapi.extension",  # celowo wyłączone: wymaga autoapi_dirs
]:
    if _try_load(ext):
        extensions.append(ext)

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
autosectionlabel_prefix_document = True

# ── Intersphinx (stabilny, poprawny) ──────────────────────────────────────────
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# ── Breathe / Exhale (C++) ────────────────────────────────────────────────────
# Włącz tylko jeżeli jest Doxygen XML (index.xml). Inaczej wyłącz bez kraksy.
if (DOXY_XML / "index.xml").exists():
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
else:
    for _ext in ("exhale", "breathe"):
        if _ext in extensions:
            extensions.remove(_ext)
            print(f"[conf.py] ! disabling {_ext}: missing {DOXY_XML/'index.xml'}")

# ── BibTeX (włącz tylko, jeśli są .bib) ───────────────────────────────────────
if "sphinxcontrib.bibtex" in extensions:
    _bibfiles = [str(p.relative_to(DOCS_DIR)) for p in DOCS_DIR.rglob("*.bib")]
    if _bibfiles:
        bibtex_bibfiles = _bibfiles
        # przykładowe style (opcjonalnie):
        # bibtex_default_style = "unsrt"
        # bibtex_reference_style = "label"
        print(f"[conf.py] ✓ bibtex enabled, files: {bibtex_bibfiles}")
    else:
        extensions.remove("sphinxcontrib.bibtex")
        print("[conf.py] ! no .bib files — disabling sphinxcontrib.bibtex")

# ── Custom lexers (ciche fallbacki) ───────────────────────────────────────────
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

html_title = "OTClient v8 — Authoring & API"

# CSS/JS ładowane tylko jeśli istnieją (kolejność: późniejsze nadpisują wcześniejsze)
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

html_baseurl = os.environ.get("HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/")
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

# ── Sitemap / Hoverxref ───────────────────────────────────────────────────────
sitemap_url_scheme = "{link}"
hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"

# ── Favicons ──────────────────────────────────────────────────────────────────
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# ── Warnings / Linkcheck ─────────────────────────────────────────────────────
suppress_warnings = ["myst.header", "myst.nb.render"]
linkcheck_ignore = [r'http://localhost:\d+/', r'https://placehold\.co/.*', r'.*\.local']
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# ── (opcjonalnie) Copilot snippet — ładowany po zdefiniowaniu opcji ──────────
_copilot_snippet = DOCS_DIR / "copilot" / "sphinx" / "conf_copilot_snippet.py"
if _copilot_snippet.exists():
    try:
        # dajemy mu dostęp do globals(), żeby widział extensions/html_theme_options itd.
        exec(_copilot_snippet.read_text(encoding="utf-8"), globals(), globals())
        print(f"[conf.py] ✓ Copilot snippet loaded")
    except Exception as e:
        print(f"[conf.py] ✗ Copilot snippet error: {e}")

# --- Copilot Docs integration (robust) ---------------------------------------
# 1) dopnij potrzebne rozszerzenia (bez duplikatów)
if "sphinx.ext.graphviz" not in extensions:
    extensions.append("sphinx.ext.graphviz")

# 2) bezpieczna modyfikacja opcji motywu (PyData)
html_theme_options = dict(globals().get("html_theme_options", {}) or {})
_navbar_links = list(html_theme_options.get("navbar_links", []))
# Użyj _zdekodowanej_ ścieżki bez spacji/encodowania:
_copilot_url = "copilot/index.html"
if not any((isinstance(x, dict) and x.get("url") == _copilot_url) for x in _navbar_links):
    _navbar_links.append({"name": "Copilot Docs", "url": _copilot_url, "internal": True})
html_theme_options["navbar_links"] = _navbar_links
globals()["html_theme_options"] = html_theme_options  # zapisz z powrotem

# 3) Zgłaszanie *tylko śledzonych* plików z docs/copilot/diagrams jako zależności
from pathlib import Path
import subprocess

COPILOT_DIR = Path(__file__).parent / "copilot"
COPILOT_DIAGRAMS = COPILOT_DIR / "diagrams"
DOCS_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_DIR.parent.resolve()

# rozszerzenia plików, które mają wpływać na „last updated”
_DIAGRAM_GLOBS = ("*.svg", "*.png", "*.jpg", "*.jpeg", "*.gif", "*.webp",
                  "*.pdf", "*.mmd", "*.mermaid", "*.gv", "*.dot", "*.drawio")

def _git_tracked_under(path: Path) -> list[Path]:
    """
    Zwraca listę plików śledzonych przez Git pod podanym katalogiem.
    Gdy git nieosiągalny (np. lokalny build z ZIPa), wraca do zwykłego rglob,
    ale i tak filtruje tylko pliki (żadnych katalogów).
    """
    try:
        res = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "ls-files", "-z", str(path)],
            check=True, capture_output=True
        )
        raw = res.stdout.split(b"\x00")
        files = []
        for b in raw:
            if not b:
                continue
            p = (REPO_ROOT / b.decode("utf-8")).resolve()
            if p.is_file():
                files.append(p)
        return files
    except Exception as e:
        print(f"[conf.py] (warn) git ls-files failed: {e}")
        # fallback – bierzemy tylko istniejące pliki
        return [p for pat in _DIAGRAM_GLOBS for p in path.rglob(pat) if p.is_file()]

def _note_copilot_diagram_deps(app):
    """Zgłasza pliki z copilot/diagrams jako dependencies (tylko śledzone przez Git)."""
    if not COPILOT_DIAGRAMS.exists():
        return
    tracked = _git_tracked_under(COPILOT_DIAGRAMS)

    # dodatkowe filtrowanie po wzorcach, żeby nie wrzucać śmieci
    allow = set()
    suffixes = {ext.lower().lstrip("*") for ext in _DIAGRAM_GLOBS}
    for p in tracked:
        if p.suffix.lower() in suffixes:
            allow.add(p)

    for p in sorted(allow):
        try:
            rel_to_docs = p.relative_to(DOCS_DIR)
        except ValueError:
            # jeżeli plik jest poza docs/, Sphinx oczekuje ścieżki względnej względem źródeł
            # pomijamy takie pliki – i tak nie wpływają na stronę „copilot”
            continue
        # najważniejsze: *plik*, nie katalog
        app.env.note_dependency(str(rel_to_docs))

def setup(app):
    # zarejestruj callback wcześnie, zanim „sphinx_last_updated_by_git” policzy czasy
    app.connect("env-before-read-docs", lambda app, env, docnames: _note_copilot_diagram_deps(app))
    return
# --- end Copilot Docs integration --------------------------------------------
