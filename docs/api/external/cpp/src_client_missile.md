# src/client/missile.h

```cpp
public:
    void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr);
```
```cpp
void setId(uint32 id);
```
```cpp
void setPath(const Position& fromPosition, const Position& toPosition);
```
```cpp
uint32 getId() { return m_id; } MissilePtr asMissile() { return static_self_cast<Missile>();
```
```cpp
bool isMissile() { return true; } const ThingTypePtr& getThingType();
```