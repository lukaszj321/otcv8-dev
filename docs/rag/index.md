# RAG – Wyszukiwanie semantyczne i indeksowanie

:::{admonition} Co to jest RAG?
:class: tip
RAG (Retrieval-Augmented Generation) to system wyszukiwania semantycznego wykorzystujący embeddingi do znalezienia najbardziej relevantnych fragmentów dokumentacji. Pozwala na inteligentne przeszukiwanie całej bazy wiedzy projektu.
:::

## Przegląd systemu

System RAG w OTClient v8 składa się z:

- **Indeksu embeddingów** – przechowuje wektorowe reprezentacje dokumentów
- **Metadanych** – informacje o źródłach i kontekście
- **Silnika zapytań** – wyszukuje najbardziej podobne fragmenty
- **Interfejsu wyszukiwania** – dostępny przez HTML lub CLI

## Instalacja

### Wymagane zależności

```bash
# Zainstaluj pakiety RAG
pip install -r requirements-rag.txt
```

Plik `requirements-rag.txt` zawiera:
- `sentence-transformers` – generowanie embeddingów
- `faiss-cpu` lub `faiss-gpu` – szybkie wyszukiwanie wektorowe
- `numpy` – operacje numeryczne

## Budowa indeksu

### Podstawowe użycie

```bash
# Zbuduj indeks z dokumentacji
python tools/rag_index.py \
  --paths docs api modules \
  --out docs/rag/rag_index.faiss \
  --meta docs/rag/rag_meta.json
```

### Parametry

- `--paths` – katalogi do zindeksowania (docs, api, modules, etc.)
- `--out` – ścieżka wyjściowa dla indeksu FAISS
- `--meta` – ścieżka do pliku metadanych JSON
- `--model` – (opcjonalny) model embeddingów (domyślnie: `all-MiniLM-L6-v2`)
- `--chunk-size` – (opcjonalny) rozmiar fragmentów tekstu (domyślnie: 512)

### Przykład z dodatkowymi opcjami

```bash
python tools/rag_index.py \
  --paths docs api \
  --out rag_index.faiss \
  --meta rag_meta.json \
  --model sentence-transformers/all-mpnet-base-v2 \
  --chunk-size 1024
```

## Zapytania

### Z linii poleceń

```bash
# Wyszukaj informacje o hookach
python tools/rag_query.py \
  --index docs/rag/rag_index.faiss \
  --meta docs/rag/rag_meta.json \
  --q "jak wywołać hook X?" \
  --top-k 5
```

### Interaktywny tryb

```bash
# Uruchom w trybie interaktywnym
python tools/rag_query.py \
  --index docs/rag/rag_index.faiss \
  --meta docs/rag/rag_meta.json \
  --interactive
```

### Interfejs HTML

Dostępny plik `search.html` w katalogu `docs/rag/` umożliwia przeszukiwanie przez przeglądarkę:

```bash
# Uruchom lokalny serwer
cd docs/rag
python -m http.server 8080
# Otwórz: http://localhost:8080/search.html
```

## Przykładowe zapytania

### Znajdowanie funkcji API

```
Q: "funkcje do zarządzania inventory"
→ Znajdzie: dokumentację modułu game_inventory, funkcje Lua dla inwentarza
```

### Znajdowanie przykładów

```
Q: "przykład tworzenia OTUI window"
→ Znajdzie: szablony OTUI, przykłady z modułów, tutoriale
```

### Rozwiązywanie problemów

```
Q: "błąd połączenia z serwerem"
→ Znajdzie: dokumentację network, troubleshooting, logi
```

## Struktura embeddingów

Aktualny plik `embeddings.json` zawiera:
- **~6.8 MB** wektorowych reprezentacji
- **2493** zindeksowanych dokumentów
- Pokrycie: API, moduły, UI, core, network, assets

## Aktualizacja indeksu

Indeks należy przebudować po:
- Dodaniu nowej dokumentacji
- Znaczących zmianach w istniejących plikach
- Zmianie modelu embeddingów

```bash
# Automatyczna aktualizacja w CI
# (zobacz .github/workflows/sphinx-pages.yml)
```

## Integracja z dokumentacją

Wyniki RAG można zintegrować jako:

1. **Statyczna strona Q&A** – pre-generowane odpowiedzi na częste pytania
2. **Sugestie linków** – automatyczne podpowiedzi w dokumentacji
3. **Tooltips** – kontekstowa pomoc w UI dokumentacji
4. **API endpoint** – serwis wyszukiwania dla zewnętrznych narzędzi

:::{note}
System RAG działa **niezależnie od Sphinx**. Można go używać offline lub zintegrować z własnymi narzędziami developerskimi.
:::

## Zaawansowane użycie

### Custom model embeddingów

```python
from sentence_transformers import SentenceTransformer

# Załaduj własny model
model = SentenceTransformer('path/to/your/model')
# Użyj w rag_index.py z parametrem --model
```

### Filtrowanie wyników

```python
# Filtruj wyniki po typie dokumentu
results = query(text="...", filters={"type": "api"})
```

### Eksport wyników

```bash
# Eksportuj wyniki do JSON
python tools/rag_query.py \
  --index rag_index.faiss \
  --meta rag_meta.json \
  --q "query" \
  --format json \
  --output results.json
```

## Zobacz też

- {doc}`../api/index` – Dokumentacja API
- {doc}`../modules/index` – Dokumentacja modułów
- {doc}`../workbench/index` – Przykłady i szablony
- [Sentence Transformers](https://www.sbert.net/) – Dokumentacja biblioteki
- [FAISS](https://faiss.ai/) – Biblioteka wyszukiwania wektorowego

