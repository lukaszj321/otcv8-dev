# src/framework/util/point.h

```cpp
return TPoint<T>(x - other.x, y - other.y).getLength();
```
```cpp
public: TPoint() : x(0), y(0);
```
```cpp
bool isNull();
```
```cpp
TSize<T> toSize();
```
```cpp
TPoint<T> operator*(const TPoint<T>& other);
```
```cpp
TPoint<T> operator*(float v);
```
```cpp
TPoint<T> operator&(int a);
```
```cpp
bool operator<(const TPoint<T>&other);
```
```cpp
bool operator>(const TPoint<T>&other);
```
```cpp
float length();
```
```cpp
float distanceFrom(const TPoint<T>& other);
```
```cpp
std::ostream& operator<<(std::ostream& out, const TPoint<T>& point);
```
```cpp
std::istream& operator>>(std::istream& in, TPoint<T>& point);
```