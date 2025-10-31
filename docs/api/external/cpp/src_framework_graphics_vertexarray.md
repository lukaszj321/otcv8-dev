---
title: "src/framework/graphics/vertexarray.h"
source_file: "src/framework/graphics/vertexarray.h"
generated_at: "2025-10-31T23:33:30.345Z"
doc_type: "cpp_api"
---

# src/framework/graphics/vertexarray.h

(vertexarray)=
## `VertexArray`

**Signature:**
```cpp
public: VertexArray();
```

**Returns:**
- `public:`

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

**Returns:**
- `inline void`

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

**Returns:**
- `inline void`

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

**Returns:**
- `inline void`

---

(addrect)=
## `addRect`

**Signature:**
```cpp
inline void addRect(const RectF& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const RectF&` | `rect` | - |

**Returns:**
- `inline void`

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

**Returns:**
- `inline void`

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

**Returns:**
- `inline void`

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
