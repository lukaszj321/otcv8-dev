import { OpenAI } from "openai";
import { glob } from "glob";
import fs from "fs/promises";

// proste cięcie na kawałki
const chunk = (s, n = 1200) => {
  const parts = [];
  for (let i = 0; i < s.length; i += n) parts.push(s.slice(i, i + n));
  return parts;
};

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const files = await glob("docs/**/*.md", { ignore: ["docs/_rag/**"] });
const out = [];

for (const path of files) {
  const raw = await fs.readFile(path, "utf8");
  // wywal proste front-mattery jeśli kiedyś dodasz
  const content = raw.replace(/^---[\s\S]*?---\n/, "");
  const chunks = chunk(content);

  for (let i = 0; i < chunks.length; i++) {
    const text = chunks[i];
    const emb = await openai.embeddings.create({
      model: "text-embedding-3-small",
      input: text
    });
    out.push({
      path,
      idx: i,
      embedding: emb.data[0].embedding,
      text
    });
  }
}

await fs.mkdir("docs/_rag", { recursive: true });
await fs.writeFile("docs/_rag/embeddings.json", JSON.stringify(out));
console.log("OK -> docs/_rag/embeddings.json");
