---
title: "src/framework/stdext/shared_object.h"
source_file: "src/framework/stdext/shared_object.h"
generated_at: "2025-11-01T08:46:04.936Z"
doc_type: "cpp_api"
---

# src/framework/stdext/shared_object.h

(add_ref)=
## `add_ref`

**Signature:**
```cpp
void add_ref();
```

---

(dec_ref)=
## `dec_ref`

**Signature:**
```cpp
void dec_ref();
```

---

(ref_count)=
## `ref_count`

**Signature:**
```cpp
refcount_t ref_count();
```

**Returns:**
- `refcount_t`

---

(static_self_cast)=
## `static_self_cast`

**Signature:**
```cpp
stdext::shared_object_ptr<T> static_self_cast();
```

**Returns:**
- `stdext::shared_object_ptr&lt;T&gt;`

---

(dynamic_self_cast)=
## `dynamic_self_cast`

**Signature:**
```cpp
stdext::shared_object_ptr<T> dynamic_self_cast();
```

**Returns:**
- `stdext::shared_object_ptr&lt;T&gt;`

---

(const_self_cast)=
## `const_self_cast`

**Signature:**
```cpp
stdext::shared_object_ptr<T> const_self_cast();
```

**Returns:**
- `stdext::shared_object_ptr&lt;T&gt;`

---

(reset)=
## `reset`

**Signature:**
```cpp
void reset();
```

---

(reset-1)=
## `reset`

**Signature:**
```cpp
void reset(T* rhs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T*` | `rhs` | - |

---

(swap)=
## `swap`

**Signature:**
```cpp
void swap(shared_object_ptr& rhs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `shared_object_ptr&` | `rhs` | - |

---

(get)=
## `get`

**Signature:**
```cpp
T* get();
```

**Returns:**
- `T*`

---

(use_count)=
## `use_count`

**Signature:**
```cpp
refcount_t use_count();
```

**Returns:**
- `refcount_t`

---

(is_unique)=
## `is_unique`

**Signature:**
```cpp
bool is_unique();
```

**Returns:**
- `bool`

---

(operator)=
## `operator*`

**Signature:**
```cpp
T& operator*();
```

**Returns:**
- `T&`

---

(unspecified_bool_type)=
## `unspecified_bool_type`

**Signature:**
```cpp
operator unspecified_bool_type();
```

**Returns:**
- `operator`

---

(add_ref-1)=
## `add_ref`

**Signature:**
```cpp
private: void add_ref();
```

---

(dec_ref-1)=
## `dec_ref`

**Signature:**
```cpp
void dec_ref();
```

---

(operator-1)=
## `operator<`

**Signature:**
```cpp
bool operator<(shared_object_ptr<T> const& a, shared_object_ptr<T> const& b);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `shared_object_ptr&lt;T&gt; const&` | `a` | - |
| `shared_object_ptr&lt;T&gt; const&` | `b` | - |

**Returns:**
- `bool`

---

(get_pointer)=
## `get_pointer`

**Signature:**
```cpp
T* get_pointer(shared_object_ptr<T> const& p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `shared_object_ptr&lt;T&gt; const&` | `p` | - |

**Returns:**
- `T*`

---

(static_pointer_cast)=
## `static_pointer_cast`

**Signature:**
```cpp
shared_object_ptr<T> static_pointer_cast(shared_object_ptr<U> const& p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `shared_object_ptr&lt;U&gt; const&` | `p` | - |

**Returns:**
- `shared_object_ptr&lt;T&gt;`

---

(const_pointer_cast)=
## `const_pointer_cast`

**Signature:**
```cpp
shared_object_ptr<T> const_pointer_cast(shared_object_ptr<U> const& p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `shared_object_ptr&lt;U&gt; const&` | `p` | - |

**Returns:**
- `shared_object_ptr&lt;T&gt;`

---

(dynamic_pointer_cast)=
## `dynamic_pointer_cast`

**Signature:**
```cpp
shared_object_ptr<T> dynamic_pointer_cast(shared_object_ptr<U> const& p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `shared_object_ptr&lt;U&gt; const&` | `p` | - |

**Returns:**
- `shared_object_ptr&lt;T&gt;`

---

(make_shared_object)=
## `make_shared_object`

**Signature:**
```cpp
stdext::shared_object_ptr<T> make_shared_object(Args... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Args...` | `args` | - |

**Returns:**
- `stdext::shared_object_ptr&lt;T&gt;`

---

(swap-1)=
## `swap`

**Signature:**
```cpp
void swap(stdext::shared_object_ptr<T>& lhs, stdext::shared_object_ptr<T>& rhs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `stdext::shared_object_ptr&lt;T&gt;&` | `lhs` | - |
| `stdext::shared_object_ptr&lt;T&gt;&` | `rhs` | - |

---
