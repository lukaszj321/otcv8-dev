# Specyfikacja implementacji (MASTER v1.0): **Studio React/Electron** dla skryptĂłw **OTClient v8** + **modules/game_bot (vBot)**

> Dokument centralny â€“ peÄąâ€šna, profesjonalna specyfikacja do autonomicznej implementacji narzÄ™dzia. Zawiera architekturÄ™, modele danych, protokoÄąâ€šy, checklisty, reguÄąâ€šy jakoÄąâ€şci, plan wdroÄąÄ˝enia, testy, ryzyka i artefakty startowe. Wszystkie kroki sÄ… deterministyczne i moÄąÄ˝liwe do zautomatyzowania na podstawie danych zawartych w tym dokumencie.

---
## 0. Executive Summary
- **Cel:** zbudowaÄ‡ wieloplatformowe Studio (desktop **Electron** + **React/TypeScript**) do tworzenia, analizy i utrzymania skryptĂłw **Lua/OTUI/OTML** dla **OTClient v8** oraz **vBot**.
- **Core features:**
  1) Inteligentne **podpowiedzi API** (kuratorowany `api.json` + indeks ze skanu repo),
  2) **Lint/autoĂ˘â‚¬â€fix** dla **OTUI** i lekkie reguÄąâ€šy dla **Lua**,
  3) **Generator** moduÄąâ€šĂłw/szablonĂłw,
  4) Integracja z klientem: **hotĂ˘â‚¬â€reload** i **Log Viewer** (debug przez logi),
  5) Praca **offlineĂ˘â‚¬â€first**.
- **Ograniczenia:** brak oficjalnego stepĂ˘â‚¬â€debuggera Lua; debug realizowany przez logi oraz hotĂ˘â‚¬â€reload.

---
## 1. SÄąâ€šownik pojÄ™Ä‡
- **OTClient v8** â€“ klient gry (Lua/OTUI/OTML).
- **vBot** â€“ moduÄąâ€š `modules/game_bot` (makra/triggery).
- **HotĂ˘â‚¬â€reload** â€“ `g_modules.reloadModules()` (skrĂłt w kliencie lub moduÄąâ€š dev).
- **Flag file** â€“ plikĂ˘â‚¬â€flaga `modules/.dev/reload.flag` wyzwalajÄ…cy hotĂ˘â‚¬â€reload.
- **NDJSON** â€“ log *newlineĂ˘â‚¬â€delimited JSON* (kaÄąÄ˝da linia = obiekt JSON).

---
## 2. Zakres / Poza zakresem
**MVP w zakresie:** edycja Lua/OTUI/OTML, podpowiedzi API, lint/autoĂ˘â‚¬â€fix (OTUI + LuaĂ˘â‚¬â€lite), generator szablonĂłw, skan repo i indeks, Log Viewer, hotĂ˘â‚¬â€reload.

**Poza MVP:** stepĂ˘â‚¬â€debugger (breakpointy), zdalne eval Lua; profiling runtime; zÄąâ€šoÄąÄ˝one RPC do klienta (inne niÄąÄ˝ plik/log/skrĂłt).

---
## 3. Architektura systemu
**Wariant rekomendowany:** Desktop **Electron** (React/TS + Node/FS), integracja z OTClient przez system plikĂłw i skrĂłt hotĂ˘â‚¬â€reload.

`$fenceInfo
+--------------------+       IPC        +-------------------+
| React/TS Frontend  | <--------------> | Electron Main/Pre |
| (Vite + Monaco)    |                  |   + Node/FS       |
+--------------------+                  +-------------------+
          |   FS (read/write JSON, pliki projektu)             
v
+--------------------+         plik/flag/log         +----------------+
|  Projekt lokalny   | <----------------------------> |  OTClient v8  |
| (lua/otui/otmod/Ă˘â‚¬Â¦) |                               | (hotĂ˘â‚¬â€reload)  |
+--------------------+                                +----------------+
```

