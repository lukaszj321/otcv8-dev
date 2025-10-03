// RAG bez API: generuje wektory i zapisuje do docs/rag/embeddings.json
import { pipeline } from '@xenova/transformers';
import { glob } from 'glob';
import fs from 'fs/promises';

function chunkText(s, n = 1200) { const out=[]; for (let i=0;i<s.length;i+=n) out.push(s.slice(i,i+n)); return out; }
const stripFM = (t) => t.replace(/^---[\s\S]*?---\n/, '');

const files = await glob('docs/**/*.md', { ignore: ['docs/rag/**'] });
const extractor = await pipeline('feature-extraction', 'Xenova/all-MiniLM-L6-v2');

const results = [];
for (const path of files) {
  const raw = await fs.readFile(path, 'utf8');
  for (const [i, text] of chunkText(stripFM(raw)).entries()) {
    const emb = await extractor(text, { pooling: 'mean', normalize: true });
    results.push({ path, idx: i, text, embedding: Array.from(emb.data) });
  }
}

await fs.mkdir('docs/rag', { recursive: true });
await fs.writeFile('docs/rag/embeddings.json', JSON.stringify(results));
console.log('OK -> docs/rag/embeddings.json');
