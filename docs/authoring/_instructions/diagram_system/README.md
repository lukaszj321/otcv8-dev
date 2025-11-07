# System Projektowania Diagramów: Przewodnik dla Twórców (zaktualizowane odwołania do narzędzi)

Ta wersja README zawiera kompletne wytyczne projektowe oraz precyzyjne odniesienia do narzędzi walidacyjnych i schematów, które znajdują się w repo. Zawiera instrukcje jak używać: JSON Schema frontmatter, konfiguracji `mermaid-lint`, skryptów do walidacji linków i normalizacji node-id.

Uwaga: wszystkie operacje walidacyjne (lint, render, link-check) wykonuj lokalnie lub w CI przed otwarciem PR; poniższe przykłady zakładają środowisko z Python 3.8+ i Node.js 18–20.

---

## Spis treści (skrót)
1. Wprowadzenie (filozofia i porządek plików)  
2. Gdzie znajdują się nowe pliki narzędzi i schematów  
3. Jak lokalnie zweryfikować frontmatter (JSON Schema)  
4. Jak uruchomić mermaid-lint z projektem (konfiguracja)  
5. Jak sprawdzić linki `click` (skrypt validate_diagram_links.py)  
6. Jak normalizować node-id (skrypt node_id_normalizer.py)  
7. Propozycja kroku CI (przykład workflow — dodawać tylko, gdy repo nie ma równoważnego)  
8. Zaktualizowana checklista i wskazówki PR

---

## 1. Przypomnienie kluczowych zasad
- Wszystkie diagramy Mermaid powinny używać canonical init header:
```text
%%{init: {'theme':'dark','themeVariables': {'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}, 'securityLevel':'loose'}}%%
```
- Każdy automatycznie wygenerowany blok musi mieć idempotency marker:
```text
<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=<40hex>; generated_at=<ISO8601> -->
```
- Frontmatter w plikach `.md` związanych z diagramami powinien być zgodny ze schematem JSON umieszczonym w repo.

---

## 2. Lokalizacje plików narzędzi i schematu (aktualne)
Uwaga: pliki zostały umieszczone w następujących ścieżkach w repo. README i przykłady uruchomień poniżej odnoszą się do tych ścieżek.

- JSON Schema frontmatter:
  - `docs/authoring/_instructions/diagram_system/frontmatter.schema.json`

- mermaid-lint configuration:
  - `docs/authoring/_instructions/diagram_system/.mermaid-lintrc`

- Skrypty narzędzi (validator i normalizer):
  - `docs/scripts/diagram-tools/validate_diagram_links.py`
  - `docs/scripts/diagram-tools/node_id_normalizer.py`

Upewnij się, że generator/CI odnosi się do dokładnie tych ścieżek (z prefiksem `docs/`).

---

## 3. Walidacja frontmatter (JSON Schema)

Plik schematu:
- `docs/authoring/_instructions/diagram_system/frontmatter.schema.json`

Jak zweryfikować frontmatter w plikach `.md`:
1. Wyodrębnij frontmatter YAML z nagłówka `---` w pliku `.md` (np. przy pomocy prostego skryptu Python albo narzędzia YAML).
2. Przekonwertuj YAML na JSON i użyj walidatora JSON Schema (np. `ajv` lub `jsonschema` w Pythonie) przeciw plikowi `frontmatter.schema.json`.

Przykładowe podejście z Pythonem:
- Parsuj frontmatter z pliku `.md` (biblioteka `python-frontmatter` lub własny parser).
- Waliduj z `jsonschema.validate(instance, schema)` przy użyciu pliku `docs/authoring/_instructions/diagram_system/frontmatter.schema.json`.

Zalecenie: uruchamiać walidację frontmatter w CI na wszystkich zmienionych plikach `.md` przed mergem.

---

## 4. mermaid-lint — konfiguracja i uruchomienie

Konfiguracja znajduje się w:
- `docs/authoring/_instructions/diagram_system/.mermaid-lintrc`

