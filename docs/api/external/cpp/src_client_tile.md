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
public:
    void clean();
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
const Position& getPosition() { return m_position; } int getDrawElevation() { return m_drawElevation; } std::vector<ItemPtr> getItems();
```
```cpp
std::vector<CreaturePtr> getCreatures();
```
```cpp
std::vector<CreaturePtr> getWalkingCreatures() { return m_walkingCreatures; } std::vector<ThingPtr> getThings() { return m_things; } std::vector<EffectPtr> getEffects() { return m_effects; } ItemPtr getGround();
```
```cpp
int getGroundSpeed();
```
```cpp
bool isBlocking() { return m_blocking != 0; } uint8 getMinimapColorByte();
```
```cpp
int getThingCount() { return m_things.size() + m_effects.size();
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
bool hasTranslucentLight() { return m_flags & TILESTATE_TRANSLUECENT_LIGHT; } bool mustHookSouth();
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
void overwriteMinimapColor(uint8 color) { m_minimapColor = color; } void remFlag(uint32 flag) { m_flags &= ~flag; } void setFlag(uint32 flag) { m_flags |= flag; } void setFlags(uint32 flags) { m_flags = flags; } bool hasFlag(uint32 flag) { return (m_flags & flag) == flag; } uint32 getFlags() { return m_flags; } void setHouseId(uint32 hid) { m_houseId = hid; } uint32 getHouseId() { return m_houseId; } bool isHouseTile() { return m_houseId != 0 && (m_flags & TILESTATE_HOUSE) == TILESTATE_HOUSE; } void select() { m_selected = true; } void unselect() { m_selected = false; } bool isSelected() { return m_selected; } TilePtr asTile() { return static_self_cast<Tile>();
```
```cpp
void setSpeed(uint16_t speed, uint8_t blocking) { m_speed = speed; m_blocking = blocking; } void setText(const std::string& text, Color color);
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
void resetFill() { m_fill = Color::alpha; } bool canShoot(int distance);
```
```cpp
void setWidget(UIWidgetPtr widget) { m_widget = widget; } UIWidgetPtr getWidget() { return m_widget; } void removeWidget() { if (m_widget) { m_widget->destroy();
```
```cpp
private:
    void checkTranslucentLight();
```