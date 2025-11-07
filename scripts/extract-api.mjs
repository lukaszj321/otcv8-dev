#!/usr/bin/env node
/**
 * OTCv8 - kompletny i bezpieczny ekstraktor API
 *
 * Funkcje:
 * - skanuje repo rekurencyjnie w katalogach: data, modules, vc16, src (w tym podkatalogi android, client, framework),
 *   android (java/xml), layouts/**, include/**, src/** itp.
 * - używa parserów Tree-sitter (opcjonalnie, auto-install po fladze --install-deps) dla C++, Lua i Java,
 *   z bezpiecznymi fallbackami regex gdy parsery niedostępne
 * - generuje: docs/api/otcv8-full-api.md, docs/api/schemas/*.md, docs/api/external/cpp/*.md (jeśli --no-split-cpp nie użyte),
 *   docs/_data/_api_manifest.json, docs/_data/_api_entities.json (przydatne do RAG)
 * - opcjonalnie uruchamia tools/lua-binding-generator/generate_lua_bindings.lua (--run-lua-bindgen)
 *
 * Uruchamianie:
 *   node scripts/extract-api.mjs
 *   node scripts/extract-api.mjs --install-deps            # spróbuje zainstalować tree-sitter i języki
 *   node scripts/extract-api.mjs --run-lua-bindgen         # uruchomi generator lua bindów (jeżeli lua dostępne)
 *   node scripts/extract-api.mjs --no-split-cpp            # nie dzieli C++ per plik
 *
 * Uwaga: automatyczna instalacja odbywa się tylko gdy jawnie podasz --install-deps.
 */

import fs from "fs/promises";
import path from "path";
import { glob } from "glob";
import { spawnSync } from "child_process";

const argv = new Set(process.argv.slice(2));
const SPLIT_CPP = !argv.has("--no-split-cpp"); // Default: split per-header
const INSTALL_DEPS = argv.has("--install-deps") || process.env.AUTO_INSTALL_TREESITTER === "1";
const RUN_LUA_BINDGEN = argv.has("--run-lua-bindgen");
const MAX_DOC_PREVIEW = 400;

// ===== ŚCIEŻKI WYJŚCIOWE =====
const OUT_MAIN = "docs/api/otcv8-full-api.md";
const OUT_SCHEMAS_DIR = "docs/api/schemas";
const OUT_SCHEMAS_INDEX = "docs/api/schemas/index.md";
const OUT_CPP_DIR = "docs/api/external/cpp";
const OUT_CPP_INDEX = "docs/api/external/cpp/index.md";
const OUT_MANIFEST = "docs/_data/_api_manifest.json";
const OUT_ENTITIES = "docs/_data/_api_entities.json";
const OUT_LUA_BINDINGS = "docs/api/lua-bindings.txt";

// ===== ZESTAW GLOBÓW (rozszerzone) =====
const LUA_GLOB = [
  "**/*.lua",
  "!**/node_modules/**",
  "!**/site/**",
  "!**/_build/**",
  "!docs/**"
];
const UI_GLOB = ["layouts/**/*.{otui,otml,txt}", "!docs/**"];
const WS_GLOB = [
  "**/*.{json,js,ts,tsx}",
  "!**/node_modules/**",
  "!**/site/**",
  "!**/_build/**",
  "!docs/**"
];
const CPP_GLOB = [
  "include/**/*.{h,hpp,hxx}",
  "src/**/*.{h,hpp,hxx}",
  "vc16/**/*.{h,hpp,hxx}",
  "modules/**/*.{h,hpp,hxx}",
  "data/**/*.{h,hpp,hxx}",
  "!**/node_modules/**",
  "!**/site/**",
  "!**/_build/**",
  "!docs/**"
];
const JAVA_GLOB = ["android/**/*.java", "src/**/*.java", "!**/node_modules/**", "!**/site/**", "!**/_build/**", "!docs/**"];
const XML_GLOB = ["android/**/*.xml", "res/**/*.xml", "layouts/**/*.{xml,otui,otml}", "!**/node_modules/**", "!**/site/**", "!**/_build/**", "!docs/**"];
const OTHER_TEXT_GLOB = ["data/**/*.*", "modules/**/*.*", "vc16/**/*.*", "!**/node_modules/**", "!docs/**"];

