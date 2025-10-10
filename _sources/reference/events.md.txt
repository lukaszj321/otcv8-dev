# Events Reference

(events-overview)=
## Przegląd systemu zdarzeń

System zdarzeń w OTClientV8 umożliwia asynchroniczną komunikację między komponentami. Wykorzystuje wzorzec Observer/Pub-Sub do powiadamiania o zmianach stanu.

(events-index)=
## Index zdarzeń

### Game Events
* [onGameStart](#event-onGameStart) - rozpoczęcie sesji gry
* [onGameEnd](#event-onGameEnd) - zakończenie sesji gry
* [onLogin](#event-onLogin) - logowanie gracza
* [onLogout](#event-onLogout) - wylogowanie gracza

### Creature Events
* [onCreatureAppear](#event-onCreatureAppear) - pojawienie się stworzenia
* [onCreatureDisappear](#event-onCreatureDisappear) - zniknięcie stworzenia
* [onCreatureMove](#event-onCreatureMove) - ruch stworzenia

### Player Events
* [onHealthChange](#event-onHealthChange) - zmiana zdrowia
* [onManaChange](#event-onManaChange) - zmiana many
* [onPositionChange](#event-onPositionChange) - zmiana pozycji

### Text Events
* [onTextMessage](#event-onTextMessage) - wiadomość tekstowa
* [onTalk](#event-onTalk) - komunikat czatu

(events-connection)=
## Podłączanie zdarzeń

### Podstawowa składnia

```lua
-- Podłączenie do zdarzenia
connect(ObjectClass, {
    eventName = function(param1, param2)
        -- Obsługa zdarzenia
    end
})

-- Odłączenie zdarzenia
disconnect(ObjectClass, {
    eventName = callbackFunction
})
```

(event-onGameStart)=
## Event: onGameStart

Wywoływane gdy sesja gry się rozpoczyna.

**Sygnatura**
```lua
function onGameStart()
```

**Parametry**
Brak

**Przykład użycia**

```lua
function onGameStart()
    print("Game session started!")
    
    -- Inicjalizacja UI
    local gameInterface = g_ui.getRootWidget():recursiveGetChildById('gameInterface')
    if gameInterface then
        gameInterface:show()
    end
    
    -- Załadowanie konfiguracji
    loadConfiguration()
end

connect(g_game, { onGameStart = onGameStart })
```

(event-onLogin)=
## Event: onLogin

Wywoływane po pomyślnym zalogowaniu gracza do gry.

**Sygnatura**
```lua
function onLogin(localPlayer)
```

**Parametry**
* `localPlayer` *(LocalPlayer)* - obiekt lokalnego gracza

**Przykład użycia**

```lua
function onLogin(localPlayer)
    print("Player logged in:", localPlayer:getName())
    print("Position:", localPlayer:getPosition())
    
    -- Powiadomienie w UI
    displayStatusMessage("Welcome, " .. localPlayer:getName() .. "!")
    
    -- Inicjalizacja modułów specyficznych dla gracza
    initializePlayerModules()
end

connect(g_game, { onLogin = onLogin })
```

(event-onCreatureAppear)=
## Event: onCreatureAppear

Wywoływane gdy stworzenie pojawia się w polu widzenia gracza.

**Sygnatura**
```lua
function onCreatureAppear(creature)
```

**Parametry**
* `creature` *(Creature)* - pojawione stworzenie

**Przykład użycia**

```lua
function onCreatureAppear(creature)
    local name = creature:getName()
    local pos = creature:getPosition()
    
    print(string.format("Creature appeared: %s at %s", name, pos))
    
    -- Sprawdzenie czy to potwór
    if creature:isMonster() then
        print("Monster detected:", name)
        -- Możliwość aktywacji auto-targetu lub alarmu
        onMonsterDetected(creature)
    end
end

connect(g_game, { onCreatureAppear = onCreatureAppear })
```

(event-onHealthChange)=
## Event: onHealthChange

Wywoływane gdy zdrowie gracza się zmienia.

**Sygnatura**
```lua
function onHealthChange(localPlayer, health, maxHealth)
```

**Parametry**
* `localPlayer` *(LocalPlayer)* - lokalny gracz
* `health` *(number)* - aktualne zdrowie
* `maxHealth` *(number)* - maksymalne zdrowie

**Przykład użycia**

```lua
function onHealthChange(localPlayer, health, maxHealth)
    local percent = math.floor((health / maxHealth) * 100)
    
    -- Aktualizacja UI
    updateHealthBar(percent)
    
    -- Ostrzeżenie o niskim zdrowiu
    if percent < 20 then
        playSound("low_health_warning.ogg")
        showWarning("Critical health!")
    end
    
    -- Automatyczne użycie potion
    if percent < 50 and hasHealthPotion() then
        useHealthPotion()
    end
end

connect(LocalPlayer, { onHealthChange = onHealthChange })
```

(event-onTextMessage)=
## Event: onTextMessage

Wywoływane gdy gracz otrzymuje wiadomość tekstową.

**Sygnatura**
```lua
function onTextMessage(mode, text)
```

**Parametry**
* `mode` *(MessageMode)* - tryb wiadomości (np. MESSAGE_INFO_DESCR)
* `text` *(string)* - treść wiadomości

**Przykład użycia**

```lua
function onTextMessage(mode, text)
    -- Filtrowanie spamu
    if isSpam(text) then
        return -- Ignoruj
    end
    
    -- Logowanie wiadomości
    logMessage(mode, text)
    
    -- Specjalna obsługa dla niektórych typów
    if mode == MessageModes.MessageInfoDescr then
        -- Wiadomości systemowe
        addToConsole(text, "#00FF00")
    elseif mode == MessageModes.MessagePrivateFrom then
        -- Prywatne wiadomości
        showPrivateMessageNotification(text)
    end
end

connect(g_game, { onTextMessage = onTextMessage })
```

(events-advanced)=
## Zaawansowane techniki

### Event priorities

```lua
-- Wysokie priorytety wykonywane jako pierwsze
connect(g_game, { onGameStart = earlyHandler }, true) -- high priority
connect(g_game, { onGameStart = normalHandler })      -- normal priority
```

### Event cancellation

Niektóre eventy mogą być anulowane przez zwrócenie `false`:

```lua
function onCreatureAppear(creature)
    -- Filtruj niektóre stworzenia
    if shouldIgnoreCreature(creature) then
        return false -- Anuluj dalsze przetwarzanie
    end
    return true
end
```

### Disconnect patterns

```lua
-- Zachowanie referencji do callbacka
local myHandler = function() end
connect(g_game, { onGameStart = myHandler })

-- Późniejsze odłączenie
disconnect(g_game, { onGameStart = myHandler })
```

(events-lifecycle)=
## Cykl życia zdarzeń

```{mermaid}
sequenceDiagram
    participant Source as Event Source
    participant Dispatcher as Event Dispatcher
    participant Handler1 as Handler 1 (high priority)
    participant Handler2 as Handler 2 (normal priority)
    
    Source->>Dispatcher: emit(event, params)
    Dispatcher->>Handler1: callback(params)
    Handler1-->>Dispatcher: return true
    Dispatcher->>Handler2: callback(params)
    Handler2-->>Dispatcher: return true
    Dispatcher-->>Source: event complete
```

(events-best-practices)=
## Dobre praktyki

1. **Cleanup** - zawsze disconnect w `terminate()`
2. **Performance** - unikaj ciężkich operacji w event handlerach
3. **Error handling** - owijaj w pcall dla bezpieczeństwa
4. **Naming** - używaj opisowych nazw dla handlerów
5. **Documentation** - dokumentuj parametry zdarzeń

(events-see-also)=
## Zobacz też

* [API Reference](api.md) - C++ API
* [Modules Reference](modules.md) - system modułów
* [Chapter: Events](../chapters/02_events.md) - pełna dokumentacja zdarzeń
* [Examples: Diagrams](../examples/diagrams.md#diagram-event-flow) - diagram przepływu zdarzeń
