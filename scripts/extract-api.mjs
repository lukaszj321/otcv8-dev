#!/usr/bin/env node
/**
 * OTCv8 - pełny AUTO-extract API z repo → docs/api/otcv8-full-api.md
 * Zbiera:
 *  - Lua: eventy on*, globalne funkcje, moduły (M.*), ctx.* (+ LDoc/EmmyLua)
 *  - OTUI: ID + typy
 *  - WS: typy (po "type": "...") + JSON Schema (*.schema.json)
 *  - C++: publiczne prototypy + Doxygen @brief
 */
import fs from "fs/promises";
import path from "path";
import { glob } from "glob";

const OUT = "docs/api/otcv8-full-api.md";
const read = async f => { try { return await fs.readFile(f, "utf8"); } catch { return ""; } };
const uniq = a => [...new Set(a)].sort();
const ensureDir = p => fs.mkdir(path.dirname(p), { recursive: true });

/* ---------- 1) LUA ---------- */
const luaFiles = await glob([
  "**/*.lua",
  "!**/node_modules/**",
  "!**/site/**"
], { nodir: true });

const lua = {
  events: new Set(),
  globals: new Set(),
  ctx: new Map(),          // name -> samples
  modules: new Map(),      // file -> Set(exported)
  docs: new Map()          // symbol -> doc string (LDoc/EmmyLua)
};

