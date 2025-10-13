
---
title: 01_core — C++ API (Doxygen → Sphinx)
owner: docs/authoring
inputs:
  - źródła: src/**/*.h, src/**/*.hpp, include/**/*{h,hpp,hxx,c,cc,cpp}
  - zależności: doxygen >=1.9
outputs:
  - pliki_md: docs/authoring/01_core/cpp/*.md + docs/authoring/01_core/index.md
render:
  - myst: toctree, code-block cpp, admonitions, H2/H3/H4
rules:
  - idempotent: usuń docs/authoring/01_core/cpp przed generacją
  - jeśli brak .doxygen/xml/index.xml → utwórz tymczasowy Doxyfile i odpal doxygen (INPUT=src include)
  - linki: względne (bez surowych URL)
  - kotwice: autosectionlabel (H2..H4), myst_heading_anchors=4
acceptance:
  - index.md zawiera ```{{toctree}}``` wszystkich cpp/*.md
  - brak błędów Sphinx (pydata), poprawne code-blocki
---

## Zadanie
1) Z XML Doxygena odczytaj listę plików i prototypów (sygnatura + @brief jeśli jest).
2) Dla **każdego pliku** utwórz `docs/authoring/01_core/cpp/<plik>.md`:
   - H1: nazwa pliku
   - Lista funkcji jako bloki:
     ```cpp
     <sygnatura>;
     ```
     *<@brief>* (jeśli występuje).
3) Landing `docs/authoring/01_core/index.md`:
   - opis + **ToC** do `cpp/*`
   - sekcja **Metryki** (jeśli istnieje `datasets/summary.csv`)
   - sekcja **Powiązania** (odnośniki do innych rozdziałów).

## Mapowanie
- Strony: `docs/authoring/01_core/cpp/*.md`
- Landing: `docs/authoring/01_core/index.md`

## Szablon ToC dla index.md
```{{toctree}}
:maxdepth: 1
:caption: C++ pliki (API)

cpp/*
```

:::{admonition} Wskazówka: jakość diagramów
:class: tip
- Używamy `sphinxcontrib-mermaid` + `docs/_static/custom-dark-mermaid.css`, aby strzałki i etykiety były czytelne w dark/light mode.
- Węzły mają linki (`click <id> "<rel-url>" "otwórz"`), co poprawia nawigację w dokumentacji.
- Dla dużych diagramów użyj `:class: dropdown` aby były zwijane.
:::
