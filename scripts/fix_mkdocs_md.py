#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Skrypt porządkujący pliki Markdown pod MkDocs/Material.

Funkcje:
1) Naprawa rozstrzelonych nagłówków (A r c h i t e k t u r a → Architektura),
   ale TYLKO gdy cały tytuł nie ma nigdzie dwóch liter obok siebie (bez spacji).
2) Dodanie pustej linii po każdym nagłówku (#..######).
3) Domknięcie niedomkniętych bloków Jinja `{% raw %}` → dodanie brakujących `{% endraw %}` na końcu pliku.
4) Pusta linia przed i po blokach kodu (```...```), w tym ```mermaid```.
5) Tryb --dry-run (domyślny) wypisuje diff, --apply zapisuje zmiany. Tworzy kopie .bak.

Użycie:
  python3 scripts/fix_mkdocs_md.py                # dry-run (diff)
  python3 scripts/fix_mkdocs_md.py --apply        # zapis zmian
  python3 scripts/fix_mkdocs_md.py docs/guides    # tylko podkatalog
"""

from __future__ import annotations
import sys
import re
import difflib
from pathlib import Path
from typing import List

# Klasa znaków dla liter (łapiemy PL i większość europejskich akcentów)
LETTER = r"A-Za-zÀ-ÖØ-öø-ÿĀ-žŻżŹźĆćŁłŃńŚśÓóĄąĘę"

HDR_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)\s*$")
CODE_FENCE_RE = re.compile(r"^```")  # dowolny blok kodu
RAW_OPEN_RE = re.compile(r"{%\s*raw\s*%}")
RAW_CLOSE_RE = re.compile(r"{%\s*endraw\s*%}")

# warunek: „rozstrzelony” – nigdzie nie ma dwóch liter obok siebie,
# ale są litera-spacja-litera (czyli wszystko jest „pooddzielane” spacjami)
HAS_ADJ_LETTERS = re.compile(rf"[{LETTER}]{{2}}")
HAS_LETTER_SPACE_LETTER = re.compile(rf"[{LETTER}]\s[{LETTER}]")

def collapse_spaced_letters_if_stretched(title: str) -> str:
    """Jeśli CAŁY tytuł jest zrobiony z liter rozdzielonych spacją (brak dwóch liter obok siebie),
    sklej litery w słowa, ale nie ruszaj spacji przed znakami nieliterowymi (np. przed '(')."""
    if HAS_ADJ_LETTERS.search(title):
        # tytuł normalny (ma gdzieś dwie litery obok siebie) – nic nie zmieniamy
        return title
    if not HAS_LETTER_SPACE_LETTER.search(title):
        # nie wygląda na rozstrzelony
        return title

    # Sklejamy tylko przestrzenie pomiędzy literami: L <spacja> L → LL
    # Uwaga: to usunęłoby też spacje między normalnymi słowami – ale do tej
    # funkcji trafiają wyłącznie „rozstrzelone” tytuły (brak LL w całym stringu),
    # więc to zachowanie jest pożądane.
    new = re.sub(rf"(?P<a>[{LETTER}])\s(?P<b>[{LETTER}])", r"\g<a>\g<b>", title)
    return new

def ensure_blank_line_after_headers(lines: List[str]) -> List[str]:
    out: List[str] = []
    for i, line in enumerate(lines):
        out.append(line)
        if HDR_RE.match(line.rstrip("\n")):
            # jeśli następna linia istnieje i nie jest pusta ani płotkiem kodu – wstaw pustą
            nxt = lines[i+1] if i+1 < len(lines) else ""
            if nxt.strip() != "":
                out.append("\n")
    return out

def ensure_blank_lines_around_code_fences(lines: List[str]) -> List[str]:
    out: List[str] = []
    for i, line in enumerate(lines):
        is_fence = CODE_FENCE_RE.match(line.strip())
        if is_fence:
            # przed
            if out and out[-1].strip() != "":
                out.append("\n")
            out.append(line)
            # po – dodamy przy przetwarzaniu kolejnej linii, ale jeśli to koniec
            # pliku albo następna linia niepusta, dolejemy pustą tuż po płotku
            nxt = lines[i+1] if i+1 < len(lines) else None
            if nxt is None or nxt.strip() != "":
                out.append("\n")
            continue
        out.append(line)
    return out

def fix_raw_blocks(text: str) -> str:
    opens = len(RAW_OPEN_RE.findall(text))
    closes = len(RAW_CLOSE_RE.findall(text))
    if opens > closes:
        missing = opens - closes
        text = text.rstrip() + ("\n" if not text.endswith("\n") else "")
        text += ("\n" + "{% endraw %}\n") * missing
    return text

def process_file(path: Path) -> str:
    original = path.read_text(encoding="utf-8", errors="replace")
    lines = original.splitlines(keepends=True)

    # 1) napraw nagłówki
    new_lines: List[str] = []
    in_code_block = False
    for line in lines:
        stripped = line.rstrip("\n")
        if CODE_FENCE_RE.match(stripped.strip()):
            in_code_block = not in_code_block  # toggle
            new_lines.append(line)
            continue

        if not in_code_block:
            m = HDR_RE.match(stripped)
            if m:
                hashes = m.group("hashes")
                title = m.group("title")
                fixed_title = collapse_spaced_letters_if_stretched(title)
                # Zastąp wielokrotne spacje pojedynczą (po sklejeniu liter)
                fixed_title = re.sub(r"\s{2,}", " ", fixed_title).strip()
                line = f"{hashes} {fixed_title}\n"
        new_lines.append(line)

    # 2) puste linie po nagłówkach
    new_lines = ensure_blank_line_after_headers(new_lines)

    # 3) puste linie wokół bloków kodu
    new_lines = ensure_blank_lines_around_code_fences(new_lines)

    # 4) domknięcie {% raw %} → {% endraw %}
    new_text = "".join(new_lines)
    new_text = fix_raw_blocks(new_text)

    return new_text

def iter_markdown_files(root: Path) -> List[Path]:
    if root.is_file() and root.suffix.lower() == ".md":
        return [root]
    base = root if root.exists() else Path("docs")
    return [p for p in base.rglob("*.md") if p.is_file()]

def main():
    apply = "--apply" in sys.argv
    # ścieżki startowe (domyślnie docs/)
    start_paths = [Path(p) for p in sys.argv[1:] if not p.startswith("--")]
    if not start_paths:
        start_paths = [Path("docs")]

    files: List[Path] = []
    for sp in start_paths:
        files.extend(iter_markdown_files(sp))

    if not files:
        print("Brak plików .md do przetworzenia (sprawdź ścieżkę / repo).")
        sys.exit(0)

    any_changes = False
    for path in sorted(files):
        try:
            new_text = process_file(path)
        except Exception as e:
            print(f"[WARN] Błąd przetwarzania {path}: {e}")
            continue

        old_text = path.read_text(encoding="utf-8", errors="replace")
        if old_text != new_text:
            any_changes = True
            if apply:
                # kopia zapasowa
                bak = path.with_suffix(path.suffix + ".bak")
                if not bak.exists():
                    bak.write_text(old_text, encoding="utf-8")
                path.write_text(new_text, encoding="utf-8")
                print(f"[FIXED] {path}")
            else:
                print(f"--- DIFF {path} ---")
                diff = difflib.unified_diff(
                    old_text.splitlines(),
                    new_text.splitlines(),
                    fromfile=str(path),
                    tofile=str(path) + " (fixed)",
                    lineterm=""
                )
                for l in diff:
                    print(l)

    if not any_changes:
        print("OK: brak zmian do wprowadzenia.")

if __name__ == "__main__":
    main()
