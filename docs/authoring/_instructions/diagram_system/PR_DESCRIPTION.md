# PR: Fix and enhance Mermaid diagrams in documentation

## Overview

This PR introduces comprehensive fixes and enhancements to the diagram system instructions in `docs/authoring/_instructions/diagram_system/` to remove ambiguities and add missing rules necessary for automatic generation, fixing, and validation of Mermaid diagrams.

## Motivation

The existing diagram system documentation lacked:
- Clear guidance on choosing the right diagram type for specific content
- Standardized approach to handling placeholders and incomplete diagrams
- Conventions for idempotent auto-generation of diagrams
- Formal metadata specifications (frontmatter)
- Renderer compatibility information
- CI/CD integration guidelines
- Detailed style mapping examples

These gaps made it difficult for both human developers and AI agents to consistently create, maintain, and validate diagrams across the documentation.

## Changes Summary

### Modified Files (3 files, +708 lines)

1. **`README.md`** (+363 lines)
   - Added comprehensive sections on diagram type selection
   - Documented placeholder and missing file handling strategies
   - Defined idempotency markers for auto-generated diagrams
   - Specified frontmatter schema with ISO 8601 date format
   - Added Mermaid version and renderer compatibility matrix
   - Provided CI/CD integration guidelines
   - Extended quality checklist with practical verification steps
   - Added code snippets for common patterns

2. **`02_VISUAL_GUIDELINES.md`** (+159 lines)
   - Added detailed element type → classDef mapping table
   - Provided hex color values and use case examples
   - Documented label breaking rules with `<br>` tag
   - Added subgraph usage patterns and best practices
   - Defined click fallback strategies for non-interactive renderers
   - Included practical code examples throughout

3. **`03_DESIGN_PATTERNS/README.md`** (+186 lines)
   - Clarified patterns vs. templates concept
   - Added heuristic-based pattern selection guide
   - Documented step-by-step adaptation workflow
   - Provided real-world adaptation examples (3 scenarios)
   - Added adaptation checklist
   - Included advanced tips and anti-patterns

## Key Improvements

### 1. Decision-Making Guidance

**New Section 5 in README.md: "Mapping Treści → Typ Diagramu"**

Provides:
- Decision table mapping content type to diagram type
- Step-by-step algorithm for choosing the right visualization
- Practical example with rationale

**Impact:** Eliminates guesswork when starting a new diagram. Both humans and AI agents can now systematically select the appropriate diagram type.

### 2. Placeholder Handling

**New Section 6 in README.md: "Obsługa Placeholderów i Brakujących Plików"**

Defines two approaches:
- **Approach A:** Placeholder diagram with TODO marker
- **Approach B:** Markdown TODO comment with planned elements

**Impact:** Prevents broken references while maintaining clear documentation of future work.

### 3. Idempotency Support

**New Section 7 in README.md: "Idempotencja i Marker Generowanego Bloku"**

Introduces standardized markers:
```plaintext
%% AUTO-GENERATED: Do not edit manually
%% Generator: <tool_name>
%% Source: <data_source_path>
%% Generated: <ISO_8601_timestamp>
```

**Impact:** Enables safe re-generation of diagrams without manual merge conflicts. AI agents can detect and respect auto-generated content.

### 4. Metadata Standardization

**New Section 8 in README.md: "Specyfikacja Frontmatter"**

Defines required fields:
- `diagram_id`: Unique identifier (kebab-case)
- `type`: Mermaid diagram type
- `last_updated`: ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SSZ)
- `tags`: Categorization array

**Impact:** Consistent metadata enables automated indexing, search, and validation.

### 5. Renderer Compatibility

**New Section 9 in README.md: "Wersja Mermaid i Kompatybilność Rendererów"**

Provides compatibility matrix for:
- GitHub Markdown
- Sphinx (sphinxcontrib-mermaid)
- MkDocs
- mermaid-cli

**Impact:** Developers know which features work in which environments and can implement appropriate fallbacks.

### 6. CI/CD Integration

**New Section 10 in README.md: "Walidacja i CI"**

Includes:
- Ready-to-use GitHub Actions workflow
- Alternative tools (mermaid-lint, markdownlint)
- Local validation commands

**Impact:** Automated validation catches syntax errors before merge, reducing manual review burden.

### 7. Visual Guidelines Enhancements

**New content in 02_VISUAL_GUIDELINES.md:**

- **Detailed mapping table** with hex colors, stroke, text colors, and use cases
- **Label breaking rules** with max lines and formatting conventions
- **Subgraph patterns** with direction control and nesting limits
- **Click fallback** with comment-based alternatives

**Impact:** Eliminates ambiguity in visual styling. All diagrams will use consistent colors and formatting.

### 8. Pattern Adaptation Guide

**New content in 03_DESIGN_PATTERNS/README.md:**

- **Patterns vs. Templates** clarification
- **Pattern selection heuristics** based on tags and content type
- **3 practical adaptation examples:**
  - Module dependency visualization
  - Authorization flow sequence
  - Placeholder creation
- **Adaptation checklist** with verification steps

**Impact:** Developers understand that patterns are starting points, not copy-paste templates. Clear examples show how to adapt generic patterns to specific needs.

## Design Decisions

