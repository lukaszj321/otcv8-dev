# src/framework/input/mouse.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void loadCursors(std::string filename);
```
```cpp
void addCursor(const std::string& name, const std::string& file, const Point& hotSpot);
```
```cpp
void pushCursor(const std::string& name);
```
```cpp
void popCursor(const std::string& name);
```
```cpp
bool isCursorChanged();
```
```cpp
bool isPressed(Fw::MouseButton mouseButton);
```