# src/framework/graphics/hardwarebuffer.h

```cpp
void bind() { glBindBuffer(m_type, m_id);
```
```cpp
static void unbind(Type type) { glBindBuffer(type, 0);
```
```cpp
void write(void *data, int count, UsagePattern usage) { glBufferData(m_type, count, data, usage);
```