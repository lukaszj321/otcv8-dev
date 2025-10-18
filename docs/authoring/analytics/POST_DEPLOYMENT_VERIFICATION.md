# Post-Deployment Verification Guide

This guide explains how to verify the Mermaid rendering fix after the PR is merged and GitHub Pages is deployed.

## Prerequisites

- PR must be merged to `main` branch
- GitHub Actions workflow must complete successfully
- GitHub Pages must redeploy (usually 2-5 minutes after merge)

## Verification Steps

### 1. Wait for Deployment

After merging the PR, monitor the GitHub Actions workflow:

1. Go to: https://github.com/lukaszj321/otcv8-dev/actions
2. Look for the latest "Build & Deploy Docs (Sphinx)" workflow run
3. Wait for it to show ✅ (green checkmark)
4. Wait an additional 1-2 minutes for Pages to update

### 2. Verify Live Pages

Visit these three pages and verify diagrams render correctly:

**Chapter 09 - Logging:**
- URL: https://lukaszj321.github.io/otcv8-dev/authoring/09_logging/index.html
- Expected: 2 interactive Mermaid diagrams (logging_architecture and logging_flow)
- Verify:
  - [ ] Diagrams are SVG (not code blocks)
  - [ ] Dark theme applied
  - [ ] Click on diagram nodes works (links to facets)

**Chapter 03 - Modules:**
- URL: https://lukaszj321.github.io/otcv8-dev/authoring/03_modules/index.html
- Expected: 2 interactive Mermaid diagrams (module_dependencies and lua_cpp_binding_flow)
- Verify:
  - [ ] Diagrams are SVG (not code blocks)
  - [ ] Dark theme applied
  - [ ] Click on diagram nodes works

**Chapter 06 - Assets:**
- URL: https://lukaszj321.github.io/otcv8-dev/authoring/06_assets/index.html
- Expected: 2 inline Mermaid diagrams (Asset Pipeline Flowchart and Texture Loading Sequence)
- Verify:
  - [ ] Diagrams are SVG (not code blocks)
  - [ ] Dark theme applied
  - [ ] Flowchart and sequence diagram both render

### 3. Capture Screenshots

For each of the 3 pages above:

1. **Full page screenshot**: Showing the entire page with diagrams visible
2. **Diagram close-up**: Zoomed view of one diagram showing interactivity
3. **Click interaction** (if possible): Screenshot showing tooltip/highlight when hovering over clickable nodes

#### Recommended Tool: Browser DevTools

```
1. Open the page
2. Press F12 to open DevTools
3. Press Ctrl+Shift+P (or Cmd+Shift+P on Mac)
4. Type "screenshot" and select "Capture full size screenshot"
5. Save with descriptive name: e.g., "09_logging_diagrams_working.png"
```

#### Alternative: Manual Screenshots

- Windows: Snipping Tool or Win+Shift+S
- Mac: Cmd+Shift+4
- Linux: gnome-screenshot or flameshot

### 4. Verify _sources

Check that Sphinx `_sources` files also have correct formatting:

1. Navigate to: https://lukaszj321.github.io/otcv8-dev/_sources/authoring/09_logging/index.md.txt
2. Search for "```{mermaid}" (Ctrl+F)
3. Verify: The directive starts at the beginning of the line (column 0), no spaces before the backticks

Expected (correct):
```
```{mermaid}
:caption: Logger architecture
:file: ./diagrams/logging_architecture.mmd
```
```

**NOT** (incorrect - this was the bug):
```

```{mermaid}
    :caption: Logger architecture
    :file: ./diagrams/logging_architecture.mmd
```
```

Repeat for the other 2 chapters:
- https://lukaszj321.github.io/otcv8-dev/_sources/authoring/03_modules/index.md.txt
- https://lukaszj321.github.io/otcv8-dev/_sources/authoring/06_assets/index.md.txt

### 5. Test Click Handlers (Optional)

On each page, try clicking on diagram elements (nodes, boxes):

1. Hover over a node in a flowchart diagram
2. Look for cursor change (should become pointer/hand)
3. Click the node
4. Verify: Page scrolls to the facet section OR opens the referenced page

Example: In `09_logging/index.html`, clicking on "Logger" node should jump to the `facet-09_logging.architecture` anchor.

### 6. Report Results

After verification, post a comment on the original issue with:

1. **Status**: ✅ VERIFIED or ❌ ISSUES FOUND
2. **Screenshots**: Attach the 3 (or more) screenshots
3. **URLs tested**: List the 3 pages verified
4. **Notes**: Any observations or issues

#### Example Comment Template

```markdown
## Live Verification Results

**Status:** ✅ VERIFIED

### Screenshots

![09_logging diagrams](09_logging_diagrams_working.png)
![03_modules diagrams](03_modules_diagrams_working.png)
![06_assets diagrams](06_assets_diagrams_working.png)

### Pages Tested

- ✅ https://lukaszj321.github.io/otcv8-dev/authoring/09_logging/index.html
- ✅ https://lukaszj321.github.io/otcv8-dev/authoring/03_modules/index.html
- ✅ https://lukaszj321.github.io/otcv8-dev/authoring/06_assets/index.html

### Observations

- All Mermaid diagrams render as interactive SVG
- Dark theme applied correctly
- Click handlers work on flowchart nodes
- _sources files show no indentation

**Issue resolved! 🎉**
```

## Troubleshooting

### Issue: Diagrams still render as code blocks

**Possible causes:**
1. Browser cache - Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
2. GitHub Pages not updated yet - Wait 5 more minutes and retry
3. Changes not merged - Verify PR is merged and workflow succeeded

### Issue: 404 errors on pages

**Possible causes:**
1. GitHub Pages still deploying - Wait and retry
2. URL typo - Double-check the URLs above

### Issue: Click handlers don't work

**Possible causes:**
1. This is expected for sequence diagrams (they don't support click)
2. Only flowcharts (graph TD/LR) have click handlers
3. Browser JavaScript disabled - Enable JavaScript

## Success Criteria

The fix is successful when:

- [x] All 3 pages load without errors
- [x] All Mermaid diagrams render as SVG (not code blocks)
- [x] Dark theme is applied to diagrams
- [x] _sources files have no indentation before `{mermaid}`
- [x] Screenshots captured and attached to issue

## Next Steps After Verification

1. Close the original issue with a reference to this verification
2. Update the issue with the "fixed" label
3. Celebrate! 🎉

---

**Note:** This verification guide is part of the complete solution documented in:
- [SOLUTION_SUMMARY.md](SOLUTION_SUMMARY.md)
- [index_indentation_root_cause.md](index_indentation_root_cause.md)
- [qa_summary.md](../qa/qa_summary.md)
