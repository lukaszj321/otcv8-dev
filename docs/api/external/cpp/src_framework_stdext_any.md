---
title: "src/framework/stdext/any.h"
source_file: "src/framework/stdext/any.h"
generated_at: "2025-10-31T23:33:30.358Z"
doc_type: "cpp_api"
---

# src/framework/stdext/any.h

(type)=
## `type`

**Signature:**
```cpp
virtual const std::type_info& type();
```

**Returns:**
- `virtual const std::type_info&`

---

(clone)=
## `clone`

**Signature:**
```cpp
virtual placeholder* clone();
```

**Returns:**
- `virtual placeholder*`

---

(cast)=
## `cast`

**Signature:**
```cpp
const T& cast();
```

**Returns:**
- `const T&`

---

(type)=
## `type`

**Signature:**
```cpp
const std::type_info& type();
```

**Returns:**
- `const std::type_info&`

---

(clone)=
## `clone`

**Signature:**
```cpp
placeholder* clone();
```

**Returns:**
- `placeholder*`

---

(any)=
## `any`

**Signature:**
```cpp
template<typename T> any(const T& value) : content(new holder<T>(value));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T& value) : content(new holder&lt;T&gt;(value)` | - | - |

**Returns:**
- `template&lt;typename T&gt;`

---

(swap)=
## `swap`

**Signature:**
```cpp
any& swap(any& rhs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `any&` | `rhs` | - |

**Returns:**
- `any&`

---

(empty)=
## `empty`

**Signature:**
```cpp
bool empty();
```

**Returns:**
- `bool`

---

(type)=
## `type`

**Signature:**
```cpp
const std::type_info & type();
```

**Returns:**
- `const std::type_info &`

---

(any_cast)=
## `any_cast`

**Signature:**
```cpp
const T& any_cast(const any& operand);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const any&` | `operand` | - |

**Returns:**
- `const T&`

---

(anycast)=
## `any::cast`

**Signature:**
```cpp
const T& any::cast();
```

**Returns:**
- `const T&`

---
