# System Projektowania Diagramów: Przewodnik dla Twórców

## 1. Wprowadzenie

Witaj w systemie projektowania diagramów. Ten zbiór dokumentów stanowi kompletny przewodnik do tworzenia spójnych, czytelnych i semantycznie bogatych diagramów Mermaid dla naszego projektu. Został zaprojektowany tak, aby mógł być interpretowany zarówno przez ludzi, jak i przez zautomatyzowanych agentów AI.

**Celem tego systemu jest transformacja diagramów z pasywnych ilustracji w aktywne narzędzia inżynierskie.**

## 2. Architektura Systemu

Ten system składa się z trzech fundamentalnych filarów, które razem tworzą kompletny framework:

1.  **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**: **"Dlaczego?"** - Definiuje nasze podstawowe zasady myślowe. Przeczytaj go, aby zrozumieć, co sprawia, że diagram jest skuteczny.
2.  **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)**: **"Jak ma wyglądać?"** - Ścisła specyfikacja techniczna wszystkich elementów wizualnych (kolory, ikony, style). To jest Twoja paleta narzędzi.
3.  **Biblioteka Wzorców Projektowych (poniżej)**: **"Jak to zrobić?"** - Zbiór gotowych do użycia, praktycznych wzorców dla najczęstszych zadań. To Twoja książka kucharska.

---

## 3. Biblioteka Wzorców Projektowych

### 3.1. Cel Biblioteki

Ta biblioteka to zbiór gotowych do użycia wzorców ("przepisów") dla szerokiej gamy zadań wizualizacyjnych. Odpowiada na dwa pytania:
*   **Co chcę pokazać?** → Jaki typ diagramu wybieram?
*   **Jak to narysować, żeby było spójne, czytelne i interaktywne?**

### 3.2. Standardy Globalne
Obowiązują dla wszystkich przykładów oraz dla nowo tworzonych diagramów.

*   **Blok Inicjalizujący (`init`):**
    *   Każdy diagram Mermaid musi zaczynać się od prefiksu: `%%{init: {'theme': 'dark'}}%%`.
*   **Interaktywność (`click`):**
    *   Stosuj `click` tam, gdzie jest to wspierane, do linkowania do innych sekcji lub dokumentów.
    *   Diagram musi pozostać czytelny, nawet jeśli `click` nie zadziała w danym rendererze.
*   **Rozbijanie Złożoności:**
    *   Zamiast jednego przeładowanego diagramu, preferuj system: jeden diagram `overview` + kilka diagramów szczegółowych, połączonych linkami.

### 3.3. Indeks i Zasady Doboru Diagramu

Poniżej znajduje się indeks do plików z wzorcami oraz zasady, jak i kiedy używać każdego typu diagramu w kontekście tego projektu.

#### **[Część A: Przepływy i Procesy](./03_DESIGN_PATTERNS/A_Flows_and_Processes.md)**
*   **Zasady:** Używaj do wizualizacji logiki, interakcji w czasie i przepływu sterowania. Nie rysuj tu statycznej architektury.
*   **Zawiera wzorce dla:** `flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `journey`, `sankey-beta`.

#### **[Część B: Struktura i Relacje](./03_DESIGN_PATTERNS/B_Structure_and_Relations.md)**
*   **Zasady:** Używaj do pokazywania statycznej architektury, hierarchii i relacji między komponentami.
*   **Zawiera wzorce dla:** `flowchart` (symulujący `classDiagram`), `erDiagram`, `mindmap`.

#### **[Część C: Czas i Planowanie](./03_DESIGN_PATTERNS/C_Time_and_Planning.md)**
*   **Zasady:** Używaj, gdy oś czasu (historycznego lub w milisekundach) jest kluczowym wymiarem.
*   **Zawiera wzorce dla:** `timeline`, `gantt`, `gitGraph`.

#### **[Część D: Wizualizacja Danych i Analiza](./03_DESIGN_PATTERNS/D_Data_and_Analysis.md)**
*   **Zasady:** Używaj do prezentacji danych ilościowych, proporcji i jako wsparcie w podejmowaniu decyzji strategicznych.
*   **Zawiera wzorce dla:** `pie`, `quadrantChart`, `xychart-beta`.

#### **[Część E: Techniki Zaawansowane](./03_DESIGN_PATTERNS/E_Advanced_Techniques.md)**
*   **Zasady:** Używaj do tworzenia połączonych, wielopoziomowych systemów wizualizacji, które prowadzą użytkownika od ogółu do szczegółu.
*   **Zawiera wzorzec:** Złożonej Wizualizacji (Łączenie Diagramów).

### 3.4. Meta-Zasada: Jak Wybrać Właściwe Narzędzie?
1.  Najpierw zadaj pytanie: **Co chcę pokazać?** Strukturę, czas, przepływ, decyzję, priorytet czy historię?
2.  Następnie dobierz typ diagramu z powyższego indeksu.
3.  Pamiętaj: **Każdy diagram ma mieć jedno, jasne zadanie.** Jeśli staje się przeładowany i próbuje robić wszystko naraz, należy go uprościć lub podzielić na kilka mniejszych.

## 4. Indeks Wzorców

### Część A: Przepływy i Procesy

1. [Wzorzec Przepływu Danych (`flowchart`)](#wzorzec-przeplywu-danych-flowchart)
2. [Wzorzec Sekwencji Interakcji (`sequenceDiagram`)](#wzorzec-sekwencji-interakcji-sequencediagram)
3. [Wzorzec Maszyny Stanów (`stateDiagram-v2`)](#wzorzec-maszyny-stanow-statediagram-v2)
4. [Wzorzec Podróży Użytkownika/Systemu (`journey`)](#wzorzec-podrozy-uzytkownikasystemu-journey)
5. [Wzorzec Analizy Przepływu Zasobów (`sankey-beta`)](#wzorzec-analizy-przeplywu-zasobow-sankey-beta)

### Część B: Struktura i Relacje

6. [Wzorzec Struktury Klas (`classDiagram`)](#wzorzec-struktury-klas-classdiagram)
7. [Wzorzec Modelu Danych (`erDiagram`)](#wzorzec-modelu-danych-erdiagram)
8. [Wzorzec Mapy Myśli (`mindmap`)](#wzorzec-mapy-mysli-mindmap)

### Część C: Czas i Planowanie

9. [Wzorzec Osi Czasu Zdarzeń (`timeline`)](#wzorzec-osi-czasu-zdarzen-timeline)
10. [Wzorzec Harmonogramu Projektu (`gantt`)](#wzorzec-harmonogramu-projektu-gantt)
11. [Wzorzec Historii Wersji (`gitGraph`)](#wzorzec-historii-wersji-gitgraph)

### Część D: Wizualizacja Danych i Analiza

12. [Wzorzec Dystrybucji Danych (`pie`)](#wzorzec-dystrybucji-danych-pie)
13. [Wzorzec Analizy Strategicznej (`quadrantChart`)](#wzorzec-analizy-strategicznej-quadrantchart)
14. [Wzorzec Danych XY (`xychart-beta`)](#wzorzec-danych-xy-xychart-beta)

### Część E: Techniki Zaawansowane

15. [Złożony Wzorzec Wizualizacji (Łączenie Diagramów)](#zlozony-wzorzec-wizualizacji-laczenie-diagramow)
