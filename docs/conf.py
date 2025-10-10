project = "OTClientV8 Dev Docs"
author = "OTCV8 Team"
version = "0.1"
release = "0.1.0"
language = "pl"

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "attrs",
    "substitution",
    "tasklist",
    "fieldlist",
]
myst_heading_anchors = 3

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
    "sphinx": ("https://www.sphinx-doc.org/en/master", {}),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_logo = "_static/only-light/logo-light.svg"
html_favicon = "_static/only-light/logo-light.svg"

html_theme_options = {
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lukaszj321/otcv8-dev",
            "icon": "fab fa-github",
            "type": "fontawesome",
        },
    ],
    "show_prev_next": True,
    "header_links_before_dropdown": 8,
}

def setup(app):
    app.add_css_file("css/custom.css")

autosectionlabel_prefix_document = True
nitpicky = False
suppress_warnings = ["ref.ref", "myst.xref_missing"]
