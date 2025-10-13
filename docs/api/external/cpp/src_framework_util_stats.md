# src/framework/util/stats.h

```cpp
public: void add(int type, Stat* stats);
```
```cpp
std::string get(int type, int limit, bool pretty);
```
```cpp
void clear(int type);
```
```cpp
void clearAll();
```
```cpp
std::string getSlow(int type, int limit, unsigned int minTime, bool pretty);
```
```cpp
void clearSlow(int type);
```
```cpp
void addWidget(UIWidget* widget);
```
```cpp
void removeWidget(UIWidget* widget);
```
```cpp
std::string getWidgetsInfo(int limit, bool pretty);
```
```cpp
int types();
```
```cpp
int64_t getSleepTime();
```
```cpp
void resetSleepTime();
```
```cpp
inline void addTexture();
```
```cpp
inline void removeTexture();
```
```cpp
inline void addThing();
```
```cpp
inline void removeThing();
```
```cpp
inline void addCreature();
```
```cpp
inline void removeCreature();
```
```cpp
public: AutoStat(int type, const std::string& description, const std::string& extraDescription = "") : m_type(type), m_stat(new Stat(0, description, extraDescription)), m_timePoint(std::chrono::high_resolution_clock::now());
```