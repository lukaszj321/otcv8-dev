#!/usr/bin/env python
import argparse, os, json, pathlib, re, sys
from tqdm import tqdm

def read_texts(paths):
    exts = {".md", ".rst", ".txt"}
    files = []
    for p in paths:
        p = pathlib.Path(p)
        if p.is_file() and p.suffix in exts:
            files.append(p)
        elif p.is_dir():
            for f in p.rglob("*"):
                if f.suffix in exts:
                    files.append(f)
    return files

def clean_md(text:str)->str:
    text = re.sub(r"`{1,3}.*?`{1,3}", " ", text, flags=re.S)
    text = re.sub(r"\{.*?\}", " ", text, flags=re.S)  # strip myst attrs
    text = re.sub(r"[#>`*_~\-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paths", nargs="+", required=True)
    ap.add_argument("--out", required=True, help="plik FAISS")
    ap.add_argument("--meta", required=True, help="plik JSON z metadanymi")
    args = ap.parse_args()

    from sentence_transformers import SentenceTransformer
    import faiss
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    files = read_texts(args.paths)
    texts, metas = [], []
    for f in tqdm(files, desc="Czytanie"):
        try:
            t = f.read_text(encoding="utf-8", errors="ignore")
            ct = clean_md(t)
            if not ct:
                continue
            texts.append(ct)
            metas.append({"path": str(f)})
        except Exception as e:
            print("WARN:", f, e, file=sys.stderr)

    if not texts:
        print("Brak tekstów do indeksu")
        sys.exit(1)

    emb = model.encode(texts, show_progress_bar=True, convert_to_numpy=True, normalize_embeddings=True)
    d = emb.shape[1]
    index = faiss.IndexFlatIP(d)
    index.add(emb)

    faiss.write_index(index, args.out)
    pathlib.Path(args.meta).write_text(json.dumps({"metas": metas}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Zapisano: {args.out}, {args.meta}, vlen={len(texts)}")

if __name__ == "__main__":
    main()
