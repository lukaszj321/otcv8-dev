# -- Podstawy --------------------------------------------------------------
project = "OTCv8"
root_doc = "index"  # główny plik (ten z canvasa)

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

myst_enable_extensions = ["colon_fence", "linkify", "attrs_block", "deflist", "tasklist"]

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
pygments_dark_style = "native"

# -- Brand / meta ----------------------------------------------------------
html_theme_options = {
    "sidebar_hide_name": True,
    "announcement": "📣 Dev build dokumentacji (auto z CI).",
}

html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
sitemap_url_scheme = "{link}"

ogp_site_url = html_baseurl
ogp_image = "_static/cover.png"

favicons = [{"rel": "icon", "href": "favicon.svg"}]

# -- Ważne: wykluczenia duplikatów/backupów -------------------------------
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/__md_backup_*",         # wycina wszystkie backupy
]
