
---
chapter: "12_otmod"
slug: "12_otmod"
title: "OTMOD — moduły, hooki i lifecycle (specyfikacja + praktyka)"
status: "agent_ready"
doc_class: "module"
language: "pl"
summary: >
  Specyfikacja manifestów OTMOD, zależności, hooków (@onLoad/@onUnload),
  deterministyczne ładowanie i powiązania z UI/Lua. Zawiera schematy datasetów
  oraz heurystyki ekstrakcji dla agenta.
tags: ["otmod","modules","lua","ui","lifecycle","authoring","rag"]
artifacts:
  datasets:
    - id: "modules_index"
      file: "modules_index.csv"
      headers: ["module","description","author","sandboxed","scripts","load_later","dependencies","website","path"]
      facet: "12_otmod.modules_index"
    - id: "module_scripts"
      file: "module_scripts.csv"
      headers: ["module","script","order","source_file","lines","exports","requires"]
      facet: "12_otmod.module_scripts"
    - id: "module_deps"
      file: "module_deps.csv"
      headers: ["module","depends_on","type","note"]
      facet: "12_otmod.module_deps"
    - id: "module_hooks"
      file: "module_hooks.csv"
      headers: ["module","hook","function","priority","source_file","line"]
      facet: "12_otmod.module_hooks"
    - id: "module_ui_links"
      file: "module_ui_links.csv"
      headers: ["module","otui_file","widget_root","widgets_count","images_count","fonts_used","styles_used"]
      facet: "12_otmod.module_ui_links"
  diagrams:
    - id: "lifecycle"
      file: "lifecycle.mmd"
      facet: "12_otmod.lifecycle"
    - id: "deps"
      file: "deps.mmd"
      facet: "12_otmod.deps"
xrefs:
  - to: "04_ui.widgets_index"
    type: "renders"
    evidence: "docs/authoring/12_otmod/datasets/module_ui_links.csv"
---

# OTMOD — Moduły, Hooki, Zależności, UI i lifecycle (specyfikacja + praktyka)

**Cel rozdziału:** Zdefiniować **format OTMOD**, przepływ życia modułów, typowe hooki, schemat zależności oraz powiązania z UI (OTUI). Ten rozdział to *starter kit* dla agentów do analizy modułów i budowania RAG.

::: {admonition} Czym jest OTMOD?
Plik **`.otmod`** opisuje moduł klienta OTClient: metadane, listę skryptów, hooki cyklu życia i zależności. Moduły mogą wczytywać OTUI, emitować zdarzenia i korzystać z API Lua.
:::

:::{admonition} Po co OTMOD?
:class: note
Moduły izolują odpowiedzialności i wymuszają **deterministyczne ładowanie**. To minimalizuje problemy typu „co ładuje się pierwsze?” i poprawia debugowalność.
:::

```{contents}
:local:
:depth: 2
```

## Manifest — składnia i zasady

```otmod
Module
  name: game_interface
  description: Create the game interface, where the ingame stuff starts
  author: OTClient team
  website: https://github.com/edubart/otclient
  sandboxed: true
  scripts: [ widgets/uigamemap, gameinterface ]
  load-later: [ game_skills, game_inventory, game_console ]
  @onLoad: init()
  @onUnload: terminate()
```

- **name**: unikalny identyfikator modułu (używaj `kebab_case`).
- **scripts**: kolejność ma znaczenie (bootstrap → widgets → adaptery).
- **load-later**: miękkie zależności (ładowane po rdzeniu UI).
- **@onLoad/@onUnload**: hooki cyklu życia — czyste init/terminate.
- **sandboxed**: blokuje side‑effects poza interfejsem API (zalecane `true`).

## Schematy datasetów (kontrakt)

### `modules_index.csv`
| module | description | author | sandboxed | scripts | load_later | dependencies | website | path |
|---|---|---|---|---|---|---|---|---|

### `module_scripts.csv`
| module | script | order | source_file | lines | exports | requires |
|---|---|---|---|---|---|---|

### `module_deps.csv`
| module | depends_on | type | note |
|---|---|---|---|

