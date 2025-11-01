---
title: "src/framework/ui/uilayout.h"
source_file: "src/framework/ui/uilayout.h"
generated_at: "2025-11-01T08:19:49.471Z"
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
- `bool`

---

(isuiboxlayout)=
## `isUIBoxLayout`

**Signature:**
```cpp
virtual bool isUIBoxLayout();
```

**Returns:**
- `bool`

---

(isuihorizontallayout)=
## `isUIHorizontalLayout`

**Signature:**
```cpp
virtual bool isUIHorizontalLayout();
```

**Returns:**
- `bool`

---

(isuiverticallayout)=
## `isUIVerticalLayout`

**Signature:**
```cpp
virtual bool isUIVerticalLayout();
```

**Returns:**
- `bool`

---

(isuigridlayout)=
## `isUIGridLayout`

**Signature:**
```cpp
virtual bool isUIGridLayout();
```

**Returns:**
- `bool`

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
