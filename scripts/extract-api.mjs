#!/usr/bin/env node
/**
 * OTCv8 – AUTO pełne API z repo → docs/api/otcv8-full-api.md (+ schemas, manifest)
 * Rozszerzenia:
 *  - pełne listy (bez obcinania)
 *  - MyST: {contents}, H2/H3/H4, kotwice
 *  - JSON Schema => docs/api/schemas/*.md + index
 *  - Lua: sygnatury M.fn(args) + komentarze LDoc/Emmy
 *  - C++: opcjonalny split per plik (--split-cpp)
 *  - Manifest do RAG: docs/_data/_api_manifest.json
 */

import fs from "fs/promises";
import path from "path";
import { glob } from "glob";

const argv = new Set(process.argv.slice(2));
const SPLIT_CPP = argv.has("--split-cpp"); // per-file strony dla C++
const MAX_DOC_PREVIEW = 200;

// ===== KONFIG =====
const OUT_MAIN = "docs/api/otcv8-full-api.md";
const OUT_SCHEMAS_DIR = "docs/api/schemas";
const OUT_SCHEMAS_INDEX = "docs/api/schemas/index.md";
const OUT_CPP_DIR = "docs/api/external/cpp"; // gdy --split-cpp
const OUT_MANIFEST = "docs/_data/_api_manifest.json";

// skanowane katalogi
const LUA_GLOB = ["**/*.lua", "!**/node_modules/**", "!**/site/**"];
const UI_GLOB = ["layouts/**/*.{otui,otml,txt}"];
const WS_GLOB = ["**/*.{json,js,ts,tsx}", "!**/node_modules/**", "!**/site/**"];
const CPP_GLOB = ["include/**/*.{h,hpp,hxx}", "src/**/*.{h,hpp,hxx}"];

const read = async f => { try { return await fs.readFile(f, "utf8"); } catch { return ""; } };
const ensureDir = p => fs.mkdir(path.dirname(p), { recursive: true });
const uniq = a => [...new Set(a)].sort((x, y) => x.localeCompare(y));
const esc = s => String(s ?? "").replace(/\|/g, "\\|").replace(/</g, "&lt;").replace(/>/g, "&gt;");

