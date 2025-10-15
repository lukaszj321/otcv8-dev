
---
doc_id: "authoring.12_otmod.index"
source_path: "modules/**"
source_sha: "HEAD"
last_sync_iso: "2025-10-15T22:21:56Z"
doc_class: "guide"
language: "pl"
title: "OTMOD — Struktura modułów i packaging"
summary: "Kompletny przewodnik po systemie modułów OTClient v8: struktura OTMOD, lifecycle hooks, zarządzanie zależnościami, hot-reload i integracja z UI/Lua."
tags: ["otclient", "otmod", "modules", "packaging", "lua", "dependencies", "lifecycle", "rag"]
---

# OTMOD — Struktura modułów i packaging

**Cel rozdziału:** Udokumentować system pakowania modułów OTClient v8 (format OTMOD), lifecycle hooks (`@onLoad`, `@onUnload`), zarządzanie zależnościami, sandboxing i integrację z UI oraz kodem Lua.

```{contents} Spis treści
:depth: 3
:local:
```

:::{admonition} TL;DR
:class: tip
Moduły (`.otmod`) to samodzielne pakiety funkcjonalności zawierające skrypty Lua, UI (OTUI), zasoby i metadane. Są ładowane przez `ModuleManager` zgodnie z deklarowanymi zależnościami.
:::

## Wprowadzenie domenowe

System modułowy OTClient v8 opiera się na **plikach manifestowych** (`.otmod`), które deklarują:
- Metadane modułu (nazwa, wersja, autor, opis)
- Zależności od innych modułów
- Skrypty Lua do załadowania
- Pliki UI (OTUI) do zarejestrowania
- Lifecycle hooks (`@onLoad`, `@onUnload`, `@onTerminate`)
- Opcje sandboxing i autoload

Moduły są organizowane w katalogu `modules/**` i ładowane w kolejności wynikającej z grafu zależności (topological sort). System umożliwia **hot-reload** (przeładowanie w runtime) oraz **conditional loading** (ładowanie tylko gdy spełnione warunki).

### Podstawowa anatomia modułu

```
modules/
  game_skills/
    skills.otmod      # manifest
    skills.lua        # główny skrypt
    skills.otui       # UI layout
    README.md         # dokumentacja (opcjonalna)
```

**Przykład manifestu (`skills.otmod`):**
```yaml
Module
  name: game_skills
  description: Skills panel displaying character attributes
  author: OTClient Team
  website: https://github.com/edubart/otclient
  version: 1.0
  
  dependencies:
    - game_interface
    - gamelib
  
  scripts:
    - skills.lua
  
  @onLoad: |
    dofile('skills.lua')
    init()
  
  @onUnload: |
    terminate()
```

### Katalogi modułów

- **`corelib/`** - biblioteki podstawowe (globals, string/table extensions, UI helpers)
- **`gamelib/`** - logika gry (protokół, pozycje, creatures, items)
- **`client_*/`** - moduły interfejsu klienta (entergame, options, styles, profiles)
- **`game_*/`** - moduły funkcjonalności gry (battle, inventory, console, minimap)

## Architektura / Przepływ

### Diagram lifecycle modułu

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
sequenceDiagram
    participant MM as ModuleManager
    participant M as Module
    participant LUA as Lua VM
    participant UI as UI System
    
    MM->>M: discoverModule(path)
    M-->>MM: manifest loaded
    
    MM->>M: loadModule()
    M->>LUA: execute scripts
    LUA->>M: @onLoad hook
    
    alt Has UI files
        M->>UI: registerUI(*.otui)
        UI-->>M: UI registered
    end
    
    M-->>MM: module loaded
    
    Note over MM,UI: Module is now active
    
    MM->>M: unloadModule()
    M->>LUA: @onUnload hook
    LUA->>UI: destroyWidgets()
    M-->>MM: module unloaded
