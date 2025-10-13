# src/client/map.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void addMapView(const MapViewPtr& mapView);
```
```cpp
void removeMapView(const MapViewPtr& mapView);
```
```cpp
void notificateTileUpdate(const Position& pos, bool updateMinimap = false);
```
```cpp
void requestVisibleTilesCacheUpdate();
```
```cpp
bool loadOtcm(const std::string& fileName);
```
```cpp
void saveOtcm(const std::string& fileName);
```
```cpp
void loadOtbm(const std::string& fileName);
```
```cpp
void saveOtbm(const std::string& fileName);
```
```cpp
void clean();
```
```cpp
void cleanDynamicThings();
```
```cpp
void cleanTexts();
```
```cpp
void addThing(const ThingPtr& thing, const Position& pos, int stackPos = -1);
```
```cpp
void setTileSpeed(const Position & pos, uint16_t speed, uint8_t blocking);
```
```cpp
ThingPtr getThing(const Position& pos, int stackPos);
```
```cpp
bool removeThing(const ThingPtr& thing);
```
```cpp
bool removeThingByPos(const Position& pos, int stackPos);
```
```cpp
void colorizeThing(const ThingPtr& thing, const Color& color);
```
```cpp
void removeThingColor(const ThingPtr& thing);
```
```cpp
StaticTextPtr getStaticText(const Position& pos);
```
```cpp
const TilePtr& createTile(const Position& pos);
```
```cpp
const TilePtr& createTileEx(const Position& pos, const Items&... items);
```
```cpp
const TilePtr& getOrCreateTile(const Position& pos);
```
```cpp
const TilePtr& getTile(const Position& pos);
```
```cpp
const TileList getTiles(int floor = -1);
```
```cpp
void cleanTile(const Position& pos);
```
```cpp
void setShowZone(tileflags_t zone, bool show);
```
```cpp
void setShowZones(bool show);
```
```cpp
void setZoneColor(tileflags_t flag, const Color& color);
```
```cpp
Color getZoneColor(tileflags_t flag);
```
```cpp
void setForceShowAnimations(bool force);
```
```cpp
bool isForcingAnimations();
```
```cpp
bool isShowingAnimations();
```
```cpp
void setShowAnimations(bool show);
```
```cpp
void addCreature(const CreaturePtr& creature);
```
```cpp
CreaturePtr getCreatureById(uint32 id);
```
```cpp
void removeCreatureById(uint32 id);
```
```cpp
std::vector<CreaturePtr> getSightSpectators(const Position& centerPos, bool multiFloor);
```
```cpp
std::vector<CreaturePtr> getSpectators(const Position& centerPos, bool multiFloor);
```
```cpp
std::vector<CreaturePtr> getSpectatorsInRange(const Position& centerPos, bool multiFloor, int xRange, int yRange);
```
```cpp
std::vector<CreaturePtr> getSpectatorsInRangeEx(const Position& centerPos, bool multiFloor, int minXRange, int maxXRange, int minYRange, int maxYRange);
```
```cpp
std::vector<CreaturePtr> getSpectatorsByPattern(const Position& centerPos, const std::string& pattern, Otc::Direction direction);
```
```cpp
void setCentralPosition(const Position& centralPosition);
```
```cpp
bool isLookPossible(const Position& pos);
```
```cpp
bool isCovered(const Position& pos, int firstFloor = 0);
```
```cpp
bool isCompletelyCovered(const Position& pos, int firstFloor = 0);
```
```cpp
bool isAwareOfPosition(const Position& pos, bool extended = false);
```
```cpp
bool isAwareOfPositionForClean(const Position& pos, bool extended = false);
```
```cpp
void setAwareRange(const AwareRange& range);
```
```cpp
void resetAwareRange();
```
```cpp
int getFirstAwareFloor();
```
```cpp
int getLastAwareFloor();
```
```cpp
PathFindResult_ptr newFindPath(const Position& start, const Position& goal, std::shared_ptr<std::list<Node*>> visibleNodes);
```
```cpp
void findPathAsync(const Position & start, const Position & goal, std::function<void(PathFindResult_ptr)> callback);
```
```cpp
int getMinimapColor(const Position& pos);
```
```cpp
bool isPatchable(const Position& pos);
```
```cpp
bool isWalkable(const Position& pos, bool ignoreCreatures);
```
```cpp
bool isSightClear(const Position& fromPos, const Position& toPos);
```
```cpp
bool checkSightLine(const Position& fromPos, const Position& toPos);
```
```cpp
private: void removeUnawareThings();
```
```cpp
public: TileBlock();
```
```cpp
const TilePtr& create(const Position& pos);
```
```cpp
const TilePtr& getOrCreate(const Position& pos);
```
```cpp
const TilePtr& get(const Position& pos);
```
```cpp
void remove(const Position& pos);
```
```cpp
uint getTileIndex(const Position& pos);
```
```cpp
int horizontal();
```
```cpp
int vertical();
```
```cpp
void setHouseFile(const std::string& file);
```
```cpp
void setSpawnFile(const std::string& file);
```
```cpp
void setDescription(const std::string& desc);
```
```cpp
void clearDescriptions();
```
```cpp
void setWidth(uint16 w);
```
```cpp
void setHeight(uint16 h);
```
```cpp
std::string getHouseFile();
```
```cpp
std::string getSpawnFile();
```
```cpp
Size getSize();
```
```cpp
std::vector<std::string> getDescriptions();
```
```cpp
void setZoneOpacity(float opacity);
```
```cpp
float getZoneOpacity();
```
```cpp
tileflags_t getZoneFlags();
```
```cpp
bool showZones();
```
```cpp
bool showZone(tileflags_t zone);
```
```cpp
void setLight(const Light& light);
```
```cpp
AwareRange getAwareRange();
```
```cpp
Size getAwareRangeAsSize();
```
```cpp
Light getLight();
```
```cpp
Position getCentralPosition();
```
```cpp
const std::vector<MissilePtr>& getFloorMissiles(int z);
```
```cpp
std::vector<AnimatedTextPtr> getAnimatedTexts();
```
```cpp
std::vector<StaticTextPtr> getStaticTexts();
```
```cpp
uint getBlockIndex(const Position& pos);
```