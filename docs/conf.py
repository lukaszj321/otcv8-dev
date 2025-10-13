# -- Sphinx core config ------------------------------------------------
import os
import sys
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
    "sphinxcontrib.mermaid",
    "sphinx_codeautolink",
    "hoverxref.extension",
    # UWAGA: ablog dokładamy niżej warunkowo
]

# --- ABlog (ładuj bezpiecznie; jeśli brak – nie wywala builda) ----------
try:
    import ablog  # noqa: F401
    extensions.append("ablog")
    blog_title = "OTCv8 Blog"
    blog_path = "blog"
    blog_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
    blog_authors = {"lukasz": ("lukasz", "https://github.com/lukaszj321")}
except Exception:
    pass

# --- Lexer dla OTUI (wyłącz warning o nieznanym lexerze) ----------------
from sphinx.highlighting import lexers
try:
    from pygments.lexers.data import IniLexer
    lexers["otui"] = IniLexer()  # treat .otui blocks jak INI
except Exception:
    pass

# --- MyST ---------------------------------------------------------------
myst_enable_extensions = [
    "colon_fence", "attrs_block", "attrs_inline",
    "deflist", "linkify", "substitution", "tasklist",
    "replacements", "html_admonition", "html_image",
]
# Stabilne kotwice H1..H4 (lepsze linkowanie między plikami)
myst_heading_anchors = 4

# Autosectionlabel: krótsze/clean sidebary i proste :ref: do nagłówków
extensions += ["sphinx.ext.autosectionlabel"]
autosectionlabel_prefix_document = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}

# -- HTML / Theme -------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_title = "OTClientV8 Docs"
html_static_path = ["_static"]
html_css_files = ["custom.css", "custom-dark-mermaid.css"]  # dark-mode fix
html_js_files = ["custom.js"]

html_theme_options = {
    "logo": {"text": "OTClientV8"},
    "show_nav_level": 1,          # mniej hałasu w sidebarze
    "navigation_depth": 2,
    "collapse_navigation": True,  # składany sidebar
    "navbar_align": "content",
    "secondary_sidebar_items": ["page-toc", "sourcelink"],
    "use_edit_page_button": True,
    "footer_items": ["copyright"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lukaszj321/otcv8-dev",
            "icon": "fa-brands fa-github",
        },
    ],
}

html_context = {
    "github_user": "lukaszj321",
    "github_repo": "otcv8-dev",
    "github_version": "master",
    "doc_path": "docs",
}

# sitemap
html_baseurl = "https://lukaszj321.github.io/otcv8-dev/"
sitemap_url_scheme = "{link}"

# OpenGraph
ogp_site_url = html_baseurl
ogp_description_length = 200

# Mermaid + Graphviz (dark/light aware)
mermaid_version = "10.9.1"
graphviz_output_format = "svg"
graphviz_dot_args = ["-Gbgcolor=transparent"]

# Copybutton
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\$ |In \[\d+\]: |\.\.\.: "
copybutton_only_copy_prompt_lines = False

# Hoverxref
hoverxref_auto_ref = True

# Extra static (uwaga: to wskazuje folder poza docs/)
html_extra_path = ["../data"]
