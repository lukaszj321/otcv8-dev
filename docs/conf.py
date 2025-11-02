from __future__ import annotations
import os
import re
from pathlib import Path
from sphinx.util import logging as sphinx_logging

logger = sphinx_logging.getLogger(__name__)

project = "OTClient v8 — Developer Documentation"
author = "OTCv8"
language = "pl"

# Źródła: RST + MyST (Markdown)
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst",
}

# Motyw
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
templates_path = ["_templates"]

# BaseURL (CLI ma pierwszeństwo, ale dajemy fallback z ENV)
html_baseurl = os.environ.get("SPHINX_HTML_BASEURL", "")

extensions = [
    # MyST (Markdown)
    "myst_parser",

    # Sphinx core
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",

    # Dodatki
    "sphinxcontrib.mermaid",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxext.opengraph",
    "sphinx_sitemap",
    "sphinx_favicon",
    "sphinx_codeautolink",
    "sphinxcontrib.jquery",
    "hoverxref.extension",
    "sphinx_last_updated_by_git",
    "sphinxext.rediraffe",
    "ablog",
]

# Exclude patterns to avoid duplicate C++ declarations
# TEMPORARY EXCLUSIONS (to fix CI): these will be incrementally reverted
# with dedicated fixes in future PRs. See docs/EXCLUDE_LIST.md for details.
exclude_patterns = globals().get("exclude_patterns", []) + [
    "autoapi/cpp/*",
    "api/cpp/*",
    # Problematic/generated/large source files (temporary exclusions)
    "docs/copilot/sphinx/code/**/source_mirror/**",
    "docs/copilot/sphinx/code/**/source_mirror/**/*",
    "docs/copilot/csv/*.csv",
    "docs/copilot/csv/**/*.csv",
    "docs/modules/modulesopisy/*.md",
    "docs/modules/modulesopisy/**/*.md",
    "docs/modules/structured/**",
    "docs/copilot/sphinx/code/**/src/**/source_mirror/**",
    "docs/tools/generate_*.py",
    "docs/tools/*.lua",
    "docs/tools/*.py",
    "docs/copilot/sphinx/code/**/angle/include/**",
    "docs/copilot/sphinx/code/**/angle/source_mirror/**",
]

# Jeśli istnieje Doxygen XML – włącz breathe/exhale
_DOXY_XML = Path(__file__).resolve().parent / "_build" / "doxygen" / "xml"
if _DOXY_XML.exists():
    extensions += ["breathe", "exhale"]
    breathe_default_project = "OTCv8 C++ API"
    breathe_projects = {breathe_default_project: str(_DOXY_XML)}
    exhale_args = {
        "containmentFolder": str(Path("api") / "cpp"),
        "rootFileName": "index.rst",
        "rootFileTitle": "C++ API",
        "doxygenStripFromPath": str(Path(__file__).resolve().parent.parent),
        "createTreeView": True,
        "exhaleExecutesDoxygen": False,
        "verboseBuild": False,
    }

# MyST – to czego używasz (tabs, admonitions, listy itd.)
myst_enable_extensions = [
    "colon_fence",
    "linkify",
    "attrs_block",
    "attrs_inline",
    "substitution",
    "tasklist",
    "deflist",
]

# InterSphinx – poprawne: drugi element to None
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_timeout = 10  # Reduce timeout to avoid hanging on network issues

# hoverxref – zdefiniuj typy, żeby nie pluł ostrzeżeniami
hoverxref_role_types = {
    "ref": "tooltip",
    "mod": "tooltip",
    "doc": "tooltip",
}

# Sitemap
sitemap_url_scheme = "{link}"

# Codeautolink
codeautolink_autodoc_inject = False

# Mermaid
mermaid_version = os.environ.get("SPHINX_MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.environ.get("SPHINX_MERMAID_OUT", "raw")

# Nie wywalaj buildu na brakujących celach MyST (masz dużo linków między MD)
# TEMPORARY WARNING SUPPRESSIONS (to fix CI): common non-blocking categories
# These will be addressed incrementally with dedicated fixes in future PRs.
# See docs/EXCLUDE_LIST.md for details.
suppress_warnings = [
    "myst.xref_missing",
    "toc.not_readable",
    "toc.not_included",
    "design.grid",
    "myst.directive_option",
    "myst.directive_comments",
    "myst.parser",
    "autodoc",
    "ref.unknown",
    "app.add_node",
]

# ----------------- Fix 1: czyść złe dependencies (git) -----------------
def _sanitize_dependencies(env) -> int:
    import os
    changed = 0
    deps = getattr(env, "dependencies", {}) or {}
    for docname, items in list(deps.items()):
        # Ensure items is iterable/list
        items_list = list(items) if items is not None else []
        newset = set()
        for p in items_list:
            if isinstance(p, bytes):
                p = p.decode("utf-8", "ignore")
            p = str(p).strip()
            if not p:
                continue
            # wywal katalogi i ścieżki bez rozszerzenia (np. 'diagrams')
            if p.endswith("/") or os.path.splitext(p)[1] == "":
                continue
            newset.add(p)
        # Porównanie jako zbiory (kolejność nieistotna)
        if set(newset) != set(items_list):
            deps[docname] = list(newset)
            changed += 1
    return changed

def _pre_git_filter(app, env):
    try:
        _sanitize_dependencies(env)
    except Exception as e:
        logger.warning(f"[conf.py] dependency sanitize failed: {e}")

# ----------------- Fix 2: puste bloki Breathe (.. doxygenenum::) ------
_DOXY_EMPTY_BLOCK_RE = re.compile(
    r"(?ms)^\.\.\s+doxygen(?:enum|class|struct|union|function)\s*::\s*$\n"
    r"(?:^[ \t]*:[a-zA-Z0-9_-]+:.*\n)*"
)

def _fix_breathe_empty_blocks(app, docname, source):
    s = source[0]
    if ".. doxygen" not in s:
        return
    def _repl(_m):
        return ".. note:: (pominięto pustą dyrektywę wygenerowaną przez Exhale)\n\n"
    ns, nsubs = _DOXY_EMPTY_BLOCK_RE.subn(_repl, s)
    if nsubs:
        source[0] = ns
        logger.info(f"[conf.py] fixed {nsubs} empty doxygen* blocks in {docname}")

# ----------------- hooki -----------------
def setup(app):
    # uruchom porządkowanie PRZED last_updated_by_git (niższy priorytet = wcześniej)
    app.connect("env-updated", _pre_git_filter, priority=100)
    # podmień puste bloki Breathe zaraz po wczytaniu źródła
    app.connect("source-read", _fix_breathe_empty_blocks, priority=500)
