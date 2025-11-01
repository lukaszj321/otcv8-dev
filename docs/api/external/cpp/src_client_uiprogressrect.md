---
title: "src/client/uiprogressrect.h"
source_file: "src/client/uiprogressrect.h"
generated_at: "2025-11-01T08:46:04.905Z"
doc_type: "cpp_api"
---

# src/client/uiprogressrect.h

(uiprogressrect)=
## `UIProgressRect`

**Signature:**
```cpp
public: UIProgressRect();
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

(setpercent)=
## `setPercent`

**Signature:**
```cpp
void setPercent(float percent);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `percent` | - |

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

(getpercent)=
## `getPercent`

**Signature:**
```cpp
float getPercent();
```

**Returns:**
- `float`

---
