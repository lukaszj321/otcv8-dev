# Listy

<hr/>

## 1) Podstawowe listy

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**
````md
- A
- B
  - B.1

1. jeden
2. dwa
`````

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

## 2) Lista mieszana (punktowana + numerowana)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
- Sekcja
  1. krok pierwszy
  2. krok drugi
- Podsumowanie
```

:::

:::{grid-item}
**Efekt**

* Sekcja

  1. krok pierwszy
  2. krok drugi
* Podsumowanie
  :::

:::
:::

<hr/>

## 3) Lista zadań (task-list)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
- [x] Przygotuj repo
- [ ] Skonfiguruj CI
- [ ] Dodaj dokumentację
```

:::

:::{grid-item}
**Efekt**

* [x] Przygotuj repo
* [ ] Skonfiguruj CI
* [ ] Dodaj dokumentację
  :::

:::
:::

<hr/>

## 4) Lista definicji (definition list)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
Termin A
: Krótkie objaśnienie.

Termin B
: Dłuższy opis z przykładem i **pogrubieniem**.
```

:::

:::{grid-item}
**Efekt**

Termin A
: Krótkie objaśnienie.

Termin B
: Dłuższy opis z przykładem i **pogrubieniem**.
:::

:::
:::

<hr/>

## 5) Lista w admonition

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
:::{note} Wymagania
- Python 3.12+
- Sphinx 7.4+
- pydata-sphinx-theme
:::
```

:::

:::{grid-item}
**Efekt**

:::{note} Wymagania

* Python 3.12+
* Sphinx 7.4+
* pydata-sphinx-theme
  :::
  :::

:::
:::

<hr/>

## 6) Dwie kolumny z listami (sphinx-design)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Checklist**
- [x] Build lokalny
- [x] Lint
- [ ] Deploy
:::

:::{grid-item}
**Kroki**
1. `make clean`
2. `make html`
3. publikacja
:::

:::
```

:::

:::{grid-item}
**Efekt**

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Checklist**

* [x] Build lokalny
* [x] Lint
* [ ] Deploy
  :::

:::{grid-item}
**Kroki**

1. `make clean`
2. `make html`
3. publikacja
   :::

:::
:::

:::
:::

<hr/>

## 7) Zagnieżdżenia wielopoziomowe

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
- Warstwa 1
  - Warstwa 2
    - Warstwa 3
      - Warstwa 4
```

:::

:::{grid-item}
**Efekt**

* Warstwa 1

  * Warstwa 2

    * Warstwa 3

      * Warstwa 4
        :::

:::
:::

<hr/>

## 8) Elementy z wieloma akapitami

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
- Pierwszy element

  Drugi akapit tego **samego** elementu (pusta linia + wcięcie 2–3 spacje).

- Drugi element
```

:::

:::{grid-item}
**Efekt**

* Pierwszy element

  Drugi akapit tego **samego** elementu (pusta linia + wcięcie 2–3 spacje).

* Drugi element
  :::

:::
:::

<hr/>

## 9) Listy w zakładkach (tabs)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
:::{tab-set}
:::{tab-item} Kroki
1. Init
2. Build
3. Test
:::
:::{tab-item} Wymagania
- Python
- Sphinx
- Theme
:::
:::
```

:::

:::{grid-item}
**Efekt**

:::{tab-set}

:::{tab-item} Kroki

1. Init
2. Build
3. Test

:::

:::{tab-item} Wymagania

* Python
* Sphinx
* Theme

:::

:::

:::
:::
