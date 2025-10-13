# src/client/tile.h

```cpp
void calculateCorpseCorrection();
```
```cpp
void drawGround(const Point& dest, LightView* lightView = nullptr);
```
```cpp
void drawBottom(const Point& dest, LightView* lightView = nullptr);
```
```cpp
void drawCreatures(const Point& dest, LightView* lightView = nullptr);
```
```cpp
void drawTop(const Point& dest, LightView* lightView = nullptr);
```
```cpp
void drawTexts(Point dest);
```
```cpp
void drawWidget(Point dest);
```
```cpp
public: void clean();
```
```cpp
void addWalkingCreature(const CreaturePtr& creature);
```
```cpp
void removeWalkingCreature(const CreaturePtr& creature);
```
```cpp
void addThing(const ThingPtr& thing, int stackPos);
```
```cpp
bool removeThing(ThingPtr thing);
```
```cpp
ThingPtr getThing(int stackPos);
```
```cpp
EffectPtr getEffect(uint16 id);
```
```cpp
bool hasThing(const ThingPtr& thing);
```
```cpp
int getThingStackPos(const ThingPtr& thing);
```
```cpp
ThingPtr getTopThing();
```
```cpp
ThingPtr getTopLookThing();
```
```cpp
ThingPtr getTopLookThingEx(Point offset);
```
```cpp
ThingPtr getTopUseThing();
```
```cpp
CreaturePtr getTopCreature();
```
```cpp
CreaturePtr getTopCreatureEx(Point offset);
```
```cpp
ThingPtr getTopMoveThing();
```
```cpp
ThingPtr getTopMultiUseThing();
```
```cpp
ThingPtr getTopMultiUseThingEx(Point offset);
```
```cpp
std::vector<ItemPtr> getItems();
```
```cpp
std::vector<CreaturePtr> getCreatures();
```
```cpp
ItemPtr getGround();
```
```cpp
int getGroundSpeed();
```
```cpp
uint8 getMinimapColorByte();
```
```cpp
bool isPathable();
```
```cpp
bool isWalkable(bool ignoreCreatures = false);
```
```cpp
bool isFullGround();
```
```cpp
bool isFullyOpaque();
```
```cpp
bool isSingleDimension();
```
```cpp
bool isLookPossible();
```
```cpp
bool isBlockingProjectile();
```
```cpp
bool isClickable();
```
```cpp
bool isEmpty();
```
```cpp
bool isDrawable();
```
```cpp
bool mustHookSouth();
```
```cpp
bool mustHookEast();
```
```cpp
bool hasCreature();
```
```cpp
bool hasBlockingCreature();
```
```cpp
bool limitsFloorsView(bool isFreeView = false);
```
```cpp
bool canErase();
```
```cpp
int getElevation();
```
```cpp
bool hasElevation(int elevation = 1);
```
```cpp
void setText(const std::string& text, Color color);
```
```cpp
std::string getText();
```
```cpp
void setTimer(int time, Color color);
```
```cpp
int getTimer();
```
```cpp
void setFill(Color color);
```
```cpp
bool canShoot(int distance);
```
```cpp
private: void checkTranslucentLight();
```
```cpp
const Position& getPosition();
```
```cpp
int getDrawElevation();
```
```cpp
std::vector<CreaturePtr> getWalkingCreatures();
```
```cpp
std::vector<ThingPtr> getThings();
```
```cpp
std::vector<EffectPtr> getEffects();
```
```cpp
bool isBlocking();
```
```cpp
int getThingCount();
```
```cpp
bool hasTranslucentLight();
```
```cpp
void overwriteMinimapColor(uint8 color);
```
```cpp
void remFlag(uint32 flag);
```
```cpp
void setFlag(uint32 flag);
```
```cpp
void setFlags(uint32 flags);
```
```cpp
bool hasFlag(uint32 flag);
```
```cpp
uint32 getFlags();
```
```cpp
void setHouseId(uint32 hid);
```
```cpp
uint32 getHouseId();
```
```cpp
bool isHouseTile();
```
```cpp
void select();
```
```cpp
void unselect();
```
```cpp
bool isSelected();
```
```cpp
TilePtr asTile();
```
```cpp
void setSpeed(uint16_t speed, uint8_t blocking);
```
```cpp
void resetFill();
```
```cpp
void setWidget(UIWidgetPtr widget);
```
```cpp
UIWidgetPtr getWidget();
```
```cpp
void removeWidget();
```