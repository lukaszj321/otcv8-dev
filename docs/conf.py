# -- Sphinx core config ------------------------------------------------
from datetime import datetime

project = "OTClientV8"
author = "OTClientV8 Team"
year = datetime.now().year
copyright = f"{year}, {author}"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinxcontrib.mermaid",   # ważne: kropka, NIE podkreślenie
    "sphinx_codeautolink",
    "hoverxref.extension",
]

# ABlog – miękko (w CI i tak instalujemy)
try:
    __import__("ablog")
    extensions.append("ablog")
except Exception:
    pass

# Lexer 'otui' jako INI, żeby nie sypał warningami
from sphinx.highlighting import lexers
try:
    from pygments.lexers.data import IniLexer
    lexers["otui"] = IniLexer()
except Exception:
    pass

myst_enable_extensions = [
    "colon_fence", "attrs_block", "attrs_inline",
    "deflist", "linkify", "substitution", "tasklist",
    "replacements", "html_admonition", "html_image",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}

# -- HTML / Theme -------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_title = "OTClientV8 Docs"
html_static_path = ["_static"]
html_css_files = ["custom.css", "custom-dark-mermaid.css"]
html_js_files = ["custom.js"]
html_theme_options = {
    "logo": { "text": "OTClientV8" },
    "show_nav_level": 1,
    "navbar_align": "content",
    "secondary_sidebar_items": ["page-toc", "sourcelink"],
    "navigation_depth": 2,
    "collapse_navigation": True,
    "use_edit_page_button": True,
    "footer_items": ["copyright"],
    "icon_links": [
        { "name": "GitHub",
          "url": "https://github.com/lukaszj321/otcv8-dev",
          "icon": "fa-brands fa-github" },
    ],
}
html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# sitemap / OpenGraph
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
sitemap_url_scheme = "{link}"
ogp_site_url = html_baseurl
ogp_description_length = 200

# Mermaid
mermaid_version = "10.9.1"

# Copybutton
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\$ |In \[\d+\]: |\.\.\.: "
copybutton_only_copy_prompt_lines = False

# Hoverxref
hoverxref_auto_ref = True

# Extra static
html_extra_path = ["../data"]

# Lepsze refy i kotwice
extensions += ["sphinx.ext.autosectionlabel"]
autosectionlabel_prefix_document = True
myst_heading_anchors = 4