Przykładowe uruchomienie lokalne:
1. Zainstaluj mermaid-lint (globalnie lub jako devDependency):
   - `npm install -D @mermaid-js/mermaid-lint` (lub odpowiedni pakiet dla używanej wersji)
2. Jeśli masz pliki `.mmd`:
   - `npx mermaid-lint "docs/authoring/**/*.mmd"`
3. Jeżeli diagramy są osadzone w plikach `.md`, wyodrębnij bloki ```mermaid``` do tymczasowych `.mmd` lub użyj skryptu, który skanuje `.md` i uruchamia linter na fragmentach.

Zalecenie: dodać do CI krok uruchamiający mermaid-lint nad repozytorium diagramów.

---

## 5. Sprawdzanie linków `click` — validate_diagram_links.py

Skrypt:
- `docs/scripts/diagram-tools/validate_diagram_links.py`

Co robi:
- Przeszukuje pliki `.md` (domyślnie katalog `docs/`) i wyciąga wystąpienia `click NodeID "path" "tooltip"`.
- Dla relatywnych ścieżek sprawdza, czy plik istnieje (próbuje dopasować `.md` jeśli target wskazuje `.html`).
- Dla fragmentów `file#anchor` próbuje dopasować anchor do nagłówków w pliku `.md` (heurystyka slugify).
- Zwraca raport JSON (opcjonalnie) i kod wyjścia ≠0 jeśli wykryje braki.

Przykładowe użycie:
```bash
# z repo root
python3 docs/scripts/diagram-tools/validate_diagram_links.py docs --report /tmp/diagram_links_report.json
```

Interpretacja exit code:
- 0 — wszystkie linki znalezione,
- 2 — brakujące pliki,
- 3 — brakujące anchor-y (lub kombinacja z brakującymi plikami).

W CI: uruchom ten skrypt i wykorzystaj raport do generowania komentarzy/ostrzeżeń w PR lub do failowania jobu, jeśli chcesz.

---

## 6. Normalizacja node-id — node_id_normalizer.py

Skrypt:
- `docs/scripts/diagram-tools/node_id_normalizer.py`

Co robi:
- Normalizuje etykietę do bezpiecznego node-id: lowercase, spaces → underscore, usuwa niedozwolone znaki.
- Może skanować katalog (`--dir`) i wygenerować mapping oryginal → znormalizowany (przydatne przy masowych zmianach).

Przykłady:
```bash
# jednorazowo - zgeneruje normalized id dla etykiety
python3 docs/scripts/diagram-tools/node_id_normalizer.py "Game Engine v2"

# skanuje katalog i zapisuje mapę
python3 docs/scripts/diagram-tools/node_id_normalizer.py --dir docs/authoring --report /tmp/node_id_map.json
```

Generatorzy i skrypty aktualizujące diagramy powinni stosować tę normalizację lub identyczny algorytm, żeby zapewnić zgodność z regex `^[a-z0-9_:-]+$`.

---

## 7. Validate-diagrams CI — co jest w repo i jak postępować

W repo znajduje się zoptymalizowany workflow walidujący diagramy: `.github/workflows/validate-diagrams-docs.yml`.

Co robi ten workflow (skrót)
- uruchamia się tylko dla PR-ów zmieniających pliki w katalogu `docs` (paths filter),
- wykrywa zmienione pliki w PR i uruchamia kroki jedynie gdy dotyczy to `.md`/`.mmd`,
- używa cache npm i `npm ci` gdy repo zawiera `package.json`, w przeciwnym razie instaluje minimalne narzędzia globalnie,
- wykonuje `mermaid-lint`, sprawdza `click` targety (`validate_diagram_links.py`) i przeprowadza smoke‑render tylko dla zmienionych `.mmd`,
- instalacja zależności i renderowanie są pomijane dla PR‑ów z forków (bezpieczeństwo),
- stosuje `concurrency + cancel-in-progress` i upload‑uje raporty/artefakty (raport link‑check, SVG).

