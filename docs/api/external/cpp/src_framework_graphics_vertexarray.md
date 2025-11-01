---
title: "src/framework/graphics/vertexarray.h"
source_file: "src/framework/graphics/vertexarray.h"
generated_at: "2025-11-01T08:19:49.448Z"
doc_type: "cpp_api"
---

# src/framework/graphics/vertexarray.h

(vertexarray)=
## `VertexArray`

**Signature:**
```cpp
public: VertexArray();
```

---

(addvertex)=
## `addVertex`

**Signature:**
```cpp
inline void addVertex(float x, float y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `x` | - |
| `float` | `y` | - |

---

(addtriangle)=
## `addTriangle`

**Signature:**
```cpp
inline void addTriangle(const Point& a, const Point& b, const Point& c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `a` | - |
| `const Point&` | `b` | - |
| `const Point&` | `c` | - |

---

(addrect)=
## `addRect`

**Signature:**
```cpp
inline void addRect(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(addrect-1)=
## `addRect`

**Signature:**
```cpp
inline void addRect(const RectF& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const RectF&` | `rect` | - |

---

(addquad)=
## `addQuad`

**Signature:**
```cpp
inline void addQuad(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(addupsidedownquad)=
## `addUpsideDownQuad`

**Signature:**
```cpp
inline void addUpsideDownQuad(const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `rect` | - |

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(vertexcount)=
## `vertexCount`

**Signature:**
```cpp
int vertexCount();
```

**Returns:**
- `int`

---

(size)=
## `size`

**Signature:**
```cpp
int size();
```

**Returns:**
- `int`

---

(cache)=
## `cache`

**Signature:**
```cpp
void cache();
```

---

(iscached)=
## `isCached`

**Signature:**
```cpp
bool isCached();
```

**Returns:**
- `bool`

---

(gethardwarecache)=
## `getHardwareCache`

**Signature:**
```cpp
HardwareBuffer* getHardwareCache();
```

**Returns:**
- `HardwareBuffer*`

---
