---
title: Moduły – przegląd
---

# Moduły

:::{admonition} Jak to jest zorganizowane?
:class: tip
Ta sekcja ma **dwa widoki**:
1) **Strukturalny** – moduły pogrupowane w kategorie (bot_tools, core, dev_tools, gameplay).  
2) **Opisowy** – dłuższe omówienia i przewodniki (folder `modulesopisy`).
:::

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Bot tools
:link: structured/bot_tools/INDEX
:link-type: doc
:shadow: md
Skriptowanie i automatyzacja (Cavebot, Targetbot, VBot, panele, funkcje).
:::

:::{grid-item-card} Core
:link: structured/core/INDEX
:link-type: doc
:shadow: md
Biblioteki bazowe klienta i runtime.
:::

:::{grid-item-card} Dev tools
:link: structured/dev_tools/INDEX
:link-type: doc
:shadow: md
Narzędzia deweloperskie (style, profile, bugreport, updater, protocol, shaders).
:::

:::{grid-item-card} Gameplay
:link: structured/gameplay/INDEX
:link-type: doc
:shadow: md
Interfejs gry, inv, minimap, questy, rynek, hotkeys, statystyki, shop…
:::

:::{grid-item-card} Opisy modułów (Narrative)
:link: modulesopisy/index
:link-type: doc
:shadow: md
Szersze opisy (4 rozdziały): core, gameplay (2), misc.
:::
:::

## Struktura modułów

```{toctree}
:caption: Kategorie (strukturalne)
:maxdepth: 2
:titlesonly:

structured/bot_tools/INDEX
structured/core/INDEX
structured/dev_tools/INDEX
structured/gameplay/INDEX
```

## Opisy modułów (Narrative)

```{toctree}
:caption: Modules – opisy
:maxdepth: 1
:titlesonly:

modulesopisy/index
modulesopisy/modules_core
modulesopisy/modules_game_1
modulesopisy/modules_game_2
modulesopisy/modules_misc
```
