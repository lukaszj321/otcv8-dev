Lua Bindings (repo, generator)
==============================

Poniższa tabela jest zasilana **automatycznie** przez narzędzie z repo: ``tools/lua-binding-generator``.
Po uruchomieniu generatora wyeksportuj dane do pliku CSV: ``docs/copilot/csv/lua_bindings_repo.csv``
(z kolumnami: ``cpp_symbol``, ``lua_name``, ``file``, ``note``).

.. csv-table:: lua_bindings_repo.csv
   :file: ../csv/lua_bindings_repo.csv
   :header-rows: 1

Instrukcja
----------
1. Uruchom generator w ``tools/lua-binding-generator`` zgodnie z README narzędzia.
2. Wyeksportuj wyniki do ``csv/lua_bindings_repo.csv`` (format jak wyżej).
3. (Opcjonalnie) dodaj JSONL do ``rag/`` z wpisami per-binding.
4. Zbuduj dokumentację: ``sphinx-build -b html docs docs/_build/html``.