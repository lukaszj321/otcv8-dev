---
title: "src/framework/stdext/math.h"
source_file: "src/framework/stdext/math.h"
generated_at: "2025-11-01T06:09:06.204Z"
doc_type: "cpp_api"
---

# src/framework/stdext/math.h

(adler32)=
## `adler32`

**Signature:**
```cpp
uint32_t adler32(const uint8_t *buffer, size_t size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uint8_t *buffer` | - | - |
| `size_t` | `size` | - |

**Returns:**
- `uint32_t`

---

(random_range)=
## `random_range`

**Signature:**
```cpp
long random_range(long min, long max);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `long` | `min` | - |
| `long` | `max` | - |

**Returns:**
- `long`

---

(random_range-1)=
## `random_range`

**Signature:**
```cpp
float random_range(float min, float max);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `min` | - |
| `float` | `max` | - |

**Returns:**
- `float`

---

(round)=
## `round`

**Signature:**
```cpp
double round(double r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `double` | `r` | - |

**Returns:**
- `double`

---

(is_power_of_two)=
## `is_power_of_two`

**Signature:**
```cpp
inline bool is_power_of_two(size_t v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `v` | - |

**Returns:**
- `bool`

---

(to_power_of_two)=
## `to_power_of_two`

**Signature:**
```cpp
inline size_t to_power_of_two(size_t v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `size_t` | `v` | - |

**Returns:**
- `size_t`

---

(readule16)=
## `readULE16`

**Signature:**
```cpp
inline uint16_t readULE16(const uchar *addr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uchar *addr` | - | - |

**Returns:**
- `uint16_t`

---

(readule32)=
## `readULE32`

**Signature:**
```cpp
inline uint32_t readULE32(const uchar *addr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uchar *addr` | - | - |

**Returns:**
- `uint32_t`

---

(readule64)=
## `readULE64`

**Signature:**
```cpp
inline uint64_t readULE64(const uchar *addr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uchar *addr` | - | - |

**Returns:**
- `uint64_t`

---

(writeule16)=
## `writeULE16`

**Signature:**
```cpp
inline void writeULE16(uchar *addr, uint16_t value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar *addr` | - | - |
| `uint16_t` | `value` | - |

---

(writeule32)=
## `writeULE32`

**Signature:**
```cpp
inline void writeULE32(uchar *addr, uint32_t value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar *addr` | - | - |
| `uint32_t` | `value` | - |

---

(writeule64)=
## `writeULE64`

**Signature:**
```cpp
inline void writeULE64(uchar *addr, uint64_t value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar *addr` | - | - |
| `uint64_t` | `value` | - |

---

(readsle16)=
## `readSLE16`

**Signature:**
```cpp
inline int16_t readSLE16(const uchar *addr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uchar *addr` | - | - |

**Returns:**
- `int16_t`

---

(readsle32)=
## `readSLE32`

**Signature:**
```cpp
inline int32_t readSLE32(const uchar *addr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uchar *addr` | - | - |

**Returns:**
- `int32_t`

---

(readsle64)=
## `readSLE64`

**Signature:**
```cpp
inline int64_t readSLE64(const uchar *addr);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const uchar *addr` | - | - |

**Returns:**
- `int64_t`

---

(writesle16)=
## `writeSLE16`

**Signature:**
```cpp
inline void writeSLE16(uchar *addr, int16_t value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar *addr` | - | - |
| `int16_t` | `value` | - |

---

(writesle32)=
## `writeSLE32`

**Signature:**
```cpp
inline void writeSLE32(uchar *addr, int32_t value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar *addr` | - | - |
| `int32_t` | `value` | - |

---

(writesle64)=
## `writeSLE64`

**Signature:**
```cpp
inline void writeSLE64(uchar *addr, int64_t value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar *addr` | - | - |
| `int64_t` | `value` | - |

---

(clamp)=
## `clamp`

**Signature:**
```cpp
template<typename T> T clamp(T x, T min, T max);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `x` | - |
| `T` | `min` | - |
| `T` | `max` | - |

**Returns:**
- `template&lt;typename T&gt; T`

---
