# QA & Bench Suite (MASTER) - **OTClient Studio**

> Cel: kompletna, wykonywalna specyfikacja testow jakoLci i benchmarkow dla **Studio React/Electron** tworzacego skrypty **OTClient v8 + vBot**. Dokument opisuje: matryce testowa, wektory testow, E2E (Playwright), benchmarki (perf/mem), stabilnoLc/awarie, bezpieczeL"stwo, CI/CD, metryki oraz kryteria akceptacji. **Transfer 1:1** - gotowe do bezpoLredniej implementacji.

---
## 0) Zakres i zaL'oLLenia
- **Zakres QA:** parsery (Luaa'Lite/OTUI/OTML), lint (OTUI/Lua), generator szablonow, IDE providers (hover/completion/signature/symbols), integracja z OTClient (hota'reload + logi NDJSON), UI/UX, FS/konfiguracja, i18n/A11y, bezpieczeL"stwo, wydajnoLc i stabilnoLc.
- **Profil dziaL'ania:** offlinea'first, deterministyczne wyniki, brak uruchamiania Lua.
- **LarodL'a kontraktow:**
  - Schematy AST i JSON: *Parser & Schemas (MASTER)*.
  - Spec MASTER implementacji: *Specyfikacja implementacji (MASTER)*.
  - Lint: *OTUI Lint Rules (MASTER)*.
  - vBot: *vBot Playbook (MASTER)*.
  - IDE: *IDE Providers Spec (MASTER)*.

