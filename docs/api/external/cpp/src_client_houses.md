# src/client/houses.h

```cpp
public: House();
```
```cpp
void setTile(const TilePtr& tile);
```
```cpp
TilePtr getTile(const Position& pos);
```
```cpp
void addDoor(const ItemPtr& door);
```
```cpp
void removeDoorById(uint32 doorId);
```
```cpp
protected: void load(const TiXmlElement* elem);
```
```cpp
void save(TiXmlElement* elem);
```
```cpp
public: HouseManager();
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
HouseList filterHouses(uint32 townId);
```
```cpp
protected: HouseList::iterator findHouse(uint32 houseId);
```
```cpp
void setName(const std::string& name);
```
```cpp
std::string getName();
```
```cpp
void setId(uint32 hId);
```
```cpp
uint32 getId();
```
```cpp
void setTownId(uint32 tid);
```
```cpp
uint32 getTownId();
```
```cpp
void setSize(uint32 s);
```
```cpp
uint32 getSize();
```
```cpp
void setRent(uint32 r);
```
```cpp
uint32 getRent();
```
```cpp
void setEntry(const Position& p);
```
```cpp
Position getEntry();
```
```cpp
void removeDoor(const ItemPtr& door);
```
```cpp
void clear();
```
```cpp
HouseList getHouseList();
```