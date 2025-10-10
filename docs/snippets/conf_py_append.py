# === PYDATA + rozszerzenia (do dopisania na końcu conf.py) ===

# Upewnij się, że lista extensions istnieje
try:
    extensions
except NameError:
    extensions = []

_exts = [
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
for _e in _exts:
    if _e not in extensions:
        extensions.append(_e)

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "logo": {"text": "OTClient v8 Dev"},
    "show_prev_next": True,
    "show_toc_level": 2,
    "navigation_depth": 3,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lukaszj321/otcv8-dev",
            "icon": "fa-brands fa-github",
        },
    ],
}

# Edycja stron i breadcrumbs
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# Pliki statyczne i CSS
if "html_static_path" not in globals():
    html_static_path = []
if "_static" not in html_static_path:
    html_static_path.append("_static")
html_css_files = (html_css_files if "html_css_files" in globals() else []) + ["custom.css"]

# MyST konfiguracja
myst_enable_extensions = list(set((globals().get("myst_enable_extensions") or []) + [
    "linkify", "colon_fence", "attrs", "deflist", "tasklist"
]))
myst_heading_anchors = 3

# Sitemap + OpenGraph
sitemap_url_scheme = "{link}"
ogp_site_url = "https://lukaszj321.github.io/otcv8-dev/"
ogp_image = "images/og/default-og.png"

# Favicons
favicons = [
    {"rel": "icon", "href": "favicon/favicon-32x32.png", "sizes": "32x32"},
    {"rel": "icon", "href": "favicon/favicon-16x16.png", "sizes": "16x16"},
    {"rel": "manifest", "href": "favicon/site.webmanifest"},
]

# Mermaid
mermaid_version = "10.9.1"

# Hoverxref
hoverxref_auto_ref = True
hoverxref_roles = ["doc"]

# Code autolink
codeautolink_autodoc_inject = False
