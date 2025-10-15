
---
doc_id: "authoring.11_data.index"
source_path: "data/**"
source_sha: "HEAD"
last_sync_iso: "2025-10-15T22:21:56Z"
doc_class: "guide"
language: "pl"
title: "Data — Zasoby statyczne i struktura assetów"
summary: "Kompletny inwentarz zasobów statycznych OTClient v8: obrazy, fonty, style OTUI, lokalizacje, dźwięki i shadery wraz z wzorcami użycia i integracją z UI."
tags: ["otclient", "data", "assets", "images", "fonts", "styles", "locales", "sounds", "shaders", "otui", "rag"]
---

# Data — Zasoby statyczne i struktura assetów

**Cel rozdziału:** Udokumentować pełną strukturę katalogu `data/**` zawierającą wszystkie zasoby statyczne OTClient v8 (obrazy, fonty, style OTUI, lokalizacje, dźwięki, shadery) wraz z ich wykorzystaniem w UI i możliwościami nadpisania przez layouty.

```{contents} Spis treści
:depth: 3
:local:
```

:::{admonition} TL;DR
:class: tip
Katalog `data/**` zawiera podstawowe zasoby aplikacji. Wszystkie ścieżki są względne do tego katalogu. Layouty (`layouts/<name>/**`) mogą nadpisać dowolny asset zachowując identyczną strukturę ścieżek.
:::

## Wprowadzenie domenowe

Katalog `data/**` stanowi **repozytorium źródłowe** dla wszystkich zasobów statycznych używanych przez OTClient v8. W przeciwieństwie do kodu Lua czy C++, zasoby te nie są kompilowane - są ładowane w runtime przez odpowiednie moduły (renderer graficzny, system audio, parser OTUI).

### Podstawowa organizacja

Struktura `data/**` jest podzielona tematycznie na 7 głównych podkatalogów:

