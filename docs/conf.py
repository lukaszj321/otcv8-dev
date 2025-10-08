# conf.py
import os
import sys
from datetime import datetime

# -- Podstawy projektu ---------------------------------------------------------
project = "OTCv8 — Dokumentacja"
author = "OTCv8"
copyright = f"{datetime.now():%Y}, {author}"

language = "pl"

# -- Rozszerzenia --------------------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
]

# anchor-y do nagłówków Markdown, rozszerzenia MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "attrs_block",
    "attrs_inline",
    "linkify",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 4

# autosectionlabel: prefiksuj ścieżką pliku, żeby uniknąć duplikatów
autosectionlabel_prefix_document = True

# -- Wejście / wykluczenia ----------------------------------------------------
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    # kopie zapasowe /md_backup/ — powodowały duplikaty etykiet
    "**/__md_backup_*/*",
    "docs/**/__md_backup_*/*",
]

# -- Motyw i HTML --------------------------------------------------------------
html_theme = "furo"
html_title = project
html_static_path = ["_static"]
html_css_files = ["custom.css"]  # opcjonalnie, jeśli masz

# Ustaw baseurl (wymagane m.in. dla sitemap)
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"

html_theme_options = {
    "navigation_with_keys": True,
    # możesz dodać kolory / logotyp później
}

# -- Sitemap -------------------------------------------------------------------
sitemap_url_scheme = "{link}"

# -- Ostrzeżenia do przytłumienia (opcjonalnie) --------------------------------
# Jeżeli wciąż łapiesz duplikaty odniesień z legacy-linków:
# suppress_warnings = ["ref.ref"]

# -- Drobiazgi -----------------------------------------------------------------
# Jeśli chcesz ładniejsze kopie kodu bez promptów:
copybutton_prompt_text = r">>> |\\$ |In \\[\\d\\]: |\\.\\.\\. "
copybutton_prompt_is_regexp = True
