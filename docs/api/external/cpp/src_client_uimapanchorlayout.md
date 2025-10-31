---
title: "src/client/uimapanchorlayout.h"
source_file: "src/client/uimapanchorlayout.h"
generated_at: "2025-10-31T23:33:30.331Z"
doc_type: "cpp_api"
---

# src/client/uimapanchorlayout.h

(gethookedpoint)=
## `getHookedPoint`

**Signature:**
```cpp
int getHookedPoint(const UIWidgetPtr& hookedWidget, const UIWidgetPtr& parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `hookedWidget` | - |
| `const UIWidgetPtr&` | `parentWidget` | - |

**Returns:**
- `int`

---

(addpositionanchor)=
## `addPositionAnchor`

**Signature:**
```cpp
void addPositionAnchor(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |
| `Fw::AnchorEdge` | `anchoredEdge` | - |
| `const Position&` | `hookedPosition` | - |
| `Fw::AnchorEdge` | `hookedEdge` | - |

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

(uipositionanchor)=
## `UIPositionAnchor`

**Signature:**
```cpp
public: UIPositionAnchor(Fw::AnchorEdge anchoredEdge, const Position& hookedPosition, Fw::AnchorEdge hookedEdge) : UIAnchor(anchoredEdge, std::string(), hookedEdge), m_hookedPosition(hookedPosition);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AnchorEdge` | `anchoredEdge` | - |
| `const Position&` | `hookedPosition` | - |
| `Fw::AnchorEdge` | `hookedEdge` | - |

**Returns:**
- `public:`

---

(gethookedwidget)=
## `getHookedWidget`

**Signature:**
```cpp
UIWidgetPtr getHookedWidget(const UIWidgetPtr& widget, const UIWidgetPtr& parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |
| `const UIWidgetPtr&` | `parentWidget` | - |

**Returns:**
- `UIWidgetPtr`

---

(uimapanchorlayout)=
## `UIMapAnchorLayout`

**Signature:**
```cpp
public: UIMapAnchorLayout(UIWidgetPtr parentWidget) : UIAnchorLayout(parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `parentWidget` | - |

**Returns:**
- `public:`

---
