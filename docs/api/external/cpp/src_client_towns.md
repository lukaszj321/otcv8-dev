# src/client/towns.h

```cpp
public: TownManager();
```
```cpp
void addTown(const TownPtr& town);
```
```cpp
void removeTown(uint32 townId);
```
```cpp
const TownPtr& getTown(uint32 townId);
```
```cpp
const TownPtr& getTownByName(std::string name);
```
```cpp
void sort();
```
```cpp
protected: TownList::iterator findTown(uint32 townId);
```
```cpp
public: Town();
```
```cpp
void setId(uint32 tid);
```
```cpp
void setName(const std::string& name);
```
```cpp
void setPos(const Position& pos);
```
```cpp
uint32 getId();
```
```cpp
std::string getName();
```
```cpp
Position getPos();
```
```cpp
TownList getTowns();
```
```cpp
void clear();
```