### 1. Scope Limitation

**Decision:** All changes confined to `docs/authoring/_instructions/diagram_system/`

**Rationale:** Minimize blast radius. These are instructional documents for documentation authors, not runtime code.

### 2. Backward Compatibility

**Decision:** Additive changes only; no removal of existing content

**Rationale:** Existing diagrams remain valid. New guidelines apply to future diagrams and updates.

### 3. Practical Examples

**Decision:** Include multiple code snippets and real-world scenarios

**Rationale:** Examples reduce interpretation errors and accelerate adoption, especially for AI agents.

### 4. ISO 8601 for Timestamps

**Decision:** Mandate `YYYY-MM-DDTHH:MM:SSZ` format for all dates

**Rationale:** Unambiguous, sortable, widely supported. Prevents timezone confusion.

### 5. Fallback Strategies

**Decision:** Document fallbacks for features not supported by all renderers

**Rationale:** GitHub is primary target, but we support multiple rendering environments.

## Implementation Guide: GitHub Actions for Diagram Validation

### Step 1: Create Workflow File

Create `.github/workflows/validate-diagrams.yml`:

```yaml
name: Validate Mermaid Diagrams

on:
  pull_request:
    paths:
      - 'docs/**/*.mmd'
      - 'docs/**/*.md'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Mermaid CLI
        run: npm install -g @mermaid-js/mermaid-cli

      - name: Find all .mmd files
        id: find-files
        run: |
          echo "files=$(find docs -name '*.mmd' -type f | tr '\n' ' ')" >> $GITHUB_OUTPUT

      - name: Validate Mermaid syntax
        run: |
          for file in ${{ steps.find-files.outputs.files }}; do
            echo "Validating $file"
            mmdc -i "$file" -o /tmp/output.svg || exit 1
          done

      - name: Check frontmatter (optional)
        run: |
          # Add custom script to validate frontmatter in .md files
          echo "Frontmatter validation placeholder"
```

### Step 2: Add Pre-commit Hook (Optional)

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Validate diagrams before commit

DIAGRAM_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.mmd$')

if [ -n "$DIAGRAM_FILES" ]; then
  echo "Validating Mermaid diagrams..."
  for file in $DIAGRAM_FILES; do
    echo "Checking $file"
    mmdc -i "$file" -o /tmp/test.svg || exit 1
  done
  echo "✓ All diagrams valid"
fi
```

Make executable: `chmod +x .git/hooks/pre-commit`

### Step 3: Configure markdownlint

Add to `.markdownlint.json`:

```json
{
  "MD033": false,
  "MD041": false
}
```

This allows HTML in Markdown (needed for `<br>` in labels) and missing top-level H1.

### Step 4: Enable Actions

1. Go to repository **Settings** → **Actions** → **General**
2. Enable "Allow all actions and reusable workflows"
3. Save

### Step 5: Test

1. Create a test PR with a diagram change
2. Verify workflow runs in **Actions** tab
3. Check for validation errors in logs

## Testing Performed

### Manual Validation

1. ✅ Verified all Markdown syntax with markdownlint
2. ✅ Checked all internal links resolve correctly
3. ✅ Validated code snippets render properly on GitHub
4. ✅ Reviewed for consistency with existing documentation style

### Content Review

1. ✅ All new sections align with existing philosophy (01_DESIGN_PHILOSOPHY.md)
2. ✅ Visual guidelines maintain consistency with existing classDef definitions
3. ✅ Pattern examples use only documented types and styles
4. ✅ No breaking changes to existing content

## Migration Path for Existing Diagrams

Existing diagrams **do not need immediate updates**. New guidelines apply to:
1. New diagrams created after this PR
2. Existing diagrams being significantly modified
3. Auto-generated diagrams (which can adopt markers immediately)

## Future Work

1. **Automated diagram generation** from CSV datasets (using markers from Section 7)
2. **Diagram linting tool** that checks compliance with visual guidelines
3. **Interactive diagram editor** in documentation tooling
4. **Frontmatter validation** in CI (currently placeholder in workflow)
5. **Diagram versioning** system with change tracking

## References

- [Mermaid.js Documentation](https://mermaid.js.org/)
- [GitHub Markdown Spec](https://github.github.com/gfm/)
- [ISO 8601 Date Format](https://en.wikipedia.org/wiki/ISO_8601)
- [Font Awesome 4.7 Icons](https://fontawesome.com/v4.7.0/icons/)

## Checklist

- [x] All changes confined to `docs/authoring/_instructions/diagram_system/`
- [x] No existing content removed or broken
- [x] Code snippets are syntactically valid
- [x] Examples follow documented guidelines
- [x] Internal links verified
- [x] Markdown lint passing (with acceptable existing style)
- [x] Commit message follows conventional commits
- [x] PR description is comprehensive

## Reviewers

Please verify:
1. Clarity and completeness of new sections
2. Accuracy of code examples
3. Usefulness of practical scenarios
4. GitHub Actions workflow validity
5. Alignment with project documentation standards

---

**PR Title:** Fix and enhance Mermaid diagrams in documentation

**Labels:** documentation, enhancement, diagrams

**Milestone:** Documentation Improvements

**Related Issues:** N/A (proactive enhancement)
