#!/usr/bin/env python3
"""
Check generated Mermaid outputs for common truncation markers like:
  - "... 38 more"
  - "… 12 more"
  - any literal "..." followed by "more"

Usage:
  python3 docs/scripts/diagram-tools/check_truncation.py [ROOT] [--report /path/out.json]

Returns:
  0 - OK (no truncation markers)
  1 - truncation markers found (report generated if --report given)
"""
import re
import sys
import json
from pathlib import Path

# Specific patterns to detect truncated summaries like "... 38 more" or "… 12 more"
SPECIFIC_TRUNC = re.compile(r'(?:\.\.\.|…)\s*\d+\s*more', re.IGNORECASE)
# Generic suspicious patterns: any ellipsis or unicode ellipsis (we then verify context)
ELLIPSIS = re.compile(r'(?:\.\.\.|…)', re.IGNORECASE)

ROOT_DEFAULT = Path("docs")

def find_mermaid_blocks_in_md(text):
    blocks = []
    in_block = False
    buf = []
    for line in text.splitlines():
        if line.strip().startswith("```mermaid"):
            in_block = True
            buf = []
            continue
        if in_block:
            if line.strip().startswith("```"):
                in_block = False
                blocks.append("\n".join(buf))
                buf = []
                continue
            buf.append(line)
    return blocks

def check_text_for_truncation(text):
    # Check for explicit "... N more" patterns first
    if SPECIFIC_TRUNC.search(text):
        matches = SPECIFIC_TRUNC.findall(text)
        return True, {"type": "specific", "matches": matches}
    # If ellipsis present along with the word 'more' on same line, flag it
    for i, line in enumerate(text.splitlines()):
        if ELLIPSIS.search(line) and 'more' in line.lower():
            # Return the line to help debugging
            return True, {"type": "ellipsis_line", "line": line.strip(), "lineno": i+1}
    # No clear truncation detected
    return False, {}

def scan_root(root: Path):
    report = {"checked_files": 0, "truncated": []}
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix == ".mmd":
            report["checked_files"] += 1
            try:
                txt = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            found, info = check_text_for_truncation(txt)
            if found:
                report["truncated"].append({"path": str(p), "info": info})
        elif p.suffix == ".md":
            try:
                txt = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            blocks = find_mermaid_blocks_in_md(txt)
            if not blocks:
                continue
            report["checked_files"] += 1
            for i, b in enumerate(blocks):
                found, info = check_text_for_truncation(b)
                if found:
                    report["truncated"].append({
                        "path": str(p),
                        "block_index": i,
                        "info": info
                    })
    return report

def main():
    args = sys.argv[1:]
    root = Path(args[0]) if args and not args[0].startswith("--") else ROOT_DEFAULT
    report_path = None
    if "--report" in args:
        i = args.index("--report")
        if i+1 < len(args):
            report_path = Path(args[i+1])
    report = scan_root(Path(root))
    if report_path:
        try:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception:
            # best-effort: ignore write errors, but continue to print
            pass
    if report["truncated"]:
        print("TRUNCATION MARKERS FOUND:")
        for item in report["truncated"]:
            print(json.dumps(item, ensure_ascii=False))
        sys.exit(1)
    else:
        print("OK — no truncation markers found (checked files: {})".format(report["checked_files"]))
        sys.exit(0)

if __name__ == "__main__":
    main()
