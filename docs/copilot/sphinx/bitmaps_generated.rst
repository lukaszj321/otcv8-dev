Wygenerowane bitmapy / atlasy
=============================

Ta sekcja dokumentuje produkty narzędzia: ``tools/gimp-bitmap-generator``.
Po uruchomieniu generatora wyeksportuj listę wyników do CSV: ``docs/copilot/csv/bitmaps_generated.csv``
(z kolumnami: ``output_path``, ``width``, ``height``, ``source_set``, ``note``).

.. csv-table:: bitmaps_generated.csv
   :file: ../csv/bitmaps_generated.csv
   :header-rows: 1

Instrukcja
----------
1. Uruchom narzędzie w ``tools/gimp-bitmap-generator`` zgodnie z README narzędzia.
2. Zapisz zestaw wyników do ``csv/bitmaps_generated.csv`` (format jak wyżej).
3. (Opcjonalnie) dołącz manifesty/miniatury do ``source_mirror/`` i dopisz linki w tej stronie.
4. Zbuduj dokumentację: ``sphinx-build -b html docs docs/_build/html``.