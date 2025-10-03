// RAG bez API: generuje wektory z @xenova/transformers (WASM)
// Zapis: docs/_rag/embeddings.json

import { pipeline } from '@xenova/transformers';
import { glob } from 'glob';
import fs from 'fs/promises';

// proste cięcie na ~1200 znaków
function chunkText(s, n = 1200) {
  const out = [];
  for (let i = 0; i < s.length; i += n) out.push(s.slice(i, i + n));
  return out;
}

// usuń ewentualny front-matter `---`
const stripFM = (t) => t.replace(/^---[\s\S]*?---\n/, '');

const files = await glob('docs/**/*.md', { ignore: ['docs/_rag/**'] });

// model bez klucza, pobierany automatycznie z HF
const extractor = await pipeline('feature-extraction', 'Xenova/all-MiniLM-L6-v2');

const results = [];
for (const path of files) {
  const raw = await fs.readFile(path, 'utf8');
  const chunks = chunkText(stripFM(raw));
  for (let i = 0; i < chunks.length; i++) {
    const text = chunks[i];
    const emb = await extractor(text, { pooling: 'mean', normalize: true });
    results.push({
      path,
      idx: i,
      text,
      embedding: Array.from(emb.data) // Float32Array -> JSON
    });
  }
}

await fs.mkdir('docs/_rag', { recursive: true });
await fs.writeFile('docs/_rag/embeddings.json', JSON.stringify(results));
console.log('OK -> docs/_rag/embeddings.json');
