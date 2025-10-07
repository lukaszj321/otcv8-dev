# Parser & Schemas (MASTER): **AST + JSON Schema** dla **OTClient Studio**

> Cel dokumentu: dostarczyÄ‡ **kompletne, operacyjne** specyfikacje parserĂłw (LuaĂ˘â‚¬â€Lite, OTUI/OTML) oraz **kontrakty walidacyjne** (JSON Schema) dla artefaktĂłw narzÄ™dzia: `api.json`, `project-index.json`, `otui-rules.json`, `templates.json`, `docstrings.json`, `assets-map.json`, `.studio/config.json`, a takÄąÄ˝e **schemat linii logu NDJSON**. Wszystko w formie gotowej do bezpoÄąâ€şredniej implementacji (TypeScript/Node) i automatycznej walidacji.

---
## 0) ZaÄąâ€šoÄąÄ˝enia ogĂłlne
- **DeterministycznoÄąâ€şÄ‡:** Emisja AST/indeksĂłw musi byÄ‡ deterministyczna (stabilne sortowanie kluczy, list po `loc.start.offset`).
- **Lokalizacja (`loc`):** KaÄąÄ˝dy wÄ™zeÄąâ€š ma `loc`:
`$fenceInfo
{"file":"/abs/path.lua","start":{"offset":123,"line":5,"column":10},"end":{"offset":140,"line":5,"column":27}}
```
- **Identyfikator wÄ™zÄąâ€ša (`id`)**: opcjonalny, `sha1(file + start.offset + type)`.
- **Tolerant parsing:** Parser nie przerywa na pierwszy bÄąâ€šÄ…d; emituje `errors[]` i moÄąÄ˝liwie peÄąâ€šne AST.
- **Kody bÄąâ€šÄ™dĂłw:** prefiksowane domenÄ… (`LUA_`, `OTUI_`, `OTMOD_`, `GEN_`). Sekcja 7.

