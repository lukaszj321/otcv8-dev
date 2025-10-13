# src/framework/graphics/graphics.h

```cpp
public: Graphics();
```
```cpp
void init();
```
```cpp
void terminate();
```
```cpp
void resize(const Size& size);
```
```cpp
void checkDepthSupport();
```
```cpp
void checkForError(const std::string& function, const std::string& file, int line);
```
```cpp
void checkDepthSupport();
```
```cpp
int getMaxTextureSize();
```
```cpp
const Size& getViewportSize();
```
```cpp
std::string getVendor();
```
```cpp
std::string getRenderer();
```
```cpp
std::string getVersion();
```
```cpp
std::string getExtensions();
```
```cpp
bool ok();
```