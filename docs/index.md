---
title: OTClientV8 – Dokumentacja
---

# OTClientV8 – Dokumentacja

```{toctree}
:hidden:
:maxdepth: 2
:caption: Spis treści

overview/getting_started
dashboard/index
api/index
rag/index
```

:::{admonition} Co to jest?
:class: tip
OTClientV8 to nowoczesny klient i framework skryptowy (Lua/C++) z bogatym zestawem modułów, API i narzędzi.
:::

:::{grid} 2
:gutter: 2

:::{grid-item}
:columns: 8

## Start

- **Szybki start** → {doc}`overview/getting_started`
- **API (surowe)** → {doc}`api/index`
- **RAG / wyszukiwarka semantyczna** → {doc}`rag/index`
- **Dashboard** → {doc}`dashboard/index`

:::

:::{grid-item}
:columns: 4

## Podgląd

<div class="simple-slider" data-interval="4000">
  <div class="slide"><img src="https://placehold.co/600x360?text=UI+Mock" alt="UI preview"></div>
  <div class="slide"><img src="https://placehold.co/600x360?text=Modules" alt="Modules"></div>
  <div class="slide"><img src="https://placehold.co/600x360?text=API+Docs" alt="API"></div>
</div>

:::
:::

## Przykładowy katalog danych

Poniżej przykładowa tabela (CSV) wczytywana podczas builda:

```{csv-table} Moduły i status
:header: "Nazwa", "Opis", "Status"
:file: _data/modules.csv
:widths: 20, 60, 20
```
