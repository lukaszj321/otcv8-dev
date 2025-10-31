---
title: "src/framework/ui/uianchorlayout.h"
source_file: "src/framework/ui/uianchorlayout.h"
generated_at: "2025-10-31T23:33:30.363Z"
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
- `virtual UIWidgetPtr`

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
- `virtual int`

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

(addanchor)=
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
- `protected: virtual bool`

---

(updatewidget)=
## `updateWidget`

**Signature:**
```cpp
virtual bool updateWidget(const UIWidgetPtr& widget, const UIAnchorGroupPtr& anchorGroup, UIWidgetPtr first = nullptr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |
| `const UIAnchorGroupPtr&` | `anchorGroup` | - |
| `UIWidgetPtr first =` | `nullptr` | - |

**Returns:**
- `virtual bool`

---

(uianchor)=
## `UIAnchor`

**Signature:**
```cpp
public: UIAnchor(Fw::AnchorEdge anchoredEdge, const std::string& hookedWidgetId, Fw::AnchorEdge hookedEdge) : m_anchoredEdge(anchoredEdge), m_hookedEdge(hookedEdge), m_hookedWidgetId(hookedWidgetId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::AnchorEdge` | `anchoredEdge` | - |
| `const std::string&` | `hookedWidgetId` | - |
| `Fw::AnchorEdge hookedEdge) : m_anchoredEdge(anchoredEdge)` | - | - |
| `m_hookedEdge(hookedEdge)` | - | - |
| `m_hookedWidgetId(` | `hookedWidgetId` | - |

**Returns:**
- `public:`

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

(uianchorgroup)=
## `UIAnchorGroup`

**Signature:**
```cpp
public: UIAnchorGroup() : m_updated(true);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) : m_updated(` | `true` | - |

**Returns:**
- `public:`

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

(uianchorlayout)=
## `UIAnchorLayout`

**Signature:**
```cpp
public: UIAnchorLayout(UIWidgetPtr parentWidget) : UILayout(parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr parentWidget) : UILayout(` | `parentWidget` | - |

**Returns:**
- `public:`

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
