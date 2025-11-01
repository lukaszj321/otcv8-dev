---
title: "src/framework/util/rect.h"
source_file: "src/framework/util/rect.h"
generated_at: "2025-11-01T05:32:59.311Z"
doc_type: "cpp_api"
---

# src/framework/util/rect.h

(if)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignTopRight) moveTopRight(r.topRight());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignTopRight) moveTopRight(r.topRight()` | - |

**Returns:**
- `else`

---

(if-1)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignTopCenter) moveTopCenter(r.topCenter());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignTopCenter) moveTopCenter(r.topCenter()` | - |

**Returns:**
- `else`

---

(if-2)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignBottomLeft) moveBottomLeft(r.bottomLeft());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignBottomLeft) moveBottomLeft(r.bottomLeft()` | - |

**Returns:**
- `else`

---

(if-3)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignBottomRight) moveBottomRight(r.bottomRight());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignBottomRight) moveBottomRight(r.bottomRight()` | - |

**Returns:**
- `else`

---

(if-4)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignBottomCenter) moveBottomCenter(r.bottomCenter());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignBottomCenter) moveBottomCenter(r.bottomCenter()` | - |

**Returns:**
- `else`

---

(if-5)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignLeftCenter) moveCenterLeft(r.centerLeft());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignLeftCenter) moveCenterLeft(r.centerLeft()` | - |

**Returns:**
- `else`

---

(if-6)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignCenter) moveCenter(r.center());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignCenter) moveCenter(r.center()` | - |

**Returns:**
- `else`

---

(if-7)=
## `if`

**Signature:**
```cpp
else if(align == Fw::AlignRightCenter) moveCenterRight(r.centerRight());
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `align` | - | `= Fw::AlignRightCenter) moveCenterRight(r.centerRight()` | - |

**Returns:**
- `else`

---

(isnull)=
## `isNull`

**Signature:**
```cpp
bool isNull();
```

**Returns:**
- `bool`

---

(isempty)=
## `isEmpty`

**Signature:**
```cpp
bool isEmpty();
```

**Returns:**
- `bool`

---

(isvalid)=
## `isValid`

**Signature:**
```cpp
bool isValid();
```

**Returns:**
- `bool`

---

(left)=
## `left`

**Signature:**
```cpp
inline T left();
```

**Returns:**
- `T`

---

(top)=
## `top`

**Signature:**
```cpp
inline T top();
```

**Returns:**
- `T`

---

(right)=
## `right`

**Signature:**
```cpp
inline T right();
```

**Returns:**
- `T`

---

(bottom)=
## `bottom`

**Signature:**
```cpp
inline T bottom();
```

**Returns:**
- `T`

---

(horizontalcenter)=
## `horizontalCenter`

**Signature:**
```cpp
inline T horizontalCenter();
```

**Returns:**
- `T`

---

(verticalcenter)=
## `verticalCenter`

**Signature:**
```cpp
inline T verticalCenter();
```

**Returns:**
- `T`

---

(x)=
## `x`

**Signature:**
```cpp
inline T x();
```

**Returns:**
- `T`

---

(y)=
## `y`

**Signature:**
```cpp
inline T y();
```

**Returns:**
- `T`

---

(topleft)=
## `topLeft`

**Signature:**
```cpp
TPoint<T> topLeft();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(bottomright)=
## `bottomRight`

**Signature:**
```cpp
TPoint<T> bottomRight();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(topright)=
## `topRight`

**Signature:**
```cpp
TPoint<T> topRight();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(bottomleft)=
## `bottomLeft`

**Signature:**
```cpp
TPoint<T> bottomLeft();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(topcenter)=
## `topCenter`

**Signature:**
```cpp
TPoint<T> topCenter();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(bottomcenter)=
## `bottomCenter`

**Signature:**
```cpp
TPoint<T> bottomCenter();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(centerleft)=
## `centerLeft`

**Signature:**
```cpp
TPoint<T> centerLeft();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(centerright)=
## `centerRight`

**Signature:**
```cpp
TPoint<T> centerRight();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(center)=
## `center`

**Signature:**
```cpp
TPoint<T> center();
```

**Returns:**
- `TPoint&lt;T&gt;`

---

(size)=
## `size`

**Signature:**
```cpp
TSize<T> size();
```

**Returns:**
- `TSize&lt;T&gt;`

---

(reset)=
## `reset`

**Signature:**
```cpp
void reset();
```

---

(clear)=
## `clear`

**Signature:**
```cpp
void clear();
```

---

(setleft)=
## `setLeft`

**Signature:**
```cpp
void setLeft(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(settop)=
## `setTop`

**Signature:**
```cpp
void setTop(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(setright)=
## `setRight`

**Signature:**
```cpp
void setRight(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(setbottom)=
## `setBottom`

**Signature:**
```cpp
void setBottom(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(setx)=
## `setX`

**Signature:**
```cpp
void setX(T x);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `x` | - |

---

(sety)=
## `setY`

**Signature:**
```cpp
void setY(T y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `y` | - |

---

(settopleft)=
## `setTopLeft`

**Signature:**
```cpp
void setTopLeft(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(setbottomright)=
## `setBottomRight`

**Signature:**
```cpp
void setBottomRight(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(settopright)=
## `setTopRight`

**Signature:**
```cpp
void setTopRight(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(setbottomleft)=
## `setBottomLeft`

**Signature:**
```cpp
void setBottomLeft(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(setwidth)=
## `setWidth`

**Signature:**
```cpp
void setWidth(T width);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `width` | - |

---

(setheight)=
## `setHeight`

**Signature:**
```cpp
void setHeight(T height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `height` | - |

---

(setsize)=
## `setSize`

**Signature:**
```cpp
void setSize(const TSize<T>& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&` | `size` | - |

---

(setrect)=
## `setRect`

**Signature:**
```cpp
void setRect(T x, T y, T width, T height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `x` | - |
| `T` | `y` | - |
| `T` | `width` | - |
| `T` | `height` | - |

---

(setcoords)=
## `setCoords`

**Signature:**
```cpp
void setCoords(int left, int top, int right, int bottom);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `left` | - |
| `int` | `top` | - |
| `int` | `right` | - |
| `int` | `bottom` | - |

---

(expandleft)=
## `expandLeft`

**Signature:**
```cpp
void expandLeft(T add);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `add` | - |

---

(expandtop)=
## `expandTop`

**Signature:**
```cpp
void expandTop(T add);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `add` | - |

---

(expandright)=
## `expandRight`

**Signature:**
```cpp
void expandRight(T add);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `add` | - |

---

(expandbottom)=
## `expandBottom`

**Signature:**
```cpp
void expandBottom(T add);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `add` | - |

---

(expand)=
## `expand`

**Signature:**
```cpp
void expand(T top, T right, T bottom, T left);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `top` | - |
| `T` | `right` | - |
| `T` | `bottom` | - |
| `T` | `left` | - |

---

(expand-1)=
## `expand`

**Signature:**
```cpp
void expand(T add);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `add` | - |

---

(translate)=
## `translate`

**Signature:**
```cpp
void translate(T x, T y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `x` | - |
| `T` | `y` | - |

---

(translate-1)=
## `translate`

**Signature:**
```cpp
void translate(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(resize)=
## `resize`

**Signature:**
```cpp
void resize(const TSize<T>& size);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TSize&lt;T&gt;&` | `size` | - |

---

(resize-1)=
## `resize`

**Signature:**
```cpp
void resize(T width, T height);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `width` | - |
| `T` | `height` | - |

---

(move)=
## `move`

**Signature:**
```cpp
void move(T x, T y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `x` | - |
| `T` | `y` | - |

---

(move-1)=
## `move`

**Signature:**
```cpp
void move(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(moveleft)=
## `moveLeft`

**Signature:**
```cpp
void moveLeft(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(movetop)=
## `moveTop`

**Signature:**
```cpp
void moveTop(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(moveright)=
## `moveRight`

**Signature:**
```cpp
void moveRight(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(movebottom)=
## `moveBottom`

**Signature:**
```cpp
void moveBottom(T pos);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `pos` | - |

---

(movetopleft)=
## `moveTopLeft`

**Signature:**
```cpp
void moveTopLeft(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movebottomright)=
## `moveBottomRight`

**Signature:**
```cpp
void moveBottomRight(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movetopright)=
## `moveTopRight`

**Signature:**
```cpp
void moveTopRight(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movebottomleft)=
## `moveBottomLeft`

**Signature:**
```cpp
void moveBottomLeft(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movetopcenter)=
## `moveTopCenter`

**Signature:**
```cpp
void moveTopCenter(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movebottomcenter)=
## `moveBottomCenter`

**Signature:**
```cpp
void moveBottomCenter(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movecenterleft)=
## `moveCenterLeft`

**Signature:**
```cpp
void moveCenterLeft(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movecenterright)=
## `moveCenterRight`

**Signature:**
```cpp
void moveCenterRight(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(translated)=
## `translated`

**Signature:**
```cpp
TRect<T> translated(int x, int y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `int` | `x` | - |
| `int` | `y` | - |

**Returns:**
- `TRect&lt;T&gt;`

---

(translated-1)=
## `translated`

**Signature:**
```cpp
TRect<T> translated(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

**Returns:**
- `TRect&lt;T&gt;`

---

(expanded)=
## `expanded`

**Signature:**
```cpp
TRect<T> expanded(T add);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `add` | - |

**Returns:**
- `TRect&lt;T&gt;`

---

(movecenter)=
## `moveCenter`

**Signature:**
```cpp
void moveCenter(const TPoint<T> &p);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TPoint&lt;T&gt; &p` | - | - |

---

(movehorizontalcenter)=
## `moveHorizontalCenter`

**Signature:**
```cpp
void moveHorizontalCenter(T x);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `x` | - |

---

(moveverticalcenter)=
## `moveVerticalCenter`

**Signature:**
```cpp
void moveVerticalCenter(T y);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `T` | `y` | - |

---

(contains)=
## `contains`

**Signature:**
```cpp
bool contains(const TPoint<T> &p, bool insideOnly = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const TPoint&lt;T&gt; &p` | - |  | - |
| `bool` | `insideOnly` | `false` | - |

**Returns:**
- `bool`

---

(contains-1)=
## `contains`

**Signature:**
```cpp
bool contains(const TRect<T> &r, bool insideOnly = false);
```

**Parameters:**

| Type | Name | Default | Description |
|------|------|---------|-------------|
| `const TRect&lt;T&gt; &r` | - |  | - |
| `bool` | `insideOnly` | `false` | - |

**Returns:**
- `bool`

---

(intersects)=
## `intersects`

**Signature:**
```cpp
bool intersects(const TRect<T> &r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TRect&lt;T&gt; &r` | - | - |

**Returns:**
- `bool`

---

(united)=
## `united`

**Signature:**
```cpp
TRect<T> united(const TRect<T> &r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TRect&lt;T&gt; &r` | - | - |

**Returns:**
- `TRect&lt;T&gt;`

---

(intersection)=
## `intersection`

**Signature:**
```cpp
TRect<T> intersection(const TRect<T> &r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TRect&lt;T&gt; &r` | - | - |

**Returns:**
- `TRect&lt;T&gt;`

---

(bind)=
## `bind`

**Signature:**
```cpp
void bind(const TRect<T> &r);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TRect&lt;T&gt; &r` | - | - |

---

(alignin)=
## `alignIn`

**Signature:**
```cpp
void alignIn(const TRect<T> &r, Fw::AlignmentFlag align);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `const TRect&lt;T&gt; &r` | - | - |
| `Fw::AlignmentFlag` | `align` | - |

---

(operator)=
## `operator*`

**Signature:**
```cpp
TRect<T> operator*(float num);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `float` | `num` | - |

**Returns:**
- `TRect&lt;T&gt;`

---

(operator-1)=
## `operator<<`

**Signature:**
```cpp
std::ostream& operator<<(std::ostream& out, const TRect<T>& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::ostream&` | `out` | - |
| `const TRect&lt;T&gt;&` | `rect` | - |

**Returns:**
- `std::ostream&`

---

(operator-2)=
## `operator>>`

**Signature:**
```cpp
std::istream& operator>>(std::istream& in, TRect<T>& rect);
```

**Parameters:**

| Type | Name | Description |
|------|------|-------------|
| `std::istream&` | `in` | - |
| `TRect&lt;T&gt;&` | `rect` | - |

**Returns:**
- `std::istream&`

---
