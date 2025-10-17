---
title: "08 — Authoring Index & Navigation"
purpose: "Build landing pages and TOC for authoring chapters."

outputs:
  - "docs/authoring/index.md"
  - "docs/authoring/<chapter>/index.md"

requirements:
  - "Use PyData grid cards + toctree"
  - "Each chapter index must include:"
  - "  • Contents ({contents} :local:)"
  - "  • Datasets ({csv-table} with at least one CSV)"
  - "  • Diagrams ({mermaid} with at least one diagram)"
  - "  • Appendix / Facets anchors for all stems"
  - "All intra-site links relative (./) and validated by Sphinx"
  - "Frontmatter present on landing + all chapter pages"
  - "Use MyST directives (not raw HTML)"

---

chapter_index_template: |
  ---
  title: {chapter_title}
  ---
  # {chapter_title}

  ```{toctree}
  :hidden:
  :maxdepth: 2
  ```
  <!-- add child pages here if any -->

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

landing_template: |
  ---
  title: Authoring — embedded
  ---
  # Authoring — embedded

  :::{grid} 1 1 2 3
  :gutter: 2

  :::{grid-item-card} Authoring — Overview
  :link: index
  :link-type: doc
  Strona główna sekcji Authoring.
  :::

  :::{grid-item-card} 01 — Core
  :link: 01_core/index
  :link-type: doc
  Podstawy klienta, framework, C++ i API.
  :::

  :::{grid-item-card} 01 — Runtime
  :link: 01_runtime/index
  :link-type: doc
  Wykonanie, pętla, kontekst.
  :::

  :::{grid-item-card} 02 — Events
  :link: 02_events/index
  :link-type: doc
  Zdarzenia i sygnały.
  :::

  :::{grid-item-card} 03 — Modules
  :link: 03_modules/index
  :link-type: doc
  Moduły i rozszerzenia.
  :::

  :::{grid-item-card} 04 — UI
  :link: 04_ui/index
  :link-type: doc
  Interfejs, widżety, motywy.
  :::

  :::{grid-item-card} 05 — Events (II)
  :link: 05_events/index
  :link-type: doc
  Zaawansowane wzorce zdarzeń.
  :::

  :::{grid-item-card} 05 — Network
  :link: 05_network/index
  :link-type: doc
  Warstwa sieciowa i protokoły.
  :::

  :::{grid-item-card} 06 — Assets
  :link: 06_assets/index
  :link-type: doc
  Zasoby, pipeline, wersjonowanie.
  :::

  :::{grid-item-card} 07 — Settings & Crypto
  :link: 07_settings_crypto/index
  :link-type: doc
  Konfiguracja, bezpieczeństwo, kryptografia.
  :::

  :::{grid-item-card} 08 — Audio
  :link: 08_audio/index
  :link-type: doc
  Dźwięk, miks, efekty.
  :::

  :::{grid-item-card} 09 — Logging
  :link: 09_logging/index
  :link-type: doc
  Logowanie, diagnostyka, observability.
  :::

  :::{grid-item-card} 10 — Game Runtime
  :link: 10_game_runtime/index
  :link-type: doc
  Uruchomienie gry, sceny, pętle.
  :::

  :::{grid-item-card} 11 — Data
  :link: 11_data/index
  :link-type: doc
  Dane, modele, migracje.
  :::

  :::{grid-item-card} 12 — OTMod
  :link: 12_otmod/index
  :link-type: doc
  Format OTMod, specyfikacje, narzędzia.
  :::

  :::{grid-item-card} 13 — Layouts
  :link: 13_layouts/index
  :link-type: doc
  Layouty, siatki, responsywność.
  :::

  :::{grid-item-card} 14 — Android
  :link: 14_android/index
  :link-type: doc
  Android/ABI, buildy, UX mobilny.
  :::

  :::{grid-item-card} 15 — VC16
  :link: 15_vc16/index
  :link-type: doc
  Toolchain VC16, kompilacja, CI.
  :::

  :::

acceptance:
  - [ ] Landing pokazuje wszystkie rozdziały (01..15) z działającymi linkami
  - [ ] Każdy rozdział ma frontmatter, `{contents} :local:`, ≥1 `{csv-table}`, ≥1 `{mermaid}`
  - [ ] `summary.csv` istnieje w `datasets/` lub sekcja Datasets ukryta warunkowo
  - [ ] Brak błędów linków (nitpicky) przy `sphinx-build -W`
  - [ ] Anchory `facet-<chapter>.<stem>` obecne (jeśli są stem-y)

## IPC

**Kanały IPC (Studio/Electron)**

- `studio:authoring.index.scan` — skanuje `docs/authoring/**` i tworzy spis treści + indeks artefaktów per rozdział.
- `studio:authoring.index.open` `{ section }` — otwiera wybraną sekcję w Studio.
- `studio:authoring.index.validate` — weryfikuje kotwice facetów i ścieżki do datasetów/diagramów.

## Sanity

- [ ] Wszystkie ścieżki w indeksie są względne i istnieją na dysku.
- [ ] Kotwice facetalne w odnośnikach (`#facet-<chapter>.<id>`) kierują do zdefiniowanych facetów.
- [ ] Rozdziały mają uzupełnione sekcje `artifacts:` (datasets/diagrams) lub są jawnie oznaczone jako N/A.
