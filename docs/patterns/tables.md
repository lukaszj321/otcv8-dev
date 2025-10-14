
---
title: Patterns — Tables
---

# Patterns — Tables

```{admonition} CSV (scroll + sticky header)
:class: tip
Klasa `.table-compact` zmniejsza padding wierszy — użyteczne dla szerokich tabel.
```

<div class="table-compact">

```{csv-table} Example (CSV)
:file: ../authoring/_data/facets.csv
:header-rows: 1
:widths: auto
```

</div>

## List table (RST)

.. list-table:: List tables can have captions like this one.
    :widths: 10 5 10 50
    :header-rows: 1
    :stub-columns: 1

    * - List table
      - Header 1
      - Header 2
      - Header 3 long.
