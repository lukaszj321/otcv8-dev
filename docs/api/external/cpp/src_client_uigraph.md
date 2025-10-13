# src/client/uigraph.h

```cpp
public: UIGraph();
```
```cpp
void drawSelf(Fw::DrawPane drawPane);
```
```cpp
void clear();
```
```cpp
void addValue(int value, bool ignoreSmallValues = false);
```
```cpp
protected: void onStyleApply(const std::string& styleName, const OTMLNodePtr& styleNode);
```
```cpp
void setLineWidth(int width);
```
```cpp
void setCapacity(int capacity);
```
```cpp
void setTitle(const std::string& title);
```
```cpp
void setShowLabels(bool value);
```