# src/client/spritemanager.h

```cpp
public:
    SpriteManager();
```
```cpp
void terminate();
```
```cpp
bool loadSpr(std::string file);
```
```cpp
void unload();
```
```cpp
void saveSpr(std::string fileName);
```
```cpp
void saveSpr64(std::string fileName);
```
```cpp
void encryptSprites(std::string fileName);
```
```cpp
void dumpSprites(std::string dir);
```
```cpp
uint32 getSignature() { return m_signature; } int getSpritesCount() { return m_spritesCount; } ImagePtr getSpriteImage(int id);
```
```cpp
bool isLoaded() { return m_loaded; } int spriteSize() { return m_spriteSize; } float getOffsetFactor() const { return static_cast<float>(m_spriteSize) / 32.0f; } bool isHdMod() const { return m_isHdMod; } private: bool loadCasualSpr(std::string file);
```
```cpp
bool loadCwmSpr(std::string file);
```
```cpp
ImagePtr getSpriteImageCasual(int id);
```
```cpp
ImagePtr getSpriteImageHd(int id);
```