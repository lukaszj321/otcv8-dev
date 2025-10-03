#!/usr/bin/env node
/**
 * OTCv8 API extractor -> docs/api/otcv8-full-api.md
 * Zbiera:
 * - Lua: eventy (onXxx), funkcje modułów (M.*), użycia ctx.*, globalne funkcje
 * - OTUI: id + typy i wspierane pola (heurystyka)
 * - WS: typy wiadomości z JSON/TS/JS (klucze "type": "..."), schematy *.schema.json
 * - C++: nagłówki (public API) – prototypy z include/**/*.h, *.hpp
 *
 * Użycie: node scripts/extract-api.mjs
 */
import fs from "fs";
import fsp from "fs/promises";
import path from "path";
import { glob } from "glob";

const ROOT = process.cwd();
const OUT = path.join(ROOT, "docs/api/otcv8-full-api.md");

// Helpers
const read = async (p) => {
  try { return await fsp.readFile(p, "utf8"); } catch { return ""; }
};
const uniq = (arr) => [...new Set(arr)].sort();
const add = (map, key, item) => { if (!map[key]) map[key] = new Set(); map[key].add(item); };

// ---------- 1) LUA ----------
const luaFiles = await glob([
  "init.lua",
  "test.lua",
  "modules/**/*.lua",
  "src/**/*.lua"
], { dot: false, nodir: true });

let lua = {
  events: new Set(),        // onTalk, onCreatureAppear, ...
  globals: new Set(),       // say, useItem, etc. (heur.)
  ctxCalls: {},             // ctx.method -> samples
  modules: {}               // module file -> exported funcs (M.start, M.stop, ...)
};

