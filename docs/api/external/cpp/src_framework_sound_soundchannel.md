---
title: "src/framework/sound/soundchannel.h"
source_file: "src/framework/sound/soundchannel.h"
generated_at: "2025-10-31T23:33:30.356Z"
doc_type: "cpp_api"
---

# src/framework/sound/soundchannel.h

(play)=
## `play`

**Signature:**
```cpp
SoundSourcePtr play(const std::string& filename, float fadetime = 0, float gain = 1.0f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |
| `float fadetime = 0` | - | - |
| `float gain = 1.0` | `f` | - |

**Returns:**
- `SoundSourcePtr`

---

(stop)=
## `stop`

**Signature:**
```cpp
void stop(float fadetime = 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float fadetime = 0` | - | - |

---

(enqueue)=
## `enqueue`

**Signature:**
```cpp
void enqueue(const std::string& filename, float fadetime = 0, float gain = 1.0f);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |
| `float fadetime = 0` | - | - |
| `float gain = 1.0` | `f` | - |

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

(setenabled)=
## `setEnabled`

**Signature:**
```cpp
void setEnabled(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(update)=
## `update`

**Signature:**
```cpp
protected: void update();
```

**Returns:**
- `protected: void`

---

(soundchannel)=
## `SoundChannel`

**Signature:**
```cpp
public: SoundChannel(int id) : m_id(id), m_gain(1);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int id) : m_id(id)` | - | - |
| `m_gain(1` | - | - |

**Returns:**
- `public:`

---

(enable)=
## `enable`

**Signature:**
```cpp
void enable();
```

---

(disable)=
## `disable`

**Signature:**
```cpp
void disable();
```

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

(isenabled)=
## `isEnabled`

**Signature:**
```cpp
bool isEnabled();
```

**Returns:**
- `bool`

---

(getid)=
## `getId`

**Signature:**
```cpp
int getId();
```

**Returns:**
- `int`

---
