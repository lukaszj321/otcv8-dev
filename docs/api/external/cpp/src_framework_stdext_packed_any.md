---
title: "src/framework/stdext/packed_any.h"
source_file: "src/framework/stdext/packed_any.h"
generated_at: "2025-10-31T23:33:30.361Z"
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
| `std::` | `size_t` | - |

**Returns:**
- `else return`

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

(packed_any)=
## `packed_any`

**Signature:**
```cpp
template<typename T> packed_any(const T& value, typename std::enable_if<(can_pack_in_any<T>::value)>::type* = nullptr) : content(reinterpret_cast<placeholder*>(static_cast<std::size_t>(value))), scalar(true);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `value` | - |
| `typename std::enable_if&lt;(can_pack_in_any&lt;T&gt;::value)&gt;::type* = nullptr) : content(reinterpret_cast&lt;placeholder*&gt;(static_cast&lt;std::size_t&gt;(value)))` | - | - |
| `scalar(` | `true` | - |

**Returns:**
- `template&lt;typename T&gt;`

---

(packed_any)=
## `packed_any`

**Signature:**
```cpp
template<typename T> packed_any(const T& value, typename std::enable_if<!(can_pack_in_any<T>::value)>::type* = nullptr) : content(new holder<T>(value)), scalar(false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const T&` | `value` | - |
| `typename std::enable_if&lt;!(can_pack_in_any&lt;T&gt;::value)&gt;::type* = nullptr) : content(new holder&lt;T&gt;(value))` | - | - |
| `scalar(` | `false` | - |

**Returns:**
- `template&lt;typename T&gt;`

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

(type)=
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
