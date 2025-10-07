# QA & Bench Suite (MASTER) â€“ **OTClient Studio**

> Cel: kompletna, wykonywalna specyfikacja testĂłw jakoÄąâ€şci i benchmarkĂłw dla **Studio React/Electron** tworzÄ…cego skrypty **OTClient v8 + vBot**. Dokument opisuje: matrycÄ™ testowÄ…, wektory testĂłw, E2E (Playwright), benchmarki (perf/mem), stabilnoÄąâ€şÄ‡/awarie, bezpieczeÄąâ€žstwo, CI/CD, metryki oraz kryteria akceptacji. **Transfer 1:1** â€“ gotowe do bezpoÄąâ€şredniej implementacji.

---
## 0) Zakres i zaÄąâ€šoÄąÄ˝enia
- **Zakres QA:** parsery (LuaĂ˘â‚¬â€Lite/OTUI/OTML), lint (OTUI/Lua), generator szablonĂłw, IDE providers (hover/completion/signature/symbols), integracja z OTClient (hotĂ˘â‚¬â€reload + logi NDJSON), UI/UX, FS/konfiguracja, i18n/A11y, bezpieczeÄąâ€žstwo, wydajnoÄąâ€şÄ‡ i stabilnoÄąâ€şÄ‡.
- **Profil dziaÄąâ€šania:** offlineĂ˘â‚¬â€first, deterministyczne wyniki, brak uruchamiania Lua.
- **ÄąÄ…rĂłdÄąâ€ša kontraktĂłw:**
  - Schematy AST i JSON: *Parser & Schemas (MASTER)*.
  - Spec MASTER implementacji: *Specyfikacja implementacji (MASTER)*.
  - Lint: *OTUI Lint Rules (MASTER)*.
  - vBot: *vBot Playbook (MASTER)*.
  - IDE: *IDE Providers Spec (MASTER)*.

---
## 1) Matryca testowa (obszary Ä‚â€” kategorie)
| Obszar | Kategorie testĂłw |
|---|---|
| **Parsery** | poprawnoÄąâ€şÄ‡ AST vs schema, tolerance (ParseError), relacje (`dofile`, `g_ui.loadUI`), edgeĂ˘â‚¬â€cases (komentarze/unicode) |
| **Lint** | wykrywalnoÄąâ€şÄ‡, autoĂ˘â‚¬â€fix, idempotencja, kolizje reguÄąâ€š, konfiguracja `otui-rules.json` |
| **Generator** | tworzenie moduÄąâ€šĂłw/szablonĂłw, integralnoÄąâ€şÄ‡ Äąâ€şcieÄąÄ˝ek, zgodnoÄąâ€şÄ‡ z lintem/AST |
| **IDE Providers** | completion ranking, hover agregacja, signature mapping, symbols, definition/references (MVP+) |
| **Integracja OTClient** | hotĂ˘â‚¬â€reload (skrĂłt/flag), log NDJSON (format/rotacja), odpornoÄąâ€şÄ‡ na brak katalogu |
| **Log Viewer** | tail duÄąÄ˝y/ÄąÄ˝ywy plik, filtry, eksport, stabilnoÄąâ€şÄ‡ >1h |
| **FS/Config** | Äąâ€şcieÄąÄ˝ki, atomowe zapisy, migracje configu, ignorowane foldery |
| **UI/UX** | nawigacja, edycja, quickĂ˘â‚¬â€fix, podglÄ…d diff, motywy, skrĂłty |
| **i18n/A11y** | tÄąâ€šumaczenia, `tr()` enforce, ARIA/kontrast |
| **BezpieczeÄąâ€žstwo** | sandbox IPC, brak sieci, Äąâ€şcieÄąÄ˝ki poza projektem, path traversal, wstrzykiwanie w log |
| **WydajnoÄąâ€şÄ‡** | skan 5k plikĂłw (zimny/ciepÄąâ€šy), lint throughput, provider latency, tail throughput |
| **StabilnoÄąâ€şÄ‡** | crash recovery, przerwane I/O, uszkodzony cache/config, dÄąâ€šugi czas dziaÄąâ€šania |

---
## 2) Konwencje nazw i identyfikatorĂłw testĂłw
- Prefixy **obszarowe**: `PAR-` (Parser), `LNT-` (Lint), `GEN-`, `IDE-`, `INT-` (Integracja), `LOG-`, `FS-`, `CFG-`, `UIX-`, `I18N-`, `A11Y-`, `SEC-`, `PERF-`, `RES-` (Resilience).
- Format ID: `XXX-###` (np. `PAR-011`).

