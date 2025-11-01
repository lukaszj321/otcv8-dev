---
title: "src/framework/util/size.h"
source_file: "src/framework/util/size.h"
generated_at: "2025-11-01T08:29:23.730Z"
doc_type: "cpp_api"
---

# src/framework/util/size.h

(topoint)=
## `toPoint`

**Signature:**
```cpp
TPoint<T> toPoint();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(isnull)=
## `isNull`

**Signature:**
```cpp
bool isNull();
```

**Returns:**
- `bool`

---

(isempty)=
## `isEmpty`

**Signature:**
```cpp
bool isEmpty();
```

**Returns:**
- `bool`

---

(isvalid)=
## `isValid`

**Signature:**
```cpp
bool isValid();
```

**Returns:**
- `bool`

---

(resize)=
## `resize`

**Signature:**
```cpp
void resize(T w, T h);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `w` | - |
| `T` | `h` | - |

---

(setwidth)=
## `setWidth`

**Signature:**
```cpp
void setWidth(T w);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `w` | - |

---

(setheight)=
## `setHeight`

**Signature:**
```cpp
void setHeight(T h);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `h` | - |

---

(operator)=
## `operator*`

**Signature:**
```cpp
TSize<T> operator*(const TSize<T>& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&` | `other` | - |

**Returns:**
- `TSize&lt;T&gt;`

---

(operator-1)=
## `operator*`

**Signature:**
```cpp
TSize<T> operator*(const float v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const float` | `v` | - |

**Returns:**
- `TSize&lt;T&gt;`

---

(operator-2)=
## `operator<`

**Signature:**
```cpp
bool operator<(const TSize<T>&other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&other` | - | - |

**Returns:**
- `bool`

---

(operator-3)=
## `operator>`

**Signature:**
```cpp
bool operator>(const TSize<T>&other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&other` | - | - |

**Returns:**
- `bool`

---

(expandedto)=
## `expandedTo`

**Signature:**
```cpp
TSize<T> expandedTo(const TSize<T>& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&` | `other` | - |

**Returns:**
- `TSize&lt;T&gt;`

---

(boundedto)=
## `boundedTo`

**Signature:**
```cpp
TSize<T> boundedTo(const TSize<T>& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&` | `other` | - |

**Returns:**
- `TSize&lt;T&gt;`

---

(scale)=
## `scale`

**Signature:**
```cpp
void scale(const TSize<T>& s, Fw::AspectRatioMode mode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&` | `s` | - |
| `Fw::AspectRatioMode` | `mode` | - |

---

(scale-1)=
## `scale`

**Signature:**
```cpp
void scale(int w, int h, Fw::AspectRatioMode mode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `w` | - |
| `int` | `h` | - |
| `Fw::AspectRatioMode` | `mode` | - |

---

(ratio)=
## `ratio`

**Signature:**
```cpp
float ratio();
```

**Returns:**
- `float`

---

(operator-4)=
## `operator<<`

**Signature:**
```cpp
std::ostream& operator<<(std::ostream& out, const TSize<T>& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostream&` | `out` | - |
| `const TSize&lt;T&gt;&` | `size` | - |

**Returns:**
- `std::ostream&`

---

(operator-5)=
## `operator>>`

**Signature:**
```cpp
std::istream& operator>>(std::istream& in, TSize<T>& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream&` | `in` | - |
| `TSize&lt;T&gt;&` | `size` | - |

**Returns:**
- `std::istream&`

---
