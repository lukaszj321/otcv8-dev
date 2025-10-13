# src/client/minimap.h

```cpp
public: void clean();
```
```cpp
void update();
```
```cpp
void updateTile(int x, int y, const MinimapTile& tile);
```
```cpp
public: void init();
```
```cpp
void terminate();
```
```cpp
void clean();
```
```cpp
void draw(const Rect& screenRect, const Position& mapCenter, float scale, const Color& color);
```
```cpp
Point getTilePoint(const Position& pos, const Rect& screenRect, const Position& mapCenter, float scale);
```
```cpp
Position getTilePosition(const Point& point, const Rect& screenRect, const Position& mapCenter, float scale);
```
```cpp
Rect getTileRect(const Position& pos, const Rect& screenRect, const Position& mapCenter, float scale);
```
```cpp
void updateTile(const Position& pos, const TilePtr& tile);
```
```cpp
const MinimapTile& getTile(const Position& pos);
```
```cpp
bool loadImage(const std::string& fileName, const Position& topLeft, float colorFactor);
```
```cpp
void saveImage(const std::string& fileName, const Rect& mapRect);
```
```cpp
bool loadOtmm(const std::string& fileName);
```
```cpp
void saveOtmm(const std::string& fileName);
```
```cpp
private: Rect calcMapRect(const Rect& screenRect, const Position& mapCenter, float scale);
```
```cpp
std::lock_guard<std::mutex> lock(m_lock);
```
```cpp
bool hasFlag(MinimapTileFlags flag);
```
```cpp
int getSpeed();
```
```cpp
MinimapTile& getTile(int x, int y);
```
```cpp
void resetTile(int x, int y);
```
```cpp
uint getTileIndex(int x, int y);
```
```cpp
const TexturePtr& getTexture();
```
```cpp
void mustUpdate();
```
```cpp
void justSaw();
```
```cpp
bool wasSeen();
```
```cpp
bool hasBlock(const Position& pos);
```
```cpp
MinimapBlock& getBlock(const Position& pos);
```
```cpp
Point getBlockOffset(const Point& pos);
```
```cpp
Position getIndexPosition(int index, int z);
```
```cpp
uint getBlockIndex(const Position& pos);
```