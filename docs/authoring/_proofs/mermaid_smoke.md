# Mermaid Smoke Test

This page verifies that Mermaid diagrams render correctly in the built documentation.

## Test 1: Simple Graph

```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
graph TD
    A[Start] --> B[Process]
    B --> C[End]
```

## Test 2: Sequence Diagram

```{mermaid}
%%{init: {'theme':'neutral'}}%%
sequenceDiagram
    participant Client
    participant Server
    Client->>Server: Request
    Server-->>Client: Response
```

## Test 3: Flowchart with Click

```{mermaid}
%%{init: {'theme':'dark','securityLevel':'loose'}}%%
flowchart TD
    Start[Start] --> Process[Process Data]
    Process --> Decision{Success?}
    Decision -->|Yes| Success[Complete]
    Decision -->|No| Error[Handle Error]
    click Process "./index.html#test" "Click to test"
```

## Verification Checklist

When viewing this page in the built HTML:

- [ ] Test 1 displays as an interactive diagram (not code)
- [ ] Test 2 displays as a sequence diagram (not code)
- [ ] Test 3 displays as a flowchart with clickable elements (not code)
- [ ] Browser console shows no Mermaid errors
- [ ] Page source includes `<script>` tag loading Mermaid
- [ ] `_static/` directory contains Mermaid assets

## Expected HTML Indicators

In the built `_build/html/_proofs/mermaid_smoke.html`:

1. Look for `<div class="mermaid">` elements (not `<pre><code>`)
2. Check that `_static/` includes mermaid JS files
3. Verify no syntax errors in browser console
4. Confirm SVG rendering (inspect element shows `<svg>` tags)

## Live Deployment Proof

After deployment to GitHub Pages:

- URL: `https://lukaszj321.github.io/otcv8-dev/authoring/_proofs/mermaid_smoke.html`
- Screenshot location: `docs/authoring/_proofs/screenshots/`