```

### Diagram grafu zależności

```{mermaid}
%%{init: { 'theme': 'neutral' }}%%
graph TD
    CORE[corelib]
    GAMELIB[gamelib]
    CLIENT_STYLES[client_styles]
    GAME_INTERFACE[game_interface]
    GAME_SKILLS[game_skills]
    GAME_INVENTORY[game_inventory]
    GAME_CONSOLE[game_console]
    
    CORE --> GAMELIB
    CORE --> CLIENT_STYLES
    GAMELIB --> GAME_INTERFACE
    CLIENT_STYLES --> GAME_INTERFACE
    GAME_INTERFACE --> GAME_SKILLS
    GAME_INTERFACE --> GAME_INVENTORY
    GAME_INTERFACE --> GAME_CONSOLE
    
    click CORE "./index.html#facet-12_otmod.modules_index" "Zobacz moduły"
    click GAMELIB "./index.html#facet-12_otmod.module_deps" "Zobacz zależności"
```

### Diagram resolution ścieżek zasobów

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd' } }}%%
flowchart LR
    A[Module Path Request]
    B{Absolute path?}
    C[Use as-is]
    D{Starts with /}
    E[Resolve from data/]
    F[Resolve relative to module]
    G[ResourceManager]
    
    A --> B
    B -->|Yes| C
    B -->|No| D
    D -->|Yes| E
    D -->|No| F
    C --> G
    E --> G
    F --> G
    
    G --> H[Asset Loaded]
```

## Datasets

### modules_index.csv — Katalog modułów

