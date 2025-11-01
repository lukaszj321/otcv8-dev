# Generic: sidebary i kod

> Wymagane: `sphinx_design` + `myst_enable_extensions = ["colon_fence"]`.

<hr/>

## Nagłówki

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
# H1

## H2

### H3

Zwykły akapit z **bold** i *italic*.
````

:::

:::{grid-item}
**Efekt**

# H1

## H2

### H3

Zwykły akapit z **bold** i *italic*.
:::

:::
:::

<hr/>

## Listy

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
- A
- B
  - B.1

1. jeden
2. dwa
```

:::

:::{grid-item}
**Efekt**

* A
* B

  * B.1

1. jeden
2. dwa
   :::
   :::
   :::

<hr/>

## Admonitions

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
:::{note} Info
Prosta notka.
:::

:::{warning} Uwaga
Ważny komunikat.
:::
```

:::

:::{grid-item}
**Efekt**

:::{note} Info
Prosta notka.
:::

:::{warning} Uwaga
Ważny komunikat.
:::
:::
:::

<hr/>

## Zakładki (tabs)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

````md
:::{tab-set}
:::{tab-item} Lua
```lua
print("hello")
```
:::
:::{tab-item} C++
```cpp
std::cout << "hello";
```
:::
:::
````

:::

:::{grid-item}
**Efekt**

:::{tab-set}
:::{tab-item} Lua

```lua
print("hello")
```

:::
:::{tab-item} C++

```cpp
std::cout << "hello";
```

:::
:::
:::
:::

<hr/>

## Mermaid

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

````md
```{mermaid}
flowchart LR
  A[Start] --> B[Process]
  B --> C[End]
```
````

:::

:::{grid-item}
**Efekt**

```{mermaid}
flowchart LR
  A[Start] --> B[Process]
  B --> C[End]
```

:::
:::
:::

<hr/>

## Sidebar

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

````md
```{sidebar} Sidebar
Użyteczne linki.
```

Akapit obok sidebara.
````

:::

:::{grid-item}
**Efekt**

```{sidebar} Sidebar
Użyteczne linki.
```

Akapit obok sidebara.
:::
:::
:::

<hr/>

## CSV Table (inline)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

````md
```{csv-table} Minimalny przykład
:header-rows: 1
:widths: 30 70
Name,Description
"/v1/login","Authenticate user"
"/v1/profile","Get profile"
```
````

:::

:::{grid-item}
**Efekt**

```{csv-table} Minimalny przykład
:header-rows: 1
:widths: 30 70
Name,Description
"/v1/login","Authenticate user"
"/v1/profile","Get profile"
```

:::
:::
:::

