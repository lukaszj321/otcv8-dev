# src/client/outfit.h

```cpp
public: Outfit();
```
```cpp
return Color::getOutfitColor(color);
```
```cpp
void draw(Point dest, Otc::Direction direction, uint walkAnimationPhase, bool animate = true, LightView* lightView = nullptr, bool ui = false);
```
```cpp
void draw(const Rect& dest, Otc::Direction direction, uint animationPhase, bool animate = true, bool ui = false, bool oldScaling = false);
```
```cpp
void resetClothes();
```
```cpp
static Color getColor(int color);
```
```cpp
void setId(int id);
```
```cpp
void setAuxId(int id);
```
```cpp
void setHead(int head);
```
```cpp
void setBody(int body);
```
```cpp
void setLegs(int legs);
```
```cpp
void setFeet(int feet);
```
```cpp
void setAddons(int addons);
```
```cpp
void setMount(int mount);
```
```cpp
void setWings(int wings);
```
```cpp
void setAura(int aura);
```
```cpp
void setCategory(ThingCategory category);
```
```cpp
void setShader(const std::string& shader);
```
```cpp
void setHealthBar(uint8 id);
```
```cpp
void setManaBar(uint8 id);
```
```cpp
void setCenter(bool value);
```
```cpp
void resetShader();
```
```cpp
int getId();
```
```cpp
int getAuxId();
```
```cpp
int getHead();
```
```cpp
int getBody();
```
```cpp
int getLegs();
```
```cpp
int getFeet();
```
```cpp
int getAddons();
```
```cpp
int getMount();
```
```cpp
int getWings();
```
```cpp
int getAura();
```
```cpp
ThingCategory getCategory();
```
```cpp
std::string getShader();
```
```cpp
int getHealthBar();
```
```cpp
int getManaBar();
```