---
title: "src/framework/util/matrix.h"
source_file: "src/framework/util/matrix.h"
generated_at: "2025-11-01T00:11:49.070Z"
doc_type: "cpp_api"
---

# src/framework/util/matrix.h

(setidentity)=
## `setIdentity`

**Signature:**
```cpp
void setIdentity();
```

---

(isidentity)=
## `isIdentity`

**Signature:**
```cpp
bool isIdentity();
```

**Returns:**
- `bool`

---

(fill)=
## `fill`

**Signature:**
```cpp
void fill(T value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `value` | - |

---

(mat)=
## `mat`

**Signature:**
```cpp
out << mat(i,j);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `i` | - | - |
| `j` | - | - |

**Returns:**
- `out &lt;&lt;`

---

(mat-1)=
## `mat`

**Signature:**
```cpp
in >> mat(i,j);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `i` | - | - |
| `j` | - | - |

**Returns:**
- `in &gt;&gt;`

---

(matrix)=
## `Matrix`

**Signature:**
```cpp
public: Matrix();
```

---

(matrix-1)=
## `Matrix`

**Signature:**
```cpp
template<typename U> Matrix(const std::initializer_list<U>& values);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::initializer_list&lt;U&gt;&` | `values` | - |

**Returns:**
- `template&lt;typename U&gt;`

---

(matrix-2)=
## `Matrix`

**Signature:**
```cpp
template<typename U> Matrix(const U *values);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const U *values` | - | - |

**Returns:**
- `template&lt;typename U&gt;`

---

(operator)=
## `operator`

**Signature:**
```cpp
T& operator()(int row, int column);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `)(int` | `row` | - |
| `int` | `column` | - |

**Returns:**
- `T&`

---

(operator-1)=
## `operator<<`

**Signature:**
```cpp
std::ostream& operator<<(std::ostream& out, const Matrix<N,M,T>& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostream&` | `out` | - |
| `const Matrix&lt;N,M,T&gt;&` | `mat` | - |

**Returns:**
- `std::ostream&`

---

(operator-2)=
## `operator>>`

**Signature:**
```cpp
std::istream& operator>>(std::istream& in, Matrix<N,M,T>& mat);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream&` | `in` | - |
| `Matrix&lt;N,M,T&gt;&` | `mat` | - |

**Returns:**
- `std::istream&`

---
