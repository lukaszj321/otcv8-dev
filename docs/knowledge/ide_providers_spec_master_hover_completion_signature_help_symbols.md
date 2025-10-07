?# IDE Providers Spec (MASTER) - **Hover**, **Completion**, **Signature Help**, **Symbols**

> Cel: pelna specyfikacja warstwy IDE dla **OTClient Studio** (Monaco + Electron). Dokument definiuje kontrakty, algorytmy, scoring, trigger-y, schematy JSON, IPC, test-wektory i wymagania wydajnosci. **Transfer 1:1** - gotowe do bezposredniej implementacji.

---
# # 0) Zalozenia i kontekst
- **Jezyki:** `lua` (Lua-Lite) i `otui` (OTUI/OTML).
- **Zr�dla wiedzy:** `resources/api.json` (kuratorowane), `project-index.json` (skan), `docstrings.json` (adnotacje), `otui-rules.json` (lint).
- **Silnik:** Monaco Editor (providers + Diagnostics).
- **Cele:** wysoka trafnosc podpowiedzi, determinizm wynik�w, niskie op�znienia (UX 60 FPS).

---
# # 1) Rejestracja jezyk�w i provider�w (Monaco)
# # # 1.1 Identyfikatory
- `languageId.luastudio = "lua"` (dialekt Lua-Lite)
- `languageId.otuistudio = "otui"`
# # # 1.2 Rejestracja
- `monaco.languages.register({ id: languageId.luastudio })`
- `monaco.languages.register({ id: languageId.otuistudio })`
# # # 1.3 Providerzy (interfejsy Monaco)
- **Completion**: `registerCompletionItemProvider(id, provider)`
- **Hover**: `registerHoverProvider(id, provider)`
- **Signature Help**: `registerSignatureHelpProvider(id, provider)`
- **Document Symbols**: `registerDocumentSymbolProvider(id, provider)`
- **Definition/References**: (opcjonalnie MVP+) `registerDefinitionProvider`, `registerReferenceProvider`

> Dostawcy komunikuja sie z warstwa analiz przez **IPC** (sekcja �7) i uzywaja lokalnych cache'y (sekcja �6).

---
# # 2) Completion (auto-uzupelnianie)
# # # 2.1 Triggery
- **Lua**: `.` `:` `(` `,` spacja po `function`/`local` oraz po `on` (eventy).
- **OTUI**: poczatek linii/po `\n`, po `:` (wartosc), w nagl�wku deklaracji po `"<"` (typ bazowy), w kluczu (sugestie atrybut�w wg kategorii), po `style:` (style zasob�w).
# # # 2.2 Zr�dla sugestii
1) **API globalne** (`api.json`): `g_*` managery, funkcje, eventy.
2) **Symbole projektu** (`project-index.json`): funkcje zdefiniowane lokalnie, widzety OTUI, pliki/sciezki.
3) **Docstrings** (`docstrings.json`): parametry i typy - doprecyzowanie sygnatur.
4) **Heurystyki vBot**: `macro(`, `onTextMessage`, `say(` itp. - boost rank.
# # # 2.3 Scoring i ranking
Kazdy kandydat ma **score** ? [0..1]. Koncowa kolejnosc = malejaco po `score`, tie-break: dlugosc nazwy ?, alfabetycznie.

**Skladniki score:**
- `s_prefix` - dopasowanie prefiksu (FZF/substring): 0.6-1.0
- `s_source` - priorytet zr�dla: API=1.0, projekt=0.9, docstring=0.85, heurystyka=0.8
- `s_context` - trafnosc kontekstu (np. po `.` proponuj czlonk�w obiektu; po `:` metody; w OTUI klucze): 0.0-0.3
- `s_recent` - pamiec ostatnio uzytych: +0.05 (TTL)

`score = 0.7*s_prefix + 0.2*s_source + 0.1*s_context + s_recent`
# # # 2.4 Typy pozycji (Monaco CompletionItemKind)
- `Function`, `Method`, `Property`, `Variable`, `Class` (OTUI typy), `Keyword`, `Snippet`, `File`, `Folder`.
# # # 2.5 Snippety i InsertText
- **Lua - funkcja lokalna:** `local ${1:name} = function(${2:args})\n  ${0}\nend`
- **Lua - modul skeleton:** `local M = {}\nfunction M.${1:fn}(${2})\n  ${0}\nend\nreturn M`
- **OTUI - widzet:** `${1:Widget} < ${2:UIWidget} {\n  id: ${3:id}\n  width: ${4:100}\n  text: tr("${5:Text}")\n}`
# # # 2.6 Kontekstowe listy
- **Lua `.`/`:`** ? czlonkowie obiektu (`api.json.objects[].members`) + symbole znalezione w projekcie.
- **OTUI klucz** ? lista atrybut�w dozwolonych przez typ (kategoria + reguly `otui-rules.json`).
- **OTUI wartosc `style:`** ? style z `assets-map.json.styles`.
# # # 2.7 Przyklad odpowiedzi (IPC ? FE)
```json
{
  "items": [
    {"label":"g_modules.reloadModules","kind":"Function","detail":"OTClient v8","insertText":"g_modules.reloadModules()","range": {"start":123,"end":123},"score":0.98},
    {"label":"g_resources.readFile","kind":"Method","detail":"string readFile(path)","insertText":"g_resources.readFile(${1:path})","insertTextRules":"snippet","score":0.93}
],
  "isIncomplete": false,
  "ttlMs": 3000
}
```