---
## 3) Zasoby testowe (fixtures) â€“ struktura
`$fenceInfo
qa/
Ă˘â€ťĹ›Ă˘â€ťâ‚¬ fixtures/
Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ sample-project-small/
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ modules/client/client.otmod
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ modules/client/client.lua
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ modules/client/ui/main.otui
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ images/button.png
Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ sample-project-large/         # generator wygeneruje 5k plikĂłw
Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ otui/
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ valid/
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ invalid/
Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ lua/
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ valid/
Ă˘â€ťâ€š  Ă˘â€ťâ€š  Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ invalid/
Ă˘â€ťâ€š  Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ templates/
Ă˘â€ťĹ›Ă˘â€ťâ‚¬ expected/
Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ ast/
Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ lint/
Ă˘â€ťâ€š  Ă˘â€ťĹ›Ă˘â€ťâ‚¬ generator/
Ă˘â€ťâ€š  Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ ide/
Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ manifests/
   Ă˘â€ťĹ›Ă˘â€ťâ‚¬ tests.json        # definicje przypadkĂłw
   Ă˘â€ťâ€ťĂ˘â€ťâ‚¬ perf.json         # scenariusze benchmarkĂłw
```

---
## 4) Parsery â€“ przypadki i kryteria
**PARĂ˘â‚¬â€001 (OTUI proste):** plik `main.otui` Ă˘â€ â€™ AST zgodny ze schema `otui-ast.schema.json`; kategorie `idĂ˘â€ â€™BEHAVIOR`, `widthĂ˘â€ â€™GEOMETRY`, `textĂ˘â€ â€™STYLE`.
**PARĂ˘â‚¬â€002 (OTUI zagnieÄąÄ˝dÄąÄ˝enia):** wielopoziomowe `Decl` + dziedziczenie; brak cykli.
**PARĂ˘â‚¬â€003 (OTUI bÄąâ€šÄ™dy):** niezamkniÄ™ty blok Ă˘â€ â€™ `ParseError` z kodem `OTUI_001`, tolerant parsing zwraca resztÄ™ AST.
**PARĂ˘â‚¬â€010 (Lua funkcje/metody):** deklaracje `function M.a()` i `obj:method()` Ă˘â€ â€™ poprawne wÄ™zÄąâ€šy `FunctionDecl` i `CallExpr.method`.
**PARĂ˘â‚¬â€011 (Lua relacje):** `dofile('x.lua')`, `require('y')` Ă˘â€ â€™ `relations.includes`.
**PARĂ˘â‚¬â€012 (LuaĂ˘â€ â€™OTUI):** `g_ui.loadUI('ui/main.otui')` Ă˘â€ â€™ `relations.lua_to_otui`.
**PARĂ˘â‚¬â€020 (Docstrings):** `---@param / @return` Ă˘â€ â€™ `docstrings.json`.
**Kryteria:** walidacja JSON Schema (brak bÄąâ€šÄ™dĂłw), deterministyczne `loc`, brak crash.

---
## 5) Lint â€“ przypadki i kryteria
**LNTĂ˘â‚¬â€001 (kolejnoÄąâ€şÄ‡ pĂłl):** wymuÄąâ€ş `GEOMETRYĂ˘â€ â€™STYLEĂ˘â€ â€™BEHAVIOR`, autoĂ˘â‚¬â€fix generuje spĂłjny diff, idempotentny (drugie uruchomienie: 0 zmian).
**LNTĂ˘â‚¬â€002 (`tr()`):** wrap staÄąâ€šych stringĂłw w `text:`; ignoruj `id`.
**LNTĂ˘â‚¬â€003 (anchors/margins):** wykryj sprzecznoÄąâ€şci, brak autoĂ˘â‚¬â€fix (sugestie).
**LNTĂ˘â‚¬â€004 (assets):** brakujÄ…cy obraz/font/style â€“ ERROR z propozycjami (fuzzy).
**LNTĂ˘â‚¬â€005 (duplikaty id):** wykryj powtĂłrzenia.
**LNTĂ˘â‚¬â€010 (Lua locals):** ostrzeÄąÄ˝ o globalach; autoĂ˘â‚¬â€fix `local` gdy bez kolizji.
**LNTĂ˘â‚¬â€011 (`unpack`):** zamieÄąâ€ž na `table.unpack`.
**Kryteria:** 100% wykrywalnoÄąâ€şci dla zestawu wzorcowego; brak falseĂ˘â‚¬â€positive dla plikĂłw poprawnych.

