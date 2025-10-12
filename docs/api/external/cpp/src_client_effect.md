# src/client/effect.h

```cpp
public:
    void draw(const Point& dest, bool animate = true, LightView* lightView = nullptr) override {} void draw(const Point& dest, int offsetX = 0, int offsetY = 0, bool animate = true, LightView* lightView = nullptr);
```
```cpp
void setId(uint32 id) override; uint32 getId() override { return m_id; } EffectPtr asEffect() { return static_self_cast<Effect>();
```