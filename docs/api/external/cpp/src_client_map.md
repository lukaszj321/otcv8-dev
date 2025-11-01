---
title: "src/client/map.h"
source_file: "src/client/map.h"
generated_at: "2025-11-01T08:45:15.281Z"
doc_type: "cpp_api"
---

# src/client/map.h

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(addmapview)=
## `addMapView`

**Signature:**
```cpp
void addMapView(const MapViewPtr& mapView);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const MapViewPtr&` | `mapView` | - |

---

(removemapview)=
## `removeMapView`

**Signature:**
```cpp
void removeMapView(const MapViewPtr& mapView);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const MapViewPtr&` | `mapView` | - |

---

(notificatetileupdate)=
## `notificateTileUpdate`

**Signature:**
```cpp
void notificateTileUpdate(const Position& pos, bool updateMinimap = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Position&` | `pos` |  | - |
| `bool` | `updateMinimap` | `false` | - |

---

(requestvisibletilescacheupdate)=
## `requestVisibleTilesCacheUpdate`

**Signature:**
```cpp
void requestVisibleTilesCacheUpdate();
```

---

(loadotcm)=
## `loadOtcm`

**Signature:**
```cpp
bool loadOtcm(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `bool`

---

(saveotcm)=
## `saveOtcm`

**Signature:**
```cpp
void saveOtcm(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(loadotbm)=
## `loadOtbm`

**Signature:**
```cpp
void loadOtbm(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(saveotbm)=
## `saveOtbm`

**Signature:**
```cpp
void saveOtbm(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(clean)=
## `clean`

**Signature:**
```cpp
void clean();
```

---

(cleandynamicthings)=
## `cleanDynamicThings`

**Signature:**
```cpp
void cleanDynamicThings();
```

---

(cleantexts)=
## `cleanTexts`

**Signature:**
```cpp
void cleanTexts();
```

---

(addthing)=
## `addThing`

**Signature:**
```cpp
void addThing(const ThingPtr& thing, const Position& pos, int stackPos = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const ThingPtr&` | `thing` |  | - |
| `const Position&` | `pos` |  | - |
| `int` | `stackPos` | `-1` | - |

---

(settilespeed)=
## `setTileSpeed`

**Signature:**
```cpp
void setTileSpeed(const Position & pos, uint16_t speed, uint8_t blocking);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position &` | `pos` | - |
| `uint16_t` | `speed` | - |
| `uint8_t` | `blocking` | - |

---

(getthing)=
## `getThing`

**Signature:**
```cpp
ThingPtr getThing(const Position& pos, int stackPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `stackPos` | - |

**Returns:**
- `ThingPtr`

---

(removething)=
## `removeThing`

**Signature:**
```cpp
bool removeThing(const ThingPtr& thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |

**Returns:**
- `bool`

---

(removethingbypos)=
## `removeThingByPos`

**Signature:**
```cpp
bool removeThingByPos(const Position& pos, int stackPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `stackPos` | - |

**Returns:**
- `bool`

---

(colorizething)=
## `colorizeThing`

**Signature:**
```cpp
void colorizeThing(const ThingPtr& thing, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |
| `const Color&` | `color` | - |

---

(removethingcolor)=
## `removeThingColor`

**Signature:**
```cpp
void removeThingColor(const ThingPtr& thing);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const ThingPtr&` | `thing` | - |

---

(getstatictext)=
## `getStaticText`

**Signature:**
```cpp
StaticTextPtr getStaticText(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `StaticTextPtr`

---

(createtile)=
## `createTile`

**Signature:**
```cpp
const TilePtr& createTile(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `const TilePtr&`

---

(createtileex)=
## `createTileEx`

**Signature:**
```cpp
const TilePtr& createTileEx(const Position& pos, const Items&... items);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `const Items&...` | `items` | - |

**Returns:**
- `const TilePtr&`

---

(getorcreatetile)=
## `getOrCreateTile`

**Signature:**
```cpp
const TilePtr& getOrCreateTile(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `const TilePtr&`

---

(gettile)=
## `getTile`

**Signature:**
```cpp
const TilePtr& getTile(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `const TilePtr&`

---

(gettiles)=
## `getTiles`

**Signature:**
```cpp
const TileList getTiles(int floor = -1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `int` | `floor` | `-1` | - |

**Returns:**
- `const TileList`

---

(cleantile)=
## `cleanTile`

**Signature:**
```cpp
void cleanTile(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(setshowzone)=
## `setShowZone`

**Signature:**
```cpp
void setShowZone(tileflags_t zone, bool show);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `tileflags_t` | `zone` | - |
| `bool` | `show` | - |

---

(setshowzones)=
## `setShowZones`

**Signature:**
```cpp
void setShowZones(bool show);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `show` | - |

---

(setzonecolor)=
## `setZoneColor`

**Signature:**
```cpp
void setZoneColor(tileflags_t flag, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `tileflags_t` | `flag` | - |
| `const Color&` | `color` | - |

---

(getzonecolor)=
## `getZoneColor`

**Signature:**
```cpp
Color getZoneColor(tileflags_t flag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `tileflags_t` | `flag` | - |

**Returns:**
- `Color`

---

(setforceshowanimations)=
## `setForceShowAnimations`

**Signature:**
```cpp
void setForceShowAnimations(bool force);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `force` | - |

---

(isforcinganimations)=
## `isForcingAnimations`

**Signature:**
```cpp
bool isForcingAnimations();
```

**Returns:**
- `bool`

---

(isshowinganimations)=
## `isShowingAnimations`

**Signature:**
```cpp
bool isShowingAnimations();
```

**Returns:**
- `bool`

---

(setshowanimations)=
## `setShowAnimations`

**Signature:**
```cpp
void setShowAnimations(bool show);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `show` | - |

---

(addcreature)=
## `addCreature`

**Signature:**
```cpp
void addCreature(const CreaturePtr& creature);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const CreaturePtr&` | `creature` | - |

---

(getcreaturebyid)=
## `getCreatureById`

**Signature:**
```cpp
CreaturePtr getCreatureById(uint32 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |

**Returns:**
- `CreaturePtr`

---

(removecreaturebyid)=
## `removeCreatureById`

**Signature:**
```cpp
void removeCreatureById(uint32 id);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint32` | `id` | - |

---

(getsightspectators)=
## `getSightSpectators`

**Signature:**
```cpp
std::vector<CreaturePtr> getSightSpectators(const Position& centerPos, bool multiFloor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centerPos` | - |
| `bool` | `multiFloor` | - |

**Returns:**
- `std::vector&lt;CreaturePtr&gt;`

---

(getspectators)=
## `getSpectators`

**Signature:**
```cpp
std::vector<CreaturePtr> getSpectators(const Position& centerPos, bool multiFloor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centerPos` | - |
| `bool` | `multiFloor` | - |

**Returns:**
- `std::vector&lt;CreaturePtr&gt;`

---

(getspectatorsinrange)=
## `getSpectatorsInRange`

**Signature:**
```cpp
std::vector<CreaturePtr> getSpectatorsInRange(const Position& centerPos, bool multiFloor, int xRange, int yRange);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centerPos` | - |
| `bool` | `multiFloor` | - |
| `int` | `xRange` | - |
| `int` | `yRange` | - |

**Returns:**
- `std::vector&lt;CreaturePtr&gt;`

---

(getspectatorsinrangeex)=
## `getSpectatorsInRangeEx`

**Signature:**
```cpp
std::vector<CreaturePtr> getSpectatorsInRangeEx(const Position& centerPos, bool multiFloor, int minXRange, int maxXRange, int minYRange, int maxYRange);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centerPos` | - |
| `bool` | `multiFloor` | - |
| `int` | `minXRange` | - |
| `int` | `maxXRange` | - |
| `int` | `minYRange` | - |
| `int` | `maxYRange` | - |

**Returns:**
- `std::vector&lt;CreaturePtr&gt;`

---

(getspectatorsbypattern)=
## `getSpectatorsByPattern`

**Signature:**
```cpp
std::vector<CreaturePtr> getSpectatorsByPattern(const Position& centerPos, const std::string& pattern, Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centerPos` | - |
| `const std::string&` | `pattern` | - |
| `Otc::Direction` | `direction` | - |

**Returns:**
- `std::vector&lt;CreaturePtr&gt;`

---

(setcentralposition)=
## `setCentralPosition`

**Signature:**
```cpp
void setCentralPosition(const Position& centralPosition);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `centralPosition` | - |

---

(islookpossible)=
## `isLookPossible`

**Signature:**
```cpp
bool isLookPossible(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `bool`

---

(iscovered)=
## `isCovered`

**Signature:**
```cpp
bool isCovered(const Position& pos, int firstFloor = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Position&` | `pos` |  | - |
| `int` | `firstFloor` | `0` | - |

**Returns:**
- `bool`

---

(iscompletelycovered)=
## `isCompletelyCovered`

**Signature:**
```cpp
bool isCompletelyCovered(const Position& pos, int firstFloor = 0);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Position&` | `pos` |  | - |
| `int` | `firstFloor` | `0` | - |

**Returns:**
- `bool`

---

(isawareofposition)=
## `isAwareOfPosition`

**Signature:**
```cpp
bool isAwareOfPosition(const Position& pos, bool extended = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Position&` | `pos` |  | - |
| `bool` | `extended` | `false` | - |

**Returns:**
- `bool`

---

(isawareofpositionforclean)=
## `isAwareOfPositionForClean`

**Signature:**
```cpp
bool isAwareOfPositionForClean(const Position& pos, bool extended = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const Position&` | `pos` |  | - |
| `bool` | `extended` | `false` | - |

**Returns:**
- `bool`

---

(setawarerange)=
## `setAwareRange`

**Signature:**
```cpp
void setAwareRange(const AwareRange& range);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const AwareRange&` | `range` | - |

---

(resetawarerange)=
## `resetAwareRange`

**Signature:**
```cpp
void resetAwareRange();
```

---

(getfirstawarefloor)=
## `getFirstAwareFloor`

**Signature:**
```cpp
int getFirstAwareFloor();
```

**Returns:**
- `int`

---

(getlastawarefloor)=
## `getLastAwareFloor`

**Signature:**
```cpp
int getLastAwareFloor();
```

**Returns:**
- `int`

---

(newfindpath)=
## `newFindPath`

**Signature:**
```cpp
PathFindResult_ptr newFindPath(const Position& start, const Position& goal, std::shared_ptr<std::list<Node*>> visibleNodes);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `start` | - |
| `const Position&` | `goal` | - |
| `std::shared_ptr&lt;std::list&lt;Node*&gt;&gt;` | `visibleNodes` | - |

**Returns:**
- `PathFindResult_ptr`

---

(findpathasync)=
## `findPathAsync`

**Signature:**
```cpp
void findPathAsync(const Position & start, const Position & goal, std::function<void(PathFindResult_ptr)> callback);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position &` | `start` | - |
| `const Position &` | `goal` | - |
| `std::function&lt;void(PathFindResult_ptr)&gt;` | `callback` | - |

---

(getminimapcolor)=
## `getMinimapColor`

**Signature:**
```cpp
int getMinimapColor(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `int`

---

(ispatchable)=
## `isPatchable`

**Signature:**
```cpp
bool isPatchable(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `bool`

---

(iswalkable)=
## `isWalkable`

**Signature:**
```cpp
bool isWalkable(const Position& pos, bool ignoreCreatures);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `bool` | `ignoreCreatures` | - |

**Returns:**
- `bool`

---

(issightclear)=
## `isSightClear`

**Signature:**
```cpp
bool isSightClear(const Position& fromPos, const Position& toPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `fromPos` | - |
| `const Position&` | `toPos` | - |

**Returns:**
- `bool`

---

(checksightline)=
## `checkSightLine`

**Signature:**
```cpp
bool checkSightLine(const Position& fromPos, const Position& toPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `fromPos` | - |
| `const Position&` | `toPos` | - |

**Returns:**
- `bool`

---

(removeunawarethings)=
## `removeUnawareThings`

**Signature:**
```cpp
private: void removeUnawareThings();
```

---

(tileblock)=
## `TileBlock`

**Signature:**
```cpp
public: TileBlock();
```

---

(create)=
## `create`

**Signature:**
```cpp
const TilePtr& create(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `const TilePtr&`

---

(getorcreate)=
## `getOrCreate`

**Signature:**
```cpp
const TilePtr& getOrCreate(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `const TilePtr&`

---

(get)=
## `get`

**Signature:**
```cpp
const TilePtr& get(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `const TilePtr&`

---

(remove)=
## `remove`

**Signature:**
```cpp
void remove(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

---

(gettileindex)=
## `getTileIndex`

**Signature:**
```cpp
uint getTileIndex(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `uint`

---

(horizontal)=
## `horizontal`

**Signature:**
```cpp
int horizontal();
```

**Returns:**
- `int`

---

(vertical)=
## `vertical`

**Signature:**
```cpp
int vertical();
```

**Returns:**
- `int`

---

(sethousefile)=
## `setHouseFile`

**Signature:**
```cpp
void setHouseFile(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(setspawnfile)=
## `setSpawnFile`

**Signature:**
```cpp
void setSpawnFile(const std::string& file);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `file` | - |

---

(setdescription)=
## `setDescription`

**Signature:**
```cpp
void setDescription(const std::string& desc);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `desc` | - |

---

(cleardescriptions)=
## `clearDescriptions`

**Signature:**
```cpp
void clearDescriptions();
```

---

(setwidth)=
## `setWidth`

**Signature:**
```cpp
void setWidth(uint16 w);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `w` | - |

---

(setheight)=
## `setHeight`

**Signature:**
```cpp
void setHeight(uint16 h);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `uint16` | `h` | - |

---

(gethousefile)=
## `getHouseFile`

**Signature:**
```cpp
std::string getHouseFile();
```

**Returns:**
- `std::string`

---

(getspawnfile)=
## `getSpawnFile`

**Signature:**
```cpp
std::string getSpawnFile();
```

**Returns:**
- `std::string`

---

(getsize)=
## `getSize`

**Signature:**
```cpp
Size getSize();
```

**Returns:**
- `Size`

---

(getdescriptions)=
## `getDescriptions`

**Signature:**
```cpp
std::vector<std::string> getDescriptions();
```

**Returns:**
- `std::vector&lt;std::string&gt;`

---

(setzoneopacity)=
## `setZoneOpacity`

**Signature:**
```cpp
void setZoneOpacity(float opacity);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `opacity` | - |

---

(getzoneopacity)=
## `getZoneOpacity`

**Signature:**
```cpp
float getZoneOpacity();
```

**Returns:**
- `float`

---

(getzoneflags)=
## `getZoneFlags`

**Signature:**
```cpp
tileflags_t getZoneFlags();
```

**Returns:**
- `tileflags_t`

---

(showzones)=
## `showZones`

**Signature:**
```cpp
bool showZones();
```

**Returns:**
- `bool`

---

(showzone)=
## `showZone`

**Signature:**
```cpp
bool showZone(tileflags_t zone);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `tileflags_t` | `zone` | - |

**Returns:**
- `bool`

---

(setlight)=
## `setLight`

**Signature:**
```cpp
void setLight(const Light& light);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Light&` | `light` | - |

---

(getawarerange)=
## `getAwareRange`

**Signature:**
```cpp
AwareRange getAwareRange();
```

**Returns:**
- `AwareRange`

---

(getawarerangeassize)=
## `getAwareRangeAsSize`

**Signature:**
```cpp
Size getAwareRangeAsSize();
```

**Returns:**
- `Size`

---

(getlight)=
## `getLight`

**Signature:**
```cpp
Light getLight();
```

**Returns:**
- `Light`

---

(getcentralposition)=
## `getCentralPosition`

**Signature:**
```cpp
Position getCentralPosition();
```

**Returns:**
- `Position`

---

(getfloormissiles)=
## `getFloorMissiles`

**Signature:**
```cpp
const std::vector<MissilePtr>& getFloorMissiles(int z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `z` | - |

**Returns:**
- `const std::vector&lt;MissilePtr&gt;&`

---

(getanimatedtexts)=
## `getAnimatedTexts`

**Signature:**
```cpp
std::vector<AnimatedTextPtr> getAnimatedTexts();
```

**Returns:**
- `std::vector&lt;AnimatedTextPtr&gt;`

---

(getstatictexts)=
## `getStaticTexts`

**Signature:**
```cpp
std::vector<StaticTextPtr> getStaticTexts();
```

**Returns:**
- `std::vector&lt;StaticTextPtr&gt;`

---

(getblockindex)=
## `getBlockIndex`

**Signature:**
```cpp
uint getBlockIndex(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `uint`

---
