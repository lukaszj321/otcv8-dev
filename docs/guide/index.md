---
title: Guide & Components
---

# Guide & Components

Praktyczne elementy PyData + sphinx‑design stosowane w projekcie.

```{toctree}
:maxdepth: 2
:hidden:
kitchen/admonitions
kitchen/blocks
kitchen/tables
kitchen/lists
kitchen/generic
kitchen/components
kitchen/indices
```

## Kitchen‑sink in practice

Admonitions, grids, cards, tabs, dropdowns – z linkami do realnych użyć.

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Admonitions
:link: kitchen/admonitions
Notatki, ostrzeżenia, tips.
:::

:::{grid-item-card} Komponenty
:link: kitchen/components
Grids, cards, tabs, badges.
:::

:::{grid-item-card} Tabele
:link: kitchen/tables
CSV-table i inne.
:::

:::{grid-item-card} Indeksy
:link: kitchen/indices
Generowanie indeksów.
:::
:::

````{tabs}
```{tab} Guide
**Best practices + checklisty:**

- Używaj grid-item-card dla navigation
- Tabs (Guide/Reference/Examples) dla struktury treści
- Dropdowns dla checklistów i zadań
- Mermaid/Graphviz z dark mode init
- CSV-table dla danych tabelarycznych
- Literalinclude z regionami dla kodu

**Workflow:**
1. Projektuj strukturę (grid + tabs)
2. Dodaj content w każdym tab
3. Osadź przykłady (CSV/kod/diagramy)
4. Zweryfikuj dark mode i responsywność
```

```{tab} Reference
**Dostępne komponenty:**
- **sphinx-design:** grid, card, tabs, dropdown, badge
- **myst-nb:** MyST Markdown z Jupyter
- **sphinxcontrib-mermaid:** Mermaid diagrams
- **sphinx.ext.graphviz:** Graphviz diagrams
- **sphinx-copybutton:** Copy button na blokach kodu

**Konfiguracja (conf.py):**
- `secondary_sidebar_items`: page-toc, sourcelink, edit-this-page
- `mermaid_output_format`: svg (lepszy dla CI)
- `mermaid_init_js`: dark theme
- `html_theme_options`: PyData theme config

**Linki do indeksów:**
- {ref}`authoring/index` — Główne rozdziały
- {ref}`copilot/sphinx/index` — Code scanner output
- {ref}`authoring/04_ui/index` — UI widgets
```

```{tab} Examples
**CSV‑table (datasets)**
```{csv-table} UI Signals — przykład z authoring
:header-rows: 1
:file: ../authoring/04_ui/datasets/signals.csv
:widths: 20, 20, 30, 30
```

**Mermaid — Sequence Diagram**
```{mermaid}
%%{init: {'theme':'dark'}}%%
sequenceDiagram
  participant User
  participant App
  participant Core
  User->>App: Click button
  App->>Core: init()
  Core-->>App: ready
  App-->>User: Show UI
```

**Graphviz — Component Architecture**
```{graphviz}
:align: center

digraph G {
  rankdir=TB;
  bgcolor="transparent";
  node [style=filled, fillcolor="#1e1e1e", fontcolor="#ddd", shape=box];
  edge [color="#9aa0a6"];
  
  subgraph cluster_ui {
    label="UI Layer";
    style=filled;
    fillcolor="#2d2d30";
    fontcolor="#ddd";
    "PyData Theme" -> "Sphinx Design";
    "Sphinx Design" -> "Cards";
    "Sphinx Design" -> "Grids";
    "Sphinx Design" -> "Tabs";
  }
  
  subgraph cluster_content {
    label="Content Layer";
    style=filled;
    fillcolor="#2d2d30";
    fontcolor="#ddd";
    "MyST Markdown" -> "Code Blocks";
    "MyST Markdown" -> "CSV Tables";
    "MyST Markdown" -> "Diagrams";
  }
  
  "PyData Theme" -> "MyST Markdown";
  "Diagrams" -> "Mermaid";
  "Diagrams" -> "Graphviz";
}
```

**Literalinclude — C++ z regionami**
```{literalinclude} ../../src/framework/xml/tinyxml.cpp
:language: cpp
:start-after: // region file_open_example
:end-before: // endregion file_open_example
:emphasize-lines: 3-6
```

**Literalinclude — Lua z regionami**
```{literalinclude} ../../modules/corelib/globals.lua
:language: lua
:start-after: -- region schedule_event_example
:end-before: -- endregion schedule_event_example
:emphasize-lines: 5-7
```

**Badges & Icons**
{badge}`success,success` {badge}`warning,warning` {badge}`info,info` {badge}`danger,danger`

**Dropdown — Advanced Options**
```{dropdown} Advanced configuration
- Theme customization via `html_theme_options`
- Custom CSS in `_static/`
- JavaScript extensions via `html_js_files`
- Mermaid version pinning: `mermaid_version = "10.9.0"`
```
```
````

## Sidebar & buttons

Prawy TOC + „Show source" + „Edit this page" włączone globalnie.

**Konfiguracja:**
```python
html_theme_options = {
    "secondary_sidebar_items": ["page-toc", "sourcelink", "edit-this-page"],
    "show_prev_next": True,
    "navigation_with_keys": True,
}
```

## Dark mode verification

```{dropdown} Quick tasks (Guide)
- [x] Dark‑mode przykładów OK (Mermaid/Graphviz)
- [x] `copybutton` na blokach kodu działa
- [x] „See also" spójny z Authoring/Copilot Docs
- [x] Grid cards renderują się responsywnie
- [x] Tabs przełączają się poprawnie
- [x] CSV tables mają nagłówki
- [x] Literalinclude używa regionów (nie linii)
```

:::{grid} 1 1 2 3
**See also:** {ref}`authoring/index` · {ref}`copilot/sphinx/index` · {ref}`authoring/04_ui/index`
:::