**Alternatywa web:** React + lokalny serwis Node (HTTP/WebSocket) + File System Access API (ograniczenia dostÄ™pu; rekomendowane tylko gdy Electron jest niewskazany).

---
## 4. Wymagania funkcjonalne (FR)
**FRĂ˘â‚¬â€01 â€“ Projekty:** wybĂłr katalogu, ostatnie projekty, walidacja (`modules/`, `.otmod`).
**FRĂ˘â‚¬â€02 â€“ Eksplorator:** drzewo `.lua/.otui/.otmod` + assets; CRUD na plikach; dragĂ˘â‚¬â€drop; operacje atomowe.
**FRĂ˘â‚¬â€03 â€“ Edytor:** Monaco (Lua/OTUI/OTML/JSON), goĂ˘â‚¬â€to symbol, minimapa, format, folding.
**FRĂ˘â‚¬â€04 â€“ IntelliSense:** hover, signature help, autocomplete z `api.json` + indeks projektu + docstrings.
**FRĂ˘â‚¬â€05 â€“ Lint OTUI:** kolejnoÄąâ€şÄ‡ pĂłl, `tr()` dla staÄąâ€šych, anchors/margins, istnienie zasobĂłw; autoĂ˘â‚¬â€fix dla kolejnoÄąâ€şci i `tr()`.
**FRĂ˘â‚¬â€06 â€“ Lint Lua (lite):** preferuj `local`, wykryj globalne; `table.unpack` vs `unpack`.
**FRĂ˘â‚¬â€07 â€“ Generator:** moduÄąâ€šy (`.otmod` + `main.lua` + `ui/*.otui`) + snippety vBot z checklistÄ….
**FRĂ˘â‚¬â€08 â€“ Skan/Indeks:** glob, parsery Lua/OTUI/OTML, relacje `dofile/require` i `g_ui.loadUI`; cache inkrementalny.
**FRĂ˘â‚¬â€09 â€“ Integracja z OTClient:** przycisk â€žPrzeÄąâ€šaduj w kliencieâ€ť (skrĂłt/flag file).
**FRĂ˘â‚¬â€10 â€“ Log Viewer:** tail NDJSON/tekst, filtry (level/tag/file:line), wyszukiwarka, eksport.
**FRĂ˘â‚¬â€11 â€“ Ustawienia:** Äąâ€şcieÄąÄ˝ki artefaktĂłw i logu, ignore patterns, motyw; import/eksport.
**FRĂ˘â‚¬â€12 â€“ Wbudowany help:** panel â€žAPI & HowĂ˘â‚¬â€toâ€ť, wyszukiwarka offline.

**Kryteria akceptacji (wybrane):** indeks 5k plikĂłw < 5 s z cache; brak crashy przy edycji plikĂłw 2 MB; >90% trafieÄąâ€ž podpowiedzi dla znanych symboli; autoĂ˘â‚¬â€fix deterministyczny.

---
## 5. Wymagania niefunkcjonalne (NFR)
- **Perf:** indeks < 5 s (cache), < 30 s zimny start; Monaco 60 FPS podczas pisania.
- **Security:** brak sieci (offlineĂ˘â‚¬â€first), sandbox Renderer, IPC whitelist, brak uruchamiania Lua.
- **Portability:** Windows/macOS/Linux; Web (opcjonalnie, ograniczenia FS API).
- **Reliability:** zapisy atomowe (tempĂ˘â€ â€™rename), odtwarzanie cache po awarii.

