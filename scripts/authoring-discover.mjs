#!/usr/bin/env node
/**
 * Autoodkrywanie zasobów w docs/reposzablony/szablony/**
 * Tworzy docs/reposzablony/_auto/*_assets.md oraz _auto/toctree.md
 * - CSV -> {csv-table}
 * - Obrazy -> galeria
 * - Mermaid/MMD -> wklejka
 */
import fs from "fs/promises";
import path from "path";
import { glob } from "glob";

const ROOT = "docs/reposzablony";
const SZABLONY = path.join(ROOT, "szablony");
const OUT_DIR = path.join(ROOT, "_auto");

const esc = s => String(s ?? "").replace(/\|/g,"\\|");

async function ensureDir(p){ await fs.mkdir(p, { recursive: true }); }
async function exists(p){ try{ await fs.access(p); return true; } catch { return false; } }

const csvOf = async dir => glob(path.join(dir, "**/*.csv").replace(/\\/g,"/"));
const imgsOf = async dir => glob(path.join(dir, "**/*.{png,jpg,jpeg,svg,gif,webp}").replace(/\\/g,"/"));
const mermaidOf = async dir => glob(path.join(dir, "**/*.{mermaid,mmd}").replace(/\\/g,"/"));
const mdBase = p => path.basename(p).replace(/\.(md|markdown)$/i,"");

(async () => {
  if(!await exists(SZABLONY)) process.exit(0);

  await ensureDir(OUT_DIR);
  const subdirs = new Set(
    (await glob(path.join(SZABLONY, "**/*.md").replace(/\\/g,"/")))
      .map(f => path.dirname(f))
  );
  const toc = [];

  for (const dir of [...subdirs].sort()){
    const relDir = dir.slice(SZABLONY.length+1).replace(/\\/g,"/");
    const name = relDir || "root";
    const outFile = path.join(OUT_DIR, `${name.replace(/\//g,"_")}_assets.md`);
    const lines = [];
    lines.push(`---\ntitle: Auto assets — ${name}\n---\n`);
    lines.push(`# Auto assets — ${name}\n`);

    const csvs = await csvOf(dir);
    const imgs = await imgsOf(dir);
    const mer = await mermaidOf(dir);

    if(csvs.length){
      lines.push("## CSV");
      for(const c of csvs.sort()){
        const rel = path.relative(ROOT, c).replace(/\\/g,"/");
        lines.push(`\n**${esc(path.basename(c))}**\n`);
        lines.push("```{csv-table}");
        lines.push(`:file: ${rel}`);
        lines.push(":header-rows: 1");
        lines.push("```");
      }
      lines.push("");
    }

    if(imgs.length){
      lines.push("## Obrazy");
      for(const i of imgs.sort()){
        const rel = path.relative(ROOT, i).replace(/\\/g,"/");
        lines.push(`![](${rel})`);
      }
      lines.push("");
    }

    if(mer.length){
      lines.push("## Diagramy (Mermaid)");
      for(const m of mer.sort()){
        const code = await fs.readFile(m, "utf8").catch(()=> "");
        if(code.trim()){
          lines.push("```{mermaid}");
          lines.push(code.trim());
          lines.push("```");
        }
      }
      lines.push("");
    }

    if(lines.length<=3) continue; // nic nie znaleziono
    await ensureDir(path.dirname(outFile));
    await fs.writeFile(outFile, lines.join("\n"), "utf8");
    toc.push(`_auto/${path.basename(outFile).replace(/\.md$/,"")}`);
  }

  const TOC_FILE = path.join(OUT_DIR, "toctree.md");
  const body = [
    "# Auto-wygenerowane zasoby",
    "",
    "```{toctree}",
    ":maxdepth: 1",
    ...toc.map(x=>x),
    "```",
    ""
  ].join("\n");
  await fs.writeFile(TOC_FILE, body, "utf8");

  console.log(`[authoring-discover] OK. Autogen: ${toc.length} stron, + toctree.`);
})();
