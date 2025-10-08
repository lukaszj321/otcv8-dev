# OTCv8 — Dokumentacja (pełny spis treści)

Pełny, **automatyczny spis treści** całej dokumentacji z folderu `docs/`.
Jeśli jakiejś strony nie widać: sprawdź, czy plik ma nagłówek `# Tytuł` oraz czy nie zaczyna/kończy się samą linią `---`.

> W menu poniżej sekcje rozwijają się do poziomu 2–3; kliknięcie w dział otwiera listę wszystkich podstron.

---

```{toctree}
:maxdepth: 2
:caption: Start

README
modules/structured/README
```

```{toctree}
:maxdepth: 3
:caption: API
:glob:

api/*.md
api/*/*.md
api/*/*/*.md
```

```{toctree}
:maxdepth: 3
:caption: Dane / Specyfikacje
:glob:

data/*.md
data/*/*.md
```

```{toctree}
:maxdepth: 2
:caption: Moduły (wszystkie)
:glob:

modules/*.md
modules/*/*.md
modules/structured/*.md
modules/structured/*/*.md
```

```{toctree}
:maxdepth: 2
:caption: C++
:glob:

cpp/*.md
```

```{toctree}
:maxdepth: 1
:caption: Pozostałe
:glob:

*.md
```