---
## 6) Generator â€“ przypadki i kryteria
**GENĂ˘â‚¬â€001 (moduÄąâ€š default):** wygeneruj `.otmod` + `hello.lua` + `ui/hello.otui`; skaner wykrywa pliki; lint OK.
**GENĂ˘â‚¬â€002 (vBot macro):** wygeneruj plik `vb_auto_heal.lua`; zawiera guards + cooldown + log; przechodzi lint LuaĂ˘â‚¬â€lite.
**GENĂ˘â‚¬â€010 (konflikt Äąâ€şcieÄąÄ˝ek):** prĂłba nadpisania istniejÄ…cych plikĂłw Ă˘â€ â€™ bÄąâ€šÄ…d z sugestiÄ… `--force` lub zmiany nazwy.
**Kryteria:** pliki powstajÄ… atomowo (tempĂ˘â€ â€™rename), zawartoÄąâ€şÄ‡ zgodna z template, lint = 0 ERROR.

---
## 7) IDE Providers â€“ przypadki i kryteria
**IDEĂ˘â‚¬â€COMPĂ˘â‚¬â€01 (Lua, API):** prefiks `g_res` + `.` Ă˘â€ â€™ `g_resources.readFile` (score Ă˘â€°Ä„ 0.9).
**IDEĂ˘â‚¬â€COMPĂ˘â‚¬â€02 (OTUI, klucze):** w kontekÄąâ€şcie klucza lista atrybutĂłw wg kategorii i typĂłw.
**IDEĂ˘â‚¬â€COMPĂ˘â‚¬â€03 (style):** `style:` Ă˘â€ â€™ style z `assets-map.json.styles`.
**IDEĂ˘â‚¬â€HOVĂ˘â‚¬â€01:** hover na `g_modules.reloadModules` Ă˘â€ â€™ opis z `api.json`.
**IDEĂ˘â‚¬â€SIGĂ˘â‚¬â€01:** `g_resources.readFile(` Ă˘â€ â€™ `path: string` jako aktywny parametr.
**IDEĂ˘â‚¬â€SYMĂ˘â‚¬â€01:** symbole dokumentu (Lua/OTUI) â€“ poprawne zakresy.
**Kryteria:** czasy odpowiedzi zgodne z budÄąÄ˝etem (Â§10), deterministyczny ranking.

---
## 8) Integracja z OTClient â€“ przypadki i kryteria
**INTĂ˘â‚¬â€001 (flaga reload):** utwĂłrz `modules/.dev/reload.flag` Ă˘â€ â€™ `reload requested/done` w NDJSON.
**INTĂ˘â‚¬â€002 (antyĂ˘â‚¬â€drganie):** 3Ä‚â€” flaga < 800 ms Ă˘â€ â€™ 1 reload.
**INTĂ˘â‚¬â€003 (rotacja logu):** po przekroczeniu `maxLogBytes` plik nie roÄąâ€şnie, odcina peÄąâ€šne linie.
**INTĂ˘â‚¬â€010 (brak katalogu .dev):** moduÄąâ€š loguje do konsoli; brak crash.
**Kryteria:** brak wyjÄ…tkĂłw, log zgodny ze schematem `log-line.schema.json`.

---
## 9) Log Viewer â€“ przypadki i kryteria
**LOGĂ˘â‚¬â€001:** tail ÄąÄ˝ywego pliku (1000 linii/min) bez utraty wpisĂłw.
**LOGĂ˘â‚¬â€002:** filtry `level/tag/file:line` dziaÄąâ€šajÄ… i zwracajÄ… podzbiĂłr deterministycznie.
**LOGĂ˘â‚¬â€003:** eksport do `.ndjson` i `.txt` â€“ zawartoÄąâ€şÄ‡ zgodna z filtrem.
**Kryteria:** stabilna praca > 1h, zuÄąÄ˝ycie RAM < 200 MB.

---
## 10) Benchmarki (wydajnoÄąâ€şÄ‡) â€“ budÄąÄ˝ety i scenariusze
**BUDÄąÂ»ETY** (zgodne z MASTER):
- **Skan 5k plikĂłw:** ciepÄąâ€šy < **5 s**, zimny < **30 s**.
- **Lint pliku OTUI:** < **50 ms** (Äąâ€şrednio, na warm cache).
- **Completion:** warm < **6 ms**, cold < **25 ms**.
- **Tail logu:** Ă˘â€°Ä„ **1000 linii/min** bez backlogu; CPU < **15%** na 4C/8T.
- **RAM indeksu 5k:** < **500 MB**.

