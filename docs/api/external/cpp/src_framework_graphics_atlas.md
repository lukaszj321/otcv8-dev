---
title: "src/framework/graphics/atlas.h"
source_file: "src/framework/graphics/atlas.h"
generated_at: "2025-11-01T08:19:49.439Z"
doc_type: "cpp_api"
---

# src/framework/graphics/atlas.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(reload)=
## `reload`

**Signature:**
```cpp
void reload();
```

---

(cache)=
## `cache`

**Signature:**
```cpp
Point cache(uint64_t hash, const Size& size, bool& draw);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint64_t` | `hash` | - |
| `const Size&` | `size` | - |
| `bool&` | `draw` | - |

**Returns:**
- `Point`

---

(cachefont)=
## `cacheFont`

**Signature:**
```cpp
Point cacheFont(const TexturePtr& fontTexture);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TexturePtr&` | `fontTexture` | - |

**Returns:**
- `Point`

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

(reset)=
## `reset`

**Signature:**
```cpp
private: void reset();
```

---

(resetatlas)=
## `resetAtlas`

**Signature:**
```cpp
void resetAtlas(int location);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |

---

(findspace)=
## `findSpace`

**Signature:**
```cpp
bool findSpace(int location, int index);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |
| `int` | `index` | - |

**Returns:**
- `bool`

---

(calculateindex)=
## `calculateIndex`

**Signature:**
```cpp
inline int calculateIndex(const Size& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `size` | - |

**Returns:**
- `int`

---

(get)=
## `get`

**Signature:**
```cpp
TexturePtr get(int location);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `location` | - |

**Returns:**
- `TexturePtr`

---
