# src/framework/graphics/paintershaderprogram.h

```cpp
virtual void setupUniforms();
```
```cpp
public:
    PainterShaderProgram(const std::string& name);
```
```cpp
bool link();
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
void setColor(const Color& color);
```
```cpp
void setMatrixColor(const Matrix4& colors);
```
```cpp
void setDepth(float depth);
```
```cpp
void setResolution(const Size& resolution);
```
```cpp
void setOffset(const Point& offset);
```
```cpp
void setCenter(const Point& center);
```
```cpp
void updateTime();
```
```cpp
void addMultiTexture(const std::string& file);
```
```cpp
void bindMultiTextures();
```
```cpp
void clearMultiTextures();
```