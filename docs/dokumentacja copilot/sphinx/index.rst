Copilot Docs — DEV-SCAN 1:1 + PLUS
====================================

Ten dział zbiera artefakty generowane automatycznie z repozytorium OTClient v8:
indeksy kodu (C++/Lua/OTUI), diagramy zależności, cross-referencje, dane narzędzi oraz RAG.

.. toctree::
   :maxdepth: 2
   :caption: Przegląd i indeksy
   :hidden:

   overview
   integration_guide

.. toctree::
   :maxdepth: 2
   :caption: Kod źródłowy
   :hidden:

   src_code
   src_client
   src_framework
   code_index
   anchors

.. toctree::
   :maxdepth: 2
   :caption: Moduły i UI
   :hidden:

   modules
   modules_repo
   layouts
   mods
   lua_api

.. toctree::
   :maxdepth: 2
   :caption: Eventy i cross-linki
   :hidden:

   events_hooks
   crosslinks

.. toctree::
   :maxdepth: 2
   :caption: Struktury danych
   :hidden:

   trees
   trees_real

.. toctree::
   :maxdepth: 2
   :caption: Platformy i build
   :hidden:

   vc16

.. toctree::
   :maxdepth: 2
   :caption: Narzędzia z repo
   :hidden:

   lua_bindings_repo
   bitmaps_generated

Opis sekcji
-----------

**DEV-SCAN 1:1** to kompletne mapowanie struktury projektu:

- **Kod źródłowy**: indeksy plików C++ (client/framework), klasy, funkcje, enums
- **Moduły Lua**: funkcje, eventy, zależności między modułami
- **UI/OTUI**: widżety, hierarchie, powiązania z assets
- **Data/Assets**: pliki zasobów, lokalizacje, style

**PLUS** dodaje zaawansowane artefakty:

- **code_index**: każdy plik źródłowy jako osobna strona z ``literalinclude``
- **anchors**: linki do konkretnych linii kodu (per-file TOC)
- **crosslinks**: mapowania widget→asset, event→file, moduł→UI
- **trees_real**: prawdziwe drzewa katalogów (blueprinty)

**Narzędzia z repo**:

- **lua_bindings_repo**: bindingi C++→Lua wygenerowane z ``tools/lua-binding-generator``
- **bitmaps_generated**: atlasy/bitmapy wygenerowane z ``tools/gimp-bitmap-generator``

Szybki start
------------

1. Sprawdź :doc:`overview` dla listy dostępnych artefaktów (CSV, diagramy)
2. Zobacz :doc:`integration_guide` jak wpiąć do własnej dokumentacji Sphinx
3. Przeglądaj konkretne sekcje z menu po lewej stronie
4. Używaj wyszukiwarki (Ctrl+K lub przycisk 🔍) do znajdowania symboli/plików

Diagramy i visualizacje
-----------------------

Dokumentacja zawiera diagramy Mermaid i Graphviz:

- Grafy zależności modułów
- Hierarchie klas UI
- Mapy cross-referencji
- Drzewa struktury danych

Wszystkie diagramy są dostępne do pobrania w katalogach ``diagrams/`` i ``blueprints/``.

RAG i wyszukiwanie
------------------

Katalog ``rag/`` zawiera:

- ``rag_kb.jsonl``: baza wiedzy w formacie JSONL (chunki, embeddingi)
- ``cards/*.json``: karty wiedzy per-moduł/plik
- ``cards_index.csv``: indeks wszystkich kart

Można użyć tych danych do zasilenia semantycznego wyszukiwania lub asystenta AI.
