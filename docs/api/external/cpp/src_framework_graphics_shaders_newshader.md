# src/framework/graphics/shaders/newshader.h

```cpp
void main()\n\ {\n\ gl_Position = vec4((u_ProjectionMatrix * u_TransformMatrix * vec3(a_Vertex.xy, 1.0)).xy, 1.0, 1.0);
```
```cpp
void main()\n\ {\n\ gl_Position = vec4((u_ProjectionMatrix * u_TransformMatrix * vec3(a_Vertex.xy + u_Offset, 1.0)).xy, 1.0, 1.0);
```
```cpp
void main()\n\ {\n\ gl_Position = vec4((u_ProjectionMatrix * u_TransformMatrix * vec3(a_Vertex.xy, 1.0)).xy, 1.0, 1.0);
```