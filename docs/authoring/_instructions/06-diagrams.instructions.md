
---
title: 06 — Diagrams Authoring
purpose: Unify diagram style and interactivity across chapters.
rules:
  mermaid_init: "%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%"
  theme: neutral
  background: transparent
  ids: CamelCase of stem or semantic id (e.g., WidgetsHierarchy)
  click_anchor: 'click <ID> "./index.html#facet-<chapter>.<stem>" "Open <stem>"'
  store_under: docs/authoring/<chapter>/diagrams/*.mmd
  include_in_index: MyST ```{mermaid}``` blocks (not PNG)
templates:
  graph:
    file: graph_template.mmd
    body: |
      graph TD
        A[Source] --> B[Dataset]
  sequence:
    file: sequence_template.mmd
    body: |
      sequenceDiagram
        participant C as Client
        participant S as Server
        C->>S: Request
        S->>C: Response
qa:
  - Check the first line starts with %%{init: ...}%% or add it
  - Ensure at least one click anchor if matching CSV facet exists
