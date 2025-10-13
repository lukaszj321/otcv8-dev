# src/framework/util/databuffer.h

```cpp
public: DataBuffer(uint res = 64) : m_size(0), m_capacity(res), m_buffer(new T[m_capacity]);
```
```cpp
inline void reset();
```
```cpp
inline void clear();
```
```cpp
inline bool empty();
```
```cpp
inline uint size();
```
```cpp
inline const T& at(uint i);
```
```cpp
inline const T& last();
```
```cpp
inline const T& first();
```
```cpp
inline void reserve(uint n);
```
```cpp
inline void resize(uint n, T def = T());
```
```cpp
inline void grow(uint n, bool precise = false);
```
```cpp
inline void add(const T& v);
```