# src/client/thingtypemanager.h

```cpp
public:
    void init();
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
std::set<int> getMarketCategories() { return m_marketCategories; } const ThingTypePtr& getNullThingType() { return m_nullThingType; } const ItemTypePtr& getNullItemType() { return m_nullItemType; } const ThingTypePtr& getThingType(uint16 id, ThingCategory category);
```
```cpp
const ItemTypePtr& getItemType(uint16 id);
```
```cpp
ThingType* rawGetThingType(uint16 id, ThingCategory category) { VALIDATE(id < m_thingTypes[category].size());
```
```cpp
ItemType* rawGetItemType(uint16 id) { VALIDATE(id < m_itemTypes.size());
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
const ItemTypeList& getItemTypes() { return m_itemTypes; } uint32 getDatSignature() { return m_datSignature; } uint32 getOtbMajorVersion() { return m_otbMajorVersion; } uint32 getOtbMinorVersion() { return m_otbMinorVersion; } uint16 getContentRevision() { return m_contentRevision; } bool isDatLoaded() { return m_datLoaded; } bool isXmlLoaded() { return m_xmlLoaded; } bool isOtbLoaded() { return m_otbLoaded; } bool isValidDatId(uint16 id, ThingCategory category) { return id >= 1 && id < m_thingTypes[category].size();
```
```cpp
bool isValidOtbId(uint16 id) { return id >= 1 && id < m_itemTypes.size();
```