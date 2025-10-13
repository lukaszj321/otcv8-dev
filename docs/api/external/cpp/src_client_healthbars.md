# src/client/healthbars.h

```cpp
void setTexture(const std::string& path);
```
```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void addHealthBackground(const std::string& path, int offsetX, int offsetY, int barOffsetX, int barOffsetY, int height);
```
```cpp
void addManaBackground(const std::string& path, int offsetX, int offsetY, int barOffsetX, int barOffsetY, int height);
```
```cpp
std::string getHealthBarPath(int id);
```
```cpp
std::string getManaBarPath(int id);
```
```cpp
Point getHealthBarOffset(int id);
```
```cpp
Point getManaBarOffset(int id);
```
```cpp
Point getHealthBarOffsetBar(int id);
```
```cpp
Point getManaBarOffsetBar(int id);
```
```cpp
int getHealthBarHeight(int id);
```
```cpp
int getManaBarHeight(int id);
```
```cpp
public: void setPath(const std::string& path);
```
```cpp
std::string getPath();
```
```cpp
TexturePtr getTexture();
```
```cpp
void setOffset(int x, int y);
```
```cpp
Point getOffset();
```
```cpp
void setBarOffset(int x, int y);
```
```cpp
Point getBarOffset();
```
```cpp
void setHeight(int height);
```
```cpp
int getHeight();
```
```cpp
HealthBarPtr getHealthBar(int id);
```
```cpp
HealthBarPtr getManaBar(int id);
```