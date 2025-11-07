# Filozofia Projektowania Diagramów: Instrukcja Operacyjna

## 1. Wprowadzenie: Cel i Nadrzędna Dyrektywa

### 1.1. Cel Dokumentu
Ten dokument definiuje **fundamentalne zasady myślowe** i **strategiczne cele**, które stoją za każdym diagramem w tym projekcie. Nie jest to specyfikacja techniczna, lecz **przewodnik po procesie twórczym** – nasze "Dlaczego?". Ma on na celu zapewnienie, że każdy diagram jest nie tylko technicznie poprawny, ale przede wszystkim **użyteczny, klarowny i celowy**.

### 1.2. Nadrzędna Dyrektywa
**Twoim zadaniem NIE jest tworzenie graficznej reprezentacji kodu. Twoim zadaniem jest TWORZENIE WIEDZY poprzez wizualizację ukrytych relacji, procesów i kontekstu.** Diagram, który tylko listuje metody klasy, jest porażką. Diagram, który wyjaśnia, *jak* i *dlaczego* ta klasa działa z innymi, jest sukcesem.

---

## 2. Pięć Filarów Doskonałego Diagramu

Każdy diagram, który tworzysz, musi opierać się na pięciu fundamentalnych filarach. Zignorowanie któregokolwiek z nich prowadzi do powstania bezwartościowej wizualizacji.

### Filar #1: Opowiadaj Jedną, Spójną Historię
*   **Zasada:** Każdy diagram musi mieć jeden, jasno zdefiniowany cel i opowiadać jedną, spójną historię.
*   **W praktyce:** Przed rozpoczęciem pracy, zdefiniuj tę historię w jednym zdaniu. Jeśli diagram próbuje opowiedzieć kilka historii naraz, **musisz go podzielić** (patrz Sekcja 3).

### Filar #2: Optymalizuj pod Kątem Zrozumienia w 5 Sekund
*   **Zasada:** Diagram musi być zaprojektowany tak, aby jego główny cel i kluczowe komponenty były zrozumiałe na pierwszy rzut oka.
*   **W praktyce:** Zawsze i bezwzględnie stosuj nasz system wizualny z **[02_VISUAL_GUIDELINES.md](./02_VISUAL_GUIDELINES.md)**. Kolory i ikony to Twój główny język komunikacji, nie dodatek.

### Filar #3: Wizualizuj Kontekst, a Nie Implementację
*   **Zasada:** Diagramy nie są graficzną reprezentacją listy metod klasy. Ich celem jest wizualizacja **ukrytej złożoności**.
*   **W praktyce:** Skupiaj się na pokazywaniu **relacji między komponentami**, przepływów danych, maszyn stanów i interakcji z systemami zewnętrznymi.

### Filar #4: Projektuj jako Część Większej Całości
*   **Zasada:** Żaden diagram nie jest samotną wyspą. Każdy jest częścią większej, połączonej sieci wiedzy.
*   **W praktyce:** Aktywnie używaj interaktywności (`click`) i **Technik Kompozycji** (opisanych w głównym `README.md`), aby tworzyć połączone systemy wizualizacji.

### **Filar #5: Abstrakcja ponad Kompletność (Zasada "Zakaz Listowania")**

*   **Problem:** Najczęstszym błędem jest tworzenie diagramów, które próbują wylistować wszystkich członków dużej klasy, co kończy się bezużytecznym, uciętym wynikiem (`... X more`).
*   **Nadrzędna Zasada:** **ABSOLUTNIE ZABRONIONE jest tworzenie diagramów, których jedynym celem jest wylistowanie wszystkich atrybutów i metod klasy.** Taki diagram jest antywzorcem i będzie traktowany jako błąd.
*   **W praktyce:**
    *   **Zawsze wybieraj:** Zamiast pokazywać wszystko, wybierz **3-5 kluczowych metod i atrybutów**, które najlepiej opowiadają "historię" danej klasy.
    *   **"Czerwona Flaga":** Jeśli klasa ma więcej niż 10-15 członków, jest to **niepodważalny sygnał**, że prosty diagram-lista jest **złym narzędziem**. Zamiast niego, **musisz** zastosować jedną z zaawansowanych technik opisanych w Sekcji 3.

---

## 3. Zarządzanie Złożonością: Obowiązkowa Sztuka Dzielenia

**Złota Reguła:** Nigdy nie twórz "Boskiego Diagramu" (God Diagram), który próbuje pokazać wszystko. Złożoność jest wrogiem przejrzystości.

