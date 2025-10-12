# src/framework/graphics/bitmapfont.h

```cpp
public:
    BitmapFont(const std::string& name) : m_name(name) { static int id = 1; m_id = id++; } /// Load font from otml node void load(const OTMLNodePtr& fontNode);
```
```cpp
void drawText(const std::string& text, const Point& startPos, const Color& color = Color::white, bool shadow = false);
```
Simple text render starting at startPos

```cpp
void drawText(const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align = Fw::AlignTopLeft, const Color& color = Color::white, bool shadow = false);
```
Advanced text render delimited by a screen region and alignment

```cpp
void drawColoredText(const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align, const std::vector<std::pair<int, Color>>& colors, bool shadow = false);
```
```cpp
void calculateDrawTextCoords(CoordsBuffer& coordsBuffer, const std::string& text, const Rect& screenCoords, Fw::AlignmentFlag align = Fw::AlignTopLeft);
```
```cpp
const std::vector<Point>& calculateGlyphsPositions(const std::string& text, Fw::AlignmentFlag align = Fw::AlignTopLeft, Size* textBoxSize = NULL);
```
Calculate glyphs positions to use on render, also calculates textBoxSize if wanted

```cpp
Size calculateTextRectSize(const std::string& text);
```
Simulate render and calculate text size

```cpp
std::string wrapText(const std::string& text, int maxWidth, std::vector<std::pair<int, Color>>* colors = nullptr);
```
```cpp
int getId() { return m_id; } std::string getName() { return m_name; } int getGlyphHeight() { return m_glyphHeight; } const Rect* getGlyphsTextureCoords() { return m_glyphsTextureCoords; } const Size* getGlyphsSize() { return m_glyphsSize; } const TexturePtr& getTexture() { return m_texture; } int getYOffset() { return m_yOffset; } Size getGlyphSpacing() { return m_glyphSpacing; } private: /// Calculates each font character by inspecting font bitmap void calculateGlyphsWidthsAutomatically(const ImagePtr& image, const Size& glyphSize);
```
```cpp
void updateColors(std::vector<std::pair<int, Color>>* colors, int pos, int newTextLen);
```