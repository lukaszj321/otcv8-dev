// Generuje embeddings bez kluczy → zapis do docs/rag/embeddings.json
import { pipeline } from '@xenova/transformers';
import { glob } from 'glob';
import fs from 'fs/promises';

const stripFM = (t) => t.replace(/^---[\s\S]*?---\n/, '');
const chunk = (s, n = 1200) => { const o=[]; for (let i=0;i<s.length;i+=n) o.push(s.slice(i,i+n)); return o; };

const files = await glob('docs/**/*.md', { ignore: ['docs/rag/**'] });

// model działa offline (WASM) – bez żadnego API
const extractor = await pipeline('feature-extraction', 'Xenova/all-MiniLM-L6-v2');

const out = [];
for (const path of files) {
  const raw = await fs.readFile(path, 'utf8');
  for (const [idx, text] of chunk(stripFM(raw)).entries()) {
    const vec = await extractor(text, { pooling: 'mean', normalize: true });
    out.push({ path, idx, text, embedding: Array.from(vec.data) });
  }
}

await fs.mkdir('docs/rag', { recursive: true });
await fs.writeFile('docs/rag/embeddings.json', JSON.stringify(out));
console.log('OK -> docs/rag/embeddings.json | chunks:', out.length);
