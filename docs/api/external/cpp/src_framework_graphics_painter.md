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
void setTransformMatrix(const Matrix3& transformMatrix) { m_transformMatrix = transformMatrix; } void setProjectionMatrix(const Matrix3& projectionMatrix) { m_projectionMatrix = projectionMatrix; } void setTextureMatrix(const Matrix3& textureMatrix) { m_textureMatrix = textureMatrix; } void setCompositionMode(CompositionMode compositionMode);
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
void setShaderProgram(PainterShaderProgram* shaderProgram) { m_shaderProgram = shaderProgram; } void setTexture(const TexturePtr& texture);
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
Matrix3 getTransformMatrix() { return m_transformMatrix; } Matrix3 getProjectionMatrix() { return m_projectionMatrix; } Matrix3 getTextureMatrix() { return m_textureMatrix; } BlendEquation getBlendEquation() { return m_blendEquation; } PainterShaderProgram* getShaderProgram() { return m_shaderProgram; } bool getAlphaWriting() { return m_alphaWriting; } void resetBlendEquation() { setBlendEquation(BlendEquation_Add);
```
```cpp
void resetTexture() { setTexture(nullptr);
```
```cpp
void resetAlphaWriting() { setAlphaWriting(true);
```
```cpp
void resetTransformMatrix() { setTransformMatrix(Matrix3());
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
inline void drawTexturedRect(const Rect& dest, const TexturePtr& texture) { drawTexturedRect(dest, texture, Rect(Point(0, 0), texture->getSize()));
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
void setDrawProgram(PainterShaderProgram* drawProgram) { m_drawProgram = drawProgram; } bool hasShaders() { return true; } void drawText(const Point& pos, CoordsBuffer& coordsBuffer, const Color& color, const TexturePtr& texture);
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
void setColor(const Color& color) { m_color = color; } void setShaderProgram(const PainterShaderProgramPtr& shaderProgram) { setShaderProgram(shaderProgram.get());
```
```cpp
void scale(float factor) { scale(factor, factor);
```
```cpp
void translate(const Point& p) { translate(p.x, p.y);
```
```cpp
void rotate(const Point& p, float angle) { rotate(p.x, p.y, angle);
```
```cpp
void setDepth(float depth) { m_depth = depth; } float getDepth() { return m_depth; } DepthFunc getDepthFunc() { return m_depthFunc; } void resetDepth() { return setDepth(0.0f);
```
```cpp
void resetDepthFunc() { setDepthFunc(DepthFunc_None);
```
```cpp
Size getResolution() { return m_resolution; } Color getColor() { return m_color; } Rect getClipRect() { return m_clipRect; } CompositionMode getCompositionMode() { return m_compositionMode; } void resetClipRect() { setClipRect(Rect());
```
```cpp
void resetCompositionMode() { setCompositionMode(CompositionMode_Normal);
```
```cpp
void resetColor() { setColor(Color::white);
```
```cpp
void resetShaderProgram() { setShaderProgram(nullptr);
```
```cpp
int draws() { return m_draws; } int calls() { return m_calls; } void resetDraws() { m_draws = m_calls = 0; } void setDrawColorOnTextureShaderProgram() { setShaderProgram(m_drawSolidColorOnTextureProgram);
```
```cpp
void setMatrixColor(const Matrix4& mat4) { m_matrixColor = mat4; } void setDrawOutfitLayersProgram() { setShaderProgram(m_drawOutfitLayersProgram);
```
```cpp
protected:
    void updateGlTexture();
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