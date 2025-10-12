# src/framework/graphics/deptharray.h

```cpp
public:
    inline void addDepth(float depth) { m_buffer << depth; } void clear() { m_buffer.reset();
```
```cpp
int depthCount() const { return m_buffer.size();
```
```cpp
int count() const { return m_buffer.size();
```
```cpp
int size() const { return m_buffer.size();
```