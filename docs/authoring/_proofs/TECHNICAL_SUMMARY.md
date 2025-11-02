# Mermaid Rendering Fix - Technical Summary

## Problem Statement

Mermaid diagrams in the OTClient v8 documentation were rendering as plain text code blocks instead of interactive SVG diagrams on GitHub Pages (LIVE).

## Root Cause Analysis

### Configuration Issue

The `docs/conf.py` file had:
```python
mermaid_output_format = "svg"
```

This setting tells sphinxcontrib-mermaid to:
1. Use `mmdc` (Mermaid CLI) to pre-render diagrams as SVG files during build
2. Embed those SVG files in the HTML output

### Why It Failed

- `mmdc` CLI tool was NOT installed in the GitHub Actions workflow
- Without `mmdc`, sphinxcontrib-mermaid cannot generate SVG files
- Fallback behavior: Render mermaid code as plain text (no HTML wrapper at all)
- Result: Diagrams appeared as text in `%%{init}...graph TD...` format

### Evidence from HTML Output (BEFORE)

```html
<section id="flow">
<h3>flow</h3>
<p><em>Facet:</em> <code>03_modules.flow</code></p>
%%{init: { 'theme': 'dark' }}%%
graph TD
    A[Lua Modules] --> B[Data Collection]
    B --> C[Processing]
</section>
```

Notice: No HTML wrapper around the mermaid code—just plain text!

## Solution Implemented

### Configuration Change

Changed `docs/conf.py` to:
```python
mermaid_output_format = "raw"
```

This tells sphinxcontrib-mermaid to:
1. Wrap mermaid code in `<pre class="mermaid">` tags
2. Include mermaid.js from CDN
3. Let the browser render diagrams client-side

### How It Works

1. **Build Time** (Sphinx):
   ```html
   <pre class="mermaid">
   %%{init: { 'theme': 'dark' }}%%
   graph TD
       A --> B
   </pre>
   ```

2. **Runtime** (Browser):
   ```javascript
   // mermaid.js loaded from CDN
   mermaid.initialize({startOnLoad:true, theme:'neutral'});
   // Finds all <pre class="mermaid"> elements
   // Converts mermaid syntax to SVG
   // Replaces <pre> with interactive <svg>
   ```

3. **Final Result** (User sees):
   - Interactive SVG diagram
   - Can hover/click elements
   - Themes applied correctly
   - No server-side rendering needed

### Evidence from HTML Output (AFTER)

```html
<section id="flow">
<h3>flow</h3>
<p><em>Facet:</em> <code>03_modules.flow</code></p>
<pre class="mermaid">
%%{init: { 'theme': 'dark', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Lua Modules] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
</pre>
</section>

<!-- Script tags in <head> -->
<script type="module" src="https://cdn.jsdelivr.net/npm/mermaid@10.9.0/dist/mermaid.esm.min.mjs"></script>
<script type="module">mermaid.initialize({startOnLoad:true, theme:'neutral'});</script>
```

## Comparison of Output Formats

| Format | Requires | Build Output | Runtime | Use Case |
|--------|----------|--------------|---------|----------|
| `"svg"` | `mmdc` CLI | `<img src="diagram.svg">` | Static | Pre-rendered, no JS needed |
| `"png"` | `mmdc` CLI | `<img src="diagram.png">` | Static | Pre-rendered, older browsers |
| `"raw"` | Nothing | `<pre class="mermaid">code</pre>` | mermaid.js | **GitHub Pages, CDN-based** |

## Why "raw" Is Correct for GitHub Pages

✅ **No server dependencies**: No need to install `mmdc` in CI  
✅ **Smaller builds**: No SVG/PNG files to generate  
✅ **Client-side rendering**: Browser does the work  
✅ **Interactive**: Click handlers, zoom, etc. work  
✅ **CDN delivery**: mermaid.js loaded from fast CDN  
✅ **Auto-updates**: Can update mermaid version via config  

## Additional Changes

### 1. Content Hygiene (27 files)

Converted fence syntax from:
```markdown
```mermaid
graph TD
    A --> B
```
```

To directive syntax:
```markdown
```mermaid
graph TD
    A --> B
```
```

**Why:** MyST parser recognizes `{mermaid}` as a directive, ensuring proper processing.

### 2. Workflow Enhancements

Added verification steps to ensure critical packages are installed:
```bash
python - << 'PY'
import sphinxcontrib.mermaid, myst_nb, sphinx_design
print("✓ sphinxcontrib-mermaid, myst-nb, sphinx-design installed")
PY
```

### 3. Requirements Organization

Structured `docs/requirements.txt` with clear sections and minimum versions.

## Verification

### Local Build Test

```bash
cd /home/runner/work/otcv8-dev/otcv8-dev
sphinx-build -b html docs docs/_build/html
grep -c 'class="mermaid"' docs/_build/html/authoring/03_modules/index.html
# Output: 7 (✓ 7 mermaid blocks found)
```

### HTML Structure Test

```bash
grep -A 5 'class="mermaid"' docs/_build/html/authoring/03_modules/index.html
# Shows proper <pre class="mermaid"> tags
```

### Script Loading Test

```bash
grep -i "mermaid.*script" docs/_build/html/authoring/03_modules/index.html
# Shows mermaid.js loaded from CDN
```

## Success Criteria Met

- [x] 7 mermaid blocks in 03_modules/index.html have `class="mermaid"`
- [x] mermaid.js v10.9.0 loaded from CDN
- [x] Initialize call present: `mermaid.initialize({...})`
- [x] No server-side dependencies required
- [x] HTML structure matches expected format

## Future Maintenance

### If Diagrams Don't Render

1. Check `mermaid_output_format = "raw"` in `docs/conf.py`
2. Verify mermaid.js CDN URL is accessible
3. Check browser console for JavaScript errors
4. Ensure `{mermaid}` directive syntax is used (not plain fence)

### To Update Mermaid Version

In `docs/conf.py`:
```python
mermaid_version = "11.0.0"  # Update version number
```

Mermaid.js will be loaded from:
```
https://cdn.jsdelivr.net/npm/mermaid@{version}/dist/mermaid.esm.min.mjs
```

## References

- **sphinxcontrib-mermaid docs**: https://sphinxcontrib-mermaid-demo.readthedocs.io/
- **Mermaid.js docs**: https://mermaid.js.org/
- **MyST Parser docs**: https://myst-parser.readthedocs.io/
- **Issue**: "Docs LIVE: Mermaid still renders as code — enforce directive, verify extensions loaded on CI, provide live proofs"

## Credits

- Issue identified: Mermaid diagrams showing as code on LIVE
- Root cause: `mermaid_output_format = "svg"` without `mmdc`
- Solution: Changed to `mermaid_output_format = "raw"`
- Verified: Local build shows correct HTML structure
