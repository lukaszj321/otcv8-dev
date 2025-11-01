---
title: "src/framework/sound/soundmanager.h"
source_file: "src/framework/sound/soundmanager.h"
generated_at: "2025-11-01T08:29:23.718Z"
doc_type: "cpp_api"
---

# src/framework/sound/soundmanager.h

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

(poll)=
## `poll`

**Signature:**
```cpp
void poll();
```

---

(setaudioenabled)=
## `setAudioEnabled`

**Signature:**
```cpp
void setAudioEnabled(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(stopall)=
## `stopAll`

**Signature:**
```cpp
void stopAll();
```

---

(preload)=
## `preload`

**Signature:**
```cpp
void preload(std::string filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `filename` | - |

---

(play)=
## `play`

**Signature:**
```cpp
SoundSourcePtr play(std::string filename, float fadetime = 0, float gain = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `std::string` | `filename` |  | - |
| `float` | `fadetime` | `0` | - |
| `float` | `gain` | `0` | - |

**Returns:**
- `SoundSourcePtr`

---

(getchannel)=
## `getChannel`

**Signature:**
```cpp
SoundChannelPtr getChannel(int channel);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `channel` | - |

**Returns:**
- `SoundChannelPtr`

---

(resolvesoundfile)=
## `resolveSoundFile`

**Signature:**
```cpp
std::string resolveSoundFile(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `std::string`

---

(ensurecontext)=
## `ensureContext`

**Signature:**
```cpp
void ensureContext();
```

---

(createsoundsource)=
## `createSoundSource`

**Signature:**
```cpp
private: SoundSourcePtr createSoundSource(const std::string& filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |

**Returns:**
- `SoundSourcePtr`

---

(isaudioenabled)=
## `isAudioEnabled`

**Signature:**
```cpp
bool isAudioEnabled();
```

**Returns:**
- `bool`

---

(enableaudio)=
## `enableAudio`

**Signature:**
```cpp
void enableAudio();
```

---

(disableaudio)=
## `disableAudio`

**Signature:**
```cpp
void disableAudio();
```

---
