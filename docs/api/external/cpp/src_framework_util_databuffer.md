# src/framework/util/databuffer.h

```cpp
public:
    DataBuffer(uint res = 64) : m_size(0), m_capacity(res), m_buffer(new T[m_capacity]) { } ~DataBuffer() { if(m_buffer) delete[] m_buffer; } DataBuffer(const DataBuffer<T>& d) { m_size = d.m_size; m_capacity = std::max<uint>(64, d.m_size * 2);
```
```cpp
inline void reset() { m_size = 0; } inline void clear() { m_size = 0; m_capacity = 0; delete[] m_buffer; m_buffer = nullptr; } inline bool empty() const { return m_size == 0; } inline uint size() const { return m_size; } inline T *data() const { return m_buffer; } inline const T& at(uint i) const { return m_buffer[i]; } inline const T& last() const { return m_buffer[m_size-1]; } inline const T& first() const { return m_buffer[0]; } inline const T& operator[](uint i) const { return m_buffer[i]; } inline T& operator[](uint i) { return m_buffer[i]; } inline void reserve(uint n) { if(n > m_capacity) { T *buffer = new T[n]; memcpy(buffer, m_buffer, m_size * sizeof(T));
```
```cpp
inline void resize(uint n, T def = T()) { if(n == m_size) return; reserve(n);
```
```cpp
inline void grow(uint n, bool precise = false) { if(n <= m_size) return; if(n > m_capacity) { uint newcapacity = m_capacity; if (precise) { newcapacity = n; } else { do { newcapacity *= 4; } while (newcapacity < n);
```
```cpp
inline void add(const T& v) { grow(m_size + 1);
```