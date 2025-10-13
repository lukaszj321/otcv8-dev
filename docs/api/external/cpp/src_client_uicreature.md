# src/client/uicreature.h

```cpp
public: void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void setOutfit(const Outfit& outfit);
```
```cpp
void setCenter(bool value);
```
```cpp
protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
void setCreature(const CreaturePtr& creature);
```
```cpp
void setFixedCreatureSize(bool fixed);
```
```cpp
CreaturePtr getCreature();
```
```cpp
Outfit getOutfit();
```
```cpp
bool isFixedCreatureSize();
```
```cpp
void setAutoRotating(bool value);
```
```cpp
void setDirection(Otc::Direction direction);
```
```cpp
Otc::Direction getDirection();
```
```cpp
void setScale(float scale);
```
```cpp
float getScale();
```
```cpp
void setAnimate(bool value);
```
```cpp
bool isAnimating();
```
```cpp
void setOldScaling(bool value);
```