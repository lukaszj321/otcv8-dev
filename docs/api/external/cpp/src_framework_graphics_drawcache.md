---
title: "src/framework/graphics/drawcache.h"
source_file: "src/framework/graphics/drawcache.h"
generated_at: "2025-11-01T04:06:42.746Z"
doc_type: "cpp_api"
---

# src/framework/graphics/drawcache.h

(draw)=
## `draw`

**Signature:**
```cpp
void draw();
```

---

(bind)=
## `bind`

**Signature:**
```cpp
void bind();
```

---

(release)=
## `release`

**Signature:**
```cpp
void release();
```

---

(addrect)=
## `addRect`

**Signature:**
```cpp
void addRect(const Rect& dest, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Color&` | `color` | - |

---

(addtexturedrect)=
## `addTexturedRect`

**Signature:**
```cpp
void addTexturedRect(const Rect& dest, const Rect& src, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Rect&` | `src` | - |
| `const Color&` | `color` | - |

---

(addcoords)=
## `addCoords`

**Signature:**
```cpp
void addCoords(CoordsBuffer& coords, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `CoordsBuffer&` | `coords` | - |
| `const Color&` | `color` | - |

---

(addtexturedcoords)=
## `addTexturedCoords`

**Signature:**
```cpp
void addTexturedCoords(CoordsBuffer& coords, const Point& offset, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `CoordsBuffer&` | `coords` | - |
| `const Point&` | `offset` | - |
| `const Color&` | `color` | - |

---

(hasspace)=
## `hasSpace`

**Signature:**
```cpp
bool hasSpace(int size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `size` | - |

**Returns:**
- `bool`

---

(getsize)=
## `getSize`

**Signature:**
```cpp
inline int getSize();
```

**Returns:**
- `int`

---

(addrectraw)=
## `addRectRaw`

**Signature:**
```cpp
private: inline void addRectRaw(float* dest, const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float*` | `dest` | - |
| `const Rect&` | `rect` | - |

---

(addcolorraw)=
## `addColorRaw`

**Signature:**
```cpp
inline void addColorRaw(const Color& color, int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |
| `int` | `count` | - |

---