### `module_hooks.csv`
| module | hook | function | priority | source_file | line |
|---|---|---|---|---|---|

### `module_ui_links.csv`
| module | otui_file | widget_root | widgets_count | images_count | fonts_used | styles_used |
|---|---|---|---|---|---|---|

## Heurystyki ekstrakcji

- `*.otmod` → `modules_index.csv` (klucze: name/description/...).
- `scripts[]` → `module_scripts.csv` (+ exports/require z Lua).
- `dependencies`/`load-later` → `module_deps.csv` (typy: `hard`/`soft`).
- Hooki `@onLoad/@onUnload` → `module_hooks.csv` (priorytety opcjonalne).
- Powiązania z OTUI → `module_ui_links.csv`.

## Przykłady (game_skills)

```otmod
Module
  name: game_skills
  description: Manage skills window
  author: baxnie, edubart
  website: https://github.com/edubart/otclient
  sandboxed: true
  scripts: [ skills ]
  @onLoad: init()
  @onUnload: terminate()
  dependencies: [ game_interface ]
```

### Fragment OTUI (powiązanie)
```otui
MiniWindow
  id: skillWindow
  !text: tr('Skills')
  icon: /images/topbuttons/skills
  @onClose: modules.game_skills.onMiniWindowClose()
```

## Diagramy

### Lifecycle
```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
sequenceDiagram
  participant L as Loader
  participant M as Module(OTMOD)
  participant S as Scripts(Lua)
  L->>M: load()
  M->>S: scripts[] bootstrap
  M->>S: @onLoad -> init()
  S-->>M: ready()
  L->>M: unload()
  M->>S: @onUnload -> terminate()
```

### Zależności
```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  game_interface --> game_skills
  game_interface --> game_inventory
  game_interface --> game_console
  game_skills --> game_stats
```

{SPHINX_DESIGN_BLOCK}

{RAG_GUIDE_BLOCK}

{CODE_STANDARDS_BLOCK}


## Blueprinty

- Zobacz `../blueprints/otmod_blueprints.csv` — szkielety produkcyjne (core/feature).
- Każdy blueprint zawiera **obowiązkowe klucze**, **opcjonalne**, blok przykładowy oraz notatki wdrożeniowe.

## Blueprint OTMOD (kanoniczny)

```otmod
Module
  name: game_interface
  description: Create the game interface, where the ingame stuff starts
  author: OTClient team
  website: https://github.com/edubart/otclient
  sandboxed: true
  scripts: [ widgets/uigamemap, gameinterface ]
  load-later:
    - game_buttons
    - game_hotkeys
    - game_questlog
    - game_textmessage
    - game_console
    - game_outfit
    - game_healthinfo
    - game_skills
    - game_inventory
    - game_containers
    - game_viplist
    - game_battle
    - game_minimap
    - game_npctrade
    - game_textwindow
    - game_playertrade
    - game_bugreport
    - game_playerdeath
    - game_playermount
    - game_ruleviolation
    - game_market
    - game_spelllist
    - game_cooldown
    - game_modaldialog
    - game_unjustifiedpoints
    - game_walking
    - game_shop
    - game_itemselector
    - client_textedit
    - client_profiles
    - game_actionbar
    - game_prey
    - game_imbuing
    - game_stats
    - game_shaders
    - game_bot
  @onLoad: init()
  @onUnload: terminate()
```

## Hooki cyklu życia i konwencje

- `@onLoad: init()` – punkt startowy modułu; rejestruje UI, eventy, skróty, itp.  
- `@onUnload: terminate()` – czyszczenie zasobów, odpinanie eventów.

**Konwencje plików Lua:**  
- `init()` i `terminate()` zdefiniowane w głównym skrypcie modułu (`<module_name>.lua` lub pliku wskazanym w `scripts`).  
- API eksportowane do innych modułów: przez globalny namespace `modules.<module_name>`.

**Przykład minimalnego modułu:**

```otmod
Module
  name: sample
  description: Minimal module example
  author: you
  scripts: [ sample ]
  @onLoad: init()
  @onUnload: terminate()
```

