# src/framework/util/framecounter.h

```cpp
public:
    void addFrame() // not thread-safe { ticks_t now = stdext::millis();
```
```cpp
int getFps() // thread safe { return m_frames.load();
```