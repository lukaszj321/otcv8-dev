# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 7/8, PyData >=0.16) ---------

import os
import json
from pathlib import Path
from importlib import import_module
from collections.abc import Mapping, Sequence

# -- Project -------------------------------------------------------------------
project = "OTClient v8 — Developer Documentation"
author = "Dildo"
language = "pl"

# -- Paths ---------------------------------------------------------------------
DOCS_DIR = Path(__file__).parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"
EXTRA_DIR = DOCS_DIR / "_extra"  # LDoc output lives here
DOXY_XML = DOCS_DIR / "_build" / "doxygen" / "xml"

templates_path = ["_templates"] if TEMPLATES_DIR.exists() else []
html_static_path = ["_static"] if STATIC_DIR.exists() else []
html_extra_path = ["_extra"] if EXTRA_DIR.exists() else []  # LDoc HTML

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    ".venv",
    "venv",
]

# -- Extensions ----------------------------------------------------------------
extensions = [
    "myst_nb",
    "sphinx.ext.autosectionlabel",  # auto-id dla nagłówków
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
]

# Krytyczne (ładowane warunkowo)
_critical_exts = [
    "sphinxcontrib.mermaid",  # Mermaid diagrams
    "sphinx_design",          # Grid/cards
    "breathe",                # C++ (Doxygen -> Sphinx)
]
for ext in _critical_exts:
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ Critical extension loaded: {ext}")
    except Exception as e:
        print(f"[conf.py] ✗ CRITICAL extension failed to load: {ext} ({e})")

# Opcjonalne (jeśli są zainstalowane)
_optional_exts = [
    "sphinx_copybutton",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "sphinxcontrib.jquery",
    "sphinx_hoverxref",
]
for ext in list(_optional_exts):
    try:
        import_module(ext)
        extensions.append(ext)
    except Exception:
        print(f"[conf.py] optional extension skipped: {ext}")

# Bezpiecznik: nie ładuj myst_parser razem z myst_nb
if "myst_nb" in extensions and "myst_parser" in extensions:
    extensions.remove("myst_parser")

# -- MyST / Notebooks ----------------------------------------------------------
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
myst_fence_as_directive = ["mermaid"]  # ```mermaid => {mermaid}

# Prefiksy sekcji (unikalne anchor-y)
autosectionlabel_prefix_document = True

# -- Breathe (C++ via Doxygen) -------------------------------------------------
breathe_projects = {}
breathe_default_project = None

DOXY_INDEX = DOXY_XML / "index.xml"
if DOXY_INDEX.exists():
    breathe_projects["OTCv8 C++ API"] = str(DOXY_XML)
    breathe_default_project = "OTCv8 C++ API"
    print(f"[conf.py] ✓ Doxygen XML detected: {DOXY_INDEX}")
else:
    # Gdy brak XML, wyłącz Breathe i pomiń stronę C++
    if "breathe" in extensions:
        extensions.remove("breathe")
    exclude_patterns += ["autoapi/cpp/**"]
    print(f"[conf.py] ⚠ Doxygen XML not found ({DOXY_INDEX}). "
          f"Disabling Breathe and excluding 'autoapi/cpp/**'.")

# -- Custom lexers for OTUI/OTMOD (silence warnings) ---------------------------
try:
    from sphinx.highlighting import lexers
    from pygments.lexers.data import YamlLexer, IniLexer
    lexers["otui"] = YamlLexer()   # zbliżona składnia
    lexers["otmod"] = IniLexer()
except Exception as e:
    print(f"[conf.py] (warn) custom lexers not set: {e}")

# -- HTML / Theme --------------------------------------------------------------
try:
    import pydata_sphinx_theme  # noqa
    html_theme = "pydata_sphinx_theme"
except Exception:
    print("[conf.py] pydata-sphinx-theme not available — falling back to 'alabaster'")
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"

# CSS (kolejność ma znaczenie – ostatnie nadpisują wcześniejsze)
html_css_files = []
def _add_css(path: str):
    if (STATIC_DIR / path).exists():
        html_css_files.append(path)

for _p in [
    "tables.css",
    "tables-premium.css",
    "custom-dark-mermaid.css",
    "css/custom.css",
    "css/layout.css",  # szerokości kolumn / responsywność
]:
    _add_css(_p)

# JS (inicjalizacja Mermaid po stronie klienta)
html_js_files = []
if (STATIC_DIR / "custom.js").exists():
    html_js_files.append("custom.js")

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

html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# -- Mermaid (kliencki RAW) ----------------------------------------------------
# Render w przeglądarce – brak Puppeteera/mmdc w CI
mermaid_version = "10.9.1"
mermaid_output_format = "raw"
mermaid_init_js = ""  # inicjalizacja wykonana w _static/custom.js

