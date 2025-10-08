# -- Project info -----------------------------------------------------
project = "OTCv8 — Dokumentacja"
author = "OTCv8 contributors"

# -- General config ----------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.mermaid",
]

source_suffix = {
    ".md": "myst",
    ".rst": "restructuredtext",
}

# MyST config: allow extended Markdown features
myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "substitution",
    "colon_fence",
    "tasklist",
    "smartquotes",
]

# Create anchors for all headings so you can link like (#some-heading)
myst_heading_anchors = 6

# Let fenced ```mermaid blocks render as diagrams (no content changes needed)
myst_fence_as_directive = {
    "mermaid": "mermaid",
}

# Optional: automatically create :ref: labels for section titles
autosectionlabel_prefix_document = True

# TEMP: keep CI logs cleaner while we migrate anchors/labels
suppress_warnings = [
    "myst.xref_missing",
]

# -- HTML theme --------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

# -- Pygments/lexers ---------------------------------------------------
# Map custom fences to existing lexers so '```otui' and '```otml' don't warn.
def setup(app):
    try:
        from pygments.lexers.data import IniLexer, YamlLexer
        from pygments.lexers.special import TextLexer
        app.add_lexer("otui", IniLexer())
        app.add_lexer("otml", YamlLexer())
        # Fallback if someone uses ```mermaid without the extension picking it up
        app.add_lexer("mermaid", TextLexer())
    except Exception as e:
        # Never fail the build because of missing lexers in CI
        print(f"[conf.py] lexer setup skipped: {e}")
