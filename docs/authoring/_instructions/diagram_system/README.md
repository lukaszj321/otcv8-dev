# System Projektowania Diagramów: Przewodnik dla Twórców

## 1. Wprowadzenie

Witaj w systemie projektowania diagramów. Ten zbiór dokumentów stanowi kompletny przewodnik do tworzenia spójnych, czytelnych i semantycznie bogatych diagramów Mermaid dla naszego projektu. Został zaprojektowany tak, aby mógł być interpretowany zarówno przez ludzi, jak i przez zautomatyzowanych agentów AI.

**Celem tego systemu jest transformacja diagramów z pasywnych ilustracji w aktywne narzędzia inżynierskie.**

## 2. Struktura Systemu

Ten system składa się z trzech fundamentalnych filarów, które razem tworzą kompletny, hierarchiczny framework:

*   **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**: **"Dlaczego?"** - Definiuje nasze podstawowe zasady myślowe. Przeczytaj go, aby zrozumieć, co sprawia, że diagram jest skuteczny.

*   **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)**: **"Jak ma wyglądać?"** - Ścisła specyfikacja techniczna wszystkich elementów wizualnych (kolory, ikony, style). To jest Twoja paleta narzędzi.

*   **[Biblioteka Wzorców Projektowych](./03_DESIGN_PATTERNS/) (`03_DESIGN_PATTERNS/`)**: **"Jak to zrobić?"** - Zbiór gotowych do użycia, praktycznych wzorców. Działa jak "książka kucharska" dla twórców diagramów. Składa się z następujących plików:
    *   **[README.md](./03_DESIGN_PATTERNS/README.md):** Główny **spis treści** i przewodnik po całej bibliotece wzorców. **Zawsze zaczynaj tutaj.**
    *   **[A_Flows_and_Processes.md](./03_DESIGN_PATTERNS/A_Flows_and_Processes.md):** Wzorce do wizualizacji dynamicznych procesów, logiki i interakcji w czasie (`flowchart`, `sequenceDiagram`, etc.).
    *   **[B_Structure_and_Relations.md](./03_DESIGN_PATTERNS/B_Structure_and_Relations.md):** Wzorce do pokazywania statycznej architektury i relacji (`classDiagram`, `erDiagram`).
    *   **[C_Time_and_Planning.md](./03_DESIGN_PATTERNS/C_Time_and_Planning.md):** Wzorce do wizualizacji harmonogramów i zdarzeń w czasie (`gantt`, `timeline`).
    *   **[D_Data_and_Analysis.md](./03_DESIGN_PATTERNS/D_Data_and_Analysis.md):** Wzorce do prezentacji danych ilościowych i analizy strategicznej (`pie`, `quadrantChart`).
    *   **[E_Advanced_Techniques.md](./03_DESIGN_PATTERNS/E_Advanced_Techniques.md):** Wzorce pokazujące, jak łączyć różne typy diagramów w spójne systemy.

## 3. Proces Tworzenia Wizualizacji: Algorytm dla AI i Deweloperów

Aby stworzyć nową wizualizację, postępuj zgodnie z poniższym, strategicznym procesem. Na końcu tego dokumentu znajduje się **[Checklista Jakości](#4-checklista-jakości-diagramu)**, której należy użyć do weryfikacji finalnego rezultatu.

### Krok 1: Analiza i Definicja Celu
Zanim napiszesz kod, odpowiedz: Co chcę pokazać? Jaka jest główna "historia"? Do której warstwy architektonicznej należy główny komponent?

### Krok 2: Wybór Strategii — Jeden Diagram czy System Diagramów?
To jest najważniejsza decyzja projektowa. Zgodnie z naszą Złotą Regułą: **Nigdy nie twórz "Boskiego Diagramu"**.

*   **Scenariusz A (Prosty):** Tworzysz jeden, skupiony diagram.
*   **Scenariusz B (Złożony):** Projektujesz system połączonych diagramów (np. `overview` + `details`).

### Krok 3: Wybór Wzorca Projektowego
Przejdź do **[indeksu biblioteki wzorców](./03_DESIGN_PATTERNS/README.md)**, wybierz odpowiednią kategorię i plik, a następnie zaadaptuj wariant, który najlepiej pasuje do diagramu, który aktualnie tworzysz.

### Krok 4: Implementacja i Zastosowanie Stylu
Napisz kod Mermaid, implementując strukturę z wzorca i stosując style z **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)**.

