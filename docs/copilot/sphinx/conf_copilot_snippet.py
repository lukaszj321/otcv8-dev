# --- Copilot Docs snippet (append to your conf.py) ---
extensions = list(set(extensions + ["sphinx.ext.graphviz"]))  # ensure graphviz
html_theme_options = dict(html_theme_options or {})
navbar_links = list(html_theme_options.get("navbar_links", []))
navbar_links.append({"name": "Copilot Docs", "url": "dokumentacja%20copilot/index.html", "internal": True})
html_theme_options["navbar_links"] = navbar_links
# --- end ---
