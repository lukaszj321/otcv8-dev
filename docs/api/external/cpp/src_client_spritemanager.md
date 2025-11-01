---
title: "src/client/spritemanager.h"
source_file: "src/client/spritemanager.h"
generated_at: "2025-11-01T08:45:15.287Z"
doc_type: "cpp_api"
---

# src/client/spritemanager.h

(spritemanager)=
## `SpriteManager`

**Signature:**
```cpp
public: SpriteManager();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(loadspr)=
## `loadSpr`

**Signature:**
```cpp
bool loadSpr(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(unload)=
## `unload`

**Signature:**
```cpp
void unload();
```

---

(savespr)=
## `saveSpr`

**Signature:**
```cpp
void saveSpr(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(savespr64)=
## `saveSpr64`

**Signature:**
```cpp
void saveSpr64(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(encryptsprites)=
## `encryptSprites`

**Signature:**
```cpp
void encryptSprites(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(dumpsprites)=
## `dumpSprites`

**Signature:**
```cpp
void dumpSprites(std::string dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `dir` | - |

---

(getspriteimage)=
## `getSpriteImage`

**Signature:**
```cpp
ImagePtr getSpriteImage(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `ImagePtr`

---

(loadcasualspr)=
## `loadCasualSpr`

**Signature:**
```cpp
private: bool loadCasualSpr(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(loadcwmspr)=
## `loadCwmSpr`

**Signature:**
```cpp
bool loadCwmSpr(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(getspriteimagecasual)=
## `getSpriteImageCasual`

**Signature:**
```cpp
ImagePtr getSpriteImageCasual(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `ImagePtr`

---

(getspriteimagehd)=
## `getSpriteImageHd`

**Signature:**
```cpp
ImagePtr getSpriteImageHd(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `ImagePtr`

---

(getsignature)=
## `getSignature`

**Signature:**
```cpp
uint32 getSignature();
```

**Returns:**
- `uint32`

---

(getspritescount)=
## `getSpritesCount`

**Signature:**
```cpp
int getSpritesCount();
```

**Returns:**
- `int`

---

(isloaded)=
## `isLoaded`

**Signature:**
```cpp
bool isLoaded();
```

**Returns:**
- `bool`

---

(spritesize)=
## `spriteSize`

**Signature:**
```cpp
int spriteSize();
```

**Returns:**
- `int`

---

(getoffsetfactor)=
## `getOffsetFactor`

**Signature:**
```cpp
float getOffsetFactor();
```

**Returns:**
- `float`

---

(ishdmod)=
## `isHdMod`

**Signature:**
```cpp
bool isHdMod();
```

**Returns:**
- `bool`

