# src/framework/ui/uigridlayout.h

```cpp
public:
    UIGridLayout(UIWidgetPtr parentWidget);
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
void setCellSize(const Size& size) { m_cellSize = size; update();
```
```cpp
void setCellWidth(int width) { m_cellSize.setWidth(width);
```
```cpp
void setCellHeight(int height) { m_cellSize.setHeight(height);
```
```cpp
void setCellSpacing(int spacing) { m_cellSpacing = spacing; update();
```
```cpp
void setNumColumns(int columns) { m_numColumns = columns; update();
```
```cpp
void setNumLines(int lines) { m_numLines = lines; update();
```
```cpp
void setAutoSpacing(bool enable) { m_autoSpacing = enable; update();
```
```cpp
void setFitChildren(bool enable) { m_fitChildren = enable; update();
```
```cpp
void setFlow(bool enable) { m_flow = enable; update();
```
```cpp
Size getCellSize() { return m_cellSize; } int getCellSpacing() { return m_cellSpacing; } int getNumColumns() { return m_numColumns; } int getNumLines() { return m_numLines; } virtual bool isUIGridLayout() { return true; } protected: bool internalUpdate();
```