?# QA & Bench Suite (MASTER) - **OTClient Studio**

> Cel: kompletna, wykonywalna specyfikacja test�w jakosci i benchmark�w dla **Studio React/Electron** tworzacego skrypty **OTClient v8 + vBot**. Dokument opisuje: matryce testowa, wektory test�w, E2E (Playwright), benchmarki (perf/mem), stabilnosc/awarie, bezpieczenstwo, CI/CD, metryki oraz kryteria akceptacji. **Transfer 1:1** - gotowe do bezposredniej implementacji.

---
# # 0) Zakres i zalozenia
- **Zakres QA:** parsery (Lua-Lite/OTUI/OTML), lint (OTUI/Lua), generator szablon�w, IDE providers (hover/completion/signature/symbols), integracja z OTClient (hot-reload + logi NDJSON), UI/UX, FS/konfiguracja, i18n/A11y, bezpieczenstwo, wydajnosc i stabilnosc.
- **Profil dzialania:** offline-first, deterministyczne wyniki, brak uruchamiania Lua.
- **Zr�dla kontrakt�w:**
  - Schematy AST i JSON: *Parser & Schemas (MASTER)*.
  - Spec MASTER implementacji: *Specyfikacja implementacji (MASTER)*.
  - Lint: *OTUI Lint Rules (MASTER)*.
  - vBot: *vBot Playbook (MASTER)*.
  - IDE: *IDE Providers Spec (MASTER)*.

---
# # 1) Matryca testowa (obszary � kategorie)
| Obszar | Kategorie test�w |
|---|---|
| **Parsery** | poprawnosc AST vs schema, tolerance (ParseError), relacje (`dofile`, `g_ui.loadUI`), edge-cases (komentarze/unicode) |
| **Lint** | wykrywalnosc, auto-fix, idempotencja, kolizje regul, konfiguracja `otui-rules.json` |
| **Generator** | tworzenie modul�w/szablon�w, integralnosc sciezek, zgodnosc z lintem/AST |
| **IDE Providers** | completion ranking, hover agregacja, signature mapping, symbols, definition/references (MVP+) |
| **Integracja OTClient** | hot-reload (skr�t/flag), log NDJSON (format/rotacja), odpornosc na brak katalogu |
| **Log Viewer** | tail duzy/zywy plik, filtry, eksport, stabilnosc >1h |
| **FS/Config** | sciezki, atomowe zapisy, migracje configu, ignorowane foldery |
| **UI/UX** | nawigacja, edycja, quick-fix, podglad diff, motywy, skr�ty |
| **i18n/A11y** | tlumaczenia, `tr()` enforce, ARIA/kontrast |
| **Bezpieczenstwo** | sandbox IPC, brak sieci, sciezki poza projektem, path traversal, wstrzykiwanie w log |
| **Wydajnosc** | skan 5k plik�w (zimny/cieply), lint throughput, provider latency, tail throughput |
| **Stabilnosc** | crash recovery, przerwane I/O, uszkodzony cache/config, dlugi czas dzialania |

---
# # 2) Konwencje nazw i identyfikator�w test�w
- Prefixy **obszarowe**: `PAR-` (Parser), `LNT-` (Lint), `GEN-`, `IDE-`, `INT-` (Integracja), `LOG-`, `FS-`, `CFG-`, `UIX-`, `I18N-`, `A11Y-`, `SEC-`, `PERF-`, `RES-` (Resilience).
- Format ID: `XXX-###` (np. `PAR-011`).

---
# # 3) Zasoby testowe (fixtures) - struktura
```
qa/
?? fixtures/
?  ?? sample-project-small/
?  ?  ?? modules/client/client.otmod
?  ?  ?? modules/client/client.lua
?  ?  ?? modules/client/ui/main.otui
?  ?  ?? images/button.png
?  ?? sample-project-large/         # generator wygeneruje 5k plik�w
?  ?? otui/
?  ?  ?? valid/
?  ?  ?? invalid/
?  ?? lua/
?  ?  ?? valid/
?  ?  ?? invalid/
?  ?? templates/
?? expected/
?  ?? ast/
?  ?? lint/
?  ?? generator/
?  ?? ide/
?? manifests/
   ?? tests.json        # definicje przypadk�w
   ?? perf.json         # scenariusze benchmark�w
```

