# OTClient v8 - Dokumentacja Techniczna + RAG

Automatycznie generowana dokumentacja techniczna i zbiory RAG dla OTClient v8.

## Struktura

```
docs/reposzablony/
├── 01_core/api/          # Dokumentacja API C++
│   ├── cpp/              # Pliki MD (195 plików)
│   └── diagrams/         # Diagramy klas (178 plików .mmd)
├── 03_modules/lua/       # Dokumentacja modułów Lua (188 plików)
├── 04_ui/                # Dokumentacja interfejsu OTUI
│   ├── otui/             # Pliki MD (133 pliki)
│   └── diagrams/         # Diagramy hierarchii (76 plików .mmd)
├── 05_events/            # Indeks zdarzeń
│   └── index.md          # 1506 wykrytych zdarzeń
├── datasets/             # Zbiory RAG
│   ├── api.{csv,ndjson}       # 5674 rekordy (C++ API)
│   ├── ui.{csv,ndjson}        # 1035 rekordów (OTUI)
│   ├── modules.{csv,ndjson}   # 3642 rekordy (Lua)
│   ├── events.{csv,ndjson}    # 1506 rekordów (zdarzenia)
│   └── chunks/                # Rotacja plików >50MB
├── qa/                   # Raporty QA
│   ├── frontmatter_issues.csv
│   ├── chunking_report.csv
│   ├── link_lint.csv
│   ├── dataset_sanity.csv
│   ├── diagram_lint.csv
│   ├── idempotency.md
│   └── qa_summary.md
├── analytics/            # Raporty analityczne
│   ├── coverage.csv           # Pokrycie dokumentacją
│   ├── gaps.csv               # Braki
│   ├── xref_stats.csv         # Statystyki relacji
│   ├── coverage_matrix.md     # Macierz moduł×artefakt
│   ├── overview.mmd           # Diagram architektury
│   ├── run_summary.json       # Metryki zbiorcze
│   └── errors.md              # Agregacja błędów
├── _tools/               # Narzędzia generacji
│   ├── cpp_doc_generator.py
│   ├── lua_doc_generator.py
│   ├── otui_doc_generator.py
│   ├── events_doc_generator.py
│   ├── rag_datasets_generator.py
│   ├── qa_checker.py
│   ├── analytics_generator.py
│   └── README.md
└── _shared/lua/          # Współdzielone narzędzia
    └── docio.lua         # IO dla ekstraktorów Lua
```

## Statystyki

- **Plików dokumentacji:** 532 (517 głównych + 15 pomocniczych)
- **C++ API:** 195 plików
- **Lua modułów:** 188 plików
- **OTUI widgetów:** 133 pliki
- **Diagramów:** 254 (178 C++ + 76 OTUI)
- **Rekordów RAG:** 11,857
- **Chunków:** 9,809
- **Wykrytych zdarzeń:** 1,506
- **Rozmiar datasets:** 8.4 MB

## Frontmatter

Każdy plik MD zawiera metadane YAML:

```yaml
---
doc_id: "<stable-id>"              # Stabilny identyfikator
source_path: "<repo-rel-path>"     # Ścieżka do źródła
source_sha: "<git-sha>"            # Git SHA (śledzenie zmian)
last_sync_iso: "2025-10-09T..."    # Timestamp synchronizacji
doc_class: "api|ui|spec|guide"     # Kategoria dokumentu
language: "pl"                      # Język dokumentacji
title: "<title>"                    # Tytuł
summary: "<1-2 zdania>"            # Podsumowanie
tags: ["tag1", "tag2"]             # Tagi do filtrowania
---
```

## Chunkowanie dla RAG

- **Limit:** ≤ 1200 tokenów na chunk
- **Overlap:** ~10% między chunkami
- **Granice:** Nagłówki H2-H4
- **Ochrona:** Nie dzielimy tabel i bloków kodu

## Użycie

### Regeneracja dokumentacji

```bash
cd docs/reposzablony/_tools

# C++ API
python3 cpp_doc_generator.py --source-dir ../../../src

# Lua modułów
python3 lua_doc_generator.py

# OTUI widgetów
python3 otui_doc_generator.py

# Zdarzenia
python3 events_doc_generator.py

# Datasets RAG
python3 rag_datasets_generator.py

# QA
python3 qa_checker.py

# Analytics
python3 analytics_generator.py
```

### Wyszukiwanie w datasets

**CSV (Excel, BI tools):**
```bash
# Znajdź wszystkie API C++ dla animacji
grep -i "animation" datasets/api.csv
```

**NDJSON (RAG systems):**
```bash
# Znajdź chunki o widgetach
jq 'select(.doc_class == "ui")' datasets/ui.ndjson
```

### Integracja z RAG

Datasets są gotowe do użycia w:
- Semantic search (vector DB)
- Retrieval-Augmented Generation (RAG)
- Fine-tuning modeli
- Business Intelligence

Format NDJSON zawiera:
- `chunk_id` - unikalny ID chunku
- `content_full` - pełna treść
- `doc_id`, `source_path`, `source_sha` - metadane
- `doc_class`, `language` - kategorie
- `chunk_index`, `chunk_count` - pozycja w dokumencie

## QA Status

- ✅ **Frontmatter:** 98% poprawnych (507/517)
- ⚠️ **Chunking:** 27 sekcji nieznacznie powyżej limitu (akceptowalne)
- ⚠️ **Links:** 402 brakujących cross-references (do uzupełnienia)
- ✅ **Datasets:** Wszystkie prawidłowe
- ✅ **Diagrams:** Wszystkie w limicie 80 linii
- ✅ **Idempotencja:** PASS (generator sprawdza treść przed zapisem)

## Utrzymanie

Wszystkie generatory są **idempotentne** - można je uruchamiać wielokrotnie bez powodowania zmian, jeśli źródła się nie zmieniły.

System automatycznie:
- Porównuje treść przed zapisem
- Ekstrahuje Git SHA dla śledzenia zmian
- Ustawia timestampy ISO
- Dzieli duże pliki (rotacja >50MB)
- Generuje raporty QA i analytics

## Wymagania

- Python 3.7+
- Git (do ekstrakcji SHA)
- UTF-8, LF line endings

## Licencja

Zgodna z OTClient v8

## Kontakt

Zobacz główny README projektu OTClient v8.
