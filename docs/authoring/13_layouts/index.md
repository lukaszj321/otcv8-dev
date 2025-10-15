---
doc_id: "authoring.13_layouts.index"
source_path: "layouts/**"
source_sha: "HEAD"
last_sync_iso: "2025-10-15T22:21:56Z"
doc_class: "guide"
language: "pl"
title: "Layouts — Override assetów i motywy wizualne"
summary: "Kompleksowy system layoutów OTClient v8: mechanizm override zasobów, struktura katalogów, wsparcie motywów (retro, mobile) i integracja z data/."
tags: ["otclient", "layouts", "themes", "overrides", "assets", "ui", "rag"]
---

# Layouts — Override assetów i motywy wizualne

**Cel rozdziału:** Udokumentować system layoutów OTClient v8 umożliwiający override zasobów z `data/**` przez alternatywne wersje w `layouts/<name>/**`, wspierający motywy wizualne (retro, mobile) i dynamiczne przełączanie w runtime.

```{contents} Spis treści
:depth: 3
:local:
```

:::{admonition} TL;DR
:class: tip
Layouty to warstwy nadpisujące `data/**` z zachowaniem identycznej struktury ścieżek. Aktywny layout ma priorytet przy rozwiązywaniu ścieżek zasobów.
:::

## Wprowadzenie domenowe

System layoutów w OTClient v8 implementuje **strategię override** dla zasobów statycznych (obrazy, style OTUI, fonty, dźwięki, shadery). Umożliwia:

1. **Warianty wizualne** - różne palety kolorów, ikony, ramki UI
2. **Adaptacja platformowa** - mobile (większe przyciski), desktop (kompaktowy UI)
3. **Tematyka eventowa** - retro style, święta, eventy specjalne
4. **A/B testing** - testowanie nowych designów bez modyfikacji kodu

### Mechanizm działania

```
# Zapytanie o asset
g_resources.resolvePath('/images/ui/button.png')

# Resolution algorithm
1. Sprawdź: layouts/<active_layout>/images/ui/button.png
2. Jeśli istnieje → zwróć ścieżkę z layoutu
3. W przeciwnym razie → zwróć data/images/ui/button.png
```

### Katalogi layoutów

Aktualnie dostępne:
- **`retro/`** - pixel-art style, klasyczne UI Tibia
- **`mobile/`** - większe przyciski, scroll bars, uproszczone menu

## Architektura / Przepływ

