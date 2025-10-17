---
title: 03 — RAG Datasets (Authoring Plan)
purpose: Build clean RAG-friendly corpora from chapter sources, with consistent metadata and facet IDs.
scope: "docs/authoring/**"
constraints:
  - GH Actions only, no network
  - Store outputs as CSV/JSON alongside chapter datasets

schema:
  chunking:
    - unit: section/paragraph/codeblock
    - max_chars: 1200
    - overlap: 120
  metadata:
    - chapter          # e.g., "02_events"
    - facet_id         # "<chapter>.<stem>"
    - source_path      # .md/.otui/.lua/.h/.cpp
    - title            # section title if available
    - tags             # JSON array in CSV cell (e.g. ["ui","events"])
    - lang             # "pl" / "en"
    - hash             # sha1 of content
  files:
    - rag_chunks.csv: ["id","chapter","facet_id","title","lang","source_path","start","end","text","hash","tags"]
    - rag_index.json: # list of objects
        - "id"
        - "facet_id"
        - "source_path"
        - "title"
        - "tags"
        - "hash"

outputs:
  - "docs/authoring/<chapter>/datasets/rag_chunks.csv"
  - "docs/authoring/_data/rag_index.json"

placement:
  - Per chapter: "docs/authoring/<chapter>/datasets/rag_chunks.csv"
  - Global index (optional): "docs/authoring/_data/rag_index.json"

acceptance:
  - [ ] rag_chunks.csv exists in chapters with real content
  - [ ] facet_id matches stems used by CSV/diagrams
  - [ ] tags serialized as JSON arrays in CSV
  - [ ] No PII or secrets (basic scrubbing rules applied)
