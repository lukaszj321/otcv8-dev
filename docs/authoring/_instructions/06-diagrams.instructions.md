---
title: "06 — Diagrams Authoring"
purpose: "Unify diagram style and interactivity across chapters."
rules:
  mermaid_init: "%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%"
  first_line_required: true
  ascii_arrows_only: true
  theme: "neutral"
  background: "transparent"
  ids: "CamelCase of stem or semantic id (e.g., WidgetsHierarchy)"
  click_anchor: 'click <ID> "./index.html#facet-<chapter>.<stem>" "Open <stem>"'
  store_under: "docs/authoring/<chapter>/diagrams/*.mmd"
  include_in_index: "MyST {mermaid} blocks (not PNG)"

templates:
  graph:
    file: "graph_template.mmd"
    body: |
      %%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
      graph LR
        UI[Dashboard (SPA)] -->|handshake (JWT/token)| WS[(WebSocket)]
        WS -->|connect| S[Server (Node)]
        S -->|events: metrics, logs, char_info| UI
        UI -->|cmd: START/STOP, settings| S

      click UI "./index.html#facet-06.UI" "Open UI"
      click WS "./index.html#facet-06.WS" "Open WS"
      click S "./index.html#facet-06.Server" "Open Server"

  sequence:
    file: "sequence_template.mmd"
    body: |
      %%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
      sequenceDiagram
        participant UI as Dashboard (SPA)
        participant WS as WebSocket (wss)
        participant S as Server (Node)

        UI->>WS: handshake (JWT / token)
        WS->>S: connect
        S-->>UI: events: metrics, logs, char_info
        UI->>S: cmd: START/STOP, settings

acceptance:
  - "[ ] First line is `%%{init: ...}%%`"
  - "[ ] No `click` in `sequenceDiagram`"
  - "[ ] Flowcharts have at least one valid `click` (if facet exists)"

## IPC

**Kanały IPC (Studio/Electron)**

- "studio:diagrams.validate" — walidacja bloków Mermaid w rozdziale; sprawdza `init` i klikalne kotwice.
- "studio:diagrams.scan" — skan `diagrams/*.mmd` i raport spójności (theme, background, ids).
- "studio:diagrams.open" `{ id | file }` — otwiera diagram w podglądzie Studio.

## Sanity

- "[ ] Pierwsza linia każdego diagramu zawiera `%%{init: ...}%%` z `theme: neutral` i transparentnym tłem."
- "[ ] W `sequenceDiagram` nie używamy `click` (tylko w `graph`/`flowchart`)."
- "[ ] Flowcharty posiadają co najmniej jeden `click` do istniejącego facetu (jeśli facet istnieje)."
- "[ ] Pliki zapisane w `docs/authoring/<chapter>/diagrams/*.mmd` i włączone jako bloki `{mermaid}` w tekście."
---
