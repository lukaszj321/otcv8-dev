# Dashboard

Poniżej przykład rozkładu „dwóch kolumn” z mieszanymi treściami: wykres (placeholder), lista linków i diagram.

:::{grid} 2
:gutter: 2

:::{grid-item}
:columns: 8

## Kafle szybkich akcji
:::{card} 📚 API
:link: ../api/index.html
Dokumentacja API (surowe i generowane).
:::

:::{card} 🧠 RAG
:link: ../rag/index.html
Wyszukiwanie semantyczne, przykłady i CLI.
:::

:::{card} 🧩 Moduły
:link: ../index.html
Przegląd komponentów i modułów.
:::

:::

:::{grid-item}
:columns: 4

## Diagram (Mermaid)
```{mermaid}
flowchart TD
    A[Start] --> B{Wybierz sekcję}
    B -->|API| C[API Docs]
    B -->|RAG| D[RAG Search]
    B -->|UI| E[UI/Modules]
```

:::
:::
