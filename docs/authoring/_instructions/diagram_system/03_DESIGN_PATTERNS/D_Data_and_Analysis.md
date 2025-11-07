## Część D: Wizualizacja Danych i Analiza

### Wzorzec Dystrybucji Danych (`pie`)

`pie` służy do pokazania **proporcji** w jednym wymiarze. Jest prosty, ograniczony i dokładnie o to chodzi.

**Kiedy stosować:**

- udział typów błędów,
- udział platform / środowisk,
- udział modułów w ruchu / zdarzeniach / ticketach,
- szybki „snapshot” bez potrzeby pełnego `sankey-beta`.

> Jeśli zaczynasz kombinować z więcej niż 6–7 kategoriami, użyj czegoś innego.

---

#### Wariant 1: Typy Błędów w Kliencie

**Cel:** Pokazać, co naprawdę psuje użytkownikom dzień.

```mermaid
%%{init: {'theme': 'dark'}}%%
pie showData
    title Error Types Share
    "Validation" : 40
    "Network" : 25
    "Auth" : 20
    "Other" : 15
```

**Jak użyć:**
Opis pod spodem: dane z crash reporter + logów za ostatni okres. Szybki argument, gdzie inwestować w stabilizację.

---

#### Wariant 2: Udział Platform / Środowisk

**Cel:** Pokazać, gdzie OTClient jest realnie używany.

```mermaid
%%{init: {'theme': 'dark'}}%%
pie showData
    title Client Sessions by Platform
    "Windows" : 65
    "Linux" : 20
    "macOS" : 10
    "Other" : 5
```

**Jak użyć:**
Uzasadnia priorytety: testy, optymalizacje, bugfixy per platforma, bez wypisywania tego w tabelkach.

---

#### Wariant 3: Udział Modułów w Zgłoszeniach Bugów

**Cel:** Pokazać, które obszary kodu generują najwięcej problemów.

```mermaid
%%{init: {'theme': 'dark'}}%%
pie showData
    title Bug Reports by Module
    "UI" : 30
    "Network" : 25
    "Inventory" : 15
    "Rendering" : 20
    "Other" : 10
```

**Jak użyć:**

* Pomaga zdecydować, które moduły docelowo dostać:

  * więcej testów,
  * więcej dokumentacji,
  * własne diagramy (`flowchart`, `sequenceDiagram`).

---

To wystarczy. `pie` jest narzędziem jednowymiarowym. Jak tylko próbujesz pokazać coś bardziej złożonego niż „udział X w Y”, przesiadasz się na `sankey-beta`, `xychart-beta` albo `quadrantChart`.


---

### Wzorzec Analizy Strategicznej (`quadrantChart`)

`quadrantChart` służy do podejmowania decyzji na podstawie **dwóch wymiarów**. Typowe zastosowania:

- wartość vs złożoność,
- ryzyko vs krytyczność,
- pokrycie testami vs złożoność,
- wpływ na użytkownika vs koszt utrzymania.

Dobre tam, gdzie normalnie robisz tabelkę „Feature / Value / Cost / Risk”, a każdy interpretuje ją inaczej.

> Jeśli Twój renderer nie wspiera `quadrantChart`, traktuj ten wzorzec jako opcjonalny.

---

#### Wariant 1: Priorytetyzacja Feature’ów OTClienta

**Cel:** Określić, które funkcje robić najpierw, patrząc na stosunek wartości do złożoności.

```mermaid
%%{init: {
  "theme": "dark",
  "quadrantChart": {
    "chartWidth": 600,
    "chartHeight": 380,
    "titleFontSize": 18,
    "quadrantLabelFontSize": 13,
    "xAxisLabelFontSize": 12,
    "yAxisLabelFontSize": 12,
    "quadrantInternalBorderStrokeWidth": 1,
    "quadrantExternalBorderStrokeWidth": 2,
    "xAxisPosition": "bottom",
    "yAxisPosition": "left"
  }
}}%%
quadrantChart
    title Feature Prioritization (Value vs Complexity)
    x-axis Low Complexity --> High Complexity
    y-axis Low Value --> High Value

    quadrant-1 Quick Wins
    quadrant-2 Strategic Bets
    quadrant-3 Fillers
    quadrant-4 Avoid

    "Improved Logging UI": [0.2, 0.7]
    "Inventory QoL": [0.3, 0.9]
    "New Theme System": [0.6, 0.8]
    "Full Engine Rewrite": [0.95, 0.6]
    "Obscure Debug Panel": [0.4, 0.2]
```

