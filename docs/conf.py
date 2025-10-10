# -- Podstawowa konfiguracja Sphinx ------------------------------------------
import os, sys

project = "OTClient v8"
author = "OTCv8 Team"
copyright = "2024, OTCv8"
release = "0.1"

# -- Rozszerzenia -------------------------------------------------------------
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

# MyST (Markdown w Sphinx)
myst_enable_extensions = [
    "attrs_block", "attrs_inline", "colon_fence", "deflist",
    "fieldlist", "linkify", "smartquotes", "substitution", "tasklist",
]
myst_heading_anchors = 4  # generuj linki do nagłówków H1..H4

# Bazowy URL (wymagany przez sitemap)
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

# -- Motyw i wygląd -----------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme_options = {
    "navigation_depth": 3,
    "show_nav_level": 2,
    "collapse_navigation": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lukaszj321/otcv8-dev",
            "icon": "fab fa-github",
        },
    ],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
}

# Copybutton (usuń prompt z kopiowanego kodu)
copybutton_prompt_text = r">>> |\$ |\(venv\)\$ "
copybutton_prompt_is_regexp = True

# Mermaid
mermaid_version = "10.9.0"

# HoverXRef (podpowiedzi po najechaniu)
hoverxref_auto_ref = True
hoverxref_intersphinx = []  # można dodać mapowania, jeśli będzie potrzeba

# OpenGraph
ogp_site_url = html_baseurl
ogp_image = "https://raw.githubusercontent.com/lukaszj321/otcv8-dev/master/docs/_static/og-image.png"

# Favicons — jeśli dodasz pliki do docs/_static, odkomentuj
# html_favicon = "_static/favicon.ico"
# favicons = [
#     {"rel": "icon", "href": "favicon.ico"},
# ]

# Sitemap
sitemap_url_scheme = "{link}"