1. **images/** - bitmapy PNG (ikony, sprite'y UI, tła, elementy gry)
2. **fonts/** - definicje fontów w formacie `.otfont` (bitmap fonts)
3. **styles/** - style OTUI (`.otui`) definiujące wygląd widgetów
4. **locales/** - pliki lokalizacji (`.lua`) z tłumaczeniami tekstów
5. **sounds/** - efekty dźwiękowe (`.ogg`) dla eventów gry
6. **shaders/** - programy shaderów (vertex/fragment) dla efektów wizualnych
7. **cursors/** - kursory myszy (PNG)

### Mechanizm ładowania

Assets są rozwiązywane (resolved) przez `ResourceManager` zgodnie z algorytmem:

1. Jeśli aktywny layout: sprawdź `layouts/<name>/<path>`
2. W przeciwnym razie: użyj `data/<path>`
3. Jeśli nie znaleziono: fallback lub błąd

Ta strategia umożliwia **całkowite przekształcenie wyglądu** aplikacji bez modyfikacji kodu.

## Architektura / Przepływ

### Diagram organizacji zasobów

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    ROOT[data/**]
    ROOT --> IMAGES[images/**<br/>~300 PNG files]
    ROOT --> FONTS[fonts/**<br/>11 bitmap fonts]
    ROOT --> STYLES[styles/**<br/>33 OTUI styles]
    ROOT --> LOCALES[locales/**<br/>6 languages]
    ROOT --> SOUNDS[sounds/**<br/>8 OGG files]
    ROOT --> SHADERS[shaders/**<br/>8 GLSL programs]
    ROOT --> CURSORS[cursors/**<br/>cursor sprites]
    
    IMAGES --> IMG_UI[ui/]
    IMAGES --> IMG_GAME[game/]
    IMAGES --> IMG_TOP[topbuttons/]
    IMAGES --> IMG_FLAGS[flags/]
    
    STYLES --> STY_BASE[10-*.otui<br/>base widgets]
    STYLES --> STY_COMP[20-*.otui<br/>composite]
    STYLES --> STY_FEAT[30-*.otui<br/>features]
    STYLES --> STY_GAME[40-*.otui<br/>game modules]
    
    click IMAGES "#facet-11_data.images" "Zobacz katalog images"
    click FONTS "#facet-11_data.fonts" "Zobacz katalog fonts"
    click STYLES "#facet-11_data.styles" "Zobacz katalog styles"
```

### Diagram ładowania assetu

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
sequenceDiagram
    participant UI as UIWidget
    participant RM as ResourceManager
    participant LAY as layouts/<name>/**
    participant DATA as data/**
    
    UI->>RM: load("images/ui/button.png")
    RM->>LAY: exists("images/ui/button.png")?
    alt Layout active & file exists
        LAY-->>RM: layouts/retro/images/ui/button.png
        RM-->>UI: Image loaded (layout override)
    else No layout or file missing
        RM->>DATA: load("images/ui/button.png")
        DATA-->>RM: data/images/ui/button.png
        RM-->>UI: Image loaded (default)
    end
```

### Diagram zależności OTUI → Assets

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd' } }}%%
graph LR
    A[styles/10-buttons.otui]
    B[images/ui/button.png]
    C[images/ui/button_rounded.png]
    D[fonts/verdana-11px-antialised.otfont]
    
    A -->|image-source| B
    A -->|image-source| C
    A -->|font| D
    
    E[modules/game_buttons/buttons.otui]
    E -->|@onLoad| A
    E -->|icon refs| F[images/topbuttons/*.png]
    
    click A "#facet-11_data.styles" "Zobacz styles"
    click B "#facet-11_data.images" "Zobacz images"
```

## Datasets

### images.csv — Katalog obrazów

*Facet:* [`11_data.images`](#facet-11_data.images)

Tabela zawiera pełny spis obrazów PNG z katalogu `data/images/**` wraz z informacjami o wykorzystaniu w UI.

| asset_id | rel_path | category | format | size_px | used_in_files | used_in_widgets | note |
|---|---|---|---|---|---|---|---|
| img.ui.button | images/ui/button.png | ui_widget | png | 98x20 | styles/10-buttons.otui | UIButton | podstawowy przycisk |
| img.ui.button_rounded | images/ui/button_rounded.png | ui_widget | png | 98x20 | styles/10-buttons.otui | UIButton | zaokrąglony przycisk |
| img.ui.tabbutton_square | images/ui/tabbutton_square.png | ui_widget | png | 98x18 | styles/20-tabbars.otui | TabBarButton | kwadratowa zakładka |
| img.ui.window | images/ui/window.png | ui_container | png | 128x128 | styles/10-windows.otui | UIWindow | ramka okna 9-patch |
| img.ui.panel_flat | images/ui/panel_flat.png | ui_container | png | 32x32 | styles/10-panels.otui | UIPanel | płaski panel |
| img.topbuttons.skills | images/topbuttons/skills.png | icon | png | 96x22 | modules/game_skills | TopButton | ikona umiejętności |
| img.topbuttons.inventory | images/topbuttons/inventory.png | icon | png | 96x22 | modules/game_inventory | TopButton | ikona ekwipunku |
| img.game.slots.head | images/game/slots/head.png | game_ui | png | 34x34 | game_inventory | InventorySlot | slot na hełm |
| img.game.actionbarslot | images/game/actionbarslot.png | game_ui | png | 34x34 | game_actionbar | ActionBarSlot | slot paska akcji |
| img.flags.en | images/flags/en.png | icon | png | 32x32 | client_locales | FlagButton | flaga języka EN |

```{csv-table} images (próbka)
:header-rows: 1
:file: ./datasets/images.csv
:widths: auto
```

**Uwagi implementacyjne:**
- PNG z kanałem alpha (RGBA)
- Sprite'y używające `image-clip` muszą mieć dokładne wymiary (width×height)
- Nazwy plików: lowercase, snake_case, bez spacji
- 9-patch sprites: border zdefiniowany w OTUI (np. `border: 4`)

### fonts.csv — Katalog fontów

*Facet:* [`11_data.fonts`](#facet-11_data.fonts)

Fonty w formacie `.otfont` (bitmap font z teksturą PNG i plikiem definiującym glify).

| id | family | size | style | path | otui_ref | usage |
|---|---|---|---|---|---|---|
| verdana-11px-antialised | Verdana | 11px | antialised | fonts/verdana-11px-antialised.otfont | UILabel, UIButton | domyślny font UI |
| verdana-11px-rounded | Verdana | 11px | rounded | fonts/verdana-11px-rounded.otfont | UIWindow | font nagłówków okien |
| verdana-9px | Verdana | 9px | normal | fonts/verdana-9px.otfont | UIConsole | font czatu i konsoli |
| terminus-14px-bold | Terminus | 14px | bold | fonts/terminus-14px-bold.otfont | UILabel | font nagłówków |
| cipsoftFont | CipSoft | 11px | normal | fonts/cipsoftFont.otfont | UILabel | klasyczny font Tibia |

```{csv-table} fonts (próbka)
:header-rows: 1
:file: ./datasets/fonts.csv
:widths: auto
```

**Struktura pliku `.otfont`:**
```yaml
Font:
  name: verdana-11px-antialised
  size: 11
  texture: verdana-11px.png
  glyph-spacing: 1
  space-width: 4
  height: 15
  
  # Definicje glifów (A-Z, 0-9, znaki specjalne)
  Glyph:
    char: A
    rect: 0 0 8 11
```

### styles.csv — Katalog stylów OTUI

*Facet:* [`11_data.styles`](#facet-11_data.styles)

Style definiują wygląd widgetów (kolory, obrazy, marginesy, layout).

| style_id | widget_type | source_file | priority | properties_count | images_used | note |
|---|---|---|---|---|---|---|
| Button | UIButton | styles/10-buttons.otui | 10 | 12 | button.png, button_rounded.png | podstawowy styl przycisków |
| RoundedButton | UIButton | styles/10-buttons.otui | 10 | 8 | button_rounded.png | przycisk zaokrąglony |
| TabButton | TabBarButton | styles/20-tabbars.otui | 20 | 10 | tabbutton_square.png | przycisk zakładki |
| Window | UIWindow | styles/10-windows.otui | 10 | 15 | window.png | ramka okna |
| MiniWindow | UIMiniWindow | styles/30-miniwindow.otui | 30 | 18 | miniwindow.png | małe okno gry |
| Panel | UIPanel | styles/10-panels.otui | 10 | 6 | panel_flat.png | płaski panel |
| GameButton | GameButton | styles/40-gamebuttons.otui | 40 | 14 | button_topgame.png | przyciski top bar w grze |

```{csv-table} styles (próbka)
:header-rows: 1
:file: ./datasets/styles.csv
:widths: auto
```

**Hierarchia priorytetów (numery prefixów):**
- `10-*.otui` - style bazowe widgetów (buttons, windows, panels)
- `20-*.otui` - kompozyty (tabbars, scrollbars, spinboxes)
- `30-*.otui` - funkcje specjalne (miniwindows, messageboxes)
- `40-*.otui` - moduły gry (inventory, console, minimap)

### locales.csv — Katalog lokalizacji

*Facet:* [`11_data.locales`](#facet-11_data.locales)

Pliki tłumaczeń w formacie Lua (tabele key-value).

| lang_code | language | path | keys_count | status | coverage |
|---|---|---|---|---|---|
| en | English | locales/en.lua | 450 | complete | 100% |
| pl | Polski | locales/pl.lua | 448 | complete | 99.5% |
| pt | Português | locales/pt.lua | 445 | complete | 98.8% |
| es | Español | locales/es.lua | 442 | complete | 98.2% |
| de | Deutsch | locales/de.lua | 438 | partial | 97.3% |
| sv | Svenska | locales/sv.lua | 430 | partial | 95.5% |

```{csv-table} locales (próbka)
:header-rows: 1
:file: ./datasets/locales.csv
:widths: auto
```

**Przykład struktury pliku `en.lua`:**
```lua
Locale = {
  name = "English",
  languageName = "English",
  
  -- UI translations
  ["Login"] = "Login",
  ["Password"] = "Password",
  ["Character List"] = "Character List",
  ["Enter Game"] = "Enter Game",
  
  -- Game messages
  ["You have been killed by %s"] = "You have been killed by %s",
  ["Level advanced from %d to %d"] = "Level advanced from %d to %d",
  
  -- Errors
  ["Connection failed"] = "Connection failed",
  ["Invalid credentials"] = "Invalid credentials"
}
```

### sounds.csv — Katalog dźwięków

*Facet:* [`11_data.sounds`](#facet-11_data.sounds)

Efekty dźwiękowe w formacie OGG Vorbis.

| sound_id | path | channel | usage | loop | volume | duration_s | note |
|---|---|---|---|---|---|---|---|
| player_attack | sounds/Player_Attack.ogg | sfx | combat | false | 1.0 | 0.8 | dźwięk ataku gracza |
| low_health | sounds/Low_Health.ogg | alert | health_warning | true | 0.8 | 2.5 | alarm niskiego HP |
| low_mana | sounds/Low_Mana.ogg | alert | mana_warning | true | 0.8 | 2.5 | alarm niskiej many |
| private_message | sounds/Private_Message.ogg | notification | chat | false | 1.0 | 0.5 | powiadomienie PM |
| creature_detected | sounds/Creature_Detected.ogg | alert | bot_detection | false | 1.0 | 1.0 | wykryto stworzenie |
| alarm | sounds/alarm.ogg | alert | generic | true | 1.0 | 3.0 | alarm ogólny |

```{csv-table} sounds (próbka)
:header-rows: 1
:file: ./datasets/sounds.csv
:widths: auto
```

**Kanały audio:**
- `sfx` - efekty dźwiękowe gry
- `alert` - alarmy i ostrzeżenia
- `notification` - powiadomienia systemowe
- `ambient` - dźwięki otoczenia (nieużywane obecnie)

### shaders.csv — Katalog shaderów

*Facet:* [`11_data.shaders`](#facet-11_data.shaders)

Programy shaderów GLSL dla efektów wizualnych (map i outfitów).

| shader_id | vertex_path | fragment_path | target | defines | usage | note |
|---|---|---|---|---|---|---|
| map_default | shaders/map_default_vertex.frag | shaders/map_default_fragment.frag | map | - | default | podstawowy rendering mapy |
| map_rainbow | shaders/map_rainbow_vertex.frag | shaders/map_rainbow_fragment.frag | map | RAINBOW_EFFECT | cosmetic | efekt tęczy na mapie |
| outfit_default | shaders/outfit_default_vertex.frag | shaders/outfit_default_fragment.frag | outfit | - | default | podstawowy rendering postaci |
| outfit_rainbow | shaders/outfit_rainbow_vertex.frag | shaders/outfit_rainbow_fragment.frag | outfit | RAINBOW_EFFECT | cosmetic | efekt tęczy na postaci |

```{csv-table} shaders (próbka)
:header-rows: 1
:file: ./datasets/shaders.csv
:widths: auto
```

**Przykład shaderu (fragment):**
```glsl
// map_default_fragment.frag
#version 120
uniform sampler2D u_Tex0;
varying vec2 v_TexCoord;
varying vec4 v_Color;

void main() {
    vec4 texColor = texture2D(u_Tex0, v_TexCoord);
    gl_FragColor = texColor * v_Color;
}
```

### ui_asset_usage.csv — Mapowanie UI → Assets

*Facet:* [`11_data.ui_asset_usage`](#facet-11_data.ui_asset_usage)

Tabela pokazująca, które widgety używają których assetów.

| widget_id | widget_type | asset_type | asset_path | property | optional | note |
|---|---|---|---|---|---|---|
| Button | UIButton | image | images/ui/button.png | image-source | false | obowiązkowy sprite |
| Button | UIButton | font | fonts/verdana-11px-antialised.otfont | font | true | domyślny font |
| Window | UIWindow | image | images/ui/window.png | image-source | false | ramka 9-patch |
| TabButton | TabBarButton | image | images/ui/tabbutton_square.png | image-source | false | sprite zakładki |
| MiniWindow | UIMiniWindow | image | images/ui/miniwindow.png | image-source | false | ramka małego okna |

```{csv-table} ui_asset_usage (próbka)
:header-rows: 1
:file: ./datasets/ui_asset_usage.csv
:widths: auto
```

## Blueprints — Wzorce użycia assetów

### Blueprint 1: Definicja fontu OTUI

**Plik:** `data/fonts/custom-font-12px.otfont`

```yaml
Font:
  name: custom-font-12px
  size: 12
  texture: custom-font-12px.png
  glyph-spacing: 1
  space-width: 5
  height: 16
  
  # Definicje znaków (przykład)
  Glyph:
    char: A
    rect: 0 0 9 12
  
  Glyph:
    char: B
    rect: 9 0 9 12
  
  # ... (dalsze glify)
```

**Użycie w OTUI:**
```yaml
Label < UILabel
  font: custom-font-12px
  color: #ffffff
```

### Blueprint 2: Style OTUI wykorzystujący obrazy

**Plik:** `data/styles/10-custom-buttons.otui`

```yaml
CustomButton < UIButton
  size: 106 24
  
  image-source: /images/ui/button.png
  image-border: 3
  image-clip: 0 0 106 24
  
  font: verdana-11px-antialised
  text-offset: 0 0
  color: #c0c0c0
  
  $hover:
    image-clip: 0 24 106 24
    color: #ffffff
  
  $pressed:
    image-clip: 0 48 106 24
    text-offset: 1 1
  
  $disabled:
    color: #808080
    image-clip: 0 72 106 24
```

**Struktura sprite'a:** 
- Wysokość: 96px (4 stany × 24px)
- Stany: normal (0), hover (24), pressed (48), disabled (72)

### Blueprint 3: Konfiguracja lokalizacji

**Plik:** `data/locales/custom.lua`

```lua
Locale = {
  name = "Custom",
  languageName = "Custom Language",
  
  -- Podstawowe UI
  ["Login"] = "Zaloguj",
  ["Password"] = "Hasło",
  ["Enter Game"] = "Wejdź do gry",
  ["Options"] = "Opcje",
  
  -- Komunikaty gry
  ["You have %d hit points"] = "Masz %d punktów życia",
  ["Level advanced from %d to %d"] = "Awans z poziomu %d na %d",
  
  -- Błędy
  ["Connection failed"] = "Błąd połączenia",
  ["Invalid password"] = "Nieprawidłowe hasło"
}

return Locale
```

**Ładowanie:**
```lua
-- W module client_locales
g_locales.installLocale(locale)
g_locales.setLocale(locale)
```

### Blueprint 4: Shader z efektem specjalnym

**Vertex shader:** `data/shaders/custom_vertex.frag`

```glsl
#version 120
attribute vec2 a_Position;
attribute vec2 a_TexCoord;
attribute vec4 a_Color;

uniform mat3 u_TransformMatrix;
uniform mat3 u_ProjectionMatrix;

varying vec2 v_TexCoord;
varying vec4 v_Color;

void main() {
    gl_Position = vec4(u_ProjectionMatrix * u_TransformMatrix * vec3(a_Position, 1.0), 1.0);
    v_TexCoord = a_TexCoord;
    v_Color = a_Color;
}
```

**Fragment shader:** `data/shaders/custom_fragment.frag`

```glsl
#version 120
uniform sampler2D u_Tex0;
uniform float u_Time;

varying vec2 v_TexCoord;
varying vec4 v_Color;

void main() {
    vec4 texColor = texture2D(u_Tex0, v_TexCoord);
    
    // Efekt pulsowania
    float pulse = (sin(u_Time * 3.14) + 1.0) * 0.5;
    vec4 finalColor = texColor * v_Color;
    finalColor.rgb = mix(finalColor.rgb, vec3(1.0), pulse * 0.2);
    
    gl_FragColor = finalColor;
}
```

**Aktywacja w C++:**
```cpp
PainterShaderProgram* shader = g_painter->getShader("custom");
shader->bind();
shader->setUniformValue("u_Time", g_clock.seconds());
// ... render calls ...
shader->release();
```

### Blueprint 5: Dźwięk z triggerem w Lua

**Definicja w module:**
```lua
-- modules/game_audio/audio.lua
function playAlertSound(soundType)
    local sounds = {
        low_health = 'Low_Health.ogg',
        low_mana = 'Low_Mana.ogg',
        creature = 'Creature_Detected.ogg'
    }
    
    local soundFile = sounds[soundType]
    if soundFile then
        g_sounds.playSound('/sounds/' .. soundFile)
    end
end

-- Trigger na zmianę HP
function onHealthChange(localPlayer, health, maxHealth)
    local hpPercent = (health / maxHealth) * 100
    
    if hpPercent < 20 and not alertActive then
        playAlertSound('low_health')
        alertActive = true
    elseif hpPercent > 30 then
        alertActive = false
    end
end

connect(LocalPlayer, { onHealthChange = onHealthChange })
```

## How-to / Playbook

### Procedura 1: Dodanie nowego obrazu UI

**Krok 1:** Przygotuj asset PNG
```bash
# Wymagania
# - Format: PNG with alpha
# - Rozmiar: wielokrotność 2 (np. 32x32, 64x64, 96x24)
# - Nazwa: lowercase_with_underscores.png

# Umieść w odpowiednim podkatalogu
cp new_button.png data/images/ui/
```

**Krok 2:** Dodaj do stylu OTUI
```yaml
# data/styles/10-buttons.otui
NewButton < UIButton
  image-source: /images/ui/new_button.png
  size: 96 24
  image-border: 4
```

**Krok 3:** Testuj w module
```lua
-- modules/test/test.lua
local button = g_ui.createWidget('NewButton', parent)
button:setText('Test')
```

**Krok 4:** Weryfikacja
```bash
# Sprawdź logi czy asset został załadowany
# W konsoli klienta: brak błędów "unable to load"
```

### Procedura 2: Dodanie nowego języka

**Krok 1:** Utwórz plik lokalizacji
```bash
# Kopiuj szablon z en.lua
cp data/locales/en.lua data/locales/xx.lua
```

**Krok 2:** Przetłumacz klucze
```lua
-- data/locales/xx.lua
Locale = {
  name = "LanguageName",
  languageName = "Native Name",
  
  -- Tłumaczenia...
  ["Login"] = "Translated Login",
  -- ...
}

return Locale
```

**Krok 3:** Dodaj flagę
```bash
# Przygotuj PNG 32x32
cp flag_xx.png data/images/flags/xx.png
```

**Krok 4:** Zarejestruj w module
```lua
-- modules/client_locales/locales.lua
-- Plik automatycznie skanuje data/locales/*.lua
-- Wystarczy restart klienta
```

### Procedura 3: Nadpisanie assetu przez layout

**Krok 1:** Utwórz strukturę layoutu
```bash
mkdir -p layouts/custom/images/ui
mkdir -p layouts/custom/styles
```

**Krok 2:** Skopiuj asset z zachowaniem ścieżki
```bash
# Asset bazowy
# data/images/ui/button.png
# 
# Asset w layoutcie (identyczna ścieżka!)
cp custom_button.png layouts/custom/images/ui/button.png
```

**Krok 3:** Aktywuj layout
```lua
-- W module lub init.lua
g_resources.setLayout('custom')
```

**Krok 4:** Weryfikacja
```lua
-- Sprawdź rozwiązaną ścieżkę
local path = g_resources.resolvePath('/images/ui/button.png')
print(path)  -- Powinno być: layouts/custom/images/ui/button.png
```

### Procedura 4: Debugging brakujących assetów

**Krok 1:** Włącz verbose logging
```lua
-- W konsoli klienta
g_logger.setLevel(LogDebug)
```

**Krok 2:** Sprawdź logi załadowania
```bash
# Szukaj w logach:
grep "unable to load" otclient.log
grep "resource not found" otclient.log
```

**Krok 3:** Weryfikuj ścieżki w OTUI
```yaml
# Prawidłowo (ścieżka bezwzględna od data/)
image-source: /images/ui/button.png

# Nieprawidłowo (ścieżka względna)
image-source: button.png  # NIE
```

**Krok 4:** Sprawdź case sensitivity
```bash
# Linux/Mac: rozróżnia wielkość liter
# Windows: nie rozróżnia

# Zawsze używaj lowercase
images/UI/Button.png  # BŁĄD
images/ui/button.png  # OK
```

### Procedura 5: Optymalizacja zasobów

**Krok 1:** Kompresja PNG
```bash
# Użyj optipng lub pngcrush
optipng -o7 data/images/**/*.png

