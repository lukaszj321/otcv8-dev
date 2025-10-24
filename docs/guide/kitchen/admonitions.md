# Admonitions (kitchen-sink)

Upewnij się, że w `conf.py` masz `myst_enable_extensions = ["colon_fence"]`.

---

:::{warning} Uwaga
Ważny komunikat.
:::

:::{note} Info (prosta notka)
To jest zwykła notka informacyjna.
:::

:::{tip} Wskazówka
Możesz używać **skrótów klawiaturowych** i *snippetów* w edytorze.

* `Ctrl+K` – szybkie polecenia
* `Ctrl+/` – komentarz
  :::

:::{important} Ważne
Zawsze aktualizuj zależności przed buildem: `pip install -U -r requirements.txt`.
:::

:::{hint} Podpowiedź
Admonitions mogą zawierać bloki kodu i listy.

```bash
make clean && make html
```

:::

:::{warning} Uwaga
Zbyt agresywne cache może powodować **stare** artefakty. Wyczyść `_build/` i `.doctrees/`.
:::

:::{caution} Ostrożnie
Nie mieszaj składni ``mermaid` z ``{mermaid}` w jednym pliku – wybierz **jedną**.
:::

:::{attention} Zwróć uwagę
`stateDiagram-v2` wymaga Mermaid ≥ 10. Ustaw w `conf.py`: `mermaid_version = "10.9.1"`.
:::

:::{error} Błąd
Brak rozszerzenia `sphinxcontrib-mermaid` w `extensions` → diagramy nie renderują się.
:::

:::{danger} Niebezpieczeństwo
Usuwanie `_build/` w złym katalogu może skasować Twoje artefakty CI.
:::

:::{admonition} FAQ — najczęstsze pytania
**P:** Czy mogę wstawić tabelę?

**O:** Tak:

|  Klucz | Wartość |
| -----: | :------ |
|   tema | dark    |
| wersja | 10.9.1  |
|    ::: |         |

:::{admonition} Z kodem (Python)
:class: tip

```python
def hello(name: str) -> str:
    return f"Hello, {name}!"

print(hello("OTClient v8"))
```

:::

:::{admonition} Zagnieżdżone bloki
Możesz łączyć różne elementy:

* lista
* kod

```md
:::{note} Wewnątrz
To też działa.
:::
```

:::

:::{admonition} Styl własny przez klasę
:class: warning my-extra-class
Dodatkowe klasy możesz ostylować w CSS motywu.
:::

:::{admonition} Z kotwicą do linkowania
:name: adm-example-anchor
Ten blok ma stałą kotwicę. Link: `[skocz tutaj](#adm-example-anchor)`.
:::

:::{admonition} Porównanie wariantów
**Kiedy użyć `note`?** Gdy przekazujesz neutralną informację.

**Kiedy `warning`?** Gdy istnieje ryzyko błędu.

**Kiedy `important`?** Gdy coś jest kluczowe dla poprawnego działania.
:::
