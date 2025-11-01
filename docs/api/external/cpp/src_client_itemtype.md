---
title: "src/client/itemtype.h"
source_file: "src/client/itemtype.h"
generated_at: "2025-11-01T06:09:06.163Z"
doc_type: "cpp_api"
---

# src/client/itemtype.h

(itemtype)=
## `ItemType`

**Signature:**
```cpp
public: ItemType();
```

---

(unserialize)=
## `unserialize`

**Signature:**
```cpp
void unserialize(const BinaryTreePtr& node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const BinaryTreePtr&` | `node` | - |

---

(setserverid)=
## `setServerId`

**Signature:**
```cpp
void setServerId(uint16 serverId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `serverId` | - |

---

(getserverid)=
## `getServerId`

**Signature:**
```cpp
uint16 getServerId();
```

**Returns:**
- `uint16`

---

(setclientid)=
## `setClientId`

**Signature:**
```cpp
void setClientId(uint16 clientId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `clientId` | - |

---

(getclientid)=
## `getClientId`

**Signature:**
```cpp
uint16 getClientId();
```

**Returns:**
- `uint16`

---

(setcategory)=
## `setCategory`

**Signature:**
```cpp
void setCategory(ItemCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ItemCategory` | `category` | - |

---

(getcategory)=
## `getCategory`

**Signature:**
```cpp
ItemCategory getCategory();
```

**Returns:**
- `ItemCategory`

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

(setdesc)=
## `setDesc`

**Signature:**
```cpp
void setDesc(const std::string& desc);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `desc` | - |

---

(getdesc)=
## `getDesc`

**Signature:**
```cpp
std::string getDesc();
```

**Returns:**
- `std::string`

---

(isnull)=
## `isNull`

**Signature:**
```cpp
bool isNull();
```

**Returns:**
- `bool`

---

(iswritable)=
## `isWritable`

**Signature:**
```cpp
bool isWritable();
```

**Returns:**
- `bool`

---
