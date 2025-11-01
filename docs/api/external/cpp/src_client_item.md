---
title: "src/client/item.h"
source_file: "src/client/item.h"
generated_at: "2025-11-01T00:11:49.018Z"
doc_type: "cpp_api"
---

# src/client/item.h

(item)=
## `Item`

**Signature:**
```cpp
public: Item();
```

---

(create)=
## `create`

**Signature:**
```cpp
static ItemPtr create(int id, int countOrSubtype = 1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `id` |  | - |
| `int` | `countOrSubtype` | `1` | - |

**Returns:**
- `ItemPtr`

---

(createfromotb)=
## `createFromOtb`

**Signature:**
```cpp
static ItemPtr createFromOtb(int id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `id` | - |

**Returns:**
- `ItemPtr`

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Point&` | `dest` |  | - |
| `bool` | `animate` | `true` | - |
| `LightView*` | `lightView` | `nullptr` | - |

---

(draw-1)=
## `draw`

**Signature:**
```cpp
void draw(const Rect& dest, bool animate = true);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Rect&` | `dest` |  | - |
| `bool` | `animate` | `true` | - |

---

(setid)=
## `setId`

**Signature:**
```cpp
void setId(uint32 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |

---

(setotbid)=
## `setOtbId`

**Signature:**
```cpp
void setOtbId(uint16 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |

---

(getsubtype)=
## `getSubType`

**Signature:**
```cpp
int getSubType();
```

**Returns:**
- `int`

---

(getcount)=
## `getCount`

**Signature:**
```cpp
int getCount();
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

(isvalid)=
## `isValid`

**Signature:**
```cpp
bool isValid();
```

**Returns:**
- `bool`

---

(unserializeitem)=
## `unserializeItem`

**Signature:**
```cpp
void unserializeItem(const BinaryTreePtr& in);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const BinaryTreePtr&` | `in` | - |

---

(serializeitem)=
## `serializeItem`

**Signature:**
```cpp
void serializeItem(const OutputBinaryTreePtr& out);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const OutputBinaryTreePtr&` | `out` | - |

---

(ismoveable)=
## `isMoveable`

**Signature:**
```cpp
bool isMoveable();
```

**Returns:**
- `bool`

---

(isground)=
## `isGround`

**Signature:**
```cpp
bool isGround();
```

**Returns:**
- `bool`

---

(clone)=
## `clone`

**Signature:**
```cpp
ItemPtr clone();
```

**Returns:**
- `ItemPtr`

---

(calculatepatterns)=
## `calculatePatterns`

**Signature:**
```cpp
void calculatePatterns(int& xPattern, int& yPattern, int& zPattern);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int&` | `xPattern` | - |
| `int&` | `yPattern` | - |
| `int&` | `zPattern` | - |

---

(calculateanimationphase)=
## `calculateAnimationPhase`

**Signature:**
```cpp
int calculateAnimationPhase(bool animate);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `animate` | - |

**Returns:**
- `int`

---

(getexactsize)=
## `getExactSize`

**Signature:**
```cpp
int getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `layer` | `0` | - |
| `int` | `xPattern` | `0` | - |
| `int` | `yPattern` | `0` | - |
| `int` | `zPattern` | `0` | - |
| `int` | `animationPhase` | `0` | - |

**Returns:**
- `int`

---

(getthingtype)=
## `getThingType`

**Signature:**
```cpp
const ThingTypePtr& getThingType();
```

**Returns:**
- `const ThingTypePtr&`

---

(setcountorsubtype)=
## `setCountOrSubType`

**Signature:**
```cpp
void setCountOrSubType(int value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `value` | - |

---

(setcount)=
## `setCount`

**Signature:**
```cpp
void setCount(int count);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `count` | - |

---

(setsubtype)=
## `setSubType`

**Signature:**
```cpp
void setSubType(int subType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `subType` | - |

---

(setcolor)=
## `setColor`

**Signature:**
```cpp
void setColor(const Color& c);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `c` | - |

---

(settooltip)=
## `setTooltip`

**Signature:**
```cpp
void setTooltip(const std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |

---

(setquicklootflags)=
## `setQuickLootFlags`

**Signature:**
```cpp
void setQuickLootFlags(uint32 flags);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `flags` | - |

---

(setshader)=
## `setShader`

**Signature:**
```cpp
void setShader(const std::string& str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `str` | - |

---

(getcountorsubtype)=
## `getCountOrSubType`

**Signature:**
```cpp
int getCountOrSubType();
```

**Returns:**
- `int`

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

(getclientid)=
## `getClientId`

**Signature:**
```cpp
uint16 getClientId();
```

**Returns:**
- `uint16`

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

(gettooltip)=
## `getTooltip`

**Signature:**
```cpp
std::string getTooltip();
```

**Returns:**
- `std::string`

---

(getquicklootflags)=
## `getQuickLootFlags`

**Signature:**
```cpp
uint32 getQuickLootFlags();
```

**Returns:**
- `uint32`

---

(getshader)=
## `getShader`

**Signature:**
```cpp
std::string getShader();
```

**Returns:**
- `std::string`

---

(setdepotid)=
## `setDepotId`

**Signature:**
```cpp
void setDepotId(uint16 depotId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `depotId` | - |

---

(getdepotid)=
## `getDepotId`

**Signature:**
```cpp
uint16 getDepotId();
```

**Returns:**
- `uint16`

---

(setdoorid)=
## `setDoorId`

**Signature:**
```cpp
void setDoorId(uint8 doorId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint8` | `doorId` | - |

---

(getdoorid)=
## `getDoorId`

**Signature:**
```cpp
uint8 getDoorId();
```

**Returns:**
- `uint8`

---

(getuniqueid)=
## `getUniqueId`

**Signature:**
```cpp
uint16 getUniqueId();
```

**Returns:**
- `uint16`

---

(getactionid)=
## `getActionId`

**Signature:**
```cpp
uint16 getActionId();
```

**Returns:**
- `uint16`

---

(setactionid)=
## `setActionId`

**Signature:**
```cpp
void setActionId(uint16 actionId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `actionId` | - |

---

(setuniqueid)=
## `setUniqueId`

**Signature:**
```cpp
void setUniqueId(uint16 uniqueId);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `uniqueId` | - |

---

(gettext)=
## `getText`

**Signature:**
```cpp
std::string getText();
```

**Returns:**
- `std::string`

---

(getdescription)=
## `getDescription`

**Signature:**
```cpp
std::string getDescription();
```

**Returns:**
- `std::string`

---

(setdescription)=
## `setDescription`

**Signature:**
```cpp
void setDescription(std::string desc);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `desc` | - |

---

(settext)=
## `setText`

**Signature:**
```cpp
void setText(std::string txt);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `txt` | - |

---

(getteleportdestination)=
## `getTeleportDestination`

**Signature:**
```cpp
Position getTeleportDestination();
```

**Returns:**
- `Position`

---

(setteleportdestination)=
## `setTeleportDestination`

**Signature:**
```cpp
void setTeleportDestination(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(setasync)=
## `setAsync`

**Signature:**
```cpp
void setAsync(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(ishousedoor)=
## `isHouseDoor`

**Signature:**
```cpp
bool isHouseDoor();
```

**Returns:**
- `bool`

---

(isdepot)=
## `isDepot`

**Signature:**
```cpp
bool isDepot();
```

**Returns:**
- `bool`

---

(iscontainer)=
## `isContainer`

**Signature:**
```cpp
bool isContainer();
```

**Returns:**
- `bool`

---

(isdoor)=
## `isDoor`

**Signature:**
```cpp
bool isDoor();
```

**Returns:**
- `bool`

---

(isteleport)=
## `isTeleport`

**Signature:**
```cpp
bool isTeleport();
```

**Returns:**
- `bool`

---

(asitem)=
## `asItem`

**Signature:**
```cpp
ItemPtr asItem();
```

**Returns:**
- `ItemPtr`

---

(isitem)=
## `isItem`

**Signature:**
```cpp
bool isItem();
```

**Returns:**
- `bool`

---

(getcontaineritems)=
## `getContainerItems`

**Signature:**
```cpp
ItemVector getContainerItems();
```

**Returns:**
- `ItemVector`

---

(getcontaineritem)=
## `getContainerItem`

**Signature:**
```cpp
ItemPtr getContainerItem(int slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |

**Returns:**
- `ItemPtr`

---

(addcontaineritemindexed)=
## `addContainerItemIndexed`

**Signature:**
```cpp
void addContainerItemIndexed(const ItemPtr& i, int slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `i` | - |
| `int` | `slot` | - |

---

(addcontaineritem)=
## `addContainerItem`

**Signature:**
```cpp
void addContainerItem(const ItemPtr& i);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemPtr&` | `i` | - |

---

(removecontaineritem)=
## `removeContainerItem`

**Signature:**
```cpp
void removeContainerItem(int slot);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `slot` | - |

---

(clearcontaineritems)=
## `clearContainerItems`

**Signature:**
```cpp
void clearContainerItems();
```

---

(setcustomattribute)=
## `setCustomAttribute`

**Signature:**
```cpp
void setCustomAttribute(uint16 key, uint64 value);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `key` | - |
| `uint64` | `value` | - |

---

(getcustomattribute)=
## `getCustomAttribute`

**Signature:**
```cpp
uint64 getCustomAttribute(uint16 key);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `key` | - |

**Returns:**
- `uint64`

---
