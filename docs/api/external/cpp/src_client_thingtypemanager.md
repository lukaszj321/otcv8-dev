---
title: "src/client/thingtypemanager.h"
source_file: "src/client/thingtypemanager.h"
generated_at: "2025-10-31T23:33:30.329Z"
doc_type: "cpp_api"
---

# src/client/thingtypemanager.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

**Returns:**
- `public: void`

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(check)=
## `check`

**Signature:**
```cpp
void check();
```

---

(loaddat)=
## `loadDat`

**Signature:**
```cpp
bool loadDat(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(loadotml)=
## `loadOtml`

**Signature:**
```cpp
bool loadOtml(std::string file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `file` | - |

**Returns:**
- `bool`

---

(loadotb)=
## `loadOtb`

**Signature:**
```cpp
void loadOtb(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(loadxml)=
## `loadXml`

**Signature:**
```cpp
void loadXml(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(parseitemtype)=
## `parseItemType`

**Signature:**
```cpp
void parseItemType(uint16 id, TiXmlElement *elem);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |
| `TiXmlElement *` | `elem` | - |

---

(savedat)=
## `saveDat`

**Signature:**
```cpp
void saveDat(std::string fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `fileName` | - |

---

(dumptextures)=
## `dumpTextures`

**Signature:**
```cpp
void dumpTextures(std::string dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `dir` | - |

---

(replacetextures)=
## `replaceTextures`

**Signature:**
```cpp
void replaceTextures(std::string dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `dir` | - |

---

(additemtype)=
## `addItemType`

**Signature:**
```cpp
void addItemType(const ItemTypePtr& itemType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ItemTypePtr&` | `itemType` | - |

---

(finditemtypebyclientid)=
## `findItemTypeByClientId`

**Signature:**
```cpp
const ItemTypePtr& findItemTypeByClientId(uint16 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |

**Returns:**
- `const ItemTypePtr&`

---

(finditemtypebyname)=
## `findItemTypeByName`

**Signature:**
```cpp
const ItemTypePtr& findItemTypeByName(std::string name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `name` | - |

**Returns:**
- `const ItemTypePtr&`

---

(finditemtypesbyname)=
## `findItemTypesByName`

**Signature:**
```cpp
ItemTypeList findItemTypesByName(std::string name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `name` | - |

**Returns:**
- `ItemTypeList`

---

(finditemtypesbystring)=
## `findItemTypesByString`

**Signature:**
```cpp
ItemTypeList findItemTypesByString(std::string str);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `str` | - |

**Returns:**
- `ItemTypeList`

---

(getthingtype)=
## `getThingType`

**Signature:**
```cpp
const ThingTypePtr& getThingType(uint16 id, ThingCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |
| `ThingCategory` | `category` | - |

**Returns:**
- `const ThingTypePtr&`

---

(getitemtype)=
## `getItemType`

**Signature:**
```cpp
const ItemTypePtr& getItemType(uint16 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |

**Returns:**
- `const ItemTypePtr&`

---

(findthingtypebyattr)=
## `findThingTypeByAttr`

**Signature:**
```cpp
ThingTypeList findThingTypeByAttr(ThingAttr attr, ThingCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ThingAttr` | `attr` | - |
| `ThingCategory` | `category` | - |

**Returns:**
- `ThingTypeList`

---

(finditemtypebycategory)=
## `findItemTypeByCategory`

**Signature:**
```cpp
ItemTypeList findItemTypeByCategory(ItemCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ItemCategory` | `category` | - |

**Returns:**
- `ItemTypeList`

---

(getthingtypes)=
## `getThingTypes`

**Signature:**
```cpp
const ThingTypeList& getThingTypes(ThingCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `ThingCategory` | `category` | - |

**Returns:**
- `const ThingTypeList&`

---

(getmarketcategories)=
## `getMarketCategories`

**Signature:**
```cpp
std::set<int> getMarketCategories();
```

**Returns:**
- `std::set&lt;int&gt;`

---

(getnullthingtype)=
## `getNullThingType`

**Signature:**
```cpp
const ThingTypePtr& getNullThingType();
```

**Returns:**
- `const ThingTypePtr&`

---

(getnullitemtype)=
## `getNullItemType`

**Signature:**
```cpp
const ItemTypePtr& getNullItemType();
```

**Returns:**
- `const ItemTypePtr&`

---

(rawgetthingtype)=
## `rawGetThingType`

**Signature:**
```cpp
ThingType* rawGetThingType(uint16 id, ThingCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |
| `ThingCategory` | `category` | - |

**Returns:**
- `ThingType*`

---

(rawgetitemtype)=
## `rawGetItemType`

**Signature:**
```cpp
ItemType* rawGetItemType(uint16 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |

**Returns:**
- `ItemType*`

---

(getitemtypes)=
## `getItemTypes`

**Signature:**
```cpp
const ItemTypeList& getItemTypes();
```

**Returns:**
- `const ItemTypeList&`

---

(getdatsignature)=
## `getDatSignature`

**Signature:**
```cpp
uint32 getDatSignature();
```

**Returns:**
- `uint32`

---

(getotbmajorversion)=
## `getOtbMajorVersion`

**Signature:**
```cpp
uint32 getOtbMajorVersion();
```

**Returns:**
- `uint32`

---

(getotbminorversion)=
## `getOtbMinorVersion`

**Signature:**
```cpp
uint32 getOtbMinorVersion();
```

**Returns:**
- `uint32`

---

(getcontentrevision)=
## `getContentRevision`

**Signature:**
```cpp
uint16 getContentRevision();
```

**Returns:**
- `uint16`

---

(isdatloaded)=
## `isDatLoaded`

**Signature:**
```cpp
bool isDatLoaded();
```

**Returns:**
- `bool`

---

(isxmlloaded)=
## `isXmlLoaded`

**Signature:**
```cpp
bool isXmlLoaded();
```

**Returns:**
- `bool`

---

(isotbloaded)=
## `isOtbLoaded`

**Signature:**
```cpp
bool isOtbLoaded();
```

**Returns:**
- `bool`

---

(isvaliddatid)=
## `isValidDatId`

**Signature:**
```cpp
bool isValidDatId(uint16 id, ThingCategory category);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |
| `ThingCategory` | `category` | - |

**Returns:**
- `bool`

---

(isvalidotbid)=
## `isValidOtbId`

**Signature:**
```cpp
bool isValidOtbId(uint16 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `id` | - |

**Returns:**
- `bool`

---
