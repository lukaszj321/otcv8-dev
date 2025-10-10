# Chapter 01 - Core Architecture

(core-overview)=
## Przegląd

Architektura rdzenia OTClientV8 opiera się na modularnym silniku C++ z bindingami Lua. System składa się z warstw: Core Engine, Framework, Client Layer i Modules.

:::note
Ten rozdział opisuje fundamentalną architekturę projektu. Dla szczegółów implementacyjnych patrz [API Reference](../reference/api.md).
:::

(core-layers)=
## Warstwy architektury

### Warstwa 1: Core Engine (C++)

Niskopoziomowy silnik napisany w C++, odpowiedzialny za:

* Rendering grafiki (OpenGL/DirectX)
* Zarządzanie zasobami (tekstury, dźwięk, fonty)
* System zdarzeń
* Network stack
* Zarządzanie pamięcią

### Warstwa 2: Framework

Framework dostarcza abstrakcji wysokiego poziomu:

* UI System (OTUI)
* Module Loader
* Resource Manager
* Platform Abstraction Layer
* Lua Bindings

### Warstwa 3: Client Layer

Implementacja logiki specyficznej dla gry:

* Game Protocol
* Creature Management
* Map Rendering
* Inventory System
* Chat System

### Warstwa 4: Modules (Lua)

Moduły napisane w Lua:

* Game Interface
* Bot Framework
* Custom UI Panels
* Extensions

(core-architecture-diagram)=
## Diagram architektury

```{mermaid}
graph TB
    subgraph Lua Layer
        M1[Modules Lua]
        M2[Scripts]
        M3[UI Definitions OTUI]
    end
    
    subgraph Client Layer
        C1[Game Protocol]
        C2[Creature Manager]
        C3[Map Renderer]
        C4[UI Manager]
    end
    
    subgraph Framework
        F1[Module Loader]
        F2[Event System]
        F3[Resource Manager]
        F4[Lua Bindings]
    end
    
    subgraph Core Engine
        E1[Graphics OpenGL/DX]
        E2[Audio System]
        E3[Network TCP/UDP]
        E4[Memory Manager]
    end
    
    M1 --> F4
    M2 --> F4
    M3 --> C4
    
    C1 --> F2
    C2 --> F3
    C3 --> E1
    C4 --> F1
    
    F1 --> E4
    F2 --> E4
    F3 --> E2
    F4 --> C1
    
    style Lua Layer fill:#e1f5ff
    style Client Layer fill:#fff3e0
    style Framework fill:#f3e5f5
    style Core Engine fill:#c8e6c9
```

(core-directories)=
## Struktura katalogów

### src/framework/

Framework zawiera podstawowe komponenty:

```
src/framework/
├── core/          # Podstawowe typy i narzędzia
├── graphics/      # System renderingu
├── net/           # Warstwa sieciowa
├── sound/         # System audio
├── ui/            # System UI (OTUI)
└── xml/           # Parser XML
```

### src/client/

Kod specyficzny dla klienta gry:

```
src/client/
├── animatedtext.cpp/h    # Animowane teksty
├── creature.cpp/h         # Stworzenia
├── game.cpp/h             # Główna logika gry
├── localplayer.cpp/h      # Lokalny gracz
├── map.cpp/h              # Mapa świata
├── mapview.cpp/h          # Widok mapy
├── protocolgame.cpp/h     # Protokół gry
└── uimap.cpp/h            # Widget mapy
```

### modules/

Moduły Lua:

```
modules/
├── corelib/           # Biblioteki core Lua
├── client/            # Główny moduł klienta
├── game_*/            # Moduły gry (interface, battle, etc.)
└── gamelib/           # Biblioteki pomocnicze
```

(core-initialization)=
## Inicjalizacja systemu

### Sekwencja uruchomienia

```{mermaid}
sequenceDiagram
    participant Main as main()
    participant App as Application
    participant ModLoader as Module Loader
    participant Game as Game Engine
    participant UI as UI System
    
    Main->>App: initialize()
    App->>ModLoader: loadModules()
    ModLoader->>ModLoader: discoverModules()
    ModLoader->>ModLoader: resolveDependencies()
    
    loop For each module
        ModLoader->>Module: init.lua
        Module-->>ModLoader: ok
    end
    
    App->>Game: init()
    App->>UI: loadUI()
    UI-->>App: ready
    App->>Main: run()
    Main->>App: mainLoop()
```

### Kod inicjalizacji

```lua
-- init.lua (główny plik inicjalizacyjny)
function init()
    -- Inicjalizacja core libraries
    dofile('modules/corelib/corelib.otmod')
    
    -- Załadowanie modułów
    g_modules.discoverModules()
    g_modules.ensureModuleLoaded('client')
    g_modules.autoLoadModules(100) -- Priority ≥ 100
    
    -- Inicjalizacja UI
    g_window.setTitle('OTClient')
    g_window.setIcon('/images/clienticon.png')
    
    -- Event handlers
    connect(g_app, {
        onRun = onApplicationRun,
        onExit = onApplicationExit
    })
end
```

(core-main-loop)=
## Główna pętla

### Tick System

