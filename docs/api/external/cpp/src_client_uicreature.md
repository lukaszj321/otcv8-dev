---
title: "src/client/uicreature.h"
source_file: "src/client/uicreature.h"
generated_at: "2025-11-01T08:19:49.429Z"
doc_type: "cpp_api"
---

# src/client/uicreature.h

(drawself)=
## `drawSelf`

**Signature:**
```cpp
public: void drawSelf(Fw::DrawPane drawPane);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Fw::DrawPane` | `drawPane` | - |

---

(setoutfit)=
## `setOutfit`

**Signature:**
```cpp
void setOutfit(const Outfit& outfit);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Outfit&` | `outfit` | - |

---

(setcenter)=
## `setCenter`

**Signature:**
```cpp
void setCenter(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

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

(setcreature)=
## `setCreature`

**Signature:**
```cpp
void setCreature(const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const CreaturePtr&` | `creature` | - |

---

(setfixedcreaturesize)=
## `setFixedCreatureSize`

**Signature:**
```cpp
void setFixedCreatureSize(bool fixed);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `fixed` | - |

---

(getcreature)=
## `getCreature`

**Signature:**
```cpp
CreaturePtr getCreature();
```

**Returns:**
- `CreaturePtr`

---

(getoutfit)=
## `getOutfit`

**Signature:**
```cpp
Outfit getOutfit();
```

**Returns:**
- `Outfit`

---

(isfixedcreaturesize)=
## `isFixedCreatureSize`

**Signature:**
```cpp
bool isFixedCreatureSize();
```

**Returns:**
- `bool`

---

(setautorotating)=
## `setAutoRotating`

**Signature:**
```cpp
void setAutoRotating(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(setdirection)=
## `setDirection`

**Signature:**
```cpp
void setDirection(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

---

(getdirection)=
## `getDirection`

**Signature:**
```cpp
Otc::Direction getDirection();
```

**Returns:**
- `Otc::Direction`

---

(setscale)=
## `setScale`

**Signature:**
```cpp
void setScale(float scale);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `scale` | - |

---

(getscale)=
## `getScale`

**Signature:**
```cpp
float getScale();
```

**Returns:**
- `float`

---

(setanimate)=
## `setAnimate`

**Signature:**
```cpp
void setAnimate(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---

(isanimating)=
## `isAnimating`

**Signature:**
```cpp
bool isAnimating();
```

**Returns:**
- `bool`

---

(setoldscaling)=
## `setOldScaling`

**Signature:**
```cpp
void setOldScaling(bool value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `value` | - |

---
