---
title: "src/framework/ui/uiboxlayout.h"
source_file: "src/framework/ui/uiboxlayout.h"
generated_at: "2025-10-31T23:33:30.363Z"
doc_type: "cpp_api"
---

# src/framework/ui/uiboxlayout.h

(uiboxlayout)=
## `UIBoxLayout`

**Signature:**
```cpp
public: UIBoxLayout(UIWidgetPtr parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `parentWidget` | - |

**Returns:**
- `public:`

---

(applystyle)=
## `applyStyle`

**Signature:**
```cpp
void applyStyle(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

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

(setspacing)=
## `setSpacing`

**Signature:**
```cpp
void setSpacing(int spacing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `spacing` | - |

---

(setfitchildren)=
## `setFitChildren`

**Signature:**
```cpp
void setFitChildren(bool fitParent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `fitParent` | - |

---

(isuiboxlayout)=
## `isUIBoxLayout`

**Signature:**
```cpp
bool isUIBoxLayout();
```

**Returns:**
- `bool`

---