*Facet:* [`12_otmod.modules_index`](#facet-12_otmod.modules_index)

Spis wszystkich modułów z podstawowymi metadanymi.

| module | description | author | version | scripts_count | otui_count | dependencies | sandboxed | autoload |
|---|---|---|---|---|---|---|---|---|
| corelib | Core library with utilities and UI extensions | OTClient Team | 1.0 | 42 | 0 | - | false | true |
| gamelib | Game protocol and entity management | OTClient Team | 1.0 | 15 | 0 | corelib | false | true |
| client_styles | UI styles definitions | OTClient Team | 1.0 | 1 | 0 | corelib | false | true |
| client_entergame | Login screen and character list | OTClient Team | 1.0 | 2 | 3 | corelib | false | true |
| client_options | Settings panel | OTClient Team | 1.0 | 1 | 7 | corelib | false | true |
| game_interface | Main game interface | OTClient Team | 1.0 | 1 | 1 | gamelib, client_styles | false | true |
| game_skills | Skills panel | OTClient Team | 1.0 | 1 | 1 | game_interface | false | true |
| game_inventory | Inventory slots display | OTClient Team | 1.0 | 1 | 1 | game_interface | false | true |
| game_console | Chat console | OTClient Team | 1.0 | 1 | 4 | game_interface | false | true |
| game_battle | Battle list | OTClient Team | 1.0 | 1 | 2 | game_interface | false | true |

```{csv-table} modules_index (próbka)
:header-rows: 1
:file: ./datasets/modules_index.csv
:widths: auto
```

**Konwencje nazewnicze:**
- `corelib`, `gamelib` - biblioteki podstawowe
- `client_*` - moduły interfejsu klienta
- `game_*` - moduły funkcjonalności gry
- `bot_*` - moduły automatyzacji (jeśli obecne)

### module_deps.csv — Graf zależności

*Facet:* [`12_otmod.module_deps`](#facet-12_otmod.module_deps)

Tabela zależności między modułami (krawędzie grafu).

| module | depends_on | type | optional | min_version | note |
|---|---|---|---|---|---|
| gamelib | corelib | hard | false | 1.0 | wymaga core utilities |
| client_styles | corelib | hard | false | 1.0 | wymaga UI helpers |
| game_interface | gamelib | hard | false | 1.0 | wymaga game protocol |
| game_interface | client_styles | hard | false | 1.0 | wymaga style definitions |
| game_skills | game_interface | hard | false | 1.0 | wymaga głównego interface |
| game_inventory | game_interface | hard | false | 1.0 | wymaga głównego interface |
| game_console | game_interface | hard | false | 1.0 | wymaga głównego interface |
| game_hotkeys | game_console | soft | true | 1.0 | opcjonalnie, dla bindowania klawiszy czatu |

```{csv-table} module_deps (próbka)
:header-rows: 1
:file: ./datasets/module_deps.csv
:widths: auto
```

**Typy zależności:**
- `hard` - moduł nie załaduje się bez zależności
- `soft` - moduł załaduje się, ale część funkcji może być niedostępna
- `conflict` - nie może być załadowany jednocześnie z zależnością

### module_scripts.csv — Skrypty Lua

*Facet:* [`12_otmod.module_scripts`](#facet-12_otmod.module_scripts)

Lista plików Lua załadowanych przez moduły.

| module | script_path | role | lines | functions_exported | events_hooked | note |
|---|---|---|---|---|---|---|
| corelib | globals.lua | core | 250 | 15 | 0 | globals and utility functions |
| corelib | string.lua | core | 180 | 12 | 0 | string extensions |
| corelib | table.lua | core | 220 | 18 | 0 | table extensions |
| gamelib | game.lua | core | 350 | 25 | 8 | main game logic |
| gamelib | protocol.lua | core | 420 | 30 | 0 | protocol constants |
| game_skills | skills.lua | feature | 280 | 5 | 3 | skills panel logic |
| game_inventory | inventory.lua | feature | 195 | 4 | 2 | inventory management |
| game_console | console.lua | feature | 480 | 12 | 6 | chat console |

```{csv-table} module_scripts (próbka)
:header-rows: 1
:file: ./datasets/module_scripts.csv
:widths: auto
```

**Role skryptów:**
- `core` - logika podstawowa, utilities
- `feature` - implementacja konkretnej funkcjonalności
- `ui` - obsługa UI (callbacks, event handlers)
- `protocol` - obsługa protokołu sieciowego

### module_hooks.csv — Lifecycle hooks

*Facet:* [`12_otmod.module_hooks`](#facet-12_otmod.module_hooks)

Hooks wykonywane podczas lifecycle modułu.

| module | hook | code_snippet | async | critical | note |
|---|---|---|---|---|---|
| game_skills | @onLoad | dofile('skills.lua'); init() | false | true | inicjalizacja panelu |
| game_skills | @onUnload | terminate() | false | true | cleanup widgetów |
| game_inventory | @onLoad | dofile('inventory.lua'); setup() | false | true | setup slotów ekwipunku |
| game_console | @onLoad | initConsole() | false | true | setup konsoli czatu |
| game_hotkeys | @onLoad | loadHotkeys() | true | false | ładowanie hotkeysów |

```{csv-table} module_hooks (próbka)
:header-rows: 1
:file: ./datasets/module_hooks.csv
:widths: auto
```

**Dostępne hooks:**
- `@onLoad` - wykonywany przy ładowaniu modułu
- `@onUnload` - wykonywany przy wyładowaniu modułu
- `@onTerminate` - wykonywany przy zamykaniu aplikacji
- `@onAutoLoad` - wykonywany automatycznie przy starcie (jeśli `autoload: true`)

### module_ui_links.csv — Powiązania z UI

*Facet:* [`12_otmod.module_ui_links`](#facet-12_otmod.module_ui_links)

Mapowanie modułów na pliki OTUI i widgety.

| module | otui_file | widget_root | parent_widget | anchor | hotkey | note |
|---|---|---|---|---|---|---|
| game_skills | skills.otui | SkillsWindow | GameInterface | right | Ctrl+S | panel umiejętności |
| game_inventory | inventory.otui | InventoryPanel | GameInterface | right | Ctrl+I | ekwipunek |
| game_console | console.otui | ConsolePanel | GameInterface | bottom | - | konsola czatu |
| game_battle | battle.otui | BattleWindow | GameInterface | left | Ctrl+B | lista walki |
| client_entergame | entergame.otui | EnterGame | MainWindow | center | - | ekran logowania |

```{csv-table} module_ui_links (próbka)
:header-rows: 1
:file: ./datasets/module_ui_links.csv
:widths: auto
```

### lua_exports.csv — Eksportowane funkcje Lua

*Facet:* [`12_otmod.lua_exports`](#facet-12_otmod.lua_exports)

Funkcje Lua dostępne globalnie lub przez moduł (API publiczne).

| module | function | params | returns | raises | availability | note |
|---|---|---|---|---|---|---|
| corelib | tr(text) | text:string | string | - | global | translacja tekstów |
| corelib | connect(obj, signals) | obj:table, signals:table | - | - | global | hookowanie sygnałów |
| corelib | disconnect(obj, signals) | obj:table, signals:table | - | - | global | unhookowanie sygnałów |
| gamelib | g_game.isOnline() | - | boolean | - | global | sprawdza czy połączony |
| gamelib | g_game.getLocalPlayer() | - | Player | - | global | zwraca lokalnego gracza |
| game_skills | getSkillValue(skillId) | skillId:number | number | - | module | wartość umiejętności |

```{csv-table} lua_exports (próbka - CSV w datasets/)
:header-rows: 1
:file: ./datasets/lua_exports.csv
:widths: auto
```

## Blueprints — Wzorce modułów

### Blueprint 1: Minimalny moduł funkcjonalny

**Struktura plików:**
```
modules/
  my_feature/
    my_feature.otmod
    my_feature.lua
    my_feature.otui
```

**Manifest (`my_feature.otmod`):**
```yaml
Module
  name: my_feature
  description: Example feature module
  author: Developer
  version: 1.0
  
  dependencies:
    - game_interface
  
  @onLoad: |
    dofile('my_feature.lua')
    MyFeature.init()
  
  @onUnload: |
    MyFeature.terminate()
```

**Skrypt (`my_feature.lua`):**
```lua
MyFeature = {}

local featureWindow

function MyFeature.init()
  -- Connect UI
  featureWindow = g_ui.loadUI('my_feature')
  featureWindow:hide()
  
  -- Add toggle button
  local topButton = modules.game_interface.addTopMenuButton('myFeatureButton', 
    tr('My Feature'), '/images/topbuttons/my_feature', MyFeature.toggle)
  
  -- Connect events
  connect(g_game, { onGameStart = MyFeature.onGameStart,
                    onGameEnd = MyFeature.onGameEnd })
end

function MyFeature.terminate()
  disconnect(g_game, { onGameStart = MyFeature.onGameStart,
                        onGameEnd = MyFeature.onGameEnd })
  featureWindow:destroy()
end

function MyFeature.toggle()
  featureWindow:setVisible(not featureWindow:isVisible())
end

function MyFeature.onGameStart()
  -- Inicjalizacja przy wejściu do gry
end

function MyFeature.onGameEnd()
  -- Cleanup przy wyjściu z gry
end
```

**UI (`my_feature.otui`):**
```yaml
FeatureWindow < MiniWindow
  id: featureWindow
  !text: tr('My Feature')
  size: 200 150
  
  Label
    anchors.top: parent.top
    anchors.left: parent.left
    anchors.right: parent.right
    text: Example content
    margin: 5
  
  Button
    id: closeButton
    text: Close
    anchors.bottom: parent.bottom
    anchors.horizontalCenter: parent.horizontalCenter
    margin-bottom: 5
    @onClick: modules.my_feature.toggle()
```

### Blueprint 2: Moduł z zależnościami opcjonalnymi

**Manifest z soft dependency:**
```yaml
Module
  name: enhanced_console
  description: Console with optional spell checking
  
  dependencies:
    - game_console
  
  optional-dependencies:
    - spell_checker
    - emoji_support
  
  @onLoad: |
    dofile('enhanced_console.lua')
    
    -- Sprawdź czy moduły opcjonalne są dostępne
    if g_modules.getModule('spell_checker') then
      EnhancedConsole.enableSpellCheck()
    end
    
    if g_modules.getModule('emoji_support') then
      EnhancedConsole.enableEmoji()
    end
    
    EnhancedConsole.init()
```

### Blueprint 3: Moduł z hot-reload

**Skrypt z hot-reload support:**
```lua
EnhancedFeature = {}

local cachedData = {}

function EnhancedFeature.init()
  -- Załaduj cache z pliku (persistent data)
  if g_resources.fileExists('/config/enhanced_feature.json') then
    local data = g_resources.readFileContents('/config/enhanced_feature.json')
    cachedData = json.decode(data)
  end
  
  -- Setup UI
  setupUI()
end

function EnhancedFeature.terminate()
  -- Zapisz cache przed wyładowaniem
  local data = json.encode(cachedData)
  g_resources.writeFileContents('/config/enhanced_feature.json', data)
  
  -- Cleanup
  destroyUI()
end

-- Funkcja hot-reload (może być wywołana bez terminate/init)
function EnhancedFeature.reload()
  print('[EnhancedFeature] Hot-reloading...')
  
  -- Zachowaj state
  local savedState = getCurrentState()
  
  -- Przeładuj UI
  destroyUI()
  setupUI()
  
  -- Przywróć state
  restoreState(savedState)
  
  print('[EnhancedFeature] Hot-reload complete')
end
```

**Hot-reload w konsoli:**
```lua
-- W konsoli klienta
g_modules.reloadModule('enhanced_feature')
```

### Blueprint 4: Moduł sandboxowany

**Manifest z sandboxing:**
```yaml
Module
  name: untrusted_plugin
  description: Third-party plugin with sandbox
  sandboxed: true
  
  allowed-globals:
    - g_ui
    - g_game
    - tr
  
  blocked-functions:
    - io.*
    - os.*
    - require
    - dofile
  
  @onLoad: |
    -- Kod wykonywany w sandboxie
    -- Brak dostępu do io.*, os.*, require, dofile
    dofile('plugin.lua')
```

**Sandbox enforcement (C++ side - informacyjnie):**
```cpp
// W ModuleManager::loadModule()
if (module->isSandboxed()) {
    // Utwórz izolowany environment
    lua_newtable(L);  // env table
    
    // Kopiuj tylko dozwolone globale
    for (const auto& global : module->getAllowedGlobals()) {
        lua_getglobal(L, global.c_str());
        lua_setfield(L, -2, global.c_str());
    }
    
    // Zablokuj niebezpieczne funkcje
    lua_pushnil(L);
    lua_setfield(L, -2, "require");
    lua_pushnil(L);
    lua_setfield(L, -2, "dofile");
    
    // Ustaw jako environment
    lua_setfenv(L, -2);
}
```

### Blueprint 5: Moduł z konfiguracją

**Manifest z konfiguracją:**
```yaml
Module
  name: configurable_feature
  description: Feature with user configuration
  
  config:
    default-enabled: true
    refresh-interval: 1000
    max-items: 100
  
  @onLoad: |
    local config = g_modules.getModuleConfig('configurable_feature')
    
    ConfigurableFeature.init({
      enabled = config['default-enabled'],
      interval = config['refresh-interval'],
      maxItems = config['max-items']
    })
```

**Użycie w kodzie:**
```lua
ConfigurableFeature = {}

function ConfigurableFeature.init(config)
  self.config = config
  
  if config.enabled then
    self.timer = scheduleEvent(self.refresh, config.interval)
  end
end

function ConfigurableFeature.refresh()
  -- Odśwież dane
  local items = fetchItems(self.config.maxItems)
  updateUI(items)
  
  -- Zaplanuj następne odświeżenie
  self.timer = scheduleEvent(self.refresh, self.config.interval)
end
```

## How-to / Playbook

### Procedura 1: Tworzenie nowego modułu

**Krok 1:** Utwórz strukturę katalogów
```bash
mkdir modules/my_module
cd modules/my_module
```

**Krok 2:** Utwórz manifest
```bash
cat > my_module.otmod << 'EOF'
Module
  name: my_module
  description: My custom module
  author: Me
  version: 1.0
  
  dependencies:
    - game_interface
  
  @onLoad: |
    dofile('my_module.lua')
    MyModule.init()
  
  @onUnload: |
    MyModule.terminate()
EOF
```

**Krok 3:** Utwórz skrypt główny
```bash
cat > my_module.lua << 'EOF'
MyModule = {}

function MyModule.init()
  print('[MyModule] Initializing...')
  -- Twoja logika tutaj
end

function MyModule.terminate()
  print('[MyModule] Terminating...')
  -- Cleanup tutaj
end
EOF
```

**Krok 4:** Testuj w kliencie
```lua
-- W konsoli klienta
g_modules.discoverModule('/modules/my_module')
g_modules.ensureModuleLoaded('my_module')
```

**Krok 5:** Debug
```lua
-- Sprawdź czy moduł załadowany
g_modules.getModule('my_module')

-- Sprawdź błędy
g_logger.getLastErrors()
```

### Procedura 2: Zarządzanie zależnościami

**Krok 1:** Deklaruj zależności w manifeście
```yaml
Module
  name: advanced_feature
  
  dependencies:
    - corelib          # wymagane: core utilities
    - game_interface   # wymagane: główny interface
    - game_console     # wymagane: dostęp do czatu
  
  optional-dependencies:
    - bot_lib          # opcjonalne: jeśli bot enabled
```

**Krok 2:** Sprawdź dostępność w kodzie
```lua
function AdvancedFeature.init()
  -- Sprawdź czy wymagana zależność załadowana
  if not g_modules.getModule('game_interface') then
    error('[AdvancedFeature] Missing required module: game_interface')
    return
  end
  
  -- Obsłuż opcjonalną zależność
  if g_modules.getModule('bot_lib') then
    print('[AdvancedFeature] Bot support enabled')
    self.botEnabled = true
  else
    print('[AdvancedFeature] Bot support disabled')
    self.botEnabled = false
  end
end
```

**Krok 3:** Waliduj graf zależności
```lua
-- Sprawdź cykl zależności
python docs/authoring/_tools/otmod_indexer.py --check-cycles
```

### Procedura 3: Hot-reload modułu

**Krok 1:** Przygotuj moduł do hot-reload
```lua
MyModule = {}

-- Stan który przetrwa reload
MyModule.persistentState = {}

function MyModule.init()
  -- Przywróć state jeśli istnieje
  if MyModule.persistentState.data then
    restoreFromState(MyModule.persistentState.data)
  end
  
  setupUI()
end

function MyModule.terminate()
  -- Zapisz state przed wyładowaniem
  MyModule.persistentState.data = saveCurrentState()
  
  cleanupUI()
end
```

**Krok 2:** Reload w konsoli
```lua
-- Przeładuj moduł
g_modules.reloadModule('my_module')

-- Lub wyładuj i załaduj ponownie
g_modules.unloadModule('my_module')
g_modules.ensureModuleLoaded('my_module')
```

**Krok 3:** Automatyczny reload przy zmianie plików
```lua
-- W module watcher (dev mode)
g_resources.addWatcher('/modules/my_module/*.lua', function(path)
  print('[Dev] File changed: ' .. path)
  g_modules.reloadModule('my_module')
end)
```

### Procedura 4: Debugowanie błędów modułu

**Krok 1:** Włącz verbose logging
```lua
g_logger.setLevel(LogDebug)
```

**Krok 2:** Sprawdź status modułu
```lua
local module = g_modules.getModule('my_module')
if not module then
  print('Module not found')
elseif not module:isLoaded() then
  print('Module not loaded')
  print('Error: ' .. module:getLoadError())
else
  print('Module loaded successfully')
end
```

**Krok 3:** Analiza zależności
```lua
-- Pokaż zależności modułu
local deps = module:getDependencies()
for _, dep in ipairs(deps) do
  local depMod = g_modules.getModule(dep)
  if not depMod or not depMod:isLoaded() then
    print('[ERROR] Missing dependency: ' .. dep)
  end
end
```

**Krok 4:** Stack trace przy błędzie
```lua
-- W my_module.lua
function MyModule.riskyFunction()
  local success, err = pcall(function()
    -- Kod który może wywołać błąd
    dangerousOperation()
  end)
  
  if not success then
    print('[MyModule] Error in riskyFunction:')
    print(debug.traceback(err))
  end
end
```

### Procedura 5: Testowanie modułu

**Krok 1:** Utwórz test suite
```lua
-- modules/my_module/test.lua
MyModuleTest = {}

function MyModuleTest.run()
  print('[Test] Running MyModule tests...')
  
  MyModuleTest.testInit()
  MyModuleTest.testFunctionality()
  MyModuleTest.testCleanup()
  
  print('[Test] All tests passed')
end

function MyModuleTest.testInit()
  assert(MyModule, 'Module not loaded')
  assert(MyModule.init, 'init function missing')
  MyModule.init()
  assert(MyModule.isInitialized, 'Module not initialized')
end

function MyModuleTest.testFunctionality()
  local result = MyModule.someFunction(123)
  assert(result == expectedValue, 'Unexpected result')
end

function MyModuleTest.testCleanup()
  MyModule.terminate()
  assert(not MyModule.isInitialized, 'Module not cleaned up')
end
```

**Krok 2:** Uruchom testy
```lua
-- W konsoli klienta
dofile('/modules/my_module/test.lua')
MyModuleTest.run()
```

**Krok 3:** CI/CD integration
```bash
# W skrypcie CI
python -c "
import otclient_test_runner
runner = otclient_test_runner.TestRunner()
runner.loadModule('my_module')
runner.runTests()
exit(0 if runner.allPassed() else 1)
"
```

## Integracje / Pułapki

### Pułapka 1: Cykliczne zależności

**Problem:**
```yaml
# Module A
dependencies:
  - module_b

# Module B
dependencies:
  - module_a  # BŁĄD: cykl
```

**Remedium:**
- Wydziel wspólny kod do trzeciego modułu (np. `common_lib`)
- Użyj `optional-dependencies` dla jednej strony zależności
- Refaktoryzuj aby usunąć cykl

**Detekcja:**
```python
# docs/authoring/_tools/otmod_indexer.py --check-cycles
# Output: ERROR: Circular dependency: module_a -> module_b -> module_a
```

### Pułapka 2: Konflikty w globalnej przestrzeni nazw

**Problem:**
```lua
-- Module A
function toggle()  -- Global!
  -- ...
end

-- Module B
function toggle()  -- Global! Nadpisuje Module A
  -- ...
end
```

**Remedium:**
```lua
-- Module A
ModuleA = {}
function ModuleA.toggle()
  -- ...
end

-- Module B
ModuleB = {}
function ModuleB.toggle()
  -- ...
end
```

### Pułapka 3: Memory leaks przy unload

**Problem:**
```lua
function MyModule.init()
  -- Tworzy widget ale nie cleanup w terminate
  self.widget = g_ui.createWidget('MyWidget')
  
  -- Event listener bez disconnect
  connect(g_game, { onGameStart = self.onGameStart })
end

function MyModule.terminate()
  -- BRAK: self.widget:destroy()
  -- BRAK: disconnect(g_game, { onGameStart = self.onGameStart })
end
```

**Remedium:**
```lua
function MyModule.terminate()
  if self.widget then
    self.widget:destroy()
    self.widget = nil
  end
  
  disconnect(g_game, { onGameStart = self.onGameStart })
end
```

### Pułapka 4: Ścieżki względne w dofile

**Problem:**
```lua
-- W my_module.lua (katalog: modules/my_module/)
dofile('helper.lua')  # BŁĄD: szuka w bieżącym katalogu roboczym, nie module
```

**Remedium:**
```lua
-- Użyj ścieżki względnej do modułu
local modulePath = g_modules.getModule('my_module'):getPath()
dofile(modulePath .. '/helper.lua')

-- Lub funkcja pomocnicza
function MyModule.dofile(filename)
  local path = g_modules.getModule('my_module'):getPath() .. '/' .. filename
  dofile(path)
end
```

### Pułapka 5: Autoload bez warunku

**Problem:**
```yaml
Module
  name: game_feature
  autoload: true  # Ładuje nawet jeśli gra nie jest aktywna
  
  @onLoad: |
    -- Próbuje użyć g_game bez sprawdzenia
    local player = g_game.getLocalPlayer()  # BŁĄD: nil
```

**Remedium:**
```yaml
Module
  name: game_feature
  autoload: false  # Ładuj ręcznie w odpowiednim momencie
  
  @onLoad: |
    -- Lub sprawdź warunek
    if g_game.isOnline() then
      setupFeature()
    else
      connect(g_game, { onGameStart = setupFeature })
    end
```

## QA & Checklists

### Checklist: Nowy moduł

- [ ] Manifest (`.otmod`) zawiera wszystkie wymagane pola
- [ ] Nazwa modułu: lowercase, snake_case
- [ ] Zależności zadeklarowane kompletnie
- [ ] `@onLoad` i `@onUnload` hooks zdefiniowane
- [ ] Wszystkie skrypty Lua znajdują się w katalogu modułu
- [ ] Brak konfliktów w globalnej przestrzeni nazw (używaj namespace'ów)
- [ ] Cleanup w `@onUnload` (disconnect events, destroy widgets)
- [ ] Testowane: load, funkcjonalność, unload
- [ ] Dodane do `modules_index.csv` i pozostałych datasets
- [ ] Dokumentacja README.md w katalogu modułu (opcjonalnie)

### Checklist: Zależności

- [ ] Wszystkie hard dependencies dostępne
- [ ] Brak cykli zależności (sprawdź narzędziem)
- [ ] Optional dependencies obsłużone gracefully (if exists)
- [ ] Kolejność ładowania respektuje graf zależności
- [ ] Testy z różnymi kombinacjami zależności opcjonalnych

### Checklist: Hot-reload

- [ ] State preservation implemented (jeśli potrzebne)
- [ ] UI recreation działa poprawnie
- [ ] Event listeners odłączane przed reload
- [ ] Memory leaks weryfikowane (przed/po reload)
- [ ] Testowane: wielokrotny reload bez błędów

### Link-lint OK

```bash
python docs/authoring/_tools/link_lint.py --chapter 12_otmod
# Expected: 0 errors
```

### Diagram-lint OK

```bash
python docs/authoring/_tools/diagram_lint.py --chapter 12_otmod
# Expected: all diagrams have %%{init: ...}%% header
```

### Dataset-sanity OK

```bash
python docs/authoring/_tools/csv_schema_check.py --chapter 12_otmod
# Expected:
# - headers match schema
# - no empty rows
# - no NaN values
```

### Idempotency OK

```bash
python docs/authoring/_tools/otmod_indexer.py --output /tmp/run1/
python docs/authoring/_tools/otmod_indexer.py --output /tmp/run2/
diff -r /tmp/run1/ /tmp/run2/
# Expected: no differences
```

## See Also

### Crosslinks do innych rozdziałów

- **`03_modules`** — Dokumentacja API Lua modułów
- **`04_ui`** — Widgety OTUI używane w modułach
- **`11_data`** — Zasoby ładowane przez moduły
- **`02_events`** — System eventów i sygnałów
- **`01_core`** — C++ API ModuleManager

### Narzędzia

- `docs/authoring/_tools/otmod_indexer.py` - skaner modułów
- `docs/authoring/_tools/xref_builder.py` - builder cross-references
- `g_modules` API - runtime management modułów

## Appendix / Facets

(facet-12_otmod.modules_index)=
### Facet: `12_otmod.modules_index`
Type: dataset
Schema: `module, description, author, version, scripts_count, otui_count, dependencies, sandboxed, autoload`

(facet-12_otmod.module_deps)=
### Facet: `12_otmod.module_deps`
Type: dataset
Schema: `module, depends_on, type, optional, min_version, note`

(facet-12_otmod.module_scripts)=
### Facet: `12_otmod.module_scripts`
Type: dataset
Schema: `module, script_path, role, lines, functions_exported, events_hooked, note`

(facet-12_otmod.module_hooks)=
### Facet: `12_otmod.module_hooks`
Type: dataset
Schema: `module, hook, code_snippet, async, critical, note`

(facet-12_otmod.module_ui_links)=
### Facet: `12_otmod.module_ui_links`
Type: dataset
Schema: `module, otui_file, widget_root, parent_widget, anchor, hotkey, note`

(facet-12_otmod.lua_exports)=
### Facet: `12_otmod.lua_exports`
Type: dataset
Schema: `module, function, params, returns, raises, availability, note`

(facet-12_otmod.module_lifecycle)=
### Facet: `12_otmod.module_lifecycle`
Type: diagram
Format: mermaid (sequenceDiagram)