# Lub pngquant dla lossy compression
pngquant --quality=80-95 data/images/**/*.png
```

**Krok 2:** Atlas tekstur (dla zaawansowanych)
```python
# Połącz małe obrazy w większe atlasy
# Generuj image-clip w OTUI
python tools/generate_atlas.py data/images/ui/ --output ui_atlas.png
```

**Krok 3:** Lazy loading fontów
```lua
-- Nie ładuj wszystkich fontów na starcie
-- Ładuj on-demand w modułach
function loadFontIfNeeded(fontName)
    if not g_fonts.fontExists(fontName) then
        g_fonts.importFont(fontName)
    end
end
```

**Krok 4:** Profilowanie
```lua
-- Zmierz czas ładowania
local start = g_clock.millis()
g_resources.loadAsset('/images/ui/button.png')
local elapsed = g_clock.millis() - start
print('Load time: ' .. elapsed .. 'ms')
```

## Integracje / Pułapki

### Pułapka 1: Case sensitivity ścieżek

**Problem:**
```lua
-- Windows: działa
g_textures.getTexture('/Images/UI/Button.png')

-- Linux/Mac: ERROR - plik nie znaleziony
```

**Remedium:**
- Zawsze używaj lowercase w nazwach plików
- Weryfikuj na Linux przed release
- Dodaj pre-commit hook:
```bash
# .git/hooks/pre-commit
find data/ -name '*[A-Z]*' | grep -q . && echo "ERROR: Uppercase in filenames" && exit 1
```

### Pułapka 2: Brak kanału alpha w PNG

**Problem:**
```
Obrazy bez alpha channel są renderowane z czarnym tłem
```

**Remedium:**
```bash
# Konwertuj do RGBA
convert image.png -alpha set output.png