---
## 1) OTUI/OTML â€” Gramatyka i AST
## 1.1 Gramatyka (EBNF â€“ praktyczna)
`$fenceInfo
File        := (Decl | Comment)*
Decl        := Type ("<" Base ">")? Spacing? "{" Body "}"
Body        := (KV | Decl | Comment)*
KV          := Key Spacing? ":" Spacing? Value
Type        := Ident
Base        := Ident
Key         := Ident
Value       := String | Number | Bool | Ident | Array | Object
Array       := "[" (Value ("," Value)*)? "]"
Object      := "{" (KV ("," KV)*)? "}"
Comment     := /#.*$/
Ident       := /[A-Za-z_][A-Za-z0-9_\-]*/
String      := '"' (\\.|[^"\\])* '"' | '\'' (\\.|[^'\\])* '\''
Number      := /[-+]?[0-9]+(\.[0-9]+)?/
Bool        := "true" | "false"
```
## 1.2 AST OTUI â€” JSON Schema
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/otui-ast.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "OTUI AST",
  "type": "object",
  "required": ["type", "loc", "body"],
  "properties": {
    "type": {"const": "OTUIFile"},
    "loc": {"$ref": "#/definitions/Loc"},
    "errors": {"type": "array", "items": {"$ref": "#/definitions/ParseError"}},
    "body": {
      "type": "array",
      "items": {"$ref": "#/definitions/Node"}
}
},
  "definitions": {
    "Loc": {
      "type": "object",
      "required": ["file","start","end"],
      "properties": {
        "file": {"type": "string"},
        "start": {"$ref": "#/definitions/Pos"},
        "end": {"$ref": "#/definitions/Pos"}
}
},
    "Pos": {
      "type": "object",
      "required": ["offset","line","column"],
      "properties": {
        "offset": {"type": "integer", "minimum": 0},
        "line": {"type": "integer", "minimum": 1},
        "column": {"type": "integer", "minimum": 1}
}
},
    "ParseError": {
      "type": "object",
      "required": ["code","message","loc"],
      "properties": {
        "code": {"type": "string"},
        "message": {"type": "string"},
        "loc": {"$ref": "#/definitions/Loc"}
}
},
    "Node": {
      "oneOf": [
        {"$ref": "#/definitions/Decl"},
        {"$ref": "#/definitions/KV"}
]
},
    "Decl": {
      "type": "object",
      "required": ["type","name","loc","body"],
      "properties": {
        "type": {"const": "Decl"},
        "name": {"type": "string"},
        "base": {"type": ["string","null"]},
        "id": {"type": ["string","null"]},
        "loc": {"$ref": "#/definitions/Loc"},
        "body": {
          "type": "array",
          "items": {"$ref": "#/definitions/Node"}
}
}
},
    "KV": {
      "type": "object",
      "required": ["type","key","value","loc"],
      "properties": {
        "type": {"const": "KV"},
        "key": {"type": "string"},
        "value": {"$ref": "#/definitions/Value"},
        "category": {"type": ["string","null"], "enum": ["GEOMETRY","STYLE","BEHAVIOR",null]},
        "loc": {"$ref": "#/definitions/Loc"}
}
},
    "Value": {
      "oneOf": [
        {"$ref": "#/definitions/StringLiteral"},
        {"$ref": "#/definitions/NumberLiteral"},
        {"$ref": "#/definitions/BooleanLiteral"},
        {"$ref": "#/definitions/Identifier"},
        {"$ref": "#/definitions/ArrayLiteral"},
        {"$ref": "#/definitions/ObjectLiteral"}
]
},
    "StringLiteral": {"type":"object","required":["type","value","loc"],"properties":{"type":{"const":"StringLiteral"},"value":{"type":"string"},"loc":{"$ref":"#/definitions/Loc"}}},
    "NumberLiteral": {"type":"object","required":["type","value","loc"],"properties":{"type":{"const":"NumberLiteral"},"value":{"type":"number"},"loc":{"$ref":"#/definitions/Loc"}}},
    "BooleanLiteral": {"type":"object","required":["type","value","loc"],"properties":{"type":{"const":"BooleanLiteral"},"value":{"type":"boolean"},"loc":{"$ref":"#/definitions/Loc"}}},
    "Identifier": {"type":"object","required":["type","name","loc"],"properties":{"type":{"const":"Identifier"},"name":{"type":"string"},"loc":{"$ref":"#/definitions/Loc"}}},
    "ArrayLiteral": {"type":"object","required":["type","elements","loc"],"properties":{"type":{"const":"ArrayLiteral"},"elements":{"type":"array","items":{"$ref":"#/definitions/Value"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "ObjectLiteral": {"type":"object","required":["type","properties","loc"],"properties":{"type":{"const":"ObjectLiteral"},"properties":{"type":"array","items":{"$ref":"#/definitions/KV"}},"loc":{"$ref":"#/definitions/Loc"}}}
}
}
```
## 1.3 Kategoryzacja atrybutĂłw (lint)
- **GEOMETRY:** `x,y,width,height,anchors,margin,padding,min-width,max-width,min-height,max-height`
- **STYLE:** `font,color,image,style,opacity,icon,background,spacing`
- **BEHAVIOR:** `id,focusable,draggable,enabled,visible,onClick,onText,tooltip`
> Lista jest rozszerzalna per projekt (`otui-rules.json`).
## 1.4 PrzykÄąâ€šad AST (OTUI)
WejÄąâ€şcie:
`$fenceInfo
MainWindow < UIWidget {
  id: main
  width: 300
  text: "Hello"
}
```
Szkic wyjÄąâ€şcia (skrĂłcony):
`$fenceInfo
{
  "type":"OTUIFile","loc":{"file":"/p/ui/main.otui","start":{"offset":0,"line":1,"column":1},"end":{"offset":55,"line":5,"column":2}},
  "errors":[],
  "body":[
    {"type":"Decl","name":"MainWindow","base":"UIWidget","loc":{...},"body":[
      {"type":"KV","key":"id","category":"BEHAVIOR","value":{"type":"Identifier","name":"main","loc":{...}},"loc":{...}},
      {"type":"KV","key":"width","category":"GEOMETRY","value":{"type":"NumberLiteral","value":300,"loc":{...}},"loc":{...}},
      {"type":"KV","key":"text","category":"STYLE","value":{"type":"StringLiteral","value":"Hello","loc":{...}},"loc":{...}}
]}
]
}
```

---
## 2) LuaĂ˘â‚¬â€Lite â€” AST i zakres parsera
> Celem jest lekki AST do potrzeb IDE (symbole, funkcje, wywoÄąâ€šania, literaÄąâ€šy, tabele). Nie jest to peÄąâ€šna interpretacja Lua.
## 2.1 Zakres tokenĂłw/wÄ™zÄąâ€šĂłw
- **WÄ™zÄąâ€šy:** `Chunk, LocalStatement, Assignment, FunctionDecl, CallStatement, CallExpr, Identifier, StringLiteral, NumberLiteral, BooleanLiteral, NilLiteral, TableConstructor, TableField, ReturnStatement, IfStatement (nagÄąâ€šĂłwki), DoBlock (prosty)`.
- **Pomijane:** zÄąâ€šoÄąÄ˝one metatablice, goto/label (oznacz jako `UnknownNode`).
## 2.2 LuaĂ˘â‚¬â€Lite AST â€” JSON Schema
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/lua-lite-ast.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Lua-Lite AST",
  "type": "object",
  "required": ["type","loc","body"],
  "properties": {
    "type": {"const": "Chunk"},
    "loc": {"$ref": "#/definitions/Loc"},
    "errors": {"type":"array","items":{"$ref":"#/definitions/ParseError"}},
    "body": {"type":"array","items":{"$ref":"#/definitions/Stmt"}}
},
  "definitions": {
    "Loc": {"type":"object","required":["file","start","end"],"properties":{"file":{"type":"string"},"start":{"$ref":"#/definitions/Pos"},"end":{"$ref":"#/definitions/Pos"}}},
    "Pos": {"type":"object","required":["offset","line","column"],"properties":{"offset":{"type":"integer","minimum":0},"line":{"type":"integer","minimum":1},"column":{"type":"integer","minimum":1}}},
    "ParseError": {"type":"object","required":["code","message","loc"],"properties":{"code":{"type":"string"},"message":{"type":"string"},"loc":{"$ref":"#/definitions/Loc"}}},

    "Stmt": {"oneOf":[
      {"$ref":"#/definitions/LocalStatement"},
      {"$ref":"#/definitions/Assignment"},
      {"$ref":"#/definitions/FunctionDecl"},
      {"$ref":"#/definitions/CallStatement"},
      {"$ref":"#/definitions/ReturnStatement"},
      {"$ref":"#/definitions/IfStatement"},
      {"$ref":"#/definitions/DoBlock"}
    ]},

    "Expr": {"oneOf":[
      {"$ref":"#/definitions/Identifier"},
      {"$ref":"#/definitions/StringLiteral"},
      {"$ref":"#/definitions/NumberLiteral"},
      {"$ref":"#/definitions/BooleanLiteral"},
      {"$ref":"#/definitions/NilLiteral"},
      {"$ref":"#/definitions/CallExpr"},
      {"$ref":"#/definitions/TableConstructor"}
    ]},

    "Identifier": {"type":"object","required":["type","name","loc"],"properties":{"type":{"const":"Identifier"},"name":{"type":"string"},"loc":{"$ref":"#/definitions/Loc"}}},
    "StringLiteral": {"type":"object","required":["type","value","loc"],"properties":{"type":{"const":"StringLiteral"},"value":{"type":"string"},"loc":{"$ref":"#/definitions/Loc"}}},
    "NumberLiteral": {"type":"object","required":["type","value","loc"],"properties":{"type":{"const":"NumberLiteral"},"value":{"type":"number"},"loc":{"$ref":"#/definitions/Loc"}}},
    "BooleanLiteral": {"type":"object","required":["type","value","loc"],"properties":{"type":{"const":"BooleanLiteral"},"value":{"type":"boolean"},"loc":{"$ref":"#/definitions/Loc"}}},
    "NilLiteral": {"type":"object","required":["type","loc"],"properties":{"type":{"const":"NilLiteral"},"loc":{"$ref":"#/definitions/Loc"}}},

    "LocalStatement": {"type":"object","required":["type","names","values","loc"],"properties":{"type":{"const":"LocalStatement"},"names":{"type":"array","items":{"$ref":"#/definitions/Identifier"}},"values":{"type":"array","items":{"$ref":"#/definitions/Expr"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "Assignment": {"type":"object","required":["type","targets","values","loc"],"properties":{"type":{"const":"Assignment"},"targets":{"type":"array","items":{"$ref":"#/definitions/Expr"}},"values":{"type":"array","items":{"$ref":"#/definitions/Expr"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "FunctionDecl": {"type":"object","required":["type","name","params","body","loc"],"properties":{"type":{"const":"FunctionDecl"},"name":{"$ref":"#/definitions/Expr"},"params":{"type":"array","items":{"$ref":"#/definitions/Identifier"}},"body":{"type":"array","items":{"$ref":"#/definitions/Stmt"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "CallStatement": {"type":"object","required":["type","expression","loc"],"properties":{"type":{"const":"CallStatement"},"expression":{"$ref":"#/definitions/CallExpr"},"loc":{"$ref":"#/definitions/Loc"}}},
    "CallExpr": {"type":"object","required":["type","callee","args","method","loc"],"properties":{"type":{"const":"CallExpr"},"callee":{"$ref":"#/definitions/Expr"},"args":{"type":"array","items":{"$ref":"#/definitions/Expr"}},"method":{"type":["string","null"]},"loc":{"$ref":"#/definitions/Loc"}}},
    "TableConstructor": {"type":"object","required":["type","fields","loc"],"properties":{"type":{"const":"TableConstructor"},"fields":{"type":"array","items":{"$ref":"#/definitions/TableField"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "TableField": {"type":"object","required":["type","key","value","loc"],"properties":{"type":{"const":"TableField"},"key":{"oneOf":[{"$ref":"#/definitions/Identifier"},{"$ref":"#/definitions/StringLiteral"},{"$ref":"#/definitions/NumberLiteral"},{"type":"null"}]},"value":{"$ref":"#/definitions/Expr"},"loc":{"$ref":"#/definitions/Loc"}}},
    "ReturnStatement": {"type":"object","required":["type","arguments","loc"],"properties":{"type":{"const":"ReturnStatement"},"arguments":{"type":"array","items":{"$ref":"#/definitions/Expr"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "IfStatement": {"type":"object","required":["type","clauses","loc"],"properties":{"type":{"const":"IfStatement"},"clauses":{"type":"array","items":{"$ref":"#/definitions/IfClause"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "IfClause": {"type":"object","required":["type","test","consequent","loc"],"properties":{"type":{"const":"IfClause"},"test":{"$ref":"#/definitions/Expr"},"consequent":{"type":"array","items":{"$ref":"#/definitions/Stmt"}},"loc":{"$ref":"#/definitions/Loc"}}},
    "DoBlock": {"type":"object","required":["type","body","loc"],"properties":{"type":{"const":"DoBlock"},"body":{"type":"array","items":{"$ref":"#/definitions/Stmt"}},"loc":{"$ref":"#/definitions/Loc"}}}
}
}
```
## 2.3 Mapowanie zdarzeÄąâ€ž/symboli istotnych dla OTClient/vBot
- Wykrywanie `g_ui.loadUI("Ă˘â‚¬Â¦")` Ă˘â€ â€™ relacja `lua_to_otui`.
- Wykrywanie `dofile("Ă˘â‚¬Â¦")`/`require("Ă˘â‚¬Â¦")` Ă˘â€ â€™ relacja `includes`.
- Heurystyki vBot: identyfikuj wywoÄąâ€šania `macro(`, callbacki `onTextMessage`, `onCreatureHealth`, itp. Ă˘â€ â€™ taguj w indeksie jako `botSymbols`.

---
## 3) Kontrakty walidacji artefaktĂłw (JSON Schema)
## 3.1 `resources/api.json`
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/api.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "API Catalogue",
  "type": "object",
  "required": ["$schemaVersion","functions","events","objects"],
  "properties": {
    "$schemaVersion": {"type":"integer","minimum":1},
    "generatedAt": {"type":"string","format":"date-time"},
    "functions": {
      "type":"array",
      "uniqueItems": true,
      "items": {
        "type":"object",
        "required":["name","module","params","returns","description"],
        "properties": {
          "name": {"type":"string","pattern":"^[A-Za-z_][A-Za-z0-9_\.:]*$"},
          "module": {"type":"string"},
          "params": {"type":"array","items":{"type":"object","required":["name","type"],"properties":{"name":{"type":"string"},"type":{"type":"string"},"optional":{"type":"boolean"}}}},
          "returns": {"type":"array","items":{"type":"object","required":["type"],"properties":{"type":{"type":"string"}}}},
          "description": {"type":"string"},
          "examples": {"type":"array","items":{"type":"string"}},
          "since": {"type":"string"},
          "deprecated": {"type":"boolean"}
}
}
},
    "events": {"type":"array","items":{"type":"object","required":["name","target","payload"],"properties":{"name":{"type":"string"},"target":{"type":"string"},"payload":{"type":"array","items":{"type":"object","required":["name","type"],"properties":{"name":{"type":"string"},"type":{"type":"string"}}}},"description":{"type":"string"}}}},
    "objects": {"type":"array","items":{"type":"object","required":["name","description"],"properties":{"name":{"type":"string"},"members":{"type":"array","items":{"oneOf":[{"type":"string"},{"type":"object"}]}},"description":{"type":"string"}}}}
}
}
```
## 3.2 `project-index.json`
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/project-index.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Project Index",
  "type": "object",
  "required": ["$schemaVersion","root","files","symbols","relations"],
  "properties": {
    "$schemaVersion": {"type":"integer","minimum":1},
    "root": {"type":"string"},
    "files": {"type":"object","required":["lua","otui","otmod"],"properties":{"lua":{"type":"array","items":{"type":"string"}},"otui":{"type":"array","items":{"type":"string"}},"otmod":{"type":"array","items":{"type":"string"}}}},
    "symbols": {"type":"object","properties":{"functions":{"type":"object","additionalProperties":{"type":"array","items":{"type":"string"}}},"widgets":{"type":"object","additionalProperties":{"type":"array","items":{"type":"string"}}},"botSymbols":{"type":"object","additionalProperties":{"type":"array","items":{"type":"string"}}}}},
    "relations": {"type":"object","properties":{"lua_to_otui":{"type":"array","items":{"type":"object","required":["lua","otui","via"],"properties":{"lua":{"type":"string"},"otui":{"type":"string"},"via":{"type":"string"}}}},"includes":{"type":"array","items":{"type":"object","required":["from","to","via"],"properties":{"from":{"type":"string"},"to":{"type":"string"},"via":{"type":"string"}}}}}}
}
}
```
## 3.3 `otui-rules.json`
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/otui-rules.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "OTUI Lint Rules",
  "type": "object",
  "required": ["$schemaVersion","rules"],
  "properties": {
    "$schemaVersion": {"type":"integer","minimum":1},
    "rules": {"type":"array","items":{"type":"object","required":["id","description","fixable"],"properties":{"id":{"type":"string"},"description":{"type":"string"},"fixable":{"type":"boolean"}}}}
}
}
```
## 3.4 `templates.json`
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/templates.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Generator Templates",
  "type": "object",
  "required": ["$schemaVersion"],
  "properties": {
    "$schemaVersion": {"type":"integer","minimum":1}
},
  "additionalProperties": {
    "type": "object",
    "required": ["title","files","checklist"],
    "properties": {
      "title": {"type":"string"},
      "files": {"type":"array","items":{"type":"object","required":["path","contents"],"properties":{"path":{"type":"string"},"contents":{"type":"string"}}}},
      "checklist": {"type":"array","items":{"type":"string"}}
}
}
}
```
## 3.5 `docstrings.json`
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/docstrings.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Docstrings Index",
  "type": "object",
  "required": ["$schemaVersion","entries"],
  "properties": {
    "$schemaVersion": {"type":"integer","minimum":1},
    "entries": {"type":"array","items":{"type":"object","required":["file","line","symbol"],"properties":{"file":{"type":"string"},"line":{"type":"integer","minimum":1},"symbol":{"type":"string"},"params":{"type":"array","items":{"type":"object","required":["name","type"],"properties":{"name":{"type":"string"},"type":{"type":"string"}}}},"returns":{"type":"array","items":{"type":"object","required":["type"],"properties":{"type":{"type":"string"}}}},"comment":{"type":"string"}}}}
}
}
```
## 3.6 `assets-map.json`
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/assets-map.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Assets Map",
  "type": "object",
  "required": ["$schemaVersion","assets"],
  "properties": {
    "$schemaVersion": {"type":"integer","minimum":1},
    "assets": {"type":"object","properties":{"images":{"type":"array","items":{"type":"string"}},"fonts":{"type":"array","items":{"type":"string"}},"styles":{"type":"array","items":{"type":"string"}}}}
}
}
```
## 3.7 `.studio/config.json`
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/studio-config.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Studio Config",
  "type": "object",
  "required": ["$schemaVersion","projectRoot","apiPath","otuiRulesPath","templatesPath","logPath","ignore"],
  "properties": {
    "$schemaVersion": {"type":"integer","minimum":1},
    "projectRoot": {"type":"string"},
    "apiPath": {"type":"string"},
    "otuiRulesPath": {"type":"string"},
    "templatesPath": {"type":"string"},
    "logPath": {"type":"string"},
    "ignore": {"type":"array","items":{"type":"string"}}
}
}
```
## 3.8 `ndjson` (schemat pojedynczej linii logu)
`$fenceInfo
{
  "$id": "https://schemas.otc.studio/log-line.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Log Line (NDJSON)",
  "type": "object",
  "required": ["ts","level","msg"],
  "properties": {
    "ts": {"type":"string","format":"date-time"},
    "level": {"type":"string","enum":["DEBUG","INFO","WARN","ERROR"]},
    "tag": {"type":["string","null"]},
    "file": {"type":["string","null"]},
    "line": {"type":["integer","null"],"minimum":1},
    "msg": {"type":"string"},
    "meta": {"type":["object","array","string","number","boolean","null"]}
}
}
```

---
## 4) Kontrakty IPC (Parser Service)
**KanaÄąâ€šy:**
- `parser:otui:parse` Ă˘â€ â€™ req: `{path | content}` Ă˘â€ â€™ res: `OTUIFile` (AST) + `errors[]`.
- `parser:lua:parse` Ă˘â€ â€™ req: `{path | content}` Ă˘â€ â€™ res: `Chunk` (AST) + `errors[]`.
- `parser:scan:index` Ă˘â€ â€™ req: `{root}` Ă˘â€ â€™ res: `project-index.json`.
- `parser:docstrings` Ă˘â€ â€™ req: `{files[]}` Ă˘â€ â€™ res: `docstrings.json`.

**BÄąâ€šÄ™dy:** `{code,msg,loc?}`; kody wg Â§7.

---
## 5) ReguÄąâ€šy walidacji i jakoÄąâ€şci
- **JSON Schema gates:** kaÄąÄ˝da emisja `*.json` walidowana przed zapisem; bÄąâ€šÄ…d = rollback.
- **Stabilne sortowanie:** listy sortuj po `loc.start.offset` lub alfabetycznie (klucze obiektĂłw alfabetycznie).
- **Backupy:** przy autoĂ˘â‚¬â€fix zapisz `*.bak` + diff.
- **Hash indeksu:** `sha1(size+mtime)` dla cache inkrementalnego.

---
## 6) Test vectors (prĂłbki wejÄąâ€şcia/wyjÄąâ€şcia)
## 6.1 OTUI proste
WejÄąâ€şcie `main.otui`:
`$fenceInfo
Window < UIWidget {
  id: root
  width: 320
  text: "Title"
}
```
Oczekiwany AST: zgodny ze schematem Â§1.2 (sprawdÄąĹź kategorie: idĂ˘â€ â€™BEHAVIOR, widthĂ˘â€ â€™GEOMETRY, textĂ˘â€ â€™STYLE).
## 6.2 LuaĂ˘â‚¬â€Lite â€” symbole
WejÄąâ€şcie `client.lua`:
`$fenceInfo
local M = {}
function M.reload()
  g_modules.reloadModules()
