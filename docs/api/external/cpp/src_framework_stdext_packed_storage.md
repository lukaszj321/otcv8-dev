# src/framework/stdext/packed_storage.h

```cpp
void set(Key id, const T& value) { for(SizeType i=0;i<m_size;++i) { if(m_values[i].id == id) { m_values[i].value = value; return; } } auto tmp = new value_pair[m_size+1]; if(m_size > 0) { std::copy(m_values, m_values + m_size, tmp);
```
```cpp
bool remove(Key id) { auto begin = m_values; auto end = m_values + m_size; auto it = std::find_if(begin, end, [=](const value_pair& pair) -> bool { return pair.id == id; });
```
```cpp
template<typename T>
    T get(Key id) const { for(SizeType i=0;i<m_size;++i) if(m_values[i].id == id) return packed_any_cast<T>(m_values[i].value);
```
```cpp
return T();
```