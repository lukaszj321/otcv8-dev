---
title: Settings & Cryptography — export kit
---

# Settings & Cryptography — export kit

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

### config_flow
*Facet:* [`07_settings_crypto.config_flow`](#facet-07_settings_crypto.config_flow)

```{mermaid}
%%{init: { 'theme': 'neutral', 'themeVariables': { 'primaryTextColor': '#ddd', 'lineColor': '#9aa0a6' } }}%%
graph TD
    A[07_settings_crypto.config_flow] --> B[Dataset]
    B --> C[Page]

click A "./index.html#facet-07_settings_crypto.config_flow" "Open config_flow"
```

## Cross-References

- **affects** → `01_runtime.counters` (evidence: `docs/authoring/01_runtime/datasets/counters.csv`)
- **secures** → `05_network.network_messages` (evidence: `docs/authoring/05_network/datasets/network_messages.csv`)

## Appendix / Facets

(facet-07_settings_crypto.config_flow)=
### Facet: `07_settings_crypto.config_flow`
Type: diagram

(facet-07_settings_crypto.crypto_primitives)=
### Facet: `07_settings_crypto.crypto_primitives`
Type: dataset

(facet-07_settings_crypto.secrets)=
### Facet: `07_settings_crypto.secrets`
Type: dataset

(facet-07_settings_crypto.settings)=
### Facet: `07_settings_crypto.settings`
Type: dataset

(facet-07_settings_crypto.summary)=
### Facet: `07_settings_crypto.summary`
Type: dataset
