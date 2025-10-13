# src/client/item.h

```cpp
public: Item();
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
int getSubType();
```
```cpp
int getCount();
```
```cpp
std::string getName();
```
```cpp
bool isValid();
```
```cpp
void unserializeItem(const BinaryTreePtr& in);
```
```cpp
void serializeItem(const OutputBinaryTreePtr& out);
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
void setCountOrSubType(int value);
```
```cpp
void setCount(int count);
```
```cpp
void setSubType(int subType);
```
```cpp
void setColor(const Color& c);
```
```cpp
void setTooltip(const std::string& str);
```
```cpp
void setQuickLootFlags(uint32 flags);
```
```cpp
void setShader(const std::string& str);
```
```cpp
int getCountOrSubType();
```
```cpp
uint32 getId();
```
```cpp
uint16 getClientId();
```
```cpp
uint16 getServerId();
```
```cpp
std::string getTooltip();
```
```cpp
uint32 getQuickLootFlags();
```
```cpp
std::string getShader();
```
```cpp
void setDepotId(uint16 depotId);
```
```cpp
uint16 getDepotId();
```
```cpp
void setDoorId(uint8 doorId);
```
```cpp
uint8 getDoorId();
```
```cpp
uint16 getUniqueId();
```
```cpp
uint16 getActionId();
```
```cpp
void setActionId(uint16 actionId);
```
```cpp
void setUniqueId(uint16 uniqueId);
```
```cpp
std::string getText();
```
```cpp
std::string getDescription();
```
```cpp
void setDescription(std::string desc);
```
```cpp
void setText(std::string txt);
```
```cpp
Position getTeleportDestination();
```
```cpp
void setTeleportDestination(const Position& pos);
```
```cpp
void setAsync(bool enable);
```
```cpp
bool isHouseDoor();
```
```cpp
bool isDepot();
```
```cpp
bool isContainer();
```
```cpp
bool isDoor();
```
```cpp
bool isTeleport();
```
```cpp
ItemPtr asItem();
```
```cpp
bool isItem();
```
```cpp
ItemVector getContainerItems();
```
```cpp
ItemPtr getContainerItem(int slot);
```
```cpp
void addContainerItemIndexed(const ItemPtr& i, int slot);
```
```cpp
void addContainerItem(const ItemPtr& i);
```
```cpp
void removeContainerItem(int slot);
```
```cpp
void clearContainerItems();
```
```cpp
void setCustomAttribute(uint16 key, uint64 value);
```
```cpp
uint64 getCustomAttribute(uint16 key);
```