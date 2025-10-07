# Presety Kanoniczne - OTClient v8 Core (OTUI + TypeScript + Lua)

**Paleta:** `otc_core_v1`  **Wersja:** 1.0\
**Cel:** Minimalne, **kanoniczne** presety dla kaLLdego komponentu z palety "OTClient v8 Core", w 100% zgodne z taksonomia (rozdz. 4 specyfikacji) oraz zasadami **STRICT OTUI**.

> **Konwencje**
>
> - Wszystkie bloki **OTUI sa STRICT**: koL"ce linii LF, **wciecia = 2 spacje**, **brak komentarzy**.
> - Serializator emituje atrybuty w kolejnoLci **GEOMETRIA a' STYL a' ZACHOWANIE** i mapuje `style.text` a' `!text: tr('...')`.
> - Bloki **TypeScript (TS)** zakL'adaja AST w ksztaL'cie `WidgetNode` oraz serializer zgodny z powyLLszymi zasadami.

---
## Spis treLci

- [A. Windows (Okna GL'owne)](#a-windows-okna-gL'owne)
  - [A.1 MainWindow](#a1-mainwindow)
  - [A.2 StaticMainWindow](#a2-staticmainwindow)
  - [A.3 MiniWindow](#a3-miniwindow)
  - [A.4 ContainerWindow](#a4-containerwindow)
  - [A.5 DialogWindow](#a5-dialogwindow)
- [B. Layout & Organization (UkL'ad i Organizacja)](#b-layout--organization-ukL'ad-i-organizacja)
  - [B.1 UIWidget (alias: Widget)](#b1-uiwidget-alias-widget)
  - [B.2 Panel](#b2-panel)
  - [B.3 GroupBox](#b3-groupbox)
  - [B.4 Titlebar](#b4-titlebar)
  - [B.5 Toolbar](#b5-toolbar)
  - [B.6 TabBar](#b6-tabbar)
  - [B.7 TabWidget](#b7-tabwidget)
  - [B.8 Splitter (2 dzieci)](#b8-splitter-2-dzieci)
  - [B.9 HorizontalSeparator](#b9-horizontalseparator)
  - [B.10 StatusOverlay](#b10-statusoverlay)
- [C. Input Controls (Kontrolki WejLciowe)](#c-input-controls-kontrolki-wejLciowe)
  - [C.1 Button](#c1-button)
  - [C.2 CheckBox](#c2-checkbox)
  - [C.2a RoundCheckBox (wariant CheckBox)](#c2a-roundcheckbox-wariant-checkbox)
  - [C.3 TextEdit](#c3-textedit)
  - [C.4 PasswordTextEdit](#c4-passwordtextedit)
  - [C.5 MultilineTextEdit (+ Scroll)](#c5-multilinetextedit--scroll)
  - [C.6 ComboBox](#c6-combobox)
- [D. Data Display (WyLwietlanie Danych)](#d-data-display-wyLwietlanie-danych)
  - [D.1 Label (alias: UILabel)](#d1-label-alias-uilabel)
  - [D.2 TextList (+ Scroll)](#d2-textlist--scroll)
  - [D.3 ProgressBar](#d3-progressbar)
- [E. Indicators & Scrolling (WskaLsniki i Przewijanie)](#e-indicators--scrolling-wskaLsniki-i-przewijanie)
  - [E.1 VerticalScrollBar](#e1-verticalscrollbar)
  - [E.2 HorizontalScrollBar](#e2-horizontalscrollbar)
- [F. Uwagi implementacyjne (Sparky)](#f-uwagi-implementacyjne-sparky)
- [G. Lua - OTUI jako string + glue (kontrolery)](#g-lua--otui-jako-string--glue-kontrolery)
  - [G.1 MiniWindow - Lua](#g1-miniwindow--lua)
  - [G.2 ContainerWindow - Lua](#g2-containerwindow--lua)
  - [G.3 DialogWindow - Lua](#g3-dialogwindow--lua)
  - [G.4 Wrappers: TextList / MultilineTextEdit](#g4-wrappers-textlist--multilinetextedit)
  - [G.5 Wzorzec integracyjny](#g5-wzorzec-integracyjny)

---
## A. Windows (Okna GL'owne)
## A.1 MainWindow

**OTUI**

MainWindow
  id: main
  size: 320 220
  background-color: alpha

  UIWidget
    id: content
    anchors.fill: parent
    padding: 6
```

**TypeScript (TS)**

export function presetMainWindow(): WidgetNode {
  return {
    base: 'MainWindow',
    geometry: { id: 'main', size: [320, 220] },
    style: { backgroundColor: 'alpha' },
    children: [
      { base: 'UIWidget', geometry: { id: 'content', anchors: { fill: 'parent' }, padding: 6 } }
]
};
}
```
## A.2 StaticMainWindow

**OTUI**

StaticMainWindow
  id: staticMain
  size: 320 220
  background-color: alpha

  UIWidget
    id: content
    anchors.fill: parent
    padding: 6
```

**TypeScript (TS)**

export function presetStaticMainWindow(): WidgetNode {
  return {
    base: 'StaticMainWindow',
    geometry: { id: 'staticMain', size: [320, 220] },
    style: { backgroundColor: 'alpha' },
    children: [
      { base: 'UIWidget', geometry: { id: 'content', anchors: { fill: 'parent' }, padding: 6 } }
]
};
}
```
## A.3 MiniWindow

**OTUI**

MiniWindow < MainWindow
  id: mini
  size: 260 180
  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Mini Window')

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 6

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28
```

**TypeScript (TS)**

export function presetMiniWindow(): WidgetNode {
  return {
    base: 'MiniWindow',
    extends: 'MainWindow',
    geometry: { id: 'mini', size: [260, 180] },
    style: { backgroundColor: 'alpha' },
    children: [
      { base: 'UIWidget', geometry: { id: 'titlebar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { text: 'Mini Window', textAutoResize: true } },
        { base: 'Button', geometry: { id: 'minimizeBtn', anchors: { right: 'closeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: '-' } },
        { base: 'Button', geometry: { id: 'closeBtn', anchors: { right: 'parent.right', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: 'x' } }
      ] },
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'parent.right', top: 'titlebar.bottom', bottom: 'footer.top' }, padding: 6 } },
      { base: 'UIWidget', geometry: { id: 'footer', anchors: { left: 'parent.left', right: 'parent.right', bottom: 'parent.bottom' }, height: 28 } }
]
};
}
```
## A.4 ContainerWindow

**OTUI**

ContainerWindow < MainWindow
  id: container
  size: 300 220
  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Container')

    Button
      id: backBtn
      anchors.right: pinBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('<')

    Button
      id: pinBtn
      anchors.right: minimizeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('*')

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: parent.bottom
    padding: 6
```

**TypeScript (TS)**

export function presetContainerWindow(): WidgetNode {
  return {
    base: 'ContainerWindow',
    extends: 'MainWindow',
    geometry: { id: 'container', size: [300, 220] },
    style: { backgroundColor: 'alpha' },
    children: [
      { base: 'UIWidget', geometry: { id: 'titlebar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { text: 'Container', textAutoResize: true } },
        { base: 'Button', geometry: { id: 'backBtn', anchors: { right: 'pinBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 20 }, style: { text: '<' } },
        { base: 'Button', geometry: { id: 'pinBtn', anchors: { right: 'minimizeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 20 }, style: { text: '*' } },
        { base: 'Button', geometry: { id: 'minimizeBtn', anchors: { right: 'closeBtn.left', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: '-' } },
        { base: 'Button', geometry: { id: 'closeBtn', anchors: { right: 'parent.right', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: 'x' } }
      ] },
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'parent.right', top: 'titlebar.bottom', bottom: 'parent.bottom' }, padding: 6 } }
]
};
}
```
## A.5 DialogWindow

**OTUI**

DialogWindow < MainWindow
  id: dialog
  size: 260 160
  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Dialog')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 6

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28

    Button
      id: okButton
      anchors.right: cancelButton.left
      anchors.bottom: parent.bottom
      width: 64
      margin-right: 8
      !text: tr('Ok')

    Button
      id: cancelButton
      anchors.right: parent.right
      anchors.bottom: parent.bottom
      width: 64
      margin-right: 8
      !text: tr('Cancel')
```

**TypeScript (TS)**

export function presetDialogWindow(): WidgetNode {
  return {
    base: 'DialogWindow',
    extends: 'MainWindow',
    geometry: { id: 'dialog', size: [260, 160] },
    style: { backgroundColor: 'alpha' },
    children: [
      { base: 'UIWidget', geometry: { id: 'titlebar', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 20 }, children: [
        { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { text: 'Dialog', textAutoResize: true } }
      ] },
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'parent.right', top: 'titlebar.bottom', bottom: 'footer.top' }, padding: 6 } },
      { base: 'UIWidget', geometry: { id: 'footer', anchors: { left: 'parent.left', right: 'parent.right', bottom: 'parent.bottom' }, height: 28 }, children: [
        { base: 'Button', geometry: { id: 'okButton', anchors: { right: 'cancelButton.left', bottom: 'parent.bottom' }, width: 64, marginRight: 8 }, style: { text: 'Ok' } },
        { base: 'Button', geometry: { id: 'cancelButton', anchors: { right: 'parent.right', bottom: 'parent.bottom' }, width: 64, marginRight: 8 }, style: { text: 'Cancel' } }
      ] }
]
};
}
```

---
## B. Layout & Organization (UkL'ad i Organizacja)
## B.1 UIWidget (alias: Widget)

**OTUI**

UIWidget
  id: w
  size: 100 60
  background-color: alpha
```

**TypeScript (TS)**

export function presetUIWidget(): WidgetNode {
  return { base: 'UIWidget', geometry: { id: 'w', size: [100, 60] }, style: { backgroundColor: 'alpha' } };
}
```
## B.2 Panel

**OTUI**

Panel
  id: panel
  anchors.fill: parent
  padding: 6
```

**TypeScript (TS)**

export function presetPanel(): WidgetNode {
  return { base: 'Panel', geometry: { id: 'panel', anchors: { fill: 'parent' }, padding: 6 } };
}
```
## B.3 GroupBox

**OTUI**

GroupBox
  id: group
  size: 220 120

  UIWidget
    id: header
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 18

    Label
      id: caption
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Group')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: header.bottom
    anchors.bottom: parent.bottom
    padding: 6
```

**TypeScript (TS)**

export function presetGroupBox(): WidgetNode {
  return {
    base: 'GroupBox',
    geometry: { id: 'group', size: [220, 120] },
    children: [
      { base: 'UIWidget', geometry: { id: 'header', anchors: { left: 'parent.left', right: 'parent.right', top: 'parent.top' }, height: 18 }, children: [
        { base: 'Label', geometry: { id: 'caption', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { textAutoResize: true, text: 'Group' } }
      ] },
      { base: 'UIWidget', geometry: { id: 'content', anchors: { left: 'parent.left', right: 'parent.right', top: 'header.bottom', bottom: 'parent.bottom' }, padding: 6 } }
]
};
}
```
## B.4 Titlebar

**OTUI**

Titlebar
  id: tb
  size: 200 20

  Label
    id: title
    anchors.left: parent.left
    anchors.verticalCenter: parent.verticalCenter
    margin-left: 6
    text-auto-resize: true
    !text: tr('Title')

  Button
    id: closeBtn
    anchors.right: parent.right
    anchors.verticalCenter: parent.verticalCenter
    width: 16
    !text: tr('x')
```

**TypeScript (TS)**

export function presetTitlebar(): WidgetNode {
  return {
    base: 'Titlebar',
    geometry: { id: 'tb', size: [200, 20] },
    children: [
      { base: 'Label', geometry: { id: 'title', anchors: { left: 'parent.left', verticalCenter: 'parent.verticalCenter' }, marginLeft: 6 }, style: { text: 'Title', textAutoResize: true } },
      { base: 'Button', geometry: { id: 'closeBtn', anchors: { right: 'parent.right', verticalCenter: 'parent.verticalCenter' }, width: 16 }, style: { text: 'x' } }
]
};
}
```
## B.5 Toolbar

**OTUI**

Toolbar
  id: tools
  size: 200 22

  Button
    id: action1
    width: 20
    !text: tr('A')

  HorizontalSeparator
    id: sep
    size: 2 20

  Button
    id: action2
    width: 20
    !text: tr('B')
```

**TypeScript (TS)**

export function presetToolbar(): WidgetNode {
  return {
    base: 'Toolbar',
    geometry: { id: 'tools', size: [200, 22] },
    children: [
      { base: 'Button', geometry: { id: 'action1', width: 20 }, style: { text: 'A' } },
      { base: 'HorizontalSeparator', geometry: { id: 'sep', size: [2, 20] } },
      { base: 'Button', geometry: { id: 'action2', width: 20 }, style: { text: 'B' } }
]
};
}
```
## B.6 TabBar

**OTUI**

TabBar
  id: tabbar
  size: 220 22

  Button
    id: tab1
    width: 60
    !text: tr('Tab 1')

  Button
    id: tab2
    anchors.left: tab1.right
    width: 60
    !text: tr('Tab 2')
```

**TypeScript (TS)**

export function presetTabBar(): WidgetNode {
  return {
    base: 'TabBar',
    geometry: { id: 'tabbar', size: [220, 22] },
    children: [
      { base: 'Button', geometry: { id: 'tab1', width: 60 }, style: { text: 'Tab 1' } },
      { base: 'Button', geometry: { id: 'tab2', anchors: { left: 'tab1.right' }, width: 60 }, style: { text: 'Tab 2' } }
]
};
}
```
## B.7 TabWidget

**OTUI**

TabWidget
  id: tabcontent
  anchors.fill: parent
```

**TypeScript (TS)**

export function presetTabWidget(): WidgetNode {
  return { base: 'TabWidget', geometry: { id: 'tabcontent', anchors: { fill: 'parent' } } };
}
```
## B.8 Splitter (2 dzieci)

**OTUI**

Splitter
  id: split
  size: 300 160

  Panel
    id: left
    anchors.left: parent.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    width: 140

  Panel
    id: right
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    width: 140
```

**TypeScript (TS)**

export function presetSplitter(): WidgetNode {
  return {
    base: 'Splitter',
    geometry: { id: 'split', size: [300, 160] },
    children: [
      { base: 'Panel', geometry: { id: 'left', anchors: { left: 'parent.left', top: 'parent.top', bottom: 'parent.bottom' }, width: 140 } },
      { base: 'Panel', geometry: { id: 'right', anchors: { right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' }, width: 140 } }
]
};
}
```
## B.9 HorizontalSeparator

**OTUI**

HorizontalSeparator
  id: hsep
  size: 200 2
```

**TypeScript (TS)**

export function presetHorizontalSeparator(): WidgetNode {
  return { base: 'HorizontalSeparator', geometry: { id: 'hsep', size: [200, 2] } };
}
```
## B.10 StatusOverlay

**OTUI**

StatusOverlay
  id: overlay
  size: 240 80

  Label
    id: message
    anchors.left: parent.left
    anchors.right: parent.right
    !text: tr('Working...')

  ProgressBar
    id: progress
    anchors.left: parent.left
    anchors.right: cancel.left
    anchors.top: message.bottom
    margin-top: 6

  Button
    id: cancel
    anchors.right: parent.right
    anchors.top: message.bottom
    width: 64
    margin-top: 6
    !text: tr('Cancel')
```

**TypeScript (TS)**

export function presetStatusOverlay(): WidgetNode {
  return {
    base: 'StatusOverlay',
    geometry: { id: 'overlay', size: [240, 80] },
    children: [
      { base: 'Label', geometry: { id: 'message', anchors: { left: 'parent.left', right: 'parent.right' } }, style: { text: 'Working...' } },
      { base: 'ProgressBar', geometry: { id: 'progress', anchors: { left: 'parent.left', right: 'cancel.left', top: 'message.bottom' }, marginTop: 6 } },
      { base: 'Button', geometry: { id: 'cancel', anchors: { right: 'parent.right', top: 'message.bottom' }, width: 64, marginTop: 6 }, style: { text: 'Cancel' } }
]
};
}
```

---
## C. Input Controls (Kontrolki WejLciowe)
## C.1 Button

**OTUI**

Button
  id: btn
  width: 64
  !text: tr('Ok')
```

**TypeScript (TS)**

export function presetButton(): WidgetNode {
  return { base: 'Button', geometry: { id: 'btn', width: 64 }, style: { text: 'Ok' } };
}
```
## C.2 CheckBox

**OTUI**

CheckBox
  id: check
  width: 16
```

**TypeScript (TS)**

export function presetCheckBox(): WidgetNode {
  return { base: 'CheckBox', geometry: { id: 'check', width: 16 } };
}
```
## C.2a RoundCheckBox (wariant CheckBox)

**OTUI**

CheckBox
  id: roundCheck
  width: 16
```

**TypeScript (TS)**

export function presetRoundCheckBox(): WidgetNode {
  return { base: 'CheckBox', geometry: { id: 'roundCheck', width: 16 }, variant: 'RoundCheckBox' } as any;
}
```
## C.3 TextEdit

**OTUI**

TextEdit
  id: edit
  width: 120
```

**TypeScript (TS)**

export function presetTextEdit(): WidgetNode {
  return { base: 'TextEdit', geometry: { id: 'edit', width: 120 } };
}
```
## C.4 PasswordTextEdit

**OTUI**

PasswordTextEdit
  id: pass
  width: 120
```

**TypeScript (TS)**

export function presetPasswordTextEdit(): WidgetNode {
  return { base: 'PasswordTextEdit', geometry: { id: 'pass', width: 120 } };
}
```
## C.5 MultilineTextEdit (+ Scroll)

**OTUI**

UIWidget
  id: wrapMultiline
  size: 220 120

  MultilineTextEdit
    id: multi
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    step: 16
```

**TypeScript (TS)**

export function presetMultilineTextEdit(): WidgetNode {
  return {
    base: 'UIWidget',
    geometry: { id: 'wrapMultiline', size: [220, 120] },
    children: [
      { base: 'MultilineTextEdit', geometry: { id: 'multi', anchors: { left: 'parent.left', right: 'scroll.left', top: 'parent.top', bottom: 'parent.bottom' } } },
      { base: 'VerticalScrollBar', geometry: { id: 'scroll', anchors: { right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' } }, behavior: { step: 16 } as any }
]
};
}
```
## C.6 ComboBox

**OTUI**

ComboBox
  id: combo
  width: 120
```

**TypeScript (TS)**

export function presetComboBox(): WidgetNode {
  return { base: 'ComboBox', geometry: { id: 'combo', width: 120 } };
}
```

---
## D. Data Display (WyLwietlanie Danych)
## D.1 Label (alias: UILabel)

**OTUI**

Label
  id: label
  text-wrap: true
  !text: tr('Label')
```

**TypeScript (TS)**

export function presetLabel(): WidgetNode {
  return { base: 'Label', geometry: { id: 'label' }, style: { text: 'Label', textWrap: true } };
}
```
## D.2 TextList (+ Scroll)

**OTUI**

UIWidget
  id: wrapList
  size: 220 140

  TextList
    id: list
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    step: 16
```

**TypeScript (TS)**

export function presetTextList(): WidgetNode {
  return {
    base: 'UIWidget',
    geometry: { id: 'wrapList', size: [220, 140] },
    children: [
      { base: 'TextList', geometry: { id: 'list', anchors: { left: 'parent.left', right: 'scroll.left', top: 'parent.top', bottom: 'parent.bottom' } } },
      { base: 'VerticalScrollBar', geometry: { id: 'scroll', anchors: { right: 'parent.right', top: 'parent.top', bottom: 'parent.bottom' } }, behavior: { step: 16 } as any }
]
};
}
```
## D.3 ProgressBar

**OTUI**

ProgressBar
  id: progress
  size: 200 14
```

**TypeScript (TS)**

export function presetProgressBar(): WidgetNode {
  return { base: 'ProgressBar', geometry: { id: 'progress', size: [200, 14] } };
}
```

---
## E. Indicators & Scrolling (WskaLsniki i Przewijanie)
## E.1 VerticalScrollBar

**OTUI**

VerticalScrollBar
  id: vscroll
  height: 120
  step: 16
```

**TypeScript (TS)**

export function presetVerticalScrollBar(): WidgetNode {
  return { base: 'VerticalScrollBar', geometry: { id: 'vscroll', height: 120 }, behavior: { step: 16 } as any };
}
```
## E.2 HorizontalScrollBar

**OTUI**

HorizontalScrollBar
  id: hscroll
  width: 200
  step: 16
```

**TypeScript (TS)**

export function presetHorizontalScrollBar(): WidgetNode {
  return { base: 'HorizontalScrollBar', geometry: { id: 'hscroll', width: 200 }, behavior: { step: 16 } as any };
}
```

---
## F. Uwagi implementacyjne (Sparky)

- Presety sa **minimalne**: zachowuja sloty, parowanie (TextList/Multiline a" ScrollBar) i deterministyczna strukture do serializacji.
- Gdy wymagana jest para przewijania, uLLywaj **sasiadujacych** (sibling) `VerticalScrollBar`/`HorizontalScrollBar` oraz odpowiednich kotwic `right: scroll.left` / `bottom: hscroll.top`.
- Presety okien zawieraja `titlebar` (Mini/Container/Dialog) oraz minimalne `content`/`footer`.
- **TypeScript** moLLe wstrzykiwac zdarzenia (`@onEnter/@onEscape/@onClick`) w generatorach, lecz celowo ich tu nie dodano, aby presety pozostaL'y neutralne.
- Serializer musi zapewnic **STRICT OTUI** oraz konwersje `style.text` a' `!text: tr('...')`.

---
## G. Lua - OTUI jako string + glue (kontrolery)

> **Cel:** dodac do presetow trzeci filar - **Lua**, ktory zawiera: (1) kanoniczny blok **OTUI jako string** (STRICT, bez komentarzy w samym OTUI), (2) minimalistyczny **glue** (kontrolery/wywoL'ania) spojny z presetami.
>
> **WaLLne:** w runtime uLLywaj **plikow** i `g_ui.displayUI('...')`. Bloki OTUI w Lua poniLLej sL'uLLa gL'ownie do **importu/eksportu** w edytorze.
## G.1 MiniWindow - Lua

**Lua (OTUI jako string - STRICT)**

local MiniWindow_OTUI = [[
MiniWindow < MainWindow
  id: mini
  size: 260 180
  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Mini Window')

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 6

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28
]]
```

**Lua (glue - kontroler i standardowe operacje)**

MiniWindowController = MiniWindowController or {}

function MiniWindowController.mountFromFile()
  local win = g_ui.displayUI('mini') -- w runtime uLLywaj plikow .otui
  MiniWindowController._wire(win)
  return win
end

function MiniWindowController._wire(win)
  if not win then return end
  local minimizeBtn = win:recursiveGetChildById('minimizeBtn')
  local closeBtn = win:recursiveGetChildById('closeBtn')
  if minimizeBtn then minimizeBtn.onClick = MiniWindowController.onToggleMinimize end
  if closeBtn then closeBtn.onClick = MiniWindowController.onClose end
end

function MiniWindowController.onToggleMinimize(btn)
  local win = btn and btn:getParent() and btn:getParent():getParent()
  if not win then return end
  local content = win:getChildById('content')
  local footer = win:getChildById('footer')
  if content then content:setVisible(not content:isVisible()) end
  if footer then footer:setVisible(not footer:isVisible()) end
end

function MiniWindowController.onClose(btn)
  local win = btn and btn:getParent() and btn:getParent():getParent()
  if win then win:hide() end
end
```
## G.2 ContainerWindow - Lua

**Lua (OTUI jako string - STRICT)**

local ContainerWindow_OTUI = [[
ContainerWindow < MainWindow
  id: container
  size: 300 220
  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Container')

    Button
      id: backBtn
      anchors.right: pinBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('<')

    Button
      id: pinBtn
      anchors.right: minimizeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 20
      !text: tr('*')

    Button
      id: minimizeBtn
      anchors.right: closeBtn.left
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('-')

    Button
      id: closeBtn
      anchors.right: parent.right
      anchors.verticalCenter: parent.verticalCenter
      width: 16
      !text: tr('x')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: parent.bottom
    padding: 6
]]
```

**Lua (glue - kontroler i standardowe operacje)**

ContainerController = ContainerController or {}

function ContainerController.mountFromFile()
  local win = g_ui.displayUI('container')
  ContainerController._wire(win)
  return win
end

function ContainerController._wire(win)
  if not win then return end
  local backBtn = win:recursiveGetChildById('backBtn')
  local pinBtn = win:recursiveGetChildById('pinBtn')
  local minBtn = win:recursiveGetChildById('minimizeBtn')
  local closeBtn = win:recursiveGetChildById('closeBtn')
  if backBtn then backBtn.onClick = ContainerController.onBack end
  if pinBtn then pinBtn.onClick = ContainerController.onTogglePin end
  if minBtn then minBtn.onClick = ContainerController.onToggleMinimize end
  if closeBtn then closeBtn.onClick = ContainerController.onClose end
end

function ContainerController.onBack(btn)
  local win = btn and btn:getParent() and btn:getParent():getParent()
  if win then win:hide() end -- docelowo: nawigacja wstecz
end

function ContainerController.onTogglePin(btn)
  -- docelowo: zmiana stanu przypiecia
end

function ContainerController.onToggleMinimize(btn)
  local win = btn and btn:getParent() and btn:getParent():getParent()
  if not win then return end
  local content = win:getChildById('content')
  if content then content:setVisible(not content:isVisible()) end
end

function ContainerController.onClose(btn)
  local win = btn and btn:getParent() and btn:getParent():getParent()
  if win then win:hide() end
end
```
## G.3 DialogWindow - Lua

**Lua (OTUI jako string - STRICT)**

local DialogWindow_OTUI = [[
DialogWindow < MainWindow
  id: dialog
  size: 260 160
  background-color: alpha

  UIWidget
    id: titlebar
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    height: 20

    Label
      id: title
      anchors.left: parent.left
      anchors.verticalCenter: parent.verticalCenter
      margin-left: 6
      text-auto-resize: true
      !text: tr('Dialog')

  UIWidget
    id: content
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: titlebar.bottom
    anchors.bottom: footer.top
    padding: 6

  UIWidget
    id: footer
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    height: 28

  Button
    id: okButton
    anchors.right: cancelButton.left
    anchors.bottom: parent.bottom
    width: 64
    margin-right: 8
    !text: tr('Ok')

  Button
    id: cancelButton
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    width: 64
    margin-right: 8
    !text: tr('Cancel')
]]
```

**Lua (glue - kontroler i standardowe operacje)**

DialogController = DialogController or {}

function DialogController.mountFromFile()
  local win = g_ui.displayUI('dialog')
  DialogController._wire(win)
  return win
end

function DialogController._wire(win)
  if not win then return end
  local okBtn = win:recursiveGetChildById('okButton')
  local cancelBtn = win:recursiveGetChildById('cancelButton')
  if okBtn then okBtn.onClick = DialogController.onOk end
  if cancelBtn then cancelBtn.onClick = DialogController.onCancel end
end

function DialogController.onOk(widget)
  local win = widget and widget:getParent() and widget:getParent():getParent()
  if win then win:hide() end
end

function DialogController.onCancel(widget)
  local win = widget and widget:getParent() and widget:getParent():getParent()
  if win then win:hide() end
end
```
## G.4 Wrappers: TextList / MultilineTextEdit

**Lua (OTUI dla MultilineTextEdit + VerticalScrollBar)**

local MultilineWrapper_OTUI = [[
UIWidget
  id: wrapMultiline
  size: 220 120

  MultilineTextEdit
    id: multi
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    step: 16
]]
```

**Lua (OTUI dla TextList + VerticalScrollBar)**

local TextListWrapper_OTUI = [[
UIWidget
  id: wrapList
  size: 220 140

  TextList
    id: list
    anchors.left: parent.left
    anchors.right: scroll.left
    anchors.top: parent.top
    anchors.bottom: parent.bottom

  VerticalScrollBar
    id: scroll
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    step: 16
]]
```
## G.5 Wzorzec integracyjny

**Lua (zalecany runtimea'flow)**

-- 1) Eksportuj z edytora do pliku .otui w Twoim module (poza runtime).
-- 2) W runtime L'aduj z pliku i przewiaLL kontroler.
local win = g_ui.displayUI('mini') -- np. modules/yourmod/mini.otui
MiniWindowController._wire(win)
```

**Edytor (rounda'trip)**

- Import: wykryj w Lua staL'e w formie `local <Name>_OTUI = [[...]]` i wczytaj blok jako LsrodL'o UI.
- Eksport: zapisz do `.otui` oraz opcjonalnie zaktualizuj powyLLszy blok (z zachowaniem STRICT).
