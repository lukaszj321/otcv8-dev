# API — przegląd modułów

**Cel:** zebrać nawigację po _surowym API_ w jednym miejscu. Poniższe sekcje mogą wykorzystywać automatycznie wygenerowane indeksy (`glob`) wskazujące na Twoje istniejące foldery (np. `01_core/api`, `03_modules`, `04_ui`).

## Jak czytać
- H2/H3/H4 odwzorowują hierarchię: **moduł → klasa → metoda/funkcja → parametry → snippet**.
- Każda funkcja powinna mieć **kompletny snippet użycia**, nie tylko nagłówek.

```{{toctree}}
:caption: Surowe API (z repo)
:maxdepth: 2
:glob:

../01_core/api/**
../03_modules/**
../04_ui/**
```

## Konwencja snippetów (placeholder)
```cpp
// Nazwa: Module::Function
// Parametry: x:int, y:string, options?:Config
// Zwraca: Result<T>
auto out = Module::Function(42, "abc", {{/* ...options... */}});
// assert(out.ok());
```
