---
title: "src/client/minimap.h"
source_file: "src/client/minimap.h"
generated_at: "2025-11-01T08:29:23.681Z"
doc_type: "cpp_api"
---

# src/client/minimap.h

(clean)=
## `clean`

**Signature:**
```cpp
public: void clean();
```

---

(update)=
## `update`

**Signature:**
```cpp
void update();
```

---

(updatetile)=
## `updateTile`

**Signature:**
```cpp
void updateTile(int x, int y, const MinimapTile& tile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |
| `const MinimapTile&` | `tile` | - |

---

(init)=
## `init`

**Signature:**
```cpp
public: void init();
```

---

(terminate)=
## `terminate`

**Signature:**
```cpp
void terminate();
```

---

(clean-1)=
## `clean`

**Signature:**
```cpp
void clean();
```

---

(draw)=
## `draw`

**Signature:**
```cpp
void draw(const Rect& screenRect, const Position& mapCenter, float scale, const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `screenRect` | - |
| `const Position&` | `mapCenter` | - |
| `float` | `scale` | - |
| `const Color&` | `color` | - |

---

(gettilepoint)=
## `getTilePoint`

**Signature:**
```cpp
Point getTilePoint(const Position& pos, const Rect& screenRect, const Position& mapCenter, float scale);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `const Rect&` | `screenRect` | - |
| `const Position&` | `mapCenter` | - |
| `float` | `scale` | - |

**Returns:**
- `Point`

---

(gettileposition)=
## `getTilePosition`

**Signature:**
```cpp
Position getTilePosition(const Point& point, const Rect& screenRect, const Position& mapCenter, float scale);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `point` | - |
| `const Rect&` | `screenRect` | - |
| `const Position&` | `mapCenter` | - |
| `float` | `scale` | - |

**Returns:**
- `Position`

---

(gettilerect)=
## `getTileRect`

**Signature:**
```cpp
Rect getTileRect(const Position& pos, const Rect& screenRect, const Position& mapCenter, float scale);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `const Rect&` | `screenRect` | - |
| `const Position&` | `mapCenter` | - |
| `float` | `scale` | - |

**Returns:**
- `Rect`

---

(updatetile-1)=
## `updateTile`

**Signature:**
```cpp
void updateTile(const Position& pos, const TilePtr& tile);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |
| `const TilePtr&` | `tile` | - |

---

(gettile)=
## `getTile`

**Signature:**
```cpp
const MinimapTile& getTile(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `const MinimapTile&`

---

(loadimage)=
## `loadImage`

**Signature:**
```cpp
bool loadImage(const std::string& fileName, const Position& topLeft, float colorFactor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |
| `const Position&` | `topLeft` | - |
| `float` | `colorFactor` | - |

**Returns:**
- `bool`

---

(saveimage)=
## `saveImage`

**Signature:**
```cpp
void saveImage(const std::string& fileName, const Rect& mapRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |
| `const Rect&` | `mapRect` | - |

---

(loadotmm)=
## `loadOtmm`

**Signature:**
```cpp
bool loadOtmm(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

**Returns:**
- `bool`

---

(saveotmm)=
## `saveOtmm`

**Signature:**
```cpp
void saveOtmm(const std::string& fileName);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::string&` | `fileName` | - |

---

(calcmaprect)=
## `calcMapRect`

**Signature:**
```cpp
private: Rect calcMapRect(const Rect& screenRect, const Position& mapCenter, float scale);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `screenRect` | - |
| `const Position&` | `mapCenter` | - |
| `float` | `scale` | - |

**Returns:**
- `Rect`

---

(lock)=
## `lock`

**Signature:**
```cpp
std::lock_guard<std::mutex> lock(m_lock);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `m_lock` | - | - |

**Returns:**
- `std::lock_guard&lt;std::mutex&gt;`

---

(hasflag)=
## `hasFlag`

**Signature:**
```cpp
bool hasFlag(MinimapTileFlags flag);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `MinimapTileFlags` | `flag` | - |

**Returns:**
- `bool`

---

(getspeed)=
## `getSpeed`

**Signature:**
```cpp
int getSpeed();
```

**Returns:**
- `int`

---

(gettile-1)=
## `getTile`

**Signature:**
```cpp
MinimapTile& getTile(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

**Returns:**
- `MinimapTile&`

---

(resettile)=
## `resetTile`

**Signature:**
```cpp
void resetTile(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

---

(gettileindex)=
## `getTileIndex`

**Signature:**
```cpp
uint getTileIndex(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

**Returns:**
- `uint`

---

(gettexture)=
## `getTexture`

**Signature:**
```cpp
const TexturePtr& getTexture();
```

**Returns:**
- `const TexturePtr&`

---

(mustupdate)=
## `mustUpdate`

**Signature:**
```cpp
void mustUpdate();
```

---

(justsaw)=
## `justSaw`

**Signature:**
```cpp
void justSaw();
```

---

(wasseen)=
## `wasSeen`

**Signature:**
```cpp
bool wasSeen();
```

**Returns:**
- `bool`

---

(hasblock)=
## `hasBlock`

**Signature:**
```cpp
bool hasBlock(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `bool`

---

(getblock)=
## `getBlock`

**Signature:**
```cpp
MinimapBlock& getBlock(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `MinimapBlock&`

---

(getblockoffset)=
## `getBlockOffset`

**Signature:**
```cpp
Point getBlockOffset(const Point& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |

**Returns:**
- `Point`

---

(getindexposition)=
## `getIndexPosition`

**Signature:**
```cpp
Position getIndexPosition(int index, int z);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `index` | - |
| `int` | `z` | - |

**Returns:**
- `Position`

---

(getblockindex)=
## `getBlockIndex`

**Signature:**
```cpp
uint getBlockIndex(const Position& pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Position&` | `pos` | - |

**Returns:**
- `uint`

---
