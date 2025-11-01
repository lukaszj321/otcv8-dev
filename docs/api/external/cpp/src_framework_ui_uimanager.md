---
title: "src/framework/ui/uimanager.h"
source_file: "src/framework/ui/uimanager.h"
generated_at: "2025-11-01T08:46:04.939Z"
doc_type: "cpp_api"
---

# src/framework/ui/uimanager.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(render)=
## `render`

**Signature:**
```cpp
void render(Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::DrawPane` | `drawPane` | - |

---

(resize)=
## `resize`

**Signature:**
```cpp
void resize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(inputevent)=
## `inputEvent`

**Signature:**
```cpp
void inputEvent(const InputEvent& event);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const InputEvent&` | `event` | - |

---

(updatepressedwidget)=
## `updatePressedWidget`

**Signature:**
```cpp
void updatePressedWidget(const Fw::MouseButton button, const UIWidgetPtr& newPressedWidget, const Point& clickedPos = Point(), bool fireClicks = true);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Fw::MouseButton` | `button` |  | - |
| `const UIWidgetPtr&` | `newPressedWidget` |  | - |
| `const Point&` | `clickedPos` | `Point()` | - |
| `bool` | `fireClicks` | `true` | - |

---

(updatedraggingwidget)=
## `updateDraggingWidget`

**Signature:**
```cpp
bool updateDraggingWidget(const UIWidgetPtr& draggingWidget, const Point& clickedPos = Point());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const UIWidgetPtr&` | `draggingWidget` |  | - |
| `const Point&` | `clickedPos` | `Point()` | - |

**Returns:**
- `bool`

---

(updatehoveredwidget)=
## `updateHoveredWidget`

**Signature:**
```cpp
void updateHoveredWidget(bool now = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `now` | `false` | - |

---

(clearstyles)=
## `clearStyles`

**Signature:**
```cpp
void clearStyles();
```

---

(importstyle)=
## `importStyle`

**Signature:**
```cpp
bool importStyle(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(importstylefromstring)=
## `importStyleFromString`

**Signature:**
```cpp
bool importStyleFromString(std::string data);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `data` | - |

**Returns:**
- `bool`

---

(importstylefromotml)=
## `importStyleFromOTML`

**Signature:**
```cpp
void importStyleFromOTML(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

---

(getstyle)=
## `getStyle`

**Signature:**
```cpp
OTMLNodePtr getStyle(const std::string& styleName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |

**Returns:**
- `OTMLNodePtr`

---

(getstyleclass)=
## `getStyleClass`

**Signature:**
```cpp
std::string getStyleClass(const std::string& styleName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |

**Returns:**
- `std::string`

---

(loaduifromstring)=
## `loadUIFromString`

**Signature:**
```cpp
UIWidgetPtr loadUIFromString(const std::string& data, const UIWidgetPtr& parent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `data` | - |
| `const UIWidgetPtr&` | `parent` | - |

**Returns:**
- `UIWidgetPtr`

---

(loadui)=
## `loadUI`

**Signature:**
```cpp
UIWidgetPtr loadUI(std::string file, const UIWidgetPtr& parent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |
| `const UIWidgetPtr&` | `parent` | - |

**Returns:**
- `UIWidgetPtr`

---

(createwidget)=
## `createWidget`

**Signature:**
```cpp
UIWidgetPtr createWidget(const std::string& styleName, const UIWidgetPtr& parent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |
| `const UIWidgetPtr&` | `parent` | - |

**Returns:**
- `UIWidgetPtr`

---

(createwidgetfromotml)=
## `createWidgetFromOTML`

**Signature:**
```cpp
UIWidgetPtr createWidgetFromOTML(const OTMLNodePtr& widgetNode, const UIWidgetPtr& parent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `widgetNode` | - |
| `const UIWidgetPtr&` | `parent` | - |

**Returns:**
- `UIWidgetPtr`

---

(onwidgetappear)=
## `onWidgetAppear`

**Signature:**
```cpp
protected: void onWidgetAppear(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(onwidgetdisappear)=
## `onWidgetDisappear`

**Signature:**
```cpp
void onWidgetDisappear(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(onwidgetdestroy)=
## `onWidgetDestroy`

**Signature:**
```cpp
void onWidgetDestroy(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(displayui)=
## `displayUI`

**Signature:**
```cpp
UIWidgetPtr displayUI(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

**Returns:**
- `UIWidgetPtr`

---

(setmousereceiver)=
## `setMouseReceiver`

**Signature:**
```cpp
void setMouseReceiver(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(setkeyboardreceiver)=
## `setKeyboardReceiver`

**Signature:**
```cpp
void setKeyboardReceiver(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(setdebugboxesdrawing)=
## `setDebugBoxesDrawing`

**Signature:**
```cpp
void setDebugBoxesDrawing(bool enabled);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enabled` | - |

---

(resetmousereceiver)=
## `resetMouseReceiver`

**Signature:**
```cpp
void resetMouseReceiver();
```

---

(resetkeyboardreceiver)=
## `resetKeyboardReceiver`

**Signature:**
```cpp
void resetKeyboardReceiver();
```

---

(getmousereceiver)=
## `getMouseReceiver`

**Signature:**
```cpp
UIWidgetPtr getMouseReceiver();
```

**Returns:**
- `UIWidgetPtr`

---

(getkeyboardreceiver)=
## `getKeyboardReceiver`

**Signature:**
```cpp
UIWidgetPtr getKeyboardReceiver();
```

**Returns:**
- `UIWidgetPtr`

---

(getdraggingwidget)=
## `getDraggingWidget`

**Signature:**
```cpp
UIWidgetPtr getDraggingWidget();
```

**Returns:**
- `UIWidgetPtr`

---

(gethoveredwidget)=
## `getHoveredWidget`

**Signature:**
```cpp
UIWidgetPtr getHoveredWidget();
```

**Returns:**
- `UIWidgetPtr`

---

(getpressedwidget)=
## `getPressedWidget`

**Signature:**
```cpp
UIWidgetPtr getPressedWidget();
```

**Returns:**
- `UIWidgetPtr`

---

(getrootwidget)=
## `getRootWidget`

**Signature:**
```cpp
UIWidgetPtr getRootWidget();
```

**Returns:**
- `UIWidgetPtr`

---

(ismousegrabbed)=
## `isMouseGrabbed`

**Signature:**
```cpp
bool isMouseGrabbed();
```

**Returns:**
- `bool`

---

(iskeyboardgrabbed)=
## `isKeyboardGrabbed`

**Signature:**
```cpp
bool isKeyboardGrabbed();
```

**Returns:**
- `bool`

---

(isdrawingdebugboxes)=
## `isDrawingDebugBoxes`

**Signature:**
```cpp
bool isDrawingDebugBoxes();
```

**Returns:**
- `bool`

---
