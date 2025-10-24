# Indeksy i spisy

## 1) Prosta lista linków

:::{grid} 1 1 2 2
:gutter: 3

:::{grid-item}
**Kod**

```md
# Indeksy i spisy

- :ref:`genindex`
- :ref:`modindex`
- :ref:`search`
```

:::

:::{grid-item}
**Efekt**

# Indeksy i spisy

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
  :::

:::

---

## 2) Przyciski (sphinx-design)

:::{grid} 1 1 2 2
:gutter: 3

:::{grid-item}
**Kod**

```md
:::{grid} 1 3 3 3
:gutter: 2

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

---

## 3) Karty (sphinx-design)

:::{grid} 1 1 2 2
:gutter: 3

:::{grid-item}
**Kod**

```md
:::{grid} 1 1 2 3
:gutter: 3

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

---

## 4) Sekcja na stronie głównej

:::{grid} 1 1 2 2
:gutter: 3

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

---

## 5) Nawigacja w stopce (role inline)

:::{grid} 1 1 2 2
:gutter: 3

:::{grid-item}
**Kod**

```md
---

Powrót do [:ref:`genindex`] · [:ref:`modindex`] · [:ref:`search`]
```

:::

:::{grid-item}
**Efekt**

---

Powrót do [:ref:`genindex`] · [:ref:`modindex`] · [:ref:`search`]
:::

:::

---

## 6) Uwaga do `modindex`

:::{grid} 1 1 2 2
:gutter: 3

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
