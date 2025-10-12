# src/client/houses.h

```cpp
public:
    House();
```
```cpp
void setTile(const TilePtr& tile);
```
```cpp
TilePtr getTile(const Position& pos);
```
```cpp
void setName(const std::string& name) { m_attribs.set(HouseAttrName, name);
```
```cpp
std::string getName() { return m_attribs.get<std::string>(HouseAttrName);
```
```cpp
void setId(uint32 hId) { m_attribs.set(HouseAttrId, hId);
```
```cpp
uint32 getId() { return m_attribs.get<uint32>(HouseAttrId);
```
```cpp
void setTownId(uint32 tid) { m_attribs.set(HouseAttrTown, tid);
```
```cpp
uint32 getTownId() { return m_attribs.get<uint32>(HouseAttrTown);
```
```cpp
void setSize(uint32 s) { m_attribs.set(HouseAttrSize, s);
```
```cpp
uint32 getSize() { return m_attribs.get<uint32>(HouseAttrSize);
```
```cpp
void setRent(uint32 r) { m_attribs.set(HouseAttrRent, r);
```
```cpp
uint32 getRent() { return m_attribs.get<uint32>(HouseAttrRent);
```
```cpp
void setEntry(const Position& p) { m_attribs.set(HouseAttrEntry, p);
```
```cpp
Position getEntry() { return m_attribs.get<Position>(HouseAttrEntry);
```
```cpp
void addDoor(const ItemPtr& door);
```
```cpp
void removeDoor(const ItemPtr& door) { removeDoorById(door->getDoorId());
```
```cpp
void removeDoorById(uint32 doorId);
```
```cpp
protected:
    void load(const TiXmlElement* elem);
```
```cpp
void save(TiXmlElement* elem);
```
```cpp
public:
    HouseManager();
```
```cpp
void addHouse(const HousePtr& house);
```
```cpp
void removeHouse(uint32 houseId);
```
```cpp
HousePtr getHouse(uint32 houseId);
```
```cpp
HousePtr getHouseByName(std::string name);
```
```cpp
void load(const std::string& fileName);
```
```cpp
void save(const std::string& fileName);
```
```cpp
void sort();
```
```cpp
void clear() { m_houses.clear();
```
```cpp
HouseList getHouseList() { return m_houses; } HouseList filterHouses(uint32 townId);
```
```cpp
protected:
    HouseList::iterator findHouse(uint32 houseId);
```