# src/framework/graphics/shaderprogram.h

```cpp
public: ShaderProgram(const std::string& name);
```
```cpp
static PainterShaderProgramPtr create(const std::string& name, const std::string& vertexShader, const std::string& fragmentShader, bool colorMatrix = false);
```
```cpp
bool addShader(const ShaderPtr& shader);
```
```cpp
bool addShaderFromSourceCode(Shader::ShaderType shaderType, const std::string& sourceCode);
```
```cpp
bool addShaderFromSourceFile(Shader::ShaderType shaderType, const std::string& sourceFile);
```
```cpp
void removeShader(const ShaderPtr& shader);
```
```cpp
void removeAllShaders();
```
```cpp
virtual bool link();
```
```cpp
bool bind();
```
```cpp
static void release();
```
```cpp
std::string log();
```
```cpp
int getAttributeLocation(const char* name);
```
```cpp
void bindAttributeLocation(int location, const char* name);
```
```cpp
void bindUniformLocation(int location, const char* name);
```
```cpp
static void disableAttributeArray(int location);
```
```cpp
static void enableAttributeArray(int location);
```
```cpp
void disableAttributeArray(const char* name);
```
```cpp
void enableAttributeArray(const char* name);
```
```cpp
void setAttributeArray(int location, const float* values, int size, int stride = 0);
```
```cpp
void setAttributeValue(int location, float value);
```
```cpp
void setAttributeValue(int location, float x, float y);
```
```cpp
void setAttributeValue(int location, float x, float y, float z);
```
```cpp
void setAttributeArray(const char* name, const float* values, int size, int stride = 0);
```
```cpp
void setAttributeValue(const char* name, float value);
```
```cpp
void setAttributeValue(const char* name, float x, float y);
```
```cpp
void setAttributeValue(const char* name, float x, float y, float z);
```
```cpp
void setUniformValue(int location, const Color& color);
```
```cpp
void setUniformValue(int location, int value);
```
```cpp
void setUniformValue(int location, float value);
```
```cpp
void setUniformValue(int location, float x, float y);
```
```cpp
void setUniformValue(int location, float x, float y, float z);
```
```cpp
void setUniformValue(int location, float x, float y, float z, float w);
```
```cpp
void setUniformValue(int location, const Matrix2& mat);
```
```cpp
void setUniformValue(int location, const Matrix3& mat);
```
```cpp
void setUniformValue(int location, const Matrix4& mat);
```
```cpp
void setUniformValue(int location, int count, const int* value);
```
```cpp
void setUniformValue(const char* name, const Color& color);
```
```cpp
void setUniformValue(const char* name, int value);
```
```cpp
void setUniformValue(const char* name, float value);
```
```cpp
void setUniformValue(const char* name, float x, float y);
```
```cpp
void setUniformValue(const char* name, float x, float y, float z);
```
```cpp
void setUniformValue(const char* name, float x, float y, float z, float w);
```
```cpp
void setUniformValue(const char* name, const Matrix2& mat);
```
```cpp
void setUniformValue(const char* name, const Matrix3& mat);
```
```cpp
void setUniformValue(const char* name, const Matrix4& mat);
```
```cpp
bool isLinked();
```
```cpp
uint getProgramId();
```
```cpp
ShaderList getShaders();
```
```cpp
std::string getName();
```