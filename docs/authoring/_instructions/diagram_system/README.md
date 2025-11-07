# System Projektowania Diagramów: Przewodnik dla Twórców

## 1. Wprowadzenie

Witaj w systemie projektowania diagramów. Ten zbiór dokumentów stanowi kompletny przewodnik do tworzenia spójnych, czytelnych i semantycznie bogatych diagramów Mermaid dla naszego projektu. Został zaprojektowany tak, aby mógł być interpretowany zarówno przez ludzi, jak i przez zautomatyzowanych agentów AI.

**Celem tego systemu jest transformacja diagramów z pasywnych ilustracji w aktywne narzędzia inżynierskie.**

## 2. Struktura Systemu

Ten system składa się z trzech fundamentalnych filarów, które razem tworzą kompletny, hierarchiczny framework:

*   **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**: **"Dlaczego?"** - Definiuje nasze podstawowe zasady myślowe. Przeczytaj go, aby zrozumieć, co sprawia, że diagram jest skuteczny.

*   **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)**: **"Jak ma wyglądać?"** - Ścisła specyfikacja techniczna wszystkich elementów wizualnych (kolory, ikony, style). To jest Twoja paleta narzędzi.

*   **[Biblioteka Wzorców Projektowych](./03_DESIGN_PATTERNS/) (`03_DESIGN_PATTERNS/`)**: **"Jak to zrobić?"** - Zbiór gotowych do użycia, praktycznych wzorców. Działa jak "książka kucharska" dla twórców diagramów. Składa się z następujących plików:
    *   **[README.md](./03_DESIGN_PATTERNS/README.md):** Główny **spis treści** i przewodnik po całej bibliotece wzorców. **Zawsze zaczynaj tutaj.**
    *   **[A_Flows_and_Processes.md](./03_DESIGN_PATTERNS/A_Flows_and_Processes.md):** Wzorce do wizualizacji dynamicznych procesów, logiki i interakcji w czasie (`flowchart`, `sequenceDiagram`, etc.).
    *   **[B_Structure_and_Relations.md](./03_DESIGN_PATTERNS/B_Structure_and_Relations.md):** Wzorce do pokazywania statycznej architektury i relacji (`classDiagram`, `erDiagram`).
    *   **[C_Time_and_Planning.md](./03_DESIGN_PATTERNS/C_Time_and_Planning.md):** Wzorce do wizualizacji harmonogramów i zdarzeń w czasie (`gantt`, `timeline`).
    *   **[D_Data_and_Analysis.md](./03_DESIGN_PATTERNS/D_Data_and_Analysis.md):** Wzorce do prezentacji danych ilościowych i analizy strategicznej (`pie`, `quadrantChart`).
    *   **[E_Advanced_Techniques.md](./03_DESIGN_PATTERNS/E_Advanced_Techniques.md):** Wzorce pokazujące, jak łączyć różne typy diagramów w spójne systemy.

## 3. Proces Tworzenia Wizualizacji: Algorytm dla AI i Deweloperów

Aby stworzyć nową wizualizację, postępuj zgodnie z poniższym, strategicznym procesem. Na końcu tego dokumentu znajduje się **[Checklista Jakości](#4-checklista-jakości-diagramu)**, której należy użyć do weryfikacji finalnego rezultatu.

### Krok 1: Analiza i Definicja Celu
Zanim napiszesz kod, odpowiedz: Co chcę pokazać? Jaka jest główna "historia"? Do której warstwy architektonicznej należy główny komponent?

### Krok 2: Wybór Strategii — Jeden Diagram czy System Diagramów?
To jest najważniejsza decyzja projektowa. Zgodnie z naszą Złotą Regułą: **Nigdy nie twórz "Boskiego Diagramu"**.

*   **Scenariusz A (Prosty):** Tworzysz jeden, skupiony diagram.
*   **Scenariusz B (Złożony):** Projektujesz system połączonych diagramów (np. `overview` + `details`).

### Krok 3: Wybór Wzorca Projektowego
Przejdź do **[indeksu biblioteki wzorców](./03_DESIGN_PATTERNS/README.md)**, wybierz odpowiednią kategorię i plik, a następnie zaadaptuj wariant, który najlepiej pasuje do diagramu, który aktualnie tworzysz.

### Krok 4: Implementacja i Zastosowanie Stylu
Napisz kod Mermaid, implementując strukturę z wzorca i stosując style z **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)**.

