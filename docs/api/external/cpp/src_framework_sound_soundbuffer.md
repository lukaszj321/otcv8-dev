---
title: "src/framework/sound/soundbuffer.h"
source_file: "src/framework/sound/soundbuffer.h"
generated_at: "2025-10-31T23:33:30.356Z"
doc_type: "cpp_api"
---

# src/framework/sound/soundbuffer.h

(soundbuffer)=
## `SoundBuffer`

**Signature:**
```cpp
public: SoundBuffer();
```

**Returns:**
- `public:`

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

(fillbuffer)=
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
