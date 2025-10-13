# src/framework/graphics/painter.h

```cpp
void bind();
```
```cpp
void unbind();
```
```cpp
void resetState();
```
```cpp
void refreshState();
```
```cpp
void saveState();
```
```cpp
void saveAndResetState();
```
```cpp
void restoreSavedState();
```
```cpp
void clear(const Color& color);
```
```cpp
void clearRect(const Color& color, const Rect& rect);
```
```cpp
void setCompositionMode(CompositionMode compositionMode);
```
```cpp
void setBlendEquation(BlendEquation blendEquation);
```
```cpp
void setDepthFunc(DepthFunc func);
```
```cpp
void setClipRect(const Rect& clipRect);
```
```cpp
void setTexture(const TexturePtr& texture);
```
```cpp
void setAlphaWriting(bool enable);
```
```cpp
void setResolution(const Size& resolution);
```
```cpp
void scale(float x, float y);
```
```cpp
void translate(float x, float y);
```
```cpp
void rotate(float angle);
```
```cpp
void rotate(float x, float y, float angle);
```
```cpp
void pushTransformMatrix();
```
```cpp
void popTransformMatrix();
```
```cpp
void drawCoords(CoordsBuffer& coordsBuffer, DrawMode drawMode = Triangles, ColorArray* colorBuffer = nullptr, const std::vector<std::pair<int, Color>>* colors = nullptr);
```
```cpp
void drawFillCoords(CoordsBuffer& coordsBuffer);
```
```cpp
void drawTextureCoords(CoordsBuffer& coordsBuffer, const TexturePtr& texture, const std::vector<std::pair<int, Color>>* colors = nullptr);
```
```cpp
void drawTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```
```cpp
void drawColorOnTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```
```cpp
void drawUpsideDownTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```
```cpp
void drawRepeatedTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```
```cpp
void drawFilledRect(const Rect& dest);
```
```cpp
void drawText(const Point& pos, CoordsBuffer& coordsBuffer, const Color& color, const TexturePtr& texture);
```
```cpp
void drawText(const Point& pos, CoordsBuffer& coordsBuffer, const std::vector<std::pair<int, Color>>& colors, const TexturePtr& texture);
```
```cpp
void drawLine(const std::vector<float>& vertex, int size, int width = 1);
```
```cpp
void setSecondTexture(const TexturePtr& texture);
```
```cpp
void setOffset(const Point& offset);
```
```cpp
void setAtlasTextures(const TexturePtr& atlas);
```
```cpp
void drawCache(const std::vector<float>& vertex, const std::vector<float>& texture, const std::vector<float>& color, int size);
```
```cpp
protected: void updateGlTexture();
```
```cpp
void updateGlCompositionMode();
```
```cpp
void updateGlBlendEquation();
```
```cpp
void updateGlClipRect();
```
```cpp
void updateGlAlphaWriting();
```
```cpp
void updateGlViewport();
```
```cpp
void updateDepthFunc();
```
```cpp
void setTransformMatrix(const Matrix3& transformMatrix);
```
```cpp
void setProjectionMatrix(const Matrix3& projectionMatrix);
```
```cpp
void setTextureMatrix(const Matrix3& textureMatrix);
```
```cpp
void setShaderProgram(PainterShaderProgram* shaderProgram);
```
```cpp
Matrix3 getTransformMatrix();
```
```cpp
Matrix3 getProjectionMatrix();
```
```cpp
Matrix3 getTextureMatrix();
```
```cpp
BlendEquation getBlendEquation();
```
```cpp
PainterShaderProgram* getShaderProgram();
```
```cpp
bool getAlphaWriting();
```
```cpp
void resetBlendEquation();
```
```cpp
void resetTexture();
```
```cpp
void resetAlphaWriting();
```
```cpp
void resetTransformMatrix();
```
```cpp
inline void drawTexturedRect(const Rect& dest, const TexturePtr& texture);
```
```cpp
void setDrawProgram(PainterShaderProgram* drawProgram);
```
```cpp
bool hasShaders();
```
```cpp
void setColor(const Color& color);
```
```cpp
void setShaderProgram(const PainterShaderProgramPtr& shaderProgram);
```
```cpp
void scale(float factor);
```
```cpp
void translate(const Point& p);
```
```cpp
void rotate(const Point& p, float angle);
```
```cpp
void setDepth(float depth);
```
```cpp
float getDepth();
```
```cpp
DepthFunc getDepthFunc();
```
```cpp
void resetDepth();
```
```cpp
void resetDepthFunc();
```
```cpp
Size getResolution();
```
```cpp
Color getColor();
```
```cpp
Rect getClipRect();
```
```cpp
CompositionMode getCompositionMode();
```
```cpp
void resetClipRect();
```
```cpp
void resetCompositionMode();
```
```cpp
void resetColor();
```
```cpp
void resetShaderProgram();
```
```cpp
int draws();
```
```cpp
int calls();
```
```cpp
void resetDraws();
```
```cpp
void setDrawColorOnTextureShaderProgram();
```
```cpp
void setMatrixColor(const Matrix4& mat4);
```
```cpp
void setDrawOutfitLayersProgram();
```