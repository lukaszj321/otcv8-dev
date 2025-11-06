# Wzorce Projektowe Diagramów

## 1. Cel Dokumentu

Ten dokument to zbiór gotowych do użycia **wzorców projektowych ("przepisów")** dla najczęstszych typów komponentów w naszym systemie. Działa jak "książka kucharska" dla twórców diagramów. Celem tych wzorców jest zapewnienie spójności strukturalnej i przyspieszenie procesu tworzenia, jednocześnie pozostawiając pole na dostosowanie do konkretnego przypadku.

## 2. Indeks Wzorców
1.  [Wzorzec Przepływu Danych (Potok)](#wzorzec-przeplywu-danych-potok)
2.  [Wzorzec Menedżera Cyklem Życia](#wzorzec-menedzera-cyklem-zycia)
3.  [Wzorzec Komponentu UI](#wzorzec-komponentu-ui)
4.  [Wzorzec Maszyny Stanów](#wzorzec-maszyny-stanow)
5.  [Wzorzec Mostu Systemowego](#wzorzec-mostu-systemowego)

---

### Wzorzec Przepływu Danych (Potok)
*   **Kiedy stosować:** Dla klas, których główną rolą jest transformacja danych (np. szyfrowanie, parsowanie, serializacja).
*   **Kluczowe Elementy:** Wejście, Seria Kroków Przetwarzania, Wyjście, Obsługa Błędów.
*   **Rekomendowana Orientacja:** `graph LR` (Left-to-Right).
*   **Przykładowy Kod:**
    ```mermaid
    graph LR
        classDef data fill:#27ae60
        classDef process fill:#3498db
        classDef error fill:#c0392b

        subgraph "Input"
            InputData["fa:fa-file-alt Raw Data"]:::data
        end
        subgraph "Processing Pipeline"
            Step1["fa:fa-plug Step 1: Validate"]:::process
            Step2["fa:fa-cogs Step 2: Transform"]:::process
            Step3["fa:fa-database Step 3: Store"]:::process
        end
        subgraph "Output"
            OutputData["fa:fa-check-circle Processed Data"]:::data
            ErrorData["fa:fa-exclamation-triangle Error"]:::error
        end
        
        InputData ==> Step1 --> Step2 --> Step3 ==> OutputData
        Step1 -- "Invalid data" --> ErrorData
    ```

### Wzorzec Menedżera Cyklem Życia
*   **Kiedy stosować:** Dla klas, które zarządzają tworzeniem, stanem i niszczeniem innych obiektów (np. `Application`, `WindowManager`, `ModuleManager`).
*   **Kluczowe Elementy:** Inicjator, Menedżer, Zarządzane Obiekty, Kluczowe stany/fazy.
*   **Rekomendowana Orientacja:** `graph TD` (Top-Down).
*   **Przykładowy Kod:**
    ```mermaid
    graph TD
        classDef manager fill:#3498db
        classDef managed fill:#9b59b6
        classDef initiator fill:#e67e22

        Initiator["fa:fa-play-circle Initiator (e.g., App Start)"]:::initiator

        subgraph "Manager"
            Manager["fa:fa-cogs The Manager"]:::manager
        end

        subgraph "Managed Objects & States"
            Phase1["Phase 1: Initialization"]
            Phase2["Phase 2: Active Loop"]
            Phase3["Phase 3: Shutdown"]
            
            ObjA["fa:fa-box Managed Object A"]:::managed
            ObjB["fa:fa-box Managed Object B"]:::managed
        end

        Initiator --> Manager
        Manager -- "controls" --> Phase1 --> Phase2 --> Phase3
        Manager -- "creates/destroys" --> ObjA
        Manager -- "creates/destroys" --> ObjB
    ```

### Wzorzec Komponentu UI
*   **Kiedy stosować:** Dla wszystkich widgetów i okien interfejsu użytkownika.
*   **Kluczowe Elementy:** Źródło Danych, Struktura (kluczowe sub-komponenty), Interakcje Użytkownika, Zdarzenia Aplikacji.
*   **Rekomendowana Orientacja:** `graph TD`.
*   **Przykładowy Kod:**
    ```mermaid
    graph TD
        classDef ui fill:#9b59b6
        classDef data fill:#27ae60
        classDef event fill:#e67e22

        DataSource["fa:fa-database Data Source (e.g., Game State)"]:::data
        AppEvent["fa:fa-bolt Application Event"]:::event

        subgraph "UI Widget"
            direction LR
            MainWidget["fa:fa-desktop Main Widget"]:::ui
            subgraph "Key Sub-Components"
                Button["fa:fa-mouse-pointer Button"]:::ui
                Label["fa:fa-tag Label"]:::ui
                List["fa:fa-list List"]:::ui
            end
            MainWidget --> Button & Label & List
        end
        
        subgraph "Interactions & Data Flow"
            UserAction["fa:fa-hand-pointer User Click"]
            UserAction -.-> Button
            Button -.-> AppEvent
            DataSource ==> Label
            DataSource ==> List
        end
        
        DataSource -- "updates" --> MainWidget
    ```

### Wzorzec Maszyny Stanów
*   **Kiedy stosować:** Dla klas, które mają wyraźnie zdefiniowane i ograniczone stany (np. połączenie sieciowe, stan postaci w grze).
*   **Kluczowe Elementy:** Stany, Przejścia (wyzwalane przez zdarzenia/akcje).
*   **Rekomendowana Orientacja:** `graph TD` lub `LR` (zależnie od logiki).
*   **Przykładowy Kod:**
    ```mermaid
    graph TD
        classDef state fill:#2ecc71
        
        [*] --> State1
        
        State1["fa:fa-circle State A"]:::state
        State2["fa:fa-circle State B"]:::state
        State3["fa:fa-circle State C"]:::state

        State1 -->|Event X| State2
        State2 -->|Event Y| State3
        State3 -->|Event Z| State1
        State2 -->|Error Event| [*]
    ```

### Wzorzec Mostu Systemowego
*   **Kiedy stosować:** Dla klas, które działają jako pośrednik lub "tłumacz" między dwoma różnymi systemami (np. naszą aplikacją a API systemu operacyjnego).
*   **Kluczowe Elementy:** System Zewnętrzny, Most (nasza klasa), System Wewnętrzny.
*   **Rekomendowana Orientacja:** `graph LR`.
*   **Przykładowy Kod:**
    ```mermaid
    graph LR
        classDef external fill:#7f8c8d
        classDef bridge fill:#3498db
        classDef internal fill:#2ecc71

        subgraph "External System (e.g., OS)"
            ExternalAPI["fa:fa-windows External API / Events"]:::external
        end

        subgraph "The Bridge"
            Bridge["fa:fa-plug Our Bridge Class"]:::bridge
        end

        subgraph "Internal System"
            InternalAPI["fa:fa-bolt Internal Events / API"]:::internal
        end

        ExternalAPI -- "Raw events" --> Bridge
        Bridge -- "Translates to" --> InternalAPI
        InternalAPI -- "Commands" --> Bridge
        Bridge -- "Translates to" --> ExternalAPI
    ```
