---
title: Language template generator
---

# Language template generator

```{admonition} Źródło
:class: tip
Skrypt: `tools/gen_lang_template.sh`
```

## Podgląd skryptu
```{literalinclude} ../../tools/gen_lang_template.sh
:language: bash
```

## Przykładowy szablon (do pobrania)
Minimalny szablon pliku lokalizacji, który można powielić na `locale_template_<lang>.lua`.

```{code-block} lua
:caption: locale_template_en.lua
return {
  ok = "OK",
  cancel = "Cancel"
}
```