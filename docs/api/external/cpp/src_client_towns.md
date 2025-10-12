# src/client/towns.h

```cpp
public:
    Town() { } Town(uint32 tid, const std::string& name, const Position& pos=Position());
```
```cpp
void setId(uint32 tid) { m_id = tid; } void setName(const std::string& name) { m_name = name; } void setPos(const Position& pos) { m_pos = pos; } uint32 getId() { return m_id; } std::string getName() { return m_name; } Position getPos() { return m_pos; } private: uint32 m_id; std::string m_name; Position m_pos; // temple pos }; class TownManager { public: TownManager();
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
TownList getTowns() { return m_towns; } void clear() { m_towns.clear();
```
```cpp
protected:
    TownList::iterator findTown(uint32 townId);
```