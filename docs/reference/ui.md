# UI Reference

(ui-overview)=
## Przegląd systemu UI

System UI w OTClientV8 wykorzystuje deklaratywny język OTUI do definiowania interfejsu użytkownika. OTUI jest podobny do CSS i umożliwia tworzenie hierarchicznych układów widgetów.

(ui-widget-hierarchy)=
## Hierarchia widgetów

```{mermaid}
graph TD
    UIWidget[UIWidget - bazowa klasa]
    UIWidget --> UIButton[UIButton]
    UIWidget --> UILabel[UILabel]
    UIWidget --> UITextEdit[UITextEdit]
    UIWidget --> UIWindow[UIWindow]
    UIWidget --> UICheckBox[UICheckBox]
    UIWidget --> UIScrollArea[UIScrollArea]
    UIWidget --> UICreature[UICreature]
    UIWidget --> UIItem[UIItem]
    UIWidget --> UIMap[UIMap]
    
    UIWindow --> UIMiniWindow[UIMiniWindow]
    UIScrollArea --> UIList[UIList]
    
    style UIWidget fill:#ff9800
    style UIWindow fill:#4caf50
    style UIMap fill:#2196f3
```

(ui-index)=
## Index komponentów

### Podstawowe widgety
* [UIWidget](#ui-widget) - bazowy widget
* [UIButton](#ui-button) - przycisk
* [UILabel](#ui-label) - etykieta tekstowa
* [UITextEdit](#ui-textedit) - pole tekstowe
* [UICheckBox](#ui-checkbox) - checkbox

### Kontenery
* [UIWindow](#ui-window) - okno
* [UIMiniWindow](#ui-miniwindow) - mini okno
* [UIScrollArea](#ui-scrollarea) - obszar przewijalny
* [UIList](#ui-list) - lista

### Specjalne widgety
* [UICreature](#ui-creature) - widget stworzenia
* [UIItem](#ui-item) - widget przedmiotu
* [UIMap](#ui-map) - widget mapy

(ui-otui-syntax)=
## Składnia OTUI

### Podstawowa struktura

```yaml
WidgetType
  id: uniqueId
  anchors.top: parent.top
  anchors.left: parent.left
  size: 100 30
  text: Button Text
  @onClick: onButtonClick()
  
  ChildWidget
    id: child1
    anchors.fill: parent
```

### Właściwości (properties)

```yaml
# Rozmiar i pozycja
size: 100 50
width: 100
height: 50

# Anchors (kotewki)
anchors.top: parent.top
anchors.left: parent.left
anchors.right: parent.right
anchors.bottom: parent.bottom
anchors.fill: parent
anchors.centerIn: parent

# Marginesy
margin: 5
margin-top: 10
margin-left: 5

# Tekst
text: Hello World
font: verdana-11px-antialised
text-color: #FFFFFF

# Tło i obrazy
background: #000000
background-color: #FFFFFF
image-source: /images/button.png
image-border: 3

# Zachowanie
visible: true
enabled: true
focusable: true
```

### Eventy i handlers

```yaml
Button
  @onClick: modules.mymodule.onButtonClick()
  @onHoverChange: modules.mymodule.onHover()
  @onKeyPress: modules.mymodule.onKey()
```

(ui-button)=
## UIButton

Przycisk z tekstem lub obrazem.

### Przykład OTUI

```yaml
Button
  id: myButton
  text: Click Me
  size: 100 30
  anchors.top: parent.top
  anchors.horizontalCenter: parent.horizontalCenter
  @onClick: onButtonClick()
```

### Stany przycisku

```yaml
Button
  # Stan normalny
  background-color: #404040
  text-color: #FFFFFF
  
  # Stan hover
  $hover:
    background-color: #505050
  
  # Stan wciśnięty
  $pressed:
    background-color: #303030
  
  # Stan disabled
  $disabled:
    background-color: #202020
    text-color: #808080
```

(ui-window)=
## UIWindow

Okno z tytułem i możliwością zamykania/minimalizacji.

### Przykład OTUI

```{literalinclude} ../../modules/game_battle/battle.otui
:language: yaml
:caption: `modules/game_battle/battle.otui` - Battle window example
:linenos:
:lines: 39-50
```

### Właściwości okna

```yaml
MiniWindow
  id: myWindow
  !text: tr('Window Title')
  size: 300 200
  @onClose: modules.mymodule.onClose()
  &save: true       # Zapisz pozycję
  &autoOpen: true   # Otwórz automatycznie
```

(ui-textedit)=
## UITextEdit

Pole edycji tekstu.

### Przykład

```yaml
TextEdit
  id: nameInput
  size: 200 20
  anchors.top: parent.top
  anchors.left: parent.left
  text: Enter name...
  max-length: 20
  @onTextChange: onNameChange()
```

(ui-lua-api)=
## API Lua dla UI

### Tworzenie widgetów

```lua
-- Utworzenie przycisku
local button = g_ui.createWidget('Button', parentWidget)
button:setText('Click Me')
button:setSize({100, 30})

-- Załadowanie OTUI
local window = g_ui.loadUI('mywindow.otui', parentWidget)

-- Znalezienie widgetu
local button = window:getChildById('myButton')
local label = window:recursiveGetChildById('statusLabel')
```

### Manipulacja widgetami

```lua
-- Pokazywanie/ukrywanie
widget:show()
widget:hide()
widget:setVisible(true)

-- Włączanie/wyłączanie
widget:setEnabled(true)
widget:setEnabled(false)

-- Pozycja i rozmiar
widget:setPosition({x = 100, y = 50})
widget:setSize({width = 200, height = 100})
widget:resize(200, 100)

-- Tekst
widget:setText('New text')
local text = widget:getText()

-- Kolor
widget:setColor('#FF0000')
widget:setBackgroundColor('#000000')

-- Niszczenie
widget:destroy()
```

### Event handling

```lua
-- onClick
button.onClick = function(widget)
    print('Button clicked!', widget:getId())
end

-- onTextChange
textEdit.onTextChange = function(widget, text)
    print('Text changed:', text)
end

-- onKeyPress
widget.onKeyPress = function(widget, keyCode, keyText)
    if keyCode == KeyEscape then
        widget:hide()
        return true -- Event handled
    end
    return false
end
```

(ui-layouts)=
## Układy (Layouts)

### Vertical Layout

```yaml
Panel
  layout:
    type: verticalBox
    spacing: 5
    fit-children: true
  
  Button
    text: Button 1
  Button
    text: Button 2
  Button
    text: Button 3
```

### Horizontal Layout

```yaml
Panel
  layout:
    type: horizontalBox
    spacing: 10
  
  Label
    text: Name:
  TextEdit
    id: nameInput
```

### Grid Layout

```yaml
Panel
  layout:
    type: grid
    cell-size: 32 32
    cell-spacing: 2
    num-columns: 8
    num-lines: 6
```

(ui-anchors)=
## Zaawansowane kotwice

### Centrowanie

```yaml
Widget
  # Centrum poziome
  anchors.horizontalCenter: parent.horizontalCenter
  
  # Centrum pionowe
  anchors.verticalCenter: parent.verticalCenter
  
  # Centrum w obu osiach
  anchors.centerIn: parent
```

### Relatywne kotwice

```yaml
Widget1
  id: first
  
Widget2
  # Umieszczenie poniżej Widget1
  anchors.top: first.bottom
  anchors.left: first.left
  margin-top: 5
```

(ui-styling)=
## Stylowanie

### Definiowanie stylów

```yaml
# Plik: styles/buttons.otui
CustomButton < Button
  size: 100 30
  background-color: #404040
  text-color: #FFFFFF
  font: verdana-11px-antialised
  
  $hover:
    background-color: #505050

# Użycie
CustomButton
  id: myButton
  text: Custom Styled
```

(ui-best-practices)=
## Dobre praktyki

1. **ID unikalne** - używaj unikalnych ID dla widgetów
2. **Stylowanie** - definiuj style wielokrotnego użytku
3. **Anchors** - preferuj anchors nad absolutnym pozycjonowaniem
4. **Layouts** - używaj layoutów dla automatycznego układania
5. **Cleanup** - niszcz widgety gdy nie są potrzebne
6. **Translation** - używaj `tr()` dla tekstów do tłumaczenia
7. **Resources** - przechowuj obrazy w `/images/`

(ui-example-complete)=
## Kompletny przykład

```yaml
# mywindow.otui
MiniWindow
  id: myWindow
  !text: tr('My Window')
  size: 400 300
  @onClose: modules.mymodule.onWindowClose()
  
  Panel
    id: contentPanel
    anchors.fill: parent
    margin: 5
    layout:
      type: verticalBox
      spacing: 5
    
    Label
      text: Enter your name:
      font: verdana-11px-antialised
    
    TextEdit
      id: nameInput
      height: 20
      max-length: 30
      @onTextChange: modules.mymodule.onNameChange()
    
    Panel
      height: 30
      layout:
        type: horizontalBox
        spacing: 5
      
      Button
        id: okButton
        !text: tr('OK')
        @onClick: modules.mymodule.onOk()
      
      Button
        id: cancelButton
        !text: tr('Cancel')
        @onClick: modules.mymodule.onCancel()
```

### Obsługa Lua

```lua
-- mymodule.lua
local window

function init()
    window = g_ui.loadUI('mywindow.otui', modules.game_interface.getRightPanel())
end

function terminate()
    if window then
        window:destroy()
        window = nil
    end
end

function onNameChange(widget, text)
    print('Name changed to:', text)
    -- Walidacja
    local okButton = window:recursiveGetChildById('okButton')
    okButton:setEnabled(#text > 0)
end

function onOk()
    local nameInput = window:recursiveGetChildById('nameInput')
    local name = nameInput:getText()
    
    if #name > 0 then
        print('Name entered:', name)
        window:hide()
    end
end

function onCancel()
    window:hide()
end

function onWindowClose()
    -- Cleanup przy zamknięciu
    print('Window closed')
end
```

(ui-see-also)=
## Zobacz też

* [API Reference](api.md) - C++ API
* [Modules Reference](modules.md) - system modułów
* [Chapter: UI](../chapters/04_ui.md) - pełna dokumentacja UI
* [Examples: Diagrams](../examples/diagrams.md#diagram-ui-hierarchy) - diagram hierarchii UI
