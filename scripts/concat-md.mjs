// Użycie: node scripts/concat-md.mjs mkdocs.yml OUT.md
import fs from "fs/promises";
import path from "path";
import { load as yamlLoad } from "js-yaml";

const [, , mkdocsPath, outPath] = process.argv;
if (!mkdocsPath || !outPath) {
  console.error("Użycie: node scripts/concat-md.mjs mkdocs.yml OUT.md");
  process.exit(1);
}

const repoRoot = process.cwd();
const mk = yamlLoad(await fs.readFile(mkdocsPath, "utf8"));
const docsDir = mk?.docs_dir || "docs";
const nav = mk?.nav || [];

function collectNavFiles(items, acc = []) {
  for (const e of items) {
    const [label, val] = Object.entries(e)[0];
    if (typeof val === "string" && val.endsWith(".md")) acc.push({ label, file: val });
    else if (Array.isArray(val)) collectNavFiles(val, acc);
  }
  return acc;
}

let files = collectNavFiles(nav);

// Fallback, gdy nav puste
if (!files.length) {
  const { glob } = await import("glob");
  const all = await glob(`${docsDir}/**/*.md`, { ignore: [`${docsDir}/rag/**`] });
  files = all.map(f => ({ label: path.basename(f, ".md"), file: f.replace(`${docsDir}/`, "") }));
}

const stripFM = t => t.replace(/^---[\s\S]*?---\n/, "");
let out = `# ${mk?.site_name || "Documentation"}\n`;

for (const { label, file } of files) {
  // plik z nav (np. "index.md") → realna ścieżka w docsDir
  const rel = file.startsWith(`${docsDir}/`) ? file : path.join(docsDir, file);
  const abs = path.join(repoRoot, rel);
  let md = await fs.readFile(abs, "utf8");      // ← tu były ENOENT
  md = stripFM(md).trim();
  out += `\n\n---\n\n# ${label}\n\n${md}\n`;
}

await fs.mkdir(path.dirname(outPath), { recursive: true });
await fs.writeFile(outPath, out);
console.log("OK ->", outPath);
