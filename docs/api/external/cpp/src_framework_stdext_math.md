# src/framework/stdext/math.h

```cpp
uint32_t adler32(const uint8_t *buffer, size_t size);
```
```cpp
long random_range(long min, long max);
```
```cpp
float random_range(float min, float max);
```
```cpp
double round(double r);
```
```cpp
inline bool is_power_of_two(size_t v);
```
```cpp
inline size_t to_power_of_two(size_t v);
```
```cpp
inline uint16_t readULE16(const uchar *addr);
```
```cpp
inline uint32_t readULE32(const uchar *addr);
```
```cpp
inline uint64_t readULE64(const uchar *addr);
```
```cpp
inline void writeULE16(uchar *addr, uint16_t value);
```
```cpp
inline void writeULE32(uchar *addr, uint32_t value);
```
```cpp
inline void writeULE64(uchar *addr, uint64_t value);
```
```cpp
inline int16_t readSLE16(const uchar *addr);
```
```cpp
inline int32_t readSLE32(const uchar *addr);
```
```cpp
inline int64_t readSLE64(const uchar *addr);
```
```cpp
inline void writeSLE16(uchar *addr, int16_t value);
```
```cpp
inline void writeSLE32(uchar *addr, int32_t value);
```
```cpp
inline void writeSLE64(uchar *addr, int64_t value);
```
```cpp
template<typename T> T clamp(T x, T min, T max);
```