---
# # 4) Parsery - przypadki i kryteria
**PAR-001 (OTUI proste):** plik `main.otui` ? AST zgodny ze schema `otui-ast.schema.json`; kategorie `id?BEHAVIOR`, `width?GEOMETRY`, `text?STYLE`.
**PAR-002 (OTUI zagniezdzenia):** wielopoziomowe `Decl` + dziedziczenie; brak cykli.
**PAR-003 (OTUI bledy):** niezamkniety blok ? `ParseError` z kodem `OTUI_001`, tolerant parsing zwraca reszte AST.
**PAR-010 (Lua funkcje/metody):** deklaracje `function M.a()` i `obj:method()` ? poprawne wezly `FunctionDecl` i `CallExpr.method`.
**PAR-011 (Lua relacje):** `dofile('x.lua')`, `require('y')` ? `relations.includes`.
**PAR-012 (Lua?OTUI):** `g_ui.loadUI('ui/main.otui')` ? `relations.lua_to_otui`.
**PAR-020 (Docstrings):** `---@param / @return` ? `docstrings.json`.
**Kryteria:** walidacja JSON Schema (brak bled�w), deterministyczne `loc`, brak crash.

---
# # 5) Lint - przypadki i kryteria
**LNT-001 (kolejnosc p�l):** wymus `GEOMETRY?STYLE?BEHAVIOR`, auto-fix generuje sp�jny diff, idempotentny (drugie uruchomienie: 0 zmian).
**LNT-002 (`tr()`):** wrap stalych string�w w `text:`; ignoruj `id`.
**LNT-003 (anchors/margins):** wykryj sprzecznosci, brak auto-fix (sugestie).
**LNT-004 (assets):** brakujacy obraz/font/style - ERROR z propozycjami (fuzzy).
**LNT-005 (duplikaty id):** wykryj powt�rzenia.
**LNT-010 (Lua locals):** ostrzez o globalach; auto-fix `local` gdy bez kolizji.
**LNT-011 (`unpack`):** zamien na `table.unpack`.
**Kryteria:** 100% wykrywalnosci dla zestawu wzorcowego; brak false-positive dla plik�w poprawnych.

---
# # 6) Generator - przypadki i kryteria
**GEN-001 (modul default):** wygeneruj `.otmod` + `hello.lua` + `ui/hello.otui`; skaner wykrywa pliki; lint OK.
**GEN-002 (vBot macro):** wygeneruj plik `vb_auto_heal.lua`; zawiera guards + cooldown + log; przechodzi lint Lua-lite.
**GEN-010 (konflikt sciezek):** pr�ba nadpisania istniejacych plik�w ? blad z sugestia `--force` lub zmiany nazwy.
**Kryteria:** pliki powstaja atomowo (temp?rename), zawartosc zgodna z template, lint = 0 ERROR.

---
# # 7) IDE Providers - przypadki i kryteria
**IDE-COMP-01 (Lua, API):** prefiks `g_res` + `.` ? `g_resources.readFile` (score ? 0.9).
**IDE-COMP-02 (OTUI, klucze):** w kontekscie klucza lista atrybut�w wg kategorii i typ�w.
**IDE-COMP-03 (style):** `style:` ? style z `assets-map.json.styles`.
**IDE-HOV-01:** hover na `g_modules.reloadModules` ? opis z `api.json`.
**IDE-SIG-01:** `g_resources.readFile(` ? `path: string` jako aktywny parametr.
**IDE-SYM-01:** symbole dokumentu (Lua/OTUI) - poprawne zakresy.
**Kryteria:** czasy odpowiedzi zgodne z budzetem (�10), deterministyczny ranking.

