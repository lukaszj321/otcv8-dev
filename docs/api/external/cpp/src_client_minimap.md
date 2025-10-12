# src/client/minimap.h

```cpp
bool hasFlag(MinimapTileFlags flag) const { return flags & flag; } int getSpeed() const { return speed * 10; } bool operator==(const MinimapTile& other) const { return color == other.color && flags == other.flags && speed == other.speed; } bool operator!=(const MinimapTile& other) const { return !(*this == other);
```
```cpp
public:
    void clean();
```
```cpp
void update();
```
```cpp
void updateTile(int x, int y, const MinimapTile& tile);
```
```cpp
MinimapTile& getTile(int x, int y) { return m_tiles[getTileIndex(x,y)]; } void resetTile(int x, int y) { m_tiles[getTileIndex(x,y)] = MinimapTile();
```
```cpp
uint getTileIndex(int x, int y) { return ((y % MMBLOCK_SIZE) * MMBLOCK_SIZE) + (x % MMBLOCK_SIZE);
```
```cpp
const TexturePtr& getTexture() { return m_texture; } std::array<MinimapTile, MMBLOCK_SIZE * MMBLOCK_SIZE>& getTiles() { return m_tiles; } void mustUpdate() { m_mustUpdate = true; } void justSaw() { m_wasSeen = true; } bool wasSeen() { return m_wasSeen; } private: TexturePtr m_texture; std::array<MinimapTile, MMBLOCK_SIZE * MMBLOCK_SIZE> m_tiles; stdext::boolean<true> m_mustUpdate; stdext::boolean<false> m_wasSeen; }; #pragma pack(pop) using MinimapBlock_ptr = std::shared_ptr<MinimapBlock>; class Minimap { public: void init();
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
private:
    Rect calcMapRect(const Rect& screenRect, const Position& mapCenter, float scale);
```
```cpp
bool hasBlock(const Position& pos) { return m_tileBlocks[pos.z].find(getBlockIndex(pos)) != m_tileBlocks[pos.z].end();
```
```cpp
MinimapBlock& getBlock(const Position& pos) { std::lock_guard<std::mutex> lock(m_lock);
```
```cpp
Point getBlockOffset(const Point& pos) { return Point(pos.x - pos.x % MMBLOCK_SIZE, pos.y - pos.y % MMBLOCK_SIZE);
```
```cpp
Position getIndexPosition(int index, int z) { return Position((index % (65536 / MMBLOCK_SIZE))*MMBLOCK_SIZE, (index / (65536 / MMBLOCK_SIZE))*MMBLOCK_SIZE, z);
```
```cpp
uint getBlockIndex(const Position& pos) { return ((pos.y / MMBLOCK_SIZE) * (65536 / MMBLOCK_SIZE)) + (pos.x / MMBLOCK_SIZE);
```