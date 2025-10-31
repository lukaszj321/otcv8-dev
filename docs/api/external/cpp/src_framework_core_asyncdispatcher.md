---
title: "src/framework/core/asyncdispatcher.h"
source_file: "src/framework/core/asyncdispatcher.h"
generated_at: "2025-10-31T23:33:30.332Z"
doc_type: "cpp_api"
---

# src/framework/core/asyncdispatcher.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

**Returns:**
- `public: void`

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(spawn_thread)=
## `spawn_thread`

**Signature:**
```cpp
void spawn_thread();
```

---

(stop)=
## `stop`

**Signature:**
```cpp
void stop();
```

---

(lock)=
## `lock`

**Signature:**
```cpp
std::lock_guard<std::mutex> lock(m_mutex);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `m_mutex` | - |

**Returns:**
- `std::lock_guard&lt;std::mutex&gt;`

---

(stdinvoke_resultftype)=
## `std::invoke_result<F>::type>`

**Signature:**
```cpp
return std::shared_future<typename std::invoke_result<F>::type>(prom->get_future());
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `prom-&gt;get_future()` | - | - |

**Returns:**
- `return std::shared_future&lt;typename`

---

(lock)=
## `lock`

**Signature:**
```cpp
std::lock_guard<std::mutex> lock(m_mutex);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `` | `m_mutex` | - |

**Returns:**
- `std::lock_guard&lt;std::mutex&gt;`

---

(exec_loop)=
## `exec_loop`

**Signature:**
```cpp
protected: void exec_loop();
```

**Returns:**
- `protected: void`

---

(schedule)=
## `schedule`

**Signature:**
```cpp
std::shared_future<typename std::invoke_result<F>::type> schedule(const F& task);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const F&` | `task` | - |

**Returns:**
- `std::shared_future&lt;typename std::invoke_result&lt;F&gt;::type&gt;`

---

(dispatch)=
## `dispatch`

**Signature:**
```cpp
void dispatch(std::function<void()> f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::function&lt;void()&gt;` | `f` | - |

---
