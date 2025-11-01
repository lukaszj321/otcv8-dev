---
title: "src/client/houses.h"
source_file: "src/client/houses.h"
generated_at: "2025-11-01T00:11:49.018Z"
doc_type: "cpp_api"
---

# src/client/houses.h

(house)=
## `House`

**Signature:**
```cpp
public: House();
```

---

(settile)=
## `setTile`

**Signature:**
```cpp
void setTile(const TilePtr& tile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TilePtr&` | `tile` | - |

---

(gettile)=
## `getTile`

**Signature:**
```cpp
TilePtr getTile(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `TilePtr`

---

(adddoor)=
## `addDoor`

**Signature:**
```cpp
void addDoor(const ItemPtr& door);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `door` | - |

---

(removedoorbyid)=
## `removeDoorById`

**Signature:**
```cpp
void removeDoorById(uint32 doorId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `doorId` | - |

---

(load)=
## `load`

**Signature:**
```cpp
protected: void load(const TiXmlElement* elem);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TiXmlElement*` | `elem` | - |

---

(save)=
## `save`

**Signature:**
```cpp
void save(TiXmlElement* elem);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlElement*` | `elem` | - |

---

(housemanager)=
## `HouseManager`

**Signature:**
```cpp
public: HouseManager();
```

---

(addhouse)=
## `addHouse`

**Signature:**
```cpp
void addHouse(const HousePtr& house);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const HousePtr&` | `house` | - |

---

(removehouse)=
## `removeHouse`

**Signature:**
```cpp
void removeHouse(uint32 houseId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `houseId` | - |

---

(gethouse)=
## `getHouse`

**Signature:**
```cpp
HousePtr getHouse(uint32 houseId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `houseId` | - |

**Returns:**
- `HousePtr`

---

(gethousebyname)=
## `getHouseByName`

**Signature:**
```cpp
HousePtr getHouseByName(std::string name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `name` | - |

**Returns:**
- `HousePtr`

---

(load-1)=
## `load`

**Signature:**
```cpp
void load(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(save-1)=
## `save`

**Signature:**
```cpp
void save(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(sort)=
## `sort`

**Signature:**
```cpp
void sort();
```

---

(filterhouses)=
## `filterHouses`

**Signature:**
```cpp
HouseList filterHouses(uint32 townId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `townId` | - |

**Returns:**
- `HouseList`

---

(findhouse)=
## `findHouse`

**Signature:**
```cpp
protected: HouseList::iterator findHouse(uint32 houseId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `houseId` | - |

**Returns:**
- `HouseList::iterator`

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

(setid)=
## `setId`

**Signature:**
```cpp
void setId(uint32 hId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `hId` | - |

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

(settownid)=
## `setTownId`

**Signature:**
```cpp
void setTownId(uint32 tid);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `tid` | - |

---

(gettownid)=
## `getTownId`

**Signature:**
```cpp
uint32 getTownId();
```

**Returns:**
- `uint32`

---

(setsize)=
## `setSize`

**Signature:**
```cpp
void setSize(uint32 s);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `s` | - |

---

(getsize)=
## `getSize`

**Signature:**
```cpp
uint32 getSize();
```

**Returns:**
- `uint32`

---

(setrent)=
## `setRent`

**Signature:**
```cpp
void setRent(uint32 r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `r` | - |

---

(getrent)=
## `getRent`

**Signature:**
```cpp
uint32 getRent();
```

**Returns:**
- `uint32`

---

(setentry)=
## `setEntry`

**Signature:**
```cpp
void setEntry(const Position& p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `p` | - |

---

(getentry)=
## `getEntry`

**Signature:**
```cpp
Position getEntry();
```

**Returns:**
- `Position`

---

(removedoor)=
## `removeDoor`

**Signature:**
```cpp
void removeDoor(const ItemPtr& door);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `door` | - |

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(gethouselist)=
## `getHouseList`

**Signature:**
```cpp
HouseList getHouseList();
```

**Returns:**
- `HouseList`

---
