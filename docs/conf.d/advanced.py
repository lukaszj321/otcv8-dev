# === OTCv8 advanced docs patch (import from conf.py) ===
import os
html_theme = "pydata_sphinx_theme"
html_baseurl = os.environ.get("HTML_BASEURL", "https://lukaszj321.github.io/otcv8-dev/")
html_js_files = (html_js_files if 'html_js_files' in globals() else []) + ["canonical-fix.js"]
html_css_files = (html_css_files if 'html_css_files' in globals() else []) + ["custom.css"]
extensions = list(set([
    "myst_parser","sphinx_copybutton","sphinx_design","sphinx_sitemap",
    "sphinxext.opengraph","sphinx_favicon","sphinxcontrib.mermaid",
    "sphinx_codeautolink","hoverxref.extension","sphinx.ext.autosectionlabel",
    "sphinx.ext.todo","sphinx.ext.intersphinx","ablog",
] + (extensions if 'extensions' in globals() else [])))
myst_enable_extensions = list(set((myst_enable_extensions if 'myst_enable_extensions' in globals() else []) + [
    "colon_fence","linkify","attrs_block","attrs_inline","deflist","substitution"
]))
myst_heading_anchors = 3
html_theme_options = {
    **(html_theme_options if 'html_theme_options' in globals() else {}),
    "show_toc_level": 2,
    "secondary_sidebar_items": ["page-toc","sourcelink","edit-this-page","indices"],
    "use_edit_page_button": True,
    "icon_links": [{"name":"GitHub","url":"https://github.com/lukaszj321/otcv8-dev","icon":"fab fa-github"}],
}
html_context = {
    **(html_context if 'html_context' in globals() else {}),
    "github_user":"lukaszj321","github_repo":"otcv8-dev","github_version":"master","doc_path":"docs",
    "SPHINX_HTML_BASEURL": html_baseurl,
}
sitemap_url_scheme = "{link}"
ogp_social_cards = True
ogp_site_url = html_baseurl
ogp_site_name = "OTCv8 Developer Docs"
mermaid_version = "10.9.0"
blog_baseurl = html_baseurl
blog_title = "OTCv8 Dev Blog"
blog_path = "blog"
blog_feed_archives = True
blog_feed_fulltext = True
hoverxref_auto_ref = True
hoverxref_intersphinx = ["python"]
hoverxref_roles = ["numref","ref"]
html_static_path = list(set((html_static_path if 'html_static_path' in globals() else []) + ["_static"]))