Zasady postępowania przy dodawaniu/zmianie workflow
1. Przed dodaniem nowego workflow sprawdź istniejące pliki w `.github/workflows` (szukaj: `mermaid`, `mmdc`, `mermaid-lint`, `validate-diagrams*`).  
2. Jeśli istnieje workflow o równoważnej funkcji — zamiast dodawać nowy plik, zaproponuj rozbudowę istniejącego (PR z opisem zmian i uzasadnieniem).  
3. Jeśli repo nie ma równoważnego workflow i zamierzasz dodać nowy, użyj obecnego pliku jako wzorca i przestrzegaj reguł: ograniczony trigger (paths), `concurrency`, zabezpieczenia dla forków, cache npm, minimalny zakres renderów.  
4. Przy modyfikacji workflow: opisz zmiany w README (ten punkt 7), przetestuj na prywatnej gałęzi lub wewnętrznym PR i zamieść w PR krótki raport co i dlaczego zostało zmienione.

Bezpieczeństwo i koszty — przypomnienie
- Nie uruchamiaj `npm ci` ani pełnego renderu dla PR‑ów z forków bez ochrony — uruchamiaj je tylko dla PR‑ów z tego repo albo w trybie report‑only dla forków.  
- Nie usuwaj `paths` ani `concurrency` bez uzasadnienia — to kluczowe dla ograniczenia niepotrzebnych uruchomień i kosztów.

---

## 8. Reguły dla LLM — generowanie diagramów bez skrótów

Poniższe zasady są obowiązujące dla agenta/LLM generującego bloki Mermaid. Eliminują skracanie list (np. „... 38 more”) i zapewniają pełne, walidowalne diagramy.

Zasady
- Zakaz skrótów: nie używaj „... N more”, „… N more” ani żadnych wielokropków w miejsce pełnych list.
- Wypisuj jawnie każdy węzeł i każde połączenie. Nie odwołuj się do „reszty”; wymień wszystkie elementy.
- Zwracaj wyłącznie poprawne, ogrodzone bloki Mermaid (```mermaid ... ```). Poza blokami dopuszczalny jest tylko krótki fallback Markdown dla linków `click`.
- Każdy blok musi zaczynać się od canonical init header:
```text
%%{init: {'theme':'dark','themeVariables': {'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}, 'securityLevel':'loose'}}%%
```
- Normalizacja identyfikatorów węzłów: lowercase; spacje → underscore; usuń znaki poza [a-z0-9_\-:]. Wymagany regex: `^[a-z0-9_:-]+$`.
- Długie etykiety łam za pomocą `<br/>` (maksymalnie 3 linie).
- Jeśli używasz `click`, pod blokiem dodaj sekcję „Powiązane dokumenty:” z listą tych samych linków (fallback).
- Próg czytelności: jeśli liczba węzłów > 12, podziel wynik:
  - 1 diagram „overview” (z grupowaniem/subgraph),
  - osobne diagramy „details” dla grup; żaden pojedynczy diagram nie może mieć > 12 węzłów.
- Jeśli nie możesz zwrócić pełnych danych z powodu limitu tokenów: nie używaj wielokropków. Zwróć zamiast tego dokładnie ten obiekt (poza blokami Mermaid) i przerwij:
```text
{"status":"truncated","reason":"token_limit","recommendation":"split_input","max_nodes":12}
```
- Nad każdym wygenerowanym blokiem dodaj marker idempotencji:
```text
<!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=<sha40>; generated_at=<ISO8601> -->
```
- Nie używaj mechanizmów pretty-print/inspect, które skracają kolekcje. Generuj zawartość diagramu przez jawne iteracje po elementach.