---
# # 3) Hover (podglad dokumentacji)
# # # 3.1 Zasady agregacji
- Preferuj opis z **`api.json`**; jezeli brak ? **`docstrings.json`**; nastepnie heurystyki (np. typ identyfikatora z kontekstu).
- Dodaj **sygnature**, **opis**, **odsylacze** (plik:linia) i przyklad.
# # # 3.2 Format tresci (Markdown)
- Nagl�wek: **Nazwa** i sygnatura, typ zwracany.
- Sekcje: `Opis`, `Parametry`, `Zwraca`, `Przyklad`, `Zr�dlo`.
# # # 3.3 Przyklad odpowiedzi
```json
{
  "contents": [
    {"value": "**g_modules.reloadModules()**? *void*\n\nPrzeladowuje moduly i skrypty w OTClient.\n\n**Zr�dlo:** api.json (v8)", "isTrusted": true}
],
  "range": {"start": 100, "end": 124},
  "ttlMs": 10000
}
```

---
# # 4) Signature Help (podpowiedz parametr�w)
# # # 4.1 Triggery
- **Lua:** po wpisaniu `(` oraz po `,` w kontekscie wywolania.
- **OTUI:** (opcjonalnie) dla funkcji/event handler�w w wartosciach `on...` (jezeli projekt dopuszcza).
# # # 4.2 Agregacja sygnatur
- **Priorytet:** `docstrings.json` (najbardziej szczeg�lowe typy) ? `api.json` ? heurystyka (typ `any`).
# # # 4.3 Model danych
```json
{
  "signatures": [
{
      "label": "g_resources.readFile(path: string): string",
      "parameters": [
        {"label": "path: string", "documentation": "Sciezka do pliku"}
]
}
],
  "activeSignature": 0,
  "activeParameter": 0,
  "ttlMs": 5000
}
```

---
# # 5) Document Symbols / Definition / References (MVP+)
# # # 5.1 Document Symbols (w pliku)
- **Lua:** `FunctionDecl`, `LocalStatement (function)`, `TableConstructor (klucze funkcji)`.
- **OTUI:** `Decl` (nazwa widzetu + `id`), klucze `KV` jako *children*.

**Output (przyklad):**
```json
{"symbols":[{"name":"M.reload","kind":"Function","range":{...},"selectionRange":{...}}]}
```
# # # 5.2 Definition
- **Lua:** nazwa funkcji/identyfikatora ? lokalizacja deklaracji w biezacym pliku lub w `project-index.json.symbols`.
- **OTUI:** `WidgetName`/`id` ? definicja `Decl` w pliku.
# # # 5.3 References
- Przeszukanie `project-index.json` i lekkie skanowanie token�w (prefiltrowanie po hashach plik�w).

---
# # 6) Cache, debounce i wydajnosc
- **Cache L1 (process):** rezultaty zapytan na 3-10 s (`ttlMs` w odpowiedzi). Inwalidacja na zapis/zmiane pliku.
- **Cache L2 (disk):** indeksy `project-index.json` i `docstrings.json` w `.studio-cache/`.
- **Debounce:** 120-180 ms na zapytania provider�w (per dokument).
- **Budzet czasu:** cel < 6 ms na runde completions (po cache), < 25 ms cold.
- **Big file mode:** > 2 MB: ogranicz liczbe kandydat�w (np. top 50).

---
# # 7) IPC i kontrakty uslug (backend parsers/service)
# # # 7.1 Kanaly
- `ide:completion` ? req: `CompletionQuery` ? res: `CompletionResult`
- `ide:hover` ? req: `HoverQuery` ? res: `HoverResult`
- `ide:signature` ? req: `SignatureQuery` ? res: `SignatureResult`
- `ide:symbols` ? req: `{uri}` ? res: `DocumentSymbols`
- (MVP+) `ide:definition`, `ide:references`
# # # 7.2 Modele zapytan/odpowiedzi
```json
{
  "$schemaVersion": 1,
  "CompletionQuery": {"uri":"file:///...","language":"lua|otui","position":123,"prefix":"g_res","context":{"trigger":".","scope":"expr|key|value"}},
  "CompletionResult": {"items":[],"isIncomplete":false,"ttlMs":3000},

  "HoverQuery": {"uri":"file:///...","language":"lua|otui","range":{"start":100,"end":124}},
  "HoverResult": {"contents":[{"value":"...md...","isTrusted":true}],"range":{"start":100,"end":124},"ttlMs":10000},

  "SignatureQuery": {"uri":"file:///...","language":"lua|otui","callPos":130},
  "SignatureResult": {"signatures":[],"activeSignature":0,"activeParameter":0,"ttlMs":5000},

  "DocumentSymbols": {"symbols":[{"name":"...","kind":"Function","range":{}}]}
}
```
# # # 7.3 Bledy
- Formaty: `{code,msg,details?}`; kody: `IDE_Q_BAD_REQ`, `IDE_S_TIMEOUT`, `IDE_D_SCHEMA`.

