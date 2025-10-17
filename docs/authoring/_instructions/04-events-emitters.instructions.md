---
title: 04 — Events & Emitters (Authoring Plan)
purpose: Document event streams, sources, handlers, payloads; embed matrices and sequence diagrams.
chapter: "docs/authoring/02_events"
constraints:
  - "Outputs under docs/authoring/02_events/**"
  - "Use MyST {csv-table} and {mermaid}"

outputs:
  - "docs/authoring/02_events/datasets/events_matrix.csv"
  - "docs/authoring/02_events/datasets/emitters.csv"
  - "docs/authoring/02_events/datasets/handlers.csv"
  - "docs/authoring/02_events/diagrams/event_flow.mmd"
  - "docs/authoring/02_events/index.md"

datasets:
  - file: events_matrix.csv
    header: ["id","ts","source","event","payload_schema","handlers","notes"]
  - file: emitters.csv
    header: ["emitter","event","args","notes"]
  - file: handlers.csv
    header: ["handler","event","callback","threading","notes"]

diagrams:
  style:
    mermaid_init: "%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%"
    first_line_required: true
  files:
    - file: event_flow.mmd
      desc: Typical client lifecycle (sequenceDiagram)
      # Uwaga: sequenceDiagram bez click
      template: |
        %%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
        sequenceDiagram
          participant C as Client
          participant S as Server
          C->>S: Login request
          S-->>C: Characters list

index.must_embed:
  - "datasets/events_matrix.csv via {csv-table}"
  - "diagrams/event_flow.mmd via {mermaid}"
  - "Appendix/Facets"

acceptance:
  - [ ] events_matrix.csv present and non-empty
  - [ ] event_flow.mmd renders (init in 1st line, ASCII arrows)
  - [ ] Facet anchors present in index.md (e.g., facet-02_events.event_flow)
