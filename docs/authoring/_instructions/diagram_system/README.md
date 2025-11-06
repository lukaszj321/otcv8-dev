# System Projektowania Diagramów: Przewodnik dla Twórców

## 1. Wprowadzenie

Witaj w systemie projektowania diagramów. Ten zbiór dokumentów stanowi kompletny przewodnik do tworzenia spójnych, czytelnych i semantycznie bogatych diagramów Mermaid dla naszego projektu. Został zaprojektowany tak, aby mógł być interpretowany zarówno przez ludzi, jak i przez zautomatyzowanych agentów AI.

**Celem tego systemu jest transformacja diagramów z pasywnych ilustracji w aktywne narzędzia inżynierskie.**

## 2. Struktura Systemu

Ten system składa się z trzech fundamentalnych dokumentów, które razem tworzą kompletny framework:

*   **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**: **"Dlaczego?"** - Definiuje nasze podstawowe zasady i cele. Przeczytaj go, aby zrozumieć, co sprawia, że diagram jest skuteczny.
*   **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)**: **"Co?"** - Ścisła specyfikacja techniczna wszystkich elementów wizualnych (kolory, ikony, style linii). To jest Twoja paleta narzędzi.
*   **[03_DESIGN_PATTERNS.md](./03_DESIGN_PATTERNS.md)**: **"Jak?"** - Zbiór gotowych wzorców projektowych dla najczęstszych typów komponentów. To Twoja książka kucharska.

## 3. Proces Tworzenia Diagramu: Algorytm dla AI i Deweloperów

Aby stworzyć nowy diagram, postępuj zgodnie z poniższym, pięciostopniowym procesem. Ten algorytm gwarantuje, że każdy diagram będzie spełniał nasze standardy jakości.

### Krok 1: Analiza Komponentu i Zdefiniowanie "Historii"

Zanim napiszesz jakikolwiek kod, odpowiedz na te pytania:
1.  **Jaka jest główna rola tego komponentu?** (np. zarządza cyklem życia, transformuje dane, obsługuje UI).
2.  **Jaka jest jedna, najważniejsza informacja, którą diagram ma przekazać?** To jest Twoja "historia".
3.  Do której **Warstwy Architektonicznej** należy komponent? (Sprawdź w `02_VISUAL_GUIDELINES.md`).

### Krok 2: Wybór Wzorca Projektowego

Na podstawie analizy z Kroku 1, przejdź do dokumentu **[03_DESIGN_PATTERNS.md](./03_DESIGN_PATTERNS.md)** i wybierz wzorzec, który najlepiej pasuje do roli Twojego komponentu.
*   Czy jest to menedżer? Użyj **Wzorca Menedżera Cyklem Życia**.
*   Czy transformuje dane? Użyj **Wzorca Przepływu Danych/Potoku**.
*   Czy to widget UI? Użyj **Wzorca Komponentu UI**.
*   ...i tak dalej.

Wybrany wzorzec da Ci podstawową strukturę, rekomendowaną orientację (`TD` lub `LR`) i kluczowe elementy do uwzględnienia.

### Krok 3: Implementacja Struktury i Treści

Napisz szkielet diagramu Mermaid, implementując strukturę z wybranego wzorca. Wypełnij go konkretnymi nazwami funkcji, zdarzeń i komponentów. Na tym etapie skup się na logice i treści, nie na wyglądzie.

### Krok 4: Zastosowanie Stylu Wizualnego

Teraz otwórz **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)** i zastosuj odpowiednie style do każdego elementu diagramu:
1.  Przypisz **kolor warstwy** do wszystkich węzłów.
2.  Dodaj **ikonę typu komponentu** do każdego węzła.
3.  Użyj odpowiednich **stylów linii** do pokazania natury połączeń (np. synchroniczne, asynchroniczne).
4.  Dodaj interaktywne **linki (`click`)** do odpowiedniej dokumentacji API.

### Krok 5: Przegląd i Refaktoryzacja

Na koniec, dokonaj przeglądu swojego dzieła w świetle zasad z **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**.
*   Czy diagram jest czytelny i nieprzeładowany?
*   Czy opowiada jedną, spójną "historię"?
*   Czy nie próbuje pokazać zbyt wiele naraz? (Jeśli tak, rozważ podzielenie go na kilka mniejszych diagramów).
