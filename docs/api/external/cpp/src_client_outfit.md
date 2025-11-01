---
title: "src/client/outfit.h"
source_file: "src/client/outfit.h"
generated_at: "2025-11-01T00:11:49.022Z"
doc_type: "cpp_api"
---

# src/client/outfit.h

(outfit)=
## `Outfit`

**Signature:**
```cpp
public: Outfit();
```

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw(Point dest, Otc::Direction direction, uint walkAnimationPhase, bool animate = true, LightView* lightView = nullptr, bool ui = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `Point` | `dest` |  | - |
| `Otc::Direction` | `direction` |  | - |
| `uint` | `walkAnimationPhase` |  | - |
| `bool` | `animate` | `true` | - |
| `LightView*` | `lightView` | `nullptr` | - |
| `bool` | `ui` | `false` | - |

---

(draw-1)=
## `draw`

**Signature:**
```cpp
void draw(const Rect& dest, Otc::Direction direction, uint animationPhase, bool animate = true, bool ui = false, bool oldScaling = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `Otc::Direction` | `direction` |  | - |
| `uint` | `animationPhase` |  | - |
| `bool` | `animate` | `true` | - |
| `bool` | `ui` | `false` | - |
| `bool` | `oldScaling` | `false` | - |

---

(resetclothes)=
## `resetClothes`

**Signature:**
```cpp
void resetClothes();
```

---

(getcolor)=
## `getColor`

**Signature:**
```cpp
static Color getColor(int color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `color` | - |

**Returns:**
- `Color`

---

(setid)=
## `setId`

**Signature:**
```cpp
void setId(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

---

(setauxid)=
## `setAuxId`

**Signature:**
```cpp
void setAuxId(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

---

(sethead)=
## `setHead`

**Signature:**
```cpp
void setHead(int head);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `head` | - |

---

(setbody)=
## `setBody`

**Signature:**
```cpp
void setBody(int body);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `body` | - |

---

(setlegs)=
## `setLegs`

**Signature:**
```cpp
void setLegs(int legs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `legs` | - |

---

(setfeet)=
## `setFeet`

**Signature:**
```cpp
void setFeet(int feet);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `feet` | - |

---

(setaddons)=
## `setAddons`

**Signature:**
```cpp
void setAddons(int addons);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `addons` | - |

---

(setmount)=
## `setMount`

**Signature:**
```cpp
void setMount(int mount);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `mount` | - |

---

(setwings)=
## `setWings`

**Signature:**
```cpp
void setWings(int wings);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `wings` | - |

---

(setaura)=
## `setAura`

**Signature:**
```cpp
void setAura(int aura);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `aura` | - |

---

(setcategory)=
## `setCategory`

**Signature:**
```cpp
void setCategory(ThingCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ThingCategory` | `category` | - |

---

(setshader)=
## `setShader`

**Signature:**
```cpp
void setShader(const std::string& shader);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `shader` | - |

---

(sethealthbar)=
## `setHealthBar`

**Signature:**
```cpp
void setHealthBar(uint8 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `id` | - |

---

(setmanabar)=
## `setManaBar`

**Signature:**
```cpp
void setManaBar(uint8 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `id` | - |

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

(resetshader)=
## `resetShader`

**Signature:**
```cpp
void resetShader();
```

---

(getid)=
## `getId`

**Signature:**
```cpp
int getId();
```

**Returns:**
- `int`

---

(getauxid)=
## `getAuxId`

**Signature:**
```cpp
int getAuxId();
```

**Returns:**
- `int`

---

(gethead)=
## `getHead`

**Signature:**
```cpp
int getHead();
```

**Returns:**
- `int`

---

(getbody)=
## `getBody`

**Signature:**
```cpp
int getBody();
```

**Returns:**
- `int`

---

(getlegs)=
## `getLegs`

**Signature:**
```cpp
int getLegs();
```

**Returns:**
- `int`

---

(getfeet)=
## `getFeet`

**Signature:**
```cpp
int getFeet();
```

**Returns:**
- `int`

---

(getaddons)=
## `getAddons`

**Signature:**
```cpp
int getAddons();
```

**Returns:**
- `int`

---

(getmount)=
## `getMount`

**Signature:**
```cpp
int getMount();
```

**Returns:**
- `int`

---

(getwings)=
## `getWings`

**Signature:**
```cpp
int getWings();
```

**Returns:**
- `int`

---

(getaura)=
## `getAura`

**Signature:**
```cpp
int getAura();
```

**Returns:**
- `int`

---

(getcategory)=
## `getCategory`

**Signature:**
```cpp
ThingCategory getCategory();
```

**Returns:**
- `ThingCategory`

---

(getshader)=
## `getShader`

**Signature:**
```cpp
std::string getShader();
```

**Returns:**
- `std::string`

---

(gethealthbar)=
## `getHealthBar`

**Signature:**
```cpp
int getHealthBar();
```

**Returns:**
- `int`

---

(getmanabar)=
## `getManaBar`

**Signature:**
```cpp
int getManaBar();
```

**Returns:**
- `int`

---
