# src/framework/ui/uigridlayout.h

```cpp
public: UIGridLayout(UIWidgetPtr parentWidget);
```
```cpp
void applyStyle(const OTMLNodePtr& styleNode);
```
```cpp
void removeWidget(const UIWidgetPtr& widget);
```
```cpp
void addWidget(const UIWidgetPtr& widget);
```
```cpp
protected: bool internalUpdate();
```
```cpp
void setCellSize(const Size& size);
```
```cpp
void setCellWidth(int width);
```
```cpp
void setCellHeight(int height);
```
```cpp
void setCellSpacing(int spacing);
```
```cpp
void setNumColumns(int columns);
```
```cpp
void setNumLines(int lines);
```
```cpp
void setAutoSpacing(bool enable);
```
```cpp
void setFitChildren(bool enable);
```
```cpp
void setFlow(bool enable);
```
```cpp
Size getCellSize();
```
```cpp
int getCellSpacing();
```
```cpp
int getNumColumns();
```
```cpp
int getNumLines();
```
```cpp
virtual bool isUIGridLayout();
```