### Krok 5: Przegląd i Refaktoryzacja
Sprawdź, czy diagram jest czytelny i zgodny z zasadami z **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**.

### Krok 6: Kompozycja Wizualna (dla Scenariusza B)
Jeśli projektujesz system diagramów, zaplanuj, jak zostaną one ułożone na stronie, używając jednej z technik kompozycji (np. Wiele Perspektyw, Deska Rozdzielcza).

---

## 4. Mapping Treści → Typ Diagramu

Wybór odpowiedniego typu diagramu Mermaid jest kluczowy dla skutecznej komunikacji. Poniższe heurystyki pomagają zautomatyzować ten proces:

### 4.1. Heurystyki Wyboru Typu Diagramu

| Typ Treści | Rekomendowany Diagram | Wskaźniki Kluczowe |
| :--------- | :-------------------- | :----------------- |
| **Przepływ sterowania / logika** | `flowchart` | Słowa: "jeśli", "pętla", "decyzja", "wywołanie", "zwraca" |
| **Interakcja czasowa** | `sequenceDiagram` | Słowa: "klient-serwer", "request-response", "asynchroniczny", "callback" |
| **Zmiana stanu** | `stateDiagram-v2` | Słowa: "stan", "przejście", "aktywny", "nieaktywny", "lifecycle" |
| **Relacje między encjami** | `erDiagram` lub `flowchart` z `classDef` | Słowa: "ma wiele", "należy do", "one-to-many", "foreign key" |
| **Hierarchia konceptów** | `mindmap` | Słowa: "kategorie", "taksonomia", "struktura tematów" |
| **Harmonogram / timeline** | `gantt` lub `timeline` | Daty, milestones, zakresy czasowe |
| **Proporcje / udział** | `pie` | Wartości procentowe, podziały kategorii |
| **Przepływ zasobów z wielkościami** | `sankey-beta` | Liczby reprezentujące przepływ między węzłami |
| **Historia Git** | `gitGraph` | Commity, branche, merge |

### 4.2. Decyzja: Jeden Diagram vs System Diagramów

**Pytania prowadzące:**
- Czy diagram ma więcej niż 15-20 węzłów? → Rozważ podział na `overview` + szczegóły
- Czy opisujesz wielowarstwową architekturę? → System diagramów (jeden per warstwa)
- Czy masz zarówno strukturę statyczną, jak i dynamiczny przepływ? → Dwa osobne diagramy

---

## 5. Obsługa Placeholderów i Brakujących Plików

### 5.1. Pliki `.mmd` vs Bloki Wbudowane

**Zasada:** Diagramy Mermaid mogą być przechowywane jako:
- **Pliki `.mmd`** w katalogu `diagrams/` (dla dużych, reużywalnych diagramów)
- **Bloki wbudowane** w dokumentacji Markdown (dla prostych, kontekstowych wizualizacji)

### 5.2. Gdy Plik Diagramu Nie Istnieje

Jeśli dokumentacja referencuje nieistniejący plik diagramu (np. `diagrams/missing.mmd`):

1. **Wygeneruj placeholder z metadanymi:**
   ```mermaid
   %%{init: {'theme': 'dark'}}%%
   graph TD
       TODO["🚧 Diagram do wygenerowania"]
       style TODO fill:#f59e0b,stroke:#fff,color:#000
   ```

