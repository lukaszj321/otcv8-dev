# src/client/uicreature.h

```cpp
public:
    void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void setCreature(const CreaturePtr& creature) { m_creature = creature; } void setFixedCreatureSize(bool fixed) { m_scale = fixed ? 1.0 : 0; } void setOutfit(const Outfit& outfit);
```
```cpp
CreaturePtr getCreature() { return m_creature; } Outfit getOutfit() { return m_creature ? m_creature->getOutfit() : Outfit();
```
```cpp
bool isFixedCreatureSize() { return m_scale > 0; } void setAutoRotating(bool value) { m_autoRotating = value; } void setDirection(Otc::Direction direction) { m_direction = direction; } Otc::Direction getDirection() { return m_direction; } void setScale(float scale) { m_scale = scale; } float getScale() { return m_scale; } void setAnimate(bool value) { m_animate = value; } bool isAnimating() { return m_animate; } void setCenter(bool value);
```
```cpp
void setOldScaling(bool value) { m_oldScaling = value; } protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```