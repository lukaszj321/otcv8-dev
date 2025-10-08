# OTCv8 – dokumentacja

Poniżej kompletny spis treści. Zbudowany na **Sphinx + Furo + MyST**, z podziałem na główne działy. Wszystkie pliki zostaną automatycznie zaciągnięte dzięki `:glob:`.

> Jeśli któryś dział jest zbyt obszerny, możesz w każdej chwili zmniejszyć `:maxdepth:`.

---

## API

```{toctree}
:maxdepth: 2
:caption: API
:glob:

api/**/*.md
```

## Dane / Specyfikacje

```{toctree}
:maxdepth: 2
:caption: Dane
:glob:

data/**/*.md
```

## Moduły (Structured)

### Core

```{toctree}
:maxdepth: 2
:caption: Moduły • Core
:glob:

modules/structured/core/**/*.md
```

### Dev Tools

```{toctree}
:maxdepth: 2
:caption: Moduły • Dev Tools
:glob:

modules/structured/dev_tools/**/*.md
```

### Gameplay

```{toctree}
:maxdepth: 2
:caption: Moduły • Gameplay
:glob:

modules/structured/gameplay/**/*.md
```

### Bot Tools

```{toctree}
:maxdepth: 2
:caption: Moduły • Bot Tools
:glob:

modules/structured/bot_tools/**/*.md
```

## C++

```{toctree}
:maxdepth: 2
:caption: C++
:glob:

cpp/**/*.md
```

---

## Szukasz czegoś konkretnego?

* ✅ Użyj pola **Wyszukiwanie** w nagłówku (pełnotekstowe, działa po włączeniu JS w przeglądarce).
* ✅ **Indeks alfabetyczny**: `genindex.html`.

> **Uwaga**: Kopie zapasowe i szkice w folderach typu `__md_backup*` są celowo pominięte (nie będą w nawigacji).
