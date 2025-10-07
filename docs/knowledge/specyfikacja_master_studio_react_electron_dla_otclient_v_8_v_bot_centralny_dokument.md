# Specyfikacja implementacji (MASTER v1.0): **Studio React/Electron** dla skryptow **OTClient v8** + **modules/game_bot (vBot)**

> Dokument centralny - peL'na, profesjonalna specyfikacja do autonomicznej implementacji narzedzia. Zawiera architekture, modele danych, protokoL'y, checklisty, reguL'y jakoLci, plan wdroLLenia, testy, ryzyka i artefakty startowe. Wszystkie kroki sa deterministyczne i moLLliwe do zautomatyzowania na podstawie danych zawartych w tym dokumencie.

---
## 0. Executive Summary
- **Cel:** zbudowac wieloplatformowe Studio (desktop **Electron** + **React/TypeScript**) do tworzenia, analizy i utrzymania skryptow **Lua/OTUI/OTML** dla **OTClient v8** oraz **vBot**.
- **Core features:**
  1) Inteligentne **podpowiedzi API** (kuratorowany `api.json` + indeks ze skanu repo),
  2) **Lint/autoa'fix** dla **OTUI** i lekkie reguL'y dla **Lua**,
  3) **Generator** moduL'ow/szablonow,
  4) Integracja z klientem: **hota'reload** i **Log Viewer** (debug przez logi),
  5) Praca **offlinea'first**.
- **Ograniczenia:** brak oficjalnego stepa'debuggera Lua; debug realizowany przez logi oraz hota'reload.

---
## 1. SL'ownik pojec
- **OTClient v8** - klient gry (Lua/OTUI/OTML).
- **vBot** - moduL' `modules/game_bot` (makra/triggery).
- **Hota'reload** - `g_modules.reloadModules()` (skrot w kliencie lub moduL' dev).
- **Flag file** - plika'flaga `modules/.dev/reload.flag` wyzwalajacy hota'reload.
- **NDJSON** - log *newlinea'delimited JSON* (kaLLda linia = obiekt JSON).

---
## 2. Zakres / Poza zakresem
**MVP w zakresie:** edycja Lua/OTUI/OTML, podpowiedzi API, lint/autoa'fix (OTUI + Luaa'lite), generator szablonow, skan repo i indeks, Log Viewer, hota'reload.

**Poza MVP:** stepa'debugger (breakpointy), zdalne eval Lua; profiling runtime; zL'oLLone RPC do klienta (inne niLL plik/log/skrot).

---
## 3. Architektura systemu
**Wariant rekomendowany:** Desktop **Electron** (React/TS + Node/FS), integracja z OTClient przez system plikow i skrot hota'reload.

+--------------------+       IPC        +-------------------+
| React/TS Frontend  | <--------------> | Electron Main/Pre |
| (Vite + Monaco)    |                  |   + Node/FS       |
+--------------------+                  +-------------------+
          |   FS (read/write JSON, pliki projektu)             
