---
title: "src/framework/graphics/coordsbuffer.h"
source_file: "src/framework/graphics/coordsbuffer.h"
generated_at: "2025-11-01T08:29:23.700Z"
doc_type: "cpp_api"
---

# src/framework/graphics/coordsbuffer.h

(coordsbuffer)=
## `CoordsBuffer`

**Signature:**
```cpp
public: CoordsBuffer();
```

---

(addboudingrect)=
## `addBoudingRect`

**Signature:**
```cpp
void addBoudingRect(const Rect& dest, int innerLineWidth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `int` | `innerLineWidth` | - |

---

(addrepeatedrects)=
## `addRepeatedRects`

**Signature:**
```cpp
void addRepeatedRects(const Rect& dest, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Rect&` | `src` | - |

---

(unlock)=
## `unlock`

**Signature:**
```cpp
void unlock(bool clear = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `bool` | `clear` | `false` | - |

---

(gettexturerect)=
## `getTextureRect`

**Signature:**
```cpp
Rect getTextureRect();
```

**Returns:**
- `Rect`

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(addtriangle)=
## `addTriangle`

**Signature:**
```cpp
void addTriangle(const Point& a, const Point& b, const Point& c);
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
void addRect(const Rect& dest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |

---

(addrect-1)=
## `addRect`

**Signature:**
```cpp
void addRect(const Rect& dest, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Rect&` | `src` | - |

---

(addrect-2)=
## `addRect`

**Signature:**
```cpp
void addRect(const RectF& dest, const RectF& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const RectF&` | `dest` | - |
| `const RectF&` | `src` | - |

---

(addquad)=
## `addQuad`

**Signature:**
```cpp
void addQuad(const Rect& dest, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Rect&` | `src` | - |

---

(addupsidedownquad)=
## `addUpsideDownQuad`

**Signature:**
```cpp
void addUpsideDownQuad(const Rect& dest, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const Rect&` | `src` | - |

---

(getvertexcount)=
## `getVertexCount`

**Signature:**
```cpp
int getVertexCount();
```

**Returns:**
- `int`

---

(gettexturecoordcount)=
## `getTextureCoordCount`

**Signature:**
```cpp
int getTextureCoordCount();
```

**Returns:**
- `int`

---

(getvertexhardwarecache)=
## `getVertexHardwareCache`

**Signature:**
```cpp
HardwareBuffer* getVertexHardwareCache();
```

**Returns:**
- `HardwareBuffer*`

---

(gettexturehardwarecache)=
## `getTextureHardwareCache`

**Signature:**
```cpp
HardwareBuffer* getTextureHardwareCache();
```

**Returns:**
- `HardwareBuffer*`

---

(cache)=
## `cache`

**Signature:**
```cpp
void cache();
```

---
