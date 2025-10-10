import os, sys
from datetime import datetime

project = "OTClient v8"
author = "OTCv8"
copyright = f"{datetime.now():%Y}, OTCv8"
release = "0.1"

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

myst_enable_extensions = [
    "deflist",
    "fieldlist",
    "colon_fence",
    "attrs_block",
    "attrs_inline",
    "substitution",
    "tasklist",
    "linkify",
]

# Theme
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_prev_next": True,
    "navigation_depth": 3,
    "collapse_navigation": False,
}
html_static_path = ["_static"]
templates_path = ["_templates"]

# Copy raw data/ into site for linking (images, fonts, sounds, etc.)
# Assumes repository layout: docs/conf.py and sibling ../data
html_extra_path = ["../data"]

# Sitemap (GitHub Pages URL - adjust if using custom domain)
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

# OpenGraph
ogp_site_url = html_baseurl
ogp_image = "https://lukaszj321.github.io/otcv8-dev/_static/og-image.png"
ogp_description_length = 160

# Copybutton: ignore prompts
copybutton_prompt_text = r">>> |\$ "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"

# Hoverxref
hoverxref_auto_ref = True

# Code autolink
codeautolink_autodoc_inject = False
codeautolink_concat_default = True

# MyST linkify
myst_linkify_fuzzy_links = True

# Mermaid config
mermaid_version = "10.9.1"