// MyST kotwice
const slug = s => s
  .toLowerCase()
  .replace(/[`~!@#$%^&*()+=\[\]{}|\\;:'",.<>/?]/g, "")
  .replace(/\s+/g, "-")
  .replace(/-+/g, "-")
  .replace(/^-|-$/g, "");

// =================== 1) LUA ===================
const luaFiles = await glob(LUA_GLOB, { nodir: true });
const lua = {
  events: new Set(),
  globals: new Set(),
  ctx: new Map(),                 // nazwa -> Set(odwołania)
  modules: new Map(),             // plik -> Map(nazwa -> {args, line})
  docs: new Map(),                // "M.fn" / "fn" / "ctx.fn" -> markdown doc
};

for (const f of luaFiles) {
  const t = await read(f); if (!t) continue;

  // onEvent()
  for (const m of t.matchAll(/\bon([A-Z][A-Za-z0-9_]*)\s*\(/g)) lua.events.add("on" + m[1]);

  // ctx.*
  for (const m of t.matchAll(/\bctx\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g)) {
    const k = m[1];
    const list = lua.ctx.get(k) || new Set();
    list.add(`${path.basename(f)}:${m.index}`);
    lua.ctx.set(k, list);
  }

  // M.* = function(...) i function M.fn(...)
  const modMap = new Map();
  for (const m of t.matchAll(/\bM\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*function\s*\(([^)]*)\)/g)) {
    modMap.set(m[1], { args: m[2].trim(), line: m.index });
  }
  for (const m of t.matchAll(/\bfunction\s+M\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\)/g)) {
    modMap.set(m[1], { args: m[2].trim(), line: m.index });
  }
  if (modMap.size) lua.modules.set(f, modMap);

  // globalne heurystycznie
  for (const m of t.matchAll(/\b([a-z][a-z0-9_]{2,})\s*\(/g)) {
    const n = m[1];
    if (["if", "for", "and", "end", "then", "else", "not", "nil", "true", "false", "local", "return", "function", "print", "ctx"].includes(n)) continue;
    if (!n.startsWith("on")) lua.globals.add(n);
  }

  // komentarze LDoc/Emmy poprzedzające function X(...) / function M.X(...)
  for (const m of t.matchAll(/(?:(?:---[^\n]*\n)+)\s*function\s+([A-Za-z0-9_.:]+)\s*\(([^)]*)\)/g)) {
    const sym = m[1];
    const before = t.slice(0, m.index);
    const doc = (before.match(/(---.*\n)+$/m) || [""])[0]
      .replace(/^--- ?/gm, "")
      .trim();
    if (doc) lua.docs.set(sym, doc);
  }
}

// =================== 2) OTUI ===================
const uiFiles = await glob(UI_GLOB, { nodir: true });
const ui = [];
for (const f of uiFiles) {
  const t = await read(f); if (!t) continue;
  for (const b of t.split(/\n\s*\n/)) {
    const m = b.match(/^\s*([A-Za-z][A-Za-z0-9]*)[\s\S]*?\bid:\s*([A-Za-z0-9_\-]+)/m);
    if (m) ui.push({ file: f, type: m[1], id: m[2] });
  }
}

// =================== 3) WS / JSON ===================
const txtFiles = await glob(WS_GLOB, { nodir: true });
const wsTypes = new Set();
const wsSchemas = new Map(); // $id -> file
for (const f of txtFiles) {
  const t = await read(f); if (!t) continue;
  for (const m of t.matchAll(/["']type["']\s*:\s*["']([a-zA-Z0-9._-]+)["']/g)) wsTypes.add(m[1]);
  const id = t.match(/"\$id"\s*:\s*"(.*?)"/);
  if (id && f.endsWith(".json")) wsSchemas.set(id[1], f);
}

// Render JSON schema → md (tabela właściwości)
function typeString(schema) {
  if (!schema) return "";
  const t = schema.type;
  if (Array.isArray(t)) return t.join(" | ");
  return t || (schema.anyOf ? "anyOf" : schema.oneOf ? "oneOf" : "");
}
async function renderSchemas() {
  await fs.mkdir(OUT_SCHEMAS_DIR, { recursive: true });
  const items = [];
  for (const [id, file] of [...wsSchemas.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
    let j;
    try { j = JSON.parse(await fs.readFile(file, "utf8")); } catch { continue; }
    const title = j.title || path.basename(file);
    const desc = j.description || "";
    const props = j.properties || {};
    const req = new Set(Array.isArray(j.required) ? j.required : []);
    const rows = Object.entries(props).map(([name, def]) => {
      const typ = esc(typeString(def));
      const dsc = esc(def.description || "");
      const en = def.enum ? def.enum.map(v => `\`${v}\``).join(", ") : "";
      const pattern = def.pattern ? `\`${def.pattern}\`` : "";
      const defVal = def.default !== undefined ? `\`${JSON.stringify(def.default)}\`` : "";
      const required = req.has(name) ? "yes" : "no";
      return `| \`${name}\` | ${typ} | ${dsc} | ${en} | ${pattern} | ${defVal} | ${required} |`;
    });

    const anchor = slug(title);
    const body = [
      `(${anchor})=`,
      `# ${title}`,
      id ? `**$id:** \`${id}\`` : "",
      desc ? `\n${desc}` : "",
      "\n## Properties\n",
      rows.length
        ? [
          "| name | type | description | enum | pattern | default | required |",
          "|---|---|---|---|---|---|---|",
          ...rows,
          "",
        ].join("\n")
        : "_No properties defined._\n",
    ].join("\n");
    const outName = path.basename(file).replace(/\.schema\.json$/i, ".md");
    const outPath = path.join(OUT_SCHEMAS_DIR, outName);
    await fs.writeFile(outPath, body, "utf8");
    items.push({ id, title, md: outPath });
  }

  // index
  const index = [
    "# WebSocket / JSON Schemas",
    "",
    "```{toctree}",
    ":maxdepth: 1",
    ...items.map(i => "./" + path.basename(i.md)),
    "```",
    "",
  ].join("\n");
  await fs.writeFile(OUT_SCHEMAS_INDEX, index, "utf8");

  return items;
}

