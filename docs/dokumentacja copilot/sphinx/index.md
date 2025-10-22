---
title: Copilot Docs — DEV‑SCAN 1:1 + PLUS
---

# Copilot Docs — DEV‑SCAN 1:1 + PLUS

:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} Integracja ze Sphinx
:link: integration_guide
{badge}`guide`
Opis integracji wyników skanu (indeksy kodu, cross‑linki) z PyData.
:::

:::{grid-item-card} Indeksy kodu
:link: code_index
{badge}`reference`
C++/Lua/OTUI: klasy, funkcje, eventy.
:::

:::{grid-item-card} Diagramy i struktury
:link: trees
{badge}`examples`
Mapy zależności, drzewa modułów.
:::
:::

````{tabs}
```{tab} Guide
DEV‑SCAN pipeline: gdzie lądują artefakty i jak są linkowane w Sphinx (PyData sidebar + search).
```

```{tab} Reference
Generatory, formaty wyjściowe, reguły parsowania, ograniczenia; jak dopiąć cross‑referencje.
```

```{tab} Examples
`literalinclude` z regionami (utrzymywalne fragmenty kodu).

```{literalinclude} ../../../src/framework/xml/tinyxml.cpp
:language: cpp
:lines: 1-20
```

```{literalinclude} ../../../modules/corelib/util.lua
:language: lua
:lines: 1-15
```
```
````

:::{card}
**Quality gates**
{badge}`scan ok,success` {badge}`crosslinks todo,warning` {badge}`perf check,info`
:::

```{dropdown} Quick tasks (Copilot Docs)
- [ ] `literalinclude` tylko z regionami
- [ ] Mini „See also" (Authoring/UI/Events)
- [ ] TOC nie przepełnia prawego paska
```

:::{grid} 1 1 2 3
**See also:** {ref}`authoring/index` · {ref}`04_ui/index` · {ref}`02_events/index`
:::

```{toctree}
:hidden:
:maxdepth: 2
:caption: Przegląd i indeksy

overview
integration_guide
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Kod źródłowy

src_code
src_client
src_framework
code_index
anchors
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Moduły i UI

modules
modules_repo
layouts
mods
lua_api
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Eventy i cross-linki

events_hooks
crosslinks
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Struktury danych

trees
trees_real
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Platformy i build

vc16
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Narzędzia z repo

lua_bindings_repo
bitmaps_generated
```