const reEvent = /\bon([A-Z][A-Za-z0-9_]*)\s*\(/g;                // onTalk( ...
const reGlobalFnCall = /\b([a-z][a-z0-9_]{2,})\s*\(/g;           // say( cast( ...
const reCtx = /\bctx\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g;           // ctx.emit(
const reModuleExport = /\bM\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*function\b/g; // M.start = function
const reFuncDef = /\bfunction\s+([a-zA-Z_\.][a-zA-Z0-9_\.]*)\s*\(/g;      // function say( / function M.start(

for (const f of luaFiles) {
  const t = await read(f);
  if (!t) continue;
  // events
  for (const m of t.matchAll(reEvent)) lua.events.add(m[1]);
  // ctx
  for (const m of t.matchAll(reCtx)) add(lua.ctxCalls, m[1], `${path.basename(f)}:${m.index}`);
  // module exports
  const ex = new Set();
  for (const m of t.matchAll(reModuleExport)) ex.add(m[1]);
  // also catch "function M.start(" style
  for (const m of t.matchAll(reFuncDef)) {
    if (m[1].startsWith("M.")) ex.add(m[1].slice(2));
    else lua.globals.add(m[1].split(".")[0]);
  }
  if (ex.size) lua.modules[f] = ex;
  // globals heuristics: use of say(), on map reduce noise
  for (const m of t.matchAll(reGlobalFnCall)) {
    const name = m[1];
    if (["if","for","and","end","then","else","not","nil","true","false","local","return","function","print"].includes(name)) continue;
    if (name.length < 3) continue;
    // ignore ctx.* captured elsewhere
    if (name === "ctx") continue;
    lua.globals.add(name);
  }
}
lua.events = uniq([...lua.events]).map(e => "on" + e); // restore full names
const ctxList = Object.keys(lua.ctxCalls).sort();

// ---------- 2) OTUI ----------
const otuiFiles = await glob(["layouts/**/*.otui", "layouts/**/*.otml", "layouts/**/*.txt"], { nodir: true });
const ui = [];
const reId = /^\s*(Panel|Label|Button|ProgressBar|ListView|Widget|TextEdit|CheckBox|ScrollArea|Window|Image|Item|.*)\s*[\r\n]+(?:\s+id:\s*([A-Za-z0-9_\-]+))?/m;
for (const f of otuiFiles) {
  const t = await read(f);
  if (!t) continue;
  // bruteforce: split blocks by blank line, capture first word (type) and "id:" line
  const blocks = t.split(/\n\s*\n/);
  for (const b of blocks) {
    const m = b.match(/^\s*([A-Za-z][A-Za-z0-9]*)[\s\S]*?\bid:\s*([A-Za-z0-9_\-]+)/m);
    if (m) ui.push({ file: f, type: m[1], id: m[2] });
  }
}

// ---------- 3) WebSocket ----------
const ws = {
  types: new Set(), // all "type": "..."
  schemas: {}       // schema id -> filename
};
const textFiles = await glob(["**/*.{json,js,ts,tsx}", "!node_modules/**", "!site/**"], { nodir: true });
for (const f of textFiles) {
  const t = await read(f);
  if (!t) continue;
  // JSON/TS literals:  "type": "something"
  const reType = /["']type["']\s*:\s*["']([a-zA-Z0-9\.\-_]+)["']/g;
  for (const m of t.matchAll(reType)) ws.types.add(m[1]);
  // JSON schemas
  const mId = t.match(/"\$id"\s*:\s*"(.*?)"/);
  if (mId && (f.endsWith(".schema.json") || f.includes("/schemas/"))) {
    ws.schemas[mId[1]] = f;
  }
}
const wsTypes = uniq([...ws.types]);

// ---------- 4) C++ headers ----------
const hFiles = await glob(["include/**/*.{h,hpp}", "src/**/*.{h,hpp}"], { nodir: true });
const cpp = [];
const reProto = /^\s*(?:OTC|OT|namespace\s+[A-Za-z_][A-Za-z0-9_]*)?[\s\S]*?\b([A-Za-z_][A-Za-z0-9_:<>*&\s]+)\s+([A-Za-z_][A-Za-z0-9_:<>*&]*)\s*\(([^)]*)\)\s*;/gm;
for (const f of hFiles) {
  const t = await read(f);
  if (!t) continue;
  // heurystycznie zbierz publiczne prototypy
  for (const m of t.matchAll(reProto)) {
    const sig = `${m[1].trim()} ${m[2]}(${m[3].trim()})`;
    if (sig.length < 8 || sig.includes("operator")) continue;
    cpp.push({ file: f, sig });
  }
}

// ---------- Render MD ----------
const lines = [];
const push = (s="") => lines.push(s);

push("# OTCv8 – Pełne API (auto)");
push("");
push(`Wygenerowano: ${new Date().toISOString()}`);
push("");
push("---");
push("");
push("## 1. Lua – eventy i moduły");
push("");
push("### 1.1. Zdarzenia (znalezione `on*`):");
if (lua.events.length) {
  for (const e of lua.events) push(`- \`${e}(...)\``);
} else push("_brak dopasowań_");
push("");
push("### 1.2. Wywołania `ctx.*` (API kontekstu):");
if (ctxList.length) {
  for (const m of ctxList) push(`- \`ctx.${m}(...)\``);
} else push("_brak dopasowań_");
push("");
push("### 1.3. Eksporty modułów (M.*):");
const modFiles = Object.keys(lua.modules).sort();
if (modFiles.length) {
  for (const f of modFiles) {
    push(`- **${f}**: ${[...lua.modules[f]].map(x=>"`M."+x+"()`").join(", ")}`);
  }
} else push("_brak modułów z eksportami_");
push("");
push("### 1.4. Globalne funkcje Lua (heurystyka):");
const globals = uniq([...lua.globals]).filter(n => !n.startsWith("on"));
if (globals.length) push(globals.map(n=>"- `"+n+"()`").join("\n")); else push("_brak_");

push("");
push("---");
push("");
push("## 2. OTUI – komponenty i ID");
if (ui.length) {
  const byFile = {};
  ui.forEach(x => add(byFile, x.file, `- \`${x.id}\` : **${x.type}**`));
  for (const f of Object.keys(byFile).sort()) {
    push(`### ${f}`);
    push([...byFile[f]].sort().join("\n"));
    push("");
  }
} else {
  push("_brak plików layoutów w layouts/**_");
}

push("");
push("---");
push("");
push("## 3. WebSocket – typy i schematy");
push("### 3.1. Typy wiadomości (wykryte po kluczu `type`):");
if (wsTypes.length) push(wsTypes.map(t=>"- `"+t+"`").join("\n")); else push("_brak_");
push("");
push("### 3.2. Schematy JSON:");
const schemaIds = Object.keys(ws.schemas).sort();
if (schemaIds.length) {
  for (const id of schemaIds) push(`- \`${id}\` → \`${ws.schemas[id]}\``);
} else push("_brak_");

push("");
push("---");
push("");
push("## 4. C++ – prototypy (nagłówki)");
if (cpp.length) {
  for (const it of cpp.slice(0, 500)) push(`- **${it.file}**: \`${it.sig}\``);
  if (cpp.length > 500) push(`_… ${cpp.length-500} dalszych_`);
} else push("_brak_");

push("");
push("---");
push("");
push("## 5. Uwagi");
push("- Ten plik jest generowany — **nie edytuj ręcznie**.");
push("- Rozszerz wzorce w `scripts/extract-api.mjs`, aby doprecyzować API (np. pełne sygnatury eventów).");
push("");

await fsp.mkdir(path.dirname(OUT), { recursive: true });
await fsp.writeFile(OUT, lines.join("\n"), "utf8");
console.log("OK ->", OUT);
