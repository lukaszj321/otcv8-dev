---
title: "src/framework/stdext/packed_any.h"
source_file: "src/framework/stdext/packed_any.h"
generated_at: "2025-11-01T08:46:04.936Z"
doc_type: "cpp_api"
---

# src/framework/stdext/packed_any.h

(type)=
## `type`

**Signature:**
```cpp
virtual const std::type_info& type();
```

**Returns:**
- `const std::type_info&`

---

(clone)=
## `clone`

**Signature:**
```cpp
virtual placeholder* clone();
```

**Returns:**
- `placeholder*`

---

(cast)=
## `cast`

**Signature:**
```cpp
template<typename T> T cast();
```

**Returns:**
- `template&lt;typename T&gt; T`

---

(typeid)=
## `typeid`

**Signature:**
```cpp
else return typeid(std::size_t);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::size_t` | - | - |

**Returns:**
- `else return`

---

(type-1)=
## `type`

**Signature:**
```cpp
const std::type_info& type();
```

**Returns:**
- `const std::type_info&`

---

(clone-1)=
## `clone`

**Signature:**
```cpp
placeholder* clone();
```

**Returns:**
- `placeholder*`

---

(swap)=
## `swap`

**Signature:**
```cpp
packed_any& swap(packed_any& rhs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `packed_any&` | `rhs` | - |

**Returns:**
- `packed_any&`

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

(type-2)=
## `type`

**Signature:**
```cpp
const std::type_info& type();
```

**Returns:**
- `const std::type_info&`

---

(packed_anycast)=
## `packed_any::cast`

**Signature:**
```cpp
template<typename T> T packed_any::cast();
```

**Returns:**
- `template&lt;typename T&gt; T`

---