---
## 6. Kontrakty i modele danych (kanoniczne, wersjonowane)
> KaÄąÄ˝dy JSON zawiera `$schemaVersion` i jest walidowany testami kontraktowymi.
## 6.1. `resources/api.json` (kuratorowane, seed + ingest)
`$fenceInfo
{
  "$schemaVersion": 1,
  "generatedAt": "2025-10-02T00:00:00Z",
  "functions": [
    {"name": "g_modules.reloadModules", "module": "g_modules", "params": [], "returns": [], "description": "PrzeÄąâ€šadowuje moduÄąâ€šy i skrypty OTClient.", "since": "v8"},
    {"name": "g_resources.readFile", "module": "g_resources", "params": [{"name": "path", "type": "string"}], "returns": [{"type": "string"}], "description": "Czyta plik do stringa."},
    {"name": "g_resources.writeFile", "module": "g_resources", "params": [{"name": "path", "type": "string"}, {"name": "data", "type": "string"}], "returns": [{"type": "boolean"}], "description": "Zapisuje string do pliku."}
],
  "events": [
    {"name": "onGameStart", "target": "Game", "payload": [], "description": "WywoÄąâ€šywane przy starcie gry."}
],
  "objects": [
    {"name": "g_resources", "members": ["readFile", "writeFile"], "description": "MenedÄąÄ˝er zasobĂłw."}
]
}
```
> **Uwaga:** to seed. PeÄąâ€šny `api.json` powstaje wg Â§7 z lokalnych plikĂłw dokumentacji.
## 6.2. `project-index.json` (z automatycznego skanu)
`$fenceInfo
{
  "$schemaVersion": 1,
  "root": "/abs/path/to/project",
  "files": {"lua": ["modules/game_bot/bot.lua", "modules/client/client.lua"], "otui": ["modules/client/ui/main.otui"], "otmod": ["modules/client/client.otmod"]},
  "symbols": {"functions": {"reloadScripts": ["modules/client/client.lua:120"]}, "widgets": {"MainWindow": ["modules/client/ui/main.otui:5"]}},
  "relations": {"lua_to_otui": [{"lua": "modules/client/client.lua", "otui": "modules/client/ui/main.otui", "via": "g_ui.loadUI"}], "includes": [{"from": "modules/a/main.lua", "to": "modules/a/util.lua", "via": "dofile"}]}
}
```
## 6.3. `otui-rules.json` (lint/autoĂ˘â‚¬â€fix)
`$fenceInfo
{"$schemaVersion":1,"rules":[{"id":"OTUI-001","description":"KolejnoÄąâ€şÄ‡ pĂłl: GEOMETRIAĂ˘â€ â€™STYLĂ˘â€ â€™ZACHOWANIE.","fixable":true},{"id":"OTUI-002","description":"StaÄąâ€še stringi muszÄ… uÄąÄ˝ywaÄ‡ tr().","fixable":true},{"id":"OTUI-003","description":"Walidacja anchors/margins (brak sprzecznoÄąâ€şci).","fixable":false},{"id":"OTUI-004","description":"Weryfikacja istnienia zasobĂłw (obrazy, fonty, style).","fixable":false}]}
```
## 6.4. `templates.json` (generator)
`$fenceInfo
{"$schemaVersion":1,"module.default":{"title":"ModuÄąâ€š OTClient â€” szkielet","files":[{"path":"modules/hello/hello.otmod","contents":"name: hello\n"},{"path":"modules/hello/hello.lua","contents":"-- entry point\nlocal M = {}\nreturn M\n"},{"path":"modules/hello/ui/hello.otui","contents":"MainWindow < UIWidget { }\n"}],"checklist":["UmieÄąâ€şÄ‡ katalog w modules/","Uruchom klienta i przeÄąâ€šaduj moduÄąâ€šy","SprawdÄąĹź log po starcie moduÄąâ€šu"]}}
```
## 6.5. `docstrings.json`
`$fenceInfo
{"$schemaVersion":1,"entries":[{"file":"modules/x/main.lua","line":10,"symbol":"foo","params":[{"name":"a","type":"number"}],"returns":[{"type":"boolean"}],"comment":"---@param a number\n---@return boolean"}]}
```
## 6.6. `assets-map.json`
`$fenceInfo
{"$schemaVersion":1,"assets":{"images":["images/button.png"],"fonts":["fonts/verdana.otf"],"styles":["styles/dark.otui"]}}
```
## 6.7. `.studio/config.json`
`$fenceInfo
{"$schemaVersion":1,"projectRoot":"/abs/path/to/project","apiPath":"resources/api.json","otuiRulesPath":"resources/otui-rules.json","templatesPath":"resources/templates.json","logPath":"/abs/path/to/log.ndjson","ignore":["**/node_modules/**",".git/**"]}
```

