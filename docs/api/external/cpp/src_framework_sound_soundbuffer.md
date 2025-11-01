---
title: "src/framework/sound/soundbuffer.h"
source_file: "src/framework/sound/soundbuffer.h"
generated_at: "2025-11-01T00:11:49.059Z"
doc_type: "cpp_api"
---

# src/framework/sound/soundbuffer.h

(soundbuffer)=
## `SoundBuffer`

**Signature:**
```cpp
public: SoundBuffer();
```

---

(fillbuffer)=
## `fillBuffer`

**Signature:**
```cpp
bool fillBuffer(const SoundFilePtr& soundFile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const SoundFilePtr&` | `soundFile` | - |

**Returns:**
- `bool`

---

(fillbuffer-1)=
## `fillBuffer`

**Signature:**
```cpp
bool fillBuffer(ALenum sampleFormat, const DataBuffer<char>& data, int size, int rate);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ALenum` | `sampleFormat` | - |
| `const DataBuffer&lt;char&gt;&` | `data` | - |
| `int` | `size` | - |
| `int` | `rate` | - |

**Returns:**
- `bool`

---

(getbufferid)=
## `getBufferId`

**Signature:**
```cpp
uint getBufferId();
```

**Returns:**
- `uint`

---