**Scenariusze benchmarkĂłw:**
- **PERFĂ˘â‚¬â€SCANĂ˘â‚¬â€01:** sample-project-large (5k) â€“ zimny start, pomiar czasu i RAM.
- **PERFĂ˘â‚¬â€SCANĂ˘â‚¬â€02:** powtĂłrka (ciepÄąâ€šy cache) â€“ czas < 5 s.
- **PERFĂ˘â‚¬â€LINTĂ˘â‚¬â€01:** batch 100 plikĂłw OTUI â€“ czas caÄąâ€škowity < 2 s.
- **PERFĂ˘â‚¬â€COMPĂ˘â‚¬â€01:** 100 zapytaÄąâ€ž completion (warm) â€“ P95 < 6 ms.
- **PERFĂ˘â‚¬â€LOGĂ˘â‚¬â€01:** tail logu 30 min â€“ brak wzrostu RAM.

**Format wynikĂłw (NDJSON):**
`$fenceInfo
{"ts":"...","bench":"PERF-SCAN-01","metric":"timeMs","value":12345,"meta":{"files":5000}}
{"ts":"...","bench":"PERF-COMP-01","metric":"p95Ms","value":5.7}
```

---
## 11) StabilnoÄąâ€şÄ‡ i odpornoÄąâ€şÄ‡ (Resilience)
**RESĂ˘â‚¬â€001 (przerwane I/O):** zapis atomowy (tempĂ˘â€ â€™rename); wymuÄąâ€ş przerwanie Ă˘â€ â€™ brak korupcji pliku docelowego.
**RESĂ˘â‚¬â€002 (uszkodzony cache):** `.studio-cache/*` nieczytelne Ă˘â€ â€™ autoĂ˘â‚¬â€regeneracja bez crash.
**RESĂ˘â‚¬â€003 (uszkodzony config):** `.studio/config.json` â€“ bÄąâ€šÄ…d schema Ă˘â€ â€™ komunikat i wczytanie domyÄąâ€şlnego.
**RESĂ˘â‚¬â€004 (duÄąÄ˝e pliki):** > 2 MB Ă˘â€ â€™ â€žbigĂ˘â‚¬â€file modeâ€ť (ograniczone funkcje) bez crash.
**RESĂ˘â‚¬â€005 (dÄąâ€šugi runtime):** 8h dziaÄąâ€šania, brak wyciekĂłw (> +10% RAM).

---
## 12) BezpieczeÄąâ€žstwo
**SECĂ˘â‚¬â€001 (sandbox IPC):** tylko whitelista kanaÄąâ€šĂłw; prĂłby nieznanych kanaÄąâ€šĂłw Ă˘â€ â€™ odrzucone + log.
**SECĂ˘â‚¬â€002 (path traversal):** wejÄąâ€şcia z `..` Ă˘â€ â€™ normalizacja i odrzucenie spoza `projectRoot`.
**SECĂ˘â‚¬â€003 (no network):** brak wychodzÄ…cych poÄąâ€šÄ…czeÄąâ€ž; monitoruj prĂłby i loguj ostrzeÄąÄ˝enie.
**SECĂ˘â‚¬â€004 (log injection):** znaki sterujÄ…ce w `msg` Ă˘â€ â€™ escapowane; NDJSON zawsze poprawny JSON.
**SECĂ˘â‚¬â€005 (arb. exec):** brak wykonywania Lua; walidacje w generatorze (bez eval).

---
## 13) E2E (Playwright) â€“ scenariusze
**E2EĂ˘â‚¬â€01 â€“ Open Ă˘â€ â€™ Edit Ă˘â€ â€™ Lint Ă˘â€ â€™ Generate Ă˘â€ â€™ Reload Ă˘â€ â€™ Logs**
1. Uruchom Studio (Electron, headless jeÄąâ€şli moÄąÄ˝liwe).
2. WskaÄąÄ˝ `sample-project-small`.
3. OtwĂłrz `ui/main.otui`; wstaw bÄąâ€šÄ…d kolejnoÄąâ€şci; sprawdÄąĹź diagnostykÄ™.
4. Uruchom Quick Fix (OTUIĂ˘â‚¬â€001); potwierdÄąĹź diff; zapis.
5. Generator: â€žModuÄąâ€š defaultâ€ť Ă˘â€ â€™ utwĂłrz `modules/hello/*`.
6. UtwĂłrz `modules/.dev/reload.flag` Ă˘â€ â€™ potwierdÄąĹź wpisy w Log Viewer.
7. Filtruj log po `tag=reload`; eksport do `.ndjson`.
**Kryteria:** brak bÄąâ€šÄ™dĂłw; czasy krokĂłw < 2 s kaÄąÄ˝dy.

