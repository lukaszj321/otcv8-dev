# src/framework/graphics/shaders/outfits.h

```text
void main()\n\ {\n\ gl_Position = vec4((u_ProjectionMatrix * u_TransformMatrix * vec3(a_Vertex.xy, 1.0)).xy, u_Depth / 16384.0, 1.0);
```
```text
void main()\n\ {\n\ gl_FragColor = texture2D(u_Tex0, v_TexCoord);
```