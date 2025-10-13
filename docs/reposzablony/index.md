---
title: Repo Szablony (Authoring)
---

# Repo Szablony (Authoring)

:::{admonition} Co to jest?
:class: tip
To warsztat/authoring do generowania struktury repo, szablonów i artefaktów (CSV, diagramy, itp.), które później integrujemy z dokumentacją.
:::

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} Szablony plików repo
:link: szablony/index
:link-type: doc
:shadow: md
Zbiór gotowych plików: README, CONTRIBUTING, CODEOWNERS, SECURITY, CHANGES/RELEASE, ADR, Style Guide, Diagrams, Kitchen Sink itd.
:::

:::{grid-item-card} Dane/artefakty (jeśli generowane)
:link: artifacts/index
:link-type: doc
:shadow: md
CSV, grafy, obrazy — wszystko to, co agent/CI wygenerował w tym obszarze.
:::
:::

```{toctree}
:maxdepth: 2
:caption: Nawigacja
:titlesonly:

szablony/index
artifacts/index
```

---
title: Repo szablony i wzorce dokumentów
---

# Repo szablony i wzorce dokumentów

```{contents}
:depth: 2
:backlinks: entry
```

:::{admonition} Co tu jest?
:class: tip
Zbiór gotowych szablonów i wzorców do dokumentowania repozytoriów i projektów:
README, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, zgłoszenia/PR, CHANGELOG/RELEASE,
CODEOWNERS, licencje, ADR, styl, tabele/CSV, diagramy, „kitchen sink”.
:::

:::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} README
:link: szablony/readme
:link-type: doc
:shadow: md
Szablon README z sekcjami i dobrymi praktykami.
:::

:::{grid-item-card} Contributing
:link: szablony/contributing
:link-type: doc
:shadow: md
Zasady kontrybucji, style commitów, struktura PR.
:::

:::{grid-item-card} Code of Conduct
:link: szablony/code_of_conduct
:link-type: doc
:shadow: md
Kodeks zachowania.
:::

:::{grid-item-card} Security
:link: szablony/security
:link-type: doc
:shadow: md
Zasady zgłaszania luk, wsparcie wersji.
:::

:::{grid-item-card} Issue Templates
:link: szablony/issue_templates
:link-type: doc
:shadow: md
Szablony zgłoszeń do `.github/ISSUE_TEMPLATE`.
:::

:::{grid-item-card} Pull Request Template
:link: szablony/pr_template
:link-type: doc
:shadow: md
Szablon PR.
:::

:::{grid-item-card} Changelog / Release
:link: szablony/changelog_release
:link-type: doc
:shadow: md
Wzorzec CHANGELOG i procesu wydawniczego.
:::

:::{grid-item-card} CODEOWNERS
:link: szablony/codeowners
:link-type: doc
:shadow: md
Przykładowa konfiguracja.
:::

:::{grid-item-card} Licencje
:link: szablony/license_guide
:link-type: doc
:shadow: md
Notatki o doborze i oznaczaniu licencji.
:::

:::{grid-item-card} ADR (decyzje arch.)
:link: szablony/adr
:link-type: doc
:shadow: md
Szablon dokumentowania decyzji.
:::

:::{grid-item-card} Style guide
:link: szablony/style_guide
:link-type: doc
:shadow: md
Konwencje pisania i formatowania.
:::

:::{grid-item-card} Diagramy
:link: szablony/diagrams
:link-type: doc
:shadow: md
Mermaid/Graphviz/obrazy – ciemny/jasny motyw.
:::

:::{grid-item-card} Kitchen sink
:link: szablony/kitchen_sink
:link-type: doc
:shadow: md
Przegląd komponentów PyData/Sphinx Design.
:::
:::

## Spis stron

```{toctree}
:maxdepth: 1
:caption: Szablony i wzorce

szablony/readme
szablony/contributing
szablony/code_of_conduct
szablony/security
szablony/issue_templates
szablony/pr_template
szablony/changelog_release
szablony/codeowners
szablony/license_guide
szablony/adr
szablony/style_guide
szablony/diagrams
szablony/kitchen_sink
```
