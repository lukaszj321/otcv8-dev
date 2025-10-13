# src/client/missile.h

```cpp
public: void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```
```cpp
void setId(uint32 id);
```
```cpp
void setPath(const Position& fromPosition, const Position& toPosition);
```
```cpp
const ThingTypePtr& getThingType();
```
```cpp
uint32 getId();
```
```cpp
MissilePtr asMissile();
```
```cpp
bool isMissile();
```
```cpp
Position getSource();
```
```cpp
Position getDestination();
```