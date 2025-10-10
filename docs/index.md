# OTCv8 — dokumentacja i dashboard

:::{note}
To **wersja robocza** dashboardu. Sekcje oznaczone jako _placeholder_ będą uzupełniane sukcesywnie.
:::

<div class="otc-hero">

## Szybki start

- **API (surowe)**: przegląd modułów, emiterów, zdarzeń i interfejsów → [API Overview](api/index.md)
- **Opisowa dokumentacja**: architektura, zasady, UX i przykłady → [UI & Modules](../04_ui/index.md)
- **RAG / context**: dane źródłowe i jak je trenować/odpytywać → [RAG Hub](rag/index.md)

</div>

## Dashboard

:::{grid} 1 2 2 3
:gutter: 2

:::{grid-item-card} 📚 Dokumentacja opisowa
:link: 04_ui/index.md
:link-type: doc
**Architektura UI, moduły i przepływy**. Wytyczne H2/H3/H4, style kodu i wzorce.
:::

:::{grid-item-card} 🧩 API (Core)
:link: api/index.md
:link-type: doc
Zebrane **nagłówki, funkcje, parametry** i przykłady użycia.
:::

:::{grid-item-card} 🧠 RAG / Knowledge
:link: rag/index.md
:link-type: doc
Źródła prawdy, embeddingi, aktualizacja indeksów i polityki cache.
:::

:::{grid-item-card} 🗂️ Datasets / `data/`
:link: datasets/index.md
:link-type: doc
Obrazy, fonty, binaria. Publikacja w witrynie i sposób linkowania.
:::

:::{grid-item-card} 🧭 Diagramy i grafy
:link: diagrams/index.md
:link-type: doc
Mermaid/Graphviz i wytyczne dla light/dark mode.
:::

:::{grid-item-card} 📊 Tabele i raporty
:link: tables/index.md
:link-type: doc
Struktury CSV/TSV, formatowanie i warianty responsywne.
:::

:::{grid-item-card} 📓 Notatniki / wykresy
:link: notebooks/index.md
:link-type: doc
Integracja z Jupyter (opcjonalnie `myst-nb`) i matplotlib/plotly.
:::

:::{grid-item-card} 🛣️ Roadmapa
:link: roadmap/index.md
:link-type: doc
Plan rozbudowy dokumentacji i feature’ów dashboardu.
:::

:::{grid-item-card} 🗒️ Changelogs
:link: changelogs/index.md
:link-type: doc
Historia zmian w API i dokumentacji (semver + daty).
:::

:::

```{{toctree}}
:hidden:
:maxdepth: 2
:caption: Spis treści

api/index
rag/index
datasets/index
diagrams/index
tables/index
notebooks/index
roadmap/index
changelogs/index
```
