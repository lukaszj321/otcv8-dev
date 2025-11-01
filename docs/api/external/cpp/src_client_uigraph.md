---
title: "src/client/uigraph.h"
source_file: "src/client/uigraph.h"
generated_at: "2025-11-01T04:06:42.735Z"
doc_type: "cpp_api"
---

# src/client/uigraph.h

(uigraph)=
## `UIGraph`

**Signature:**
```cpp
public: UIGraph();
```

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

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(addvalue)=
## `addValue`

**Signature:**
```cpp
void addValue(int value, bool ignoreSmallValues = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `value` |  | - |
| `bool` | `ignoreSmallValues` | `false` | - |

---

(onstyleapply)=
## `onStyleApply`

**Signature:**
```cpp
protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `styleName` | - |
| `const OTMLNodePtr&` | `styleNode` | - |

---

(setlinewidth)=
## `setLineWidth`

**Signature:**
```cpp
void setLineWidth(int width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `width` | - |

---

(setcapacity)=
## `setCapacity`

**Signature:**
```cpp
void setCapacity(int capacity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `capacity` | - |

---

(settitle)=
## `setTitle`

**Signature:**
```cpp
void setTitle(const std::string& title);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `title` | - |

---

(setshowlabels)=
## `setShowLabels`

**Signature:**
```cpp
void setShowLabels(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---
