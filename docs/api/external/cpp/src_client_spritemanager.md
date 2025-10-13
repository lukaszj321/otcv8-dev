# src/client/spritemanager.h

```cpp
public: SpriteManager();
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
ImagePtr getSpriteImage(int id);
```
```cpp
private: bool loadCasualSpr(std::string file);
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
```cpp
uint32 getSignature();
```
```cpp
int getSpritesCount();
```
```cpp
bool isLoaded();
```
```cpp
int spriteSize();
```
```cpp
float getOffsetFactor();
```
```cpp
bool isHdMod();
```