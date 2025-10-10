# Modules Reference

(modules-overview)=
## Przegląd systemu modułów

System modułów OTClientV8 umożliwia organizację kodu w niezależne, ładowalne komponenty. Każdy moduł może definiować własną logikę, UI i zależności.

(modules-index)=
## Index modułów

### Core Modules
* [corelib](#module-corelib) - podstawowe funkcje Lua
* [client](#module-client) - główny moduł klienta

### Game Modules
* [game_interface](#module-game-interface) - interfejs gry
* [game_battle](#module-game-battle) - system walki
* [game_walking](#module-game-walking) - system chodzenia

### Bot Modules
* [game_bot](#module-game-bot) - framework botów

(modules-structure)=
## Struktura modułu

Każdy moduł składa się z:
* **module.otmod** - plik deskryptora (metadata, zależności)
* **init.lua** - główny skrypt inicjalizacyjny
* ***.lua** - dodatkowe skrypty
* ***.otui** - pliki interfejsu użytkownika

Przykład `module.otmod`:

```lua
Module
  name: game_interface
  description: Main game interface
  author: OTClient team
  website: https://github.com/edubart/otclient
  version: 1.0
  
  dependencies:
    - corelib
    - game
  
  @onLoad: init.lua
  @onUnload: terminate.lua
```

(module-corelib)=
## Module: corelib

Moduł `corelib` dostarcza podstawowe funkcje pomocnicze używane przez wszystkie inne moduły.

### Globals

```{literalinclude} ../../modules/corelib/globals.lua
:language: lua
:caption: `modules/corelib/globals.lua` - Global functions
:linenos:
:lines: 1-50
```

### Kluczowe funkcje

(func-scheduleEvent)=
#### scheduleEvent

Planuje wywołanie funkcji po określonym czasie.

**Sygnatura**
```lua
function scheduleEvent(callback, delay)
```

**Parametry**
* `callback` *(function)* - funkcja do wywołania
* `delay` *(number)* - opóźnienie w milisekundach

**Zwraca**
* *(Event)* - obiekt eventu, który można anulować

**Przykład użycia**

```lua
-- Wywołanie funkcji po 1 sekundzie
local event = scheduleEvent(function()
    print("Delayed message!")
end, 1000)

-- Anulowanie eventu przed wykonaniem
-- event:cancel()
```

(func-addEvent)=
#### addEvent

Dodaje event do kolejki zdarzeń do wykonania w następnej klatce.

**Sygnatura**
```lua
function addEvent(callback, front)
```

**Parametry**
* `callback` *(function)* - funkcja do wywołania
* `front` *(boolean, optional)* - czy dodać na początek kolejki (domyślnie false)

**Zwraca**
* *(Event)* - obiekt eventu

**Przykład użycia**

```lua
-- Wykonanie w następnej klatce
addEvent(function()
    print("Next frame execution")
end)

-- Wykonanie na początku kolejki (wysoki priorytet)
addEvent(function()
    print("High priority execution")
end, true)
```

(func-cycleEvent)=
#### cycleEvent

Tworzy cykliczny event wykonywany w określonych odstępach czasu.

**Sygnatura**
```lua
function cycleEvent(callback, interval)
```

**Parametry**
* `callback` *(function)* - funkcja do cyklicznego wywoływania
* `interval` *(number)* - odstęp czasu w milisekundach

**Zwraca**
* *(Event)* - obiekt eventu, który można anulować

**Przykład użycia**

```lua
-- Wykonywanie co sekundę
local cycleEvent = cycleEvent(function()
    print("Tick:", os.time())
end, 1000)

-- Zatrzymanie cyklu
-- cycleEvent:cancel()
```

(modules-math)=
## Moduł: Math utilities

```{literalinclude} ../../modules/corelib/math.lua
:language: lua
:caption: `modules/corelib/math.lua` - Math utilities
:linenos:
:lines: 1-30
```

(modules-loading)=
## Ładowanie modułów

Moduły są ładowane automatycznie przez system, ale można je też ładować programowo:

```lua
-- Załadowanie modułu
g_modules.discoverModule("/path/to/module")
g_modules.ensureModuleLoaded("module_name")

-- Przeładowanie modułu
g_modules.reloadModule("module_name")

-- Sprawdzenie czy moduł jest załadowany
if g_modules.getModule("module_name") then
    print("Module is loaded")
end
```

(modules-dependencies)=
## Zarządzanie zależnościami

System automatycznie ładuje zależności w odpowiedniej kolejności:

```lua
-- W module.otmod
dependencies:
  - corelib
  - client
  - game
```

Cykliczne zależności są wykrywane i zgłaszane jako błędy.

(modules-best-practices)=
## Dobre praktyki

1. **Izolacja** - moduły powinny być niezależne i nie polegać na globalnym stanie
2. **Cleanup** - zawsze implementuj `terminate()` aby zwolnić zasoby
3. **Zależności** - deklaruj wszystkie zależności w `module.otmod`
4. **Namespace** - używaj unikalnych nazw dla globalnych zmiennych
5. **Events** - anuluj wszystkie eventy w `terminate()`

(modules-see-also)=
## Zobacz też

* [API Reference](api.md) - C++ API
* [Events Reference](events.md) - system zdarzeń
* [UI Reference](ui.md) - komponenty UI
* [Chapter: Modules](../chapters/03_modules.md) - pełna dokumentacja modułów