**E2EĂ˘â‚¬â€02 â€“ IntelliSense flow**
1. OtwĂłrz `client.lua`; wpisz `g_res` + `.`.
2. SprawdÄąĹź, ÄąÄ˝e lista zawiera `g_resources.readFile` z wysokim score.
3. Hover na `g_modules.reloadModules` Ă˘â€ â€™ opis.
4. Wpisz `g_resources.readFile(` Ă˘â€ â€™ signature `path: string`.
**Kryteria:** odpowiedzi < budÄąÄ˝etĂłw, poprawna zawartoÄąâ€şÄ‡.

---
## 14) CI/CD â€“ pipeline i artefakty
**NarzÄ™dzia:** pnpm/yarn, Vitest/Jest, Playwright, `electron-builder` (dryĂ˘â‚¬â€run), validator JSON Schema.

**Skrypty:**
`$fenceInfo
pnpm test:unit       # parsery, lint, generator, providers (mock IPC)
pnpm test:contract   # walidacja JSON vs schematy
pnpm test:e2e        # Playwright (Electron)
pnpm bench           # benchmarki (perf.json)
pnpm build:dry       # test buildĂłw installerĂłw bez publikacji
```

**Artefakty CI:**
- Raporty testĂłw JUnit/HTML, logi NDJSON bench, zrzuty ekranĂłw E2E, paczki `*.zip` z fixtures/expected.

**Progi jakoÄąâ€şci (fail the build):**
- Testy unit/contract/E2E â€“ 100% zielone.
- Bench â€“ ÄąÄ˝adna metryka > budÄąÄ˝et (P95), w przeciwnym razie **UNSTABLE**; dwie kolejne iteracje **FAIL**.

---
## 15) Metryki i obserwowalnoÄąâ€şÄ‡ QA
- **Metryki czasowe:** `timeMs`, `p50/p95/p99` dla providers/scan/lint.
- **Metryki pamiÄ™ci:** `rssMB`, `heapMB` podczas skanu/longĂ˘â‚¬â€run.
- **JakoÄąâ€şÄ‡ lintu:** wykrywalnoÄąâ€şÄ‡ (%) i falseĂ˘â‚¬â€positive (%).
- **StabilnoÄąâ€şÄ‡:** liczba bÄąâ€šÄ™dĂłw parsera/IO na godzinÄ™.
- **Trendy:** porĂłwnania wzglÄ™dem poprzedniego builda (delta%).

**Format metryk (NDJSON):**
`$fenceInfo
{"ts":"...","suite":"bench","case":"PERF-SCAN-01","metric":"timeMs","value":12345}
{"ts":"...","suite":"qa","case":"LNT-001","metric":"fixedIssues","value":7}
```

---
## 16) Manifest testĂłw i benchmarkĂłw
**tests.json (przykÄąâ€šad):**
`$fenceInfo
{
  "$schemaVersion": 1,
  "tests": [
    {"id":"PAR-001","path":"qa/fixtures/otui/valid/main.otui","expect":"qa/expected/ast/main.json"},
    {"id":"LNT-001","path":"qa/fixtures/otui/invalid/order.otui","expect":"qa/expected/lint/order.fixed.otui"},
    {"id":"GEN-001","template":"module.default","target":"qa/tmp/out1"}
]
}
```

**perf.json (przykÄąâ€šad):**
`$fenceInfo
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
- [ ] E2E scenariusze wykonane (zrzuty ekranĂłw zapisane).
- [ ] Bench w granicach budÄąÄ˝etĂłw; brak regresji.
- [ ] Raporty i artefakty opublikowane; trendy zaktualizowane.

---
## 18) Noty koÄąâ€žcowe
- Benchmarki uruchamiaj na stabilnym Äąâ€şrodowisku (staÄąâ€šy CPU/Gov, wyÄąâ€šÄ…czone inne obciÄ…ÄąÄ˝enia).
- Wszystkie schematy i kontrakty muszÄ… byÄ‡ wersjonowane (`$schemaVersion`) i walidowane przed zapisami.
- Zmiany w budÄąÄ˝etach wydajnoÄąâ€şci wymagajÄ… przeglÄ…du architektonicznego (ADR) i aktualizacji tego dokumentu.

