# src/client/outfit.h

```cpp
public:
    Outfit();
```
```cpp
static Color getColor(int color) { return Color::getOutfitColor(color);
```
```cpp
void draw(Point dest, Otc::Direction direction, uint walkAnimationPhase, bool animate = true, LightView* lightView = nullptr, bool ui = false);
```
```cpp
void draw(const Rect& dest, Otc::Direction direction, uint animationPhase, bool animate = true, bool ui = false, bool oldScaling = false);
```
```cpp
void setId(int id) { m_id = id; } void setAuxId(int id) { m_auxId = id; } void setHead(int head) { m_head = head; } void setBody(int body) { m_body = body; } void setLegs(int legs) { m_legs = legs; } void setFeet(int feet) { m_feet = feet; } void setAddons(int addons) { m_addons = addons; } void setMount(int mount) { m_mount = mount; } void setWings(int wings) { m_wings = wings; } void setAura(int aura) { m_aura = aura; } void setCategory(ThingCategory category) { m_category = category; } void setShader(const std::string& shader) { m_shader = shader; } void setHealthBar(uint8 id) { m_healthBar = id; } void setManaBar(uint8 id) { m_manaBar = id; } void setCenter(bool value) { m_center = value; } void resetClothes();
```