# src/framework/stdext/time.h

```cpp
ticks_t time();
```
```cpp
ticks_t millis();
```
```cpp
ticks_t micros();
```
```cpp
void millisleep(size_t ms);
```
```cpp
void microsleep(size_t us);
```
```cpp
public:
    timer() { restart();
```
```cpp
float elapsed_seconds() { return (float)((stdext::micros() - m_start)/1000000.0);
```