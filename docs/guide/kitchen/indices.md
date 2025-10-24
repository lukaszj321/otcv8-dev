# Indeksy i spisy

<hr/>

## 1) Prosta lista linków

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

````md
# Indeksy i spisy

- :ref:`genindex`
- :ref:`modindex`
- :ref:`search`
`````

:::

:::{grid-item}
**Efekt**

# Indeksy i spisy

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
  :::

:::
:::

<hr/>

## 2) Przyciski (sphinx-design)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
:::{grid} 1 3 3 3
:gutter: 2
:::{grid-row}

:::{grid-item}
:ref:`genindex`
:::

:::{grid-item}
:ref:`modindex`
:::

:::{grid-item}
:ref:`search`
:::

:::
```

:::

:::{grid-item}
**Efekt**

:::{grid} 1 3 3 3
:gutter: 2
:::{grid-row}

:::{grid-item}
:ref:`genindex`
:::

:::{grid-item}
:ref:`modindex`
:::

:::{grid-item}
:ref:`search`
:::

:::
:::

:::
:::

<hr/>

## 3) Karty (sphinx-design)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
:::{grid} 1 1 2 3
:gutter: 3
:::{grid-row}

:::{grid-item-card} 📚 Indeks haseł
:link: genindex
:link-type: ref
Przegląd wszystkich haseł.
:::

:::{grid-item-card} 🧩 Indeks modułów
:link: modindex
:link-type: ref
Lista modułów i pakietów.
:::

:::{grid-item-card} 🔎 Wyszukiwarka
:link: search
:link-type: ref
Pełnotekstowe wyszukiwanie.
:::

:::
```

:::

:::{grid-item}
**Efekt**

:::{grid} 1 1 2 3
:gutter: 3
:::{grid-row}

:::{grid-item-card} 📚 Indeks haseł
:link: genindex
:link-type: ref
Przegląd wszystkich haseł.
:::

:::{grid-item-card} 🧩 Indeks modułów
:link: modindex
:link-type: ref
Lista modułów i pakietów.
:::

:::{grid-item-card} 🔎 Wyszukiwarka
:link: search
:link-type: ref
Pełnotekstowe wyszukiwanie.
:::

:::
:::

:::
:::

<hr/>

## 4) Sekcja na stronie głównej

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
## Szybki dostęp

- **Hasła:** :ref:`genindex`
- **Moduły:** :ref:`modindex`
- **Szukaj:** :ref:`search`
```

:::

:::{grid-item}
**Efekt**

## Szybki dostęp

* **Hasła:** :ref:`genindex`
* **Moduły:** :ref:`modindex`
* **Szukaj:** :ref:`search`
  :::

:::
:::

<hr/>

## 5) Nawigacja w stopce (role inline)

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
---

Powrót do [:ref:`genindex`] · [:ref:`modindex`] · [:ref:`search`]
```

:::

:::{grid-item}
**Efekt**

<hr/>

Powrót do [:ref:`genindex`] · [:ref:`modindex`] · [:ref:`search`]
:::

:::
:::

<hr/>

## 6) Uwaga do `modindex`

:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

:::{grid-item}
**Kod**

```md
:::{note}
`modindex` generuje się, gdy używasz rozszerzeń dokumentujących API (np. `autodoc`, `autosummary`) i masz zdefiniowane moduły.
:::
```

:::

:::{grid-item}
**Efekt**

:::{note}
`modindex` generuje się, gdy używasz rozszerzeń dokumentujących API (np. `autodoc`, `autosummary`) i masz zdefiniowane moduły.
:::
:::

:::
:::
