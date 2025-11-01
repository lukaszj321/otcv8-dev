---
title: "src/framework/util/stats.h"
source_file: "src/framework/util/stats.h"
generated_at: "2025-11-01T05:32:59.312Z"
doc_type: "cpp_api"
---

# src/framework/util/stats.h

(add)=
## `add`

**Signature:**
```cpp
public: void add(int type, Stat* stats);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `type` | - |
| `Stat*` | `stats` | - |

---

(get)=
## `get`

**Signature:**
```cpp
std::string get(int type, int limit, bool pretty);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `type` | - |
| `int` | `limit` | - |
| `bool` | `pretty` | - |

**Returns:**
- `std::string`

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear(int type);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `type` | - |

---

(clearall)=
## `clearAll`

**Signature:**
```cpp
void clearAll();
```

---

(getslow)=
## `getSlow`

**Signature:**
```cpp
std::string getSlow(int type, int limit, unsigned int minTime, bool pretty);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `type` | - |
| `int` | `limit` | - |
| `unsigned int` | `minTime` | - |
| `bool` | `pretty` | - |

**Returns:**
- `std::string`

---

(clearslow)=
## `clearSlow`

**Signature:**
```cpp
void clearSlow(int type);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `type` | - |

---

(addwidget)=
## `addWidget`

**Signature:**
```cpp
void addWidget(UIWidget* widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidget*` | `widget` | - |

---

(removewidget)=
## `removeWidget`

**Signature:**
```cpp
void removeWidget(UIWidget* widget);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `UIWidget*` | `widget` | - |

---

(getwidgetsinfo)=
## `getWidgetsInfo`

**Signature:**
```cpp
std::string getWidgetsInfo(int limit, bool pretty);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `limit` | - |
| `bool` | `pretty` | - |

**Returns:**
- `std::string`

---

(types)=
## `types`

**Signature:**
```cpp
int types();
```

**Returns:**
- `int`

---

(getsleeptime)=
## `getSleepTime`

**Signature:**
```cpp
int64_t getSleepTime();
```

**Returns:**
- `int64_t`

---

(resetsleeptime)=
## `resetSleepTime`

**Signature:**
```cpp
void resetSleepTime();
```

---

(addtexture)=
## `addTexture`

**Signature:**
```cpp
inline void addTexture();
```

---

(removetexture)=
## `removeTexture`

**Signature:**
```cpp
inline void removeTexture();
```

---

(addthing)=
## `addThing`

**Signature:**
```cpp
inline void addThing();
```

---

(removething)=
## `removeThing`

**Signature:**
```cpp
inline void removeThing();
```

---

(addcreature)=
## `addCreature`

**Signature:**
```cpp
inline void addCreature();
```

---

(removecreature)=
## `removeCreature`

**Signature:**
```cpp
inline void removeCreature();
```

---
