---
title: 07_settings_crypto - Settings crypto
---

# 07_settings_crypto - Settings crypto

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
:::{grid} 1 1 2 2

:gutter: 2

:::{grid-item}

#### `entities.csv`
*Facet:* [`07_settings_crypto.entities`](#facet-07_settings_crypto.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

:::

:::{grid-item}

#### `settings.csv`
*Facet:* [`07_settings_crypto.settings`](#facet-07_settings_crypto.settings)

```{csv-table} settings
:header-rows: 1
:file: ./datasets/settings.csv
:widths: auto
```

:::

:::{grid-item}

#### `summary.csv`
*Facet:* [`07_settings_crypto.summary`](#facet-07_settings_crypto.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

:::

:::

## Diagrams
#### `architecture.mmd`
        *Facet:* [`07_settings_crypto.architecture`](#facet-07_settings_crypto.architecture)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph LR
    subgraph Settings & Crypto
        E0[Settings]
        E1[Crypto Functions]
        E2[Config Options]
        E0 --> E1
        E1 --> E2
    end
        ```

#### `crypto_overview.mmd`
        *Facet:* [`07_settings_crypto.crypto_overview`](#facet-07_settings_crypto.crypto_overview)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  CryptoOverview[07_settings_crypto:crypto_overview] --> Data[Datasets]
  Data --> Page[Index]

click CryptoOverview "./index.html#facet-07_settings_crypto.crypto_overview" "Open crypto_overview"
        ```

#### `flow.mmd`
        *Facet:* [`07_settings_crypto.flow`](#facet-07_settings_crypto.flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[Settings & Crypto] --> B[Data Collection]
    B --> C[Processing]
    C --> D[Datasets]
    C --> E[Analysis]
    D --> F[CSV Export]
    E --> G[Statistics]
    G --> H[Reports]
    F --> H
        ```

## Appendix / Facets
(facet-07_settings_crypto.architecture)=
### Facet: `07_settings_crypto.architecture`
(facet-07_settings_crypto.crypto_overview)=
### Facet: `07_settings_crypto.crypto_overview`
(facet-07_settings_crypto.entities)=
### Facet: `07_settings_crypto.entities`
(facet-07_settings_crypto.flow)=
### Facet: `07_settings_crypto.flow`
(facet-07_settings_crypto.settings)=
### Facet: `07_settings_crypto.settings`
(facet-07_settings_crypto.summary)=
### Facet: `07_settings_crypto.summary`
