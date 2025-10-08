# OTCv8 – Dokumentacja

Krótka nawigacja po projekcie. Lewy panel pokazuje spis treści generowany z poniższych toctree.

```{toctree}
:caption: Start
:maxdepth: 2

cpp/overview.md
```

```{toctree}
:caption: API
:maxdepth: 2
:glob:

api/**/*.md
```

```{toctree}
:caption: Moduły (structured)
:maxdepth: 2
:glob:

modules/structured/**/*.md
```

```{toctree}
:caption: Pozostałe
:maxdepth: 2
:glob:

modules/**/*.md
```

> Uwaga: w linkach w treści używaj odniesień do plików `.md` (np. `api/index.md`),
> wtedy Sphinx poprawnie zamieni je na `.html` lub katalogi (dla buildera `dirhtml`).