### Diagram organizacji layoutów

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    ROOT[layouts/**]
    ROOT --> RETRO[retro/<br/>105 overrides]
    ROOT --> MOBILE[mobile/<br/>5 overrides]
    
    RETRO --> RETRO_IMG[images/**]
    RETRO --> RETRO_STY[styles/**]
    
    MOBILE --> MOBILE_STY[styles/**]
    
    DATA[data/**<br/>baseline assets]
    
    RETRO_IMG -->|overrides| DATA
    RETRO_STY -->|overrides| DATA
    MOBILE_STY -->|overrides| DATA
    
    click ROOT "./index.html#facet-13_layouts.layout_index" "Zobacz layouty"
    click DATA "./../11_data/index.html" "Zobacz data"
```

### Diagram resolution override

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
sequenceDiagram
    participant UI as UIWidget
    participant RM as ResourceManager
    participant LAY as layouts/retro/**
    participant DATA as data/**
    
    UI->>RM: load("/images/ui/button.png")
    RM->>LAY: exists("images/ui/button.png")?
    
    alt Layout active & override exists
        LAY-->>RM: layouts/retro/images/ui/button.png
        RM-->>UI: Image loaded (override)
    else No override
        RM->>DATA: load("images/ui/button.png")
        DATA-->>RM: data/images/ui/button.png
        RM-->>UI: Image loaded (default)
    end
```

### Diagram przełączania layoutów

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd' } }}%%
flowchart LR
    A[User selects layout]
    B[g_resources.setLayout name]
    C[Reload UI widgets]
    D[Clear texture cache]
    E[Reparse OTUI styles]
    F[Layout active]
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
```

## Datasets

### layout_index.csv — Katalog layoutów

*Facet:* [`13_layouts.layout_index`](#facet-13_layouts.layout_index)

Lista dostępnych layoutów z metadanymi.

| layout | description | priority | author | overrides_count | images | styles | fonts | sounds | status |
|---|---|---|---|---|---|---|---|---|---|
| retro | Pixel-art retro style inspired by classic Tibia | 100 | OTClient Team | 105 | 95 | 17 | 0 | 0 | stable |
| mobile | Touch-friendly UI for mobile devices | 90 | OTClient Team | 5 | 0 | 5 | 0 | 0 | stable |

```{csv-table} layout_index
:header-rows: 1
:file: ./datasets/layout_index.csv
:widths: auto
```

**Priorytety:**
- Wyższy priority = preferowany przy konfliktach
- `100` - production ready
- `90` - beta
- `50` - alpha/experimental

### layout_overrides.csv — Mapowanie override

*Facet:* [`13_layouts.layout_overrides`](#facet-13_layouts.layout_overrides)

Szczegółowa lista nadpisań per layout.

| layout | kind | source_path | override_path | status | compatibility | note |
|---|---|---|---|---|---|---|
| retro | image | data/images/background.png | layouts/retro/images/background.png | applied | 100% | pixel-art background |
| retro | image | data/images/ui/button.png | layouts/retro/images/ui/button.png | applied | 100% | retro button sprite |
| retro | style | data/styles/10-buttons.otui | layouts/retro/styles/10-buttons.otui | applied | 100% | adjusted margins |
| mobile | style | data/styles/10-scrollbars.otui | layouts/mobile/styles/10-scrollbars.otui | applied | 100% | larger scrollbar |
| mobile | style | data/styles/30-miniwindow.otui | layouts/mobile/styles/30-miniwindow.otui | applied | 100% | touch-friendly sizing |

```{csv-table} layout_overrides (próbka)
:header-rows: 1
:file: ./datasets/layout_overrides.csv
:widths: auto
```

**Status values:**
- `applied` - override aktywny
- `missing` - plik w layoutcie brakuje
- `format_mismatch` - incompatible format/dimensions
- `deprecated` - do usunięcia

### layout_images.csv — Obrazy per layout

*Facet:* [`13_layouts.layout_images`](#facet-13_layouts.layout_images)

Metadane obrazów w layoutach.

| layout | image_path | width | height | format | theme | used_by | note |
|---|---|---|---|---|---|---|---|
| retro | images/background.png | 800 | 600 | png | dark | EntryUI | pixel-art tło |
| retro | images/ui/button.png | 98 | 80 | png | retro | UIButton | 4 stany w pionie |
| retro | images/topbuttons/skills.png | 96 | 22 | png | retro | TopButton | ikona umiejętności |
| mobile | - | - | - | - | - | - | tylko style overrides |

```{csv-table} layout_images
:header-rows: 1
:file: ./datasets/layout_images.csv
:widths: auto
```

## Blueprints — Wzorce layoutów

### Blueprint 1: Minimalny layout (tylko style)

**Struktura:**
```
layouts/
  minimal/
    styles/
      10-buttons.otui
      20-scrollbars.otui
```

**Style override (`styles/10-buttons.otui`):**
```yaml
Button < UIButton
  size: 106 24
  
  # Override tylko koloru, nie sprite'a
  color: #00ff00
  
  $hover:
    color: #00ff00
  
  $pressed:
    color: #00cc00
```

**Aktywacja:**
```lua
g_resources.setLayout('minimal')
```

### Blueprint 2: Kompletny layout (images + styles)

**Struktura:**
```
layouts/
  custom/
    images/
      background.png
      ui/
        button.png
        window.png
      topbuttons/
        skills.png
    styles/
      10-buttons.otui
      10-windows.otui
```

**Style z custom image (`styles/10-buttons.otui`):**
```yaml
Button < UIButton
  size: 106 24
  
  # Używa override image z layouts/custom/images/ui/button.png
  image-source: /images/ui/button.png
  image-border: 3
  image-clip: 0 0 106 24
  
  font: verdana-11px-antialised
  color: #c0c0c0
  
  $hover:
    image-clip: 0 24 106 24
    color: #ffffff
  
  $pressed:
    image-clip: 0 48 106 24
  
  $disabled:
    image-clip: 0 72 106 24
    color: #808080
```

### Blueprint 3: Layout z konfiguracją

**Plik konfiguracji (`layouts/custom/config.lua`):**
```lua
Layout = {
  name = "custom",
  description = "Custom theme with dark mode",
  author = "Developer",
  version = "1.0",
  
  features = {
    darkMode = true,
    highContrast = false,
    largeText = false
  },
  
  colors = {
    primary = "#00ff00",
    secondary = "#0088ff",
    background = "#1a1a1a",
    text = "#ffffff"
  }
}

return Layout
```

**Użycie w kodzie:**
```lua
local layoutConfig = g_resources.loadLayoutConfig('custom')
if layoutConfig.features.darkMode then
  applyDarkModeStyles()
end
```

### Blueprint 4: Conditional override (responsive)

**Skrypt wyboru layoutu (`init.lua`):**
```lua
-- Auto-select layout based on platform
function selectLayoutForPlatform()
  local platform = g_platform.getPlatformType()
  
  if platform == 'android' or platform == 'ios' then
    g_resources.setLayout('mobile')
  elseif g_window.getWidth() < 1024 then
    g_resources.setLayout('mobile')
  else
    g_resources.setLayout('retro')  -- default desktop
  end
end

-- Apply on startup
connect(g_app, { onRun = selectLayoutForPlatform })

-- Reapply on window resize
connect(g_window, { onResize = selectLayoutForPlatform })
```

### Blueprint 5: A/B testing layouts

**Test framework:**
```lua
LayoutABTest = {}

function LayoutABTest.init()
  -- Losowy wybór layoutu dla nowych użytkowników
  local userId = g_settings.getString('userId')
  local variant = hashUserId(userId) % 2
  
  if variant == 0 then
    g_resources.setLayout('variant_a')
    g_analytics.logEvent('layout_test', { variant = 'A' })
  else
    g_resources.setLayout('variant_b')
    g_analytics.logEvent('layout_test', { variant = 'B' })
  end
end

function LayoutABTest.logInteraction(action)
  local layout = g_resources.getCurrentLayout()
  g_analytics.logEvent('layout_interaction', {
    layout = layout,
    action = action,
    timestamp = os.time()
  })
end
```

## How-to / Playbook

### Procedura 1: Tworzenie nowego layoutu

**Krok 1:** Utwórz strukturę katalogów
```bash
mkdir -p layouts/my_theme/images/ui
mkdir -p layouts/my_theme/styles
```

**Krok 2:** Skopiuj asset do override
```bash
# Zachowaj identyczną ścieżkę jak w data/
cp data/images/ui/button.png layouts/my_theme/images/ui/button.png

# Edytuj w narzędziu graficznym (GIMP, Photoshop)
gimp layouts/my_theme/images/ui/button.png
```

**Krok 3:** Utwórz konfigurację (opcjonalnie)
```bash
cat > layouts/my_theme/config.lua << 'EOF'
Layout = {
  name = "my_theme",
  description = "My custom theme",
  author = "Me",
  version = "1.0"
}
return Layout
EOF
```

**Krok 4:** Aktywuj layout
```lua
-- W konsoli klienta lub init.lua
g_resources.setLayout('my_theme')
```

**Krok 5:** Weryfikacja
```lua
-- Sprawdź rozwiązane ścieżki
local path = g_resources.resolvePath('/images/ui/button.png')
print(path)  -- Powinno być: layouts/my_theme/images/ui/button.png
```

### Procedura 2: Override tylko stylów OTUI

**Krok 1:** Skopiuj style do layoutu
```bash
mkdir -p layouts/style_only/styles
cp data/styles/10-buttons.otui layouts/style_only/styles/
```

**Krok 2:** Zmodyfikuj właściwości (nie sprite)
```yaml
# layouts/style_only/styles/10-buttons.otui
Button < UIButton
  # Nie zmieniaj image-source (używa domyślnego z data/)
  # Zmień tylko właściwości wizualne
  
  color: #ff00ff  # Nowy kolor tekstu
  margin: 10      # Większe marginesy
  
  $hover:
    color: #ff88ff
```

**Krok 3:** Testuj
```lua
g_resources.setLayout('style_only')
-- Przyciski powinny mieć nowy kolor, ale ten sam sprite
```

### Procedura 3: Przełączanie layoutów w runtime

**Implementacja UI:**
```lua
-- W module options
function OptionsModule.createLayoutSelector()
  local layoutCombo = g_ui.createWidget('ComboBox', parent)
  
  -- Wypełnij dostępnymi layoutami
  local layouts = g_resources.getAvailableLayouts()
  for _, layout in ipairs(layouts) do
    layoutCombo:addOption(layout)
  end
  
  -- Ustaw aktualny
  layoutCombo:setCurrentOption(g_resources.getCurrentLayout())
  
  -- Handler zmiany
  layoutCombo.onOptionChange = function(widget, option)
    g_resources.setLayout(option)
    
    -- Reload UI
    g_modules.reloadModule('game_interface')
    
    -- Zapisz preferencję
    g_settings.set('layout', option)
  end
end
```

### Procedura 4: Debugging brakujących overrides

**Krok 1:** Włącz verbose logging
```lua
g_logger.setLevel(LogDebug)
g_resources.setDebugOverrides(true)
```

**Krok 2:** Monitoruj logi
```lua
-- Sprawdź które assety są override, a które nie
g_resources.onAssetResolve = function(requestedPath, resolvedPath)
  local isOverride = string.match(resolvedPath, '^layouts/')
  if isOverride then
    print('[Override] ' .. requestedPath .. ' -> ' .. resolvedPath)
  else
    print('[Default] ' .. requestedPath .. ' -> ' .. resolvedPath)
  end
end
```

**Krok 3:** Weryfikuj wymiary
```lua
-- Sprawdź czy override ma te same wymiary co oryginał
local original = g_textures.getTexture('/images/ui/button.png', 'data')
local override = g_textures.getTexture('/images/ui/button.png', 'layouts/retro')

if original:getSize() ~= override:getSize() then
  print('[WARNING] Size mismatch: ' .. original:getSize() .. ' vs ' .. override:getSize())
end
```

### Procedura 5: Migracja layoutu na nową wersję

**Krok 1:** Porównaj struktury
```bash
# Lista zmian w data/ od ostatniej wersji
git diff v1.0..v2.0 --name-only data/images/
git diff v1.0..v2.0 --name-only data/styles/
```

**Krok 2:** Identyfikuj missing overrides
```bash
# Sprawdź które pliki z data/ nie mają overrides w layoutcie
comm -23 <(find data/images -type f | sort) <(find layouts/retro/images -type f | sed 's/layouts\/retro\///g' | sort)
```

**Krok 3:** Aktualizuj overrides
```bash
# Dla każdego nowego assetu w data/, zdecyduj czy potrzebny override
for file in $(comm -23 ...); do
  echo "New asset: $file"
  echo "Create override? (y/n)"
  read answer
  if [ "$answer" = "y" ]; then
    mkdir -p "layouts/retro/$(dirname $file)"
    cp "data/$file" "layouts/retro/$file"
    # Edit in graphic tool
  fi
done
```

**Krok 4:** Testuj kompatybilność
```lua
-- Załaduj layout i sprawdź błędy
g_resources.setLayout('retro')
g_modules.reloadModule('game_interface')

-- Sprawdź logi
g_logger.getLastErrors()
```

## Integracje / Pułapki

### Pułapka 1: Incompatible dimensions

**Problem:**
```yaml
# data/images/ui/button.png: 98x20
# layouts/retro/images/ui/button.png: 100x24  # BŁĄD: różne wymiary

# OTUI używa image-clip: 0 0 98 20
# Ale override ma 100x24 -> nieprawidłowy clipping
```

**Remedium:**
```bash
# Zawsze zachowuj identyczne wymiary
identify data/images/ui/button.png
# Output: 98x20

# Resize override do dopasowania
convert layouts/retro/images/ui/button.png -resize 98x20\! output.png
```

### Pułapka 2: Missing override dla sprite sheet

**Problem:**
```
# data/images/ui/button.png: 4 stany (98x80, 4x20px każdy)
# layouts/retro/images/ui/button.png: tylko 1 stan (98x20)

# OTUI próbuje użyć image-clip: 0 60 98 20 (stan 4)
# Ale override ma tylko 20px wysokości -> błąd
```

**Remedium:**
```
# Zawsze override pełny sprite sheet, nie pojedyncze stany
# Zachowaj strukturę: width x (height_per_state * num_states)
```

### Pułapka 3: Cache texture po zmianie layoutu

**Problem:**
```lua
g_resources.setLayout('retro')
-- Stare tekstury wciąż w cache!
-- UI pokazuje poprzednie obrazy
```

**Remedium:**
```lua
g_resources.setLayout('retro')
g_textures.clearCache()  -- Wymuś przeładowanie
g_modules.reloadModule('game_interface')  -- Reload UI
```

### Pułapka 4: Override tylko częściowy

**Problem:**
```
# Layout override tylko images/ui/button.png
# Ale nie override images/ui/button_rounded.png

# UI używa obu - wygląda niespójnie
```

**Remedium:**
```
# Zawsze override pełne zestawy powiązanych assetów
# Jeśli override button.png, to też button_rounded.png, button_square.png itd.
```

### Pułapka 5: Ścieżki względne w OTUI

**Problem:**
```yaml
# W layouts/retro/styles/10-buttons.otui
Button < UIButton
  image-source: button.png  # BŁĄD: ścieżka względna
```

**Remedium:**
```yaml
# Zawsze używaj ścieżek bezwzględnych (od data/ lub layouts/)
Button < UIButton
  image-source: /images/ui/button.png  # OK
```

## QA & Checklists

### Checklist: Nowy layout

- [ ] Nazwa layoutu: lowercase, snake_case, unikalna
- [ ] Struktura katalogów identyczna z `data/**`
- [ ] Wszystkie override mają identyczne wymiary jak oryginały
- [ ] Sprite sheets kompletne (wszystkie stany)
- [ ] Style OTUI używają ścieżek bezwzględnych
- [ ] Config.lua (opcjonalny) zawiera metadane
- [ ] Testowane: aktywacja, przełączanie, reload
- [ ] Dodane do `layout_index.csv` i `layout_overrides.csv`
- [ ] Dokumentacja w README.md w katalogu layoutu

### Checklist: Override assetu

- [ ] Asset w identycznej ścieżce jak w `data/`
- [ ] Format zgodny (PNG dla obrazów, OTUI dla stylów)
- [ ] Wymiary zgodne (lub wielokrotność dla sprite sheets)
- [ ] Kompatybilność z image-clip w OTUI
- [ ] Testowane z aktywnym layoutem
- [ ] Entry w `layout_overrides.csv`

### Checklist: Przełączanie layoutów

- [ ] Clear texture cache po zmianie
- [ ] Reload modułów UI (game_interface, etc.)
- [ ] Weryfikacja: wszystkie overrides załadowane
- [ ] Brak błędów w logach
- [ ] UI renderuje się prawidłowo

### Link-lint OK

```bash
python docs/authoring/_tools/link_lint.py --chapter 13_layouts
# Expected: 0 errors
```

### Diagram-lint OK

```bash
python docs/authoring/_tools/diagram_lint.py --chapter 13_layouts
# Expected: all diagrams have %%{init: ...}%% header
```

### Dataset-sanity OK

```bash
python docs/authoring/_tools/csv_schema_check.py --chapter 13_layouts
# Expected:
# - headers match schema
# - no empty rows
# - no NaN values
```

### Idempotency OK

```bash
python docs/authoring/_tools/layout_scanner.py --output /tmp/run1/
python docs/authoring/_tools/layout_scanner.py --output /tmp/run2/
diff -r /tmp/run1/ /tmp/run2/
# Expected: no differences
```

## See Also

### Crosslinks do innych rozdziałów

- **`11_data`** — Zasoby bazowe nadpisywane przez layouty
- **`04_ui`** — Widgety OTUI używające assetów z layoutów
- **`12_otmod`** — Moduły ładujące zasoby przez layouty

### Narzędzia

- `docs/authoring/_tools/layout_scanner.py` - skaner layoutów
- `g_resources.setLayout()` - API przełączania layoutów
- `g_resources.getAvailableLayouts()` - lista layoutów

## Appendix / Facets

(facet-13_layouts.layout_index)=
### Facet: `13_layouts.layout_index`
Type: dataset
Schema: `layout, description, priority, author, overrides_count, images, styles, fonts, sounds, status`

(facet-13_layouts.layout_overrides)=
### Facet: `13_layouts.layout_overrides`
Type: dataset
Schema: `layout, kind, source_path, override_path, status, compatibility, note`

(facet-13_layouts.layout_images)=
### Facet: `13_layouts.layout_images`
Type: dataset
Schema: `layout, image_path, width, height, format, theme, used_by, note`

(facet-13_layouts.layout_organization)=
### Facet: `13_layouts.layout_organization`
Type: diagram
Format: mermaid (graph TD)

(facet-13_layouts.override_resolution)=
### Facet: `13_layouts.override_resolution`
Type: diagram
Format: mermaid (sequenceDiagram)
