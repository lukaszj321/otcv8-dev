# Lista tymczasowo wykluczonych plików z buildu Sphinx

## Cel
Ten plik dokumentuje pliki i katalogi tymczasowo wykluczone z buildu Sphinx w `conf.py` w celu naprawy CI/CD. Wykluczenia będą stopniowo cofane w kolejnych PR-ach z dedykowanymi poprawkami.

## Wykluczone wzorce (exclude_patterns)
- `docs/copilot/sphinx/code/**/source_mirror/**` — duże lustrzane kopie źródeł
- `docs/copilot/csv/*.csv` — surowe CSV mogące powodować błędy parsowania
- `docs/modules/modulesopisy/*.md` — problematyczne opisy modułów wymagające refaktoryzacji
- `docs/modules/structured/**` — strukturyzowane pliki wymagające poprawy formatowania
- `docs/tools/*.py` i `docs/tools/*.lua` — skrypty generujące, nie dokumentacja
- `docs/copilot/sphinx/code/**/angle/include/**` — nagłówki ANGLE (zbyt duże/złożone)

## Stłumione ostrzeżenia (suppress_warnings)
Kategorie nieblokujące, które będą adresowane iteracyjnie: `myst.xref_missing`, `toc.not_readable`, `toc.not_included`, `design.grid`, `myst.directive_option`, `myst.directive_comments`, `myst.parser`, `autodoc`, `ref.unknown`, `app.add_node`

## Kolejne kroki
Każdy przyszły PR powinien skupić się na naprawieniu jednej kategorii wykluczonych plików poprzez:
1. Usunięcie odpowiedniego wzorca z `exclude_patterns`
2. Naprawienie błędów w plikach
3. Weryfikację, że build Sphinx przechodzi
