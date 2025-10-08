# -- Podstawy ---------------------------------------------------------------
project = "OTCv8"
author = "OTCv8 Dev"
language = "pl"

# Od Sphinx 7 używamy root_doc zamiast master_doc
root_doc = "index"

# Wymuś traktowanie .md jako MyST Markdown
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

# -- Rozszerzenia -----------------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinxcontrib.mermaid",
    "sphinx_codeautolink",
    "hoverxref.extension",
]

myst_enable_extensions = ["colon_fence", "linkify", "attrs_block", "deflist", "tasklist"]
# kotwice do nagłówków H1–H3 (czytelne #anchor w linkach)
myst_heading_anchors = 3
myst_url_schemes = ("http", "https", "mailto")

# -- Motyw / HTML -----------------------------------------------------------
html_theme = "furo"
html_title = "OTCv8 – Dokumentacja"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "announcement": "📣 Dev build dokumentacji (auto z CI).",
}

# Absolutna baza dla linków kanonicznych / sitemap (GH Pages)
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

# OpenGraph
ogp_site_url = html_baseurl
# (opcjonalnie) ogp_image = html_baseurl + "_static/cover.png"

# Favikony (wrzuć plik do docs/_static lub usuń poniższą linijkę)
favicons = [{"rel": "icon", "href": "favicon.svg"}]

# -- Sitemap ----------------------------------------------------------------
sitemap_url_scheme = "{link}"

# -- Inne -------------------------------------------------------------------
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store",
    "**/__md_backup*/*", "**/__md_backup*",
]

# copybutton – usuwa prompt z kopiowanych bloków
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\$ "

# Mermaid (wersja zgodna z wtyczką)
mermaid_version = "10.9.1"

# codeautolink – niech składa długie bloki
codeautolink_concat_default = True
