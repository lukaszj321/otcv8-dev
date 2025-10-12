# src/framework/graphics/shaderprogram.h

```cpp
public:
    ShaderProgram(const std::string& name);
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
static void disableAttributeArray(int location) { glDisableVertexAttribArray(location);
```
```cpp
static void enableAttributeArray(int location) { glEnableVertexAttribArray(location);
```
```cpp
void disableAttributeArray(const char* name) { glDisableVertexAttribArray(getAttributeLocation(name));
```
```cpp
void enableAttributeArray(const char* name) { glEnableVertexAttribArray(getAttributeLocation(name));
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
void setAttributeArray(int location, const float* values, int size, int stride = 0) { glVertexAttribPointer(location, size, GL_FLOAT, GL_FALSE, stride, values);
```
```cpp
void setAttributeValue(int location, float value) { glVertexAttrib1f(location, value);
```
```cpp
void setAttributeValue(int location, float x, float y) { glVertexAttrib2f(location, x, y);
```
```cpp
void setAttributeValue(int location, float x, float y, float z) { glVertexAttrib3f(location, x, y, z);
```
```cpp
void setAttributeArray(const char* name, const float* values, int size, int stride = 0) { glVertexAttribPointer(getAttributeLocation(name), size, GL_FLOAT, GL_FALSE, stride, values);
```
```cpp
void setAttributeValue(const char* name, float value) { glVertexAttrib1f(getAttributeLocation(name), value);
```
```cpp
void setAttributeValue(const char* name, float x, float y) { glVertexAttrib2f(getAttributeLocation(name), x, y);
```
```cpp
void setAttributeValue(const char* name, float x, float y, float z) { glVertexAttrib3f(getAttributeLocation(name), x, y, z);
```
```cpp
void setUniformValue(int location, const Color& color) { glUniform4f(m_uniformLocations[location], color.rF(), color.gF(), color.bF(), color.aF());
```
```cpp
void setUniformValue(int location, int value) { glUniform1i(m_uniformLocations[location], value);
```
```cpp
void setUniformValue(int location, float value) { glUniform1f(m_uniformLocations[location], value);
```
```cpp
void setUniformValue(int location, float x, float y) { glUniform2f(m_uniformLocations[location], x, y);
```
```cpp
void setUniformValue(int location, float x, float y, float z) { glUniform3f(m_uniformLocations[location], x, y, z);
```
```cpp
void setUniformValue(int location, float x, float y, float z, float w) { glUniform4f(m_uniformLocations[location], x, y, z, w);
```
```cpp
void setUniformValue(int location, const Matrix2& mat) { glUniformMatrix2fv(m_uniformLocations[location], 1, GL_FALSE, mat.data());
```
```cpp
void setUniformValue(int location, const Matrix3& mat) { glUniformMatrix3fv(m_uniformLocations[location], 1, GL_FALSE, mat.data());
```
```cpp
void setUniformValue(int location, const Matrix4& mat) { glUniformMatrix4fv(m_uniformLocations[location], 1, GL_FALSE, mat.data());
```
```cpp
void setUniformValue(int location, int count, const int* value) { glUniform1iv(m_uniformLocations[location], count, value);
```
```cpp
void setUniformValue(const char* name, const Color& color) { glUniform4f(glGetUniformLocation(m_programId, name), color.rF(), color.gF(), color.bF(), color.aF());
```
```cpp
void setUniformValue(const char* name, int value) { glUniform1i(glGetUniformLocation(m_programId, name), value);
```
```cpp
void setUniformValue(const char* name, float value) { glUniform1f(glGetUniformLocation(m_programId, name), value);
```
```cpp
void setUniformValue(const char* name, float x, float y) { glUniform2f(glGetUniformLocation(m_programId, name), x, y);
```
```cpp
void setUniformValue(const char* name, float x, float y, float z) { glUniform3f(glGetUniformLocation(m_programId, name), x, y, z);
```
```cpp
void setUniformValue(const char* name, float x, float y, float z, float w) { glUniform4f(glGetUniformLocation(m_programId, name), x, y, z, w);
```
```cpp
void setUniformValue(const char* name, const Matrix2& mat) { glUniformMatrix2fv(glGetUniformLocation(m_programId, name), 1, GL_FALSE, mat.data());
```
```cpp
void setUniformValue(const char* name, const Matrix3& mat) { glUniformMatrix3fv(glGetUniformLocation(m_programId, name), 1, GL_FALSE, mat.data());
```
```cpp
void setUniformValue(const char* name, const Matrix4& mat) { glUniformMatrix4fv(glGetUniformLocation(m_programId, name), 1, GL_FALSE, mat.data());
```