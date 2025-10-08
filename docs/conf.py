# -- Podstawy ---------------------------------------------------------------
import os
import sys
sys.path.append(os.path.abspath("."))

project = "otcv8-dev"
author = "otcv8-dev"
language = "pl"
# Sphinx 7 domyślnie ma master_doc='index', więc nie trzeba ustawiać.

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
    # "sphinxext.rediraffe",  # włącz jak dodasz redirekcje (patrz uwagi niżej)
]

myst_enable_extensions = ["colon_fence", "linkify", "attrs_block", "deflist", "tasklist"]
# (opcjonalnie: kotwice H1–H3)
myst_heading_anchors = 3

# -- Wejście/wyjście --------------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst",
}

exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store",
    "**/__md_backup_*/*", "docs/**/__md_backup_*/*",
]

# -- Motyw / HTML -----------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
pygments_style = "friendly"
pygments_dark_style = "native"

html_title = "OTCv8 — Dokumentacja"
# Ścieżki logo są względem _static/
html_theme_options = {
    "light_logo": "img/logo-light.svg",
    "dark_logo": "img/logo-dark.svg",
    "sidebar_hide_name": True,
    "announcement": "📣 Dev build dokumentacji (auto z CI).",
}

# -- Sitemap (wymaga pełnego URL z trailing slash) --------------------------
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

# -- OpenGraph / Social cards -----------------------------------------------
ogp_site_url = "https://lukaszj321.github.io/otcv8-dev/"
ogp_image = "https://lukaszj321.github.io/otcv8-dev/_static/cover.png"

# -- Favicons (pliki w docs/_static/) ---------------------------------------
favicons = [
    {"rel": "icon", "href": "favicon.svg"},
    # możesz dodać kolejne rozmiary/aple-touch itp.
]

# -- Mermaid (opcjonalnie) --------------------------------------------------
# mermaid_version = "10.9.1"  # gdybyś chciał przypiąć wersję CDN

# -- Hoverxref (opcjonalne dopieszczanie) -----------------------------------
# Działa bez konfiguracji, ale możesz dodać:
hoverxref_auto_ref = True

# -- CodeAutoLink (opcjonalne dopieszczanie) --------------------------------
# Minimalnie działa „out of the box”; gdy chcesz doprecyzować języki:
codeautolink_concat_default = True
