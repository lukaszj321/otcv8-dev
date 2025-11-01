---
title: "src/framework/graphics/painter.h"
source_file: "src/framework/graphics/painter.h"
generated_at: "2025-11-01T06:09:06.186Z"
doc_type: "cpp_api"
---

# src/framework/graphics/painter.h

(bind)=
## `bind`

**Signature:**
```cpp
void bind();
```

---

(unbind)=
## `unbind`

**Signature:**
```cpp
void unbind();
```

---

(resetstate)=
## `resetState`

**Signature:**
```cpp
void resetState();
```

---

(refreshstate)=
## `refreshState`

**Signature:**
```cpp
void refreshState();
```

---

(savestate)=
## `saveState`

**Signature:**
```cpp
void saveState();
```

---

(saveandresetstate)=
## `saveAndResetState`

**Signature:**
```cpp
void saveAndResetState();
```

---

(restoresavedstate)=
## `restoreSavedState`

**Signature:**
```cpp
void restoreSavedState();
```

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(clearrect)=
## `clearRect`

**Signature:**
```cpp
void clearRect(const Color& color, const Rect& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |
| `const Rect&` | `rect` | - |

---

(setcompositionmode)=
## `setCompositionMode`

**Signature:**
```cpp
void setCompositionMode(CompositionMode compositionMode);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `CompositionMode` | `compositionMode` | - |

---

(setblendequation)=
## `setBlendEquation`

**Signature:**
```cpp
void setBlendEquation(BlendEquation blendEquation);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `BlendEquation` | `blendEquation` | - |

---

(setdepthfunc)=
## `setDepthFunc`

**Signature:**
```cpp
void setDepthFunc(DepthFunc func);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `DepthFunc` | `func` | - |

---

(setcliprect)=
## `setClipRect`

**Signature:**
```cpp
void setClipRect(const Rect& clipRect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `clipRect` | - |

---

(settexture)=
## `setTexture`

**Signature:**
```cpp
void setTexture(const TexturePtr& texture);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TexturePtr&` | `texture` | - |

---

(setalphawriting)=
## `setAlphaWriting`

**Signature:**
```cpp
void setAlphaWriting(bool enable);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `bool` | `enable` | - |

---

(setresolution)=
## `setResolution`

**Signature:**
```cpp
void setResolution(const Size& resolution);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Size&` | `resolution` | - |

---

(scale)=
## `scale`

