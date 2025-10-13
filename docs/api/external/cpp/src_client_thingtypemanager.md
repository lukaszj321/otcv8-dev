# src/client/thingtypemanager.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void check();
```
```cpp
bool loadDat(std::string file);
```
```cpp
bool loadOtml(std::string file);
```
```cpp
void loadOtb(const std::string& file);
```
```cpp
void loadXml(const std::string& file);
```
```cpp
void parseItemType(uint16 id, TiXmlElement *elem);
```
```cpp
void saveDat(std::string fileName);
```
```cpp
void dumpTextures(std::string dir);
```
```cpp
void replaceTextures(std::string dir);
```
```cpp
void addItemType(const ItemTypePtr& itemType);
```
```cpp
const ItemTypePtr& findItemTypeByClientId(uint16 id);
```
```cpp
const ItemTypePtr& findItemTypeByName(std::string name);
```
```cpp
ItemTypeList findItemTypesByName(std::string name);
```
```cpp
ItemTypeList findItemTypesByString(std::string str);
```
```cpp
const ThingTypePtr& getThingType(uint16 id, ThingCategory category);
```
```cpp
const ItemTypePtr& getItemType(uint16 id);
```
```cpp
ThingTypeList findThingTypeByAttr(ThingAttr attr, ThingCategory category);
```
```cpp
ItemTypeList findItemTypeByCategory(ItemCategory category);
```
```cpp
const ThingTypeList& getThingTypes(ThingCategory category);
```
```cpp
std::set<int> getMarketCategories();
```
```cpp
const ThingTypePtr& getNullThingType();
```
```cpp
const ItemTypePtr& getNullItemType();
```
```cpp
ThingType* rawGetThingType(uint16 id, ThingCategory category);
```
```cpp
ItemType* rawGetItemType(uint16 id);
```
```cpp
const ItemTypeList& getItemTypes();
```
```cpp
uint32 getDatSignature();
```
```cpp
uint32 getOtbMajorVersion();
```
```cpp
uint32 getOtbMinorVersion();
```
```cpp
uint16 getContentRevision();
```
```cpp
bool isDatLoaded();
```
```cpp
bool isXmlLoaded();
```
```cpp
bool isOtbLoaded();
```
```cpp
bool isValidDatId(uint16 id, ThingCategory category);
```
```cpp
bool isValidOtbId(uint16 id);
```