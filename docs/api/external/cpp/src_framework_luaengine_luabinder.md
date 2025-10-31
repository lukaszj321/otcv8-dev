---
title: "src/framework/luaengine/luabinder.h"
source_file: "src/framework/luaengine/luabinder.h"
generated_at: "2025-10-31T23:33:30.346Z"
doc_type: "cpp_api"
---

# src/framework/luaengine/luabinder.h

(call_fun_and_push_resultret)=
## `call_fun_and_push_result<Ret>`

**Signature:**
```cpp
return call_fun_and_push_result<Ret>(f, lua, args...);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `f` | - |
| `` | `lua` | - |
| `args...` | - | - |

**Returns:**
- `return`

---

(bind_lambda_funfcall)=
## `bind_lambda_fun<F>::call`

**Signature:**
```cpp
return bind_lambda_fun<F>::call(f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `f` | - |

**Returns:**
- `return`

---

(bind_fun)=
## `bind_fun`

**Signature:**
```cpp
return bind_fun(std::function<Ret(Args...)>(f));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::function&lt;Ret(Args...)&gt;(f)` | - | - |

**Returns:**
- `return`

---

(luaexception)=
## `LuaException`

**Signature:**
```cpp
throw LuaException("failed to call a member function because the passed object is nil");
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `"failed to call a member function because the passed object is nil"` | - | - |

**Returns:**
- `throw`

---

(mf)=
## `mf`

**Signature:**
```cpp
return mf(obj.get(), args...);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `obj.get()` | - | - |
| `args...` | - | - |

**Returns:**
- `return`

---

(luaexception)=
## `LuaException`

**Signature:**
```cpp
throw LuaException("failed to call a member function because the passed object is nil");
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `"failed to call a member function because the passed object is nil"` | - | - |

**Returns:**
- `throw`

---

(mf)=
## `mf`

**Signature:**
```cpp
return mf(obj, lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `obj` | - |
| `` | `lua` | - |

**Returns:**
- `return`

---

(call)=
## `call`

**Signature:**
```cpp
static void call(Tuple& tuple, LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Tuple&` | `tuple` | - |
| `LuaInterface*` | `lua` | - |

**Returns:**
- `static void`

---

(call)=
## `call`

**Signature:**
```cpp
static void call(Tuple& tuple, LuaInterface* lua);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Tuple&` | `tuple` | - |
| `LuaInterface*` | `lua` | - |

**Returns:**
- `static void`

---

(call)=
## `call`

**Signature:**
```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |
| `const F&` | `f` | - |
| `LuaInterface*` | `lua` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `static int`

---

(call)=
## `call`

**Signature:**
```cpp
static int call(const Tuple& tuple, const F& f, LuaInterface* lua, const Args&... args);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Tuple&` | `tuple` | - |
| `const F&` | `f` | - |
| `LuaInterface*` | `lua` | - |
| `const Args&...` | `args` | - |

**Returns:**
- `static int`

---

(bind_fun_specializer)=
## `bind_fun_specializer`

Bind different types of functions generating a lambda

**Signature:**
```cpp
LuaCppFunction bind_fun_specializer(const F& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const F&` | `f` | - |

**Returns:**
- `LuaCppFunction`

---

(bind_fun)=
## `bind_fun`

Bind a customized function

**Signature:**
```cpp
inline LuaCppFunction bind_fun(const std::function<int(LuaInterface*)>& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::function&lt;int(LuaInterface*)&gt;&` | `f` | - |

**Returns:**
- `inline LuaCppFunction`

---

(bind_fun)=
## `bind_fun`

Bind a std::function

**Signature:**
```cpp
LuaCppFunction bind_fun(const std::function<Ret(Args...)>& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::function&lt;Ret(Args...)&gt;&` | `f` | - |

**Returns:**
- `LuaCppFunction`

---

(call)=
## `call`

**Signature:**
```cpp
static LuaCppFunction call(const Lambda& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Lambda&` | `f` | - |

**Returns:**
- `static LuaCppFunction`

---

(stdenable_ifstdis_constructibledecltype)=
## `std::enable_if<std::is_constructible<decltype`

**Signature:**
```cpp
typename std::enable_if<std::is_constructible<decltype(&Lambda::operator())>::value, LuaCppFunction>::type bind_fun(const Lambda& f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `&Lambda::operator())&gt;::` | `value` | - |
| `LuaCppFunction&gt;::type bind_fun(const Lambda&` | `f` | - |

**Returns:**
- `typename`

---

(bind_fun)=
## `bind_fun`

Convert to C++ functions pointers to std::function then bind

**Signature:**
```cpp
LuaCppFunction bind_fun(Ret (*f)(Args...));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Ret (*f)(Args...)` | - | - |

**Returns:**
- `LuaCppFunction`

---

(bind_mem_fun)=
## `bind_mem_fun`

Bind member functions

**Signature:**
```cpp
LuaCppFunction bind_mem_fun(Ret (FC::* f)(Args...));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Ret (FC::* f)(Args...)` | - | - |

**Returns:**
- `LuaCppFunction`

---

(bind_singleton_mem_fun)=
## `bind_singleton_mem_fun`

Bind singleton member functions

**Signature:**
```cpp
LuaCppFunction bind_singleton_mem_fun(Ret (FC::*f)(Args...), C *instance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Ret (FC::*f)(Args...)` | - | - |
| `C *` | `instance` | - |

**Returns:**
- `LuaCppFunction`

---

(bind_mem_fun)=
## `bind_mem_fun`

Bind customized member functions

**Signature:**
```cpp
LuaCppFunction bind_mem_fun(int (C::*f)(LuaInterface*));
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int (C::*f)(LuaInterface*)` | - | - |

**Returns:**
- `LuaCppFunction`

---
