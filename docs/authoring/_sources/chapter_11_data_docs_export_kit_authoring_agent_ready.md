
---
chapter: "11_data"
slug: "11_data"
title: "Data — Assets, Styles, Locales, Shaders, Sounds"
status: "agent_ready"
doc_id: "authoring.11_data"
language: "pl"
last_sync_iso: "2025-10-15T15:55:31.970929"
tags: ["otclient", "data", "assets", "otui", "styles", "locales", "shaders", "sounds", "rag"]
artifacts:
  datasets:
    - id: "images"
      file: "images.csv"
      headers: ["path","kind","width","height","theme","used_by_ui_ids","notes"]
      facet: "11_data.images"
    - id: "fonts"
      file: "fonts.csv"
      headers: ["font_id","file","size","weight","mono","fallbacks"]
      facet: "11_data.fonts"
    - id: "styles"
      file: "styles.csv"
      headers: ["style_id","source_file","selector","property","value","resolved_asset"]
      facet: "11_data.styles"
    - id: "locales"
      file: "locales.csv"
      headers: ["lang","key","value","source_file"]
      facet: "11_data.locales"
    - id: "sounds"
      file: "sounds.csv"
      headers: ["path","duration_ms","channels","rate_hz","kind","used_by"]
      facet: "11_data.sounds"
    - id: "shaders"
      file: "shaders.csv"
      headers: ["name","type","file","uniforms","includes"]
      facet: "11_data.shaders"
    - id: "ui_asset_usage"
      file: "ui_asset_usage.csv"
      headers: ["ui_id","ui_file","widget_path","prop","value","asset_path","resolved_path","notes"]
      facet: "11_data.ui_asset_usage"
  diagrams:
    - id: "data_overview"
      file: "data_overview.mmd"
      facet: "11_data.data_overview"
    - id: "asset_to_ui"
      file: "asset_to_ui.mmd"
      facet: "11_data.asset_to_ui"
xrefs:
  - to: "04_ui.widgets_catalog"
    type: "renders"
    evidence: "docs/authoring/11_data/datasets/ui_asset_usage.csv"
  - to: "03_modules.lua_exports"
    type: "uses"
    evidence: "docs/authoring/12_otmod/datasets/module_ui_links.csv"
---

# Data — Assets, Styles, Locales, Shaders, Sounds

**Cel rozdziału:** Jedno, spójne źródło prawdy o wszystkich zasobach w `data/**` (oraz ich *override* w `layouts/**`). Rozdział zawiera **kontrakty datasetów**, przykładowe rekordy, reguły rozwiązywania ścieżek, a także **mapowanie asset → OTUI → funkcje** do potrzeb **RAG** i nawigacji w IDE.

:::{{admonition}} Dlaczego to ważne?
:class: tip
Dobre mapowanie zasobów pozwala agentom łączyć OTUI z rzeczywistą grafiką, czcionkami i stylami. Dzięki temu asystent w React/IDE może generować komponenty 1:1 oraz podpowiedzi do API.
:::

## Model rozwiązywania ścieżek (Data ↔ Layouts)

:::{{admonition}} Zasada override
Jeśli istnieje `layouts/<LAYOUT>/images/foo.png`, a także `data/images/foo.png` — **aktywny layout wygrywa**. Inaczej mówiąc, `layouts/<LAYOUT>/**` ma wyższy priorytet niż `data/**`.
Nie twórz layoutu o nazwie `default` – ta nazwa jest zarezerwowana.
:::

**Źródła do skanowania:**

- `data/`: `cursors/**`, `fonts/**`, `images/**`, `locales/**`, `shaders/**`, `sounds/**`, `styles/**`
- `layouts/<name>/`: analogiczne poddrzewa, które **nadpisują** zasoby z `data/`

**Reguły:**

1. Normalizuj ścieżki do formatu bezwzględnego w dokumentacji (np. `data/images/topbuttons/skills.png`).
2. Dla każdego odwołania z OTUI (np. `image-source: /images/ui/tabbutton_square`) policz **resolved_path**:
   - jeśli aktywny layout ma `/layouts/<name>/images/ui/tabbutton_square.png` → użyj tego;
   - inaczej użyj `/data/images/ui/tabbutton_square.png`.
