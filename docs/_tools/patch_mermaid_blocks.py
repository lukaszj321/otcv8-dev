#!/usr/bin/env python3
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]  # -> docs/
FILES = list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.rst"))

MERMAID_HEAD = re.compile(r"^(\s*)(%%\{init:.*?%%)?\s*(sequenceDiagram|flowchart|classDiagram|erDiagram|gantt|graph\s+(TB|TD|LR|RL|BT))", re.S | re.M)

def fix(text: str) -> str:
  # ```bash ... (mermaid) ```  -> ```mermaid ... ```
  text = re.sub(
    r"```(?:bash|text)\s*\n([\s\S]*?)\n```",
    lambda m: (
      "```mermaid\n" + m.group(1).lstrip() + "\n```"
      if MERMAID_HEAD.search(m.group(1) or "") else m.group(0)
    ),
    text,
    flags=re.M
  )
  # ```mermaid -> ```{mermaid} (bez różnicy przy myst_fence_as_directive, ale czytelniej)
  text = re.sub(r"```mermaid(\s*)\n", r"```{mermaid}\1\n", text)
  return text

def main() -> int:
  changed = 0
  for p in FILES:
    s = p.read_text(encoding="utf-8", errors="ignore")
    t = fix(s)
    if t != s:
      p.write_text(t, encoding="utf-8")
      changed += 1
      print(f"[fix] {p.relative_to(ROOT)}")
  print(f"Done. Changed files: {changed}")
  return 0

if __name__ == "__main__":
  sys.exit(main())