---
# # 8) Integracja z OTClient - przypadki i kryteria
**INT-001 (flaga reload):** utw�rz `modules/.dev/reload.flag` ? `reload requested/done` w NDJSON.
**INT-002 (anty-drganie):** 3� flaga < 800 ms ? 1 reload.
**INT-003 (rotacja logu):** po przekroczeniu `maxLogBytes` plik nie rosnie, odcina pelne linie.
**INT-010 (brak katalogu .dev):** modul loguje do konsoli; brak crash.
**Kryteria:** brak wyjatk�w, log zgodny ze schematem `log-line.schema.json`.

---
# # 9) Log Viewer - przypadki i kryteria
**LOG-001:** tail zywego pliku (1000 linii/min) bez utraty wpis�w.
**LOG-002:** filtry `level/tag/file:line` dzialaja i zwracaja podzbi�r deterministycznie.
**LOG-003:** eksport do `.ndjson` i `.txt` - zawartosc zgodna z filtrem.
**Kryteria:** stabilna praca > 1h, zuzycie RAM < 200 MB.

---
# # 10) Benchmarki (wydajnosc) - budzety i scenariusze
**BUDZETY** (zgodne z MASTER):
- **Skan 5k plik�w:** cieply < **5 s**, zimny < **30 s**.
- **Lint pliku OTUI:** < **50 ms** (srednio, na warm cache).
- **Completion:** warm < **6 ms**, cold < **25 ms**.
- **Tail logu:** ? **1000 linii/min** bez backlogu; CPU < **15%** na 4C/8T.
- **RAM indeksu 5k:** < **500 MB**.

**Scenariusze benchmark�w:**
- **PERF-SCAN-01:** sample-project-large (5k) - zimny start, pomiar czasu i RAM.
- **PERF-SCAN-02:** powt�rka (cieply cache) - czas < 5 s.
- **PERF-LINT-01:** batch 100 plik�w OTUI - czas calkowity < 2 s.
- **PERF-COMP-01:** 100 zapytan completion (warm) - P95 < 6 ms.
- **PERF-LOG-01:** tail logu 30 min - brak wzrostu RAM.

**Format wynik�w (NDJSON):**
```json
{"ts":"...","bench":"PERF-SCAN-01","metric":"timeMs","value":12345,"meta":{"files":5000}}
{"ts":"...","bench":"PERF-COMP-01","metric":"p95Ms","value":5.7}
```

---
# # 11) Stabilnosc i odpornosc (Resilience)
**RES-001 (przerwane I/O):** zapis atomowy (temp?rename); wymus przerwanie ? brak korupcji pliku docelowego.
**RES-002 (uszkodzony cache):** `.studio-cache/*` nieczytelne ? auto-regeneracja bez crash.
**RES-003 (uszkodzony config):** `.studio/config.json` - blad schema ? komunikat i wczytanie domyslnego.
**RES-004 (duze pliki):** > 2 MB ? "big-file mode" (ograniczone funkcje) bez crash.
**RES-005 (dlugi runtime):** 8h dzialania, brak wyciek�w (> +10% RAM).

---
# # 12) Bezpieczenstwo
**SEC-001 (sandbox IPC):** tylko whitelista kanal�w; pr�by nieznanych kanal�w ? odrzucone + log.
**SEC-002 (path traversal):** wejscia z `..` ? normalizacja i odrzucenie spoza `projectRoot`.
**SEC-003 (no network):** brak wychodzacych polaczen; monitoruj pr�by i loguj ostrzezenie.
**SEC-004 (log injection):** znaki sterujace w `msg` ? escapowane; NDJSON zawsze poprawny JSON.
**SEC-005 (arb. exec):** brak wykonywania Lua; walidacje w generatorze (bez eval).

---
# # 13) E2E (Playwright) - scenariusze
**E2E-01 - Open ? Edit ? Lint ? Generate ? Reload ? Logs**
1. Uruchom Studio (Electron, headless jesli mozliwe).
2. Wskaz `sample-project-small`.
3. Otw�rz `ui/main.otui`; wstaw blad kolejnosci; sprawdz diagnostyke.
4. Uruchom Quick Fix (OTUI-001); potwierdz diff; zapis.
5. Generator: "Modul default" ? utw�rz `modules/hello/*`.
6. Utw�rz `modules/.dev/reload.flag` ? potwierdz wpisy w Log Viewer.
7. Filtruj log po `tag=reload`; eksport do `.ndjson`.
**Kryteria:** brak bled�w; czasy krok�w < 2 s kazdy.

