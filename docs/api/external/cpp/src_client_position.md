# src/client/position.h

```cpp
return getAngleFromPositions(*this, position);
```
```cpp
return getDirectionFromPositions(*this, position);
```
```cpp
return std::to_string(x) + "," + std::to_string(y) + "," + std::to_string(z);
```
```cpp
public: Position() : x(65535), y(65535), z(255);
```
```cpp
Position translatedToDirection(Otc::Direction direction);
```
```cpp
Position translatedToReverseDirection(Otc::Direction direction);
```
```cpp
std::vector<Position> translatedToDirections(const std::vector<Otc::Direction>& dirs);
```
```cpp
static double getAngleFromPositions(const Position& fromPos, const Position& toPos);
```
```cpp
double getAngleFromPosition(const Position& position);
```
```cpp
static Otc::Direction getDirectionFromPositions(const Position& fromPos, const Position& toPos);
```
```cpp
Otc::Direction getDirectionFromPosition(const Position& position);
```
```cpp
bool isMapPosition();
```
```cpp
bool isValid();
```
```cpp
float distance(const Position& pos);
```
```cpp
int manhattanDistance(const Position& pos);
```
```cpp
void translate(int dx, int dy, short dz = 0);
```
```cpp
Position translated(int dx, int dy, short dz = 0);
```
```cpp
bool isInRange(const Position& pos, int xRange, int yRange, int zRange = 0);
```
```cpp
bool isInRange(const Position& pos, int minXRange, int maxXRange, int minYRange, int maxYRange);
```
```cpp
bool operator<(const Position& other);
```
```cpp
bool up(int n = 1);
```
```cpp
bool down(int n = 1);
```
```cpp
bool coveredUp(int n = 1);
```
```cpp
bool coveredDown(int n = 1);
```
```cpp
std::string toString();
```
```cpp
std::size_t operator()(const Position& pos);
```
```cpp
inline std::ostream& operator<<(std::ostream& out, const Position& pos);
```
```cpp
inline std::istream& operator>>(std::istream& in, Position& pos);
```