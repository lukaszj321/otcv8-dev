
# -- Project info -----------------------------------------------------
project = "otcv8-dev"
author = "Project Authors"

# -- Helpers ----------------------------------------------------------
def _ext_if_available(name, import_name=None, predicate=True):
    if not predicate:
        return None
    try:
        __import__(import_name or name.replace("-", "_").replace(".", "_"))
        return name
    except Exception:
        return None

from pathlib import Path
import os

_HAS_DOXYGEN_XML = (Path("docs/_doxygen/xml").exists() or Path("_doxygen/xml").exists())
_HAS_AUTOAPI_SRC = Path("src").exists()

CSV_PREVIEW_ROWS = int(os.environ.get("CSV_PREVIEW_ROWS", "100"))
CSV_PREVIEW_MAX_COLUMNS = int(os.environ.get("CSV_PREVIEW_MAX_COLUMNS", "80"))

# -- General config ---------------------------------------------------
_base_extensions = [
    "myst_parser",
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinxcontrib.mermaid",
    "sphinx_codeautolink",
    "hoverxref.extension",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    _ext_if_available("autoapi.extension", import_name="autoapi", predicate=_HAS_AUTOAPI_SRC),
    _ext_if_available("breathe", predicate=_HAS_DOXYGEN_XML),
    _ext_if_available("exhale", predicate=_HAS_DOXYGEN_XML),
    _ext_if_available("sphinxcontrib.bibtex", import_name="sphinxcontrib.bibtex"),
    _ext_if_available("sphinxcontrib.luadomain", import_name="sphinxcontrib.luadomain"),
    _ext_if_available("sphinxext.rediraffe", import_name="sphinxext.rediraffe"),
    _ext_if_available("sphinx_last_updated_by_git", import_name="sphinx_last_updated_by_git"),
    _ext_if_available("jupyter_sphinx"),
    _ext_if_available("jupyterlite_sphinx"),
]
extensions = [e for e in _base_extensions if e]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- MyST / MyST-NB ---------------------------------------------------
myst_enable_extensions = [
    "colon_fence","attrs_block","attrs_inline","deflist","linkify","substitution",
    "tasklist","replacements","html_admonition","html_image",
]
myst_heading_anchors = 3
jupyter_execute_notebooks = "off"
nb_execution_mode = "off"
nb_render_image_options = {"align": "center"}

# -- AutoAPI ----------------------------------------------------------
if "autoapi.extension" in extensions:
    autoapi_type = "python"
    autoapi_dirs = ["src"]
    autoapi_add_toctree_entry = False
    autoapi_keep_files = False
    autoapi_generate_api_docs = True

# -- Breathe / Exhale -------------------------------------------------
if "breathe" in extensions:
    _xml = "docs/_doxygen/xml" if Path("docs/_doxygen/xml").exists() else "_doxygen/xml"
    breathe_projects = {"otcv8-dev": _xml}
    breathe_default_project = "otcv8-dev"

if "exhale" in extensions:
    exhale_args = {
        "containmentFolder": "./docs/api/cpp",
        "rootFileName": "index.rst",
        "rootFileTitle": "C++ API Reference",
        "doxygenStripFromPath": "..",
        "createTreeView": True,
    }

# -- BibTeX -----------------------------------------------------------
if "sphinxcontrib.bibtex" in extensions:
    bibtex_bibfiles = []

# -- Rediraffe --------------------------------------------------------
if "sphinxext.rediraffe" in extensions:
    rediraffe_branch = "master"
    rediraffe_redirects = {}

# -- Hoverxref --------------------------------------------------------
hoverxref_auto_ref = True
hoverxref_domains = ["py", "std"]
hoverxref_role_types = {
    "ref": "modal",
    "doc": "modal",
    "class": "tooltip",
    "func": "tooltip",
}

# -- Codeautolink -----------------------------------------------------
codeautolink_autodoc_inject = False
codeautolink_concat_default = True

# -- HTML output ------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom-dark-mermaid.css", "tables.css", "tables-premium.css"]

html_theme_options = {
    "navigation_depth": 4,
    "show_nav_level": 2,
    "collapse_navigation": False,
    "use_edit_page_button": False,
    "logo": {},
    "icon_links": [
        {"name": "GitHub","url": "https://github.com/lukaszj321/otcv8-dev","icon": "fa-brands fa-github"},
    ],
}

# -- Sitemap / OpenGraph ---------------------------------------------
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
sitemap_url_scheme = "{link}"
ogp_site_url = html_baseurl
ogp_image = "https://lukaszj321.github.io/otcv8-dev/_static/favicon.png"

# -- Autosectionlabel -------------------------------------------------
autosectionlabel_prefix_document = True

# -- Mermaid ----------------------------------------------------------
mermaid_version = "10.9.0"

# -- Intersphinx ------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", {}),
}

# -- Copybutton -------------------------------------------------------
copybutton_prompt_text = r">>> |\$ "
copybutton_prompt_is_regexp = True

# -- Figures ----------------------------------------------------------
numfig = True

# -- Warnings / Quality -----------------------------------------------
suppress_warnings = ["mystnb.unknown_mime_type"]
