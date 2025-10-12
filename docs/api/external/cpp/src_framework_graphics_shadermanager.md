# src/framework/graphics/shadermanager.h

```cpp
public:
    void init();
```
```cpp
void terminate();
```
```cpp
void createShader(const std::string& name, std::string vertex, std::string fragment, bool colorMatrix = false);
```
```cpp
void createOutfitShader(const std::string& name, std::string vertex, std::string fragment) { return createShader(name, vertex, fragment, true);
```
```cpp
void addTexture(const std::string& name, const std::string& file);
```
```cpp
PainterShaderProgramPtr getShader(const std::string& name);
```