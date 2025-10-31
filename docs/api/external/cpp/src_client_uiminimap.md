---
title: "src/client/uiminimap.h"
source_file: "src/client/uiminimap.h"
generated_at: "2025-10-31T23:33:30.331Z"
doc_type: "cpp_api"
---

# src/client/uiminimap.h

(uiminimap)=
## `UIMinimap`

**Signature:**
```cpp
public: UIMinimap();
```

**Returns:**
- `public:`

---

(drawself)=
## `drawSelf`

**Signature:**
```cpp
void drawSelf(Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::DrawPane` | `drawPane` | - |

---

(setzoom)=
## `setZoom`

**Signature:**
```cpp
bool setZoom(int zoom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `zoom` | - |

**Returns:**
- `bool`

---

(setcameraposition)=
## `setCameraPosition`

**Signature:**
```cpp
void setCameraPosition(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(floorup)=
## `floorUp`

**Signature:**
```cpp
bool floorUp();
```

**Returns:**
- `bool`

---

(floordown)=
## `floorDown`

**Signature:**
```cpp
bool floorDown();
```

**Returns:**
- `bool`

---

(gettilepoint)=
## `getTilePoint`

**Signature:**
```cpp
Point getTilePoint(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `Point`

---

(gettilerect)=
## `getTileRect`

**Signature:**
```cpp
Rect getTileRect(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `Rect`

---

(gettileposition)=
## `getTilePosition`

**Signature:**
```cpp
Position getTilePosition(const Point& mousePos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `mousePos` | - |

**Returns:**
- `Position`

---

(anchorposition)=
## `anchorPosition`

**Signature:**
```cpp
void anchorPosition(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |
| `Fw::AnchorEdge` | `anchoredEdge` | - |
| `const Position&` | `hookedPosition` | - |
| `Fw::AnchorEdge` | `hookedEdge` | - |

---

(fillposition)=
## `fillPosition`

**Signature:**
```cpp
void fillPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |
| `const Position&` | `hookedPosition` | - |

---

(centerinposition)=
## `centerInPosition`

**Signature:**
```cpp
void centerInPosition(const UIWidgetPtr& anchoredWidget, const Position& hookedPosition);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |
| `const Position&` | `hookedPosition` | - |

---

(onzoomchange)=
## `onZoomChange`

**Signature:**
```cpp
protected: virtual void onZoomChange(int zoom, int oldZoom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `zoom` | - |
| `int` | `oldZoom` | - |

**Returns:**
- `protected: virtual void`

---

(oncamerapositionchange)=
## `onCameraPositionChange`

**Signature:**
```cpp
virtual void onCameraPositionChange(const Position& position, const Position& oldPosition);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |
| `const Position&` | `oldPosition` | - |

**Returns:**
- `virtual void`

---

(onstyleapply)=
## `onStyleApply`

**Signature:**
```cpp
virtual void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |
| `const OTMLNodePtr&` | `styleNode` | - |

**Returns:**
- `virtual void`

---

(update)=
## `update`

**Signature:**
```cpp
private: void update();
```

**Returns:**
- `private: void`

---

(zoomin)=
## `zoomIn`

**Signature:**
```cpp
bool zoomIn();
```

**Returns:**
- `bool`

---

(zoomout)=
## `zoomOut`

**Signature:**
```cpp
bool zoomOut();
```

**Returns:**
- `bool`

---

(setminzoom)=
## `setMinZoom`

**Signature:**
```cpp
void setMinZoom(int minZoom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `minZoom` | - |

---

(setmaxzoom)=
## `setMaxZoom`

**Signature:**
```cpp
void setMaxZoom(int maxZoom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `maxZoom` | - |

---

(getcameraposition)=
## `getCameraPosition`

**Signature:**
```cpp
Position getCameraPosition();
```

**Returns:**
- `Position`

---

(getminzoom)=
## `getMinZoom`

**Signature:**
```cpp
int getMinZoom();
```

**Returns:**
- `int`

---

(getmaxzoom)=
## `getMaxZoom`

**Signature:**
```cpp
int getMaxZoom();
```

**Returns:**
- `int`

---

(getzoom)=
## `getZoom`

**Signature:**
```cpp
int getZoom();
```

**Returns:**
- `int`

---

(getscale)=
## `getScale`

**Signature:**
```cpp
float getScale();
```

**Returns:**
- `float`

---
