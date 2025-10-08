# -- Podstawy ---------------------------------------------------------------
project = "OTCv8"
author = "OTCv8"
language = "pl"

# Sphinx 7+: jawnie ustaw root
root_doc = "index"
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}

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

# MyST + front matter (naprawia 'Document may not begin/end with a transition')
myst_enable_extensions = [
    "front_matter",
    "colon_fence",
    "linkify",
    "attrs_block",
    "deflist",
    "tasklist",
]
myst_heading_anchors = 3  # automatyczne anchor linki H1-H3

# Wytnij backupy i buildy (usuwa duplikaty labeli)
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/__md_backup_*",
]

# -- HTML / Furo ------------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
pygments_dark_style = "native"

html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "img/logo-light.svg",  # jeśli nie masz – usuń te dwie linie
    "dark_logo": "img/logo-dark.svg",
    "announcement": "📣 Dev build dokumentacji (CI).",
}

# -- Linki / sitemap / OG ---------------------------------------------------
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
sitemap_url_scheme = "{link}"  # poprawne URL-e dla dirhtml

ogp_site_url = html_baseurl
ogp_image = html_baseurl + "_static/cover.png"

# favicon (wrzuć plik do docs/_static/)
favicons = [{"rel": "icon", "href": "favicon.svg"}]

# -- Mermaid ---------------------------------------------------------------
mermaid_version = "10.9.1"
