# Workbench: skrypty, notatki i checklisty

<!-- Hidden TOC for sidebar -->
```{toctree}
:maxdepth: 2
:hidden:

template
```

<!-- Lead -->
> Szybkie miejsce do **tworzenia i dokumentowania skryptów** (Lua/C++).
> Wklej kod, opisz działanie, dodaj checklistę testów, diagram i linki do API.
> Poniżej masz kafelki z akcjami oraz katalog skryptów.

:::{grid} 2
:gutter: 2

:::{card}
:title: ➕ Nowy skrypt (użyj szablonu)
:link: template.html
:text-align: left

- skopiuj `workbench/template.md` do `workbench/my_script.md`
- uzupełnij metadane, opis, kod (blok lub `literalinclude`)
- dodaj do katalogu poniżej

:::

:::{card}
:title: 📚 Katalog skryptów
:text-align: left

Umieść pliki `.md` w `docs/workbench/` i dodaj do TOC poniżej.
Możesz też zbudować listę z CSV (przykład dalej).

:::
:::

## Katalog (TOC)

```{toctree}
:maxdepth: 1

template
```

## Lista skryptów z CSV (przykład)

Poniżej tabela wczytana z `_data/scripts.csv`. Podmień na swoje dane.

```{csv-table} **Scripts registry (example)**
:file: ../_data/scripts.csv
:header-rows: 1
:widths: 20, 20, 15, 15, 30

```

## Jak wstawić kod z pliku (bez wklejania)

```{code-block} rst
.. literalinclude:: ../../scripts/example.lua
   :language: lua
   :linenos:
   :caption: example.lua (wczytany automatycznie)
```

## Wskazówki

- Dla długich bloków kodu używaj `literalinclude`, żeby nie dublować zawartości.
- Diagramy rysuj mermaid-em – działają w dark mode (patrz szablon).
- Dla checklist używaj MyST task lists (`- [ ]`).
- Linkuj API z `docs/api/external/otcv8-full-api.md` i `docs/api/external/lua/luafunctions_client.md`.