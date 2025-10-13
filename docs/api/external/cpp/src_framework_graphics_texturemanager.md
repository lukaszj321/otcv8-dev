# src/framework/graphics/texturemanager.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void clearCache();
```
```cpp
void reload();
```
```cpp
TexturePtr getTexture(const std::string& fileName);
```
```cpp
TexturePtr loadTexture(std::stringstream& file, const std::string& source);
```
```cpp
void preload(const std::string& fileName);
```