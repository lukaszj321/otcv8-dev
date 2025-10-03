// Auto-fix docs/**/*.md
import fs from "fs/promises";
import { glob } from "glob";

const files = await glob("docs/**/*.md", { nodir: true, ignore: ["docs/build/**", "site/**"] });

for (const f of files) {
  let t = await fs.readFile(f, "utf8");
  t = t.replace(/\r\n/g, "\n");                 // CRLF -> LF
  t = t.replace(/[ \t]+$/gm, "");               // trailing spaces
  t = t.replace(/\t/g, "  ");                   // tabs -> 2 spacje
  t = t.replace(/[“”]/g, '"').replace(/[‘’]/g, "'"); // smart quotes -> ascii
  // pusta linia po nagłówkach
  t = t.replace(/(^#{1,6} .*)(?!\n\n)/gm, "$1\n");
  // admonitions
  t = t.replace(/(^|\n)!!! +([a-z]+)([^\n]*)\n(?!\n)/gi, (_m, a, b, c) => `${a}!!! ${b}${c}\n\n`);
  // domknij ``` jeśli nieparzyste
  if ((t.match(/```/g) || []).length % 2 === 1) t += "\n```\n";
  // normalize code fences
  t = t.replace(/(^|\n)``` *mermaid( *\n)?/g, "\n```mermaid\n");
  t = t.replace(/(^|\n)``` *otui( *\n)?/g, "\n```otui\n");
  t = t.replace(/([^\n])\n```/g, "$1\n\n```");
  t = t.replace(/```\n([^\n])/g, "```\n\n$1");
  await fs.writeFile(f, t);
  console.log("fixed:", f);
}
