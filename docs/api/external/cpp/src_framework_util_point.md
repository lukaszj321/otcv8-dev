# src/framework/util/point.h

```cpp
public:
    TPoint() : x(0), y(0) {} TPoint(T x, T y) : x(x), y(y) { } TPoint(const TPoint<T>& other) : x(other.x), y(other.y) { } bool isNull() const { return x==0 && y==0; } TSize<T> toSize() const { return TSize<T>(x, y);
```
```cpp
float length() const { return sqrt((float)(x*x + y*y));
```
```cpp
float distanceFrom(const TPoint<T>& other) const { return TPoint<T>(x - other.x, y - other.y).getLength();
```