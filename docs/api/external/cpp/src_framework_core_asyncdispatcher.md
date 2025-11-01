---
title: "src/framework/core/asyncdispatcher.h"
source_file: "src/framework/core/asyncdispatcher.h"
generated_at: "2025-11-01T00:11:49.032Z"
doc_type: "cpp_api"
---

# src/framework/core/asyncdispatcher.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

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
| `m_mutex` | - | - |

**Returns:**
- `std::lock_guard&lt;std::mutex&gt;`

---

(lock-1)=
## `lock`

**Signature:**
```cpp
std::lock_guard<std::mutex> lock(m_mutex);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `m_mutex` | - | - |

**Returns:**
- `std::lock_guard&lt;std::mutex&gt;`

---

(exec_loop)=
## `exec_loop`

**Signature:**
```cpp
protected: void exec_loop();
```

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