2. **Dodaj komentarz w pliku Markdown:**
   ```markdown
   <!-- TODO: Diagram 'missing.mmd' oczekuje na wygenerowanie. Zobacz docs/authoring/_instructions/diagram_system/ -->
   ```

3. **Utwórz issue tracking** (opcjonalnie) z etykietą `documentation` i `diagram-needed`.

### 5.3. Marker Automatycznie Generowanych Bloków

Każdy diagram wygenerowany automatycznie (przez agenta lub skrypt) MUSI zawierać:

```markdown
<!-- AUTO-GENERATED: Do not edit manually. Source: [ścieżka/skrypt] | Generated: 2025-11-07T07:42:00Z -->
```mermaid
...
```
<!-- END AUTO-GENERATED -->
```

**Idempotencja:** Ponowne uruchomienie generatora na tym samym źródle powinno dać identyczny wynik (deterministyczne ID węzłów, stabilna kolejność).

---

## 6. Specyfikacja Frontmatter dla Plików `.mmd`

Każdy samodzielny plik `.mmd` w katalogu `diagrams/` POWINIEN zaczynać się od komentarza YAML frontmatter:

```yaml
---
# Diagram Metadata
diagram_id: "core_architecture_overview"
title: "Core Engine Architecture"
type: "flowchart"
layers: ["core", "subsystem"]
created: "2025-01-15"
last_updated: "2025-11-07T07:42:26Z"
author: "authoring-agent"
description: "High-level overview of core engine components and their dependencies"
related_docs:
  - "docs/authoring/01_core/README.md"
  - "docs/authoring/01_runtime/README.md"
tags: ["architecture", "core", "engine"]
---
```

### 6.1. Wymagane Pola

| Pole | Typ | Opis |
| :--- | :-- | :--- |
| `diagram_id` | string | Unikalny identyfikator (kebab-case) |
| `title` | string | Tytuł czytelny dla człowieka |
| `type` | string | Typ Mermaid (`flowchart`, `sequenceDiagram`, etc.) |
| `last_updated` | ISO 8601 | Data ostatniej modyfikacji w formacie `YYYY-MM-DDTHH:MM:SSZ` |

### 6.2. Opcjonalne Pola

- `layers`: Lista warstw architektonicznych (`["core", "ui"]`)
- `created`: Data utworzenia (format `YYYY-MM-DD`)
- `author`: Autor lub narzędzie (`"authoring-agent"`, `"manual"`)
- `description`: Krótki opis (1-2 zdania)
- `related_docs`: Lista ścieżek powiązanych dokumentów
- `tags`: Lista tagów dla kategoryzacji

**Uwaga:** Frontmatter w `.mmd` jest **komentarzem** (nie wpływa na renderowanie), ale umożliwia automatyczną walidację i tracking.

---

## 7. Wersja Mermaid i Kompatybilność Rendererów

### 7.1. Środowiska Renderowania

| Środowisko | Wersja Mermaid | Uwagi |
| :--------- | :------------- | :---- |
| **GitHub (readme/docs)** | ~10.6.x | Ograniczone wsparcie dla `classDef` w niektórych typach |
| **Sphinx (myst-parser)** | ~10.x | Wymaga `sphinxcontrib-mermaid` |
| **VS Code (Preview)** | Zależna od rozszerzenia | Rekomendacja: Mermaid Preview extension |
| **mermaid-cli** | Latest (11.x+) | Narzędzie do lokalnej walidacji i renderowania |

### 7.2. Typy Diagramów - Wsparcie `classDef`

