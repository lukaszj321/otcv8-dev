---
title: Lua bindings generator
---

# Lua bindings generator

```{admonition} Źródło
:class: tip
Skrypt: `tools/generate_lua_bindings.lua`
```

## Podgląd skryptu
```{literalinclude} ../../tools/generate_lua_bindings.lua
:language: lua
```

## Wyjście (dataset)
Poniżej osadzony dataset, który zasila RAG oraz strony **01_core**.

```{csv-table} lua_bindings.csv
:header-rows: 1
:file: ../../authoring/01_core/datasets/lua_bindings.csv
:widths: auto
```

## Specyfikacja CSV
```{csv-table} lua_bindings.schema.csv
:header-rows: 1
:file: ../../authoring/_data/schemas/lua_bindings.schema.csv
:widths: auto
```