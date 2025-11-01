---
title: "src/client/missile.h"
source_file: "src/client/missile.h"
generated_at: "2025-11-01T08:45:15.283Z"
doc_type: "cpp_api"
---

# src/client/missile.h

(draw)=
## `draw`

**Signature:**
```cpp
public: void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Point&` | `dest` |  | - |
| `bool` | `animate` | `true` | - |
| `LightView*` | `lightView` | `nullptr` | - |

---

(setid)=
## `setId`

**Signature:**
```cpp
void setId(uint32 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |

---

(setpath)=
## `setPath`

**Signature:**
```cpp
void setPath(const Position& fromPosition, const Position& toPosition);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `fromPosition` | - |
| `const Position&` | `toPosition` | - |

---

(getthingtype)=
## `getThingType`

**Signature:**
```cpp
const ThingTypePtr& getThingType();
```

**Returns:**
- `const ThingTypePtr&`

---

(getid)=
## `getId`

**Signature:**
```cpp
uint32 getId();
```

**Returns:**
- `uint32`

---

(asmissile)=
## `asMissile`

**Signature:**
```cpp
MissilePtr asMissile();
```

**Returns:**
- `MissilePtr`

---

(ismissile)=
## `isMissile`

**Signature:**
```cpp
bool isMissile();
```

**Returns:**
- `bool`

---

(getsource)=
## `getSource`

**Signature:**
```cpp
Position getSource();
```

**Returns:**
- `Position`

---

(getdestination)=
## `getDestination`

**Signature:**
```cpp
Position getDestination();
```

**Returns:**
- `Position`

