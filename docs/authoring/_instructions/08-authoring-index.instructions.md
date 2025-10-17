---

title: 08 — Authoring Index & Navigation
purpose: Build landing pages and TOC for authoring chapters.
outputs:

* docs/authoring/index.md
* docs/authoring/<chapter>/index.md
  requirements:
* Use PyData grid cards + toctree
* Each chapter index must include:

  * Contents (`{contents} :local:`)
  * Datasets ({csv-table} with at least one CSV)
  * Diagrams ({mermaid} with at least one diagram)
  * Appendix / Facets anchors for all stems
* All intra-site links relative (./) and validated by Sphinx
* Frontmatter present on landing + all chapter pages
* Use MyST directives (not raw HTML)

## chapter.index.template: |

## title: {chapter_title}

# {chapter_title}

```{toctree}
:hidden:
:maxdepth: 2

# add child pages here if any
```

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets

```{csv-table} Summary
:header-rows: 1
:file: ./datasets/summary.csv
```

## Diagrams

```{mermaid}
%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph LR
  A[Source] --> B[Dataset]
```

## Appendix / Facets

  <!-- one anchor per stem produced elsewhere; keep stable IDs -->

  <!-- examples:
  <span id="facet-{chapter}.{stemA}"></span>
  <span id="facet-{chapter}.{stemB}"></span>
  -->

## landing.template: |

## title: Authoring — embedded

# Authoring — embedded

:::{grid} 1 1 2 3
:gutter: 2

::::{grid-item-card} 01 — Core
:link: 01_core/index
:link-type: doc
Podstawy klienta, framework, C++ i API.
::::

::::{grid-item-card} 01 — Runtime
:link: 01_runtime/index
:link-type: doc
Wykonanie, pętla gry, kontekst.
::::

::::{grid-item-card} 02 — Events
:link: 02_events/index
:link-type: doc
Zdarzenia i sygnały.
::::

::::{grid-item-card} 03 — Modules
:link: 03_modules/index
:link-type: doc
Moduły i rozszerzenia.
::::

::::{grid-item-card} 04 — UI
:link: 04_ui/index
:link-type: doc
Interfejs, widżety, motywy.
::::

::::{grid-item-card} 05 — Network
:link: 05_network/index
:link-type: doc
Warstwa sieciowa.
::::

::::{grid-item-card} 06 — Authoring
:link: 06_authoring/index
:link-type: doc
Pipeline tworzenia treści i diagramów.
::::

::::{grid-item-card} 07 — Assets & Crypto
:link: 07_settings_crypto/index
:link-type: doc
Ustawienia i kryptografia.
::::

::::{grid-item-card} 08 — Audio
:link: 08_audio/index
:link-type: doc
Dźwięk i miks.
::::

::::{grid-item-card} 09 — Logging
:link: 09_logging/index
:link-type: doc
Logowanie i diagnostyka.
::::

::::{grid-item-card} 10 — Game Runtime
:link: 10_game_runtime/index
:link-type: doc
Uruchomienie gry, sceny, pętle.
::::

:::

acceptance:

* [ ] Landing pokazuje wszystkie rozdziały (01..10) z działającymi linkami
* [ ] Każdy rozdział ma frontmatter, `{contents} :local:`, ≥1 `{csv-table}`, ≥1 `{mermaid}`
* [ ] `summary.csv` istnieje w `datasets/` lub sekcja Datasets jest ukryta warunkowo
* [ ] Brak błędów linków (nitpicky) przy `sphinx-build -W`
* [ ] Anchory `facet-<chapter>.<stem>` obecne (jeśli są stem-y)
