# src/client/creatures.h

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
protected: void load(TiXmlElement* node);
```
```cpp
void save(TiXmlElement* node);
```
```cpp
CreaturePtr cast();
```
```cpp
public: CreatureManager();
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
protected: void internalLoadCreatureBuffer(TiXmlElement* elem, const CreatureTypePtr& m);
```
```cpp
void setRadius(int32 r);
```
```cpp
int32 getRadius();
```
```cpp
void setCenterPos(const Position& pos);
```
```cpp
Position getCenterPos();
```
```cpp
void clear();
```
```cpp
void setSpawnTime(int32 spawnTime);
```
```cpp
int32 getSpawnTime();
```
```cpp
void setName(const std::string& name);
```
```cpp
std::string getName();
```
```cpp
void setOutfit(const Outfit& o);
```
```cpp
Outfit getOutfit();
```
```cpp
void setDirection(Otc::Direction dir);
```
```cpp
Otc::Direction getDirection();
```
```cpp
void setRace(CreatureRace race);
```
```cpp
CreatureRace getRace();
```
```cpp
void clear();
```
```cpp
bool isLoaded();
```
```cpp
bool isSpawnLoaded();
```
```cpp
const std::vector<CreatureTypePtr>& getCreatures();
```