Wzorcowy fragment prompta (do użycia z LLM)
```text
Generate Mermaid diagrams under STRICT rules:
- DO NOT truncate/abbreviate. Do NOT output "... N more" or "… N more".
- Output ONLY valid fenced Mermaid code blocks (```mermaid ... ```). Optionally add a short Markdown fallback list for click links under the block.
- Each block must start with:
  %%{init: {'theme':'dark','themeVariables': {'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}, 'securityLevel':'loose'}}%%
- Normalize node ids (lowercase, spaces->underscore, allowed chars [a-z0-9_:-]).
- Wrap long labels with <br/> (max 3 lines).
- If using click, also include a Markdown "Powiązane dokumenty" list with the same targets below the block.
- If nodes > 12, split into one overview (with subgraphs) plus per-group details; no diagram > 12 nodes.
- If token limits prevent full output, DO NOT use ellipses. Output exactly:
  {"status":"truncated","reason":"token_limit","recommendation":"split_input","max_nodes":12}
- Prepend every block with:
  <!-- mermaid-diagram: generated-by=diagram-agent v1; source_sha=<sha40>; generated_at=<ISO8601> -->
- Do not output any other text outside the Mermaid blocks or the JSON truncation object.
```

---

## 9. Zaktualizowana checklista (wersja do stosowania przed PR)

- [ ] Wszystkie zmiany dotyczą wyłącznie `docs/authoring/**` (scope).
- [ ] Diagramy zawierają canonical init header.
- [ ] Automatycznie wygenerowane diagramy mają idempotency marker.
- [ ] Frontmatter jest zgodny ze schematem: `docs/authoring/_instructions/diagram_system/frontmatter.schema.json`.
- [ ] Uruchomiono mermaid-lint z regułami z `.mermaid-lintrc` i naprawiono krytyczne błędy.
- [ ] Uruchomiono `python3 docs/scripts/diagram-tools/validate_diagram_links.py` i poprawiono/zgłoszono znalezione braki.
- [ ] Node-id zostały znormalizowane (dołącz mapę zmian, jeśli generator rolował je automatycznie).
- [ ] Wszystkie `click` mają dodatkowy fallback (lista "Powiązane dokumenty" pod diagramem).
- [ ] Krótki opis (1–2 zdania) jest dodany pod diagramem (accessibility).
- [ ] PR zawiera statystyki: liczba plików przejrzanych, naprawionych, wygenerowanych, brakujących plików oraz lista elementów wymagających ręcznej weryfikacji.
- [ ] Jeśli workflow walidacji jest proponowany — potwierdzono, że repo nie ma równoważnego workflow.

---

## 10. Najczęściej spotykane problemy i szybkie rozwiązania

- `click` powoduje brak renderu w mermaid-cli:
  - Usuń/zakomentuj `click`, pozostaw fallback markdown i opisz w PR gdzie oczekujesz klikalności w docsite (GitHub może obsługiwać `click`, mermaid-cli może nie).
- Duplikaty node-id z generatora:
  - Użyj `node_id_normalizer.py` lub upewnij się, że generator dopisuje unikalny prefiks (`doc_id_`).
- Frontmatter nie przechodzi walidacji:
  - Uruchom walidację frontmatter lokalnie i popraw `source_sha` / `last_sync_iso` formatu.

---

## 11. Dalsze uwagi
- Pliki narzędziowe znajdują się w repo pod prefiksem `docs/` (tzn. `docs/scripts/diagram-tools/...`). README/CI i generator powinny odnosić się do faktycznych ścieżek w repo — zwróć szczególną uwagę, gdy kopiujesz przykłady z zewnętrznych instrukcji.
- Jeżeli chcesz, by generator używał innej lokalizacji (np. `scripts/diagram-tools/` bez `docs/`), dostosuj ścieżki w generatorze lub przenieś pliki skryptów zgodnie z preferencją organizacyjną.

---

Powyższy README aktualizuje odwołania do narzędzi zgodnie z aktualnym układem plików w repo i zawiera praktyczne instrukcje uruchomienia oraz zaktualizowaną checklistę.
