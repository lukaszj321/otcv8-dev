---
title: "src/framework/ui/uianchorlayout.h"
source_file: "src/framework/ui/uianchorlayout.h"
generated_at: "2025-11-01T08:19:49.470Z"
doc_type: "cpp_api"
---

# src/framework/ui/uianchorlayout.h

(gethookedwidget)=
## `getHookedWidget`

**Signature:**
```cpp
virtual UIWidgetPtr getHookedWidget(const UIWidgetPtr& widget, const UIWidgetPtr& parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |
| `const UIWidgetPtr&` | `parentWidget` | - |

**Returns:**
- `UIWidgetPtr`

---

(gethookedpoint)=
## `getHookedPoint`

**Signature:**
```cpp
virtual int getHookedPoint(const UIWidgetPtr& hookedWidget, const UIWidgetPtr& parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `hookedWidget` | - |
| `const UIWidgetPtr&` | `parentWidget` | - |

**Returns:**
- `int`

---

(addanchor)=
## `addAnchor`

**Signature:**
```cpp
void addAnchor(const UIAnchorPtr& anchor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIAnchorPtr&` | `anchor` | - |

---

(addanchor-1)=
## `addAnchor`

**Signature:**
```cpp
void addAnchor(const UIWidgetPtr& anchoredWidget, Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |
| `Fw::AnchorEdge` | `anchoredEdge` | - |
| `const std::string&` | `hookedWidgetId` | - |
| `Fw::AnchorEdge` | `hookedEdge` | - |

---

(removeanchors)=
## `removeAnchors`

**Signature:**
```cpp
void removeAnchors(const UIWidgetPtr& anchoredWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |

---

(hasanchors)=
## `hasAnchors`

**Signature:**
```cpp
bool hasAnchors(const UIWidgetPtr& anchoredWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |

**Returns:**
- `bool`

---

(centerin)=
## `centerIn`

**Signature:**
```cpp
void centerIn(const UIWidgetPtr& anchoredWidget, const std::string& hookedWidgetId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |
| `const std::string&` | `hookedWidgetId` | - |

---

(fill)=
## `fill`

**Signature:**
```cpp
void fill(const UIWidgetPtr& anchoredWidget, const std::string& hookedWidgetId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `anchoredWidget` | - |
| `const std::string&` | `hookedWidgetId` | - |

---

(addwidget)=
## `addWidget`

**Signature:**
```cpp
void addWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(removewidget)=
## `removeWidget`

**Signature:**
```cpp
void removeWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

---

(internalupdate)=
## `internalUpdate`

**Signature:**
```cpp
protected: virtual bool internalUpdate();
```

**Returns:**
- `bool`

---

(updatewidget)=
## `updateWidget`

**Signature:**
```cpp
virtual bool updateWidget(const UIWidgetPtr& widget, const UIAnchorGroupPtr& anchorGroup, UIWidgetPtr first = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const UIWidgetPtr&` | `widget` |  | - |
| `const UIAnchorGroupPtr&` | `anchorGroup` |  | - |
| `UIWidgetPtr` | `first` | `nullptr` | - |

**Returns:**
- `bool`

---

(getanchorededge)=
## `getAnchoredEdge`

**Signature:**
```cpp
Fw::AnchorEdge getAnchoredEdge();
```

**Returns:**
- `Fw::AnchorEdge`

---

(gethookededge)=
## `getHookedEdge`

**Signature:**
```cpp
Fw::AnchorEdge getHookedEdge();
```

**Returns:**
- `Fw::AnchorEdge`

---

(getanchors)=
## `getAnchors`

**Signature:**
```cpp
const UIAnchorList& getAnchors();
```

**Returns:**
- `const UIAnchorList&`

---

(isupdated)=
## `isUpdated`

**Signature:**
```cpp
bool isUpdated();
```

**Returns:**
- `bool`

---

(setupdated)=
## `setUpdated`

**Signature:**
```cpp
void setUpdated(bool updated);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `updated` | - |

---

(isuianchorlayout)=
## `isUIAnchorLayout`

**Signature:**
```cpp
bool isUIAnchorLayout();
```

**Returns:**
- `bool`

---