OTClientV8 używa systemu ticków do aktualizacji stanu:

* **FPS (Frames Per Second)** - częstotliwość renderowania (max 60 FPS)
* **UPS (Updates Per Second)** - częstotliwość aktualizacji logiki (max 100 UPS)

```cpp
// Uproszczona główna pętla (C++)
while (running) {
    // Update logic
    if (shouldUpdateLogic()) {
        updateLogic(elapsedTime);
        ups++;
    }
    
    // Render frame
    if (shouldRenderFrame()) {
        renderFrame();
        fps++;
    }
    
    // Handle events
    pollEvents();
    
    // Sleep if needed
    sleepIfNeeded();
}
```

(core-memory-management)=
## Zarządzanie pamięcią

### Smart Pointers

System używa smart pointerów dla bezpieczeństwa:

```cpp
// Przykłady typów wskaźników
typedef std::shared_ptr<Creature> CreaturePtr;
typedef std::weak_ptr<Creature> CreatureWeakPtr;
typedef std::shared_ptr<Player> PlayerPtr;
typedef std::shared_ptr<Item> ItemPtr;

// Użycie
CreaturePtr creature = CreaturePtr(new Creature);
creature->setName("Dragon");

// Automatyczne czyszczenie gdy nie ma referencji
```

### Resource Caching

Zasoby są cache'owane dla wydajności:

* **Tekstury** - cache po path
* **Fonty** - cache po name i size
* **Dźwięki** - pre-load do bufora
* **Sprites** - cache w pamięci

(core-threading)=
## Model wątków

OTClientV8 używa głównie jednego wątku dla logiki gry:

* **Main Thread** - logika gry, UI, rendering
* **Network Thread** - odbiór/wysyłanie pakietów (opcjonalnie)
* **Resource Loader Thread** - ładowanie zasobów w tle

:::warning
Większość API nie jest thread-safe. Unikaj współdzielenia stanu między wątkami.
:::

(core-build-system)=
## System budowania

### CMake

Projekt używa CMake jako systemu budowania:

```bash
# Konfiguracja
cmake -B build -DCMAKE_BUILD_TYPE=Release

# Kompilacja
cmake --build build --config Release

# Instalacja
cmake --install build
```

### Build Targets

* `otclient` - główny executable
* `otclient-bot` - wersja z dodatkowymi funkcjami bota
* `otclient-dx` - wersja z DirectX zamiast OpenGL

(core-configuration)=
## Konfiguracja

### config.otml

Plik konfiguracyjny w formacie OTML:

```yaml
GameName: OTClient
GameVersion: 860
GameProtocol: 860

UIScale: 1.0
ShowFPS: true
MaxFPS: 60
MaxUPS: 100

SavedCharacterList: true
BackgroundFrameRate: 10

CreatureInformationScale: 1.0
StaticTextScale: 1.0
```

(core-example-snippets)=
## Przykłady kodu

### Tworzenie i konfiguracja gracza

```{literalinclude} ../../src/client/player.h
:language: cpp
:caption: `src/client/player.h` - Player class interface
:linenos:
:lines: 1-40
```

### Zarządzanie eventami w Lua

```lua
-- Przykład modułu z event handlingiem
local myModule = {}

function myModule.init()
    -- Inicjalizacja
    print("Module initialized")
    
    -- Podłączenie do zdarzeń
    connect(g_game, {
        onGameStart = myModule.onGameStart,
        onGameEnd = myModule.onGameEnd
    })
end

function myModule.terminate()
    -- Cleanup
    disconnect(g_game, {
        onGameStart = myModule.onGameStart,
        onGameEnd = myModule.onGameEnd
    })
    
    print("Module terminated")
end

function myModule.onGameStart()
    print("Game started!")
end

function myModule.onGameEnd()
    print("Game ended!")
end

return myModule
```

(core-performance)=
## Wydajność

### Metryki kluczowe

* **FPS ≥ 60** - płynne renderowanie
* **UPS ≥ 100** - responsywna logika
* **Memory < 500MB** - rozsądne zużycie pamięci
* **Latency < 100ms** - akceptowalne opóźnienie sieci

### Narzędzia profilowania

```lua
-- Włączenie statystyk FPS/UPS
g_app.setShowFps(true)

-- Pomiar czasu wykonania
local startTime = g_clock.millis()
-- ... kod do zmierzenia ...
local elapsed = g_clock.millis() - startTime
print("Execution time:", elapsed, "ms")
```

(core-best-practices)=
## Dobre praktyki

1. **Modularność** - dziel kod na niezależne moduły
2. **RAII** - używaj smart pointerów dla zarządzania zasobami
3. **Event-driven** - preferuj eventy nad polling
4. **Cachowanie** - cache'uj często używane zasoby
5. **Profiling** - mierz przed optymalizacją
6. **Documentation** - dokumentuj publiczne API

(core-see-also)=
## Zobacz też

* [API Reference](../reference/api.md) - szczegóły implementacji
* [Events System](02_events.md) - system zdarzeń
* [Modules](03_modules.md) - system modułów
* [Architecture Diagrams](../examples/diagrams.md) - dodatkowe diagramy