Jeśli klasa lub system jest zbyt złożony, aby zmieścić się w jednym, prostym diagramie (zgodnie z Filarem #5), **masz obowiązek zastosować strategię dzielenia na system połączonych wizualizacji "Overview + Details"**.

### 3.1. Kiedy Należy Podzielić Diagram?
*   Gdy klasa ma więcej niż 10-15 członków (Antywzorzec "Lista").
*   Gdy diagram miesza różne poziomy abstrakcji.
*   Gdy linie połączeń zaczynają przypominać "spaghetti".
*   Gdy opowiada więcej niż jedną historię.

### 3.2. Jak To Zrobić: Implementacja Systemu "Overview + Details"

Zamiast jednego pliku `.mmd`, tworzysz dedykowany **katalog**, w którym umieszczasz system połączonych diagramów. Ta technika jest szczegółowo opisana jako **[Złożony Wzorzec Wizualizacji](./03_DESIGN_PATTERNS/E_Advanced_Techniques.md)**.

#### **Ogólny Przykład Implementacji (dotyczy WSZYSTKICH złożonych klas)**

Jako **ogólny przykład**, rozważmy dowolną złożoną klasę, np. `Event`. Zamiast tworzyć jeden bezużyteczny diagram-listę, **tworzysz następującą strukturę katalogów i plików**:

```
/diagrams/
└── event/                <-- Nowy katalog dla systemu diagramów klasy 'Event'
    ├── overview.mmd      <-- Diagram przeglądowy, punkt wejściowy
    ├── lifecycle.mmd     <-- Diagram stanu
    └── interaction.mmd   <-- Diagram sekwencji
```

#### **Wymagania dla Plików w Systemie "Overview + Details"**

Poniższa tabela definiuje **minimalne wymagania** dla każdego pliku w tym systemie.

| Plik | Typ Diagramu | Cel | Kluczowe Wymagania |
| :--- | :--- | :--- | :--- |
| **`overview.mmd`** | `flowchart` | Działa jak interaktywna mapa. | - Musi być prosty i czytelny.<br/>- Musi używać pełnego systemu stylów (`classDef`).<br/>- **Musi zawierać linki `click` do wszystkich diagramów `details`**. |
| **`lifecycle.mmd`** | `stateDiagram-v2` | Pokazuje cykl życia i stany. | - Musi używać stylów warstw i modyfikatorów stanu (np. `classDef stateActive`).<br/>- Musi być w pełni ostylowany. |
| **`interaction.mmd`**| `sequenceDiagram` | Pokazuje interakcje w czasie. | - Musi używać standardowego motywu `sequenceDiagram` z bloku `init`.<br/>- Musi pokazywać kluczowe wywołania i odpowiedzi. |

---

**Ulepszone Przykłady Zawartości Plików:**

**1. `overview.mmd` (Flowchart - Obowiązkowy)**
*   **Cel:** Pokazuje ogólną koncepcję i działa jak interaktywna mapa do reszty diagramów.
*   **Przykład:**
    ```mermaid
    %%{init: {'theme': 'dark'}}%%
    graph TD
        %% Definicje stylów z 02_VISUAL_GUIDELINES.md
        classDef core fill:#3498db,stroke:#fff,color:#fff;
        classDef game fill:#e67e22,stroke:#fff,color:#fff;

        A["fa:fa-cogs EventDispatcher"]:::core;
        B["fa:fa-bolt Event"]:::game;
        C["fa:fa-code Callback Function"]:::game;
        
        A -- "triggers" --> B;
        B -- "executes" --> C;
        
        click B "./lifecycle.mmd" "Zobacz cykl życia Eventu"
        click A "./interaction.mmd" "Zobacz interakcję z Dispatcherem"
    ```

**2. `lifecycle.mmd` (StateDiagram - Rekomendowany dla klas ze stanami)**
*   **Cel:** Pokazuje cykl życia obiektu i jego możliwe stany, z pełnym wykorzystaniem "bajerów".
*   **Przykład:**
    ```mermaid
    %%{init: {'theme': 'dark'}}%%
    stateDiagram-v2
        %% Style pochodzą z 02_VISUAL_GUIDELINES.md
        classDef game fill:#e67e22,stroke:#fff,color:#fff;
        classDef stateInactive stroke-dasharray:5 5,stroke-width:2px,stroke:#ef4444;
        classDef stateActive stroke-width:3px,stroke:#2ecc71;
        
        [*] --> Created
        Created: Awaiting execution
        
        Created --> Executed : execute()
        Created --> Canceled : cancel()
        
        Executed --> [*]
        Canceled --> [*]

        note right of Created
          Nowy Event jest w stanie
          oczekiwania na wywołanie.
        end note

        %% Zastosowanie stylów warstw i stanów
        class Created,Executed,Canceled game
        class Executed stateActive
        class Canceled stateInactive
    ```

**3. `interaction.mmd` (SequenceDiagram - Rekomendowany dla klas z interakcjami)**
*   **Cel:** Pokazuje, jak inne komponenty wchodzą w interakcję z tą klasą w czasie, z pełną stylizacją.
*   **Przykład:**
    ```mermaid
    %%{init: {
      'theme': 'dark', 
      'themeVariables': { 'actorBorder': '#9b59b6', 'signalColor': '#2ecc71', 'activationBackgroundColor': '#1f2933' }
    }}%%
    sequenceDiagram
        participant D as fa:fa-cogs Dispatcher
        participant E as fa:fa-bolt Event

        D->>+E: execute()
        note over E: Event logic runs...
        E-->>-D: return
    ```

---

### 3.3. Finalna Weryfikacja Systemu Diagramów (Mini-Checklista)

Przed zatwierdzeniem nowego systemu diagramów dla złożonego komponentu, zadaj te trzy pytania:

1.  [ ] **Czy `overview.mmd` jest prosty i działa jak interaktywna "mapa drogowa"** do reszty diagramów?
2.  [ ] **Czy wszystkie diagramy `details` (`lifecycle`, `interaction` itp.) są w pełni ostylowane** zgodnie z `02_VISUAL_GUIDELINES.md` i pokazują zaawansowane funkcje?
3.  [ ] **Czy linki `click` w `overview.mmd` działają** i poprawnie prowadzą do odpowiednich, szczegółowych diagramów?

Pozytywna odpowiedź na wszystkie trzy pytania oznacza, że system jest gotowy.
