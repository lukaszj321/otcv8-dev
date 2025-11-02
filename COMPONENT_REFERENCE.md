# Component Reference Guide

Quick reference for all sphinx-design and MyST components used in the landing pages.

## Grid Layout

```markdown
:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} Card Title
:link: path/to/page
Description text here.
:::

:::{grid-item-card} Another Card
:link: another/path
More description.
:::
:::
```

**Parameters:**
- `1 1 2 3` = columns on mobile, tablet, desktop
- `:gutter:` = spacing between cards
- `:link:` = make entire card clickable

## Tabs

````markdown
```{tabs}
```{tab} Guide

Content for guide tab.
```
```{tab} Reference

Content for reference tab.
```
```{tab} Examples

Content for examples tab.
```
````
````

## CSV Table

```markdown
```{csv-table} Table Title
:header-rows: 1
:file: path/to/file.csv
:widths: 20, 20, 20, 20, 20
```
```

**Options:**
- `:header-rows: 1` = first row is header
- `:file:` = path relative to current file
- `:widths:` = column width percentages

## Mermaid Diagrams

### Flowchart
```markdown
```{mermaid}
flowchart LR
  A[Start]-->B[Process]
  B-->C[End]
```
```

### Sequence Diagram
```markdown
```{mermaid}
sequenceDiagram
  participant A
  participant B
  A->>B: Request
  B-->>A: Response
```
```

## Graphviz Diagrams

```markdown
```{graphviz}
digraph G {
  A -> B;
  B -> C;
  C -> A;
}
```
```

## Literalinclude (Code Snippets)

```markdown
```{literalinclude} ../../../path/to/file.cpp
:language: cpp
:lines: 1-20
```
```

**Options:**
- `:language:` = syntax highlighting (cpp, python, lua, etc.)
- `:lines:` = specific line range
- `:start-after:` = start after text pattern
- `:end-before:` = end before text pattern

## Badges

```markdown
{badge}`text,color`
```

**Colors:**
- `success` = green
- `info` = blue
- `warning` = yellow
- `danger` = red
- `primary` = default

**Examples:**
- `{badge}`lint ok,success``
- `{badge}`todo,warning``
- `{badge}`reference,info``

## Cards

```markdown
:::{card}
**Title Text**
Content text here.
:::
```

## Dropdowns

```markdown
```{dropdown} Dropdown Title
- [ ] Task 1
- [ ] Task 2
- [x] Task 3 (completed)
```
```

## Cross-References

```markdown
{ref}`path/to/page`
```

**Examples:**
- `{ref}`authoring/index``
- `{ref}`04_ui/index``
- `{ref}`guide/index``

## Admonitions

```markdown
:::{note}
This is a note.
:::

:::{warning}
This is a warning.
:::

:::{tip}
This is a tip.
:::

:::{important}
This is important.
:::

:::{danger}
This is a danger alert.
:::
```

## Toctree

```markdown
```{toctree}
:hidden:
:maxdepth: 2
:caption: Section Name

page1/index
page2/index
page3/index
```
```

**Options:**
- `:hidden:` = hide from main content, show in sidebar
- `:maxdepth:` = nesting depth (1-3 recommended)
- `:caption:` = section title in sidebar

## YAML Frontmatter

```markdown
---
title: Page Title
---

# Page Heading
```

**Usage:** Place at very top of .md file for page metadata.

## Complete Example

````markdown
---
title: My Landing Page
---

# My Landing Page

```{toctree}
:hidden:
:maxdepth: 2

section1/index
section2/index
```

:::{grid} 1 1 2 3
:gutter: 2

:::{grid-item-card} Feature 1
:link: feature1/index
Description of feature 1.
:::

:::{grid-item-card} Feature 2
:link: feature2/index
Description of feature 2.
:::
:::

```{tabs}
```{tab} Guide

Guide content here.
```

```{tab} Examples

**CSV Data**
```{csv-table} Sample Data
:header-rows: 1
:file: ./data/sample.csv
```

**Diagram**
```{mermaid}
flowchart LR
  A-->B
  B-->C
```
```
````

:::{card}
**Quality Gates**
{badge}`passing,success` {badge}`docs,info`
:::

```{dropdown} Quick Tasks
- [ ] Task 1
- [x] Task 2
- [ ] Task 3
```

:::{grid} 1 1 2 3
**See also:** {ref}`other/page` · {ref}`another/page`
:::
````

## Dark Mode Considerations

All components support dark mode automatically via PyData theme:

- Mermaid: uses dark theme by default (configured in conf.py)
- Graphviz: adapts to page background
- Cards/Grids: use theme colors
- Badges: have high contrast colors
- Code blocks: use theme syntax highlighting

## Responsive Breakpoints

Grid columns: `{grid} mobile tablet desktop`

Example: `{grid} 1 1 2 3`
- Mobile: 1 column
- Tablet: 2 columns (768px+)
- Desktop: 3 columns (992px+)

## Best Practices

1. **Keep TOC shallow**: Use `:maxdepth: 2` or `3` max
2. **Hide toctrees**: Use `:hidden:` on landing pages
3. **Limit cards**: 4-6 cards per grid for readability
4. **Use badges sparingly**: 2-3 per section
5. **Test responsiveness**: Check mobile, tablet, desktop views
6. **Validate links**: Ensure all {ref} targets exist
7. **Dark mode**: Test diagrams in both light and dark themes
8. **Accessibility**: Use semantic headings (H1 → H2 → H3)
