# src/framework/graphics/shaders/shadersources.h

```cpp
vec4 calculatePosition();
```
```cpp
void main() {\n\ gl_Position = calculatePosition();
```
```cpp
vec4 calculatePosition();
```
```cpp
void main()\n\ {\n\ gl_Position = calculatePosition();
```
```cpp
vec4 calculatePosition() {\n\ return vec4((u_ProjectionMatrix * u_TransformMatrix * vec3(a_Vertex.xy, 1.0)).xy, u_Depth / 16384.0, 1.0);
```
```cpp
vec4 calculatePixel();
```
```cpp
void main()\n\ {\n\ gl_FragColor = calculatePixel();
```
```cpp
vec4 calculatePixel() {\n\ return texture2D(u_Tex0, v_TexCoord) * u_Color;\n\ }\n"; static const std::string glslSolidColorFragmentShader = "\n\ uniform vec4 u_Color;\n\ vec4 calculatePixel() {\n\ return u_Color;\n\ }\n"; static const std::string glslSolidColorOnTextureFragmentShader = "\n\ uniform vec4 u_Color;\n\ varying vec2 v_TexCoord;\n\ uniform sampler2D u_Tex0;\n\ vec4 calculatePixel() {\n\ if(texture2D(u_Tex0, v_TexCoord).a > 0.01)\n\ return u_Color;\n\ return vec4(0,0,0,0);
```
```cpp
void main()\n\ {\n\ gl_Position = vec4((u_ProjectionMatrix * u_TransformMatrix * vec3(a_Vertex.xy, 1.0)).xy, u_Depth / 16384.0, 1.0);
```
```cpp
void main()\n\ {\n\ gl_FragColor = texture2D(u_Tex0, v_TexCoord);
```