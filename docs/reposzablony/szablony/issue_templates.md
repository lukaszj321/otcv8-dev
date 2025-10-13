# Issue templates

Pliki do `.github/ISSUE_TEMPLATE/`.

## Bug report (`bug_report.yml`)

```yaml
name: Bug report
description: Zgłoś błąd
labels: [bug]
body:
  - type: textarea
    id: what-happened
    attributes:
      label: Co się stało?
      description: Opisz błąd i oczekiwane zachowanie
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Wersja/commit
  - type: textarea
    id: steps
    attributes:
      label: Kroki do odtworzenia
      description: 1) … 2) …
```

## Feature request (`feature_request.yml`)

```yaml
name: Feature request
description: Zaproponuj funkcję
labels: [enhancement]
body:
  - type: textarea
    id: context
    attributes:
      label: Kontekst
  - type: textarea
    id: proposal
    attributes:
      label: Propozycja
      description: Jak to ma działać?
```
