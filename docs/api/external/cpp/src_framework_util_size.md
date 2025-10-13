# src/framework/util/size.h

```cpp
public: TSize() : wd(-1), ht(-1);
```
```cpp
TPoint<T> toPoint();
```
```cpp
bool isNull();
```
```cpp
bool isEmpty();
```
```cpp
bool isValid();
```
```cpp
void resize(T w, T h);
```
```cpp
void setWidth(T w);
```
```cpp
void setHeight(T h);
```
```cpp
TSize<T> operator*(const TSize<T>& other);
```
```cpp
TSize<T> operator*(const float v);
```
```cpp
bool operator<(const TSize<T>&other);
```
```cpp
bool operator>(const TSize<T>&other);
```
```cpp
TSize<T> expandedTo(const TSize<T>& other);
```
```cpp
TSize<T> boundedTo(const TSize<T>& other);
```
```cpp
void scale(const TSize<T>& s, Fw::AspectRatioMode mode);
```
```cpp
void scale(int w, int h, Fw::AspectRatioMode mode);
```
```cpp
float ratio();
```
```cpp
std::ostream& operator<<(std::ostream& out, const TSize<T>& size);
```
```cpp
std::istream& operator>>(std::istream& in, TSize<T>& size);
```