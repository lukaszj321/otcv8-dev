# Tabele (CSV) — gotowce

> Pliki CSV trzymaj w `_data/` (lub podobnie) i odwołuj się ścieżką **względną** względem pliku `.md`.

---

## 1) Podstawowa tabela z pliku

````md
```{csv-table} Skrypty
:header-rows: 1
:file: ../../_data/scripts.csv
:widths: 10 20 14 10 12 34
````



## 2) Z separatorami innych niż przecinek
```md
```{csv-table} Logi (średnik)
:header-rows: 1
:file: ../../_data/logs.csv
:delim: ;
:widths: 20 40 40
````


## 3) Wyrównanie kolumn i kolumna tytułowa (stub)
```md
```{csv-table} API — Endpoints
:header-rows: 1
:file: ../../_data/endpoints.csv
:widths: 24 38 38
:align: left
:stub-columns: 1
````

## 4) Z nagłówkiem zdefiniowanym inline (bez pliku)
```md
```{csv-table} Minimalny przykład
:header-rows: 1
:widths: 30 70
Name,Description
"/v1/login","Authenticate user"
"/v1/profile","Get profile"
````

## 5) Z klasą CSS i podpisem (caption)
```md
```{csv-table} 📦 Paczki (release)
:header-rows: 1
:file: ../../_data/releases.csv
:widths: 20 30 20 30
:class: my-table compact
````

## 6) Escapowanie przecinków i cudzysłowów
```md
```{csv-table} Escaping
:header-rows: 1
:widths: 50 50
Key,Value
"path","C:\\Users\\dev, ""OTCv8"""
````

## 7) Połączenie z gridem (tabela obok opisu)
```md
:::{grid} 1 1 2 2
:gutter: 3

:::{grid-item}
Opis tabeli i kontekst użycia.
:::

:::{grid-item}
```{csv-table} Skrypty
:header-rows: 1
:file: ../../_data/scripts.csv
:widths: 10 20 14 10 12 34
```

:::

:::


## 8) Najczęstsze błędy (szybka checklista)
- Ścieżka `:file:` zła względem **aktualnego** pliku `.md`.
- Brak pustej linii przed/po dyrektywie (czasem psuje render).
- CSV z BOM/Windows-1250 → użyj UTF‑8 bez BOM.
- Niespójna liczba kolumn vs `:widths:`.
- Zły separator — ustaw `:delim:`.
