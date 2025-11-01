---
title: "src/framework/graphics/graph.h"
source_file: "src/framework/graphics/graph.h"
generated_at: "2025-11-01T04:06:42.748Z"
doc_type: "cpp_api"
---

# src/framework/graphics/graph.h

(graph)=
## `Graph`

**Signature:**
```cpp
public: Graph(const std::string& name, size_t capacity = 100);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `name` |  | - |
| `size_t` | `capacity` | `100` | - |

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw(const Rect& dest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(addvalue)=
## `addValue`

**Signature:**
```cpp
void addValue(int value, bool ignoreSmallValues = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `value` |  | - |
| `bool` | `ignoreSmallValues` | `false` | - |

---