---
# # 8) Algorytmy agregacji (pseudokod TS)
# # # 8.1 Completion (Lua)
```ts
function completeLua(q: CompletionQuery): CompletionResult {
  const ctx = analyzeContextLua(q);
  const api = apiCatalog.lookup(ctx.object, ctx.memberPrefix); // api.json
  const proj = projectIndex.members(ctx.object, ctx.memberPrefix); // project-index
  const docs = docstrings.find(ctx.memberPrefix); // docstrings
  const heur = heuristicsVBot(ctx);
  const cand = mergeDedup([api, proj, docs, heur]);
  const scored = cand.map(c => ({...c, score: score(c, q)}));
  return finalize(scored, q);
}
```
# # # 8.2 Completion (OTUI)
```ts
function completeOTUI(q: CompletionQuery): CompletionResult {
  if (q.context.scope === 'key') return keysForWidget(q); // kategorie + rules
  if (q.context.scope === 'value' && q.context.key === 'style') return stylesFromAssets();
  if (q.context.scope === 'typeBase') return widgetBaseTypes();
  return genericOtuiSnippets();
}
```
# # # 8.3 Hover
```ts
function hover(q: HoverQuery): HoverResult {
  const sym = resolveSymbolAt(q.uri, q.range);
  const a = api.jsonSym(sym);
  const d = docstrings.for(sym);
  const m = mergeDocs(a, d);
  return renderMarkdown(m);
}
```
# # # 8.4 Signature Help
```ts
function signature(q: SignatureQuery): SignatureResult {
  const call = findCallAt(q.callPos);
  const fromDocs = docstrings.signature(call.callee) || api.signature(call.callee) || anySignature(call.args);
  return toSignatureResult(fromDocs, call.argIndex);
}
```

---
# # 9) Integracja z lintem i nawigacja
- **Diagnostics**: provider lintu OTUI/Lua publikuje problemy zgodnie z regulami; IDE moze proponowac **Quick Fix** (np. OTUI-001/002).
- **Go-to Definition**: uzyj `project-index.symbols` + lokalnego AST.
- **Peek References**: wyszukiwanie symboli w indeksie; prefiltrowanie po nazwach.

---
# # 10) Konfiguracja (Ustawienia uzytkownika)
```json
{
  "$schemaVersion": 1,
  "completion": {"enable": true, "maxItems": 50, "fuzzy": true, "boostVBot": true},
  "hover": {"enable": true, "markdown": true},
  "signature": {"enable": true},
  "symbols": {"enable": true},
  "ranking": {"wPrefix": 0.7, "wSource": 0.2, "wContext": 0.1},
  "performance": {"debounceMs": 150, "bigFileLimit": 2000000}
}
```

---
# # 11) Test-wektory i QA
- **COMP-01 (Lua):** `g_res` + `.` ? zawiera `g_resources.readFile` (score > 0.9).
- **COMP-02 (OTUI):** w kluczu ? lista `GEOMETRY`/`STYLE`/`BEHAVIOR` wedlug regul; `style:` zwraca style z assets.
- **HOV-01:** na `g_modules.reloadModules` ? opis z `api.json`.
- **SIG-01:** `g_resources.readFile(` ? `path: string` w `activeParameter=0`.
- **SYM-01:** `Document Symbols` zwraca funkcje i widzety z poprawnymi zakresami.
- **PERF-01:** czas odpowiedzi completions (cache warm) < 6 ms, (cold) < 25 ms.

---
# # 12) Wydajnosc i telemetria
- Zbieraj metryki: sredni czas odpowiedzi provider�w, hit ratio cache, liczba kandydat�w po deduplikacji.
- Ostrzezenia w logu aplikacji, gdy cold-path > 50 ms lub liczba kandydat�w > 500.

---
# # 13) Checklisty wdrozeniowe
- [ ] Rejestracja provider�w dla `lua` i `otui`.
- [ ] Implementacja kanal�w IPC (�7) + schemat�w zapytan/odpowiedzi.
- [ ] Agregacja `api.json` + `project-index.json` + `docstrings.json` (rankowanie �2.3).
- [ ] Snippety i trigger-y (�2.1, �2.5).
- [ ] Hover/Signature z fallbackami (�3, �4).
- [ ] Document Symbols (MVP), Definition/References (MVP+).
- [ ] Cache i debounce (�6); budzety czasu i big-file mode.
- [ ] Test-wektory (�11) zielone; telemetria (�12) aktywna.

---
# # 14) Noty koncowe
- Wyniki provider�w musza byc **stabilne** miedzy uruchomieniami (deterministyczne sortowanie); r�znice jedynie przy zmianie kontekstu lub danych.
- Wszelkie rozszerzenia musza zachowac kontrakty IPC i schematy JSON (wersjonowanie `$schemaVersion`).