end
M.init = function()
  g_ui.loadUI('ui/main.otui')
end
return M
```
Oczekiwane relacje: `lua_to_otui[0].otui == 'ui/main.otui'`; wykryta funkcja `M.reload` + wywoÄąâ€šanie `g_modules.reloadModules`.
## 6.3 `api.json` â€“ walidacja
Ziarno z dokumentu MASTER musi przejÄąâ€şÄ‡ `api.schema.json`; nazwy funkcji zgodne z regex.

---
## 7) Kody bÄąâ€šÄ™dĂłw i odzyskiwanie
- **LUA_001**: nieoczekiwany token Ă˘â€ â€™ pomiÄąâ€ž do `;`/koÄąâ€žca linii/bloku.
- **LUA_101**: niezamkniÄ™ta lista argumentĂłw Ă˘â€ â€™ zamknij heurystycznie przy `)` najbliÄąÄ˝szym.
- **OTUI_001**: niezamkniÄ™ty blok `{` Ă˘â€ â€™ domknij na koÄąâ€žcu pliku, dodaj ParseError.
- **OTUI_101**: niepoprawny literaÄąâ€š Ă˘â€ â€™ potraktuj jako `Identifier` i zarejestruj bÄąâ€šÄ…d.
- **OTMOD_001**: brak `name` Ă˘â€ â€™ bÄąâ€šÄ…d twardy (blokuj generator).
- **GEN_500**: bÄąâ€šÄ…d I/O Ă˘â€ â€™ sprĂłbuj ponownie raz, potem fail.

---
## 8) WydajnoÄąâ€şÄ‡ i limity
- AST do 2 MB pliku w < 200 ms (cel); duÄąÄ˝e pliki: tryb â€žbig-fileâ€ť (bez czÄ™Äąâ€şci analiz).
- Indeks projektu 5k plikĂłw: < 5 s z cache, < 30 s zimny start.
- ZuÄąÄ˝ycie pamiÄ™ci: < 500 MB dla indeksu 5k plikĂłw.

---
## 9) Checklisty wdroÄąÄ˝eniowe (dla tej warstwy)
- [ ] Zaimplementowane parsery (OTUI, LuaĂ˘â‚¬â€Lite) zgodnie z Â§1 i Â§2.
- [ ] Emisja AST z `loc`, `errors`, deterministycznym sortem.
- [ ] JSON Schemy z Â§3 wÄąâ€šÄ…czone w walidacjÄ™ przed zapisem.
- [ ] IPC z Â§4 â€“ kontrakty pokryte testami kontraktowymi.
- [ ] Test vectors z Â§6 â€“ zielone snapshoty AST i indeksĂłw.
- [ ] Pomiar czasu/zuÄąÄ˝ycia pamiÄ™ci â€“ w normie Â§8.

---
## 10) Noty
- ReguÄąâ€ša `tr()` dla statycznych tekstĂłw w OTUI bywa zaleÄąÄ˝na od bazy â€“ przewidziana jako **opcja** w `otui-rules.json`.
- Schematy wykorzystujÄ… Draft 2020Ă˘â‚¬â€12; moÄąÄ˝liwa migracja wstecz do DraftĂ˘â‚¬â€07 (wymaga drobnych zmian sÄąâ€šownikĂłw).