**E2E-02 - IntelliSense flow**
1. Otw�rz `client.lua`; wpisz `g_res` + `.`.
2. Sprawdz, ze lista zawiera `g_resources.readFile` z wysokim score.
3. Hover na `g_modules.reloadModules` ? opis.
4. Wpisz `g_resources.readFile(` ? signature `path: string`.
**Kryteria:** odpowiedzi < budzet�w, poprawna zawartosc.

---
# # 14) CI/CD - pipeline i artefakty
**Narzedzia:** pnpm/yarn, Vitest/Jest, Playwright, `electron-builder` (dry-run), validator JSON Schema.

**Skrypty:**
```
pnpm test:unit       # parsery, lint, generator, providers (mock IPC)
pnpm test:contract   # walidacja JSON vs schematy
pnpm test:e2e        # Playwright (Electron)
pnpm bench           # benchmarki (perf.json)
pnpm build:dry       # test build�w installer�w bez publikacji
```

**Artefakty CI:**
- Raporty test�w JUnit/HTML, logi NDJSON bench, zrzuty ekran�w E2E, paczki `*.zip` z fixtures/expected.

**Progi jakosci (fail the build):**
- Testy unit/contract/E2E - 100% zielone.
- Bench - zadna metryka > budzet (P95), w przeciwnym razie **UNSTABLE**; dwie kolejne iteracje **FAIL**.

---
# # 15) Metryki i obserwowalnosc QA
- **Metryki czasowe:** `timeMs`, `p50/p95/p99` dla providers/scan/lint.
- **Metryki pamieci:** `rssMB`, `heapMB` podczas skanu/long-run.
- **Jakosc lintu:** wykrywalnosc (%) i false-positive (%).
- **Stabilnosc:** liczba bled�w parsera/IO na godzine.
- **Trendy:** por�wnania wzgledem poprzedniego builda (delta%).

**Format metryk (NDJSON):**
```json
{"ts":"...","suite":"bench","case":"PERF-SCAN-01","metric":"timeMs","value":12345}
{"ts":"...","suite":"qa","case":"LNT-001","metric":"fixedIssues","value":7}
```

---
# # 16) Manifest test�w i benchmark�w
**tests.json (przyklad):**
```json
{
  "$schemaVersion": 1,
  "tests": [
    {"id":"PAR-001","path":"qa/fixtures/otui/valid/main.otui","expect":"qa/expected/ast/main.json"},
    {"id":"LNT-001","path":"qa/fixtures/otui/invalid/order.otui","expect":"qa/expected/lint/order.fixed.otui"},
    {"id":"GEN-001","template":"module.default","target":"qa/tmp/out1"}
]
}
```

**perf.json (przyklad):**
```json
{
  "$schemaVersion": 1,
  "benches": [
    {"id":"PERF-SCAN-01","project":"qa/fixtures/sample-project-large","metrics":["timeMs","rssMB"]},
    {"id":"PERF-COMP-01","queries":100,"metrics":["p95Ms"]}
]
}
```

---
# # 17) Checklisty i DoD
- [ ] Zasoby testowe zbudowane (small/large, valid/invalid, expected/*).
- [ ] Unit/contract/IDE tests zielone na CI.
- [ ] E2E scenariusze wykonane (zrzuty ekran�w zapisane).
- [ ] Bench w granicach budzet�w; brak regresji.
- [ ] Raporty i artefakty opublikowane; trendy zaktualizowane.

---
# # 18) Noty koncowe
- Benchmarki uruchamiaj na stabilnym srodowisku (staly CPU/Gov, wylaczone inne obciazenia).
- Wszystkie schematy i kontrakty musza byc wersjonowane (`$schemaVersion`) i walidowane przed zapisami.
- Zmiany w budzetach wydajnosci wymagaja przegladu architektonicznego (ADR) i aktualizacji tego dokumentu.