// ===== POMOCE =====
const read = async (f) => { try { return await fs.readFile(f, "utf8"); } catch { return ""; } };
const ensureDir = (p) => fs.mkdir(path.dirname(p), { recursive: true });
const uniq = (a) => [...new Set(a)].sort((x, y) => x.localeCompare(y));
const esc = (s) => String(s ?? "").replace(/\|/g, "\\|").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const slug = (s) => String(s ?? "").toLowerCase()
  .replace(/[`~!@#$%^&*()+=\[\]{}|\\;:'",.<>/?]/g, "")
  .replace(/\s+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "");

// ===== AUTOMATYCZNE INSTALOWANIE DEPENDENCJI (opcjonalne) =====
async function tryInstallTreeSitter() {
  if (!INSTALL_DEPS) return;
  console.log("Flag --install-deps detected. Attempting to install tree-sitter packages via npm...");
  const pkgs = ["tree-sitter", "tree-sitter-cpp", "tree-sitter-lua", "tree-sitter-java"];
  try {
    const res = spawnSync("npm", ["install", "--no-audit", "--no-fund", "--silent", ...pkgs], { stdio: "inherit" });
    if (res.error) {
      console.warn("npm install failed:", res.error.message);
    } else if (res.status !== 0) {
      console.warn("npm install returned non-zero status:", res.status);
    } else {
      console.log("npm install completed.");
    }
  } catch (e) {
    console.warn("Failed to run npm install:", e?.message || e);
  }
}

// ===== TRY IMPORT TREE-SITTER =====
let TS = null;
let TS_CPP = null;
let TS_LUA = null;
let TS_JAVA = null;
async function tryLoadTreeSitter() {
  try {
    const TreeSitter = (await import("tree-sitter")).default;
    TS = TreeSitter;
    try { TS_CPP = (await import("tree-sitter-cpp")).default; } catch { TS_CPP = null; }
    try { TS_LUA = (await import("tree-sitter-lua")).default; } catch { TS_LUA = null; }
    try { TS_JAVA = (await import("tree-sitter-java")).default; } catch { TS_JAVA = null; }
    console.log("Tree-sitter detection:", { TS: !!TS, TS_CPP: !!TS_CPP, TS_LUA: !!TS_LUA, TS_JAVA: !!TS_JAVA });
  } catch (err) {
    console.log("Tree-sitter unavailable. Proceeding with regex fallback. Use --install-deps to attempt auto-install.");
  }
}

// ===== Pomocnicze funkcje do parsowania i komentarzy =====
async function collectCommentsAbove(src, startIndex) {
  const up = src.slice(0, startIndex).split("\n");
  let brief = "";
  for (let j = up.length - 1; j >= 0 && j > up.length - 25; j--) {
    const line = up[j].trim();
    if (/^(?:\/\*\*|\/\/\/|\/\*|\*)/.test(line) || /^\s*\/\/\s*@?/.test(line)) {
      brief = (line.replace(/^\/\*\*?|\*+\/|^\* ?|^\/\/\/ ?|^\/\/ ?/g, "") + "\n" + brief).trim();
    } else if (line === "") {
      continue;
    } else break;
  }
  return brief;
}

function typeString(schema) {
  if (!schema) return "";
  const t = schema.type;
  if (Array.isArray(t)) return t.join(" | ");
  return t || (schema.anyOf ? "anyOf" : schema.oneOf ? "oneOf" : "");
}

async function renderSchemas(wsSchemas) {
  await fs.mkdir(OUT_SCHEMAS_DIR, { recursive: true });
  const items = [];
  for (const [id, file] of [...wsSchemas.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
    let j; try { j = JSON.parse(await fs.readFile(file, "utf8")); } catch { continue; }
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

// ===== GŁÓWNY PRZEPŁYW =====
(async () => {
  // Optional auto-install
  await tryInstallTreeSitter();
  await tryLoadTreeSitter();

  // ----- ZBIERANIE PLIKÓW -----
  const luaFiles = await glob(LUA_GLOB, { nodir: true });
  const uiFiles = await glob(UI_GLOB, { nodir: true });
  const txtFiles = await glob(WS_GLOB, { nodir: true });
  const hFiles = await glob(CPP_GLOB, { nodir: true });
  const javaFiles = await glob(JAVA_GLOB, { nodir: true });
  const xmlFiles = await glob(XML_GLOB, { nodir: true });
  const otherFiles = await glob(OTHER_TEXT_GLOB, { nodir: true });

  // ----- LUA -----
  const lua = {
    events: new Set(),
    globals: new Set(),
    ctx: new Map(),        // name -> Set(files:line)
    modules: new Map(),    // file -> Map(fname -> {args,line,modName})
    docs: new Map(),       // symbol -> doc
    moduleNames: new Set(["M", "Module", "Api", "API", "mod", "export", "exports"])
  };

  // Parse Lua files (prefer tree-sitter)
  if (TS && TS_LUA) {
    for (const f of luaFiles) {
      const t = await read(f); if (!t) continue;
      for (const m of t.matchAll(/\blocal\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\{\s*\}/g)) lua.moduleNames.add(m[1]);
      try {
        const parser = new TS();
        parser.setLanguage(TS_LUA);
        const tree = parser.parse(t);
        const visit = (node) => {
          try {
            if (node.type === "function_declaration" || node.type === "function_definition") {
              const nameNode = node.namedChildren.find(c => ["identifier", "field_expression", "method_index_expression", "index_expression"].includes(c.type));
              const paramsNode = node.namedChildren.find(c => c.type === "parameters");
              const nameText = nameNode ? t.slice(nameNode.startIndex, nameNode.endIndex) : null;
              const paramsText = paramsNode ? t.slice(paramsNode.startIndex, paramsNode.endIndex).replace(/^\(|\)$/g, "") : "";
              if (nameText) {
                if (/^on[A-Z]/.test(nameText)) lua.events.add(nameText);
                if (nameText.includes("ctx.") || nameText.includes("ctx:")) {
                  const mm = nameText.match(/[:.]([A-Za-z_][A-Za-z0-9_]*)$/);
                  if (mm) { const list = lua.ctx.get(mm[1]) || new Set(); list.add(`${f}:${node.startPosition.row+1}`); lua.ctx.set(mm[1], list); }
                }
                if (nameText.includes(".")) {
                  const mod = nameText.split(".")[0]; lua.moduleNames.add(mod);
                  const map = lua.modules.get(f) || new Map(); map.set(nameText, { args: paramsText.trim(), line: node.startPosition.row+1, modName: mod }); lua.modules.set(f, map);
                } else {
                  if (!nameText.startsWith("on")) lua.globals.add(nameText);
                }
              }
            }
            for (const c of node.namedChildren) visit(c);
          } catch (e) {}
        };
        visit(tree.rootNode);
        // extract LDoc comments preceding functions
        for (const m of t.matchAll(/(?:(?:---[^\n]*\n)+)\s*function\s+([A-Za-z0-9_.:]+)\s*\(([^)]*)\)/g)) {
          const sym = m[1]; const before = t.slice(0, m.index);
          const doc = (before.match(/(---.*\n)+$/m) || [""])[0].replace(/^--- ?/gm, "").trim();
          if (doc) lua.docs.set(sym, doc);
        }
      } catch (e) {
        // fallback to heuristics below
        console.warn("Tree-sitter Lua parse failed for", f, e?.message);
      }
      // fallback heuristics (also run to catch additional patterns)
      for (const m of (t.matchAll(/\bon([A-Z][A-Za-z0-9_]*)\s*\(/g) || [])) lua.events.add("on" + m[1]);
      for (const m of (t.matchAll(/\bctx[:.]([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g) || [])) {
        const k = m[1]; const list = lua.ctx.get(k) || new Set(); list.add(`${path.basename(f)}:${m.index}`); lua.ctx.set(k, list);
      }
      for (const modName of lua.moduleNames) {
        const modMap = lua.modules.get(f) || new Map();
        for (const m of t.matchAll(new RegExp(`\\b${modName}\\.([a-zA-Z_][a-zA-Z0-9_]*)\\s*=\\s*function\\s*\\(([^)]*)\\)`, "g"))) {
          modMap.set(`${modName}.${m[1]}`, { args: m[2].trim(), line: m.index, modName });
        }
        for (const m of t.matchAll(new RegExp(`\\bfunction\\s+${modName}\\.([a-zA-Z_][a-zA-Z0-9_]*)\\s*\\(([^)]*)\\)`, "g"))) {
          modMap.set(`${modName}.${m[1]}`, { args: m[2].trim(), line: m.index, modName });
        }
        if (modMap.size) lua.modules.set(f, modMap);
      }
      for (const m of (t.matchAll(/\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\)/g) || [])) {
        const name = m[1]; if (!name.startsWith("on")) lua.globals.add(name);
      }
      for (const m of (t.matchAll(/(?:(?:---[^\n]*\n)+)\s*function\s+([A-Za-z0-9_.:]+)\s*\(([^)]*)\)/g) || [])) {
        const sym = m[1]; const before = t.slice(0, m.index);
        const doc = (before.match(/(---.*\n)+$/m) || [""])[0].replace(/^--- ?/gm, "").trim();
        if (doc) lua.docs.set(sym, doc);
      }
    }
  } else {
    // No tree-sitter available: use original heuristics for all Lua files
    for (const f of luaFiles) {
      const t = await read(f); if (!t) continue;
      for (const m of t.matchAll(/\blocal\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*\{\s*\}/g)) lua.moduleNames.add(m[1]);
      for (const m of t.matchAll(/\bon([A-Z][A-Za-z0-9_]*)\s*\(/g)) lua.events.add("on" + m[1]);
      for (const m of t.matchAll(/\bctx[:.]([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/g)) {
        const k = m[1]; const list = lua.ctx.get(k) || new Set(); list.add(`${path.basename(f)}:${m.index}`); lua.ctx.set(k, list);
      }
      for (const modName of lua.moduleNames) {
        const modMap = lua.modules.get(f) || new Map();
        for (const m of t.matchAll(new RegExp(`\\b${modName}\\.([a-zA-Z_][a-zA-Z0-9_]*)\\s*=\\s*function\\s*\\(([^)]*)\\)`, "g"))) {
          modMap.set(`${modName}.${m[1]}`, { args: m[2].trim(), line: m.index, modName });
        }
        for (const m of t.matchAll(new RegExp(`\\bfunction\\s+${modName}\\.([a-zA-Z_][a-zA-Z0-9_]*)\\s*\\(([^)]*)\\)`, "g"))) {
          modMap.set(`${modName}.${m[1]}`, { args: m[2].trim(), line: m.index, modName });
        }
        if (modMap.size) lua.modules.set(f, modMap);
      }
      for (const m of t.matchAll(/\bfunction\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\)/g)) {
        const name = m[1]; if (!name.startsWith("on")) lua.globals.add(name);
      }
      for (const m of t.matchAll(/(?:(?:---[^\n]*\n)+)\s*function\s+([A-Za-z0-9_.:]+)\s*\(([^)]*)\)/g)) {
        const sym = m[1]; const before = t.slice(0, m.index);
        const doc = (before.match(/(---.*\n)+$/m) || [""])[0].replace(/^--- ?/gm, "").trim();
        if (doc) lua.docs.set(sym, doc);
      }
    }
  }

  // ----- OTUI (layouts) -----
  const ui = [];
  for (const f of uiFiles) {
    const t = await read(f); if (!t) continue;
    for (const b of t.split(/\n\s*\n/)) {
      const m = b.match(/^\s*([A-Za-z][A-Za-z0-9]*)[\s\S]*?\bid\s*:\s*([A-Za-z0-9_\-]+)/m);
      if (m) ui.push({ file: f, type: m[1], id: m[2] });
    }
  }

  // ----- WS / JSON -----
  const wsTypes = new Set();
  const wsSchemas = new Map(); // $id -> file
  for (const f of txtFiles) {
    const t = await read(f); if (!t) continue;
    for (const m of t.matchAll(/["']type["']\s*:\s*["']([a-zA-Z0-9._-]+)["']/g)) wsTypes.add(m[1]);
    const id = t.match(/"\$id"\s*:\s*"(.*?)"/);
    if (id && f.endsWith(".json")) wsSchemas.set(id[1], f);
  }

  // ----- C++ (nagłówki): prefer Tree-sitter, fallback regex -----
  const cppByFile = new Map();
  const cppEntities = [];

  if (TS && TS_CPP) {
    for (const f of hFiles) {
      const raw = await read(f); if (!raw) continue;
      const t = raw.replace(/\r\n/g, "\n");
      try {
        const parser = new TS();
        parser.setLanguage(TS_CPP);
        const tree = parser.parse(t);
        const fileList = cppByFile.get(f) || [];
        const visitNode = (node) => {
          try {
            // function_definition, declaration, function_declarator, constructor_declaration, destructor_name
            if (["function_definition", "function_declarator", "declaration", "init_declarator"].includes(node.type)) {
              const txt = t.slice(node.startIndex, node.endIndex);
              const declRe = /([^\n;{=]+?)\s+([A-Za-z_][A-Za-z0-9_:<>*&~]+)\s*\(([^)]*)\)\s*(?:const)?\s*(?:noexcept)?\s*(?:=\s*0\s*)?(?:;|{|$)/s;
              const m = txt.match(declRe);
              if (m) {
                const retType = m[1].trim();
                const name = m[2].trim();
                const args = (m[3] || "").trim();
                const line = node.startPosition.row + 1;
                const brief = collectCommentsAbove(t, node.startIndex);
                const sig = `${retType} ${name}(${args})`.replace(/\s+/g, " ").trim();
                fileList.push({ sig, brief, file: f, line });
                // parameter splitting (best-effort)
                const params = [];
                let current = "";
                let angleDepth = 0;
                let parenDepth = 0;
                for (let i = 0; i < args.length; i++) {
                  const ch = args[i];
                  if (ch === "<") angleDepth++;
                  else if (ch === ">") angleDepth = Math.max(0, angleDepth - 1);
                  else if (ch === "(") parenDepth++;
                  else if (ch === ")") parenDepth = Math.max(0, parenDepth - 1);
                  if (ch === "," && angleDepth === 0 && parenDepth === 0) {
                    if (current.trim()) params.push(current.trim());
                    current = "";
                    continue;
                  }
                  current += ch;
                }
                if (current.trim()) params.push(current.trim());
                const normalizedParams = params.map(p => {
                  const parts = p.split("=").map(x => x.trim());
                  const paramPart = parts[0] || "";
                  const def = parts[1] || "";
                  const match = paramPart.match(/^(.+?)\s+([A-Za-z_][A-Za-z0-9_]*)$/);
                  return {
                    raw: p,
                    type: match ? match[1].trim() : paramPart,
                    name: match ? match[2].trim() : "",
                    default: def || ""
                  };
                });
                cppEntities.push({
                  id: `${f}:${line}:${name}`,
                  kind: "cpp_function",
                  name,
                  signature: sig,
                  returnType: esc(retType),
                  params: normalizedParams,
                  doc: brief,
                  file: f,
                  line
                });
              }
            }
            for (const c of node.children) visitNode(c);
          } catch (e) {}
        };
        visitNode(tree.rootNode);
        if (fileList.length) cppByFile.set(f, fileList);
      } catch (e) {
        console.warn("Tree-sitter C++ parse failed for", f, e?.message);
      }
    }
  } else {
    // fallback regex-based extraction (improved)
    for (const f of hFiles) {
      const raw = await read(f); if (!raw) continue;
      const t = raw.replace(/\r\n/g, "\n");
      const declRe = /(^|\n)\s*(?:template\s*<[^>]+>\s*)*(?:[A-Za-z_][A-Za-z0-9_:<>*&\s]+)\s+([A-Za-z_][A-Za-z0-9_:<>*&~]*)\s*\(([^;{}]*)\)\s*(?:const\s*)?(?:noexcept\s*)?(?:=\s*0\s*)?;\s*(?=$|\n)/g;
      const defRe = /(^|\n)\s*(?:template\s*<[^>]+>\s*)*([A-Za-z_][A-Za-z0-9_:<>*&\s]+)\s+([A-Za-z_][A-Za-z0-9_:<>*&~]*)\s*\(([^;{}]*)\)\s*(?:const\s*)?(?:noexcept\s*)?\s*\{\s*/g;
      const add = (sig, brief, file, line) => {
        if (sig.trim().startsWith('return ')) return;
        if (sig.includes(') :') && sig.includes('(') && sig.split('(').length > 2) return;
        const paramPart = sig.match(/\((.*)\)/)?.[1] || '';
        if (paramPart.includes(') :') || paramPart.includes('{ }') || paramPart.includes('{  }')) return;
        const list = cppByFile.get(file) || [];
        list.push({ sig, brief, file, line });
        cppByFile.set(file, list);
      };
      for (const m of t.matchAll(declRe)) {
        const idx = m.index ?? 0;
        const retType = (m[0].match(/^\s*(?:template\s*<[^>]+>\s*)*([A-Za-z_][A-Za-z0-9_:<>*&\s]+)\s+[A-Za-z_]/m) || [, ""])[1]?.trim() ?? "";
        const name = m[2].trim();
        const args = (m[3] || "").replace(/\s+/g, " ").trim();
        const sig = `${retType} ${name}(${args})`.replace(/\s+/g, " ").trim();
        const line = t.slice(0, idx).split("\n").length;
        const brief = await collectCommentsAbove(t, idx);
        add(sig, brief, f, line);
        cppEntities.push({
          id: `${f}:${line}:${name}`,
          kind: "cpp_function",
          name,
          signature: sig,
          returnType: esc(retType),
          params: [], doc: brief, file: f, line
        });
      }
      for (const m of t.matchAll(defRe)) {
        const idx = m.index ?? 0;
        const retType = m[2].trim().replace(/\s+/g, " ");
        const name = m[3].trim();
        const args = (m[4] || "").replace(/\s+/g, " ").trim();
        const sig = `${retType} ${name}(${args})`.replace(/\s+/g, " ").trim();
        const line = t.slice(0, idx).split("\n").length;
        const brief = await collectCommentsAbove(t, idx);
        add(sig, brief, f, line);
        cppEntities.push({
          id: `${f}:${line}:${name}`,
          kind: "cpp_function",
          name,
          signature: sig,
          returnType: esc(retType),
          params: [], doc: brief, file: f, line
        });
      }
    }
  }

  // ----- Java & Android XML -----
  const javaEntities = [];
  if (TS && TS_JAVA) {
    for (const f of javaFiles) {
      const t = await read(f); if (!t) continue;
      try {
        const parser = new TS(); parser.setLanguage(TS_JAVA);
        const tree = parser.parse(t);
        const visit = (node) => {
          try {
            if (node.type === "method_declaration" || node.type === "constructor_declaration") {
              const nameNode = node.namedChildren.find(c => c.type === "identifier");
              const paramsNode = node.namedChildren.find(c => c.type === "formal_parameters" || c.type === "formal_parameter_list");
              const retNode = node.namedChildren.find(c => c.type === "type");
              const name = nameNode ? t.slice(nameNode.startIndex, nameNode.endIndex) : "<anon>";
              const paramsText = paramsNode ? t.slice(paramsNode.startIndex, paramsNode.endIndex).replace(/^\(|\)$/g, "") : "";
              const ret = retNode ? t.slice(retNode.startIndex, retNode.endIndex) : "";
              const line = node.startPosition.row + 1;
              const doc = (t.slice(0, node.startIndex).match(/(\/\*\*[\s\S]*?\*\/)\s*$/) || [""])[0].replace(/\/\*\*|\*\/|^\s*\*\s?/gm, "").trim();
              javaEntities.push({ id: `${f}:${line}:${name}`, kind: "java_method", name, signature: `${ret} ${name}(${paramsText})`, returnType: ret, params: [], doc, file: f, line });
            }
            for (const c of node.namedChildren) visit(c);
          } catch (e) {}
        };
        visit(tree.rootNode);
      } catch (e) {
        console.warn("Tree-sitter Java parse failed for", f, e?.message);
      }
    }
  } else {
    // fallback regex
    for (const f of javaFiles) {
      const t = await read(f); if (!t) continue;
      for (const m of t.matchAll(/(public|protected|private)?\s*(static)?\s*([A-Za-z0-9_<>\[\]]+\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)\s*(?:throws[^{]+)?\{/g)) {
        const ret = (m[3] || "").trim();
        const name = m[4];
        const paramsText = (m[5] || "").trim();
        const idx = m.index || 0;
        const line = t.slice(0, idx).split("\n").length;
        const doc = (t.slice(0, idx).match(/(\/\*\*[\s\S]*?\*\/)\s*$/) || [""])[0].replace(/\/\*\*|\*\/|^\s*\*\s?/gm, "").trim();
        javaEntities.push({ id: `${f}:${line}:${name}`, kind: "java_method", name, signature: `${ret} ${name}(${paramsText})`, returnType: ret, params: [], doc, file: f, line });
      }
    }
  }

  // XML entities
  const xmlEntities = [];
  for (const f of xmlFiles) {
    const t = await read(f); if (!t) continue;
    for (const m of t.matchAll(/\bid\s*=\s*["'](@\+id\/)?([A-Za-z0-9_:-]+)["']/g)) {
      xmlEntities.push({ file: f, id: m[2] });
    }
  }

  // ----- OTHER FILES (data/modules/vc16) - small snippets -----
  const otherText = [];
  for (const f of otherFiles) {
    const t = await read(f); if (!t) continue;
    if (f.endsWith(".json")) {
      try { const j = JSON.parse(t); otherText.push({ file: f, type: "json", content: JSON.stringify(j) }); } catch { otherText.push({ file: f, type: "text", content: t.slice(0, 20000) }); }
    } else {
      otherText.push({ file: f, type: "text", content: t.slice(0, 20000) });
    }
  }

  // ----- RENDERING & ZAPIS -----
  const out = [];
  const manifest = {
    generatedAt: new Date().toISOString(),
    main: OUT_MAIN,
    sections: [],
    schemas: [],
    cppSplit: SPLIT_CPP ? [] : null,
    counts: {
      lua_files: luaFiles.length,
      cpp_headers: hFiles.length,
      java_files: javaFiles.length,
      xml_files: xmlFiles.length
    }
  };

  out.push(`# OTCv8 - Pełne API (auto)\n`);
  out.push(`Wygenerowano: ${new Date().toISOString()}\n`);
  out.push(`> Ten plik jest generowany automatycznie z kodu. Nie edytuj ręcznie.\n`);
  out.push("```{contents}\n:depth: 2\n:backlinks: entry\n```\n");

  // Lua summary
  out.push(`(lua-api)=\n## 1. Lua\n`);
  out.push(`### 1.1. Zdarzenia \`on*\``);
  {
    const ev = uniq([...lua.events]);
    out.push(ev.length ? ev.map(x => `- \`${x}(...)\``).join("\n") : "_brak_");
    out.push("");
  }
  out.push(`### 1.2. Kontekst \`ctx.*\``);
  {
    const ctx = uniq([...lua.ctx.keys()]);
    out.push(ctx.length ? ctx.map(x => `- \`ctx.${x}(...)\``).join("\n") : "_brak_");
    out.push("");
  }
  out.push(`### 1.3. Moduły (eksporty)`);
  {
    const files = [...lua.modules.entries()].sort((a, b) => a[0].localeCompare(b[0]));
    if (!files.length) out.push("_brak_");
    for (const [file, map] of files) {
      out.push(`- **${file}**`);
      const items = [...map.entries()]
        .sort((a, b) => a[0].localeCompare(b[0]))
        .map(([name, meta]) => `  - \`${name}(${meta.args})\` — ${meta.line ? `line ${meta.line}` : ""}`);
      if (items.length) out.push(items.join("\n"));
    }
    out.push("");
  }
  if (lua.globals.size) {
    out.push(`### 1.4. Globalne funkcje (wykryte)`);
    const g = uniq([...lua.globals]).filter(n => !n.startsWith("on"));
    out.push(g.length ? g.map(n => "- `" + n + "()`").join("\n") : "_brak_");
    out.push("");
  }
  if (lua.docs.size) {
    out.push(`### 1.5. Komentarze LDoc/Emmy (wyciąg)`);
    for (const [sym, doc] of [...lua.docs.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
      const short = doc.replace(/\n+/g, " ").slice(0, MAX_DOC_PREVIEW);
      out.push(`- \`${sym}()\` — ${short}${doc.length > MAX_DOC_PREVIEW ? "…" : ""}`);
    }
    out.push("");
  }

  // OTUI
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

  // WS
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
  const schemaItems = await renderSchemas(wsSchemas);
  manifest.schemas = schemaItems.map(s => ({ id: s.id, title: s.title, md: s.md }));

  // Java/XML
  out.push(`(android)=\n## 4. Android / Java / XML\n`);
  out.push(`### 4.1. Java - metody wykryte`);
  if (javaEntities.length) {
    out.push(javaEntities.map(j => `- \`${j.name}()\` — ${j.file}:${j.line}`).join("\n"));
  } else {
    out.push("_brak_");
  }
  out.push("");
  out.push(`### 4.2. XML - id elementów`);
  if (xmlEntities.length) {
    const byFile = new Map();
    for (const it of xmlEntities) (byFile.get(it.file) || byFile.set(it.file, []).get(it.file)).push(it.id);
    for (const f of [...byFile.keys()].sort()) {
      out.push(`- **${f}**`);
      out.push(byFile.get(f).map(id => `  - \`${id}\``).join("\n"));
    }
  } else {
    out.push("_brak_");
  }
  out.push("");

  // C++
  out.push(`(cpp-api)=\n## 5. C++ (nagłówki)\n`);
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
    await fs.mkdir(OUT_CPP_DIR, { recursive: true });
    const idx = [];
    const files = [...cppByFile.keys()].sort();
    for (const f of files) {
      const relName = f.replace(/[\\/]/g, "_").replace(/\.(h|hpp|hxx)$/i, "") + ".md";
      const outPath = path.join(OUT_CPP_DIR, relName);
      const title = f;
      const lines = [];
      // YAML front-matter
      lines.push("---");
      lines.push(`title: "${title}"`);
      lines.push(`source_file: "${f}"`);
      lines.push(`generated_at: "${new Date().toISOString()}"`);
      lines.push(`doc_type: "cpp_api"`);
      lines.push("---");
      lines.push("");
      lines.push(`# ${title}\n`);
      const list = cppByFile.get(f) || [];
      const usedAnchors = new Set();
      for (const it of list) {
        const funcMatch = it.sig.match(/^(.*?)\s+([A-Za-z_][A-Za-z0-9_:<>*&~]*)\s*\((.*)\)$/s);
        if (funcMatch) {
          let [, retType, funcName, paramsStr] = funcMatch;
          retType = retType.replace(/^\s*(?:static|virtual|inline|explicit|constexpr)\s+/g, '').trim();
          const isConstructor = !retType || retType === funcName || retType === '';
          let anchor = slug(funcName);
          let anchorSuffix = 0;
          while (usedAnchors.has(anchor)) {
            anchorSuffix++;
            anchor = slug(funcName) + `-${anchorSuffix}`;
          }
          usedAnchors.add(anchor);
          lines.push(`(${anchor})=`);
          lines.push(`## \`${funcName}\``);
          lines.push("");
          if (it.brief) {
            lines.push(it.brief);
            lines.push("");
          }
          lines.push("**Signature:**");
          lines.push("```cpp");
          lines.push(it.sig + ";");
          lines.push("```");
          lines.push("");
          if (paramsStr && paramsStr.trim() && paramsStr.trim() !== "void") {
            const params = [];
            let current = '';
            let angleDepth = 0;
            let parenDepth = 0;
            for (let i = 0; i < paramsStr.length; i++) {
              const ch = paramsStr[i];
              if (ch === '<') angleDepth++;
              else if (ch === '>') angleDepth = Math.max(0, angleDepth - 1);
              else if (ch === '(') parenDepth++;
              else if (ch === ')') parenDepth = Math.max(0, parenDepth - 1);
              if (ch === ',' && angleDepth === 0 && parenDepth === 0) {
                if (current.trim()) params.push(current.trim());
                current = '';
                continue;
              }
              current += ch;
            }
            if (current.trim()) params.push(current.trim());
            if (params.length > 0) {
              lines.push("**Parameters:**");
              lines.push("");
              const hasDefaults = params.some(p => p.includes("="));
              if (hasDefaults) {
                lines.push("| Type | Name | Default | Description |");
                lines.push("|------|------|---------|-------------|");
              } else {
                lines.push("| Type | Name | Description |");
                lines.push("|------|------|-------------|");
              }
              for (const param of params) {
                let paramPart = param;
                let defaultVal = "";
                if (param.includes("=")) {
                  const parts = param.split("=");
                  paramPart = parts[0].trim();
                  defaultVal = parts.slice(1).join("=").trim();
                }
                const match = paramPart.match(/^(.+?)\s+([A-Za-z_][A-Za-z0-9_]*)$/);
                if (match) {
                  const [, type, name] = match;
                  if (hasDefaults) {
                    const defStr = defaultVal ? `\`${esc(defaultVal)}\`` : "";
                    lines.push(`| \`${esc(type.trim())}\` | \`${esc(name.trim())}\` | ${defStr} | - |`);
                  } else {
                    lines.push(`| \`${esc(type.trim())}\` | \`${esc(name.trim())}\` | - |`);
                  }
                } else {
                  if (hasDefaults) {
                    const defStr = defaultVal ? `\`${esc(defaultVal)}\`` : "";
                    lines.push(`| \`${esc(paramPart)}\` | - | ${defStr} | - |`);
                  } else {
                    lines.push(`| \`${esc(paramPart)}\` | - | - |`);
                  }
                }
              }
              lines.push("");
            }
          }
          if (!isConstructor && retType.trim() && retType.trim() !== "void" && !funcName.startsWith("~")) {
            lines.push("**Returns:**");
            lines.push(`- \`${esc(retType.trim())}\``);
            lines.push("");
          }
        } else {
          lines.push("```cpp");
          lines.push(it.sig + ";");
          lines.push("```");
          if (it.brief) lines.push(it.brief + "\n");
        }
        lines.push("---");
        lines.push("");
      }
      await fs.writeFile(outPath, lines.join("\n"), "utf8");
      idx.push({ title, md: outPath });
    }
    const cppIndex = [
      "# C++ - per-plik",
      "",
      "```{toctree}",
      ":maxdepth: 1",
      ...idx.map(x => "./" + path.basename(x.md)),
      "```",
      ""
    ].join("\n");
    await fs.writeFile(OUT_CPP_INDEX, cppIndex, "utf8");
    manifest.cppSplit = idx;
  }

  // ----- Informacje dodatkowe i zapis doc/main -----
  out.push(`## 6. Pozostałe informacje i wskazówki`);
  out.push("- Jeśli czegoś brakuje: doprecyzuj wzorce w tym skrypcie (sekcje regexów) lub zainstaluj tree-sitter dla dokładniejszego AST.");
  out.push(`- Dodaj JSON Schema do \`schemas/ws/*.schema.json\` — wygenerują się automatycznie jako strony w \`${OUT_SCHEMAS_DIR}\`.`);
  out.push("");

  await ensureDir(OUT_MAIN);
  await fs.writeFile(OUT_MAIN, out.join("\n"), "utf8");

  // ----- manifest (rozszerzony) -----
  const fullManifest = {
    ...manifest,
    lua: {
      events: [...lua.events],
      ctx: Object.fromEntries([...lua.ctx.entries()].map(([k, s]) => [k, [...s]])),
      modules: [...lua.modules.entries()].map(([f, m]) => [f, [...m.entries()]]),
      docs: [...lua.docs.entries()]
    },
    cpp: {
      byFile: [...cppByFile.entries()].map(([f, list]) => [f, list.map(it => ({ sig: it.sig, brief: it.brief, file: it.file, line: it.line }))])
    },
    java: javaEntities.length,
    xml: xmlEntities.length
  };
  await fs.mkdir(path.dirname(OUT_MANIFEST), { recursive: true });
  await fs.writeFile(OUT_MANIFEST, JSON.stringify(fullManifest, null, 2), "utf8");

  // ----- entities (RAG) -----
  const entities = [];
  for (const [k, doc] of lua.docs.entries()) entities.push({ id: `lua:${k}`, kind: "lua_doc", name: k, text: doc });
  for (const e of cppEntities) entities.push(e);
  for (const e of javaEntities) entities.push(e);
  for (const e of xmlEntities) entities.push({ id: `xml:${e.file}:${e.id}`, kind: "xml_id", file: e.file, name: e.id });
  for (const o of otherText) entities.push({ id: `text:${o.file}`, kind: o.type, file: o.file, text: o.content.slice(0, 20000) });
  await fs.mkdir(path.dirname(OUT_ENTITIES), { recursive: true });
  await fs.writeFile(OUT_ENTITIES, JSON.stringify(entities, null, 2), "utf8");

  console.log("OK ->", OUT_MAIN);
  if (SPLIT_CPP) console.log("C++ split ->", OUT_CPP_DIR);
  console.log("Schemas ->", OUT_SCHEMAS_DIR, "(index:", OUT_SCHEMAS_INDEX, ")");
  console.log("Manifest ->", OUT_MANIFEST);
  console.log("Entities (RAG) ->", OUT_ENTITIES);

  // ----- OPTIONAL: run Lua binding generator and capture output -----
  if (RUN_LUA_BINDGEN) {
    console.log("Flag --run-lua-bindgen set: attempting to run tools/lua-binding-generator/generate_lua_bindings.lua...");
    try {
      const which = spawnSync(process.platform === "win32" ? "where" : "which", ["lua"], { encoding: "utf8" });
      if (which.status === 0) {
        const headers = uniq(hFiles);
        if (headers.length === 0) {
          console.log("No header files found to pass to lua binding generator.");
        } else {
          const scriptPath = path.join("tools", "lua-binding-generator", "generate_lua_bindings.lua");
          const args = [scriptPath, ...headers];
          console.log("Running:", "lua", args.join(" "));
          const res = spawnSync("lua", args, { encoding: "utf8", maxBuffer: 200 * 1024 * 1024 });
          if (res.error) {
            console.warn("Failed to run lua generator:", res.error.message);
          } else {
            try {
              await fs.mkdir(path.dirname(OUT_LUA_BINDINGS), { recursive: true });
              await fs.writeFile(OUT_LUA_BINDINGS, res.stdout || "", "utf8");
              console.log("Lua binding generator output saved to", OUT_LUA_BINDINGS);
            } catch (e) { console.warn("Failed to write lua binding output:", e?.message || e); }
            if (res.stderr) console.error("lua generator stderr:", res.stderr);
          }
        }
      } else {
        console.warn("No 'lua' interpreter found on PATH; install lua or run the binding generator manually.");
      }
    } catch (e) {
      console.warn("Error attempting to run lua generator:", e?.message || e);
    }
  }
})().catch(err => {
  console.error("Fatal error during extraction:", err);
  process.exit(1);
});
