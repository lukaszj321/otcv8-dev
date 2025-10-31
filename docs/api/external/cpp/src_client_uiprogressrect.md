---
title: "src/client/uiprogressrect.h"
source_file: "src/client/uiprogressrect.h"
generated_at: "2025-10-31T23:33:30.331Z"
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

**Returns:**
- `protected: void`

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
