# src/framework/graphics/apngloader.h

```cpp
int load_apng(std::stringstream& file, struct apng_data *apng);
```
```cpp
void save_png(std::stringstream& file, unsigned int width, unsigned int height, int channels, unsigned char *pixels);
```
```cpp
void free_apng(struct apng_data *apng);
```