# -- OTClient v8 Dev Docs — Sphinx config (Sphinx 7.4.7, PyData 0.16.1) -----

import os
import json
from pathlib import Path
from importlib import import_module
from collections.abc import Mapping, Sequence

# -- Project -------------------------------------------------------------------
project = "OTClient v8 — Developer Documentation"
author = "OTClient v8 contributors"
language = "pl"

# -- Paths ---------------------------------------------------------------------
DOCS_DIR = Path(__file__).parent.resolve()
STATIC_DIR = DOCS_DIR / "_static"
TEMPLATES_DIR = DOCS_DIR / "_templates"

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

# -- Extensions ----------------------------------------------------------------
# Core extensions - always loaded
extensions = [
    "myst_nb",                      # MyST + notebooki (wykonanie wyłączone poniżej)
    "sphinx.ext.autosectionlabel",  # zamiast pip-owego "sphinx-autosectionlabel"
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",          # Graphviz diagram support
]

# Critical extensions for Mermaid rendering - try to load, fail gracefully
_critical_exts = [
    "sphinxcontrib.mermaid",  # REQUIRED for Mermaid diagram rendering
    "sphinx_design",          # REQUIRED for grid/card directives
]

for ext in _critical_exts:
    try:
        import_module(ext)
        extensions.append(ext)
        print(f"[conf.py] ✓ Critical extension loaded: {ext}")
    except Exception as e:
        print(f"[conf.py] ✗ CRITICAL extension failed to load: {ext} ({e})")

# Optional extensions — doładuj tylko jeśli są zainstalowane w CI
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

# Bezpiecznik gdyby ktoś przez przypadek dodał myst_parser obok myst_nb
if "myst_nb" in extensions and "myst_parser" in extensions:
    extensions.remove("myst_parser")

# -- MyST / Notebooks ----------------------------------------------------------
nb_execution_mode = "off"          # nie wykonujemy komórek w CI
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

# Treat certain fence types as directives (allows ```mermaid to be treated as {mermaid} directive)
# myst-nb requires list/tuple/set format (not dict)
myst_fence_as_directive = ["mermaid"]

# Labelowanie nagłówków bez kolizji
autosectionlabel_prefix_document = True

# -- HTML / Theme --------------------------------------------------------------
# Jeśli pydata-sphinx-theme nie jest zainstalowany, fallback do alabaster
try:
    import pydata_sphinx_theme  # noqa: F401
    html_theme = "pydata_sphinx_theme"
except Exception:
    print("[conf.py] pydata-sphinx-theme not available — falling back to 'alabaster'")
    html_theme = "alabaster"

html_title = "OTClient v8 — Authoring & API"
html_css_files = []
if (STATIC_DIR / "tables-premium.css").exists():
    html_css_files.append("tables-premium.css")

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
        }
    ],
}

# Publiczny URL dla sitemap/opengraph (zmień jeśli masz inny branch/URL)
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",  # zmień na "main" jeśli używasz main
    "doc_path": "docs",
}

# -- Mermaid (sphinxcontrib-mermaid) -------------------------------------------
mermaid_version = "10.9.0"
# CRITICAL: Use SVG format for server-side rendering (better for CI/Pages)
# This generates actual SVG elements that don't require client-side JS
mermaid_output_format = "svg"
mermaid_init_js = "mermaid.initialize({startOnLoad:true, theme:'dark'});"

# -- OpenGraph / SEO -----------------------------------------------------------
ogp_site_url = html_baseurl
ogp_site_name = "OTClient v8 Dev Docs"
# ogp_image = html_baseurl + "_static/og.png"

# -- Copybutton ----------------------------------------------------------------
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_only_copy_prompt_lines = False

# -- Hoverxref -----------------------------------------------------------------
# (działa tylko jeśli zainstalowane; w przeciwnym razie zostanie pominięte powyżej)
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

# -- Linkcheck / Quality Control -----------------------------------------------
# Configuration for sphinx-build -b linkcheck
linkcheck_ignore = [
    r'http://localhost:\d+/',
    r'https://placehold\.co/.*',
    r'.*\.local',
]
linkcheck_timeout = 10
linkcheck_retries = 2
linkcheck_workers = 5