| Typ Diagramu | `classDef` GitHub | `classDef` Sphinx | Alternatywa |
| :----------- | :---------------- | :---------------- | :---------- |
| `flowchart` / `graph` | ✅ Pełne | ✅ Pełne | - |
| `sequenceDiagram` | ❌ Brak | ❌ Brak | Użyj `themeVariables` w `init` |
| `stateDiagram-v2` | ✅ Częściowe | ✅ Częściowe | Używaj modyfikatorów stanu |
| `erDiagram` | ❌ Brak | ❌ Brak | Użyj `themeVariables` |
| `mindmap` | ❌ Brak | ❌ Brak | Inline HTML hack (`<font>`) |
| `pie`, `gantt`, `timeline` | ⚠️ Minimalne | ⚠️ Minimalne | Polegaj na domyślnym motywie `dark` |

### 7.3. Reguła Kompatybilności

**Jeśli diagram nie renderuje się poprawnie w GitHub, jest on błędny.** GitHub jest naszym primary target.

---

## 8. Walidacja i CI

### 8.1. Lokalna Walidacja

**Narzędzia:**
- **mermaid-cli** (`mmdc`): `npm install -g @mermaid-js/mermaid-cli`
  ```bash
  mmdc -i diagrams/example.mmd -o /tmp/example.png
  ```
- **mermaid-lint** (jeśli dostępny): Sprawdza składnię i style

**Skrypt bash dla batch validation:**
```bash
#!/bin/bash
# validate_diagrams.sh
set -e
for file in docs/authoring/_instructions/diagram_system/**/*.mmd; do
  echo "Validating $file..."
  mmdc -i "$file" -o "/tmp/$(basename $file .mmd).png" || echo "ERROR: $file failed"
done
```

### 8.2. GitHub Actions - Propozycja Workflow

**Plik:** `.github/workflows/validate-diagrams.yml`

```yaml
name: Validate Mermaid Diagrams

on:
  pull_request:
    paths:
      - 'docs/**/*.mmd'
      - 'docs/**/*.md'
  push:
    branches: [main, develop]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install mermaid-cli
        run: npm install -g @mermaid-js/mermaid-cli
      
      - name: Find and validate .mmd files
        run: |
          find docs -name "*.mmd" | while read file; do
            echo "Validating $file"
            mmdc -i "$file" -o "/tmp/$(basename $file .mmd).png" || exit 1
          done
      
      - name: Check frontmatter in .mmd files
        run: |
          python3 scripts/validate_diagram_metadata.py docs/
```

**Skrypt Python dla sprawdzania frontmatter:** `scripts/validate_diagram_metadata.py`

```python
#!/usr/bin/env python3
import sys
import re
from pathlib import Path
from datetime import datetime

REQUIRED_FIELDS = ['diagram_id', 'title', 'type', 'last_updated']

def validate_frontmatter(file_path):
    content = file_path.read_text()
    
    # Extract frontmatter (between first two '---')
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return f"Missing frontmatter in {file_path}"
    
    frontmatter = match.group(1)
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if f"{field}:" not in frontmatter:
            return f"Missing required field '{field}' in {file_path}"
    
    # Validate ISO 8601 date format for last_updated
    date_match = re.search(r'last_updated:\s*"([^"]+)"', frontmatter)
    if date_match:
        try:
            datetime.fromisoformat(date_match.group(1).replace('Z', '+00:00'))
        except ValueError:
            return f"Invalid ISO 8601 date in {file_path}: {date_match.group(1)}"
    
    return None

def main(docs_dir):
    errors = []
    for mmd_file in Path(docs_dir).rglob('*.mmd'):
        error = validate_frontmatter(mmd_file)
        if error:
            errors.append(error)
    
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    else:
        print("All diagrams validated successfully!")

if __name__ == "__main__":
    main(sys.argv[1])
```

### 8.3. Pre-commit Hook (Opcjonalnie)

**Plik:** `.git/hooks/pre-commit` (lub używając `pre-commit` framework)

```bash
#!/bin/bash
# Validate only staged .mmd files
for file in $(git diff --cached --name-only --diff-filter=ACM | grep '\.mmd$'); do
  mmdc -i "$file" -o "/tmp/$(basename $file .mmd).png" || exit 1
done
```

---

