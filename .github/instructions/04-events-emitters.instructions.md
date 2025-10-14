
---
title: 04 — Events & Emitters (Authoring Plan)
purpose: Document event streams, sources, handlers, payloads; embed matrices and sequence diagrams.
chapter: docs/authoring/02_events
constraints:
  - Outputs under docs/authoring/02_events/**
  - Use MyST `{csv-table}` and `{mermaid}`

datasets:
  - file: events_matrix.csv
    header: ["id","ts","source","event","payload_schema","handlers","notes"]
  - file: emitters.csv
    header: ["emitter","event","args","notes"]
  - file: handlers.csv
    header: ["handler","event","callback","threading","notes"]

diagrams:
  style:
    init: "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%"
  files:
    - file: event_flow.mmd
      desc: Typical client lifecycle events (sequenceDiagram)
      must_click: 'click EventFlow "./index.html#facet-02_events.event_flow" "Open event_flow"'
      template: |
        sequenceDiagram
          participant C as Client
          participant S as Server
          C->>S: Login request
          S->>C: Characters list

index.must_embed:
  - datasets/events_matrix.csv via {csv-table}
  - diagrams/event_flow.mmd via {mermaid}
  - Appendix/Facets

acceptance:
  - [ ] events_matrix.csv present and non-empty
  - [ ] event_flow.mmd renders in dark/light
  - [ ] Facets anchors generated
