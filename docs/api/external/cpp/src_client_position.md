# src/client/position.h

```cpp
public:
    Position() : x(65535), y(65535), z(255) { } Position(uint16 x, uint16 y, uint8 z) : x(x), y(y), z(z) { } Position translatedToDirection(Otc::Direction direction) { Position pos = *this; switch(direction) { case Otc::North: pos.y--; break; case Otc::East: pos.x++; break; case Otc::South: pos.y++; break; case Otc::West: pos.x--; break; case Otc::NorthEast: pos.x++; pos.y--; break; case Otc::SouthEast: pos.x++; pos.y++; break; case Otc::SouthWest: pos.x--; pos.y++; break; case Otc::NorthWest: pos.x--; pos.y--; break; default: break; } return pos; } Position translatedToReverseDirection(Otc::Direction direction) { Position pos = *this; switch(direction) { case Otc::North: pos.y++; break; case Otc::East: pos.x--; break; case Otc::South: pos.y--; break; case Otc::West: pos.x++; break; case Otc::NorthEast: pos.x--; pos.y++; break; case Otc::SouthEast: pos.x--; pos.y--; break; case Otc::SouthWest: pos.x++; pos.y--; break; case Otc::NorthWest: pos.x++; pos.y++; break; default: break; } return pos; } std::vector<Position> translatedToDirections(const std::vector<Otc::Direction>& dirs) const { Position lastPos = *this; std::vector<Position> positions; if(!lastPos.isValid()) return positions; positions.push_back(lastPos);
```
```cpp
static double getAngleFromPositions(const Position& fromPos, const Position& toPos) { // Returns angle in radians from 0 to 2Pi. -1 means positions are equal. int dx = toPos.x - fromPos.x; int dy = toPos.y - fromPos.y; if(dx == 0 && dy == 0) return -1; float angle = std::atan2(dy * -1, dx);
```
```cpp
double getAngleFromPosition(const Position& position) const { return getAngleFromPositions(*this, position);
```
```cpp
static Otc::Direction getDirectionFromPositions(const Position& fromPos, const Position& toPos) { float angle = getAngleFromPositions(fromPos, toPos) * RAD_TO_DEC; if(angle >= 360 - 22.5 || angle < 0 + 22.5) return Otc::East; else if(angle >= 45 - 22.5 && angle < 45 + 22.5) return Otc::NorthEast; else if(angle >= 90 - 22.5 && angle < 90 + 22.5) return Otc::North; else if(angle >= 135 - 22.5 && angle < 135 + 22.5) return Otc::NorthWest; else if(angle >= 180 - 22.5 && angle < 180 + 22.5) return Otc::West; else if(angle >= 225 - 22.5 && angle < 225 + 22.5) return Otc::SouthWest; else if(angle >= 270 - 22.5 && angle < 270 + 22.5) return Otc::South; else if(angle >= 315 - 22.5 && angle < 315 + 22.5) return Otc::SouthEast; else return Otc::InvalidDirection; } Otc::Direction getDirectionFromPosition(const Position& position) const { return getDirectionFromPositions(*this, position);
```
```cpp
bool isMapPosition() const { return (x >=0 && y >= 0 && z >= 0 && x < 65535 && y < 65535 && z <= Otc::MAX_Z);
```
```cpp
bool isValid() const { return !(x == 65535 && y == 65535 && z == 255);
```
```cpp
float distance(const Position& pos) const { return sqrt(pow((pos.x - x), 2) + pow((pos.y - y), 2));
```
```cpp
int manhattanDistance(const Position& pos) const { return std::abs(pos.x - x) + std::abs(pos.y - y);
```
```cpp
void translate(int dx, int dy, short dz = 0) { x += dx; y += dy; z += dz; } Position translated(int dx, int dy, short dz = 0) const { Position pos = *this; pos.x += dx; pos.y += dy; pos.z += dz; return pos; } Position operator+(const Position& other) const { return Position(x + other.x, y + other.y, z + other.z);
```
```cpp
bool isInRange(const Position& pos, int xRange, int yRange, int zRange = 0) const { return std::abs(x-pos.x) <= xRange && std::abs(y-pos.y) <= yRange && std::abs(z - pos.z) <= zRange; } bool isInRange(const Position& pos, int minXRange, int maxXRange, int minYRange, int maxYRange) const { return (pos.x >= x-minXRange && pos.x <= x+maxXRange && pos.y >= y-minYRange && pos.y <= y+maxYRange && pos.z == z);
```