# Bloki i zakładki

## 1) Podstawowe zakładki

:::{tab-set}
:::{tab-item} Lua

```lua
-- example
````

:::
:::{tab-item} C++

```cpp
// example
```

:::
:::

<hr/>

## 2) Zakładki z trzema językami

:::{tab-set}
:::{tab-item} Lua

```lua
local function add(a, b)
  return a + b
end
print(add(2,3))
```

:::
:::{tab-item} C++

```cpp
#include <iostream>
int add(int a,int b){return a+b;}
int main(){ std::cout << add(2,3); }
```

:::
:::{tab-item} Python

```python
def add(a,b):
    return a+b
print(add(2,3))
```

:::
:::

<hr/>

## 3) `sync-group` (synchronizacja wyboru między zestawami)

:::{tab-set}
:sync-group: code-lang
:::{tab-item} Lua

```lua
-- lua code
```

:::
:::{tab-item} C++

```cpp
// c++ code
```

:::
:::

:::{tab-set}
:sync-group: code-lang
:::{tab-item} Lua

```lua
-- drugi blok lua
```

:::
:::{tab-item} C++

```cpp
// drugi blok c++
```

:::
:::

<hr/>

## 4) Zakładki z domyślnie wybraną kartą

:::{tab-set}
:::{tab-item} Lua
:selected:

```lua
print("Lua selected by default")
```

:::
:::{tab-item} C++

```cpp
// other
```

:::
:::

<hr/>

## 5) Zakładki w kolumnach (przykład 2 kolumny)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**API**

:::{tab-set}
:::{tab-item} Lua

```lua
-- api
```

:::
:::{tab-item} Python

```python
# api
```

:::
:::
:::

:::{grid-item}
**Przykład użycia**

:::{tab-set}
:::{tab-item} Lua

```lua
-- use
```

:::
:::{tab-item} Python

```python
# use
```

:::
:::
:::

:::
:::

<hr/>

## 6) Zakładki z klasami CSS

:::{tab-set}
:class: my-tabs
:::{tab-item} Lua
:class: code-tab

```lua
-- stylowane
```

:::
:::{tab-item} C++
:class: code-tab

```cpp
// stylowane
```

:::
:::

<hr/>

## 7) Zakładki + admonition wewnątrz

:::{tab-set}
:::{tab-item} Lua

```lua
print("ok")
```

:::{note}
To samo w C++ na drugiej karcie.
:::
:::
:::{tab-item} C++

```cpp
#include <iostream>
int main(){ std::cout << "ok"; }
```

:::
:::