---
## 7. Procedura ingest â€“ budowa `api.json`
**WejÄąâ€şcia:** lokalne pliki dokumentacji (`OTClient_data_documentation_FULL.md`, `luafunctionscpp.md`, `modules_Documentation.md`, `src framework.md`, `src client.md`).

**Kroki:**
1) Segmentacja MD (H1â€“H3) i klasyfikacja sekcji: API/Events/Hooks/Globals/Managers.
2) Ekstrakcja sygnatur: `name(params) -> returns`, opisĂłw, przykÄąâ€šadĂłw, statusu (`since/deprecated`).
3) Normalizacja nazewnictwa (`module`: `g_resources`, `g_modules`, itp.).
4) Walidacja: unikalne `name`, kompletne `params/returns`.
5) Scalanie z `docstrings.json` (uzupeÄąâ€šnienia typĂłw/przykÄąâ€šadĂłw).
6) Eksport `resources/api.json` (dodaj `generatedAt`, `$schemaVersion`).

**Wzorce (regex â€“ przykÄąâ€šadowe):**
- Funkcja: `^\s*([A-Za-z0-9_\.\:]+)\s*\(([^)]*)\)\s*(?:->\s*([^\n{]+))?`
- Param: `---@param\s+(\w+)\s+([\w<>\|]+)`
- Return: `---@return\s+([\w<>\|]+)`
- Event: `\bon[A-Z][A-Za-z0-9]+\b` (lub sekcje â€žEventsâ€ť).

**Polityka typĂłw:** `string|number|boolean|table|any|nil|function|userdata`; `optional` jeÄąâ€şli oznaczone `?` lub w kwadratowych nawiasach.

**Quality Gate:** 0 duplikatĂłw; Ă˘â€°Ä„95% pozycji z opisem i kompletnymi parametrami; walidacja JSON wg schematu.

---
## 8. Skaner i parsery â€“ specyfikacja
**FS skan:** glob `**/*.{lua,otui,otmod}`; wyklucz `.git/**`, `**/node_modules/**`, `**/.studio-cache/**`; hash (size+mtime) Ă˘â€ â€™ indeks inkrementalny.

**Parser Lua:**
- Tokenizacja: identyfikatory, stringi, komentarze (`--`, blokowe), sÄąâ€šowa kluczowe.
- Ekstrakcja: `function name(...)`, `obj:method(...)` (pozycja file:line).
- Docstrings: `---` + adnotacje `---@param`, `---@return` Ă˘â€ â€™ `docstrings.json`.
- Relacje: `dofile("path")`, `require("...")` Ă˘â€ â€™ `relations.includes`.
- Heurystyki vBot: wykrywanie `macro(`, `onTextMessage`, itp. Ă˘â€ â€™ tag `botSymbols`.

**Parser OTUI/OTML:**
- AST wg skrĂłconej EBNF:
`$fenceInfo
File := (Decl | Comment)*
Decl := Type ("<" Base ">")? "{" (KV | Decl)* "}"
KV   := Key ":" Value
Value:= String | Number | Bool | Ident | Array | Object
```
- Kategoryzacja atrybutĂłw: GEOMETRIA (`x`,`y`,`width`,`height`,`anchors`,`margin`), STYL (`font`,`color`,`image`,`style`), ZACHOWANIE (`draggable`,`onClick`,`id`).
- Relacje: `g_ui.loadUI("path")` Ă˘â€ â€™ `relations.lua_to_otui`.

**Parser `.otmod`:** klucz:wartoÄąâ€şÄ‡ (+ listy); wymagane `name`; waliduj znaki w `name`.

