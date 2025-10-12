# src/client/creatures.h

```cpp
public:
    Spawn() = default; Spawn(int32 radius) { setRadius(radius);
```
```cpp
void setRadius(int32 r) { m_attribs.set(SpawnAttrRadius, r);
```
```cpp
int32 getRadius() { return m_attribs.get<int32>(SpawnAttrRadius);
```
```cpp
void setCenterPos(const Position& pos) { m_attribs.set(SpawnAttrCenter, pos);
```
```cpp
Position getCenterPos() { return m_attribs.get<Position>(SpawnAttrCenter);
```
```cpp
std::vector<CreatureTypePtr> getCreatures();
```
```cpp
void addCreature(const Position& placePos, const CreatureTypePtr& cType);
```
```cpp
void removeCreature(const Position& pos);
```
```cpp
void clear() { m_creatures.clear();
```
```cpp
protected:
    void load(TiXmlElement* node);
```
```cpp
void save(TiXmlElement* node);
```
```cpp
public:
    CreatureType() = default; CreatureType(const std::string& name) { setName(name);
```
```cpp
void setSpawnTime(int32 spawnTime) { m_attribs.set(CreatureAttrSpawnTime, spawnTime);
```
```cpp
int32 getSpawnTime() { return m_attribs.get<int32>(CreatureAttrSpawnTime);
```
```cpp
void setName(const std::string& name) { m_attribs.set(CreatureAttrName, name);
```
```cpp
std::string getName() { return m_attribs.get<std::string>(CreatureAttrName);
```
```cpp
void setOutfit(const Outfit& o) { m_attribs.set(CreatureAttrOutfit, o);
```
```cpp
Outfit getOutfit() { return m_attribs.get<Outfit>(CreatureAttrOutfit);
```
```cpp
void setDirection(Otc::Direction dir) { m_attribs.set(CreatureAttrDir, dir);
```
```cpp
Otc::Direction getDirection() { return m_attribs.get<Otc::Direction>(CreatureAttrDir);
```
```cpp
void setRace(CreatureRace race) { m_attribs.set(CreatureAttrRace, race);
```
```cpp
CreatureRace getRace() { return m_attribs.get<CreatureRace>(CreatureAttrRace);
```
```cpp
CreaturePtr cast();
```
```cpp
public:
    CreatureManager();
```
```cpp
void clear() { m_creatures.clear();
```
```cpp
void clearSpawns();
```
```cpp
void terminate();
```
```cpp
void loadMonsters(const std::string& file);
```
```cpp
void loadSingleCreature(const std::string& file);
```
```cpp
void loadNpcs(const std::string& folder);
```
```cpp
void loadCreatureBuffer(const std::string& buffer);
```
```cpp
void loadSpawns(const std::string& fileName);
```
```cpp
void saveSpawns(const std::string& fileName);
```
```cpp
const CreatureTypePtr& getCreatureByName(std::string name);
```
```cpp
const CreatureTypePtr& getCreatureByLook(int look);
```
```cpp
std::vector<SpawnPtr> getSpawns();
```
```cpp
SpawnPtr getSpawn(const Position& centerPos);
```
```cpp
SpawnPtr getSpawnForPlacePos(const Position& pos);
```
```cpp
SpawnPtr addSpawn(const Position& centerPos, int radius);
```
```cpp
void deleteSpawn(const SpawnPtr& spawn);
```
```cpp
bool isLoaded() { return m_loaded; } bool isSpawnLoaded() { return m_spawnLoaded; } const std::vector<CreatureTypePtr>& getCreatures() { return m_creatures; } protected: void internalLoadCreatureBuffer(TiXmlElement* elem, const CreatureTypePtr& m);
```