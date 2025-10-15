
"""
A minimal MyST/Markdown chunker: splits by ATX headings (#+), preserves fences,
respects max_chars and overlap. Designed for docs/authoring RAG prep.
"""
from __future__ import annotations
import re, os, pathlib
from typing import List

HEADING = re.compile(r'^(#{1,6})\s+.*')

def chunk_text(text: str, max_chars: int = 6000, overlap: int = 400) -> List[str]:
    lines = text.splitlines()
    chunks, cur = [], []
    cur_len = 0
    fence = None
    for ln in lines:
        if ln.strip().startswith("```"):
            fence = None if fence else "```"
        cur.append(ln)
        cur_len += len(ln) + 1
        if fence is None and HEADING.match(ln) and cur_len >= max_chars:
            chunks.append("\n".join(cur))
            cur = cur[-overlap//2:]
            cur_len = sum(len(x)+1 for x in cur)
    if cur:
        chunks.append("\n".join(cur))
    return chunks

def save_chunks(src_path: str, out_dir: str, max_chars=6000, overlap=400):
    os.makedirs(out_dir, exist_ok=True)
    txt = pathlib.Path(src_path).read_text(encoding="utf-8")
    ch = chunk_text(txt, max_chars, overlap)
    base = pathlib.Path(src_path).stem
    for i, c in enumerate(ch, 1):
        (pathlib.Path(out_dir) / f"{base}.part{i:03d}.md").write_text(c, encoding="utf-8")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: rag_chunker.py <src.md> <out_dir> [max_chars] [overlap]")
        raise SystemExit(2)
    src, out = sys.argv[1], sys.argv[2]
    maxc = int(sys.argv[3]) if len(sys.argv) > 3 else 6000
    over = int(sys.argv[4]) if len(sys.argv) > 4 else 400
    save_chunks(src, out, maxc, over)
