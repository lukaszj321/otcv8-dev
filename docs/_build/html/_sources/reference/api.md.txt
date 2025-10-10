# API Reference

(api-overview)=
## Przegląd API

OTClientV8 dostarcza bogate API w C++ dla silnika oraz Lua bindings dla skryptów. Ta sekcja zawiera kompletną referencję kluczowych klas i funkcji.

(api-index-symbols)=
## Index of Symbols

### Core Classes
* [Creature](#api-creature) - reprezentacja stworzenia w grze
* [Player](#api-player) - reprezentacja gracza
* [Game](#api-game) - główna logika gry
* [Map](#api-map) - reprezentacja mapy świata
* [Tile](#api-tile) - pojedyncze pole mapy

### UI Classes
* [UIWidget](#api-uiwidget) - bazowy widget UI
* [UIMap](#api-uimap) - widget mapy
* [UICreature](#api-uicreature) - widget stworzenia

### Network
* [Protocol](#api-protocol) - protokół sieciowy
* [Connection](#api-connection) - połączenie sieciowe

(api-creature)=
## Creature Class

Klasa `Creature` reprezentuje żywe stworzenie w grze (gracza, potwora, NPC).

```{literalinclude} ../../src/client/creature.h
:language: cpp
:caption: `src/client/creature.h` - Creature class interface
:linenos:
:lines: 23-80
```

### Kluczowe metody

**setName(const std::string& name)**

Ustawia nazwę stworzenia.

* **Parametry:**
  * `name` *(std::string)* - nowa nazwa stworzenia
* **Zwraca:** void

**setHealthPercent(uint8 healthPercent)**

Ustawia procent zdrowia stworzenia (0-100).

* **Parametry:**
  * `healthPercent` *(uint8)* - procent zdrowia (0-100)
* **Zwraca:** void

**setDirection(Otc::Direction direction)**

Ustawia kierunek patrzenia stworzenia.

* **Parametry:**
  * `direction` *(Otc::Direction)* - kierunek: North, East, South, West
* **Zwraca:** void

**setOutfit(const Outfit& outfit)**

Ustawia wygląd (outfit) stworzenia.

* **Parametry:**
  * `outfit` *(const Outfit&)* - obiekt opisujący wygląd
* **Zwraca:** void

:::note
Klasa `Creature` jest bindowana do Lua (patrz `@bindclass`) i może być używana bezpośrednio w skryptach.
:::

(api-player)=
## Player Class

Player dziedziczy po Creature i dodaje funkcjonalność specyficzną dla gracza.

```{literalinclude} ../../src/client/player.h
:language: cpp
:caption: `src/client/player.h` - Player class
:linenos:
:lines: 1-40
```

(api-lua-examples)=
## Przykłady użycia w Lua

### Pobieranie informacji o graczu

```lua
-- Pobranie lokalnego gracza
local player = g_game.getLocalPlayer()
if player then
    print("Player name:", player:getName())
    print("Health:", player:getHealthPercent())
    print("Mana:", player:getManaPercent())
    print("Position:", player:getPosition())
end
```

### Obserwowanie zmiany zdrowia

```lua
-- Callback na zmianę zdrowia
function onHealthChange(localPlayer, health, maxHealth)
    local percent = math.floor((health / maxHealth) * 100)
    print(string.format("Health: %d/%d (%d%%)", health, maxHealth, percent))
    
    if percent < 20 then
        -- Ostrzeżenie o niskim zdrowiu
        modules.game_console.addText("Warning: Low health!", "#FF0000")
    end
end

-- Połączenie sygnału
connect(LocalPlayer, { onHealthChange = onHealthChange })
```

### Iteracja po stworzeniach

```lua
-- Pobranie wszystkich widocznych stworzeń
function scanCreatures()
    local spectators = g_map.getSpectators(g_game.getLocalPlayer():getPosition(), false)
    
    for _, creature in ipairs(spectators) do
        if creature:isMonster() then
            print("Monster found:", creature:getName(), 
                  "HP:", creature:getHealthPercent(),
                  "Distance:", creature:getPosition():distance(g_game.getLocalPlayer():getPosition()))
        end
    end
end
```

(api-cpp-examples)=
## Przykłady użycia w C++

### Tworzenie i konfiguracja stworzenia

```cpp
// Utworzenie nowego stworzenia
CreaturePtr creature = CreaturePtr(new Creature);
creature->setId(12345);
creature->setName("Dragon");
creature->setHealthPercent(75);
creature->setDirection(Otc::South);

// Ustawienie wyglądu
Outfit outfit;
outfit.setCategory(ThingCategoryCreature);
outfit.setId(130);
creature->setOutfit(outfit);
```

(api-see-also)=
## Zobacz też

* [Events Reference](events.md) - system zdarzeń
* [Modules Reference](modules.md) - dokumentacja modułów Lua
* [UI Reference](ui.md) - komponenty interfejsu użytkownika
* [Przykłady](../examples/diagrams.md) - diagramy architektury
