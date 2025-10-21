# Szybki start – OTClient v8 Developer Docs

:::{admonition} Witamy!
:class: tip
Ten przewodnik pomoże Ci rozpocząć pracę z dokumentacją OTClient v8 i systemem budowania opartym na Sphinx.
:::

## Wymagania

### Środowisko developerskie

- **Python 3.10+** – wymagane do budowania dokumentacji
- **Git** – do klonowania repozytorium
- **Edytor tekstu** – zalecamy VS Code z rozszerzeniem MyST

### Instalacja zależności

```bash
# Sklonuj repozytorium
git clone https://github.com/lukaszj321/otcv8-dev.git
cd otcv8-dev

# Zainstaluj zależności Python
pip install -r requirements-docs.txt

# (Opcjonalnie) RAG / wyszukiwanie semantyczne
pip install -r requirements-rag.txt
```

## Struktura dokumentacji

```
docs/
├── _static/          # Pliki statyczne (CSS, JS, obrazy)
├── _data/            # Dane CSV i JSON
├── _templates/       # Szablony Sphinx
├── api/              # Dokumentacja API (Lua/C++)
│   └── external/     # Synchronizowane API z głównego repozytorium
├── authoring/        # Rozdziały techniczne (01-15)
├── dashboard/        # Portal deweloperski
├── modules/          # Dokumentacja modułów Lua
├── ui/               # System OTUI
├── workbench/        # Szablony i przykłady
├── rag/              # Wyszukiwanie semantyczne
├── conf.py           # Konfiguracja Sphinx
└── index.md          # Strona główna
```

## Budowanie dokumentacji

### Lokalne budowanie

```bash
# Podstawowy build HTML
sphinx-build -b html docs docs/_build/html

# Z ostrzeżeniami (zalecane)
sphinx-build -b html -W docs docs/_build/html

# Sprawdzenie linków
sphinx-build -b linkcheck docs docs/_build/linkcheck
```

### Podgląd w przeglądarce

```bash
# Uruchom lokalny serwer
cd docs/_build/html
python -m http.server 8000

# Otwórz w przeglądarce:
# http://localhost:8000
```

### Live reload (opcjonalnie)

```bash
# Zainstaluj sphinx-autobuild
pip install sphinx-autobuild

# Uruchom z auto-odświeżaniem
sphinx-autobuild docs docs/_build/html
# Otwórz: http://localhost:8000
```

## Edycja dokumentacji

### Format MyST Markdown

Dokumentacja używa **MyST** (Markedly Structured Text) – rozszerzonego Markdown kompatybilnego ze Sphinx.

#### Podstawowy przykład

```markdown
# Nagłówek H1

## Nagłówek H2

Zwykły tekst z **pogrubieniem** i *kursywą*.

- Lista punktowana
- Drugi element

1. Lista numerowana
2. Drugi element

```python
# Blok kodu
def hello():
    print("Hello, OTClient v8!")

#### Dyrektywy Sphinx

```markdown
:::{admonition} Tytuł
:class: tip
Treść admonition
:::

:::{note}
Notatka
:::

:::{warning}
Ostrzeżenie
:::
```

#### Linki krzyżowe

```markdown
# Link do innego dokumentu
{doc}`../api/index`

# Link do sekcji
{ref}`moja-sekcja`

# Definicja sekcji
(moja-sekcja)=
## Tytuł sekcji
```

#### Diagramy Mermaid

```markdown
\```{mermaid}
%%{init: {'theme':'dark'}}%%
flowchart LR
    A[Start] --> B[Process]
    B --> C[End]
\```
```

### Szablony i przykłady

Zobacz:
- {doc}`../workbench/index` – Szablony modułów i UI
- {doc}`../workbench/example_health_monitor` – Kompletny przykład modułu
- {doc}`../authoring/index` – Rozdziały techniczne

## Deploy na GitHub Pages

### Automatyczny deploy (CI)

Workflow `.github/workflows/sphinx-pages.yml` automatycznie:
1. Buduje dokumentację na każdy push do `master`/`main`
2. Synchronizuje API z głównego repozytorium
3. Publikuje na GitHub Pages

### Ręczny deploy

```bash
# Trigger workflow z GitHub UI
# Actions → Build & Deploy Docs (Sphinx) → Run workflow
```

### URL dokumentacji

Po zdeployowaniu dokumentacja będzie dostępna pod:
```
https://lukaszj321.github.io/otcv8-dev/
```

## Narzędzia developerskie

### Generowanie stron authoring

```bash
# Automatycznie tworzy strony z rozdziałów 01-15
python scripts/build_authoring_pages.py
```

### Naprawa diagramów Mermaid

```bash
# Poprawia klikalne linki w diagramach
python scripts/patch_diagrams_clicks.py
```

### RAG – indeksowanie

```bash
# Buduj indeks wyszukiwania semantycznego
python tools/rag_index.py \
  --paths docs api modules \
  --out docs/rag/rag_index.faiss \
  --meta docs/rag/rag_meta.json
```

## Rozwiązywanie problemów

### Build nie działa

```bash
# Sprawdź wersje pakietów
pip list | grep -i sphinx

# Reinstaluj zależności
pip install -r requirements-docs.txt --force-reinstall

# Wyczyść cache
rm -rf docs/_build
```

### Błędy Mermaid

Sprawdź czy:
- Pierwsza linia ma `%%{init: ...}%%`
- Używasz poprawnej składni (flowchart, sequenceDiagram, etc.)
- Brak znaków Unicode w ID węzłów

### Problemy z linkami

```bash
# Uruchom linkcheck
sphinx-build -b linkcheck docs docs/_build/linkcheck
cat docs/_build/linkcheck/output.txt
```

## Następne kroki

- 📖 Przejrzyj {doc}`../api/index` – dokumentację API
- 🧩 Zobacz {doc}`../modules/index` – dostępne moduły
- 🎨 Poznaj {doc}`../ui/index` – system OTUI
- 🔍 Przetestuj {doc}`../rag/index` – wyszukiwanie semantyczne
- 🧪 Stwórz własny moduł używając {doc}`../workbench/index`

## Pomoc i wsparcie

- **GitHub Issues**: [github.com/lukaszj321/otcv8-dev/issues](https://github.com/lukaszj321/otcv8-dev/issues)
- **Dokumentacja Sphinx**: [sphinx-doc.org](https://www.sphinx-doc.org/)
- **MyST Parser**: [myst-parser.readthedocs.io](https://myst-parser.readthedocs.io/)

---
