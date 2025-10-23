#!/usr/bin/env python3
import re
from pathlib import Path
import sys

ROOT = Path("docs")

MERMAID_RE = re.compile(
    r"(?m)^[ \t]*```(?:\{)?mermaid(?:\})?[^\n]*\n(.*?)(?:\n)[ \t]*```[ \t]*$",
    re.DOTALL,
)

def _dedent_block(block: str) -> str:
    lines = block.splitlines()
    indents = [len(re.match(r"^[ \t]*", ln).group(0)) for ln in lines if ln.strip()]
    ws = min(indents) if indents else 0
    return "\n".join(ln[ws:] for ln in lines)

def fix_text(s: str) -> str:
    def repl(m: re.Match) -> str:
        body = _dedent_block(m.group(1)).rstrip()
        return "```{mermaid}\n" + body + "\n```"
    return MERMAID_RE.sub(repl, s)

def main() -> int:
    modified = 0
    for p in ROOT.rglob("*"):
      if p.suffix.lower() not in {".md", ".rst", ".md.rst"}:
          continue
      try:
          txt = p.read_text(encoding="utf-8", errors="ignore")
      except Exception:
          continue
      new = fix_text(txt)
      if new != txt:
          p.write_text(new, encoding="utf-8")
          modified += 1
    print(f"[mermaid_hard_fix] patched files: {modified}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
