---
title: OTClientV8 – Developer Documentation
---

# OTClientV8 – Developer Documentation

:::{admonition} Witamy w dokumentacji OTClient v8
:class: tip
OTClientV8 to nowoczesny klient i framework skryptowy (Lua/C++) z bogatym zestawem modułów, API i narzędzi deweloperskich.
:::

## Główne sekcje

:::{grid} 1 1 2 3
:gutter: 3

:::{grid-item-card} 🚀 Szybki start
:link: overview/getting_started
:link-type: doc
:shadow: md

Wprowadzenie do projektu, instalacja i pierwsze kroki
:::

:::{grid-item-card} 📚 API Reference
:link: api/index
:link-type: doc
:shadow: md

Kompletna dokumentacja API (Lua/C++), funkcje i interfejsy
:::

:::{grid-item-card} 🧩 Moduły
:link: modules/index
:link-type: doc
:shadow: md

Dokumentacja modułów Lua, struktura i przykłady użycia
:::

:::{grid-item-card} 🎨 UI (OTUI)
:link: ui/index
:link-type: doc
:shadow: md

System interfejsu użytkownika, widżety i style
:::

:::{grid-item-card} 📝 Authoring
:link: authoring/index
:link-type: doc
:shadow: md

Przewodniki tworzenia dokumentacji i rozdziały techniczne
:::

:::{grid-item-card} 🔍 RAG / Wyszukiwanie
:link: rag/index
:link-type: doc
:shadow: md

Wyszukiwarka semantyczna i indeks RAG
:::

:::{grid-item-card} 🧪 Workbench
:link: workbench/index
:link-type: doc
:shadow: md

Szablony skryptów, checklisty i narzędzia deweloperskie
:::

:::{grid-item-card} 📊 Dashboard
:link: dashboard/index
:link-type: doc
:shadow: md

Portal deweloperski z przeglądem projektu
:::

:::

## Architektura systemu

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
flowchart TB
    Core[OTCv8 Core C++] --> Events[System zdarzeń]
    Core --> Modules[Moduły Lua]
    Core --> UI[System UI OTUI]
    Events --> Network[Warstwa sieciowa]
    Modules --> GameRuntime[Game Runtime]
    UI --> Assets[Zasoby grafika/dźwięk]
    Core --> Settings[Ustawienia/Krypto]
    Core --> Audio[System audio]
    Core --> Logging[System logowania]
    
    style Core fill:#2d5a8c,stroke:#4a90e2,stroke-width:3px
    style Modules fill:#2d5a3c,stroke:#4ae24a,stroke-width:2px
    style UI fill:#5a2d8c,stroke:#904ae2,stroke-width:2px
```

## Struktura dokumentacji

```{toctree}
:hidden:
:maxdepth: 2
:caption: Główne sekcje

overview/getting_started
dashboard/index
api/index
modules/index
ui/index
authoring/index
rag/index
workbench/index
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: Zasoby

guide/index
cpp/index
lua/index
data/index
tools/index
```

## Status modułów

```{csv-table} Przegląd modułów
:header: "Nazwa", "Opis", "Status"
:file: _data/modules.csv
:widths: 20, 60, 20
```

## Dodatkowe zasoby

- 🔗 **GitHub**: [lukaszj321/otcv8-dev](https://github.com/lukaszj321/otcv8-dev)
- 📖 **Edit on GitHub**: Każda strona ma link do edycji
- 🔍 **Wyszukiwarka**: Użyj pola wyszukiwania w górnym pasku
- 🌓 **Motyw**: Przełącznik jasny/ciemny w prawym górnym rogu

---
