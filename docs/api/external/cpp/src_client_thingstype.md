---
title: "src/client/thingstype.h"
source_file: "src/client/thingstype.h"
generated_at: "2025-11-01T08:19:49.426Z"
doc_type: "cpp_api"
---

# src/client/thingstype.h

(load)=
## `load`

**Signature:**
```cpp
bool load(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

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

(parsethingtype)=
## `parseThingType`

**Signature:**
```cpp
bool parseThingType(const FileStreamPtr& fin, ThingType& thingType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const FileStreamPtr&` | `fin` | - |
| `ThingType&` | `thingType` | - |

**Returns:**
- `bool`

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

(isloaded)=
## `isLoaded`

**Signature:**
```cpp
bool isLoaded();
```

**Returns:**
- `bool`

---

(getfirstitemid)=
## `getFirstItemId`

**Signature:**
```cpp
uint16 getFirstItemId();
```

**Returns:**
- `uint16`

---

(getmaxitemid)=
## `getMaxItemid`

**Signature:**
```cpp
uint16 getMaxItemid();
```

**Returns:**
- `uint16`

---

(isvaliditemid)=
## `isValidItemId`

**Signature:**
```cpp
bool isValidItemId(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `bool`

---
