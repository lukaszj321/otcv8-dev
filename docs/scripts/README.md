# Documentation Build Scripts

This directory contains scripts for validating and maintaining the Sphinx documentation build.

## verify_sphinx_build.sh

Automated Sphinx build verification script for CI/CD integration.

### Purpose

Validates that the Sphinx documentation builds successfully without critical errors. This script was created to prevent regression of fixes made in PR #(number) which resolved 50+ critical build errors.

### Usage

```bash
# Run from repository root
./docs/scripts/verify_sphinx_build.sh

# Or from docs directory
cd docs && ./scripts/verify_sphinx_build.sh
```

### Features

- **Automated Build**: Runs `sphinx-build` with proper configuration
- **Error Detection**: Counts and categorizes errors (CRITICAL, ERROR, WARNING)
- **Pattern Matching**: Detects specific error types:
  - Tab unpacking errors (ValueError)
  - CSV table errors (insufficient data)
  - Transition errors (document structure)
- **CI/CD Ready**: Returns proper exit codes for pipeline integration
- **Human-Readable**: Provides clear summary output

### Exit Codes

- `0` - Build succeeded (warnings may be present)
- `1` - Build failed with CRITICAL errors
- `1` - Build failed with non-zero exit code

### Output

The script generates:
- Console output with build progress
- `/tmp/sphinx_build.log` - Complete build log
- Summary with error counts and specific issues

### Example Output

```
=== Sphinx Build Verification ===
Docs dir: /path/to/docs
Build dir: /path/to/build/html

Running Sphinx build...
[... build output ...]

=== Build Summary ===
Critical errors: 0
Errors: 0
Warnings: 23

✅ Build completed (warnings: 23, errors: 0)
```

### Integration with CI/CD

#### GitHub Actions Example

```yaml
- name: Verify Sphinx Build
  run: |
    pip install -r requirements-docs.txt
    ./docs/scripts/verify_sphinx_build.sh
```

#### GitLab CI Example

```yaml
verify-docs:
  script:
    - pip install -r requirements-docs.txt
    - ./docs/scripts/verify_sphinx_build.sh
```

### Requirements

- Python 3.8+
- Sphinx and dependencies installed (see `requirements-docs.txt`)
- Bash shell

### Troubleshooting

**Script not executable**:
```bash
chmod +x docs/scripts/verify_sphinx_build.sh
```

**Missing dependencies**:
```bash
pip install -r requirements-docs.txt
```

**Build hangs or times out**:
- Check for infinite loops in documentation
- Verify intersphinx mappings are accessible
- Consider increasing timeout in CI/CD config

### Related Documentation

- Main fixes summary: `SPHINX_FIXES_SUMMARY.md` (repository root)
- Sphinx configuration: `docs/conf.py`
- Requirements: `requirements-docs.txt`

### Maintenance

When adding new documentation:
1. Run this script locally before committing
2. Ensure no new critical errors are introduced
3. Keep warning count reasonable (< 200)
4. Document any intentional warnings

### History

- Created: 2024-11-02
- Purpose: Prevent regression of Sphinx build fixes
- Context: Resolved 50+ critical errors in job #54296308693
