# src/framework/stdext/math.h

```cpp
inline bool is_power_of_two(size_t v) { return ((v != 0) && !(v & (v - 1)));
```
```cpp
inline size_t to_power_of_two(size_t v) { if(v == 0) return 0; size_t r = 1; while(r < v && r != 0xffffffff) r <<= 1; return r; } inline uint16_t readULE16(const uchar *addr) { return (uint16_t)addr[1] << 8 | addr[0]; } inline uint32_t readULE32(const uchar *addr) { return (uint32_t)readULE16(addr + 2) << 16 | readULE16(addr);
```
```cpp
inline uint64_t readULE64(const uchar *addr) { return (uint64_t)readULE32(addr + 4) << 32 | readULE32(addr);
```
```cpp
inline void writeULE16(uchar *addr, uint16_t value) { addr[1] = value >> 8; addr[0] = (uint8_t)value; } inline void writeULE32(uchar *addr, uint32_t value) { writeULE16(addr + 2, value >> 16);
```
```cpp
inline void writeULE64(uchar *addr, uint64_t value) { writeULE32(addr + 4, value >> 32);
```
```cpp
inline int16_t readSLE16(const uchar *addr) { return (int16_t)addr[1] << 8 | addr[0]; } inline int32_t readSLE32(const uchar *addr) { return (int32_t)readSLE16(addr + 2) << 16 | readSLE16(addr);
```
```cpp
inline int64_t readSLE64(const uchar *addr) { return (int64_t)readSLE32(addr + 4) << 32 | readSLE32(addr);
```
```cpp
inline void writeSLE16(uchar *addr, int16_t value) { addr[1] = value >> 8; addr[0] = (int8_t)value; } inline void writeSLE32(uchar *addr, int32_t value) { writeSLE16(addr + 2, value >> 16);
```
```cpp
inline void writeSLE64(uchar *addr, int64_t value) { writeSLE32(addr + 4, value >> 32);
```
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
template<typename T>
T clamp(T x, T min, T max) { return std::max<T>(min, std::min<T>(x, max));
```