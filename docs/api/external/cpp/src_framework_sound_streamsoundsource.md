---
title: "src/framework/sound/streamsoundsource.h"
source_file: "src/framework/sound/streamsoundsource.h"
generated_at: "2025-11-01T06:09:06.202Z"
doc_type: "cpp_api"
---

# src/framework/sound/streamsoundsource.h

(play)=
## `play`

**Signature:**
```cpp
void play();
```

---

(stop)=
## `stop`

**Signature:**
```cpp
void stop();
```

---

(setsoundfile)=
## `setSoundFile`

**Signature:**
```cpp
void setSoundFile(const SoundFilePtr& soundFile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const SoundFilePtr&` | `soundFile` | - |

---

(downmix)=
## `downMix`

**Signature:**
```cpp
void downMix(DownMix downMix);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `DownMix` | `downMix` | - |

---

(update)=
## `update`

**Signature:**
```cpp
void update();
```

---

(queuebuffers)=
## `queueBuffers`

**Signature:**
```cpp
private: void queueBuffers();
```

---

(unqueuebuffers)=
## `unqueueBuffers`

**Signature:**
```cpp
void unqueueBuffers();
```

---

(fillbufferandqueue)=
## `fillBufferAndQueue`

**Signature:**
```cpp
bool fillBufferAndQueue(uint buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint` | `buffer` | - |

**Returns:**
- `bool`

---

(isplaying)=
## `isPlaying`

**Signature:**
```cpp
bool isPlaying();
```

**Returns:**
- `bool`

---