---
## 1) Matryca testowa (obszary A- kategorie)
| Obszar | Kategorie testow |
|---|---|
| **Parsery** | poprawnoLc AST vs schema, tolerance (ParseError), relacje (`dofile`, `g_ui.loadUI`), edgea'cases (komentarze/unicode) |
| **Lint** | wykrywalnoLc, autoa'fix, idempotencja, kolizje reguL', konfiguracja `otui-rules.json` |
| **Generator** | tworzenie moduL'ow/szablonow, integralnoLc LcieLLek, zgodnoLc z lintem/AST |
| **IDE Providers** | completion ranking, hover agregacja, signature mapping, symbols, definition/references (MVP+) |
| **Integracja OTClient** | hota'reload (skrot/flag), log NDJSON (format/rotacja), odpornoLc na brak katalogu |
| **Log Viewer** | tail duLLy/LLywy plik, filtry, eksport, stabilnoLc >1h |
| **FS/Config** | LcieLLki, atomowe zapisy, migracje configu, ignorowane foldery |
| **UI/UX** | nawigacja, edycja, quicka'fix, podglad diff, motywy, skroty |
| **i18n/A11y** | tL'umaczenia, `tr()` enforce, ARIA/kontrast |
| **BezpieczeL"stwo** | sandbox IPC, brak sieci, LcieLLki poza projektem, path traversal, wstrzykiwanie w log |
| **WydajnoLc** | skan 5k plikow (zimny/ciepL'y), lint throughput, provider latency, tail throughput |
| **StabilnoLc** | crash recovery, przerwane I/O, uszkodzony cache/config, dL'ugi czas dziaL'ania |

---
## 2) Konwencje nazw i identyfikatorow testow
- Prefixy **obszarowe**: `PAR-` (Parser), `LNT-` (Lint), `GEN-`, `IDE-`, `INT-` (Integracja), `LOG-`, `FS-`, `CFG-`, `UIX-`, `I18N-`, `A11Y-`, `SEC-`, `PERF-`, `RES-` (Resilience).
- Format ID: `XXX-###` (np. `PAR-011`).

---
## 3) Zasoby testowe (fixtures) - struktura
qa/
a"sa" fixtures/
a"'  a"sa" sample-project-small/
a"'  a"'  a"sa" modules/client/client.otmod
a"'  a"'  a"sa" modules/client/client.lua
a"'  a"'  a"sa" modules/client/ui/main.otui
a"'  a"'  a""a" images/button.png
a"'  a"sa" sample-project-large/         # generator wygeneruje 5k plikow
a"'  a"sa" otui/
a"'  a"'  a"sa" valid/
a"'  a"'  a""a" invalid/
a"'  a"sa" lua/
a"'  a"'  a"sa" valid/
a"'  a"'  a""a" invalid/
a"'  a""a" templates/
a"sa" expected/
a"'  a"sa" ast/
a"'  a"sa" lint/
a"'  a"sa" generator/
a"'  a""a" ide/
a""a" manifests/
   a"sa" tests.json        # definicje przypadkow
   a""a" perf.json         # scenariusze benchmarkow
```

---
## 4) Parsery - przypadki i kryteria
**PARa'001 (OTUI proste):** plik `main.otui` a' AST zgodny ze schema `otui-ast.schema.json`; kategorie `ida'BEHAVIOR`, `widtha'GEOMETRY`, `texta'STYLE`.
**PARa'002 (OTUI zagnieLLdLLenia):** wielopoziomowe `Decl` + dziedziczenie; brak cykli.
**PARa'003 (OTUI bL'edy):** niezamkniety blok a' `ParseError` z kodem `OTUI_001`, tolerant parsing zwraca reszte AST.
**PARa'010 (Lua funkcje/metody):** deklaracje `function M.a()` i `obj:method()` a' poprawne wezL'y `FunctionDecl` i `CallExpr.method`.
**PARa'011 (Lua relacje):** `dofile('x.lua')`, `require('y')` a' `relations.includes`.
**PARa'012 (Luaa'OTUI):** `g_ui.loadUI('ui/main.otui')` a' `relations.lua_to_otui`.
**PARa'020 (Docstrings):** `---@param / @return` a' `docstrings.json`.
**Kryteria:** walidacja JSON Schema (brak bL'edow), deterministyczne `loc`, brak crash.

---
## 5) Lint - przypadki i kryteria
**LNTa'001 (kolejnoLc pol):** wymuL `GEOMETRYa'STYLEa'BEHAVIOR`, autoa'fix generuje spojny diff, idempotentny (drugie uruchomienie: 0 zmian).
**LNTa'002 (`tr()`):** wrap staL'ych stringow w `text:`; ignoruj `id`.
**LNTa'003 (anchors/margins):** wykryj sprzecznoLci, brak autoa'fix (sugestie).
**LNTa'004 (assets):** brakujacy obraz/font/style - ERROR z propozycjami (fuzzy).
**LNTa'005 (duplikaty id):** wykryj powtorzenia.
**LNTa'010 (Lua locals):** ostrzeLL o globalach; autoa'fix `local` gdy bez kolizji.
**LNTa'011 (`unpack`):** zamieL" na `table.unpack`.
**Kryteria:** 100% wykrywalnoLci dla zestawu wzorcowego; brak falsea'positive dla plikow poprawnych.

---
## 6) Generator - przypadki i kryteria
**GENa'001 (moduL' default):** wygeneruj `.otmod` + `hello.lua` + `ui/hello.otui`; skaner wykrywa pliki; lint OK.
**GENa'002 (vBot macro):** wygeneruj plik `vb_auto_heal.lua`; zawiera guards + cooldown + log; przechodzi lint Luaa'lite.
**GENa'010 (konflikt LcieLLek):** proba nadpisania istniejacych plikow a' bL'ad z sugestia `--force` lub zmiany nazwy.
**Kryteria:** pliki powstaja atomowo (tempa'rename), zawartoLc zgodna z template, lint = 0 ERROR.

---
## 7) IDE Providers - przypadki i kryteria
**IDEa'COMPa'01 (Lua, API):** prefiks `g_res` + `.` a' `g_resources.readFile` (score aA 0.9).
**IDEa'COMPa'02 (OTUI, klucze):** w kontekLcie klucza lista atrybutow wg kategorii i typow.
**IDEa'COMPa'03 (style):** `style:` a' style z `assets-map.json.styles`.
**IDEa'HOVa'01:** hover na `g_modules.reloadModules` a' opis z `api.json`.
**IDEa'SIGa'01:** `g_resources.readFile(` a' `path: string` jako aktywny parametr.
**IDEa'SYMa'01:** symbole dokumentu (Lua/OTUI) - poprawne zakresy.
**Kryteria:** czasy odpowiedzi zgodne z budLLetem (10), deterministyczny ranking.

---
## 8) Integracja z OTClient - przypadki i kryteria
**INTa'001 (flaga reload):** utworz `modules/.dev/reload.flag` a' `reload requested/done` w NDJSON.
**INTa'002 (antya'drganie):** 3A- flaga < 800 ms a' 1 reload.
**INTa'003 (rotacja logu):** po przekroczeniu `maxLogBytes` plik nie roLnie, odcina peL'ne linie.
**INTa'010 (brak katalogu .dev):** moduL' loguje do konsoli; brak crash.
**Kryteria:** brak wyjatkow, log zgodny ze schematem `log-line.schema.json`.

