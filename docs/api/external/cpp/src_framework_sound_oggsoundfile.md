---
title: "src/framework/sound/oggsoundfile.h"
source_file: "src/framework/sound/oggsoundfile.h"
generated_at: "2025-11-01T08:45:15.318Z"
doc_type: "cpp_api"
---

# src/framework/sound/oggsoundfile.h

(oggsoundfile)=
## `OggSoundFile`

**Signature:**
```cpp
public: OggSoundFile(const FileStreamPtr& fileStream);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FileStreamPtr&` | `fileStream` | - |

---

(prepareogg)=
## `prepareOgg`

**Signature:**
```cpp
bool prepareOgg();
```

**Returns:**
- `bool`

---

(read)=
## `read`

**Signature:**
```cpp
int read(void *buffer, int bufferSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void *buffer` | - | - |
| `int` | `bufferSize` | - |

**Returns:**
- `int`

---

(reset)=
## `reset`

**Signature:**
```cpp
void reset();
```

---

(cb_read)=
## `cb_read`

**Signature:**
```cpp
private: static size_t cb_read(void* ptr, size_t size, size_t nmemb, void* source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void*` | `ptr` | - |
| `size_t` | `size` | - |
| `size_t` | `nmemb` | - |
| `void*` | `source` | - |

**Returns:**
- `size_t`

---

(cb_seek)=
## `cb_seek`

**Signature:**
```cpp
static int cb_seek(void* source, ogg_int64_t offset, int whence);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void*` | `source` | - |
| `ogg_int64_t` | `offset` | - |
| `int` | `whence` | - |

**Returns:**
- `int`

---

(cb_close)=
## `cb_close`

**Signature:**
```cpp
static int cb_close(void* source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void*` | `source` | - |

**Returns:**
- `int`

---

(cb_tell)=
## `cb_tell`

**Signature:**
```cpp
static long cb_tell(void* source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void*` | `source` | - |

**Returns:**
- `long`

