# --- podstawy ---
project = "otcv8-dev"
author = "otcv8-dev"
language = "pl"

# --- rozszerzenia ---
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
myst_heading_anchors = 3
source_suffix = {".md": "myst", ".rst": "restructuredtext"}

# --- HTML / Furo ---
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
pygments_dark_style = "native"

html_title = "OTCv8 — Dokumentacja"
html_theme_options = {
    "light_logo": "img/logo-light.svg",
    "dark_logo": "img/logo-dark.svg",
    "sidebar_hide_name": True,
    "announcement": "📣 Dev build dokumentacji (auto z CI).",
}

# --- sitemap / ogp / favicon ---
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
ogp_site_url = "https://lukaszj321.github.io/otcv8-dev/"
ogp_image = "https://lukaszj321.github.io/otcv8-dev/_static/cover.png"

favicons = [
    {"rel": "icon", "href": "favicon.svg"},
]
