#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path("docs/authoring")
INIT = "%%{init: {'theme':'dark','securityLevel':'loose','themeVariables':{'primaryTextColor':'#ddd','lineColor':'#9aa0a6'}}}%%"

# dopasuj blok ```mermaid lub ```{mermaid} ... ```
MERMAID_BLOCK = re.compile(
    r"```{?\s*mermaid\s*}?\s*\r?\n"   # otwarcie
    r"(.*?)"                          # ciało (leniwe)
    r"\r?\n```",                      # zamknięcie
    flags=re.DOTALL | re.IGNORECASE
)

def ensure_init(body: str) -> str:
    # zostaw istniejący init; wstaw jako pierwszą niepustą linię, jeśli brak
    lines = body.splitlines()
    # pominij początkowe puste linie
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if any("%%{init:" in line for line in lines):
        return body  # init już jest
    # wstaw INIT przed pierwszą niepustą linią (albo na koniec, jeśli pusty blok)
    lines.insert(i, INIT)
    return "\n".join(lines)

def fix_text(text: str) -> str:
    def _repl(m: re.Match) -> str:
        body = m.group(1)
        body_fixed = ensure_init(body)
        return f"```mermaid\n{body_fixed}\n```"
    return MERMAID_BLOCK.sub(_repl, text)

def main() -> None:
    fixed_files = 0
    for md in ROOT.rglob("*.md"):
        txt = md.read_text(encoding="utf-8", errors="ignore")
        new = fix_text(txt)
        if new != txt:
            md.write_text(new, encoding="utf-8")
            fixed_files += 1
    print(f"fixed_files={fixed_files}")

if __name__ == "__main__":
    main()
