---
title: "src/framework/graphics/framebuffermanager.h"
source_file: "src/framework/graphics/framebuffermanager.h"
generated_at: "2025-10-31T23:33:30.341Z"
doc_type: "cpp_api"
---

# src/framework/graphics/framebuffermanager.h

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

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(createframebuffer)=
## `createFrameBuffer`

**Signature:**
```cpp
FrameBufferPtr createFrameBuffer(bool withDepth = false);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool withDepth =` | `false` | - |

**Returns:**
- `FrameBufferPtr`

---

(gettemporaryframebuffer)=
## `getTemporaryFrameBuffer`

**Signature:**
```cpp
const FrameBufferPtr& getTemporaryFrameBuffer();
```

**Returns:**
- `const FrameBufferPtr&`

---

(getdrawqueuetemporaryframebuffer)=
## `getDrawQueueTemporaryFrameBuffer`

**Signature:**
```cpp
const FrameBufferPtr& getDrawQueueTemporaryFrameBuffer();
```

**Returns:**
- `const FrameBufferPtr&`

---
