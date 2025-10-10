# Przykład: CSV → tabela

```{csv-table} Zależności modułów
:header: Moduł, Zależy od
:widths: 30, 70
:file: ../assets/samples/deps.csv
:delim: ,
```

:::note
Pliki CSV są przechowywane w `docs/assets/samples/` i mogą być łatwo aktualizowane bez modyfikacji dokumentacji.
:::

(csv-usage)=
## Jak używać CSV w dokumentacji

Aby dodać tabelę CSV do dokumentacji, użyj dyrektywy `csv-table`:

````markdown
```{csv-table} Tytuł tabeli
:header: Kolumna1, Kolumna2
:widths: 50, 50
:file: ../assets/samples/your_file.csv
:delim: ,
```
````

(csv-best-practices)=
## Dobre praktyki

1. **Nagłówki** - zawsze używaj wiersza nagłówkowego w CSV
2. **Separatory** - używaj przecinka (`,`) jako separatora
3. **Encoding** - pliki CSV powinny być w UTF-8
4. **Szerokości** - dostosuj `:widths:` do zawartości kolumn
5. **Lokalizacja** - przechowuj CSV w `docs/assets/samples/`

(see-also-csv)=
## Zobacz też

* [Diagramy](diagrams.md) - wizualizacje graficzne
* [Datasets](../datasets/index.md) - większe zbiory danych
* [Moduły](../chapters/03_modules.md) - dokumentacja modułów
