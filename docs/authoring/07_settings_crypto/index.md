---
title: 07_settings_crypto - Settings crypto
---

# 07_settings_crypto - Settings crypto

kontrolowana inwentaryzacja wybranych ustawien (whitelist) oraz metadane protokolu/crypto (wersje, RSA info) z klienta.

```{contents} Table of contents
:depth: 2
:local:
```

## Datasets
### crypto_primitives
*Facet:* [`07_settings_crypto.crypto_primitives`](#facet-07_settings_crypto.crypto_primitives)

```{csv-table} crypto_primitives
:header-rows: 1
:file: ./datasets/crypto_primitives.csv
:widths: auto
```

### entities
*Facet:* [`07_settings_crypto.entities`](#facet-07_settings_crypto.entities)

```{csv-table} entities
:header-rows: 1
:file: ./datasets/entities.csv
:widths: auto
```

### secrets
*Facet:* [`07_settings_crypto.secrets`](#facet-07_settings_crypto.secrets)

```{csv-table} secrets
:header-rows: 1
:file: ./datasets/secrets.csv
:widths: auto
```

### settings
*Facet:* [`07_settings_crypto.settings`](#facet-07_settings_crypto.settings)

```{csv-table} settings
:header-rows: 1
:file: ./datasets/settings.csv
:widths: auto
```

### summary
*Facet:* [`07_settings_crypto.summary`](#facet-07_settings_crypto.summary)

```{csv-table} summary
:header-rows: 1
:file: ./datasets/summary.csv
:widths: auto
```

## Diagrams
### architecture
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

### config_flow
        *Facet:* [`07_settings_crypto.config_flow`](#facet-07_settings_crypto.config_flow)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[07_settings_crypto.config_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-07_settings_crypto.config_flow" "Open config_flow"
        ```

### crypto_overview
        *Facet:* [`07_settings_crypto.crypto_overview`](#facet-07_settings_crypto.crypto_overview)

        ```{mermaid}
        %%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
  CryptoOverview[07_settings_crypto:crypto_overview] --> Data[Datasets]
  Data --> Page[Index]

click CryptoOverview "./index.html#facet-07_settings_crypto.crypto_overview" "Open crypto_overview"
        ```

### flow
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



## Crosslinks

- **affects** → `01_runtime.counters` (evidence: `docs/authoring/01_runtime/datasets/counters.csv`)
- **secures** → `05_network.network_messages` (evidence: `docs/authoring/05_network/datasets/network_messages.csv`)

## Appendix / Facets

(facet-07_settings_crypto.architecture)=
### Facet: `07_settings_crypto.architecture`
Type: diagram

(facet-07_settings_crypto.config_flow)=
### Facet: `07_settings_crypto.config_flow`
Type: diagram

(facet-07_settings_crypto.crypto_overview)=
### Facet: `07_settings_crypto.crypto_overview`
Type: diagram

(facet-07_settings_crypto.crypto_primitives)=
### Facet: `07_settings_crypto.crypto_primitives`
Type: dataset

(facet-07_settings_crypto.entities)=
### Facet: `07_settings_crypto.entities`
Type: dataset

(facet-07_settings_crypto.flow)=
### Facet: `07_settings_crypto.flow`
Type: diagram

(facet-07_settings_crypto.secrets)=
### Facet: `07_settings_crypto.secrets`
Type: dataset

(facet-07_settings_crypto.settings)=
### Facet: `07_settings_crypto.settings`
Type: dataset

(facet-07_settings_crypto.summary)=
### Facet: `07_settings_crypto.summary`
Type: dataset

