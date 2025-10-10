#!/usr/bin/env python
import argparse, json
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True)
    ap.add_argument("--meta", required=True)
    ap.add_argument("--q", required=True)
    ap.add_argument("--k", type=int, default=5)
    args = ap.parse_args()

    import faiss
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    qv = model.encode([args.q], convert_to_numpy=True, normalize_embeddings=True)
    index = faiss.read_index(args.index)
    D, I = index.search(qv, args.k)
    meta = json.load(open(args.meta, "r", encoding="utf-8"))["metas"]

    print("=== WYNIKI ===")
    for rank, (score, idx) in enumerate(zip(D[0], I[0]), start=1):
        m = meta[int(idx)]
        print(f"[{rank}] score={float(score):.3f}  ->  {m['path']}")

if __name__ == "__main__":
    main()
