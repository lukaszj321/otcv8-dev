---
title: "src/client/lightview.h"
source_file: "src/client/lightview.h"
generated_at: "2025-10-31T23:33:30.321Z"
doc_type: "cpp_api"
---

# src/client/lightview.h

(addlight)=
## `addLight`

**Signature:**
```cpp
return addLight(pos, light.color, light.intensity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `pos` | - |
| `light.` | `color` | - |
| `light.` | `intensity` | - |

**Returns:**
- `return`

---

(addlight)=
## `addLight`

**Signature:**
```cpp
void addLight(const Point& pos, uint8_t color, uint8_t intensity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |
| `uint8_t` | `color` | - |
| `uint8_t` | `intensity` | - |

---

(setfieldbrightness)=
## `setFieldBrightness`

**Signature:**
```cpp
void setFieldBrightness(const Point& pos, size_t start, uint8_t color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |
| `size_t` | `start` | - |
| `uint8_t` | `color` | - |

---

(lightview)=
## `LightView`

**Signature:**
```cpp
public: LightView(TexturePtr& lightTexture, const Size& mapSize, const Rect& dest, const Rect& src, uint8_t color, uint8_t intensity) : DrawQueueItem(nullptr), m_lightTexture(lightTexture), m_mapSize(mapSize), m_dest(dest), m_src(src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TexturePtr&` | `lightTexture` | - |
| `const Size&` | `mapSize` | - |
| `const Rect&` | `dest` | - |
| `const Rect&` | `src` | - |
| `uint8_t` | `color` | - |
| `uint8_t intensity) : DrawQueueItem(nullptr)` | - | - |
| `m_lightTexture(lightTexture)` | - | - |
| `m_mapSize(mapSize)` | - | - |
| `m_dest(dest)` | - | - |
| `m_src(` | `src` | - |

**Returns:**
- `public:`

---

(addlight)=
## `addLight`

**Signature:**
```cpp
inline void addLight(const Point& pos, const Light& light);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |
| `const Light&` | `light` | - |

**Returns:**
- `inline void`

---

(size)=
## `size`

**Signature:**
```cpp
size_t size();
```

**Returns:**
- `size_t`

---
