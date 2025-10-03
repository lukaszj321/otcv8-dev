#!/usr/bin/env node
// Użycie: node scripts/normalize-md.mjs OTCv8-Docs.md
import fs from 'fs';

const inFile = process.argv[2];
if (!inFile) { console.error('Użycie: node scripts/normalize-md.mjs IN.md'); process.exit(1); }
let src = fs.readFileSync(inFile, 'utf8');

// 1) Sklej linie rozbite na litery (np. "p\nr\no\nj\ne\nk\nt")
src = src.replace(/(^|\n)([A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź])\n(?=[A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź](\n|$))/g, '$1$2'); // usuń pionowe łamania
src = src.replace(/([A-Za-zĄąĆćĘęŁłŃńÓóŚśŻżŹź])\n(?!\n)/g, '$1 '); // pojedyncze \n -> spacja (w akapitach)

// 2) Złącz nagłówki ATX na jedną linię
src = src.replace(/^(#{1,6})\s+([^\n]+)\n(?!\n)/gm, (m, h, t) => `${h} ${t.trim()}\n`);

// 3) Usuń twarde łamania w tytułach typu "Architektura (\\nskrót)"
src = src.replace(/^(#{1,6}\s+[^\n]+)\n([^\n]+)$/gm, (m, a, b) => `${a} ${b}`);

// 4) Oczyść wielokrotne puste linie
src = src.replace(/\n{3,}/g, '\n\n');

fs.writeFileSync(inFile, src, 'utf8');
console.log('normalize-md: OK ->', inFile);
