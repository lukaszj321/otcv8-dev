---
title: "src/framework/util/point.h"
source_file: "src/framework/util/point.h"
generated_at: "2025-11-01T06:09:06.213Z"
doc_type: "cpp_api"
---

# src/framework/util/point.h

(isnull)=
## `isNull`

**Signature:**
```cpp
bool isNull();
```

**Returns:**
- `bool`

---

(tosize)=
## `toSize`

**Signature:**
```cpp
TSize<T> toSize();
```

**Returns:**
- `TSize&lt;T&gt;`

---

(operator)=
## `operator*`

**Signature:**
```cpp
TPoint<T> operator*(const TPoint<T>& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt;&` | `other` | - |

**Returns:**
- `TPoint&lt;T&gt;`

---

(operator-1)=
## `operator*`

**Signature:**
```cpp
TPoint<T> operator*(float v);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `v` | - |

**Returns:**
- `TPoint&lt;T&gt;`

---

(operator-2)=
## `operator&`

**Signature:**
```cpp
TPoint<T> operator&(int a);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `a` | - |

**Returns:**
- `TPoint&lt;T&gt;`

---

(operator-3)=
## `operator<`

**Signature:**
```cpp
bool operator<(const TPoint<T>&other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt;&other` | - | - |

**Returns:**
- `bool`

---

(operator-4)=
## `operator>`

**Signature:**
```cpp
bool operator>(const TPoint<T>&other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt;&other` | - | - |

**Returns:**
- `bool`

---

(length)=
## `length`

**Signature:**
```cpp
float length();
```

**Returns:**
- `float`

---

(distancefrom)=
## `distanceFrom`

**Signature:**
```cpp
float distanceFrom(const TPoint<T>& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt;&` | `other` | - |

**Returns:**
- `float`

---

(operator-5)=
## `operator<<`

**Signature:**
```cpp
std::ostream& operator<<(std::ostream& out, const TPoint<T>& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostream&` | `out` | - |
| `const TPoint&lt;T&gt;&` | `point` | - |

**Returns:**
- `std::ostream&`

---

(operator-6)=
## `operator>>`

**Signature:**
```cpp
std::istream& operator>>(std::istream& in, TPoint<T>& point);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream&` | `in` | - |
| `TPoint&lt;T&gt;&` | `point` | - |

**Returns:**
- `std::istream&`

---
