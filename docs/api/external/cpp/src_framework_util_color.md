# src/framework/util/color.h

```cpp
public:
    Color() : m_r(1.0f), m_g(1.0f), m_b(1.0f), m_a(1.0f) { } Color(uint32 rgba) { setRGBA(rgba);
```
```cpp
uint8 a() const { return 255.0f * m_a; } uint8 b() const { return 255.0f * m_b; } uint8 g() const { return 255.0f * m_g; } uint8 r() const { return 255.0f * m_r; } float aF() const { return m_a; } float bF() const { return m_b; } float gF() const { return m_g; } float rF() const { return m_r; } void setRed(int r) { m_r = 0.003921f * r; } void setGreen(int g) { m_g = 0.003921f * g; } void setBlue(int b) { m_b = 0.003921f * b; } void setAlpha(int a) { m_a = 0.003921f * a; } void setRed(float r) { m_r = r; } void setGreen(float g) { m_g = g; } void setBlue(float b) { m_b = b; } void setAlpha(float a) { m_a = a; } void setRGBA(uint8 r, uint8 g, uint8 b, uint8 a = 0xFF) { m_r = r/255.0f; m_g = g/255.0f; m_b = b/255.0f; m_a = a/255.0f; } void setRGBA(uint32 rgba) { setRGBA((rgba >> 0) & 0xff, (rgba >> 8) & 0xff, (rgba >> 16) & 0xff, (rgba >> 24) & 0xff);
```
```cpp
Color opacity(float opacity) const { return Color(m_r, m_g, m_b, m_a * opacity);
```
```cpp
return Color(std::min<float>(1.0f, m_r + other.m_r), std::min<float>(1.0f, m_g + other.m_g), std::min<float>(1.0f, m_b + other.m_b), std::min<float>(1.0f, m_a + other.m_a));
```
```cpp
std::string toHex();
```
```cpp
static uint8 to8bit(const Color& color) { uint8 c = 0; c += (color.r() / 51) * 36; c += (color.g() / 51) * 6; c += (color.b() / 51);
```
```cpp
static Color from8bit(int color) { if(color >= 216 || color <= 0) return Color(0, 0, 0);
```
```cpp
return Color(r, g, b);
```
```cpp
static Color getOutfitColor(int color);
```
```cpp
out << dec << setfill(' ');
```