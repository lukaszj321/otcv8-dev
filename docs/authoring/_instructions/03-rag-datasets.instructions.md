---
title: "03 — RAG Datasets (Authoring Plan)"
purpose: "Build clean RAG-friendly corpora from chapter sources, with consistent metadata and facet IDs."
scope: "docs/authoring/**"
constraints:
  - "GH Actions only, no network"
  - "Store outputs as CSV/JSON alongside chapter datasets"
  - "UTF-8, LF"
  - 'CSV dialect: delimiter=",", quotechar:"\"", escape=double'

schema:
  chunking:
    unit: ["section","paragraph","codeblock"]
    max_chars: 1200
    overlap: 120
  normalize:
    - strip_trailing_whitespace
    - collapse_multispaces
    - preserve_code_blocks
  metadata: ["chapter","facet_id","source_path","title","tags","lang","hash"]
  files:
    rag_chunks.csv: ["id","chapter","facet_id","title","lang","source_path","start","end","text","hash","tags"]
    rag_index.json:
      - id
      - facet_id
      - source_path
      - title
      - tags
      - hash

outputs:
  - "docs/authoring/<chapter>/datasets/rag_chunks.csv"
  - "docs/authoring/_data/rag_index.json"

placement:
  per_chapter: "docs/authoring/<chapter>/datasets/rag_chunks.csv"
  global_index: "docs/authoring/_data/rag_index.json"

rules:
  - "id unique per chapter (chapter-local monotonic or hash-based)"
  - "start/end are byte offsets in UTF-8 of `text` within source"
  - 'tags serialized as JSON arrays in CSV (e.g., ["ui","events"])'
  - "deduplicate identical chunks by `hash` in global index"

acceptance:
  - "rag_chunks.csv exists in chapters with real content"
  - "facet_id matches stems used by CSV/diagrams"
  - "tags serialized as JSON arrays in CSV"
  - "No PII or secrets (basic scrubbing rules applied)"
  - "rag_index.json builds and has no duplicate hashes"
---

# 03 — RAG Datasets

## Embedy do `index.md`

```{warning}
Missing CSV file: `./datasets/rag_chunks.csv`

Either add the dataset or update the directive.
```

## Przykładowy rekord (CSV)

```csv
id,chapter,facet_id,title,lang,source_path,start,end,text,hash,tags
11_data:img001,11_data,11_data.images,"Images index","pl","docs/authoring/11_data/index.md",0,512,"...",c0ffee...,["ui","assets"]
```

## Facet anchor (MyST)

(facet-11_data.images)=
### Facet: `11_data.images`
