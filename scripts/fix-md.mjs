// Auto-fix najczęstszych błędów w docs/**/*.md
import fs from "fs/promises";
import { glob } from "glob";

const files = await glob("docs/**/*.md", { nodir: true });

for (const f of files) {
  let t = await fs.readFile(f, "utf8");

  // Normalizacje:
  t = t.replace(/\r\n/g, "\n");                    // CRLF -> LF
  t = t.replace(/[ \t]+$/gm, "");                  // trailing spaces
  t = t.replace(/\t/g, "  ");                      // tabs -> spaces
  t = t.replace(/[“”]/g, '"').replace(/[‘’]/g, "'");// smart quotes -> ascii

  // Pusta linia po nagłówkach
  t = t.replace(/(^#{1,6} .*)(?!\n\n)/gm, "$1\n");

  // Admonitions: wymuś pustą linię po nagłówku i przed/po
  t = t.replace(/(^|\n)!!! +([a-z]+)([^\n]*)\n(?!\n)/gi, (_m, a, b, c) => `${a}!!! ${b}${c}\n\n`);
  t = t.replace(/(^!!! .+?\n)(.+?)(\n\n(?=^#{1,6} |\Z))/gms, (m, a, body, end) => {
    return a + body.replace(/\n{3,}/g, "\n\n") + end;
  });

  // Kod: domknij niedomknięte bloki ``` (ostrożnie)
  const triples = (t.match(/```/g) || []).length;
  if (triples % 2 === 1) t += "\n```\n";

  // Mermaid/OTUI: wymuś fenced blocks
  t = t.replace(/(^|\n)``` *mermaid( *\n)?/g, "\n```mermaid\n");
  t = t.replace(/(^|\n)``` *otui( *\n)?/g, "\n```otui\n");

  // Pusta linia przed/po blokiem kodu
  t = t.replace(/([^\n])\n```/g, "$1\n\n```");
  t = t.replace(/```\n([^\n])/g, "```\n\n$1");

  await fs.writeFile(f, t);
  console.log("fixed:", f);
}
