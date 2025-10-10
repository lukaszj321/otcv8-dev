<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
# Referencje API

(reference-overview)=
## Przegląd

Ta sekcja zawiera kompletną dokumentację referencyjną API OTClientV8, obejmującą:

* **C++ API** - klasy silnika, typy, funkcje
* **Events System** - zdarzenia i sygnały
* **Modules** - system modułów Lua
* **UI Components** - widgety i OTUI

(reference-quick-links)=
## Szybkie odnośniki

### Dla programistów C++
* [Creature API](api.md#api-creature) - zarządzanie stworzeniami
* [Player API](api.md#api-player) - API gracza
* [Map API](api.md#api-map) - operacje na mapie
* [Network API](api.md#api-protocol) - protokół sieciowy

### Dla skrypterów Lua
* [Global Functions](modules.md#module-corelib) - funkcje globalne
* [Event Handlers](events.md#events-connection) - obsługa zdarzeń
* [Module System](modules.md#modules-loading) - ładowanie modułów
* [UI Manipulation](ui.md#ui-lua-api) - tworzenie i manipulacja UI

### Dla designerów UI
* [OTUI Syntax](ui.md#ui-otui-syntax) - składnia OTUI
* [Widget Types](ui.md#ui-index) - typy widgetów
* [Styling](ui.md#ui-styling) - stylowanie komponentów
* [Layouts](ui.md#ui-layouts) - systemy układów

(reference-symbol-index)=
## Index symboli (A-Z)

### A
* `addEvent()` - [Modules: addEvent](modules.md#func-addEvent)
* `anchors` - [UI: Anchors](ui.md#ui-anchors)

### C
* `connect()` - [Events: Connection](events.md#events-connection)
* `Creature` - [API: Creature](api.md#api-creature)
* `cycleEvent()` - [Modules: cycleEvent](modules.md#func-cycleEvent)

### D
* `disconnect()` - [Events: Disconnection](events.md#events-connection)

### G
* `g_game` - [API: Game](api.md#api-game)
* `g_map` - [API: Map](api.md#api-map)
* `g_modules` - [Modules: Loading](modules.md#modules-loading)
* `g_ui` - [UI: Lua API](ui.md#ui-lua-api)

### L
* `LocalPlayer` - [API: Player](api.md#api-player)

### O
* `onCreatureAppear` - [Events: onCreatureAppear](events.md#event-onCreatureAppear)
* `onGameStart` - [Events: onGameStart](events.md#event-onGameStart)
* `onHealthChange` - [Events: onHealthChange](events.md#event-onHealthChange)
* `onLogin` - [Events: onLogin](events.md#event-onLogin)
* `onTextMessage` - [Events: onTextMessage](events.md#event-onTextMessage)

### P
* `Player` - [API: Player](api.md#api-player)

### S
* `scheduleEvent()` - [Modules: scheduleEvent](modules.md#func-scheduleEvent)

### U
* `UIButton` - [UI: Button](ui.md#ui-button)
* `UIWidget` - [UI: Widget](ui.md#ui-widget)
* `UIWindow` - [UI: Window](ui.md#ui-window)

(reference-by-category)=
## Symbole według kategorii

### Core System
* [Event System](events.md) - asynchroniczna komunikacja
* [Module Loader](modules.md#modules-loading) - ładowanie modułów
* [Scheduler](modules.md#func-scheduleEvent) - planowanie zadań

### Game Logic
* [Creature Management](api.md#api-creature) - stworzenia
* [Player Control](api.md#api-player) - sterowanie graczem
* [Map Operations](api.md#api-map) - operacje na mapie
* [Item Handling](api.md#api-item) - zarządzanie przedmiotami

### UI Framework
* [Widget System](ui.md#ui-widget-hierarchy) - hierarchia widgetów
* [Layout Management](ui.md#ui-layouts) - układy
* [Event Handling](ui.md#ui-lua-api) - eventy UI
* [Styling](ui.md#ui-styling) - stylowanie

### Network
* [Protocol](api.md#api-protocol) - protokół komunikacji
* [Connection Management](api.md#api-connection) - zarządzanie połączeniem

(reference-conventions)=
## Konwencje dokumentacji

### Typy parametrów

* `string` - ciąg znaków
* `number` - liczba (int lub float)
* `boolean` - wartość logiczna
* `table` - tabela Lua
* `function` - funkcja/callback
* `userdata` - obiekt C++ (np. Creature, Player)

### Opcjonalność

* `param` - parametr wymagany
* `param (optional)` - parametr opcjonalny
* `param = default` - parametr z wartością domyślną

### Przykłady kodu

Wszystkie przykłady są testowalne i mogą być użyte bezpośrednio w projekcie.

(reference-navigation)=
## Nawigacja

:::{toctree}
:maxdepth: 2
:caption: Sekcje referencyjne
=======
# Referencje / API

W tej sekcji umieszczaj szczegółowe API modułów, klas i funkcji.
Możesz dzielić pliki na mniejsze jednostki — ten folder jest wciągany via glob.
>>>>>>> Stashed changes

=======
# Referencje / API

W tej sekcji umieszczaj szczegółowe API modułów, klas i funkcji.
Możesz dzielić pliki na mniejsze jednostki — ten folder jest wciągany via glob.

>>>>>>> Stashed changes
=======
# Referencje / API

W tej sekcji umieszczaj szczegółowe API modułów, klas i funkcji.
Możesz dzielić pliki na mniejsze jednostki — ten folder jest wciągany via glob.

>>>>>>> Stashed changes
=======
# Referencje / API

W tej sekcji umieszczaj szczegółowe API modułów, klas i funkcji.
Możesz dzielić pliki na mniejsze jednostki — ten folder jest wciągany via glob.

>>>>>>> Stashed changes
=======
# Referencje / API

W tej sekcji umieszczaj szczegółowe API modułów, klas i funkcji.
Możesz dzielić pliki na mniejsze jednostki — ten folder jest wciągany via glob.

>>>>>>> Stashed changes
=======
# Referencje / API

W tej sekcji umieszczaj szczegółowe API modułów, klas i funkcji.
Możesz dzielić pliki na mniejsze jednostki — ten folder jest wciągany via glob.

>>>>>>> Stashed changes
:::tip
Używaj nagłówków **H2/H3/H4**, aby Sphinx poprawnie zbudował lokalny spis treści.
:::

(reference-see-also)=
## Zobacz też

* [Chapters](../chapters/01_specyfikacja.md) - dokumentacja opisowa
* [Examples](../examples/diagrams.md) - przykłady i diagramy
* [Datasets](../datasets/index.md) - dane i zasoby