// =================== 4) C++ ===================
const hFiles = await glob(CPP_GLOB, { nodir: true });
const cppByFile = new Map(); // file -> [{sig, brief}]
for (const f of hFiles) {
  const t = await read(f); if (!t) continue;
  const lines = t.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const L = lines[i];

    // prototyp: typ zwrotu + nazwa + (args) ;
    const m = L.match(/^\s*([A-Za-z_][A-Za-z0-9_:<>*&\s]+?)\s+([A-Za-z_][A-Za-z0-9_:<>*&]*)\s*\(([^)]*)\)\s*;/);
    if (m && !m[2].startsWith("operator")) {
      let brief = "";
      for (let j = i - 1; j >= 0 && j > i - 10; j--) {
        const b = lines[j].trim();
        if (/^(?:\/\*\*|\/\/\/|\*)/.test(b)) {
          brief = (b.replace(/^\/\*\*?|\*+\/|^\* ?|^\/\/\/ ?/g, "") + "\n" + brief).trim();
        } else if (b === "") {
          continue;
        } else break;
      }
      const sig = `${m[1].trim()} ${m[2]}(${m[3].trim()})`;
      const list = cppByFile.get(f) || [];
      list.push({ sig, brief });
      cppByFile.set(f, list);
    }
  }
}

// =================== RENDER MAIN ===================
const out = [];
const manifest = {
  generatedAt: new Date().toISOString(),
  main: OUT_MAIN,
  sections: [],
  schemas: [],
  cppSplit: SPLIT_CPP ? [] : null,
};

// nagłówek + spis treści MyST
out.push(`# OTCv8 – Pełne API (auto)\n`);
out.push(`Wygenerowano: ${new Date().toISOString()}\n`);
out.push(`> Ten plik jest generowany automatycznie z kodu. Nie edytuj ręcznie.\n`);
out.push("```{contents}\n:depth: 2\n:backlinks: entry\n```\n");

// -------- Lua --------
out.push(`(lua-api)=\n## 1. Lua\n`);

out.push(`### 1.1. Zdarzenia \`on*\``);
{
  const ev = uniq([...lua.events]);
  out.push(ev.length ? ev.map(x => `- \`${x}(...)\``).join("\n") : "_brak_");
  manifest.sections.push({ anchor: "lua-api", title: "Lua API" });
  manifest.sections.push({ anchor: "1-1-zdarzenia-on", title: "Lua: Zdarzenia" });
  out.push("");
}

out.push(`### 1.2. Kontekst \`ctx.*\``);
{
  const ctx = uniq([...lua.ctx.keys()]);
  out.push(ctx.length ? ctx.map(x => `- \`ctx.${x}(...)\``).join("\n") : "_brak_");
  out.push("");
}

out.push(`### 1.3. Moduły (eksporty \`M.*\`)`);
{
  const files = [...lua.modules.entries()].sort((a, b) => a[0].localeCompare(b[0]));
  if (!files.length) out.push("_brak_");
  for (const [file, map] of files) {
    out.push(`- **${file}**`);
    const items = [...map.entries()]
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([name, meta]) => `  - \`M.${name}(${meta.args})\``);
    if (items.length) out.push(items.join("\n"));
  }
  out.push("");
}

if (lua.globals.size) {
  out.push(`### 1.4. Globalne funkcje (heur.)`);
  const g = uniq([...lua.globals]).filter(n => !n.startsWith("on"));
  out.push(g.length ? g.map(n => "- `" + n + "()`").join("\n") : "_brak_");
  out.push("");
}

