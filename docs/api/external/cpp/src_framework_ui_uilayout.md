---
title: "src/framework/ui/uilayout.h"
source_file: "src/framework/ui/uilayout.h"
generated_at: "2025-10-31T23:33:30.364Z"
doc_type: "cpp_api"
---

# src/framework/ui/uilayout.h

(update)=
## `update`

**Signature:**
```cpp
void update();
```

---

(updatelater)=
## `updateLater`

**Signature:**
```cpp
void updateLater();
```

---

(uilayout)=
## `UILayout`

**Signature:**
```cpp
public: UILayout(UIWidgetPtr parentWidget) : m_parentWidget(parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr parentWidget) : m_parentWidget(` | `parentWidget` | - |

**Returns:**
- `public:`

---

(applystyle)=
## `applyStyle`

**Signature:**
```cpp
virtual void applyStyle(const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OTMLNodePtr&` | `styleNode` | - |

**Returns:**
- `virtual void`

---

(addwidget)=
## `addWidget`

**Signature:**
```cpp
virtual void addWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

**Returns:**
- `virtual void`

---

(removewidget)=
## `removeWidget`

**Signature:**
```cpp
virtual void removeWidget(const UIWidgetPtr& widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const UIWidgetPtr&` | `widget` | - |

**Returns:**
- `virtual void`

---

(disableupdates)=
## `disableUpdates`

**Signature:**
```cpp
void disableUpdates();
```

---

(enableupdates)=
## `enableUpdates`

**Signature:**
```cpp
void enableUpdates();
```

---

(setparent)=
## `setParent`

**Signature:**
```cpp
void setParent(UIWidgetPtr parentWidget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidgetPtr` | `parentWidget` | - |

---

(getparentwidget)=
## `getParentWidget`

**Signature:**
```cpp
UIWidgetPtr getParentWidget();
```

**Returns:**
- `UIWidgetPtr`

---

(isupdatedisabled)=
## `isUpdateDisabled`

**Signature:**
```cpp
bool isUpdateDisabled();
```

**Returns:**
- `bool`

---

(isupdating)=
## `isUpdating`

**Signature:**
```cpp
bool isUpdating();
```

**Returns:**
- `bool`

---

(isuianchorlayout)=
## `isUIAnchorLayout`

**Signature:**
```cpp
virtual bool isUIAnchorLayout();
```

**Returns:**
- `virtual bool`

---

(isuiboxlayout)=
## `isUIBoxLayout`

**Signature:**
```cpp
virtual bool isUIBoxLayout();
```

**Returns:**
- `virtual bool`

---

(isuihorizontallayout)=
## `isUIHorizontalLayout`

**Signature:**
```cpp
virtual bool isUIHorizontalLayout();
```

**Returns:**
- `virtual bool`

---

(isuiverticallayout)=
## `isUIVerticalLayout`

**Signature:**
```cpp
virtual bool isUIVerticalLayout();
```

**Returns:**
- `virtual bool`

---

(isuigridlayout)=
## `isUIGridLayout`

**Signature:**
```cpp
virtual bool isUIGridLayout();
```

**Returns:**
- `virtual bool`

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
