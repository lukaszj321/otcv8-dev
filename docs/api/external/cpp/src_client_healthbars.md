# src/client/healthbars.h

```cpp
public:
    void setPath(const std::string& path) { m_path = path; } std::string getPath() { return m_path; } void setTexture(const std::string& path);
```
```cpp
TexturePtr getTexture() { return m_texture; } void setOffset(int x, int y) { m_offset = Point(x, y);
```
```cpp
Point getOffset() { return m_offset; } void setBarOffset(int x, int y) { m_barOffset = Point(x, y);
```
```cpp
Point getBarOffset() { return m_barOffset; } void setHeight(int height) { m_height = height; } int getHeight() { return m_height; } private: std::string m_path; TexturePtr m_texture; Point m_offset; Point m_barOffset; int m_height; }; //@bindsingleton g_healthBars class HealthBars { public: void init();
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
HealthBarPtr getHealthBar(int id) { return m_healthBars[id]; } HealthBarPtr getManaBar(int id) { return m_manaBars[id]; } std::string getHealthBarPath(int id);
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