# Nitpicky mode (optional, can be enabled with -n flag)
# nitpicky = True
# nitpick_ignore = []

# -- Copilot Docs integration --------------------------------------------------
# Execute the snippet to integrate copilot section
_copilot_snippet = DOCS_DIR / "copilot/sphinx/conf_copilot_snippet.py"
if _copilot_snippet.exists():
    try:
        exec(open(_copilot_snippet, "r", encoding="utf-8").read())
        print(f"[conf.py] ✓ Copilot Docs snippet loaded from: {_copilot_snippet.relative_to(DOCS_DIR)}")
    except Exception as e:
        print(f"[conf.py] ✗ Error loading Copilot Docs snippet: {e}")

# -- Build hooks ---------------------------------------------------------------
def _json_safe(obj):
    """Convert object to JSON-serializable form"""
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
    """Setup hook to dump effective Sphinx configuration for QA"""
    
    def dump_sphinx_env(app, exception):
        """Dump effective Sphinx environment after build"""
        if exception is not None:
            return
        
        try:
            qa_dir = Path(app.srcdir) / "authoring" / "qa"
            qa_dir.mkdir(parents=True, exist_ok=True)
            
            # Convert extensions to list safely
            extensions_list = []
            if hasattr(app, 'extensions'):
                try:
                    extensions_list = list(app.extensions.keys())
                except Exception:
                    extensions_list = list(app.config.extensions) if hasattr(app.config, 'extensions') else []
            elif hasattr(app.config, 'extensions'):
                extensions_list = list(app.config.extensions)
            
            env_data = {
                "extensions": extensions_list,
                "myst_enable_extensions": list(app.config.myst_enable_extensions) if hasattr(app.config, 'myst_enable_extensions') else [],
                "myst_fence_as_directive": list(app.config.myst_fence_as_directive) if hasattr(app.config, 'myst_fence_as_directive') else [],
                "mermaid_output_format": getattr(app.config, 'mermaid_output_format', 'unknown'),
                "mermaid_version": getattr(app.config, 'mermaid_version', 'unknown'),
                "html_theme": getattr(app.config, 'html_theme', 'unknown'),
            }
            
            # Check if mermaid directive is registered
            if hasattr(app.registry, 'directives'):
                env_data["mermaid_directive_registered"] = 'mermaid' in app.registry.directives
            
            # Get package versions
            try:
                import sphinxcontrib.mermaid
                env_data["sphinxcontrib_mermaid_version"] = getattr(sphinxcontrib.mermaid, '__version__', 'unknown')
            except Exception:
                env_data["sphinxcontrib_mermaid_version"] = "not installed"
            
            try:
                import myst_nb
                env_data["myst_nb_version"] = getattr(myst_nb, '__version__', 'unknown')
            except Exception:
                env_data["myst_nb_version"] = "not installed"
            
            try:
                import sphinx_design
                env_data["sphinx_design_version"] = getattr(sphinx_design, '__version__', 'unknown')
            except Exception:
                env_data["sphinx_design_version"] = "not installed"
            
            # Use _json_safe to ensure all data is serializable
            safe_data = _json_safe(env_data)
            
            output_file = qa_dir / "sphinx_env.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(safe_data, f, indent=2, sort_keys=True)
            
            print(f"\n[conf.py] ✓ Sphinx environment dumped to: {output_file.relative_to(app.srcdir)}")
            
        except Exception as e:
            # Don't interrupt the build - save diagnostics and continue
            try:
                error_file = Path(app.outdir) / "_sphinx_env_error.txt"
                with open(error_file, 'w', encoding='utf-8') as f:
                    f.write(f"{type(e).__name__}: {e}\n")
                print(f"\n[conf.py] ✗ Error dumping Sphinx environment: {e}")
            except Exception:
                pass
    
    # Connect to build-finished event
    app.connect('build-finished', dump_sphinx_env)
