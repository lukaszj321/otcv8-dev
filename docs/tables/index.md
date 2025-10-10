# Tabele i raporty

## CSV → tabela (H2)
Przykład krótkiej tabeli w Markdown:

| Klucz | Wartość |
|------:|:--------|
| api   | v1      |
| build | Release |

### Tabele z `sphinx-design` (H3)

::::{grid} 1 2 2 3
:gutter: 2

:::{grid-item-card} Endpointy
| Route | Opis |
|---|---|
| `/status` | Healthcheck |
| `/auth` | Token |
:::

:::{grid-item-card} Limity
| Nazwa | Wartość |
|---|---|
| RPS | 120 |
| Timeout | 30s |
:::

::::

#### Warianty responsywne (H4)
- Unikaj >6 kolumn bez scrolla.
