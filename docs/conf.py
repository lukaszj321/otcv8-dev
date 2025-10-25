# ----------------------- HARDEN: MyST, diagrams, warnings -----------------------
import os, glob
from pathlib import Path

# 1) Rejestracja parsera MyST dla .md + autolabelki nagłówków
extensions = list(dict.fromkeys(globals().get("extensions", []) + [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
]))
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst",
}
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 6

# 2) MyST: nie próbuj robić cross-refów z linków MD (eliminuje myst.xref_missing)
myst_enable_extensions = list(dict.fromkeys(
    globals().get("myst_enable_extensions", []) + [
        "colon_fence", "deflist", "attrs_block", "attrs_inline",
        "linkify", "tasklist", "substitution",
    ]
))
myst_heading_anchors = 6
# kluczowe: traktuj wszystkie linki MD jako zwykłe URL-e, nie "xref"
myst_all_links_external = True

# 3) html_baseurl z ENV (fallback na Pages)
html_baseurl = os.environ.get("SPHINX_HTML_BASEURL", globals().get("html_baseurl", "https://lukaszj321.github.io/otcv8-dev"))

# 4) Skopiuj wszystkie katalogi "diagrams" do outputu (żeby ../diagrams/*.mmd były dostępne)
SRC_DIR = Path(__file__).parent
extra_paths = []
for d in glob.glob(str(SRC_DIR / "**/diagrams"), recursive=True):
    rel = os.path.relpath(d, SRC_DIR)
    if rel and not any(rel.startswith(p) for p in ("_build", "_static", "_templates")):
        extra_paths.append(rel)

html_extra_path = list(dict.fromkeys(globals().get("html_extra_path", []) + extra_paths))

# 5) Wycisz ostrzeżenia „undefined label” i „myst.xref_missing” – i tak nie są krytyczne
suppress_warnings = list(dict.fromkeys(
    globals().get("suppress_warnings", []) + [
        "ref.ref",
        "myst.xref_missing",
    ]
))

# 6) hoverxref – zdefiniuj typ dla :ref:, żeby nie pluł „unknown typ (ref)”
hoverxref_role_types = {
    "ref": "tooltip",
    "doc": "tooltip",
    **globals().get("hoverxref_role_types", {})
}

# 7) intersphinx – ustaw poprawne mapy (bez pustych `{}`)
extensions = list(dict.fromkeys(extensions + ["sphinx.ext.intersphinx"]))
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    **globals().get("intersphinx_mapping", {})
}

# 8) mermaid – wersja/render z ENV (zgodne z workflow)
mermaid_version = os.environ.get("SPHINX_MERMAID_VERSION", "10.9.1")
mermaid_output_format = os.environ.get("SPHINX_MERMAID_OUT", "raw")

# ----------------------- FIX: sphinx_last_updated_by_git & deps cleanup ----------
def _strip_bad_deps(app, env):
    """
    Zanim uruchomi się obcy handler 'env-updated' (np. z sphinx_last_updated_by_git),
    usuń z env.dependencies wpisy typu '.../diagrams' (same katalogi) oraz dziwne ścieżki
    bez rozszerzeń, które powodują 'unhandled files: {b"diagrams"}'.
    """
    try:
        deps = env.dependencies
    except Exception:
        return
    cleaned = {}
    for docname, paths in deps.items():
        keep = set()
        for p in paths:
            ps = p.decode("utf-8") if isinstance(p, (bytes, bytearray)) else str(p)
            # wywal katalogi "diagrams" i ogólnie gołe nazwy bez kropki (rozszerzenia)
            base = os.path.basename(ps.rstrip("/"))
            if base == "diagrams":
                continue
            if "." not in os.path.basename(ps):
                continue
            keep.add(ps)
        cleaned[docname] = keep
    env.dependencies = cleaned

def setup(app):
    # uruchom nasz cleanup PRZED innymi (niska wartość = wysoki priorytet wywołania)
    try:
        app.connect("env-updated", _strip_bad_deps, priority=0)
    except TypeError:
        # starsze Sphinx bez parametru priority
        app.connect("env-updated", _strip_bad_deps)

# ----------------------- THEME navbar (link do Copilot Docs) --------------------
try:
    extensions = list(dict.fromkeys(extensions + ["sphinx.ext.graphviz"]))
    html_theme_options = dict(globals().get("html_theme_options", {}) or {})
    navbar_links = list(html_theme_options.get("navbar_links", []))
    # nie duplikuj
    if not any((isinstance(x, dict) and x.get("url") == "dokumentacja%20copilot/index.html") for x in navbar_links):
        navbar_links.append({"name": "Copilot Docs", "url": "dokumentacja%20copilot/index.html", "internal": True})
    html_theme_options["navbar_links"] = navbar_links
except Exception:
    pass
# --------------------------------------------------------------------------------
