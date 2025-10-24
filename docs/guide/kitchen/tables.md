# Tabele (CSV)

> Pliki CSV trzymaj w `_data/` (lub podobnie) i odwołuj się ścieżką **względną** względem pliku `.md`.

<hr/>

## 1) Podstawowa tabela z pliku — **kod**

````md
```{csv-table} Skrypty
:header-rows: 1
:file: ../../_data/scripts.csv
:widths: 10 20 14 10 12 34
`````

`````

<hr/>

## 2) Separator inny niż przecinek — **kod**

````md
```{csv-table} Logi (średnik)
:header-rows: 1
:file: ../../_data/logs.csv
:delim: ;
:widths: 20 40 40
```
`````

<hr/>

## 3) Wyrównanie i kolumna tytułowa (stub) — **kod**

````md
```{csv-table} API — Endpoints
:header-rows: 1
:file: ../../_data/endpoints.csv
:widths: 24 38 38
:align: left
:stub-columns: 1
```
````

<hr/>

## 4) Nagłówek inline (bez pliku) — **kod**

````md
```{csv-table} Minimalny przykład
:header-rows: 1
:widths: 30 70
Name,Description
"/v1/login","Authenticate user"
"/v1/profile","Get profile"
```
````

<hr/>

## 5) Klasy CSS i podpis (caption) — **kod**

````md
```{csv-table} 📦 Paczki (release)
:header-rows: 1
:file: ../../_data/releases.csv
:widths: 20 30 20 30
:class: my-table compact
```
````

<hr/>

## 6) Escapowanie przecinków i cudzysłowów — **kod**

````md
```{csv-table} Escaping
:header-rows: 1
:widths: 50 50
Key,Value
"path","C:\\Users\\dev, ""OTCv8"""
```
````

<hr/>

## 7) W gridzie (tabela obok opisu) — **kod**

````md
:::{grid} 1 1 2 2
:gutter: 3
:::{grid-row}

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
````

<hr/>

## 8) Najczęstsze błędy (checklista)

* Ścieżka `:file:` zła względem **aktualnego** pliku `.md`.
* Brak pustej linii przed/po dyrektywie (czasem psuje render).
* CSV z BOM/Windows-1250 → użyj UTF-8 bez BOM.
* Niespójna liczba kolumn vs `:widths:`.
* Zły separator — ustaw `:delim:`.

