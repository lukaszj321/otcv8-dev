# Listy

## 1) Podstawowe listy

```md
- A
- B
  - B.1

1. jeden
2. dwa
```

## 2) Lista mieszana (punktowana + numerowana)

```md
- Sekcja
  1. krok pierwszy
  2. krok drugi
- Podsumowanie
```

## 3) Lista zadań (task-list)

```md
- [x] Przygotuj repo
- [ ] Skonfiguruj CI
- [ ] Dodaj dokumentację
```

## 4) Lista definicji (definition list)

```md
Termin A
: Krótkie objaśnienie.

Termin B
: Dłuższy opis z przykładem i **pogrubieniem**.
```

## 5) Lista w admonition

```md
:::{note} Wymagania
- Python 3.12+
- Sphinx 7.4+
- pydata-sphinx-theme
:::
```

## 6) Dwie kolumny z listami (sphinx-design)

```md
:::{grid} 1 1 2 2
:gutter: 3

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

## 7) Zagnieżdżenia wielopoziomowe

```md
- Warstwa 1
  - Warstwa 2
    - Warstwa 3
      - Warstwa 4
```

## 8) Elementy z wieloma akapitami

```md
- Pierwszy element

  Drugi akapit tego **samego** elementu (pusta linia + wcięcie 2–3 spacje).

- Drugi element
```

## 9) Listy w zakładkach (tabs)

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
