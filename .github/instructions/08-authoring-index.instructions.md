
---
title: Authoring — budowa spisu treści
owner: docs/authoring
inputs:
  - źródła: docs/authoring/**/index.md + istniejące katalogi rozdziałów
outputs:
  - md: docs/authoring/index.md (landing premium)
render:
  - myst: grids, cards, toctree (maxdepth:1), admonitions
rules:
  - pokazuj tylko rozdziały istniejące na dysku
acceptance:
  - landing ma karty do wszystkich rozdziałów oraz listę ToC
---

## Szablon landing (wygeneruj)
# Authoring — rozdziały

::{{grid}} 1 1 2 2
:gutter: 2

::{{grid-item-card}} 01 Core (C++)
:link: 01_core/index
:link-type: doc
C++ API, pliki Doxygen, metryki.
:::

::{{grid-item-card}} 02 Events
:link: 02_events/index
:link-type: doc
Emitery/subskrybenci, sekwencje.
:::

::{{grid-item-card}} 03 Modules
:link: 03_modules/index
:link-type: doc
Zestawienia modułów i widoków.
:::

::{{grid-item-card}} 04 UI
:link: 04_ui/index
:link-type: doc
OTUI, Lua snippety, drzewa widżetów.
:::
:::

```{{toctree}}
:maxdepth: 1
:caption: Authoring — spis
01_core/index
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
