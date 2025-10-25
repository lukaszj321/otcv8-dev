# -- Copilot addon for Sphinx --------------------------------------------------
# Ten plik może dopinać własne linki w navbarze itd., ale NIE psuje intersphinx.

# Jeśli ustawiasz intersphinx tutaj, używaj None zamiast {}:
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# Przykład: dopięcie linku do navbaru PyData
html_theme_options = {
    "navbar_links": [
        {"name": "Copilot Docs", "url": "dokumentacja%20copilot/index.html", "internal": True}
    ]
}

# Upewnij się, że graphviz będzie dostępny (bez rejestrowania żadnych eventów)
extensions = ["sphinx.ext.graphviz"]
