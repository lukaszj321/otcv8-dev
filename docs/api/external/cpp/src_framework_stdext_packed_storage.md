# src/framework/stdext/packed_storage.h

```cpp
return packed_any_cast<T>(m_values[i].value);
```
```cpp
return T();
```
```cpp
public: packed_storage() : m_values(nullptr), m_size(0);
```
```cpp
void set(Key id, const T& value);
```
```cpp
bool remove(Key id);
```
```cpp
template<typename T> T get(Key id);
```
```cpp
bool has(Key id);
```
```cpp
void clear();
```
```cpp
std::size_t size();
```