---
## 9) Log Viewer - przypadki i kryteria
**LOGa'001:** tail LLywego pliku (1000 linii/min) bez utraty wpisow.
**LOGa'002:** filtry `level/tag/file:line` dziaL'aja i zwracaja podzbior deterministycznie.
**LOGa'003:** eksport do `.ndjson` i `.txt` - zawartoLc zgodna z filtrem.
**Kryteria:** stabilna praca > 1h, zuLLycie RAM < 200 MB.

---
## 10) Benchmarki (wydajnoLc) - budLLety i scenariusze
**BUDL>>ETY** (zgodne z MASTER):
- **Skan 5k plikow:** ciepL'y < **5 s**, zimny < **30 s**.
- **Lint pliku OTUI:** < **50 ms** (Lrednio, na warm cache).
- **Completion:** warm < **6 ms**, cold < **25 ms**.
- **Tail logu:** aA **1000 linii/min** bez backlogu; CPU < **15%** na 4C/8T.
- **RAM indeksu 5k:** < **500 MB**.

**Scenariusze benchmarkow:**
- **PERFa'SCANa'01:** sample-project-large (5k) - zimny start, pomiar czasu i RAM.
- **PERFa'SCANa'02:** powtorka (ciepL'y cache) - czas < 5 s.
- **PERFa'LINTa'01:** batch 100 plikow OTUI - czas caL'kowity < 2 s.
- **PERFa'COMPa'01:** 100 zapytaL" completion (warm) - P95 < 6 ms.
- **PERFa'LOGa'01:** tail logu 30 min - brak wzrostu RAM.

**Format wynikow (NDJSON):**
{"ts":"...","bench":"PERF-SCAN-01","metric":"timeMs","value":12345,"meta":{"files":5000}}
{"ts":"...","bench":"PERF-COMP-01","metric":"p95Ms","value":5.7}
```

---
## 11) StabilnoLc i odpornoLc (Resilience)
**RESa'001 (przerwane I/O):** zapis atomowy (tempa'rename); wymuL przerwanie a' brak korupcji pliku docelowego.
**RESa'002 (uszkodzony cache):** `.studio-cache/*` nieczytelne a' autoa'regeneracja bez crash.
**RESa'003 (uszkodzony config):** `.studio/config.json` - bL'ad schema a' komunikat i wczytanie domyLlnego.
**RESa'004 (duLLe pliki):** > 2 MB a' "biga'file mode" (ograniczone funkcje) bez crash.
**RESa'005 (dL'ugi runtime):** 8h dziaL'ania, brak wyciekow (> +10% RAM).

---
## 12) BezpieczeL"stwo
**SECa'001 (sandbox IPC):** tylko whitelista kanaL'ow; proby nieznanych kanaL'ow a' odrzucone + log.
**SECa'002 (path traversal):** wejLcia z `..` a' normalizacja i odrzucenie spoza `projectRoot`.
**SECa'003 (no network):** brak wychodzacych poL'aczeL"; monitoruj proby i loguj ostrzeLLenie.
**SECa'004 (log injection):** znaki sterujace w `msg` a' escapowane; NDJSON zawsze poprawny JSON.
**SECa'005 (arb. exec):** brak wykonywania Lua; walidacje w generatorze (bez eval).

---
## 13) E2E (Playwright) - scenariusze
**E2Ea'01 - Open a' Edit a' Lint a' Generate a' Reload a' Logs**
1. Uruchom Studio (Electron, headless jeLli moLLliwe).
2. WskaLL `sample-project-small`.
3. Otworz `ui/main.otui`; wstaw bL'ad kolejnoLci; sprawdLs diagnostyke.
4. Uruchom Quick Fix (OTUIa'001); potwierdLs diff; zapis.
5. Generator: "ModuL' default" a' utworz `modules/hello/*`.
6. Utworz `modules/.dev/reload.flag` a' potwierdLs wpisy w Log Viewer.
7. Filtruj log po `tag=reload`; eksport do `.ndjson`.
**Kryteria:** brak bL'edow; czasy krokow < 2 s kaLLdy.

**E2Ea'02 - IntelliSense flow**
1. Otworz `client.lua`; wpisz `g_res` + `.`.
2. SprawdLs, LLe lista zawiera `g_resources.readFile` z wysokim score.
3. Hover na `g_modules.reloadModules` a' opis.
4. Wpisz `g_resources.readFile(` a' signature `path: string`.
**Kryteria:** odpowiedzi < budLLetow, poprawna zawartoLc.

---
## 14) CI/CD - pipeline i artefakty
**Narzedzia:** pnpm/yarn, Vitest/Jest, Playwright, `electron-builder` (drya'run), validator JSON Schema.

**Skrypty:**
pnpm test:unit       # parsery, lint, generator, providers (mock IPC)
pnpm test:contract   # walidacja JSON vs schematy
pnpm test:e2e        # Playwright (Electron)
pnpm bench           # benchmarki (perf.json)
pnpm build:dry       # test buildow installerow bez publikacji
```

**Artefakty CI:**
- Raporty testow JUnit/HTML, logi NDJSON bench, zrzuty ekranow E2E, paczki `*.zip` z fixtures/expected.

**Progi jakoLci (fail the build):**
- Testy unit/contract/E2E - 100% zielone.
- Bench - LLadna metryka > budLLet (P95), w przeciwnym razie **UNSTABLE**; dwie kolejne iteracje **FAIL**.

---
## 15) Metryki i obserwowalnoLc QA
- **Metryki czasowe:** `timeMs`, `p50/p95/p99` dla providers/scan/lint.
- **Metryki pamieci:** `rssMB`, `heapMB` podczas skanu/longa'run.
- **JakoLc lintu:** wykrywalnoLc (%) i falsea'positive (%).
- **StabilnoLc:** liczba bL'edow parsera/IO na godzine.
- **Trendy:** porownania wzgledem poprzedniego builda (delta%).

**Format metryk (NDJSON):**
{"ts":"...","suite":"bench","case":"PERF-SCAN-01","metric":"timeMs","value":12345}
{"ts":"...","suite":"qa","case":"LNT-001","metric":"fixedIssues","value":7}
```

---
## 16) Manifest testow i benchmarkow
**tests.json (przykL'ad):**
{
  "$schemaVersion": 1,
  "tests": [
    {"id":"PAR-001","path":"qa/fixtures/otui/valid/main.otui","expect":"qa/expected/ast/main.json"},
    {"id":"LNT-001","path":"qa/fixtures/otui/invalid/order.otui","expect":"qa/expected/lint/order.fixed.otui"},
    {"id":"GEN-001","template":"module.default","target":"qa/tmp/out1"}
]
}
```

**perf.json (przykL'ad):**
{
  "$schemaVersion": 1,
  "benches": [
    {"id":"PERF-SCAN-01","project":"qa/fixtures/sample-project-large","metrics":["timeMs","rssMB"]},
    {"id":"PERF-COMP-01","queries":100,"metrics":["p95Ms"]}
]
}
```

---
## 17) Checklisty i DoD
- [ ] Zasoby testowe zbudowane (small/large, valid/invalid, expected/*).
- [ ] Unit/contract/IDE tests zielone na CI.
- [ ] E2E scenariusze wykonane (zrzuty ekranow zapisane).
- [ ] Bench w granicach budLLetow; brak regresji.
- [ ] Raporty i artefakty opublikowane; trendy zaktualizowane.

---
## 18) Noty koL"cowe
- Benchmarki uruchamiaj na stabilnym Lrodowisku (staL'y CPU/Gov, wyL'aczone inne obciaLLenia).
- Wszystkie schematy i kontrakty musza byc wersjonowane (`$schemaVersion`) i walidowane przed zapisami.
- Zmiany w budLLetach wydajnoLci wymagaja przegladu architektonicznego (ADR) i aktualizacji tego dokumentu.
