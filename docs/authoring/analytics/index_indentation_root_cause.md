# Index Indentation Root Cause Analysis

**Issue:** Mermaid diagrams and CSV tables in generated index pages were rendering as indented code blocks instead of as interactive diagrams and tables.

**Symptom:**
- Live pages showed Mermaid code as text in gray code blocks
- Example: https://lukaszj321.github.io/otcv8-dev/authoring/09_logging/index.html
- Sphinx `_sources` files had leading spaces before `{mermaid}` and `*Facet:*` lines

## Root Cause

The issue was in `scripts/build_authoring_pages.py`, specifically in the `mmd_block()` and `csv_block()` functions (lines 109-133 in original).

### Original Code (Problematic)

```python
def csv_block(p: pathlib.Path):
    fid = f"{chapter}.{p.stem}"
    return textwrap.dedent(f"""
    ### {p.stem}
*Facet:* [`{fid}`](#facet-{fid})

    ```{{csv-table}} {p.stem}
    :header-rows: 1
    :file: ./datasets/{p.name}
    :widths: auto
```
    """).strip()

def mmd_block(p: pathlib.Path):
    content = (diagrams / p.name).read_text(encoding="utf-8") if (diagrams / p.name).exists() else "graph TD\n  A[Error]"
    content = ensure_mermaid_init(content)
    fid = f"{chapter}.{p.stem}"
    return textwrap.dedent(f"""
    ### {p.stem}
*Facet:* [`{fid}`](#facet-{fid})

    ```{{mermaid}}
    {content}
```
    """).strip()
```

### The Problem

1. **Misleading use of `textwrap.dedent()`**: The function is designed to remove common leading whitespace from ALL lines, but the triple-quoted template string had **inconsistent indentation**:
   - The first line of the template (after `"""`) had NO indentation
   - Subsequent lines had 4 spaces of indentation (matching Python code indentation)
   - The closing `"""` was also indented

2. **How `dedent()` works**: It finds the minimum common indentation across all non-blank lines and removes it. In this case:
   - First line: 0 spaces
   - Other lines: 4 spaces
   - Result: Removes 0 spaces (the minimum)

3. **The `.strip()` trap**: The `.strip()` at the end only removes leading/trailing whitespace from the **entire string**, not from each line. So the 4 spaces before each line remained.

4. **Sphinx interprets indentation as code**: In MyST Markdown, when a directive like ` ```mermaid` is indented by 4+ spaces, Sphinx treats it as a literal code block instead of executing the directive.

## The Fix

Replace `textwrap.dedent()` with explicit line-by-line construction:

```python
def csv_block(p: pathlib.Path):
    fid = f"{chapter}.{p.stem}"
    # Build block without indentation to prevent Sphinx treating it as code
    lines = [
        f"### {p.stem}",
        f"*Facet:* [`{fid}`](#facet-{fid})",
        "",
        f"```{{csv-table}} {p.stem}",
        ":header-rows: 1",
        f":file: ./datasets/{p.name}",
        ":widths: auto",
        "```"
    ]
    return "\n".join(lines)

def mmd_block(p: pathlib.Path):
    content = (diagrams / p.name).read_text(encoding="utf-8") if (diagrams / p.name).exists() else "graph TD\n  A[Error]"
    content = ensure_mermaid_init(content)
    fid = f"{chapter}.{p.stem}"
    # Build block without indentation to prevent Sphinx treating it as code
    lines = [
        f"### {p.stem}",
        f"*Facet:* [`{fid}`](#facet-{fid})",
        "",
        "```mermaid",
        content,
        "```"
    ]
    return "\n".join(lines)
```

### Why This Works

1. **Explicit control**: Each line is constructed individually with no leading whitespace
2. **Predictable output**: The ` ```mermaid` and ` ```{csv-table}` directives start at column 0
3. **Blank line separation**: Empty string in the list ensures proper MyST directive separation
4. **Content preservation**: Mermaid diagram content is inserted as-is without modification

## Impact

- **Before**: All generated index pages had broken Mermaid/CSV rendering
- **After**: All MyST directives render correctly as interactive elements
- **Files affected**: All 15+ chapter index files in `docs/authoring/*/index.md`

## Verification

Run the MyST indent scanner:
```bash
python3 docs/authoring/_tools/myst_indent_scanner.py
```

Expected result: 0 issues in generated index files.

## Prevention

- Avoid `textwrap.dedent()` with f-strings that have multi-line content
- Use explicit list construction for MyST directive generation
- Always verify MyST directives start at column 0 in generated files
- Run QA scanners before deploying docs
