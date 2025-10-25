# -- Copilot addon for Sphinx --------------------------------------------------
# Nie rejestrujemy żadnych eventów i nie psujemy intersphinx.

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

html_theme_options = {
    "navbar_links": [
        {"name": "Copilot Docs", "url": "dokumentacja%20copilot/index.html", "internal": True}
    ]
}

extensions = ["sphinx.ext.graphviz"]
