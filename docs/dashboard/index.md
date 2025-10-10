# OTCv8 Developer Portal

```{toctree}
:hidden:
:maxdepth: 2
:caption: Navigation
workbench/index
guide/index
api/index
blog/index
process/release
process/pre-commit
```

:::{admonition} Welcome
:class: tip
Nowy **landing** z kartami, toctree i skrótami.
:::

:::{grid} 1 2 3 3
:gutter: 2

:::{card} 📦 API Reference
:link: ../api/index
:link-type: doc
Pełne API (Lua/C++).
:::

:::{card} 🧪 Workbench
:link: ../workbench/index
:link-type: doc
Szablony, checklisty, CSV → tabele.
:::

:::{card} 📑 Guide & Components
:link: ../guide/index
:link-type: doc
Admonitions, bloki, listy, tabele, sidebary.
:::

:::{card} 📝 Blog (ABlog)
:link: ../blog/index
:link-type: doc
Devlog i notatki.
:::
:::

```{mermaid}
flowchart LR
  A[OTCv8 Core] --> B(Events)
  A --> C(Modules)
  A --> D(UI)
  B --> E[Network]
  E --> F[Assets]
  A --> G[Settings/Crypto]
  A --> H[Audio]
  A --> I[Logging]
  A --> J[Game Runtime]
```