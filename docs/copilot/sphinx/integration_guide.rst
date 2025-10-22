Integracja ze stroną dokumentacji (Sphinx)
=========================================

Wymagania
---------
- Sphinx 7.4.7
- PyData Theme 0.16.1
- (opcjonalnie) rozszerzenia do Mermaid/Graphviz, np. `sphinxcontrib-mermaid`, `sphinx.ext.graphviz`

Kroki dodania nowej zakładki
----------------------------
1. Folder ``copilot`` znajduje się w katalogu ``docs`` w repozytorium.
2. W głównym ``index.md`` Twojej dokumentacji dodaj odnośnik do nowej sekcji::

   .. toctree::
      :maxdepth: 2
      :caption: Copilot Docs
      :hidden:

      copilot/sphinx/index

3. (PyData Theme) Aby dodać zakładkę w navbarze, dopisz do ``html_theme_options`` w ``conf.py``::

   html_theme_options = {
       "navbar_links": [
           {"name": "Copilot Docs", "url": "copilot/sphinx/index.html", "internal": True}
       ],
   }

4. Włącz rozszerzenia w ``conf.py`` (jeśli potrzebne)::

   extensions = [
       "sphinx.ext.graphviz",
       # "sphinxcontrib.mermaid",  # jeśli używasz Mermaid
   ]

5. Zbuduj dokumentację::

   sphinx-build -b html . _build/html