### Krok 5: Przegląd i Refaktoryzacja
Sprawdź, czy diagram jest czytelny i zgodny z zasadami z **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**.

### Krok 6: Kompozycja Wizualna (dla Scenariusza B)
Jeśli projektujesz system diagramów, zaplanuj, jak zostaną one ułożone na stronie, używając jednej z technik kompozycji (np. Wiele Perspektyw, Deska Rozdzielcza).

---

## 4. Checklista Jakości Diagramu

Użyj tej checklisty przed zatwierdzeniem każdego nowego diagramu. Diagram jest gotowy, jeśli możesz odpowiedzieć "TAK" na wszystkie poniższe pytania.

### Część 1: Filozofia i Cel
-   [ ] **Jedna Historia:** Czy diagram opowiada jedną, jasno zdefiniowaną historię?
-   [ ] **Czytelność w 5 Sekund:** Czy główny cel i kluczowe komponenty są zrozumiałe na pierwszy rzut oka?
-   [ ] **Wartość Dodana:** Czy diagram wizualizuje coś, czego nie widać od razu po przeczytaniu kodu (np. relacje, przepływy)?
-   [ ] **Odpowiednie Narzędzie:** Czy typ diagramu (np. `flowchart`, `sequenceDiagram`) jest właściwie dobrany do "historii", którą opowiada?

### Część 2: Zgodność z Systemem Wizualnym
-   [ ] **Globalny `init`:** Czy diagram zaczyna się od standardowego bloku `%%{init: {'theme': 'dark', ...}}%%`?
-   [ ] **Kolory Warstw:** Czy wszystkie węzły `graph` mają poprawnie przypisany kolor warstwy architektonicznej (np. `core`, `game`, `ui`)?
-   [ ] **Ikony Komponentów:** Czy kluczowe węzły mają przypisane ikony (`fa-...`) zgodnie z ich techniczną rolą?
-   [ ] **Style Linii:** Czy style linii (`-->`, `-.->`, `==>`) i ich kolory (`linkStyle`) są użyte poprawnie i zgodnie ze znaczeniem?
-   [ ] **Zgodność z Ograniczeniami:** Czy diagram przestrzega ograniczeń stylizacji dla swojego typu (np. nie używa `classDef` w `sequenceDiagram`)?

### Część 3: Poprawność i Kompletność
-   [ ] **Renderowanie:** Czy diagram renderuje się poprawnie bez błędów parsera?
-   [ ] **Poprawność Merytoryczna:** Czy diagram wiernie odzwierciedla działanie lub strukturę opisywanego systemu?
-   [ ] **Interaktywność:** Czy kluczowe komponenty mają dodane linki `click` (jeśli są wspierane) do odpowiedniej dokumentacji?
-   [ ] **Kontekst:** Czy pod diagramem (lub w jego tytule) znajduje się krótki opis wyjaśniający, co on przedstawia i jaka jest używana jednostka (dla diagramów analitycznych)?

### Część 4: Kompozycja (jeśli dotyczy)
-   [ ] **Podział Złożoności:** Jeśli diagram jest bardzo skomplikowany, czy na pewno nie powinien być podzielony na mniejszy system `overview` + `details`?
-   [ ] **Spójność Systemu:** Jeśli diagram jest częścią większego systemu wizualizacji, czy jego linki i narracja są spójne z pozostałymi częściami?
