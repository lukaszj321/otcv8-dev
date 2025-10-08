# -- Project ---------------------------------------------------------------
project = "OTCv8"
author = "OTCv8 Dev Team"
language = "pl"

# -- General ---------------------------------------------------------------
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
myst_heading_anchors = 3  # automatyczne anchor-y do H1..H3

templates_path = ["_templates"]
exclude_patterns = ["**/__md_backup_*/*", "_build"]

# -- HTML ------------------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
pygments_dark_style = "native"

html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "img/logo-light.svg",  # opcjonalnie, jeśli masz
    "dark_logo": "img/logo-dark.svg",    # opcjonalnie, jeśli masz
    "announcement": "📣 Dev build dokumentacji (auto z CI).",
}

# Ważne dla sitemap / kanonicznych
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

# OpenGraph (ładne karty w socialach) – ustaw jeśli masz grafikę
ogp_site_url = html_baseurl
ogp_image = html_baseurl + "_static/cover.png"

# Favikony (wrzuć plik do docs/_static/)
favicons = [{"rel": "icon", "href": "favicon.svg"}]

# Jeśli używasz buildera 'dirhtml' w CI (rekomendowane na GH Pages):
sitemap_url_scheme = "{link}/"
