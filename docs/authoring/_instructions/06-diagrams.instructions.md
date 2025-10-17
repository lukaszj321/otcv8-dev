---

title: 06 — Diagrams Authoring
purpose: Unify diagram style and interactivity across chapters.
rules:

# Inject EXACTLY as the first line inside each Mermaid block (no quotes)

mermaid_init: %%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
theme: neutral
background: transparent
ids: CamelCase of stem or semantic id (e.g., WidgetsHierarchy)

# Works only for flowchart/graph; NOT supported in sequenceDiagram

click_anchor: click <ID> "./index.html#facet-<chapter>.<stem>" "Open <stem>"
store_under: docs/authoring/<chapter>/diagrams/*.mmd
include_in_index: MyST `{mermaid}` blocks (not PNG)
templates:
graph:
file: graph_template.mmd
body: |
%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph LR
UI[Dashboard (SPA)] -->|handshake (JWT/token)| WS[(WebSocket)]
WS -->|connect| S[Server (Node)]
S -->|events: metrics, logs, char_info| UI
UI -->|cmd: START/STOP, settings| S

```
    click UI "./index.html#facet-06.UI" "Open UI"
    click WS "./index.html#facet-06.WS" "Open WS"
    click S  "./index.html#facet-06.Server" "Open Server"
```

sequence:
file: sequence_template.mmd
body: |
%%{init: {'theme':'neutral','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
sequenceDiagram
participant UI as Dashboard (SPA)
participant WS as WebSocket (wss)
participant S as Server (Node)

```
    UI->>WS: handshake (JWT / token)
    WS->>S: connect
    S-->>UI: events: metrics, logs, char_info
    UI->>S: cmd: START/STOP, settings
```

qa:

* Check the first line starts with %%{init: ...}%% or add it
* Do NOT attempt `click` in sequenceDiagram (unsupported)
* Ensure at least one click anchor in flowcharts if matching CSV facet exists
