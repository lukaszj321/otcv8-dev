---
title: Authoring Tools
---

# Authoring Tools (pipeline helpers)

:::{admonition} Co to jest?
:class: tip
Strony poniżej dokumentują **narzędzia z katalogu `tools/`** i pokazują,
jak ich wyniki są osadzane w sekcji **authoring** (CSV / Mermaid / MyST).
:::

:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} TFS extended opcode
:link: tfs_extendedopcode
:link-type: doc
:shadow: md
Patch rozszerzający protokół gry o **extended opcode**.
:::

:::{grid-item-card} Lua bindings generator
:link: lua_bindings
:link-type: doc
:shadow: md
Eksporty C++ → Lua → dataset `lua_bindings.csv`.
:::

:::{grid-item-card} Needed translations
:link: translations_needed
:link-type: doc
:shadow: md
Skrypt skanujący brakujące klucze i generujący `needed_translations.csv`.
:::

:::{grid-item-card} Language template
:link: translations_template
:link-type: doc
:shadow: md
Generator szablonów plików lokalizacji.
:::

:::{grid-item-card} Bitmap font
:link: bitmap_font
:link-type: doc
:shadow: md
Generator czcionek bitmapowych do UI.
:::

:::{grid-item-card} Make snapshot
:link: make_snapshot
:link-type: doc
:shadow: md
Archiwizacja/stempel repozytorium (snapshot).
:::

:::

```{toctree}
:caption: Tools
:maxdepth: 1
:titlesonly:

tfs_extendedopcode
lua_bindings
translations_needed
translations_template
bitmap_font
make_snapshot
```