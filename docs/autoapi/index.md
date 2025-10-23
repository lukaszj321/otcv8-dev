# API (Auto) — `src` i `modules`

Dwa **oddzielne** zbiory dokumentacji. Wybierz odpowiedni zestaw w zależności od źródeł.

## 1) `src` — C++ **+** Lua (jeden pakiet)

* **C++ (Breathe/Doxygen)** → {doc}`autoapi/cpp/index`
* **Lua (LDoc)** → [otwórz LDoc dla `src/`](../_extra/ldoc-src/index.html)

```{toctree}
:maxdepth: 2
:caption: C++ z `src/`

autoapi/cpp/index
```

:::{admonition} Uwaga
`src` i `modules` są trzymane **rozdzielnie**. Linki krzyżowe między nimi dodawaj ręcznie w treści stron.
:::

---

## 2) `modules` — Lua **+** OTUI **+** OTMOD

* **Lua (LDoc)** → [otwórz LDoc dla `modules/`](../_extra/ldoc-modules/index.html)
* **OTUI/OTMOD**: nie parsujemy automatycznie; renderujemy *dosłownie* (whitespace‑sensitive).

:::{admonition} OTUI/OTMOD — whitespace‑sensitive
:class: warning

* Każdy znak ma znaczenie (spacje, taby, nowe linie).
* Prezentuj jako tekst literalny (`{code-block} text` lub `.. literalinclude::`).
* Nie używaj autoformatowania, code‑autolink i wymuszonych lexerów.
  :::

# API (Auto) — `src` i `modules`

Dwa **oddzielne** zbiory dokumentacji. Wybierz odpowiedni zestaw w zależności od źródeł.

## 1) `src` — C++ **+** Lua (jeden pakiet)

* **C++ (Breathe/Doxygen)** → {doc}`autoapi/cpp/index`
* **Lua (LDoc)** → [otwórz LDoc dla `src/`](../_extra/ldoc-src/index.html)

```{toctree}
:maxdepth: 2
:caption: C++ z `src/`

autoapi/cpp/index
```

:::{admonition} Uwaga
`src` i `modules` są trzymane **rozdzielnie**. Linki krzyżowe między nimi dodawaj ręcznie w treści stron.
:::

---

## 2) `modules` — Lua **+** OTUI **+** OTMOD

* **Lua (LDoc)** → [otwórz LDoc dla `modules/`](../_extra/ldoc-modules/index.html)
* **OTUI/OTMOD**: nie parsujemy automatycznie; renderujemy *dosłownie* (whitespace‑sensitive).

:::{admonition} OTUI/OTMOD — whitespace‑sensitive
:class: warning

* Każdy znak ma znaczenie (spacje, taby, nowe linie).
* Prezentuj jako tekst literalny (`{code-block} text` lub `.. literalinclude::`).
* Nie używaj autoformatowania, code‑autolink i wymuszonych lexerów.
  :::

---

## Diagramy — `modules`

**Statyczny DAG modułów (DOT):**

```{literalinclude} ../diagrams/modules_repo_dag.dot
:language: text
:caption: Graf zależności modułów (DOT)
```

**Wersja Mermaid (źródło):**

```{literalinclude} ../diagrams/modules_repo_dag.mmd
:language: text
:caption: Graf zależności modułów (Mermaid)
```

**Wersja Mermaid (osadzona):**

```{mermaid}
%%{init:{'theme':'dark'}}%%
%% Klikalne węzły mogą być podmieniane w CI (scripts/patch_diagrams_clicks.py)
graph TD
  A[client] -->|depends| B[corelib]
  A --> C[client_topmenu]
  C --> D[game_interface]
```

:::{admonition} Ścieżki bez spacji
Pliki trzymaj w `docs/diagrams/` i odwołuj się względnie z `autoapi/` jako `../diagrams/...`.
:::

---

## Diagramy — `src`

**Graf include (C/C++):**

```{literalinclude} ../diagrams/src_include_graph.dot
:language: text
:caption: Graf zależności #include (DOT)
```

**Graf wywołań (heurystyczny):**

```{literalinclude} ../diagrams/src_call_graph.dot
:language: text
:caption: Graf wywołań funkcji (DOT)
```

:::{admonition} Uwaga
Te pliki `.dot/.mmd` są opcjonalne — jeśli ich nie ma, sekcja się zbuduje, ale bez podglądu. Dodaj je do `docs/diagrams/`.
:::
