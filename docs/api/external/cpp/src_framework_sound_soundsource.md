---
title: "src/framework/sound/soundsource.h"
source_file: "src/framework/sound/soundsource.h"
generated_at: "2025-11-01T08:45:15.319Z"
doc_type: "cpp_api"
---

# src/framework/sound/soundsource.h

(play)=
## `play`

**Signature:**
```cpp
virtual void play();
```

---

(stop)=
## `stop`

**Signature:**
```cpp
virtual void stop();
```

---

(isbuffering)=
## `isBuffering`

**Signature:**
```cpp
virtual bool isBuffering();
```

**Returns:**
- `bool`

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

---

(update)=
## `update`

**Signature:**
```cpp
virtual void update();
```

---

(isplaying)=
## `isPlaying`

**Signature:**
```cpp
virtual bool isPlaying();
```

**Returns:**
- `bool`

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

