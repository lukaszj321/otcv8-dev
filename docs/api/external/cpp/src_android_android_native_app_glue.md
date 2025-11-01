---
title: "src/android/android_native_app_glue.h"
source_file: "src/android/android_native_app_glue.h"
generated_at: "2025-11-01T08:19:49.411Z"
doc_type: "cpp_api"
---

# src/android/android_native_app_glue.h

(android_app_read_cmd)=
## `android_app_read_cmd`

Call when ALooper_pollAll() returns LOOPER_ID_MAIN, reading the next
app command message.

**Signature:**
```cpp
int8_t android_app_read_cmd(struct android_app* android_app);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `struct android_app*` | `android_app` | - |

**Returns:**
- `int8_t`

---

(android_app_pre_exec_cmd)=
## `android_app_pre_exec_cmd`

Call with the command returned by android_app_read_cmd() to do the
initial pre-processing of the given command.  You can perform your own
actions for the command after calling this function.

**Signature:**
```cpp
void android_app_pre_exec_cmd(struct android_app* android_app, int8_t cmd);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `struct android_app*` | `android_app` | - |
| `int8_t` | `cmd` | - |

---

(android_app_post_exec_cmd)=
## `android_app_post_exec_cmd`

Call with the command returned by android_app_read_cmd() to do the
final post-processing of the given command.  You must have done your own
actions for the command before calling this function.

**Signature:**
```cpp
void android_app_post_exec_cmd(struct android_app* android_app, int8_t cmd);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `struct android_app*` | `android_app` | - |
| `int8_t` | `cmd` | - |

---

(android_main)=
## `android_main`

This is the function that application code must implement, representing
the main entry to the app.

**Signature:**
```cpp
extern void android_main(struct android_app* app);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `struct android_app*` | `app` | - |

**Returns:**
- `extern void`

---