**Kody bÄąâ€šÄ™dĂłw parsera:** `P001` (Lua tokenizer), `P101` (OTUI niezamkniÄ™ty blok), `P201` (.otmod brak `name`).

---
## 9. Lint/AutoĂ˘â‚¬â€fix â€“ reguÄąâ€šy
- **OTUIĂ˘â‚¬â€001 (order):** sortuj atrybuty: GEOMETRIA Ă˘â€ â€™ STYL Ă˘â€ â€™ ZACHOWANIE (autoĂ˘â‚¬â€fix: przetasuj z zachowaniem komentarzy).
- **OTUIĂ˘â‚¬â€002 (tr):** staÄąâ€še literaÄąâ€šy string wrapuj `tr()` (autoĂ˘â‚¬â€fix; ignoruj `id`/nazwy klas).
- **OTUIĂ˘â‚¬â€003 (anchors):** wykryj sprzecznoÄąâ€şci anchors/margins (sugestie, bez autoĂ˘â‚¬â€fix).
- **OTUIĂ˘â‚¬â€004 (assets):** zgÄąâ€šoÄąâ€ş brakujÄ…ce zasoby (fuzzy podpowiedzi).
- **LUAĂ˘â‚¬â€001 (locals):** ostrzegaj globali; autoĂ˘â‚¬â€fix: `local` jeÄąâ€şli bez kolizji.
- **LUAĂ˘â‚¬â€002 (unpack):** zamieniaj `unpack` -> `table.unpack` (autoĂ˘â‚¬â€fix bezpieczny).

---
## 10. Integracja z OTClient (hotĂ˘â‚¬â€reload, logi)
**Tryb A (podstawowy):** zapis Ă˘â€ â€™ skrĂłt hotĂ˘â‚¬â€reload w kliencie (np. Ctrl+Shift+R).

**Tryb B (z moduÄąâ€šem dev):** Studio zapisuje `modules/.dev/reload.flag`; moduÄąâ€š dev w kliencie wykrywa i:
1) wywoÄąâ€šuje `g_modules.reloadModules()`,
2) usuwa/przepisuje plik flagi,
3) opcjonalnie loguje wynik (NDJSON) do `modules/.dev/log.jsonl`.

**Szkic moduÄąâ€šu dev (Lua):**
`$fenceInfo
local dev = {}
local flagPath = 'modules/.dev/reload.flag'

local function readFile(path)
  local ok, data = pcall(function() return g_resources.readFile(path) end)
  if not ok then return nil end
  return data
end

local function fileExists(path)
  local data = readFile(path)
  return data ~= nil and #data > 0
end

local function tryReload()
  if fileExists(flagPath) then
    print('[dev] reload flag detected')
    g_modules.reloadModules()
    g_resources.writeFile(flagPath, '')
  end
end

local function start()
  addEvent(function()
    tryReload()
    scheduleEvent(start, 500)
  end)
end

start()
return dev
```

**Logi (NDJSON):** pola: `ts` (ISO), `level` (INFO|WARN|ERROR), `tag`, `file`, `line`, `msg`, `meta`.

PrzykÄąâ€šad:
`$fenceInfo
{"ts":"2025-10-02T12:34:56.789Z","level":"INFO","tag":"dev","file":"modules/x/main.lua","line":42,"msg":"Hot reload done","meta":{"changed":3}}
```

---
## 11. UI/UX (ekrany i przepÄąâ€šywy)
- **Start:** wybĂłr/ostatnie projekty, skrĂłty do dokumentacji, â€žNowy moduÄąâ€šâ€ť.
- **Eksplorator:** drzewo plikĂłw, akcje kontekstowe, status operacji FS.
- **Edytor:** Monaco + panel boczny (API/Doc), statusbar (pozycja, problems, encoding).
- **Diagnostyka:** lista Issues (filtry), Quick Fix, przejÄąâ€şcia do linii.
- **API Browser:** lista obiektĂłw Ă˘â€ â€™ szczegĂłÄąâ€šy (opis, params, examples) Ă˘â€ â€™ â€žWstaw snippetâ€ť.
- **Log Viewer:** stream z filtrami (ERR/WARN/INFO), szukanie, pauza, eksport.
- **Ustawienia:** Äąâ€şcieÄąÄ˝ki zasobĂłw, logu, motyw, ignorowane foldery, mapowanie skrĂłtu.

