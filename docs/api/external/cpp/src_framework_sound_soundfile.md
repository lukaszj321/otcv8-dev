---
title: "src/framework/sound/soundfile.h"
source_file: "src/framework/sound/soundfile.h"
generated_at: "2025-11-01T08:45:15.319Z"
doc_type: "cpp_api"
---

# src/framework/sound/soundfile.h

(soundfile)=
## `SoundFile`

**Signature:**
```cpp
public: SoundFile(const FileStreamPtr& fileStream);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FileStreamPtr&` | `fileStream` | - |

---

(loadsoundfile)=
## `loadSoundFile`

**Signature:**
```cpp
static SoundFilePtr loadSoundFile(const std::string& filename);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `filename` | - |

**Returns:**
- `SoundFilePtr`

---

(getsampleformat)=
## `getSampleFormat`

**Signature:**
```cpp
ALenum getSampleFormat();
```

**Returns:**
- `ALenum`

---

(read)=
## `read`

**Signature:**
```cpp
virtual int read(void *buffer, int bufferSize);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `void *buffer` | - | - |
| `int` | `bufferSize` | - |

**Returns:**
- `int`

---

(reset)=
## `reset`

**Signature:**
```cpp
virtual void reset();
```

---

(eof)=
## `eof`

**Signature:**
```cpp
bool eof();
```

**Returns:**
- `bool`

---

(getchannels)=
## `getChannels`

**Signature:**
```cpp
int getChannels();
```

**Returns:**
- `int`

---

(getrate)=
## `getRate`

**Signature:**
```cpp
int getRate();
```

**Returns:**
- `int`

---

(getbps)=
## `getBps`

**Signature:**
```cpp
int getBps();
```

**Returns:**
- `int`

---

(getsize)=
## `getSize`

**Signature:**
```cpp
int getSize();
```

**Returns:**
- `int`

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
