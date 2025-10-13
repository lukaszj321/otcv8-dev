# src/framework/util/rect.h

```cpp
else if(align == Fw::AlignTopRight) moveTopRight(r.topRight());
```
```cpp
else if(align == Fw::AlignTopCenter) moveTopCenter(r.topCenter());
```
```cpp
else if(align == Fw::AlignBottomLeft) moveBottomLeft(r.bottomLeft());
```
```cpp
else if(align == Fw::AlignBottomRight) moveBottomRight(r.bottomRight());
```
```cpp
else if(align == Fw::AlignBottomCenter) moveBottomCenter(r.bottomCenter());
```
```cpp
else if(align == Fw::AlignLeftCenter) moveCenterLeft(r.centerLeft());
```
```cpp
else if(align == Fw::AlignCenter) moveCenter(r.center());
```
```cpp
else if(align == Fw::AlignRightCenter) moveCenterRight(r.centerRight());
```
```cpp
public: TRect() : x1(0), y1(0), x2(-1), y2(-1);
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
inline T left();
```
```cpp
inline T top();
```
```cpp
inline T right();
```
```cpp
inline T bottom();
```
```cpp
inline T horizontalCenter();
```
```cpp
inline T verticalCenter();
```
```cpp
inline T x();
```
```cpp
inline T y();
```
```cpp
TPoint<T> topLeft();
```
```cpp
TPoint<T> bottomRight();
```
```cpp
TPoint<T> topRight();
```
```cpp
TPoint<T> bottomLeft();
```
```cpp
TPoint<T> topCenter();
```
```cpp
TPoint<T> bottomCenter();
```
```cpp
TPoint<T> centerLeft();
```
```cpp
TPoint<T> centerRight();
```
```cpp
TPoint<T> center();
```
```cpp
TSize<T> size();
```
```cpp
void reset();
```
```cpp
void clear();
```
```cpp
void setLeft(T pos);
```
```cpp
void setTop(T pos);
```
```cpp
void setRight(T pos);
```
```cpp
void setBottom(T pos);
```
```cpp
void setX(T x);
```
```cpp
void setY(T y);
```
```cpp
void setTopLeft(const TPoint<T> &p);
```
```cpp
void setBottomRight(const TPoint<T> &p);
```
```cpp
void setTopRight(const TPoint<T> &p);
```
```cpp
void setBottomLeft(const TPoint<T> &p);
```
```cpp
void setWidth(T width);
```
```cpp
void setHeight(T height);
```
```cpp
void setSize(const TSize<T>& size);
```
```cpp
void setRect(T x, T y, T width, T height);
```
```cpp
void setCoords(int left, int top, int right, int bottom);
```
```cpp
void expandLeft(T add);
```
```cpp
void expandTop(T add);
```
```cpp
void expandRight(T add);
```
```cpp
void expandBottom(T add);
```
```cpp
void expand(T top, T right, T bottom, T left);
```
```cpp
void expand(T add);
```
```cpp
void translate(T x, T y);
```
```cpp
void translate(const TPoint<T> &p);
```
```cpp
void resize(const TSize<T>& size);
```
```cpp
void resize(T width, T height);
```
```cpp
void move(T x, T y);
```
```cpp
void move(const TPoint<T> &p);
```
```cpp
void moveLeft(T pos);
```
```cpp
void moveTop(T pos);
```
```cpp
void moveRight(T pos);
```
```cpp
void moveBottom(T pos);
```
```cpp
void moveTopLeft(const TPoint<T> &p);
```
```cpp
void moveBottomRight(const TPoint<T> &p);
```
```cpp
void moveTopRight(const TPoint<T> &p);
```
```cpp
void moveBottomLeft(const TPoint<T> &p);
```
```cpp
void moveTopCenter(const TPoint<T> &p);
```
```cpp
void moveBottomCenter(const TPoint<T> &p);
```
```cpp
void moveCenterLeft(const TPoint<T> &p);
```
```cpp
void moveCenterRight(const TPoint<T> &p);
```
```cpp
TRect<T> translated(int x, int y);
```
```cpp
TRect<T> translated(const TPoint<T> &p);
```
```cpp
TRect<T> expanded(T add);
```
```cpp
void moveCenter(const TPoint<T> &p);
```
```cpp
void moveHorizontalCenter(T x);
```
```cpp
void moveVerticalCenter(T y);
```
```cpp
bool contains(const TPoint<T> &p, bool insideOnly = false);
```
```cpp
bool contains(const TRect<T> &r, bool insideOnly = false);
```
```cpp
bool intersects(const TRect<T> &r);
```
```cpp
TRect<T> united(const TRect<T> &r);
```
```cpp
TRect<T> intersection(const TRect<T> &r);
```
```cpp
void bind(const TRect<T> &r);
```
```cpp
void alignIn(const TRect<T> &r, Fw::AlignmentFlag align);
```
```cpp
TRect<T> operator*(float num);
```
```cpp
std::ostream& operator<<(std::ostream& out, const TRect<T>& rect);
```
```cpp
std::istream& operator>>(std::istream& in, TRect<T>& rect);
```