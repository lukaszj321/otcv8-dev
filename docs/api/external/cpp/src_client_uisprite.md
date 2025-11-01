---
title: "src/client/uisprite.h"
source_file: "src/client/uisprite.h"
generated_at: "2025-11-01T05:32:59.271Z"
doc_type: "cpp_api"
---

# src/client/uisprite.h

(uisprite)=
## `UISprite`

**Signature:**
```cpp
public: UISprite();
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

(setspriteid)=
## `setSpriteId`

**Signature:**
```cpp
void setSpriteId(uint32 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |

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

(getspriteid)=
## `getSpriteId`

**Signature:**
```cpp
uint32 getSpriteId();
```

**Returns:**
- `uint32`

---

(clearsprite)=
## `clearSprite`

**Signature:**
```cpp
void clearSprite();
```

---

(setspritecolor)=
## `setSpriteColor`

**Signature:**
```cpp
void setSpriteColor(Color color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Color` | `color` | - |

---

(isspritevisible)=
## `isSpriteVisible`

**Signature:**
```cpp
bool isSpriteVisible();
```

**Returns:**
- `bool`

---

(setspritevisible)=
## `setSpriteVisible`

**Signature:**
```cpp
void setSpriteVisible(bool visible);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `visible` | - |

---

(hassprite)=
## `hasSprite`

**Signature:**
```cpp
bool hasSprite();
```

**Returns:**
- `bool`

---
