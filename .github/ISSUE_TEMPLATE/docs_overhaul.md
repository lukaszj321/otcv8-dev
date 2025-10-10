---
name: Docs Overhaul
about: Kompletny upgrade dokumentacji (PyData theme, RAG, API, Workbench)
title: "[Docs] Overhaul – v1"
labels: documentation, enhancement
assignees: ""
---

## Cel
Uporządkowana dokumentacja: opisowa + API + Workbench + RAG + CI sync.

## Zakres
- [ ] Struktura rozdziałów i TOC (H2/H3/H4 dla Sphinx)
- [ ] PyData Sphinx Theme (navbar, sidebar, search, light/dark)
- [ ] Dashboard startowy (grid, karty, linki)
- [ ] Integracja API (kopiowanie `api/*.md` → `docs/api/external/`)
- [ ] Workbench (szablony skryptów, checklisty, diagramy)
- [ ] CSV tabele (rejestr modułów/skryptów)
- [ ] Diagramy (Mermaid, poprawny dark mode)
- [ ] RAG (indeks + zapytania, FAISS / sentence-transformers)
- [ ] CI: build + deploy Pages
- [ ] Linki "Edit on GitHub", sitemap, opengraph, favicons
- [ ] Kontrola jakości (linkcheck, nitpicky)

## Akceptacja
- [ ] Buduje się `sphinx-build` lokalnie
- [ ] GH Pages zawiera pełny TOC i sekcje
- [ ] API synchronizowane w CI
- [ ] 1+ przykładowy skrypt w Workbench
- [ ] Działa wyszukiwarka i nagłówki

## Snippet do CI (sync API → docs)
Wklej przed krokiem builda:

```yaml
- name: Sync API docs into docs/api/external
  run: |
    mkdir -p docs/api/external/lua
    cp -f api/otcv8-full-api.md docs/api/external/ || true
    cp -f api/lua/luafunctions_client.md docs/api/external/lua/ || true
```

## Dodatkowe zadania
- [ ] Ustawić `mermaid_init_js` w `conf.py` dla dark mode (opcjonalnie)
- [ ] Dodać `sphinx-sitemap` i `robots.txt`
- [ ] Dodać `hoverxref` dla linków API