---
title: "src/client/creatures.h"
source_file: "src/client/creatures.h"
generated_at: "2025-10-31T23:33:30.318Z"
doc_type: "cpp_api"
---

# src/client/creatures.h

(getcreatures)=
## `getCreatures`

**Signature:**
```cpp
std::vector<CreatureTypePtr> getCreatures();
```

**Returns:**
- `std::vector&lt;CreatureTypePtr&gt;`

---

(addcreature)=
## `addCreature`

**Signature:**
```cpp
void addCreature(const Position& placePos, const CreatureTypePtr& cType);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `placePos` | - |
| `const CreatureTypePtr&` | `cType` | - |

---

(removecreature)=
## `removeCreature`

**Signature:**
```cpp
void removeCreature(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(load)=
## `load`

**Signature:**
```cpp
protected: void load(TiXmlElement* node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlElement*` | `node` | - |

**Returns:**
- `protected: void`

---

(save)=
## `save`

**Signature:**
```cpp
void save(TiXmlElement* node);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlElement*` | `node` | - |

---

(cast)=
## `cast`

**Signature:**
```cpp
CreaturePtr cast();
```

**Returns:**
- `CreaturePtr`

---

(creaturemanager)=
## `CreatureManager`

**Signature:**
```cpp
public: CreatureManager();
```

**Returns:**
- `public:`

---

(clearspawns)=
## `clearSpawns`

**Signature:**
```cpp
void clearSpawns();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(loadmonsters)=
## `loadMonsters`

**Signature:**
```cpp
void loadMonsters(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(loadsinglecreature)=
## `loadSingleCreature`

**Signature:**
```cpp
void loadSingleCreature(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(loadnpcs)=
## `loadNpcs`

**Signature:**
```cpp
void loadNpcs(const std::string& folder);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `folder` | - |

---

(loadcreaturebuffer)=
## `loadCreatureBuffer`

**Signature:**
```cpp
void loadCreatureBuffer(const std::string& buffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `buffer` | - |

---

(loadspawns)=
## `loadSpawns`

**Signature:**
```cpp
void loadSpawns(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(savespawns)=
## `saveSpawns`

**Signature:**
```cpp
void saveSpawns(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(getcreaturebyname)=
## `getCreatureByName`

**Signature:**
```cpp
const CreatureTypePtr& getCreatureByName(std::string name);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::string` | `name` | - |

**Returns:**
- `const CreatureTypePtr&`

---

(getcreaturebylook)=
## `getCreatureByLook`

**Signature:**
```cpp
const CreatureTypePtr& getCreatureByLook(int look);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `look` | - |

**Returns:**
- `const CreatureTypePtr&`

---

(getspawns)=
## `getSpawns`

**Signature:**
```cpp
std::vector<SpawnPtr> getSpawns();
```

**Returns:**
- `std::vector&lt;SpawnPtr&gt;`

---

(getspawn)=
## `getSpawn`

**Signature:**
```cpp
SpawnPtr getSpawn(const Position& centerPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centerPos` | - |

**Returns:**
- `SpawnPtr`

---

(getspawnforplacepos)=
## `getSpawnForPlacePos`

**Signature:**
```cpp
SpawnPtr getSpawnForPlacePos(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `SpawnPtr`

---

(addspawn)=
## `addSpawn`

**Signature:**
```cpp
SpawnPtr addSpawn(const Position& centerPos, int radius);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centerPos` | - |
| `int` | `radius` | - |

**Returns:**
- `SpawnPtr`

---

(deletespawn)=
## `deleteSpawn`

**Signature:**
```cpp
void deleteSpawn(const SpawnPtr& spawn);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const SpawnPtr&` | `spawn` | - |

---

(internalloadcreaturebuffer)=
## `internalLoadCreatureBuffer`

**Signature:**
```cpp
protected: void internalLoadCreatureBuffer(TiXmlElement* elem, const CreatureTypePtr& m);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `TiXmlElement*` | `elem` | - |
| `const CreatureTypePtr&` | `m` | - |

**Returns:**
- `protected: void`

---

(setradius)=
## `setRadius`

**Signature:**
```cpp
void setRadius(int32 r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int32` | `r` | - |

---

(getradius)=
## `getRadius`

**Signature:**
```cpp
int32 getRadius();
```

**Returns:**
- `int32`

---

(setcenterpos)=
## `setCenterPos`

**Signature:**
```cpp
void setCenterPos(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(getcenterpos)=
## `getCenterPos`

**Signature:**
```cpp
Position getCenterPos();
```

**Returns:**
- `Position`

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(setspawntime)=
## `setSpawnTime`

**Signature:**
```cpp
void setSpawnTime(int32 spawnTime);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int32` | `spawnTime` | - |

---

(getspawntime)=
## `getSpawnTime`

**Signature:**
```cpp
int32 getSpawnTime();
```

**Returns:**
- `int32`

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

(setoutfit)=
## `setOutfit`

**Signature:**
```cpp
void setOutfit(const Outfit& o);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Outfit&` | `o` | - |

---

(getoutfit)=
## `getOutfit`

**Signature:**
```cpp
Outfit getOutfit();
```

**Returns:**
- `Outfit`

---

(setdirection)=
## `setDirection`

**Signature:**
```cpp
void setDirection(Otc::Direction dir);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `dir` | - |

---

(getdirection)=
## `getDirection`

**Signature:**
```cpp
Otc::Direction getDirection();
```

**Returns:**
- `Otc::Direction`

---

(setrace)=
## `setRace`

**Signature:**
```cpp
void setRace(CreatureRace race);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `CreatureRace` | `race` | - |

---

(getrace)=
## `getRace`

**Signature:**
```cpp
CreatureRace getRace();
```

**Returns:**
- `CreatureRace`

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

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

(isspawnloaded)=
## `isSpawnLoaded`

**Signature:**
```cpp
bool isSpawnLoaded();
```

**Returns:**
- `bool`

---

(getcreatures)=
## `getCreatures`

**Signature:**
```cpp
const std::vector<CreatureTypePtr>& getCreatures();
```

**Returns:**
- `const std::vector&lt;CreatureTypePtr&gt;&`

---
