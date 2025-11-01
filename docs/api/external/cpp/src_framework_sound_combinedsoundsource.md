---
title: "src/framework/sound/combinedsoundsource.h"
source_file: "src/framework/sound/combinedsoundsource.h"
generated_at: "2025-11-01T00:11:49.058Z"
doc_type: "cpp_api"
---

# src/framework/sound/combinedsoundsource.h

(combinedsoundsource)=
## `CombinedSoundSource`

**Signature:**
```cpp
public: CombinedSoundSource();
```

---

(addsource)=
## `addSource`

**Signature:**
```cpp
void addSource(const SoundSourcePtr& source);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const SoundSourcePtr&` | `source` | - |

---

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

(isbuffering)=
## `isBuffering`

**Signature:**
```cpp
bool isBuffering();
```

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

(setlooping)=
## `setLooping`

**Signature:**
```cpp
void setLooping(bool looping);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `looping` | - |

---

(setrelative)=
## `setRelative`

**Signature:**
```cpp
void setRelative(bool relative);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `relative` | - |

---

(setreferencedistance)=
## `setReferenceDistance`

**Signature:**
```cpp
void setReferenceDistance(float distance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `distance` | - |

---

(setgain)=
## `setGain`

**Signature:**
```cpp
void setGain(float gain);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `gain` | - |

---

(setpitch)=
## `setPitch`

**Signature:**
```cpp
void setPitch(float pitch);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `pitch` | - |

---

(setposition)=
## `setPosition`

**Signature:**
```cpp
void setPosition(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

---

(setvelocity)=
## `setVelocity`

**Signature:**
```cpp
void setVelocity(const Point& velocity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `velocity` | - |

---

(setfading)=
## `setFading`

**Signature:**
```cpp
void setFading(FadeState state, float fadetime);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FadeState` | `state` | - |
| `float` | `fadetime` | - |

---

(update)=
## `update`

**Signature:**
```cpp
protected: virtual void update();
```

---

(getsources)=
## `getSources`

**Signature:**
```cpp
std::vector<SoundSourcePtr> getSources();
```

**Returns:**
- `std::vector&lt;SoundSourcePtr&gt;`

---
