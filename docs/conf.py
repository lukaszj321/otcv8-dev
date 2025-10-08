# -- Podstawy ---------------------------------------------------------------
project = "OTCv8"
language = "pl"
html_search_language = "pl"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinxcontrib.mermaid",
    "sphinx_codeautolink",
]

# MyST/Markdown
source_suffix = [".md", ".rst"]
myst_enable_extensions = [
    "colon_fence", "linkify", "attrs_block", "deflist", "tasklist"
]
# jeśli masz pliki zaczynające się od `---` (front matter / pozioma linia)
myst_front_matter_enable = True
myst_heading_anchors = 3

# Wyklucz kopie/backupy itp.
exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store",
    "**/__md_backup_*", "**/_drafts/*"
]

# -- Motyw / statyki --------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
pygments_dark_style = "native"

html_theme_options = {
    "sidebar_hide_name": True,
    "announcement": "📣 Dev build dokumentacji (auto z CI).",
}

# Sitemap / OpenGraph (dopasuj do swojej strony)
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
ogp_site_url = html_baseurl
ogp_image = "https://lukaszj321.github.io/otcv8-dev/_static/cover.png"

# Favicons (wrzuć swoje do docs/_static/)
favicons = [{"rel": "icon", "href": "favicon.svg"}]
