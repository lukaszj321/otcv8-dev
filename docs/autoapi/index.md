---
title: API (Auto) — C++ + Lua src i modules
---

# API (Auto) — `src` i `modules`

Dwa **oddzielne** zbiory dokumentacji, widoczne w tej sekcji:

## 1) `src` — C++ **+** Lua

* **C++ (Exhale/Breathe/Doxygen)** → {doc}`autoapi/cpp/index`
* **Lua (LDoc)** → <../_extra/ldoc-src/index.html>

```{toctree}
:maxdepth: 2
:caption: C++ (`src`) – Exhale
autoapi/cpp/index
```

---

## 2) `modules` — Lua **+** OTUI **+** OTMOD

* **Lua (LDoc)** → <../_extra/ldoc-modules/index.html>
* **OTUI/OTMOD**: renderuj jako *literalny tekst* (whitespace‑sensitive).

:::{admonition} Uwaga (OTUI/OTMOD)
:class: warning
* Nie używaj autoformatu.
* Wstawiaj jako `{code-block} text` albo `.. literalinclude::`.
* Wyłącz narzędzia, które modyfikują blok.
:::
