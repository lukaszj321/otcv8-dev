---
title: "src/client/towns.h"
source_file: "src/client/towns.h"
generated_at: "2025-11-01T05:32:59.269Z"
doc_type: "cpp_api"
---

# src/client/towns.h

(townmanager)=
## `TownManager`

**Signature:**
```cpp
public: TownManager();
```

---

(addtown)=
## `addTown`

**Signature:**
```cpp
void addTown(const TownPtr& town);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TownPtr&` | `town` | - |

---

(removetown)=
## `removeTown`

**Signature:**
```cpp
void removeTown(uint32 townId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `townId` | - |

---

(gettown)=
## `getTown`

**Signature:**
```cpp
const TownPtr& getTown(uint32 townId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `townId` | - |

**Returns:**
- `const TownPtr&`

---

(gettownbyname)=
## `getTownByName`

**Signature:**
```cpp
const TownPtr& getTownByName(std::string name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `name` | - |

**Returns:**
- `const TownPtr&`

---

(sort)=
## `sort`

**Signature:**
```cpp
void sort();
```

---

(findtown)=
## `findTown`

**Signature:**
```cpp
protected: TownList::iterator findTown(uint32 townId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `townId` | - |

**Returns:**
- `TownList::iterator`

---

(town)=
## `Town`

**Signature:**
```cpp
public: Town();
```

---

(setid)=
## `setId`

**Signature:**
```cpp
void setId(uint32 tid);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `tid` | - |

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

(setpos)=
## `setPos`

**Signature:**
```cpp
void setPos(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(getid)=
## `getId`

**Signature:**
```cpp
uint32 getId();
```

**Returns:**
- `uint32`

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

(getpos)=
## `getPos`

**Signature:**
```cpp
Position getPos();
```

**Returns:**
- `Position`

---

(gettowns)=
## `getTowns`

**Signature:**
```cpp
TownList getTowns();
```

**Returns:**
- `TownList`

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---
