# src/client/map.h

```cpp
public:
    TileBlock() { m_tiles.fill(nullptr);
```
```cpp
const TilePtr& create(const Position& pos) { TilePtr& tile = m_tiles[getTileIndex(pos)]; tile = TilePtr(new Tile(pos));
```
```cpp
const TilePtr& getOrCreate(const Position& pos) { TilePtr& tile = m_tiles[getTileIndex(pos)]; if(!tile) tile = TilePtr(new Tile(pos));
```
```cpp
const TilePtr& get(const Position& pos) { return m_tiles[getTileIndex(pos)]; } void remove(const Position& pos) { m_tiles[getTileIndex(pos)] = nullptr; } uint getTileIndex(const Position& pos) { return ((pos.y % BLOCK_SIZE) * BLOCK_SIZE) + (pos.x % BLOCK_SIZE);
```
```cpp
int horizontal() { return left + right + 1; } int vertical() { return top + bottom + 1; } }; struct PathFindResult { Otc::PathFindResult status = Otc::PathFindResultNoWay; std::vector<Otc::Direction> path; int complexity = 0; Position start; Position destination; }; using PathFindResult_ptr = std::shared_ptr<PathFindResult>; struct Node { float cost; float totalCost; Position pos; Node *prev; int distance; int unseen; }; //@bindsingleton g_map class Map { public: void init();
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
void setHouseFile(const std::string& file) { m_attribs.set(OTBM_ATTR_HOUSE_FILE, file);
```
```cpp
void setSpawnFile(const std::string& file) { m_attribs.set(OTBM_ATTR_SPAWN_FILE, file);
```
```cpp
void setDescription(const std::string& desc) { m_attribs.set(OTBM_ATTR_DESCRIPTION, desc);
```
```cpp
void clearDescriptions() { m_attribs.remove(OTBM_ATTR_DESCRIPTION);
```
```cpp
void setWidth(uint16 w) { m_attribs.set(OTBM_ATTR_WIDTH, w);
```
```cpp
void setHeight(uint16 h) { m_attribs.set(OTBM_ATTR_HEIGHT, h);
```
```cpp
std::string getHouseFile() { return m_attribs.get<std::string>(OTBM_ATTR_HOUSE_FILE);
```
```cpp
std::string getSpawnFile() { return m_attribs.get<std::string>(OTBM_ATTR_SPAWN_FILE);
```
```cpp
Size getSize() { return Size(m_attribs.get<uint16>(OTBM_ATTR_WIDTH), m_attribs.get<uint16>(OTBM_ATTR_HEIGHT));
```
```cpp
std::vector<std::string> getDescriptions() { return stdext::split(m_attribs.get<std::string>(OTBM_ATTR_DESCRIPTION), "\n");
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
void setZoneOpacity(float opacity) { m_zoneOpacity = opacity; } float getZoneOpacity() { return m_zoneOpacity; } Color getZoneColor(tileflags_t flag);
```
```cpp
tileflags_t getZoneFlags() { return (tileflags_t)m_zoneFlags; } bool showZones() { return m_zoneFlags != 0; } bool showZone(tileflags_t zone) { return (m_zoneFlags & zone) == zone; } void setForceShowAnimations(bool force);
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
void setLight(const Light& light) { m_light = light; } void setCentralPosition(const Position& centralPosition);
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
AwareRange getAwareRange() { return m_awareRange; } Size getAwareRangeAsSize() { return Size(m_awareRange.horizontal(), m_awareRange.vertical());
```
```cpp
Light getLight() { return m_light; } Position getCentralPosition() { return m_centralPosition; } int getFirstAwareFloor();
```
```cpp
int getLastAwareFloor();
```
```cpp
const std::vector<MissilePtr>& getFloorMissiles(int z) { return m_floorMissiles[z]; } std::vector<AnimatedTextPtr> getAnimatedTexts() { return m_animatedTexts; } std::vector<StaticTextPtr> getStaticTexts() { return m_staticTexts; } std::tuple<std::vector<Otc::Direction>, Otc::PathFindResult> findPath(const Position& start, const Position& goal, int maxComplexity, int flags = 0);
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
private:
    void removeUnawareThings();
```
```cpp
uint getBlockIndex(const Position& pos) { return ((pos.y / BLOCK_SIZE) * (65536 / BLOCK_SIZE)) + (pos.x / BLOCK_SIZE);
```