# Przykład: Health Monitor Module

Ten przykład pokazuje prosty moduł monitorujący stan zdrowia gracza i wyświetlający powiadomienia.

## Cel

Stworzyć moduł, który:
- Monitoruje zdrowie gracza
- Wyświetla ostrzeżenie przy niskim HP
- Zapisuje logi zdarzeń

## Struktura plików

```
modules/game_health_monitor/
├── init.lua                 # Główna logika modułu
├── health_monitor.otui      # Interfejs użytkownika
└── health_monitor.lua       # Dodatkowe funkcje pomocnicze
```

## Implementacja

### init.lua

```lua
-- modules/game_health_monitor/init.lua
HealthMonitor = {}

local healthWindow
local lowHealthThreshold = 30  -- 30% HP

function HealthMonitor.init()
  print("[HealthMonitor] Initializing...")
  
  -- Załaduj UI
  healthWindow = g_ui.loadUI('health_monitor')
  healthWindow:hide()
  
  -- Rejestracja eventów
  connect(LocalPlayer, { 
    onHealthChange = HealthMonitor.onHealthChange
  })
  
  connect(g_game, {
    onGameStart = HealthMonitor.onGameStart,
    onGameEnd = HealthMonitor.onGameEnd
  })
  
  print("[HealthMonitor] Initialized")
end

function HealthMonitor.terminate()
  print("[HealthMonitor] Terminating...")
  
  -- Odłącz eventy
  disconnect(LocalPlayer, { 
    onHealthChange = HealthMonitor.onHealthChange
  })
  
  disconnect(g_game, {
    onGameStart = HealthMonitor.onGameStart,
    onGameEnd = HealthMonitor.onGameEnd
  })
  
  -- Zniszcz UI
  if healthWindow then
    healthWindow:destroy()
    healthWindow = nil
  end
  
  HealthMonitor = nil
end

function HealthMonitor.onGameStart()
  print("[HealthMonitor] Game started - monitoring active")
  if healthWindow then
    healthWindow:show()
  end
end

function HealthMonitor.onGameEnd()
  print("[HealthMonitor] Game ended - monitoring stopped")
  if healthWindow then
    healthWindow:hide()
  end
end

function HealthMonitor.onHealthChange(localPlayer, health, maxHealth)
  local healthPercent = (health / maxHealth) * 100
  
  -- Aktualizuj UI
  if healthWindow then
    local label = healthWindow:getChildById('healthLabel')
    if label then
      label:setText(string.format("HP: %d/%d (%.1f%%)", health, maxHealth, healthPercent))
    end
    
    -- Zmień kolor w zależności od poziomu HP
    if healthPercent <= lowHealthThreshold then
      label:setColor('#ff0000')  -- Czerwony
      HealthMonitor.showLowHealthWarning()
    elseif healthPercent <= 50 then
      label:setColor('#ffaa00')  -- Pomarańczowy
    else
      label:setColor('#00ff00')  -- Zielony
    end
  end
  
  -- Log zdarzenia
  g_logger.info(string.format("[HealthMonitor] Health changed: %d/%d (%.1f%%)", 
                              health, maxHealth, healthPercent))
end

function HealthMonitor.showLowHealthWarning()
  -- Wyświetl ostrzeżenie tylko raz na 10 sekund
  if not HealthMonitor.lastWarningTime or 
     os.time() - HealthMonitor.lastWarningTime > 10 then
    
    displayInfoBox("Uwaga!", "Niski poziom zdrowia! Znajdź bezpieczne miejsce.")
    HealthMonitor.lastWarningTime = os.time()
  end
end

function HealthMonitor.toggle()
  if healthWindow then
    healthWindow:setVisible(not healthWindow:isVisible())
  end
end
```

### health_monitor.otui

```lua
-- modules/game_health_monitor/health_monitor.otui
HealthMonitorWindow < MainWindow
  id: healthMonitorWindow
  !text: tr('Health Monitor')
  size: 220 80
  @onEscape: self:hide()
  
  anchors.top: parent.top
  anchors.right: parent.right
  margin-top: 60
  margin-right: 10
  
  Label
    id: healthLabel
    text: HP: -/-
    anchors.fill: parent
    text-align: center
    font: verdana-11px-rounded
    margin: 10
    
  Button
    id: closeButton
    !text: tr('Close')
    width: 60
    anchors.horizontalCenter: parent.horizontalCenter
    anchors.bottom: parent.bottom
    margin-bottom: 5
    @onClick: self:getParent():hide()
```

## Użycie

1. **Instalacja**: Skopiuj katalog `game_health_monitor` do `modules/`
2. **Aktywacja**: Upewnij się, że moduł jest załadowany w `init.lua`
3. **Testowanie**: Uruchom grę i obserwuj monitorowanie HP

## Rozszerzenia

Możliwe ulepszenia:
- Dodaj alerty dźwiękowe przy niskim HP
- Historia zmian zdrowia (wykres)
- Konfiguracja progu ostrzeżeń przez UI
- Zapis statystyk do pliku
- Integracja z systemem makr (auto-heal)

## Zobacz też

- {doc}`../modules/index` – Dokumentacja modułów
- {doc}`../api/index` – API Reference
- {doc}`template` – Szablon modułu

---
