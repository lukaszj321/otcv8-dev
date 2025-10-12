# src/framework/graphics/colorarray.h

```cpp
public:
    inline void addColor(float r, float g, float b, float a) { m_buffer << r << g << b << a; } inline void addColor(const Color& c) { addColor(c.rF(), c.gF(), c.bF(), c.aF());
```
```cpp
void clear() { m_buffer.reset();
```
```cpp
int colorCount() const { return m_buffer.size() / 4; } int count() const { return m_buffer.size() / 4; } int size() const { return m_buffer.size();
```