# -- OpenGraph / SEO -----------------------------------------------------------
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"

# -- Copybutton ----------------------------------------------------------------
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# -- Hoverxref -----------------------------------------------------------------
hoverxref_auto_ref = True
hoverxref_domains = ["std"]
hoverxref_default_type = "tooltip"

# -- Sitemap -------------------------------------------------------------------
sitemap_url_scheme = "{link}"

# -- CodeAutolink --------------------------------------------------------------
codeautolink_autodoc_inject = False
codeautolink_concat = True

# -- Favicon -------------------------------------------------------------------
favicons = []
if (STATIC_DIR / "favicon.ico").exists():
    favicons.append({"rel": "icon", "href": "favicon.ico"})

# -- Warnings / porządek -------------------------------------------------------
suppress_warnings = [
    "myst.header",
    "myst.nb.render",
]

# -- Todo ----------------------------------------------------------------------
todo_include_todos = False

# -- Linkcheck -----------------------------------------------------------------
linkcheck_ignore = [r'http://localhost:\d+/', r'https://placehold\.co/.*', r'.*\.local']
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# -- Copilot Docs integration --------------------------------------------------
_copilot_snippet = DOCS_DIR / "copilot" / "sphinx" / "conf_copilot_snippet.py"
if _copilot_snippet.exists():
    try:
        exec(open(_copilot_snippet, "r", encoding="utf-8").read())
        print(f"[conf.py] ✓ Copilot Docs snippet loaded from: {_copilot_snippet.relative_to(DOCS_DIR)}")
    except Exception as e:
        print(f"[conf.py] ✗ Error loading Copilot Docs snippet: {e}")

# -- QA dump -------------------------------------------------------------------
def _json_safe(obj):
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    if isinstance(obj, Mapping):
        return {str(k): _json_safe(v) for k, v in obj.items()}
    if isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray)):
        return [_json_safe(x) for x in obj]
    try:
        return [_json_safe(x) for x in list(obj)]
    except Exception:
        return repr(obj)

def setup(app):
    def dump_sphinx_env(app, exception):
        if exception is not None:
            return
        try:
            qa_dir = Path(app.srcdir) / "authoring" / "qa"
            qa_dir.mkdir(parents=True, exist_ok=True)

            # Bezpieczne pobranie listy rozszerzeń
            extensions_list = []
            try:
                if hasattr(app, "extensions"):
                    extensions_list = list(app.extensions.keys())
                elif hasattr(app.config, "extensions"):
                    extensions_list = list(getattr(app.config, "extensions", []))
            except Exception:
                extensions_list = list(getattr(app.config, "extensions", []))

            env_data = {
                "extensions": extensions_list,
                "myst_enable_extensions": list(getattr(app.config, "myst_enable_extensions", [])),
                "myst_fence_as_directive": list(getattr(app.config, "myst_fence_as_directive", [])),
                "mermaid_output_format": getattr(app.config, "mermaid_output_format", "unknown"),
                "mermaid_version": getattr(app.config, "mermaid_version", "unknown"),
                "html_theme": getattr(app.config, "html_theme", "unknown"),
                "breathe_projects": getattr(app.config, "breathe_projects", {}),
                "breathe_default_project": getattr(app.config, "breathe_default_project", None),
                "extra_dir_exists": EXTRA_DIR.exists(),
                "doxy_xml_exists": (DOXY_XML / "index.xml").exists(),
            }

            try:
                import sphinxcontrib.mermaid
                env_data["sphinxcontrib_mermaid_version"] = getattr(sphinxcontrib.mermaid, "__version__", "unknown")
            except Exception:
                env_data["sphinxcontrib_mermaid_version"] = "not installed"

            try:
                import myst_nb
                env_data["myst_nb_version"] = getattr(myst_nb, "__version__", "unknown")
            except Exception:
                env_data["myst_nb_version"] = "not installed"

            try:
                import sphinx_design
                env_data["sphinx_design_version"] = getattr(sphinx_design, "__version__", "unknown")
            except Exception:
                env_data["sphinx_design_version"] = "not installed"

            output_file = qa_dir / "sphinx_env.json"
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(_json_safe(env_data), f, indent=2, sort_keys=True)
            print(f"\n[conf.py] ✓ Sphinx environment dumped to: {output_file.relative_to(app.srcdir)}")
        except Exception as e:
            try:
                error_file = Path(app.outdir) / "_sphinx_env_error.txt"
                with open(error_file, "w", encoding="utf-8") as f:
                    f.write(f"{type(e).__name__}: {e}\n")
                print(f"\n[conf.py] ✗ Error dumping Sphinx environment: {e}")
            except Exception:
                pass
    app.connect("build-finished", dump_sphinx_env)