if (lua.docs.size) {
  out.push(`### 1.5. Komentarze LDoc/EmmyLua (wyciąg)`);
  for (const [sym, doc] of [...lua.docs.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
    const short = doc.replace(/\n+/g, " ").slice(0, MAX_DOC_PREVIEW);
    out.push(`- \`${sym}()\` — ${short}${doc.length > MAX_DOC_PREVIEW ? "…" : ""}`);
  }
  out.push("");
}

// -------- OTUI --------
out.push(`(otui)=\n## 2. OTUI (layouty)\n`);
if (ui.length) {
  const by = new Map();
  for (const it of ui) (by.get(it.file) || by.set(it.file, []).get(it.file)).push(it);
  for (const f of [...by.keys()].sort()) {
    const anchor = slug(`otui-${f}`);
    out.push(`(${anchor})=\n### ${f}`);
    out.push(by.get(f).map(x => `- \`${x.id}\` — **${x.type}**`).join("\n"));
    out.push("");
  }
} else {
  out.push("_brak plików layouts/_\n");
}

// -------- WS / Schemas --------
out.push(`(ws)=\n## 3. WebSocket / JSON\n`);
out.push(`### 3.1. Typy wiadomości (wykryte)`);
{
  const types = uniq([...wsTypes]);
  out.push(types.length ? types.map(t => "- `" + t + "`").join("\n") : "_brak_");
  out.push("");
}
out.push(`### 3.2. Schematy JSON ($id → plik)`);
{
  const list = [...wsSchemas.entries()].sort((a, b) => a[0].localeCompare(b[0]));
  out.push(list.length ? list.map(([id, f]) => `- \`${id}\` → \`${f}\``).join("\n") : "_brak_");
  out.push("");
}
const schemaItems = await renderSchemas();
manifest.schemas = schemaItems.map(s => ({
  id: s.id,
  title: s.title,
  md: path.relative(process.cwd(), s.md)
}));

// -------- C++ --------
out.push(`(cpp-api)=\n## 4. C++ (nagłówki)\n`);

if (!cppByFile.size) {
  out.push("_brak_\n");
} else if (!SPLIT_CPP) {
  const files = [...cppByFile.keys()].sort();
  for (const f of files) {
    const anchor = slug(`cpp-${f}`);
    out.push(`(${anchor})=\n### ${f}\n`);
    const list = cppByFile.get(f);
    for (const it of list) {
      out.push("```cpp");
      out.push(it.sig + ";");
      out.push("```");
      if (it.brief) out.push(it.brief + "\n");
    }
  }
} else {
  // split per plik
  await fs.mkdir(OUT_CPP_DIR, { recursive: true });
  const idx = [];
  const files = [...cppByFile.keys()].sort();
  for (const f of files) {
    const relName = f.replace(/[\\/]/g, "_").replace(/\.(h|hpp|hxx)$/i, "") + ".md";
    const outPath = path.join(OUT_CPP_DIR, relName);
    const title = f;
    const lines = [];
    lines.push(`# ${title}\n`);
    const list = cppByFile.get(f);
    for (const it of list) {
      lines.push("```cpp");
      lines.push(it.sig + ";");
      lines.push("```");
      if (it.brief) lines.push(it.brief + "\n");
    }
    await fs.writeFile(outPath, lines.join("\n"), "utf8");
    idx.push({ title, md: outPath });
  }
  // indeks w głównym pliku
  out.push("```{toctree}\n:maxdepth: 1");
  for (const item of idx) {
    out.push(path.relative("docs", item.md).replace(/\\/g, "/").replace(/^docs\//, ""));
  }
  out.push("```\n");
  manifest.cppSplit = idx.map(i => ({ title: i.title, md: i.md }));
}

// -------- Uwaga + linki --------
out.push(`## 5. Uwaga`);
out.push("- Jeśli czegoś brakuje: doprecyzuj wzorce w **tym skrypcie** (sekcje regexów).");
out.push(`- Dodaj JSON Schema do \`schemas/ws/*.schema.json\` — wygenerują się automatycznie jako strony w \`${OUT_SCHEMAS_DIR}\`.`);
out.push("");

// zapis
await ensureDir(OUT_MAIN);
await fs.writeFile(OUT_MAIN, out.join("\n"), "utf8");

// manifest (do RAG itp.)
await fs.mkdir(path.dirname(OUT_MANIFEST), { recursive: true });
await fs.writeFile(OUT_MANIFEST, JSON.stringify(manifest, null, 2), "utf8");

console.log("OK ->", OUT_MAIN);
if (SPLIT_CPP) console.log("C++ split ->", OUT_CPP_DIR);
console.log("Schemas ->", OUT_SCHEMAS_DIR, "(index:", OUT_SCHEMAS_INDEX, ")");
console.log("Manifest ->", OUT_MANIFEST);
