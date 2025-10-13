# src/framework/util/color.h

```cpp
return Color(m_r, m_g, m_b, m_a * opacity);
```
```cpp
return Color(std::min<float>(1.0f, m_r + other.m_r), std::min<float>(1.0f, m_g + other.m_g), std::min<float>(1.0f, m_b + other.m_b), std::min<float>(1.0f, m_a + other.m_a));
```
```cpp
std::string toHex();
```
```cpp
return Color(0, 0, 0);
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
```cpp
public: Color() : m_r(1.0f), m_g(1.0f), m_b(1.0f), m_a(1.0f);
```
```cpp
uint8 a();
```
```cpp
uint8 b();
```
```cpp
uint8 g();
```
```cpp
uint8 r();
```
```cpp
float aF();
```
```cpp
float bF();
```
```cpp
float gF();
```
```cpp
float rF();
```
```cpp
void setRed(int r);
```
```cpp
void setGreen(int g);
```
```cpp
void setBlue(int b);
```
```cpp
void setAlpha(int a);
```
```cpp
void setRed(float r);
```
```cpp
void setGreen(float g);
```
```cpp
void setBlue(float b);
```
```cpp
void setAlpha(float a);
```
```cpp
void setRGBA(uint8 r, uint8 g, uint8 b, uint8 a = 0xFF);
```
```cpp
void setRGBA(uint32 rgba);
```
```cpp
Color opacity(float opacity);
```
```cpp
Color operator*(float v);
```
```cpp
static uint8 to8bit(const Color& color);
```
```cpp
static Color from8bit(int color);
```
```cpp
inline std::ostream& operator<<(std::ostream& out, const Color& color);
```
```cpp
inline std::istream& operator>>(std::istream& in, Color& color);
```