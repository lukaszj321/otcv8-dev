# src/framework/graphics/graphics.h

```cpp
public:
    Graphics();
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
int getMaxTextureSize() { return m_maxTextureSize; } const Size& getViewportSize() { return m_viewportSize; } std::string getVendor() { return m_vendor; } std::string getRenderer() { return m_renderer; } std::string getVersion() { return m_version; } std::string getExtensions() { return m_extensions; } bool ok() { return m_ok; } void checkForError(const std::string& function, const std::string& file, int line);
```
```cpp
void checkDepthSupport();
```