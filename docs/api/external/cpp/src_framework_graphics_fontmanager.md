# src/framework/graphics/fontmanager.h

```cpp
public: FontManager();
```
```cpp
void terminate();
```
```cpp
void clearFonts();
```
```cpp
void importFont(std::string file);
```
```cpp
bool fontExists(const std::string& fontName);
```
```cpp
BitmapFontPtr getFont(const std::string& fontName);
```
```cpp
BitmapFontPtr getDefaultFont();
```
```cpp
void setDefaultFont(const std::string& fontName);
```