## 9. Checklista Jakości Diagramu

Użyj tej checklisty przed zatwierdzeniem każdego nowego diagramu. Diagram jest gotowy, jeśli możesz odpowiedzieć "TAK" na wszystkie poniższe pytania.

### Część 1: Filozofia i Cel
-   [ ] **Jedna Historia:** Czy diagram opowiada jedną, jasno zdefiniowaną historię?
-   [ ] **Czytelność w 5 Sekund:** Czy główny cel i kluczowe komponenty są zrozumiałe na pierwszy rzut oka?
-   [ ] **Wartość Dodana:** Czy diagram wizualizuje coś, czego nie widać od razu po przeczytaniu kodu (np. relacje, przepływy)?
-   [ ] **Odpowiednie Narzędzie:** Czy typ diagramu (np. `flowchart`, `sequenceDiagram`) jest właściwie dobrany do "historii", którą opowiada?

### Część 2: Zgodność z Systemem Wizualnym
-   [ ] **Globalny `init`:** Czy diagram zaczyna się od standardowego bloku `%%{init: {'theme': 'dark', ...}}%%`?
-   [ ] **Kolory Warstw:** Czy wszystkie węzły `graph` mają poprawnie przypisany kolor warstwy architektonicznej (np. `core`, `game`, `ui`)?
-   [ ] **Ikony Komponentów:** Czy kluczowe węzły mają przypisane ikony (`fa-...`) zgodnie z ich techniczną rolą?
-   [ ] **Style Linii:** Czy style linii (`-->`, `-.->`, `==>`) i ich kolory (`linkStyle`) są użyte poprawnie i zgodnie ze znaczeniem?
-   [ ] **Zgodność z Ograniczeniami:** Czy diagram przestrzega ograniczeń stylizacji dla swojego typu (np. nie używa `classDef` w `sequenceDiagram`)?

### Część 3: Poprawność i Kompletność
-   [ ] **Renderowanie:** Czy diagram renderuje się poprawnie bez błędów parsera?
-   [ ] **Poprawność Merytoryczna:** Czy diagram wiernie odzwierciedla działanie lub strukturę opisywanego systemu?
-   [ ] **Interaktywność:** Czy kluczowe komponenty mają dodane linki `click` (jeśli są wspierane) do odpowiedniej dokumentacji?
-   [ ] **Kontekst:** Czy pod diagramem (lub w jego tytule) znajduje się krótki opis wyjaśniający, co on przedstawia i jaka jest używana jednostka (dla diagramów analitycznych)?

### Część 4: Metadane i Tracking
-   [ ] **Frontmatter:** Czy plik `.mmd` zawiera kompletny frontmatter z wymaganymi polami?
-   [ ] **ISO 8601 Date:** Czy pole `last_updated` używa formatu ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`)?
-   [ ] **Marker Generacji:** Czy automatycznie wygenerowane diagramy mają marker `<!-- AUTO-GENERATED -->`?
-   [ ] **Idempotencja:** Czy ponowne wygenerowanie daje identyczny rezultat?

### Część 5: Kompozycja (jeśli dotyczy)
-   [ ] **Podział Złożoności:** Jeśli diagram jest bardzo skomplikowany, czy na pewno nie powinien być podzielony na mniejszy system `overview` + `details`?
-   [ ] **Spójność Systemu:** Jeśli diagram jest częścią większego systemu wizualizacji, czy jego linki i narracja są spójne z pozostałymi częściami?

### Część 6: Walidacja Techniczna
-   [ ] **Lokalna Walidacja:** Czy diagram przeszedł walidację przez `mmdc` (mermaid-cli)?
-   [ ] **GitHub Rendering:** Czy diagram renderuje się poprawnie w GitHub preview?
-   [ ] **Brak Antywzorców:** Czy diagram unika znanych pułapek składni (cudzysłowy w etykietach, niestandardowe groty strzałek)?
