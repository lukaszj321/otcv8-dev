---
title: "src/client/position.h"
source_file: "src/client/position.h"
generated_at: "2025-10-31T23:33:30.325Z"
doc_type: "cpp_api"
---

# src/client/position.h

(getanglefrompositions)=
## `getAngleFromPositions`

**Signature:**
```cpp
return getAngleFromPositions(*this, position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `*` | `this` | - |
| `` | `position` | - |

**Returns:**
- `return`

---

(getdirectionfrompositions)=
## `getDirectionFromPositions`

**Signature:**
```cpp
return getDirectionFromPositions(*this, position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `*` | `this` | - |
| `` | `position` | - |

**Returns:**
- `return`

---

(stdto_string)=
## `std::to_string`

**Signature:**
```cpp
return std::to_string(x) + "," + std::to_string(y) + "," + std::to_string(z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |
| `int` | `z` | - |

**Returns:**
- `return`

---

(position)=
## `Position`

**Signature:**
```cpp
public: Position() : x(65535), y(65535), z(255);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `) : x(65535)` | - | - |
| `y(65535)` | - | - |
| `z(255` | - | - |

**Returns:**
- `public:`

---

(translatedtodirection)=
## `translatedToDirection`

**Signature:**
```cpp
Position translatedToDirection(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

**Returns:**
- `Position`

---

(translatedtoreversedirection)=
## `translatedToReverseDirection`

**Signature:**
```cpp
Position translatedToReverseDirection(Otc::Direction direction);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `Otc::Direction` | `direction` | - |

**Returns:**
- `Position`

---

(translatedtodirections)=
## `translatedToDirections`

**Signature:**
```cpp
std::vector<Position> translatedToDirections(const std::vector<Otc::Direction>& dirs);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;Otc::Direction&gt;&` | `dirs` | - |

**Returns:**
- `std::vector&lt;Position&gt;`

---

(getanglefrompositions)=
## `getAngleFromPositions`

**Signature:**
```cpp
static double getAngleFromPositions(const Position& fromPos, const Position& toPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `fromPos` | - |
| `const Position&` | `toPos` | - |

**Returns:**
- `static double`

---

(getanglefromposition)=
## `getAngleFromPosition`

**Signature:**
```cpp
double getAngleFromPosition(const Position& position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |

**Returns:**
- `double`

---

(getdirectionfrompositions)=
## `getDirectionFromPositions`

**Signature:**
```cpp
static Otc::Direction getDirectionFromPositions(const Position& fromPos, const Position& toPos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `fromPos` | - |
| `const Position&` | `toPos` | - |

**Returns:**
- `static Otc::Direction`

---

(getdirectionfromposition)=
## `getDirectionFromPosition`

**Signature:**
```cpp
Otc::Direction getDirectionFromPosition(const Position& position);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `position` | - |

**Returns:**
- `Otc::Direction`

---

(ismapposition)=
## `isMapPosition`

**Signature:**
```cpp
bool isMapPosition();
```

**Returns:**
- `bool`

---

(isvalid)=
## `isValid`

**Signature:**
```cpp
bool isValid();
```

**Returns:**
- `bool`

---

(distance)=
## `distance`

**Signature:**
```cpp
float distance(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `float`

---

(manhattandistance)=
## `manhattanDistance`

**Signature:**
```cpp
int manhattanDistance(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `int`

---

(translate)=
## `translate`

**Signature:**
```cpp
void translate(int dx, int dy, short dz = 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `dx` | - |
| `int` | `dy` | - |
| `short dz = 0` | - | - |

---

(translated)=
## `translated`

**Signature:**
```cpp
Position translated(int dx, int dy, short dz = 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `dx` | - |
| `int` | `dy` | - |
| `short dz = 0` | - | - |

**Returns:**
- `Position`

---

(isinrange)=
## `isInRange`

**Signature:**
```cpp
bool isInRange(const Position& pos, int xRange, int yRange, int zRange = 0);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `xRange` | - |
| `int` | `yRange` | - |
| `int zRange = 0` | - | - |

**Returns:**
- `bool`

---

(isinrange)=
## `isInRange`

**Signature:**
```cpp
bool isInRange(const Position& pos, int minXRange, int maxXRange, int minYRange, int maxYRange);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `int` | `minXRange` | - |
| `int` | `maxXRange` | - |
| `int` | `minYRange` | - |
| `int` | `maxYRange` | - |

**Returns:**
- `bool`

---

(operator)=
## `operator<`

**Signature:**
```cpp
bool operator<(const Position& other);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `other` | - |

**Returns:**
- `bool`

---

(up)=
## `up`

**Signature:**
```cpp
bool up(int n = 1);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int n = 1` | - | - |

**Returns:**
- `bool`

---

(down)=
## `down`

**Signature:**
```cpp
bool down(int n = 1);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int n = 1` | - | - |

**Returns:**
- `bool`

---

(coveredup)=
## `coveredUp`

**Signature:**
```cpp
bool coveredUp(int n = 1);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int n = 1` | - | - |

**Returns:**
- `bool`

---

(covereddown)=
## `coveredDown`

**Signature:**
```cpp
bool coveredDown(int n = 1);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int n = 1` | - | - |

**Returns:**
- `bool`

---

(tostring)=
## `toString`

**Signature:**
```cpp
std::string toString();
```

**Returns:**
- `std::string`

---

(operator)=
## `operator`

**Signature:**
```cpp
std::size_t operator()(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `)(const Position&` | `pos` | - |

**Returns:**
- `std::size_t`

---

(operator)=
## `operator<<`

**Signature:**
```cpp
inline std::ostream& operator<<(std::ostream& out, const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostream&` | `out` | - |
| `const Position&` | `pos` | - |

**Returns:**
- `inline std::ostream&`

---

(operator)=
## `operator>>`

**Signature:**
```cpp
inline std::istream& operator>>(std::istream& in, Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream&` | `in` | - |
| `Position&` | `pos` | - |

**Returns:**
- `inline std::istream&`

---
