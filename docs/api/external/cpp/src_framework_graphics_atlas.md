# src/framework/graphics/atlas.h

```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void reload();
```
```cpp
Point cache(uint64_t hash, const Size& size, bool& draw);
```
```cpp
Point cacheFont(const TexturePtr& fontTexture);
```
```cpp
void bind();
```
```cpp
void release();
```
```cpp
private: void reset();
```
```cpp
void resetAtlas(int location);
```
```cpp
bool findSpace(int location, int index);
```
```cpp
inline int calculateIndex(const Size& size);
```
```cpp
TexturePtr get(int location);
```