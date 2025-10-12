# src/framework/stdext/dynamic_storage.h

```cpp
void set(const Key& k, const T& value) { if(m_data.size() <= k) m_data.resize(k+1);
```
```cpp
bool remove(const Key& k) { if(m_data.size() < k) return false; if(m_data[k].empty()) return false; m_data[k] = any();
```
```cpp
template<typename T> T get(const Key& k) const { return has(k) ? any_cast<T>(m_data[k]) : T();
```
```cpp
bool has(const Key& k) const { return k < m_data.size() && !m_data[k].empty();
```
```cpp
std::size_t size() const { std::size_t count = 0; for(std::size_t i=0;i<m_data.size();
```
```cpp
void clear() { m_data.clear();
```