**Jak użyć:**

* Quick Wins (Q1) → kandydaci na najbliższy sprint.
* Q2 → wysoka wartość, ale wymagają decyzji architektonicznej.
* Q4 → kulturalny parking dla pomysłów, których nie warto ruszać.

---

#### Wariant 2: Tech Debt vs Ryzyko Produkcyjne

**Cel:** Pokazać, które długi techniczne są realnym zagrożeniem, a które są tylko estetycznym wstydem.

```mermaid
%%{init: {'theme': 'dark'}}%%
quadrantChart
    title Tech Debt (Risk vs Criticality)
    x-axis Low Risk --> High Risk
    y-axis Cosmetic --> Critical

    quadrant-1 Monitor
    quadrant-2 Fix Soon
    quadrant-3 Low Priority
    quadrant-4 Immediate Action

    "Legacy NetClient": [0.9, 0.95]
    "Ad-hoc Logging": [0.7, 0.8]
    "Old UI Skin Code": [0.2, 0.2]
    "Custom Build Script": [0.4, 0.5]
```

**Jak użyć:**

* Q4 → tu pakujesz czas najpierw, bez dyskusji.
* Q1 → obserwuj, ale nie dramatyzuj.
* Zastępuje losowe listy „critical/high/medium/low”.

---

#### Wariant 3: Moduły vs Testowalność / Złożoność

**Cel:** Wskazać moduły wymagające testów, dokumentacji i diagramów w pierwszej kolejności.

```mermaid
%%{init: {'theme': 'dark'}}%%
quadrantChart
    title Modules (Coverage vs Complexity)
    x-axis Low Coverage --> High Coverage
    y-axis Low Complexity --> High Complexity

    quadrant-1 Safe Zone
    quadrant-2 Overprotected
    quadrant-3 Blind Spot
    quadrant-4 Critical Risk

    "Core Engine": [0.3, 0.9]
    "Modules System": [0.4, 0.8]
    "UI Layouts": [0.7, 0.5]
    "Network Layer": [0.2, 0.8]
    "Assets Tools": [0.6, 0.4]
```

**Jak użyć:**

* Q3 + Q4 → lista miejsc do:

  * dopisania testów,
  * opisania w dokumentacji,
  * narysowania (`flowchart`, `sequenceDiagram`).
* Diagram działa jako radar, gdzie realnie przyłożyć wysiłek.

---

### Zasady użycia `quadrantChart` w tej dokumentacji

* Stosuj, gdy masz N opcji i 2 sensowne osie porównania.
* Nie stosuj, gdy opisujesz:

  * czas (`timeline`),
  * przepływy (`sankey-beta`),
  * strukturę (`classDiagram`, `erDiagram`).

---

### Wzorzec Danych XY (`xychart-beta`)

**Kiedy:** Wydajność, metryki, trendy, porównanie stanu realnego z celem i kosztu (np. obciążenie GPU).

```mermaid
%%{init: {'theme': 'dark'}}%%
xychart-beta
    title "FPS vs Objects (detailed)"
    x-axis "Objects" [0, 100, 500, 1000, 2000]
    y-axis "FPS" 0 --> 140

    %% Główna linia: realnie zmierzony FPS
    line "Measured FPS" [120, 115, 95, 70, 40]

    %% Linia referencyjna: oczekiwany minimalny poziom
    line "Target 90 FPS" [90, 90, 90, 90, 90]

    %% Słupki: obciążenie GPU w % przy tych samych punktach pomiarowych
    bar "GPU Load (%)" [20, 35, 55, 75, 95]
```

Legenda (opis pod diagramem, nie w kodzie):

* **Measured FPS** – realne wyniki benchmarku klienta.
* **Target 90 FPS** – minimalny akceptowalny poziom wydajności.
* **GPU Load (%)** – koszt osiągnięcia danego FPS przy rosnącej liczbie obiektów.

> Uwaga: `xychart-beta` nie wspiera `click` w sposób stabilny w każdym rendererze. Jeśli potrzebujesz nawigacji, dodaj linki Markdown w tekście obok wykresu (np. do rozdziału o benchmarkach lub optymalizacjach).mermaid
> %%{init: {'theme': 'dark'}}%%

> xychart-beta

> title "FPS vs Objects"

> x-axis "Objects" 0 2000

> y-axis "FPS" 0 140

> line "FPS"
> 0 120
> 100 115
> 500 95
> 1000 70
> 2000 40
