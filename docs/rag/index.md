# RAG – wyszukiwanie semantyczne

Ten rozdział opisuje **indeksowanie** i **zapytania**.

## Instalacja (opcjonalny zestaw)
```bash
pip install -r requirements-rag.txt
```

## Budowa indeksu
```bash
python tools/rag_index.py --paths docs api --out rag_index.faiss --meta rag_meta.json
```

## Zapytanie
```bash
python tools/rag_query.py --index rag_index.faiss --meta rag_meta.json --q "jak wywołać hook X?"
```

:::{note}
To działa **poza Sphinxem**. Wyniki możesz wkleić do dokumentacji lub zintegrować jako statyczną stronę Q&A.
:::
