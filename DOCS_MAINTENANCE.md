# Documentation Maintenance Guide

Quick reference for maintaining and extending the OTClient v8 documentation.

## Quick Commands

### Local Development

```bash
# Install dependencies
pip install -r requirements-docs.txt

# Build documentation
sphinx-build -b html docs docs/_build/html

# Live preview with auto-reload
pip install sphinx-autobuild
sphinx-autobuild docs docs/_build/html

# Check links
sphinx-build -b linkcheck docs docs/_build/linkcheck

# Clean build
rm -rf docs/_build && sphinx-build -b html docs docs/_build/html
```

### Working with RAG

```bash
# Install RAG dependencies
pip install -r requirements-rag.txt

# Build RAG index
python tools/rag_index.py \
  --paths docs api modules \
  --out docs/rag/rag_index.faiss \
  --meta docs/rag/rag_meta.json

# Query RAG index
python tools/rag_query.py \
  --index docs/rag/rag_index.faiss \
  --meta docs/rag/rag_meta.json \
  --q "your question here"
```

### Authoring Scripts

```bash
# Generate authoring pages
python scripts/build_authoring_pages.py

# Patch Mermaid diagrams
python scripts/patch_diagrams_clicks.py
```

## Adding New Content

### 1. New Documentation Page

```markdown
---
title: My New Page
---

# My New Page

Content here using MyST markdown...

## See Also

- {doc}`../api/index` - Link to API
- {ref}`my-section` - Link to section
```

### 2. New Module Example

Create file in `docs/workbench/example_my_module.md`:

```markdown
# Example: My Module

Complete example with:
- init.lua implementation
- OTUI interface
- Usage instructions
```

Update `docs/workbench/index.md` toctree:

```markdown
```{toctree}
:maxdepth: 2
:hidden:

template
example_health_monitor
example_my_module

### 3. New Diagram

```markdown
\```{mermaid}
%%{init: {'theme':'dark','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%
flowchart LR
    A[Start] --> B[Process]
    B --> C[End]
\```
```

**Important**: Always include `%%{init: ...}%%` on first line for dark theme.

### 4. New CSV Table

Create CSV in `docs/_data/my_data.csv`:

```csv
name,description,status
Item1,Description 1,Active
Item2,Description 2,Pending
```

Reference in markdown:

```markdown
\```{csv-table} My Data
:header-rows: 1
:file: _data/my_data.csv
:widths: 20, 60, 20
\```
```

## MyST Markdown Cheat Sheet

### Basic Formatting

```markdown
**bold** *italic* `code`
[link](url) {doc}`other-page`
```

### Admonitions

```markdown
:::{admonition} Title
:class: tip|note|warning|danger
Content here
:::

:::{note}
Simple note
:::
```

### Grid Layout

```markdown
:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} Card Title
:link: page
:link-type: doc
:shadow: md
Card content
:::

:::{grid-item-card} Another Card
Content
:::
:::
```

### Code Blocks

```markdown
\```python
def hello():
    print("Hello")
\```

\```{code-block} lua
:linenos:
:emphasize-lines: 2,3

function init()
  -- highlighted line
  -- highlighted line
end
\```
```

### Cross-References

```markdown
# Define anchor
(my-anchor)=
## Section Title

# Reference anchor
{ref}`my-anchor`

# Reference document
{doc}`../path/to/page`
```

## Common Tasks

### Update Main Index

Edit `docs/index.md`:
- Modify grid cards to add/remove sections
- Update toctree to include new pages
- Adjust CSV table references

### Add to Sidebar Navigation

Edit relevant `index.md` file and add to `{toctree}`:

```markdown
```{toctree}
:maxdepth: 2
:caption: Section Name

page1
page2
new_page

### Modify Theme Settings

Edit `docs/conf.py`:

```python
html_theme_options = {
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_with_keys": True,
    # ... more options
}
```

### Add Extension

1. Add to `requirements-docs.txt`:
   ```
   sphinx-new-extension>=1.0.0
   ```

2. Add to `docs/conf.py`:
   ```python
   extensions = [
       # ... existing
       "sphinx_new_extension",
   ]
   ```

## CI/CD Integration

### GitHub Actions Workflow

The workflow `.github/workflows/sphinx-pages.yml` automatically:

1. **Syncs API docs**: Copies `api/*.md` to `docs/api/external/`
2. **Generates authoring pages**: Runs `build_authoring_pages.py`
3. **Patches diagrams**: Runs `patch_diagrams_clicks.py`
4. **Builds Sphinx**: Creates HTML output
5. **Deploys to Pages**: Publishes to GitHub Pages

### Trigger Build

Push to `master` or `main` branch:

```bash
git add .
git commit -m "docs: update documentation"
git push origin main
```

Or manually trigger via GitHub UI:
- Actions → Build & Deploy Docs (Sphinx) → Run workflow

## Troubleshooting

### Build Fails

```bash
# Check dependencies
pip list | grep -i sphinx

# Reinstall
pip install -r requirements-docs.txt --force-reinstall

# Clear cache
rm -rf docs/_build
```

### Mermaid Not Rendering

Check:
1. First line has `%%{init: ...}%%`
2. Syntax is correct (flowchart, sequenceDiagram, etc.)
3. No Unicode characters in node IDs
4. Extension `sphinxcontrib.mermaid` is installed

### Links Broken

```bash
# Run linkcheck
sphinx-build -b linkcheck docs docs/_build/linkcheck

# View results
cat docs/_build/linkcheck/output.txt
```

### CSV Table Not Showing

Check:
1. File path is relative to document location
2. CSV file exists and has correct format
3. Header row specified correctly
4. `:file:` path uses forward slashes

## Style Guidelines

### File Naming

- Use lowercase with underscores: `my_new_page.md`
- Keep names descriptive but concise
- Match directory structure to logical sections

### Headers

- H1 (`#`) for page title (one per page)
- H2 (`##`) for major sections
- H3 (`###`) for subsections
- H4 (`####`) for minor subsections

### Links

- Use cross-references for internal links: `{doc}` and `{ref}`
- Use regular markdown links for external URLs
- Always test links with linkcheck

### Code Examples

- Include language identifier in code blocks
- Add comments to explain non-obvious code
- Keep examples practical and tested
- Show both code and expected output

## Resources

- **Sphinx Documentation**: https://www.sphinx-doc.org/
- **MyST Parser**: https://myst-parser.readthedocs.io/
- **PyData Theme**: https://pydata-sphinx-theme.readthedocs.io/
- **Mermaid**: https://mermaid.js.org/
- **sphinx-design**: https://sphinx-design.readthedocs.io/

## Support

- **GitHub Issues**: https://github.com/lukaszj321/otcv8-dev/issues
- **Documentation**: https://lukaszj321.github.io/otcv8-dev/

---

Last Updated: 2025-10-21
