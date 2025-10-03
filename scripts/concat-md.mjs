// Użycie: node scripts/concat-md.mjs mkdocs.yml /tmp/OUT.md
import fs from "fs/promises";
import path from "path";
import { load as yamlLoad } from "js-yaml";
import { glob } from "glob";

const [, , mkdocsPath, outPath] = process.argv;
if (!mkdocsPath || !outPath) process.exit(1);

const mk = yamlLoad(await fs.readFile(mkdocsPath, "utf8"));
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
if (!files.length) {
  const all = await glob("docs/**/*.md", { ignore: ["docs/rag/**"] });
  files = all.map(f => ({ label: path.basename(f, ".md"), file: f }));
}

const stripFM = t => t.replace(/^---[\s\S]*?---\n/, "");
let out = `# ${mk?.site_name || "Documentation"}\n`;

for (const { label, file } of files) {
  let md = await fs.readFile(file, "utf8");
  md = stripFM(md).trim();
  out += `\n\n---\n\n# ${label}\n\n${md}\n`;
}

await fs.writeFile(outPath, out);
console.log("OK ->", outPath);
