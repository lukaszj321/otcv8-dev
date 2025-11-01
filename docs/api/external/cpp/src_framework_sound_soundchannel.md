---
title: "src/framework/sound/soundchannel.h"
source_file: "src/framework/sound/soundchannel.h"
generated_at: "2025-11-01T00:11:49.059Z"
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

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `filename` |  | - |
| `float` | `fadetime` | `0` | - |
| `float` | `gain` | `1.0f` | - |

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

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `float` | `fadetime` | `0` | - |

---

(enqueue)=
## `enqueue`

**Signature:**
```cpp
void enqueue(const std::string& filename, float fadetime = 0, float gain = 1.0f);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::string&` | `filename` |  | - |
| `float` | `fadetime` | `0` | - |
| `float` | `gain` | `1.0f` | - |

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