3. W `styles/**` odczytuj **wszystkie** właściwości, nie tylko assetowe (np. `color`, `icon-color`, `font`, `image-clip`).


## Co jest w `data/` (mapa aktywów)

- **images/** — ikony, sprites, tła (PNG/JPG/WebP).
- **fonts/** — czcionki bitmapowe/TTF, np. `verdana-11px-monochrome`.
- **styles/** — style OTUI (właściwości, warianty, stany `$hover/$checked/$disabled`).
- **locales/** — tłumaczenia (klucze używane przez `tr('...')`/`!text: tr('...')`).
- **cursors/** — wskaźniki myszy (możliwe warianty DPI).
- **sounds/** — efekty dźwiękowe, UI beeps.
- **shaders/** — efekty graficzne 2D (GLSL).
- **layouts/** — *override* dla zasobów (np. `mobile`, `retro`). Przy aktywnym layoucie agent **podmienia** ścieżki.

:::{note}
Wszystkie ścieżki w datasetach są **względne** i konsumpowane przez generator stron MyST.  
Przy aktywnym layoucie (np. `layouts/mobile`) zasoby w layoucie podmieniają bazowe z `data/`.
:::

## Mapowanie OTUI → Assets (pełna tabela i przykłady)

| Właściwość     | Opis                     | Rozpoznawanie                                 | Przykład                      | Uwagi                               |
| -------------- | ------------------------ | --------------------------------------------- | ----------------------------- | ----------------------------------- |
| `image-source` | Główna bitmapa widgetu   | Ścieżka bez rozszerzenia → dopełnienie `.png` | `/images/ui/tabbutton_square` | Obsługa layoutów (override)         |
| `icon`         | Ikona przycisku/elementu | Jak `image-source`                            | `/images/topbuttons/skills`   | Może mieć `icon-color`              |
| `font`         | Czcionka                 | Alias z `fonts.csv`                           | `verdana-11px-monochrome`     | Rozmiar w definicji fontu           |
| `background`   | Tło                      | Jak `image-source`                            | `/images/panels/panel_bg`     | Może współgrać z `background-color` |
| `image-color`  | Tint                     | Hex/rgba                                      | `#dfdfdf`                     | Nie zmienia ścieżki assetu          |

### Przykład adnotowanego OTUI (mapowanie)
```otui
TabBar < UITabBar
  Panel
    id: buttonsPanel
TabBarButton < UIButton
  image-source: /images/ui/tabbutton_square   # -> images/ui/tabbutton_square.png -> images.csv.asset_id=tabbutton.square
  icon-color: #dfdfdf
  $checked:
    image-clip: 0 36 98 18                    # geometry, nie-asset
```

## Heurystyki ekstrakcji (Agent)

:::{dropdown} Assety w OTUI — jak je znajdujemy?
- Skany: **`image-source`**, **`icon`**, **`font`**, **`background`**, **`image-color`**.
- Normalizacja ścieżek: `/images/ui/file` → `images/ui/file.png` (jeśli brak rozszerzenia).
- Layouty: jeżeli aktywny, `layouts/<name>/images/...` **nadpisuje** `data/images/...`.
- Zapis: **`ui_asset_usage.csv`** z kontekstem (`widget_path`, `line`, `source_file`).
- Walidacja: istnienie pliku, rozdzielczość, warianty DPI (opcjonalnie).
:::

:::{dropdown} Style — stany i dziedziczenie
- Bloki `ClassName < BaseClass` → zbiór par `prop:value`.
- Stany (`$hover`, `$checked`, `$disabled`) rozwijamy do osobnych rekordów.
- Podpinamy relacje do rozdziałów `03_modules`/`05_events` dla `@on*/&on*`.
- Porządkujemy style per widget_class → `styles.csv`.
:::

:::{dropdown} Lokalizacje
- Ekstrakcja kluczy z `tr('...')` i `!text: tr('...')` z plików `.otui` i `.lua`.
- Budujemy `locales.csv` i walidujemy brakujące tłumaczenia.
:::

{SPHINX_DESIGN_BLOCK}

## Schematy datasetów (kontrakt)

### `images.csv`
| asset_id | rel_path | category | format | size_px | used_in_files | used_in_widgets | note |
| -------- | -------- | -------- | ------ | ------- | ------------- | --------------- | ---- |

### `fonts.csv`
| font_id | rel_path | family | size_px | weight | mono | used_in_files | note |
| ------- | -------- | ------ | ------- | ------ | ---- | ------------- | ---- |

### `styles.csv`
| style_id | file | widget_class | prop | value | scope | theme | note |
| -------- | ---- | ------------ | ---- | ----- | ----- | ----- | ---- |

### `locales.csv`
| locale | key | text | source_file | line | context |
| ------ | --- | ---- | ----------- | ---- | ------- |

### `sounds.csv`
| sound_id | rel_path | format | length_ms | used_in_files | note |
| -------- | -------- | ------ | --------- | ------------- | ---- |

### `shaders.csv`
| shader_id | rel_path | type | entry | uniforms | used_in_files | note |
| --------- | -------- | ---- | ----- | -------- | ------------- | ---- |

### `ui_asset_usage.csv`
| widget_path | widget_class | prop | value | asset_rel_path | resolved_asset_id | source_file | line |
| ----------- | ------------ | ---- | ----- | -------------- | ----------------- | ----------- | ---- |

## Datasets (podgląd)

```{csv-table} images
:header-rows: 1
:file: ./datasets/images.csv
:widths: auto
```

```{csv-table} fonts
:header-rows: 1
:file: ./datasets/fonts.csv
:widths: auto
```

```{csv-table} styles
:header-rows: 1
:file: ./datasets/styles.csv
:widths: auto
```

```{csv-table} locales
:header-rows: 1
:file: ./datasets/locales.csv
:widths: auto
```

```{csv-table} sounds
:header-rows: 1
:file: ./datasets/sounds.csv
:widths: auto
```

```{csv-table} shaders
:header-rows: 1
:file: ./datasets/shaders.csv
:widths: auto
```

```{csv-table} ui_asset_usage
:header-rows: 1
:file: ./datasets/ui_asset_usage.csv
:widths: auto
```

## Diagramy

### `data_flow.mmd`
```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
flowchart LR
  A[data/*] --> B[Indexer CSV]
  B --> C[Datasets]
  C --> D[UI Pages]
  B --> E[Crosslinks]
  D --> F[RAG]
```

### `asset_linking.mmd`
```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  I[OTUI property] -->|image-source/icon/font| ASSET[(Asset file)]
  ASSET --> INDEX[images.csv/fonts.csv/...]
  INDEX --> UI[Widgets Index]
```

{RAG_GUIDE_BLOCK}

{CODE_STANDARDS_BLOCK}

## Regexy pomocnicze (parsowanie OTUI)

```text
# image-source / icon
(?m)^(?:\s*)(image-source|icon)\s*:\s*([\w\/\.-]+)

# font
(?m)^(?:\s*)font\s*:\s*([\w\-]+)

# on<Hook>
(?m)^(?:\s*)[@&]on([A-Z][A-Za-z]+)\s*:\s*([\w\.]+)\(\)
```

## Kontrakty datasetów

Poniższe CSV są **źródłem prawdy** dla agentów. Każda kolumna jest obowiązkowa; puste wartości muszą być jawnie `""`.

### Images
*Facet:* [`11_data.images`](#facet-11_data.images)

Kolumny: `path, kind, width, height, theme, used_by_ui_ids, notes`  
- `path` – absolutny path w dokumentacji (`data/...` lub `layouts/...`), bez `file://`  
- `kind` – `png|jpg|svg|ico|gif`  
- `theme` – `light|dark|neutral|auto`  
- `used_by_ui_ids` – lista `ui_id` rozdzielona `;`  
- `notes` – dowolny komentarz

**Przykład:**

```csv
path,kind,width,height,theme,used_by_ui_ids,notes
data/images/topbuttons/skills.png,png,16,16,neutral,ui.skills_window;ui.topbar,Ikona przycisku "Skills"
```

### Fonts
*Facet:* [`11_data.fonts`](#facet-11_data.fonts)

`font_id,file,size,weight,mono,fallbacks` – definiuje rodzinę i parametry renderingu.

### Styles
*Facet:* [`11_data.styles`](#facet-11_data.styles)

`style_id,source_file,selector,property,value,resolved_asset`  
Zawiera parsowane reguły OTUI (np. `image-source`, `image-clip`, `color`, `font`), z opcjonalną kolumną `resolved_asset` po dereferencji layoutu.

**Katalog właściwości OTUI (wybór):**

- `image-source` (ścieżka rel. do `images/`, bez rozszerzenia)  
- `image-clip` (x y w h)  
- `image-border`, `image-color`  
- `icon`, `icon-color`, `icon-offset-x|y`  
- `font` (`font_id` z `fonts.csv`)  
- `color`, `background-color`, `border-color`  
- Pseudoklasy: `$hover`, `$disabled`, `$checked`, `$first`, `$!first`, `$on !checked` — **tworzą warianty**; zapisuj jako `selector` rozszerzony, np. `TabBarButton$hover`.

### Locales
*Facet:* [`11_data.locales`](#facet-11_data.locales)

`lang,key,value,source_file` – dane tłumaczeń wykorzystywane przez `tr('...')`.

**Konwencje kluczy:** `ui.<obszar>.<element>` np. `ui.skills.title`.

### Sounds
*Facet:* [`11_data.sounds`](#facet-11_data.sounds)

`path,duration_ms,channels,rate_hz,kind,used_by` – metadane plików audio i powiązania.

**Wskazówka:** jeśli `used_by` wiąże dźwięk z akcją (np. `ui.button`), dodaj crosslink do modułu wywołującego (`module_hooks.csv`).

### Shaders
*Facet:* [`11_data.shaders`](#facet-11_data.shaders)

`name,type,file,uniforms,includes` – np. `type: fragment|vertex`.  
**Uniformy** zapisuj rozdzielone `;`, np. `u_strength;u_threshold`.

### UI Asset Usage
*Facet:* [`11_data.ui_asset_usage`](#facet-11_data.ui_asset_usage)

`ui_id,ui_file,widget_path,prop,value,asset_path,resolved_path,notes` – łączy właściwości OTUI (np. `image-source`, `font`, `icon`) z zasobami z `data/**` lub `layouts/**`.

**Źródła ekstrakcji:** wszystkie `*.otui` oraz style dziedziczone przez `<` (np. `TabBarButton < UIButton`).

## OTUI → Assets: reguły i przykłady

Przykładowe fragmenty i sposób wypełnienia `ui_asset_usage.csv`:

```otui
TabBarButton < UIButton
  size: 17 18
  image-source: /images/ui/tabbutton_square
  image-color: #dfdfdf
  image-clip: 0 0 98 18
  image-border: 3
  icon-color: #dfdfdf
  color: #dfdfdf
```

**Mapa ekstrakcji:**

- `prop=image-source` → `value=/images/ui/tabbutton_square` → `asset_path=data/images/ui/tabbutton_square.png` (lub `layouts/...`) → `resolved_path`.
- `prop=font` → link do `fonts.csv`.
- Kolory → `styles.csv` (jako zwykłe reguły, bez `resolved_asset`).

Kolejny fragment (okno umiejętności):

```otui
MiniWindow
  id: skillWindow
  !text: tr('Skills')
  icon: /images/topbuttons/skills
  @onClose: modules.game_skills.onMiniWindowClose()
```

**Ekstrakcja:** `ui_id=skillWindow`, asset `icon` oraz tłumaczenie z `locales`.

## Diagramy

### data_overview
*Facet:* [`11_data.data_overview`](#facet-11_data.data_overview)

```{{mermaid}}
%%{{init: {{ 'theme': 'neutral' }} }}%%
graph TD
    DATA[data/**] --> IMAGES[images/**]
    DATA --> FONTS[fonts/**]
    DATA --> STYLES[styles/**]
    DATA --> LOCALES[locales/**]
    DATA --> SHADERS[shaders/**]
    DATA --> SOUNDS[sounds/**]
    LAYOUTS[layouts/<name>/**] -->|override| IMAGES
    LAYOUTS -->|override| STYLES
    LAYOUTS -->|override| SHADERS
```

### asset_to_ui
*Facet:* [`11_data.asset_to_ui`](#facet-11_data.asset_to_ui)

```{{mermaid}}
%%{{init: {{ 'theme': 'neutral' }} }}%%
graph TD
    A[/OTUI property/] -->|image-source| B[images.csv]
    A -->|font| C[fonts.csv]
    A -->|icon| B
    B -->|resolved→| D((ui_asset_usage.csv))
    C -->|resolved→| D
    click B "./index.html#facet-11_data.images" "Open images"
    click C "./index.html#facet-11_data.fonts" "Open fonts"
    click D "./index.html#facet-11_data.ui_asset_usage" "Open usage"
```

## Heurystyki ekstrakcji (dla Agenta)

1. **Dziedziczenie**: `Child < Parent` → przepisz właściwości `Parent`, a następnie nadpisz tym, co w `Child`.
2. **Pseudoklasy**: każda sekcja `$state:` to osobny rekord `styles.csv` (dopisz sufiks do `selector`).
3. **Ścieżki bez rozszerzenia**: do `image-source` dopisuj `.png` (chyba że wykryto inny format w `images/`).
4. **Layouts**: sprawdź `layouts/<active>/...` i jeśli istnieje, ustaw `resolved_path` na layout.
5. **Tłumaczenia**: `!text: tr('Key')` → poszukaj `Key` w `locales/*.json`.

## RAG & chunking

- Podział na **H2–H4** z **overlap ≈ 10%**, **≤1200 tokenów**.
- Nie przecinaj tabel CSV ani bloków `otui`.
- Dodaj *See also* między 11_data ↔ 04_ui ↔ 12_otmod.

## QA (minimalne)

- `link-lint`: linki względne poprawne
- `diagram-lint`: każdy `.mmd` z init headerem
- `dataset sanity`: komplet nagłówków, brak `NaN`
- `idempotency`: drugi przebieg = 0 zmian

## FAQ

**Czy muszę duplikować wpisy dla layoutów?**  
Nie — agent tworzy override automatycznie (zapisując oryginał w `note`, jeśli potrzeba).

**Jak łączyć assety z UI bez ręcznego mapowania?**  
Użyj `ui_asset_usage.csv`; to automatyczna projekcja z OTUI.

**Co z ciemnym motywem?**  
Dodaj `image-color` / alternatywną bitmapę lub styl warunkowy `theme: dark`.

## See also

- `04_ui` – OTUI i widgety
- `12_otmod` – powiązania modułów → UI
- `05_events` – eventy powiązane z interakcją UI

## Appendix / Facets

(facet-11_data.images)=
### Facet: `11_data.images`
Type: dataset

(facet-11_data.fonts)=
### Facet: `11_data.fonts`
Type: dataset

(facet-11_data.styles)=
### Facet: `11_data.styles`
Type: dataset

(facet-11_data.locales)=
### Facet: `11_data.locales`
Type: dataset

(facet-11_data.sounds)=
### Facet: `11_data.sounds`
Type: dataset

(facet-11_data.shaders)=
### Facet: `11_data.shaders`
Type: dataset

(facet-11_data.ui_asset_usage)=
### Facet: `11_data.ui_asset_usage`
Type: dataset

(facet-11_data.data_overview)=
### Facet: `11_data.data_overview`
Type: diagram

(facet-11_data.asset_to_ui)=
### Facet: `11_data.asset_to_ui`
Type: diagram
