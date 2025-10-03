#!/usr/bin/env node
// Składa połamane nagłówki/akapity przed Pandoc (DOCX/EPUB)
import fs from "fs";
const f = process.argv[2];
if (!f) { console.error("Użycie: node scripts/normalize-md.mjs IN.md"); process.exit(1); }
let t = fs.readFileSync(f, "utf8");

// litery w pionie → sklej
t = t.replace(/(^|\n)([A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź])\n(?=[A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź](\n|$))/g, "$1$2");
t = t.replace(/([A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź])\n(?!\n)/g, "$1 ");

// nagłówki ATX na jedną linię
t = t.replace(/(^#{1,6})\s+([^\n]+)\n(?!\n)/gm, "$1 $2\n");

// domknij fence
if (((t.match(/```/g)||[]).length % 2)===1) t += "\n```\n";

fs.writeFileSync(f, t, "utf8");
console.log("normalize-md: OK");
