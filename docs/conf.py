
project = "OTCv8 Dev"
author = "lukaszj321"
copyright = "2025, " + author
language = "pl"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
    "linkify_it_py",
    "sphinxext.opengraph",
    "sphinxcontrib.mermaid",
    "sphinx_codeautolink",
    "hoverxref.extension",
]

myst_heading_anchors = 4
myst_enable_extensions = [
    "linkify",
    "colon_fence",
    "attrs_block",
    "attrs_inline",
    "deflist",
    "substitution",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "build", "Thumbs.db", ".DS_Store"]

html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.svg"
html_extra_path = ["../data"]
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

html_theme_options = {
    "show_nav_level": 2,
    "navigation_depth": 4,
    "collapse_navigation": True,
    "icon_links": [
        {"name": "GitHub", "url": "https://github.com/lukaszj321/otcv8-dev", "icon": "fa-brands fa-github"},
    ],
    "navbar_align": "content",
    "secondary_sidebar_items": ["page-toc", "sourcelink"],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "footer_end": ["theme-version"],
    "announcement": "⚙️ Przebudowa dokumentacji — część sekcji to placeholdery.",
}

html_css_files = ["custom.css"]

ogp_site_url = html_baseurl
ogp_image = "_static/og-image.png"
ogp_description_length = 200

codeautolink_autodoc_inject = False
hoverxref_auto_ref = True
hoverxref_intersphinx = []

copybutton_prompt_is_regexp = True
copybutton_prompt_text = r"^\$ |^>>> |^\.\.\. "

mermaid_version = "10.9.1"