v
+--------------------+         plik/flag/log         +----------------+
|  Projekt lokalny   | <----------------------------> |  OTClient v8  |
| (lua/otui/otmod/a|) |                               | (hota'reload)  |
+--------------------+                                +----------------+
```

**Alternatywa web:** React + lokalny serwis Node (HTTP/WebSocket) + File System Access API (ograniczenia dostepu; rekomendowane tylko gdy Electron jest niewskazany).

---
## 4. Wymagania funkcjonalne (FR)
**FRa'01 - Projekty:** wybor katalogu, ostatnie projekty, walidacja (`modules/`, `.otmod`).
**FRa'02 - Eksplorator:** drzewo `.lua/.otui/.otmod` + assets; CRUD na plikach; draga'drop; operacje atomowe.
**FRa'03 - Edytor:** Monaco (Lua/OTUI/OTML/JSON), goa'to symbol, minimapa, format, folding.
**FRa'04 - IntelliSense:** hover, signature help, autocomplete z `api.json` + indeks projektu + docstrings.
**FRa'05 - Lint OTUI:** kolejnoLc pol, `tr()` dla staL'ych, anchors/margins, istnienie zasobow; autoa'fix dla kolejnoLci i `tr()`.
**FRa'06 - Lint Lua (lite):** preferuj `local`, wykryj globalne; `table.unpack` vs `unpack`.
**FRa'07 - Generator:** moduL'y (`.otmod` + `main.lua` + `ui/*.otui`) + snippety vBot z checklista.
**FRa'08 - Skan/Indeks:** glob, parsery Lua/OTUI/OTML, relacje `dofile/require` i `g_ui.loadUI`; cache inkrementalny.
**FRa'09 - Integracja z OTClient:** przycisk "PrzeL'aduj w kliencie" (skrot/flag file).
**FRa'10 - Log Viewer:** tail NDJSON/tekst, filtry (level/tag/file:line), wyszukiwarka, eksport.
**FRa'11 - Ustawienia:** LcieLLki artefaktow i logu, ignore patterns, motyw; import/eksport.
**FRa'12 - Wbudowany help:** panel "API & Howa'to", wyszukiwarka offline.

**Kryteria akceptacji (wybrane):** indeks 5k plikow < 5 s z cache; brak crashy przy edycji plikow 2 MB; >90% trafieL" podpowiedzi dla znanych symboli; autoa'fix deterministyczny.

---
## 5. Wymagania niefunkcjonalne (NFR)
- **Perf:** indeks < 5 s (cache), < 30 s zimny start; Monaco 60 FPS podczas pisania.
- **Security:** brak sieci (offlinea'first), sandbox Renderer, IPC whitelist, brak uruchamiania Lua.
- **Portability:** Windows/macOS/Linux; Web (opcjonalnie, ograniczenia FS API).
- **Reliability:** zapisy atomowe (tempa'rename), odtwarzanie cache po awarii.

---
## 6. Kontrakty i modele danych (kanoniczne, wersjonowane)
> KaLLdy JSON zawiera `$schemaVersion` i jest walidowany testami kontraktowymi.
## 6.1. `resources/api.json` (kuratorowane, seed + ingest)
{
  "$schemaVersion": 1,
  "generatedAt": "2025-10-02T00:00:00Z",
  "functions": [
    {"name": "g_modules.reloadModules", "module": "g_modules", "params": [], "returns": [], "description": "PrzeL'adowuje moduL'y i skrypty OTClient.", "since": "v8"},
    {"name": "g_resources.readFile", "module": "g_resources", "params": [{"name": "path", "type": "string"}], "returns": [{"type": "string"}], "description": "Czyta plik do stringa."},
    {"name": "g_resources.writeFile", "module": "g_resources", "params": [{"name": "path", "type": "string"}, {"name": "data", "type": "string"}], "returns": [{"type": "boolean"}], "description": "Zapisuje string do pliku."}
],
  "events": [
    {"name": "onGameStart", "target": "Game", "payload": [], "description": "WywoL'ywane przy starcie gry."}
],
  "objects": [
    {"name": "g_resources", "members": ["readFile", "writeFile"], "description": "MenedLLer zasobow."}
]
}
```
> **Uwaga:** to seed. PeL'ny `api.json` powstaje wg 7 z lokalnych plikow dokumentacji.
## 6.2. `project-index.json` (z automatycznego skanu)
{
  "$schemaVersion": 1,
  "root": "/abs/path/to/project",
  "files": {"lua": ["modules/game_bot/bot.lua", "modules/client/client.lua"], "otui": ["modules/client/ui/main.otui"], "otmod": ["modules/client/client.otmod"]},
  "symbols": {"functions": {"reloadScripts": ["modules/client/client.lua:120"]}, "widgets": {"MainWindow": ["modules/client/ui/main.otui:5"]}},
  "relations": {"lua_to_otui": [{"lua": "modules/client/client.lua", "otui": "modules/client/ui/main.otui", "via": "g_ui.loadUI"}], "includes": [{"from": "modules/a/main.lua", "to": "modules/a/util.lua", "via": "dofile"}]}
}
```
## 6.3. `otui-rules.json` (lint/autoa'fix)
{"$schemaVersion":1,"rules":[{"id":"OTUI-001","description":"KolejnoLc pol: GEOMETRIAa'STYLa'ZACHOWANIE.","fixable":true},{"id":"OTUI-002","description":"StaL'e stringi musza uLLywac tr().","fixable":true},{"id":"OTUI-003","description":"Walidacja anchors/margins (brak sprzecznoLci).","fixable":false},{"id":"OTUI-004","description":"Weryfikacja istnienia zasobow (obrazy, fonty, style).","fixable":false}]}
```
## 6.4. `templates.json` (generator)
{"$schemaVersion":1,"module.default":{"title":"ModuL' OTClient - szkielet","files":[{"path":"modules/hello/hello.otmod","contents":"name: hello\n"},{"path":"modules/hello/hello.lua","contents":"-- entry point\nlocal M = {}\nreturn M\n"},{"path":"modules/hello/ui/hello.otui","contents":"MainWindow < UIWidget { }\n"}],"checklist":["UmieLc katalog w modules/","Uruchom klienta i przeL'aduj moduL'y","SprawdLs log po starcie moduL'u"]}}
```
## 6.5. `docstrings.json`
{"$schemaVersion":1,"entries":[{"file":"modules/x/main.lua","line":10,"symbol":"foo","params":[{"name":"a","type":"number"}],"returns":[{"type":"boolean"}],"comment":"---@param a number\n---@return boolean"}]}
```
## 6.6. `assets-map.json`
{"$schemaVersion":1,"assets":{"images":["images/button.png"],"fonts":["fonts/verdana.otf"],"styles":["styles/dark.otui"]}}
```
## 6.7. `.studio/config.json`
{"$schemaVersion":1,"projectRoot":"/abs/path/to/project","apiPath":"resources/api.json","otuiRulesPath":"resources/otui-rules.json","templatesPath":"resources/templates.json","logPath":"/abs/path/to/log.ndjson","ignore":["**/node_modules/**",".git/**"]}
```

---
## 7. Procedura ingest - budowa `api.json`
**WejLcia:** lokalne pliki dokumentacji (`OTClient_data_documentation_FULL.md`, `luafunctionscpp.md`, `modules_Documentation.md`, `src framework.md`, `src client.md`).

**Kroki:**
1) Segmentacja MD (H1-H3) i klasyfikacja sekcji: API/Events/Hooks/Globals/Managers.
2) Ekstrakcja sygnatur: `name(params) -> returns`, opisow, przykL'adow, statusu (`since/deprecated`).
3) Normalizacja nazewnictwa (`module`: `g_resources`, `g_modules`, itp.).
4) Walidacja: unikalne `name`, kompletne `params/returns`.
5) Scalanie z `docstrings.json` (uzupeL'nienia typow/przykL'adow).
6) Eksport `resources/api.json` (dodaj `generatedAt`, `$schemaVersion`).

**Wzorce (regex - przykL'adowe):**
- Funkcja: `^\s*([A-Za-z0-9_\.\:]+)\s*\(([^)]*)\)\s*(?:->\s*([^\n{]+))?`
- Param: `---@param\s+(\w+)\s+([\w<>\|]+)`
- Return: `---@return\s+([\w<>\|]+)`
- Event: `\bon[A-Z][A-Za-z0-9]+\b` (lub sekcje "Events").

**Polityka typow:** `string|number|boolean|table|any|nil|function|userdata`; `optional` jeLli oznaczone `?` lub w kwadratowych nawiasach.

**Quality Gate:** 0 duplikatow; aA95% pozycji z opisem i kompletnymi parametrami; walidacja JSON wg schematu.

---
## 8. Skaner i parsery - specyfikacja
**FS skan:** glob `**/*.{lua,otui,otmod}`; wyklucz `.git/**`, `**/node_modules/**`, `**/.studio-cache/**`; hash (size+mtime) a' indeks inkrementalny.

**Parser Lua:**
- Tokenizacja: identyfikatory, stringi, komentarze (`--`, blokowe), sL'owa kluczowe.
- Ekstrakcja: `function name(...)`, `obj:method(...)` (pozycja file:line).
- Docstrings: `---` + adnotacje `---@param`, `---@return` a' `docstrings.json`.
- Relacje: `dofile("path")`, `require("...")` a' `relations.includes`.
- Heurystyki vBot: wykrywanie `macro(`, `onTextMessage`, itp. a' tag `botSymbols`.

**Parser OTUI/OTML:**
- AST wg skroconej EBNF:
File := (Decl | Comment)*
Decl := Type ("<" Base ">")? "{" (KV | Decl)* "}"
KV   := Key ":" Value
Value:= String | Number | Bool | Ident | Array | Object
```
- Kategoryzacja atrybutow: GEOMETRIA (`x`,`y`,`width`,`height`,`anchors`,`margin`), STYL (`font`,`color`,`image`,`style`), ZACHOWANIE (`draggable`,`onClick`,`id`).
- Relacje: `g_ui.loadUI("path")` a' `relations.lua_to_otui`.

**Parser `.otmod`:** klucz:wartoLc (+ listy); wymagane `name`; waliduj znaki w `name`.

**Kody bL'edow parsera:** `P001` (Lua tokenizer), `P101` (OTUI niezamkniety blok), `P201` (.otmod brak `name`).

---
## 9. Lint/Autoa'fix - reguL'y
- **OTUIa'001 (order):** sortuj atrybuty: GEOMETRIA a' STYL a' ZACHOWANIE (autoa'fix: przetasuj z zachowaniem komentarzy).
- **OTUIa'002 (tr):** staL'e literaL'y string wrapuj `tr()` (autoa'fix; ignoruj `id`/nazwy klas).
- **OTUIa'003 (anchors):** wykryj sprzecznoLci anchors/margins (sugestie, bez autoa'fix).
- **OTUIa'004 (assets):** zgL'oL brakujace zasoby (fuzzy podpowiedzi).
- **LUAa'001 (locals):** ostrzegaj globali; autoa'fix: `local` jeLli bez kolizji.
- **LUAa'002 (unpack):** zamieniaj `unpack` -> `table.unpack` (autoa'fix bezpieczny).

---
## 10. Integracja z OTClient (hota'reload, logi)
**Tryb A (podstawowy):** zapis a' skrot hota'reload w kliencie (np. Ctrl+Shift+R).

**Tryb B (z moduL'em dev):** Studio zapisuje `modules/.dev/reload.flag`; moduL' dev w kliencie wykrywa i:
1) wywoL'uje `g_modules.reloadModules()`,
2) usuwa/przepisuje plik flagi,
3) opcjonalnie loguje wynik (NDJSON) do `modules/.dev/log.jsonl`.

**Szkic moduL'u dev (Lua):**
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

PrzykL'ad:
{"ts":"2025-10-02T12:34:56.789Z","level":"INFO","tag":"dev","file":"modules/x/main.lua","line":42,"msg":"Hot reload done","meta":{"changed":3}}
```

---
## 11. UI/UX (ekrany i przepL'ywy)
- **Start:** wybor/ostatnie projekty, skroty do dokumentacji, "Nowy moduL'".
- **Eksplorator:** drzewo plikow, akcje kontekstowe, status operacji FS.
- **Edytor:** Monaco + panel boczny (API/Doc), statusbar (pozycja, problems, encoding).
- **Diagnostyka:** lista Issues (filtry), Quick Fix, przejLcia do linii.
- **API Browser:** lista obiektow a' szczegoL'y (opis, params, examples) a' "Wstaw snippet".
- **Log Viewer:** stream z filtrami (ERR/WARN/INFO), szukanie, pauza, eksport.
- **Ustawienia:** LcieLLki zasobow, logu, motyw, ignorowane foldery, mapowanie skrotu.

---
## 12. IPC (Electron) - kontrakty
- `studio:scan:start` - req: `{root}` a' res: `project-index.json` | err: `{code,msg}`
- `studio:api:load` - req: `{path}` a' res: `api.json`
- `studio:lint:run` - req: `{files[]}` a' res: `{problems[]}`
- `studio:templates:generate` - req: `{templateId, targetDir, vars}` a' res: `{createdFiles[]}`
- `studio:log:tail` - req: `{path}` a' stream: `{line}` | `{eof}` | `{error}`

**BL'edy:** `E_FS_001` (dostep FS), `E_PARSE_LUA`, `E_PARSE_OTUI`, `E_JSON_SCHEMA`.

---
## 13. Warstwa stanu FE
- **Zustand:** `projectStore`, `editorStore`, `diagnosticsStore`, `apiStore`, `logStore`.
- **Persist:** `.studio/config.json` przez backend FS.
- **Normalizacja:** mapy symboli `name -> {files[]}`.

---
## 14. BezpieczeL"stwo i prywatnoLc
- Renderer sandbox, restrykcyjne IPC, brak sieci (domyLlnie), brak wykonywania Lua.
- Backup `.bak` przy autoa'fixach; zapisy atomowe.

---
## 15. WydajnoLc i stabilnoLc
- Worker Threads dla parserow; debounce 150 ms; cache w `.studio-cache/`.
- "Big file mode" w Monaco > 2 MB (ograniczenie czeLci funkcji).

---
## 16. i18n, A11y, theming
- i18n: `en`/`pl`; wymuszaj `tr()` w OTUI poprzez lint.
- A11y: ARIA, focus outlines, kontrast WCAG AA.
- Tematy: Light/Dark/Higha'Contrast; zapis w config.

---
## 17. Testy i QA
- **Unit:** parsery (Lua/OTUI), lint rules, generator.
- **Contract:** walidacja JSON kontra schemat, IPC payloady/typy.
- **Integration:** skan 5k plikow, pomiary czasu/RAM.
- **E2E (Playwright):** flow "Open a' Edit a' Lint a' Generate a' Reload a' Logs".
- **Regression:** snapshot AST/diagnostyki.

**DoD (final):** patrz 21 - wszystkie punkty odhaczone.

---
## 18. Build/Release/Update
- `electron-builder` (Win NSIS, macOS dmg, Linux AppImage); podpisy binarek.
- Autoa'update (opcjonalny), domyLlnie wyL'aczony - narzedzie offlinea'first.

---
## 19. Observability narzedzia
- Log aplikacji: `.studio/logs/app.ndjson`; poziomy: DEBUG/INFO/WARN/ERROR.
- Metryki: czas skanu, liczba plikow, czas lintu, bL'edy parserow.

---
## 20. Migracje i zgodnoLc
- `$schemaVersion` w artefaktach; migracje `vN -> vN+1` dla config/cache.

---
## 21. Plan wdroLLenia i checklisty
**Etap 0 - Inicjalizacja**
- [ ] Monorepo (pnpm), Vite+React+TS, Electron scaffold.
- [ ] Monaco, routing, layout.

**Etap 1 - Kontrakty i zasoby**
- [ ] Interfejsy TS (ApiFunction/ApiEvent/ProjectIndex/OtuiRule/Template).
- [ ] Dodac `resources/api.json` (seed), `otui-rules.json`, `templates.json`.

**Etap 2 - Skaner/Parsery**
- [ ] Glob/FS, cache, incremental hashing.
- [ ] Parser Lua + docstrings + relacje.
- [ ] Parser OTUI/OTML + kategoryzacja atrybutow.
- [ ] Parser `.otmod`.

**Etap 3 - IDE/UX**
- [ ] Explorer, Edytor, API Browser.
- [ ] Diagnostyka + Quick Fix.

**Etap 4 - Integracja z klientem**
- [ ] PrzeL'aduj (skrot/flag) + Log Viewer.

**Etap 5 - Stabilizacja**
- [ ] Testy (unit/contract/integration/E2E), pakiety instalacyjne.

**Definition of Done (KoL"cowe):**
- [ ] Aplikacja offline; projekty sie otwieraja; indeks i symbole dziaL'aja.
- [ ] `api.json` zasila podpowiedzi (hover/complete/signature help).
- [ ] Lint OTUI/Lua i autoa'fix (backup `.bak`).
- [ ] Integracja z OTClient: hota'reload + logi stabilne.
- [ ] Pakiety Win/macOS/Linux; dokumentacja uLLytkownika; sample project.

---
## 22. Ryzyka i mitigacje
- **Brak stepa'debuggera:** Log Viewer + snippety logujace + mapowanie file:line.
- **RoLLnice wersji:** `since/deprecated` w `api.json`, profile klienta.
- **WydajnoLc:** indeks inkrementalny, workers, throttling.
- **Parsery:** testy kontraktowe + snapshoty, tolerant parsing.

---
## 23. Artefakty - komplet MVP (gotowe w tym dokumencie)
- `resources/api.json` - seed (6.1 + 24.A)
- `resources/otui-rules.json` - (6.3 + 24.B)
- `resources/templates.json` - (6.4 + 24.C)
- `docstrings.json` - format (6.5)
- `assets-map.json` - format (6.6)
- `.studio/config.json` - format (6.7)

---
## 24. PrzykL'adowe dane (seed do startu)
**A. `resources/api.json` (seed)** - patrz 6.1 (peL'ny JSON wstawiony).

**B. `resources/otui-rules.json` (seed)** - patrz 6.3 (peL'ny JSON wstawiony).

**C. `resources/templates.json` (seed)** - patrz 6.4 (peL'ny JSON wstawiony).

---
## 25. Noty koL"cowe
- Ten dokument jest **LsrodL'em prawdy (SoT)**. Dodatkowe canvasy musza odwoL'ywac sie do sekcji () i kontraktow tutaj zdefiniowanych.
- Zmiany wymagaja podniesienia `$schemaVersion` i przejLcia testow kontraktowych.
- Wszelkie dane sa przygotowane z myLla o pracy **offline** w oparciu o lokalne pliki dokumentacji i kodu.