**Signature:**
```cpp
void scale(float x, float y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `x` | - |
| `float` | `y` | - |

---

(translate)=
## `translate`

**Signature:**
```cpp
void translate(float x, float y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `x` | - |
| `float` | `y` | - |

---

(rotate)=
## `rotate`

**Signature:**
```cpp
void rotate(float angle);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `angle` | - |

---

(rotate-1)=
## `rotate`

**Signature:**
```cpp
void rotate(float x, float y, float angle);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `x` | - |
| `float` | `y` | - |
| `float` | `angle` | - |

---

(pushtransformmatrix)=
## `pushTransformMatrix`

**Signature:**
```cpp
void pushTransformMatrix();
```

---

(poptransformmatrix)=
## `popTransformMatrix`

**Signature:**
```cpp
void popTransformMatrix();
```

---

(drawcoords)=
## `drawCoords`

**Signature:**
```cpp
void drawCoords(CoordsBuffer& coordsBuffer, DrawMode drawMode = Triangles, ColorArray* colorBuffer = nullptr, const std::vector<std::pair<int, Color>>* colors = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `CoordsBuffer&` | `coordsBuffer` |  | - |
| `DrawMode` | `drawMode` | `Triangles` | - |
| `ColorArray*` | `colorBuffer` | `nullptr` | - |
| `const std::vector&lt;std::pair&lt;int, Color&gt;&gt;*` | `colors` | `nullptr` | - |

---

(drawfillcoords)=
## `drawFillCoords`

**Signature:**
```cpp
void drawFillCoords(CoordsBuffer& coordsBuffer);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `CoordsBuffer&` | `coordsBuffer` | - |

---

(drawtexturecoords)=
## `drawTextureCoords`

**Signature:**
```cpp
void drawTextureCoords(CoordsBuffer& coordsBuffer, const TexturePtr& texture, const std::vector<std::pair<int, Color>>* colors = nullptr);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `CoordsBuffer&` | `coordsBuffer` |  | - |
| `const TexturePtr&` | `texture` |  | - |
| `const std::vector&lt;std::pair&lt;int, Color&gt;&gt;*` | `colors` | `nullptr` | - |

---

(drawtexturedrect)=
## `drawTexturedRect`

**Signature:**
```cpp
void drawTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const TexturePtr&` | `texture` | - |
| `const Rect&` | `src` | - |

---

(drawcolorontexturedrect)=
## `drawColorOnTexturedRect`

**Signature:**
```cpp
void drawColorOnTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const TexturePtr&` | `texture` | - |
| `const Rect&` | `src` | - |

---

(drawupsidedowntexturedrect)=
## `drawUpsideDownTexturedRect`

**Signature:**
```cpp
void drawUpsideDownTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const TexturePtr&` | `texture` | - |
| `const Rect&` | `src` | - |

---

(drawrepeatedtexturedrect)=
## `drawRepeatedTexturedRect`

**Signature:**
```cpp
void drawRepeatedTexturedRect(const Rect& dest, const TexturePtr& texture, const Rect& src);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const TexturePtr&` | `texture` | - |
| `const Rect&` | `src` | - |

---

(drawfilledrect)=
## `drawFilledRect`

**Signature:**
```cpp
void drawFilledRect(const Rect& dest);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |

---

(drawtext)=
## `drawText`

**Signature:**
```cpp
void drawText(const Point& pos, CoordsBuffer& coordsBuffer, const Color& color, const TexturePtr& texture);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |
| `CoordsBuffer&` | `coordsBuffer` | - |
| `const Color&` | `color` | - |
| `const TexturePtr&` | `texture` | - |

---

(drawtext-1)=
## `drawText`

**Signature:**
```cpp
void drawText(const Point& pos, CoordsBuffer& coordsBuffer, const std::vector<std::pair<int, Color>>& colors, const TexturePtr& texture);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `pos` | - |
| `CoordsBuffer&` | `coordsBuffer` | - |
| `const std::vector&lt;std::pair&lt;int, Color&gt;&gt;&` | `colors` | - |
| `const TexturePtr&` | `texture` | - |

---

(drawline)=
## `drawLine`

**Signature:**
```cpp
void drawLine(const std::vector<float>& vertex, int size, int width = 1);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const std::vector&lt;float&gt;&` | `vertex` |  | - |
| `int` | `size` |  | - |
| `int` | `width` | `1` | - |

---

(setsecondtexture)=
## `setSecondTexture`

**Signature:**
```cpp
void setSecondTexture(const TexturePtr& texture);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TexturePtr&` | `texture` | - |

---

(setoffset)=
## `setOffset`

**Signature:**
```cpp
void setOffset(const Point& offset);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `offset` | - |

---

(setatlastextures)=
## `setAtlasTextures`

**Signature:**
```cpp
void setAtlasTextures(const TexturePtr& atlas);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TexturePtr&` | `atlas` | - |

---

(drawcache)=
## `drawCache`

**Signature:**
```cpp
void drawCache(const std::vector<float>& vertex, const std::vector<float>& texture, const std::vector<float>& color, int size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const std::vector&lt;float&gt;&` | `vertex` | - |
| `const std::vector&lt;float&gt;&` | `texture` | - |
| `const std::vector&lt;float&gt;&` | `color` | - |
| `int` | `size` | - |

---

(updategltexture)=
## `updateGlTexture`

**Signature:**
```cpp
protected: void updateGlTexture();
```

---

(updateglcompositionmode)=
## `updateGlCompositionMode`

**Signature:**
```cpp
void updateGlCompositionMode();
```

---

(updateglblendequation)=
## `updateGlBlendEquation`

**Signature:**
```cpp
void updateGlBlendEquation();
```

---

(updateglcliprect)=
## `updateGlClipRect`

**Signature:**
```cpp
void updateGlClipRect();
```

---

(updateglalphawriting)=
## `updateGlAlphaWriting`

**Signature:**
```cpp
void updateGlAlphaWriting();
```

---

(updateglviewport)=
## `updateGlViewport`

**Signature:**
```cpp
void updateGlViewport();
```

---

(updatedepthfunc)=
## `updateDepthFunc`

**Signature:**
```cpp
void updateDepthFunc();
```

---

(settransformmatrix)=
## `setTransformMatrix`

**Signature:**
```cpp
void setTransformMatrix(const Matrix3& transformMatrix);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix3&` | `transformMatrix` | - |

---

(setprojectionmatrix)=
## `setProjectionMatrix`

**Signature:**
```cpp
void setProjectionMatrix(const Matrix3& projectionMatrix);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix3&` | `projectionMatrix` | - |

---

(settexturematrix)=
## `setTextureMatrix`

**Signature:**
```cpp
void setTextureMatrix(const Matrix3& textureMatrix);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix3&` | `textureMatrix` | - |

---

(setshaderprogram)=
## `setShaderProgram`

**Signature:**
```cpp
void setShaderProgram(PainterShaderProgram* shaderProgram);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `PainterShaderProgram*` | `shaderProgram` | - |

---

(gettransformmatrix)=
## `getTransformMatrix`

**Signature:**
```cpp
Matrix3 getTransformMatrix();
```

**Returns:**
- `Matrix3`

---

(getprojectionmatrix)=
## `getProjectionMatrix`

**Signature:**
```cpp
Matrix3 getProjectionMatrix();
```

**Returns:**
- `Matrix3`

---

(gettexturematrix)=
## `getTextureMatrix`

**Signature:**
```cpp
Matrix3 getTextureMatrix();
```

**Returns:**
- `Matrix3`

---

(getblendequation)=
## `getBlendEquation`

**Signature:**
```cpp
BlendEquation getBlendEquation();
```

**Returns:**
- `BlendEquation`

---

(getshaderprogram)=
## `getShaderProgram`

**Signature:**
```cpp
PainterShaderProgram* getShaderProgram();
```

**Returns:**
- `PainterShaderProgram*`

---

(getalphawriting)=
## `getAlphaWriting`

**Signature:**
```cpp
bool getAlphaWriting();
```

**Returns:**
- `bool`

---

(resetblendequation)=
## `resetBlendEquation`

**Signature:**
```cpp
void resetBlendEquation();
```

---

(resettexture)=
## `resetTexture`

**Signature:**
```cpp
void resetTexture();
```

---

(resetalphawriting)=
## `resetAlphaWriting`

**Signature:**
```cpp
void resetAlphaWriting();
```

---

(resettransformmatrix)=
## `resetTransformMatrix`

**Signature:**
```cpp
void resetTransformMatrix();
```

---

(drawtexturedrect-1)=
## `drawTexturedRect`

**Signature:**
```cpp
inline void drawTexturedRect(const Rect& dest, const TexturePtr& texture);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Rect&` | `dest` | - |
| `const TexturePtr&` | `texture` | - |

---

(setdrawprogram)=
## `setDrawProgram`

**Signature:**
```cpp
void setDrawProgram(PainterShaderProgram* drawProgram);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `PainterShaderProgram*` | `drawProgram` | - |

---

(hasshaders)=
## `hasShaders`

**Signature:**
```cpp
bool hasShaders();
```

**Returns:**
- `bool`

---

(setcolor)=
## `setColor`

**Signature:**
```cpp
void setColor(const Color& color);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Color&` | `color` | - |

---

(setshaderprogram-1)=
## `setShaderProgram`

**Signature:**
```cpp
void setShaderProgram(const PainterShaderProgramPtr& shaderProgram);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const PainterShaderProgramPtr&` | `shaderProgram` | - |

---

(scale-1)=
## `scale`

**Signature:**
```cpp
void scale(float factor);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `factor` | - |

---

(translate-1)=
## `translate`

**Signature:**
```cpp
void translate(const Point& p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `p` | - |

---

(rotate-2)=
## `rotate`

**Signature:**
```cpp
void rotate(const Point& p, float angle);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Point&` | `p` | - |
| `float` | `angle` | - |

---

(setdepth)=
## `setDepth`

**Signature:**
```cpp
void setDepth(float depth);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `depth` | - |

---

(getdepth)=
## `getDepth`

**Signature:**
```cpp
float getDepth();
```

**Returns:**
- `float`

---

(getdepthfunc)=
## `getDepthFunc`

**Signature:**
```cpp
DepthFunc getDepthFunc();
```

**Returns:**
- `DepthFunc`

---

(resetdepth)=
## `resetDepth`

**Signature:**
```cpp
void resetDepth();
```

---

(resetdepthfunc)=
## `resetDepthFunc`

**Signature:**
```cpp
void resetDepthFunc();
```

---

(getresolution)=
## `getResolution`

**Signature:**
```cpp
Size getResolution();
```

**Returns:**
- `Size`

---

(getcolor)=
## `getColor`

**Signature:**
```cpp
Color getColor();
```

**Returns:**
- `Color`

---

(getcliprect)=
## `getClipRect`

**Signature:**
```cpp
Rect getClipRect();
```

**Returns:**
- `Rect`

---

(getcompositionmode)=
## `getCompositionMode`

**Signature:**
```cpp
CompositionMode getCompositionMode();
```

**Returns:**
- `CompositionMode`

---

(resetcliprect)=
## `resetClipRect`

**Signature:**
```cpp
void resetClipRect();
```

---

(resetcompositionmode)=
## `resetCompositionMode`

**Signature:**
```cpp
void resetCompositionMode();
```

---

(resetcolor)=
## `resetColor`

**Signature:**
```cpp
void resetColor();
```

---

(resetshaderprogram)=
## `resetShaderProgram`

**Signature:**
```cpp
void resetShaderProgram();
```

---

(draws)=
## `draws`

**Signature:**
```cpp
int draws();
```

**Returns:**
- `int`

---

(calls)=
## `calls`

**Signature:**
```cpp
int calls();
```

**Returns:**
- `int`

---

(resetdraws)=
## `resetDraws`

**Signature:**
```cpp
void resetDraws();
```

---

(setdrawcolorontextureshaderprogram)=
## `setDrawColorOnTextureShaderProgram`

**Signature:**
```cpp
void setDrawColorOnTextureShaderProgram();
```

---

(setmatrixcolor)=
## `setMatrixColor`

**Signature:**
```cpp
void setMatrixColor(const Matrix4& mat4);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const Matrix4&` | `mat4` | - |

---

(setdrawoutfitlayersprogram)=
## `setDrawOutfitLayersProgram`

**Signature:**
```cpp
void setDrawOutfitLayersProgram();
```

---