```lua
-- modules/sample/sample.lua
function init()
  -- build UI, connect signals, etc.
end

function terminate()
  -- cleanup
end
```

## Analiza zależności

- `load-later:` – lazy-load; nie wymusza cyklu życia natychmiast, ale wyznacza **kolejność**.
- `dependencies:` – twarde zależności (często w mniejszych modułach).

**Dataset `module_deps.csv`** stanowi **macierz relacji** do generowania grafu.

## Powiązanie z UI (OTUI)

Moduły często dostarczają OTUI. Przykład (fragment **skills.otui**):

```otui
MiniWindow
  id: skillWindow
  !text: tr('Skills')
  icon: /images/topbuttons/skills
  @onClose: modules.game_skills.onMiniWindowClose()
```

**Ekstrakcja do `module_ui_links.csv`:**
- `module_name=game_skills`
- `ui_file=modules/game_skills/skills.otui`
- `ui_id=skillWindow`
- `widget_count=...`
- `assets_refs=/images/topbuttons/skills` (i inne właściwości assetowe)

Po stronie **11_data** budujemy `ui_asset_usage.csv` i łączymy po `ui_id`/`ui_file`.

## Diagramy

### lifecycle
*Facet:* [`12_otmod.lifecycle`](#facet-12_otmod.lifecycle)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
sequenceDiagram
  participant Loader
  participant Module as game_interface
  participant UI as OTUI
  Loader->>Module: @onLoad → init()
  Module->>UI: load skills.otui / register widgets
  Module-->>Loader: ready
  Loader->>Module: @onUnload → terminate()
```

### deps_graph
*Facet:* [`12_otmod.deps_graph`](#facet-12_otmod.deps_graph)

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph TD
  A[game_interface] --> B[game_skills]
  A --> C[game_hotkeys]
  B --> D[game_stats]
```

## Heurystyki analizy (dla Agenta)

1. **Kolejność ładowania**: najpierw `scripts`, potem `load-later`.
2. **API**: jeśli `modules.<name>` posiada funkcje, dopisz `provides_api=true`.
3. **UI**: szukaj plików `*.otui` w katalogu modułu; policz `widget_count` (węzły zaczynające od nazw klas).
4. **Zależności**: interpretuj listy `load-later` jako krawędzie w grafie zależności (miękkie).

## RAG & chunking

- Dziel po **sekcjach hooków i UI**; utrzymuj **≤1200 tokenów**.
- Nie tnij wewnątrz definicji `Module`/listy `scripts`.
- Dokładaj *See also* do `11_data` i `04_ui`.

## QA (minimalne)

- `link-lint`, `diagram-lint`, `dataset sanity`, `idempotency` — jak w rozdziale 11.

## FAQ

**Czy `dependencies` i `load-later` mogą tworzyć cykle?**  
Unikaj — raportuj i zrywaj pętle (QA).

**Czy hooki mogą mieć priorytety?**  
Tak, przez dodatkowy atrybut `priority` w `module_hooks.csv` (opcjonalne).

## Appendix / Facets

(facet-12_otmod.modules_index)=
### Facet: `12_otmod.modules_index`
Type: dataset

(facet-12_otmod.module_scripts)=
### Facet: `12_otmod.module_scripts`
Type: dataset

(facet-12_otmod.module_deps)=
### Facet: `12_otmod.module_deps`
Type: dataset

(facet-12_otmod.module_hooks)=
### Facet: `12_otmod.module_hooks`
Type: dataset

(facet-12_otmod.module_ui_links)=
### Facet: `12_otmod.module_ui_links`
Type: dataset

(facet-12_otmod.lifecycle)=
### Facet: `12_otmod.lifecycle`
Type: diagram

(facet-12_otmod.deps_graph)=
### Facet: `12_otmod.deps_graph`
Type: diagram


### Appendix: Test Cases & Linters
- Link-lint: wszystkie linki względne muszą przechodzić.
- Diagram-lint: każdy `.mmd` z init headerem.
- Dataset sanity: brak pustych kolumn nagłówków.
- Idempotency: brak zmian przy drugim biegu.

