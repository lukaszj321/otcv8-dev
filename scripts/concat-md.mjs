// Użycie: node scripts/concat-md.mjs mkdocs.yml /sciezka/wyjscia.md
import fs from "fs/promises";
import path from "path";
import YAML from "js-yaml";
import { glob } from "glob";

const [, , mkdocsPath, outPath] = process.argv;
if (!mkdocsPath || !outPath) {
  console.error("Użycie: node scripts/concat-md.mjs mkdocs.yml /tmp/OUT.md");
  process.exit(1);
}

const repoRoot = process.cwd();

// Wczytaj mkdocs.yml i wyciągnij listę plików .md z sekcji nav (w kolejności)
const mk = YAML.load(await fs.readFile(mkdocsPath, "utf8"));
const nav = mk?.nav || [];

function collectNavFiles(items, acc = []) {
  for (const entry of items) {
    const [label, val] = Object.entries(entry)[0];
    if (typeof val === "string") {
      if (val.endsWith(".md")) acc.push({ label, file: val });
    } else if (Array.isArray(val)) {
      collectNavFiles(val, acc);
    }
  }
  return acc;
}

let files = collectNavFiles(nav);

// Fallback: jeśli nav puste, bierz wszystkie docs/**/*.md (bez docs/rag/**)
if (!files.length) {
  const all = await glob("docs/**/*.md", { ignore: ["docs/rag/**"] });
  files = all.map((f) => ({ label: path.basename(f, ".md"), file: f }));
}

function stripFM(t) { return t.replace(/^---[\s\S]*?---\n/, ""); }

let out = `# ${mk?.site_name || "Documentation"}\n\n`;
for (const { label, file } of files) {
  const abs = path.join(repoRoot, file);
  let md = await fs.readFile(abs, "utf8");
  md = stripFM(md);
  out += `\n\n---\n\n# ${label}\n\n` + md.trim() + "\n";
}

await fs.writeFile(outPath, out);
console.log(`OK -> ${outPath}`);
