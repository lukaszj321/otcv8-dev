# src/client/item.h

```cpp
public:
    Item();
```
```cpp
static ItemPtr create(int id, int countOrSubtype = 1);
```
```cpp
static ItemPtr createFromOtb(int id);
```
```cpp
void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```
```cpp
void draw(const Rect& dest, bool animate = true);
```
```cpp
void setId(uint32 id);
```
```cpp
void setOtbId(uint16 id);
```
```cpp
void setCountOrSubType(int value) { m_countOrSubType = value; } void setCount(int count) { m_countOrSubType = count; } void setSubType(int subType) { m_countOrSubType = subType; } void setColor(const Color& c) { m_color = c; } void setTooltip(const std::string& str) { m_tooltip = str; } void setQuickLootFlags(uint32 flags) { m_quickLootFlags = flags; } void setShader(const std::string& str) { m_shader = str; } int getCountOrSubType() { return m_countOrSubType; } int getSubType();
```
```cpp
int getCount();
```
```cpp
uint32 getId() { return m_clientId; } uint16 getClientId() { return m_clientId; } uint16 getServerId() { return m_serverId; } std::string getName();
```
```cpp
bool isValid();
```
```cpp
std::string getTooltip() { return m_tooltip; } uint32 getQuickLootFlags() { return m_quickLootFlags; } std::string getShader() { return m_shader; } void unserializeItem(const BinaryTreePtr& in);
```
```cpp
void serializeItem(const OutputBinaryTreePtr& out);
```
```cpp
void setDepotId(uint16 depotId) { m_attribs.set(ATTR_DEPOT_ID, depotId);
```
```cpp
uint16 getDepotId() { return m_attribs.get<uint16>(ATTR_DEPOT_ID);
```
```cpp
void setDoorId(uint8 doorId) { m_attribs.set(ATTR_HOUSEDOORID, doorId);
```
```cpp
uint8 getDoorId() { return m_attribs.get<uint8>(ATTR_HOUSEDOORID);
```
```cpp
uint16 getUniqueId() { return m_attribs.get<uint16>(ATTR_UNIQUE_ID);
```
```cpp
uint16 getActionId() { return m_attribs.get<uint16>(ATTR_ACTION_ID);
```
```cpp
void setActionId(uint16 actionId) { m_attribs.set(ATTR_ACTION_ID, actionId);
```
```cpp
void setUniqueId(uint16 uniqueId) { m_attribs.set(ATTR_UNIQUE_ID, uniqueId);
```
```cpp
std::string getText() { return m_attribs.get<std::string>(ATTR_TEXT);
```
```cpp
std::string getDescription() { return m_attribs.get<std::string>(ATTR_DESC);
```
```cpp
void setDescription(std::string desc) { m_attribs.set(ATTR_DESC, desc);
```
```cpp
void setText(std::string txt) { m_attribs.set(ATTR_TEXT, txt);
```
```cpp
Position getTeleportDestination() { return m_attribs.get<Position>(ATTR_TELE_DEST);
```
```cpp
void setTeleportDestination(const Position& pos) { m_attribs.set(ATTR_TELE_DEST, pos);
```
```cpp
void setAsync(bool enable) { m_async = enable; } bool isHouseDoor() { return m_attribs.has(ATTR_HOUSEDOORID);
```
```cpp
bool isDepot() { return m_attribs.has(ATTR_DEPOT_ID);
```
```cpp
bool isContainer() { return m_attribs.has(ATTR_CONTAINER_ITEMS);
```
```cpp
bool isDoor() { return m_attribs.has(ATTR_HOUSEDOORID);
```
```cpp
bool isTeleport() { return m_attribs.has(ATTR_TELE_DEST);
```
```cpp
bool isMoveable();
```
```cpp
bool isGround();
```
```cpp
ItemPtr clone();
```
```cpp
ItemPtr asItem() { return static_self_cast<Item>();
```
```cpp
bool isItem() { return true; } ItemVector getContainerItems() { return m_containerItems; } ItemPtr getContainerItem(int slot) { return m_containerItems[slot]; } void addContainerItemIndexed(const ItemPtr& i, int slot) { m_containerItems[slot] = i; } void addContainerItem(const ItemPtr& i) { m_containerItems.push_back(i);
```
```cpp
void removeContainerItem(int slot) { m_containerItems[slot] = nullptr; } void clearContainerItems() { m_containerItems.clear();
```
```cpp
void calculatePatterns(int& xPattern, int& yPattern, int& zPattern);
```
```cpp
int calculateAnimationPhase(bool animate);
```
```cpp
int getExactSize(int layer = 0, int xPattern = 0, int yPattern = 0, int zPattern = 0, int animationPhase = 0);
```
```cpp
const ThingTypePtr& getThingType();
```
```cpp
void setCustomAttribute(uint16 key, uint64 value) { m_customAttribs.set(key, value);
```
```cpp
uint64 getCustomAttribute(uint16 key) { return m_customAttribs.get<uint64>(key);
```