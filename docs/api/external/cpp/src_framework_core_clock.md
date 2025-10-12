# src/framework/core/clock.h

```cpp
public:
    Clock();
```
```cpp
void update();
```
```cpp
ticks_t micros() { return m_currentMicros; } ticks_t millis() { return m_currentMillis; } float seconds() { return m_currentSeconds; } ticks_t realMicros();
```
```cpp
ticks_t realMillis();
```