# Lub w Photoshop/GIMP: Export as PNG-24 with transparency
```

### Pułapka 3: Image-clip poza granicami tekstury

**Problem:**
```yaml
# Tekstura: 100x100px
Button < UIButton
  image-source: /images/ui/button.png
  image-clip: 0 0 150 50  # BŁĄD: przekracza granice
```

**Remedium:**
```lua
-- Walidacja przed zastosowaniem
local texture = g_textures.getTexture(path)
local size = texture:getSize()
if clipRect.width > size.width or clipRect.height > size.height then
    error('Image clip exceeds texture bounds')
end
```

### Pułapka 4: Cykliczne zależności w stylach

**Problem:**
```yaml
# styles/10-buttons.otui
Button < RoundedButton  # ERROR: RoundedButton dziedziczy z Button
  # ...

RoundedButton < Button
  # ...
```

**Remedium:**
```yaml
# Użyj wspólnego przodka
BaseButton < UIButton
  # wspólne właściwości

Button < BaseButton
  # wariant 1

RoundedButton < BaseButton
  # wariant 2
```

### Pułapka 5: Fonts z niepełnym charset

**Problem:**
```
Font nie zawiera polskich znaków (ą, ć, ę, ł, ń, ó, ś, ź, ż)
Wyświetlane są jako "?" lub kwadraty
```

**Remedium:**
```yaml
# W .otfont dodaj missing glify
Glyph:
  char: ą
  rect: 200 0 8 12