---
## 12. IPC (Electron) â€“ kontrakty
- `studio:scan:start` â€“ req: `{root}` Ă˘â€ â€™ res: `project-index.json` | err: `{code,msg}`
- `studio:api:load` â€“ req: `{path}` Ă˘â€ â€™ res: `api.json`
- `studio:lint:run` â€“ req: `{files[]}` Ă˘â€ â€™ res: `{problems[]}`
- `studio:templates:generate` â€“ req: `{templateId, targetDir, vars}` Ă˘â€ â€™ res: `{createdFiles[]}`
- `studio:log:tail` â€“ req: `{path}` Ă˘â€ â€™ stream: `{line}` | `{eof}` | `{error}`

**BÄąâ€šÄ™dy:** `E_FS_001` (dostÄ™p FS), `E_PARSE_LUA`, `E_PARSE_OTUI`, `E_JSON_SCHEMA`.

---
## 13. Warstwa stanu FE
- **Zustand:** `projectStore`, `editorStore`, `diagnosticsStore`, `apiStore`, `logStore`.
- **Persist:** `.studio/config.json` przez backend FS.
- **Normalizacja:** mapy symboli `name -> {files[]}`.

---
## 14. BezpieczeÄąâ€žstwo i prywatnoÄąâ€şÄ‡
- Renderer sandbox, restrykcyjne IPC, brak sieci (domyÄąâ€şlnie), brak wykonywania Lua.
- Backup `.bak` przy autoĂ˘â‚¬â€fixach; zapisy atomowe.

---
## 15. WydajnoÄąâ€şÄ‡ i stabilnoÄąâ€şÄ‡
- Worker Threads dla parserĂłw; debounce 150 ms; cache w `.studio-cache/`.
- â€žBig file modeâ€ť w Monaco > 2 MB (ograniczenie czÄ™Äąâ€şci funkcji).

---
## 16. i18n, A11y, theming
- i18n: `en`/`pl`; wymuszaj `tr()` w OTUI poprzez lint.
- A11y: ARIA, focus outlines, kontrast WCAG AA.
- Tematy: Light/Dark/HighĂ˘â‚¬â€Contrast; zapis w config.

---
## 17. Testy i QA
- **Unit:** parsery (Lua/OTUI), lint rules, generator.
- **Contract:** walidacja JSON kontra schemat, IPC payloady/typy.
- **Integration:** skan 5k plikĂłw, pomiary czasu/RAM.
- **E2E (Playwright):** flow â€žOpen Ă˘â€ â€™ Edit Ă˘â€ â€™ Lint Ă˘â€ â€™ Generate Ă˘â€ â€™ Reload Ă˘â€ â€™ Logsâ€ť.
- **Regression:** snapshot AST/diagnostyki.

**DoD (final):** patrz Â§21 â€“ wszystkie punkty odhaczone.

---
## 18. Build/Release/Update
- `electron-builder` (Win NSIS, macOS dmg, Linux AppImage); podpisy binarek.
- AutoĂ˘â‚¬â€update (opcjonalny), domyÄąâ€şlnie wyÄąâ€šÄ…czony â€“ narzÄ™dzie offlineĂ˘â‚¬â€first.

---
## 19. Observability narzÄ™dzia
- Log aplikacji: `.studio/logs/app.ndjson`; poziomy: DEBUG/INFO/WARN/ERROR.
- Metryki: czas skanu, liczba plikĂłw, czas lintu, bÄąâ€šÄ™dy parserĂłw.

---
## 20. Migracje i zgodnoÄąâ€şÄ‡
- `$schemaVersion` w artefaktach; migracje `vN -> vN+1` dla config/cache.

