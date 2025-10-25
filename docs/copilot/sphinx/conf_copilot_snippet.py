# safe Copilot add-on for PyData / Sphinx 8
def _add_nav_link(app, config):
    opts = dict(config.html_theme_options or {})
    nav = list(opts.get("navbar_links", []))
    if not any(isinstance(x, dict) and x.get("url") == "copilot/index.html" for x in nav):
        nav.append({"name": "Copilot Docs", "url": "copilot/index.html", "internal": True})
    opts["navbar_links"] = nav
    config.html_theme_options = opts

def setup(app):
    # ZERO odwołań do nieistniejących eventów (Sphinx 8)
    app.connect("config-inited", _add_nav_link, priority=200)
