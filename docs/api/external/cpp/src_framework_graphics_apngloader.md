---
title: "src/framework/graphics/apngloader.h"
source_file: "src/framework/graphics/apngloader.h"
generated_at: "2025-11-01T08:45:15.299Z"
doc_type: "cpp_api"
---

# src/framework/graphics/apngloader.h

(load_apng)=
## `load_apng`

**Signature:**
```cpp
int load_apng(std::stringstream& file, struct apng_data *apng);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::stringstream&` | `file` | - |
| `struct apng_data *apng` | - | - |

**Returns:**
- `int`

---

(save_png)=
## `save_png`

**Signature:**
```cpp
void save_png(std::stringstream& file, unsigned int width, unsigned int height, int channels, unsigned char *pixels);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::stringstream&` | `file` | - |
| `unsigned int` | `width` | - |
| `unsigned int` | `height` | - |
| `int` | `channels` | - |
| `unsigned char *pixels` | - | - |

---

(free_apng)=
## `free_apng`

**Signature:**
```cpp
void free_apng(struct apng_data *apng);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `struct apng_data *apng` | - | - |