---
## 21. Plan wdroÄąÄ˝enia i checklisty
**Etap 0 â€“ Inicjalizacja**
- [ ] Monorepo (pnpm), Vite+React+TS, Electron scaffold.
- [ ] Monaco, routing, layout.

**Etap 1 â€“ Kontrakty i zasoby**
- [ ] Interfejsy TS (ApiFunction/ApiEvent/ProjectIndex/OtuiRule/Template).
- [ ] DodaÄ‡ `resources/api.json` (seed), `otui-rules.json`, `templates.json`.

**Etap 2 â€“ Skaner/Parsery**
- [ ] Glob/FS, cache, incremental hashing.
- [ ] Parser Lua + docstrings + relacje.
- [ ] Parser OTUI/OTML + kategoryzacja atrybutĂłw.
- [ ] Parser `.otmod`.

**Etap 3 â€“ IDE/UX**
- [ ] Explorer, Edytor, API Browser.
- [ ] Diagnostyka + Quick Fix.

**Etap 4 â€“ Integracja z klientem**
- [ ] PrzeÄąâ€šaduj (skrĂłt/flag) + Log Viewer.

**Etap 5 â€“ Stabilizacja**
- [ ] Testy (unit/contract/integration/E2E), pakiety instalacyjne.

**Definition of Done (KoÄąâ€žcowe):**
- [ ] Aplikacja offline; projekty siÄ™ otwierajÄ…; indeks i symbole dziaÄąâ€šajÄ….
- [ ] `api.json` zasila podpowiedzi (hover/complete/signature help).
- [ ] Lint OTUI/Lua i autoĂ˘â‚¬â€fix (backup `.bak`).
- [ ] Integracja z OTClient: hotĂ˘â‚¬â€reload + logi stabilne.
- [ ] Pakiety Win/macOS/Linux; dokumentacja uÄąÄ˝ytkownika; sample project.

---
## 22. Ryzyka i mitigacje
- **Brak stepĂ˘â‚¬â€debuggera:** Log Viewer + snippety logujÄ…ce + mapowanie file:line.
- **RĂłÄąÄ˝nice wersji:** `since/deprecated` w `api.json`, profile klienta.
- **WydajnoÄąâ€şÄ‡:** indeks inkrementalny, workers, throttling.
- **Parsery:** testy kontraktowe + snapshoty, tolerant parsing.

---
## 23. Artefakty â€“ komplet MVP (gotowe w tym dokumencie)
- `resources/api.json` â€“ seed (6.1 + 24.A)
- `resources/otui-rules.json` â€“ (6.3 + 24.B)
- `resources/templates.json` â€“ (6.4 + 24.C)
- `docstrings.json` â€“ format (6.5)
- `assets-map.json` â€“ format (6.6)
- `.studio/config.json` â€“ format (6.7)

---
## 24. PrzykÄąâ€šadowe dane (seed do startu)
**A. `resources/api.json` (seed)** â€“ patrz Â§6.1 (peÄąâ€šny JSON wstawiony).

**B. `resources/otui-rules.json` (seed)** â€“ patrz Â§6.3 (peÄąâ€šny JSON wstawiony).

**C. `resources/templates.json` (seed)** â€“ patrz Â§6.4 (peÄąâ€šny JSON wstawiony).

---
## 25. Noty koÄąâ€žcowe
- Ten dokument jest **ÄąĹźrĂłdÄąâ€šem prawdy (SoT)**. Dodatkowe canvasy muszÄ… odwoÄąâ€šywaÄ‡ siÄ™ do sekcji (Â§) i kontraktĂłw tutaj zdefiniowanych.
- Zmiany wymagajÄ… podniesienia `$schemaVersion` i przejÄąâ€şcia testĂłw kontraktowych.
- Wszelkie dane sÄ… przygotowane z myÄąâ€şlÄ… o pracy **offline** w oparciu o lokalne pliki dokumentacji i kodu.