# Lub wygeneruj ponownie z pełnym charset
# (użyj narzędzia do generowania bitmap fonts)
```

### Pułapka 6: Shader incompatibility

**Problem:**
```
Shader działa na Windows (DirectX), ale fail na Linux (OpenGL)
```

**Remedium:**
```glsl
// Użyj przenośnego GLSL
#version 120  // Nie używaj #version 330 bez fallback

// Unikaj:
out vec4 fragColor;  // GLSL 330+

// Zamiast:
// (wbudowane w GLSL 120)
gl_FragColor = ...
```

## QA & Checklists

### Checklist: Dodanie nowego assetu

- [ ] Asset umieszczony w prawidłowym podkatalogu `data/**`
- [ ] Nazwa pliku: lowercase, snake_case, bez spacji
- [ ] Format zgodny z typem (PNG dla obrazów, OGG dla dźwięków)
- [ ] Asset dodany do odpowiedniego CSV w `docs/authoring/11_data/datasets/`
- [ ] Jeśli obraz: sprawdzono wymiary i alpha channel
- [ ] Jeśli font: sprawdzono kompletność charset (A-Z, 0-9, znaki specjalne)
- [ ] Jeśli shader: przetestowano na OpenGL i DirectX
- [ ] Jeśli dźwięk: sprawdzono format (OGG Vorbis, mono/stereo, bitrate)
- [ ] Asset referencyjny w OTUI lub module (nie orphan)
- [ ] Brak błędów w logach przy ładowaniu

### Checklist: Override przez layout

- [ ] Layout struktura identyczna z `data/**` (ścieżki relatywne)
- [ ] Asset override zachowuje format i wymiary oryginału
- [ ] Sprawdzono kompatybilność z image-clip w OTUI
- [ ] Layout dodany do `docs/authoring/13_layouts/datasets/layout_overrides.csv`
- [ ] Przetestowano przełączanie layoutu w runtime
- [ ] Fallback do `data/**` działa jeśli asset brakuje w layoutcie

### Checklist: Integracja z UI

- [ ] Asset użyty w co najmniej jednym pliku OTUI
- [ ] Ścieżka w OTUI: bezwzględna `/images/...` (nie względna)
- [ ] Jeśli sprite sheet: image-clip zdefiniowany prawidłowo
- [ ] Jeśli font: charset pokrywa wymagane znaki (minimum ASCII)
- [ ] Jeśli shader: uniforms przekazywane poprawnie z C++
- [ ] Entry w `ui_asset_usage.csv` kompletny

### Link-lint OK

```bash
# Weryfikacja linków w datasets
python docs/authoring/_tools/link_lint.py --chapter 11_data
# Expected: 0 errors
```

### Diagram-lint OK

```bash
# Weryfikacja diagramów mermaid
python docs/authoring/_tools/diagram_lint.py --chapter 11_data
# Expected: all diagrams have %%{init: ...}%% header
```

### Dataset-sanity OK

```bash
# Weryfikacja integralności CSV
python docs/authoring/_tools/csv_schema_check.py --chapter 11_data
# Expected: 
# - headers match schema
# - no empty rows
# - no NaN values
```

### Idempotency OK

```bash
# Weryfikacja idempotencji generatora
python docs/authoring/_tools/data_asset_scan.py --output /tmp/run1/
python docs/authoring/_tools/data_asset_scan.py --output /tmp/run2/
diff -r /tmp/run1/ /tmp/run2/
# Expected: no differences
```

## See Also

### Crosslinks do innych rozdziałów

- **`04_ui`** — Widgety OTUI i style używające assetów z `data/**`
- **`13_layouts`** — Mechanizm override assetów przez layouty
- **`12_otmod`** — Moduły ładujące i używające assetów
- **`06_assets`** — Runtime asset management i caching
- **`08_audio`** — System audio i ładowanie dźwięków

### Narzędzia

- `docs/authoring/_tools/data_asset_scan.py` - scanner assetów
- `docs/authoring/_tools/ui_assets_linker.py` - linkowanie UI → assets
- `docs/authoring/_tools/csv_preview_build.py` - preview CSV datasets

## Appendix / Facets

(facet-11_data.images)=
### Facet: `11_data.images`
Type: dataset
Schema: `asset_id, rel_path, category, format, size_px, used_in_files, used_in_widgets, note`

(facet-11_data.fonts)=
### Facet: `11_data.fonts`
Type: dataset
Schema: `id, family, size, style, path, otui_ref, usage`

(facet-11_data.styles)=
### Facet: `11_data.styles`
Type: dataset
Schema: `style_id, widget_type, source_file, priority, properties_count, images_used, note`

(facet-11_data.locales)=
### Facet: `11_data.locales`
Type: dataset
Schema: `lang_code, language, path, keys_count, status, coverage`

(facet-11_data.sounds)=
### Facet: `11_data.sounds`
Type: dataset
Schema: `sound_id, path, channel, usage, loop, volume, duration_s, note`

(facet-11_data.shaders)=
### Facet: `11_data.shaders`
Type: dataset
Schema: `shader_id, vertex_path, fragment_path, target, defines, usage, note`

(facet-11_data.ui_asset_usage)=
### Facet: `11_data.ui_asset_usage`
Type: dataset
Schema: `widget_id, widget_type, asset_type, asset_path, property, optional, note`

(facet-11_data.data_overview)=
### Facet: `11_data.data_overview`
Type: diagram
Format: mermaid (graph TD)

(facet-11_data.asset_to_ui)=
### Facet: `11_data.asset_to_ui`
Type: diagram
Format: mermaid (sequenceDiagram)
