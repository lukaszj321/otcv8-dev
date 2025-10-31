---
title: "src/framework/ui/uigridlayout.h"
source_file: "src/framework/ui/uigridlayout.h"
generated_at: "2025-10-31T23:33:30.363Z"
doc_type: "cpp_api"
---

# src/framework/ui/uigridlayout.h

(uigridlayout)=
## `UIGridLayout`

**Signature:**
```cpp
public: UIGridLayout(UIWidgetPtr parentWidget);
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

(internalupdate)=
## `internalUpdate`

**Signature:**
```cpp
protected: bool internalUpdate();
```

**Returns:**
- `protected: bool`

---

(setcellsize)=
## `setCellSize`

**Signature:**
```cpp
void setCellSize(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

---

(setcellwidth)=
## `setCellWidth`

**Signature:**
```cpp
void setCellWidth(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setcellheight)=
## `setCellHeight`

**Signature:**
```cpp
void setCellHeight(int height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `height` | - |

---

(setcellspacing)=
## `setCellSpacing`

**Signature:**
```cpp
void setCellSpacing(int spacing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `spacing` | - |

---

(setnumcolumns)=
## `setNumColumns`

**Signature:**
```cpp
void setNumColumns(int columns);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `columns` | - |

---

(setnumlines)=
## `setNumLines`

**Signature:**
```cpp
void setNumLines(int lines);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `lines` | - |

---

(setautospacing)=
## `setAutoSpacing`

**Signature:**
```cpp
void setAutoSpacing(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(setfitchildren)=
## `setFitChildren`

**Signature:**
```cpp
void setFitChildren(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(setflow)=
## `setFlow`

**Signature:**
```cpp
void setFlow(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(getcellsize)=
## `getCellSize`

**Signature:**
```cpp
Size getCellSize();
```

**Returns:**
- `Size`

---

(getcellspacing)=
## `getCellSpacing`

**Signature:**
```cpp
int getCellSpacing();
```

**Returns:**
- `int`

---

(getnumcolumns)=
## `getNumColumns`

**Signature:**
```cpp
int getNumColumns();
```

**Returns:**
- `int`

---

(getnumlines)=
## `getNumLines`

**Signature:**
```cpp
int getNumLines();
```

**Returns:**
- `int`

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
