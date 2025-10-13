---
title: Authoring — Chapter Workspace
---

# Authoring (Chapters)

```{admonition} Co to jest?
:class: tip
To „robocza” sekcja dokumentacji budowana z **folderów rozdziałów**:
`01_core`, `01_runtime`, `02_events`, `03_modules`, `04_ui`, `05_events`,
`05_network`, `06_assets`, `07_settings_crypto`, `08_audio`, `09_logging`, `10_game_runtime`.
Każdy rozdział ma własny `index.md`, podkatalog `datasets/` (CSV) i `diagrams/` (Mermaid).
```

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} 01 — Core
:link: 01_core/index
:link-type: doc
Podstawy klienta, framework, C++ i API.
:::

:::{grid-item-card} 01 — Runtime
:link: 01_runtime/index
:link-type: doc
Dane i pipeline runtime.
:::

:::{grid-item-card} 02 — Events
:link: 02_events/index
:link-type: doc
System zdarzeń, strumienie, emitery.
:::

:::{grid-item-card} 03 — Modules
:link: 03_modules/index
:link-type: doc
Moduły i integracje.
:::

:::{grid-item-card} 04 — UI
:link: 04_ui/index
:link-type: doc
Interfejs OTUI, widżety, layouty.
:::

:::{grid-item-card} 05 — Events (doc)
:link: 05_events/index
:link-type: doc
Dokumenty uzupełniające.
:::

:::{grid-item-card} 05 — Network
:link: 05_network/index
:link-type: doc
Warstwa sieciowa i protokoły.
:::

:::{grid-item-card} 06 — Assets
:link: 06_assets/index
:link-type: doc
Zasoby, formaty, pipeline.
:::

:::{grid-item-card} 07 — Settings & Crypto
:link: 07_settings_crypto/index
:link-type: doc
Konfiguracja, bezpieczeństwo, kryptografia.
:::

:::{grid-item-card} 08 — Audio
:link: 08_audio/index
:link-type: doc
Silnik audio i integracje.
:::

:::{grid-item-card} 09 — Logging
:link: 09_logging/index
:link-type: doc
Logowanie, metryki, obserwowalność.
:::

:::{grid-item-card} 10 — Game Runtime
:link: 10_game_runtime/index
:link-type: doc
Pętla gry, stany, tick i zasoby.
:::
:::

## Spis rozdziałów

> **Ważne**: Ścieżki poniżej są *docname* Sphinxa (bez rozszerzeń), liczone od katalogu `docs/`.
> Nie używaj linków do GitHuba — wtedy strona nie jest włączana do nawigacji.

```{toctree}
:caption: Rozdziały (Authoring)
:maxdepth: 2
:titlesonly:

01_core/index
01_runtime/index
02_events/index
03_modules/index
04_ui/index
05_events/index
05_network/index
06_assets/index
07_settings_crypto/index
08_audio/index
09_logging/index
10_game_runtime/index
```
