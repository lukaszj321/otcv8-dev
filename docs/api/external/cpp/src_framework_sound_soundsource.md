---
title: "src/framework/sound/soundsource.h"
source_file: "src/framework/sound/soundsource.h"
generated_at: "2025-10-31T23:33:30.357Z"
doc_type: "cpp_api"
---

# src/framework/sound/soundsource.h

(play)=
## `play`

**Signature:**
```cpp
virtual void play();
```

**Returns:**
- `virtual void`

---

(stop)=
## `stop`

**Signature:**
```cpp
virtual void stop();
```

**Returns:**
- `virtual void`

---

(isbuffering)=
## `isBuffering`

**Signature:**
```cpp
virtual bool isBuffering();
```

**Returns:**
- `virtual bool`

---

(setlooping)=
## `setLooping`

**Signature:**
```cpp
virtual void setLooping(bool looping);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `looping` | - |

**Returns:**
- `virtual void`

---

(setrelative)=
## `setRelative`

**Signature:**
```cpp
virtual void setRelative(bool relative);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `relative` | - |

**Returns:**
- `virtual void`

---

(setreferencedistance)=
## `setReferenceDistance`

**Signature:**
```cpp
virtual void setReferenceDistance(float distance);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `distance` | - |

**Returns:**
- `virtual void`

---

(setgain)=
## `setGain`

**Signature:**
```cpp
virtual void setGain(float gain);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `gain` | - |

**Returns:**
- `virtual void`

---

(setpitch)=
## `setPitch`

**Signature:**
```cpp
virtual void setPitch(float pitch);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `pitch` | - |

**Returns:**
- `virtual void`

---

(setposition)=
## `setPosition`

**Signature:**
```cpp
virtual void setPosition(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

**Returns:**
- `virtual void`

---

(setvelocity)=
## `setVelocity`

**Signature:**
```cpp
virtual void setVelocity(const Point& velocity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `velocity` | - |

**Returns:**
- `virtual void`

---

(setfading)=
## `setFading`

**Signature:**
```cpp
virtual void setFading(FadeState state, float fadetime);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `FadeState` | `state` | - |
| `float` | `fadetime` | - |

**Returns:**
- `virtual void`

---

(setbuffer)=
## `setBuffer`

**Signature:**
```cpp
protected: void setBuffer(const SoundBufferPtr& buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const SoundBufferPtr&` | `buffer` | - |

**Returns:**
- `protected: void`

---

(update)=
## `update`

**Signature:**
```cpp
virtual void update();
```

**Returns:**
- `virtual void`

---

(soundsource)=
## `SoundSource`

**Signature:**
```cpp
protected: SoundSource(uint sourceId) : m_sourceId(sourceId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint sourceId) : m_sourceId(` | `sourceId` | - |

**Returns:**
- `protected:`

---

(isplaying)=
## `isPlaying`

**Signature:**
```cpp
virtual bool isPlaying();
```

**Returns:**
- `virtual bool`

---

(setname)=
## `setName`

**Signature:**
```cpp
void setName(const std::string& name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `name` | - |

---

(getname)=
## `getName`

**Signature:**
```cpp
std::string getName();
```

**Returns:**
- `std::string`

---

(getchannel)=
## `getChannel`

**Signature:**
```cpp
uchar getChannel();
```

**Returns:**
- `uchar`

---

(getgain)=
## `getGain`

**Signature:**
```cpp
float getGain();
```

**Returns:**
- `float`

---

(setchannel)=
## `setChannel`

**Signature:**
```cpp
void setChannel(uchar channel);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uchar` | `channel` | - |

---