// EmmyLua / LDoc
const reEmmy = /---[ \t]*@([a-zA-Z]+)\s+([\s\S]*?)\n(?![-]{3})/g;
const reLdocFn = /---[\s\S]*?\nfunction\s+([A-Za-z0-9_.:]+)\s*\(/g;

for (const f of luaFiles) {
  const t = await read(f);
  if (!t) continue;

  // onXxx(  -> eventy
  for (const m of t.matchAll(/\bon([A-Z][A-Za-z0-9_]*)\s*\(/g)) lua.events.add("on" + m[1]);

  // ctx.*(
  for (const m of t.matchAll(/\bctx\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g)) {
    const k = m[1];
    const a = lua.ctx.get(k) || new Set();
    a.add(`${path.basename(f)}:${m.index}`);
    lua.ctx.set(k, a);
  }

  // M.* =
  const ex = new Set();
  for (const m of t.matchAll(/\bM\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*function\b/g)) ex.add(m[1]);
  for (const m of t.matchAll(/\bfunction\s+M\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g)) ex.add(m[1]);
  if (ex.size) lua.modules.set(f, ex);

  // globalne fn (heur.)
  for (const m of t.matchAll(/\b([a-z][a-z0-9_]{2,})\s*\(/g)) {
    const name = m[1];
    if (["if","for","and","end","then","else","not","nil","true","false","local","return","function","print","ctx"].includes(name)) continue;
    if (!name.startsWith("on")) lua.globals.add(name);
  }

  // Emmy/LDoc
  for (const m of t.matchAll(/---[^\n]*\n(?:---.*\n)*\s*function\s+([A-Za-z0-9_.:]+)\s*\(([^)]*)\)/g)) {
    const sig = m[1];
    const before = t.slice(0, m.index);
    const doc = (before.match(/(---.*\n)+$/m) || [""])[0].replace(/^--- ?/gm,"").trim();
    if (doc) lua.docs.set(sig, doc);
  }
}

/* ---------- 2) OTUI ---------- */
const uiFiles = await glob([
  "layouts/**/*.{otui,otml,txt}",
], { nodir: true });

const ui = [];
for (const f of uiFiles) {
  const t = await read(f);
  if (!t) continue;
  // proste bloki: pierwszy token = typ, linia "id: <id>"
  const blocks = t.split(/\n\s*\n/);
  for (const b of blocks) {
    const m = b.match(/^\s*([A-Za-z][A-Za-z0-9]*)[\s\S]*?\bid:\s*([A-Za-z0-9_\-]+)/m);
    if (m) ui.push({ file: f, type: m[1], id: m[2] });
  }
}

/* ---------- 3) WS ---------- */
const txtFiles = await glob([
  "**/*.{json,js,ts,tsx}",
  "!**/node_modules/**",
  "!**/site/**"
], { nodir: true });

const wsTypes = new Set();
const wsSchemas = new Map();
for (const f of txtFiles) {
  const t = await read(f);
  if (!t) continue;
  for (const m of t.matchAll(/["']type["']\s*:\s*["']([a-zA-Z0-9._-]+)["']/g)) wsTypes.add(m[1]);
  const id = t.match(/"\$id"\s*:\s*"(.*?)"/);
  if (id && f.endsWith(".json")) wsSchemas.set(id[1], f);
}

/* ---------- 4) C++ ---------- */
const hFiles = await glob([
  "include/**/*.{h,hpp}",
  "src/**/*.{h,hpp}"
], { nodir: true });

const cpp = [];
for (const f of hFiles) {
  const t = await read(f);
  if (!t) continue;
  // Doxygen @brief (poprzedzający komentarz)
  const lines = t.split("\n");
  for (let i=0;i<lines.length;i++) {
    const L = lines[i];
    const m = L.match(/^\s*([A-Za-z_][A-Za-z0-9_:<>*&\s]+)\s+([A-Za-z_][A-Za-z0-9_:<>*&]*)\s*\(([^)]*)\)\s*;/);
    if (m && !m[2].startsWith("operator")) {
      // szukaj brief powyżej
      let brief = "";
      for (let j=i-1;j>=0 && j>i-10;j--){
        const b = lines[j].trim();
        if (/^\*|\/\*\*|\/\/\//.test(b)) brief = (b.replace(/^\/\*\*?|\*+\/|^\* ?|^\/\/\/ ?/g,"") + "\n" + brief).trim();
        else if (b==="") continue; else break;
      }
      cpp.push({ file: f, sig: `${m[1].trim()} ${m[2]}(${m[3].trim()})`, brief });
    }
  }
}

/* ---------- RENDER ---------- */
const out = [];
const p = s => out.push(s);

p("# OTCv8 – Pełne API (auto)");
p("");
p(`Wygenerowano: ${new Date().toISOString()}`);
p("");
p("> Ten plik jest generowany automatycznie z kodu. Nie edytuj ręcznie.");
p("");
p("---");
p("");
p("## 1. Lua");
p("");
p("### 1.1. Zdarzenia (on*)");
const ev = uniq([...lua.events]);
p(ev.length ? ev.map(x=>`- \`${x}(...)\``).join("\n") : "_brak_");
p("");
p("### 1.2. Kontekst `ctx.*`");
const ctxNames = uniq([...lua.ctx.keys()]);
p(ctxNames.length ? ctxNames.map(x=>`- \`ctx.${x}(...)\``).join("\n") : "_brak_");
p("");
p("### 1.3. Moduły (eksporty `M.*`)");
const mods = [...lua.modules.entries()].sort((a,b)=>a[0].localeCompare(b[0]));
if (mods.length) {
  for (const [file, set] of mods) p(`- **${file}**: ${[...set].map(s=>"`M."+s+"()`").join(", ")}`);
} else p("_brak_");
p("");
p("### 1.4. Globalne funkcje (heur.)");
const gfn = uniq([...lua.globals]).filter(n=>!n.startsWith("on"));
p(gfn.length ? gfn.map(n=>"- `"+n+"()`").join("\n") : "_brak_");
p("");
if (lua.docs.size) {
  p("### 1.5. Komentarze LDoc/EmmyLua (wyciąg)");
  for (const [sym, doc] of [...lua.docs.entries()].slice(0,200)) {
    p(`- \`${sym}()\` — ${doc.replace(/\n+/g," ").slice(0,200)}${doc.length>200?"…":""}`);
  }
  p("");
}
p("---");
p("");
p("## 2. OTUI (layouty)");
if (ui.length) {
  const by = {};
  for (const it of ui) (by[it.file] ??= []).push(it);
  for (const f of Object.keys(by).sort()) {
    p(`### ${f}`);
    p(by[f].map(x=>`- \`${x.id}\` — **${x.type}**`).join("\n"));
    p("");
  }
} else p("_brak plików layouts/_");
p("");
p("---");
p("");
p("## 3. WebSocket");
p("### 3.1. Typy wiadomości (wykryte)");
const types = uniq([...wsTypes]);
p(types.length ? types.map(t=>"- `"+t+"`").join("\n") : "_brak_");
p("");
p("### 3.2. Schematy JSON (\\$id → plik)");
const schemas = [...wsSchemas.entries()].sort((a,b)=>a[0].localeCompare(b[0]));
p(schemas.length ? schemas.map(([id,f])=>`- \`${id}\` → \`${f}\``).join("\n") : "_brak_");
p("");
p("---");
p("");
p("## 4. C++ (nagłówki)");
if (cpp.length) {
  for (const it of cpp.slice(0,800)) {
    p(`- **${it.file}**: \`${it.sig}\`${it.brief?` — ${it.brief}`:""}`);
  }
  if (cpp.length>800) p(`_… ${cpp.length-800} dalszych_`);
} else p("_brak_");
p("");
p("---");
p("");
p("## 5. Uwaga");
p("- Jeśli czegoś brakuje: dodaj wzorce do `scripts/extract-api.mjs`.");
p("- Możesz też dorzucić schematy do `schemas/ws/*.schema.json`, będą automatycznie zlinkowane.");
p("");

await ensureDir(OUT);
await fs.writeFile(OUT, out.join("\n"), "utf8");
console.log("OK ->", OUT);
