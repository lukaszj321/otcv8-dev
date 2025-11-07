## Część B: Struktura i Relacje

### Wzorzec Struktury Klas (`classDiagram`)

**Kiedy:** API, dziedziczenie, interfejsy, kontrakty.

> Uwaga: `click` w `classDiagram` nie jest gwarantowany w każdym rendererze.

### Wzorzec Struktury Klas (symulowany za pomocą `flowchart`)
*   **Kiedy stosować:** Do pokazywania relacji między klasami,  API, dziedziczenie, interfejsy, kontrakty. **Ten wzorzec zastępuje `classDiagram`, aby zapewnić pełne wsparcie dla naszego systemu stylów na GitHubie.**
*   **Kluczowe Elementy:** Węzły reprezentujące klasy (ze stylami warstw), listy członków (metody/atrybuty) wewnątrz węzłów, strzałki reprezentujące relacje (dziedziczenie, kompozycja).
*   **Przykłady Kod:**

### **Wariant 1** Wzorzec Pełnej Struktury Klas
```mermaid
%%{init: {'theme': 'dark'}}%%
graph LR
    %% --- Definicja palety kolorów i stylów ---
    classDef core fill:#3498db,stroke:#fff,color:#fff;
    classDef game fill:#e67e22,stroke:#fff,color:#fff;
    classDef subsystem fill:#2ecc71,stroke:#333,color:#000;
    classDef note fill:#4b5563,color:#e5e7eb,stroke:#9ca3af,stroke-dasharray:3 3;

    %% --- Definicja Węzłów-Klas ---
    subgraph "Warstwa Core"
        IClickable["
            <div style='text-align:left; padding:5px;'>
                <div style='font-size:16px; font-weight:bold;'>fa:fa-plug IClickable</div><hr/>
                <i>&lt;&lt;interface&gt;&gt;</i><br/>
                + onClick(event)
            </div>
        "]:::core;
        
        GameObject["
            <div style='text-align:left; padding:5px;'>
                <div style='font-size:16px; font-weight:bold;'>fa:fa-cube GameObject</div><hr/>
                <i>&lt;&lt;abstract&gt;&gt;</i><br/>
                # position<br/>
                + name<br/>
                + update()*
            </div>
        "]:::core;
    end;

    subgraph "Warstwa Gry"
        Character["
            <div style='text-align:left; padding:5px;'>
                <div style='font-size:16px; font-weight:bold;'>fa:fa-user-ninja Character</div><hr/>
                - health<br/>
                # mana<br/>
                + attack(target)
            </div>
        "]:::game;

        Player["
            <div style='text-align:left; padding:5px;'>
                <div style='font-size:16px; font-weight:bold;'>fa:fa-user-astronaut Player</div><hr/>
                - inventory<br/>
                + useItem(itemId)<br/>
                + onClick(event)
            </div>
        "]:::game;

        Skill["
            <div style='text-align:left; padding:5px;'>
                <div style='font-size:16px; font-weight:bold;'>fa:fa-star Skill</div><hr/>
                + name<br/>
                + execute()
            </div>
        "]:::game;
    end;
    
    subgraph "Podsystemy"
        Inventory["
            <div style='text-align:left; padding:5px;'>
                <div style='font-size:16px; font-weight:bold;'>fa:fa-box Inventory</div><hr/>
                - items<br/>
                + addItem(item)
            </div>
        "]:::subsystem;
    end;
    
    subgraph "Notatki"
        PlayerNote["
            <div style='text-align:left; padding:5px;'>
                <i><b>Notatka:</b> Player jest klikalny,<br/>
                np. w celu wyświetlenia<br/>
                menu kontekstowego.</i>
            </div>"
        ]:::note;
    end;

    %% --- Widoczne Relacje ---
    GameObject -- "extends" --> Character;
    Character -- "extends" --> Player;
    IClickable -.->|"implements"| Player;
    Player -- "uses" --> Skill;
    Player -- "contains" --> Inventory;
    Player -.-> PlayerNote;

    %% --- Niewidzialne Linki Sterujące Układem ---
    %% Te linki tworzą "rusztowanie", które wymusza poprawny układ.
    GameObject ~~~ Inventory;
    Skill ~~~ PlayerNote;

    %% --- Zaawansowana stylizacja linii ---
    linkStyle 0,1 stroke:#2ecc71,stroke-width:2px;
    %% extends
    linkStyle 2 stroke:#3498db,stroke-width:2px;
    %%implements
    linkStyle 4 stroke:#9b59b6,stroke-width:4px;
    %%contains
    linkStyle 5 stroke:#9ca3af,stroke-dasharray:3 3;
    %% link do notatki
    linkStyle 6,7 stroke-width:0px;
    %% Ukrycie linków sterujących

    %% --- Interaktywność ---
    click Inventory "#" "Kliknij, aby zobaczyć szczegółowy diagram ekwipunku";
```

---

### **Wariant 2: Wzorzec Prostej Klasy (Minimalistyczny)**

*   **Kiedy stosować:** Dla prostych klas narzędziowych lub struktur danych, które mają niewiele lub żadnych złożonych zależności.
*   **Czego uczy:** Jak tworzyć czyste, minimalistyczne diagramy, które nie są przeładowane informacjami. Pokazuje, że nie zawsze trzeba używać `subgraph` i wielu warstw.
*   **Przykładowy Kod:**
```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    %% Pełna definicja stylów, aby pokazać interakcję między warstwami
    classDef subsystem fill:#2ecc71,stroke:#333,color:#000;
    classDef game fill:#e67e22,stroke:#fff,color:#fff;
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;

    %% Źródła logów z różnych warstw architektonicznych
    subgraph "Źródła Logów (Przykłady)"
        direction LR
        A["fa:fa-user-astronaut Player"]:::game;
        B["fa:fa-network-wired Connection"]:::netsec;
        C["fa:fa-archive AssetManager"]:::subsystem;
    end

    %% Centralny serwis
    Logger["
        <div style='text-align:left; padding:5px;'>
            <div style='font-size:16px; font-weight:bold;'>fa:fa-file-alt Logger</div><hr/>
            <i>&lt;&lt;singleton&gt;&gt;</i><br/>
            - filePath: string<br/>
            + log(message: string)<br/>
            + setFile(path: string)
        </div>
    "]:::subsystem;

    %% Cel (miejsce docelowe logów)
    subgraph "Cel (Destination)"
        LogFile["fa:fa-file-text log_file.txt"]:::subsystem;
    end

    %% --- Definicje Relacji (z bezpiecznymi etykietami) ---
    A -.->|log: Player jumped| Logger;
    B -.->|log: Connection lost| Logger;
    C -.->|log: Asset loaded| Logger;
    Logger -- "writes to" --> LogFile;
    
    %% --- Interaktywność ---
    click Logger "#" "Go to Logger API";
```

---

### **Wariant 3: Wzorzec Kolaboracji (Skupiony na Zależnościach)**

*   **Kiedy stosować:** Gdy chcemy pokazać, jak jedna klasa **współpracuje** z wieloma innymi, aby wykonać zadanie (np. wzorzec Fabryki, Budowniczego). Tutaj relacje są ważniejsze niż wewnętrzna struktura klas.
*   **Czego uczy:** Jak używać prostszych węzłów (nawet bez listy metod) i skupić się na **liniach połączeń**, aby opowiedzieć historię o współpracy.
*   **Przykładowy Kod:**
```mermaid
%%{init: {'theme': 'dark'}}%%
graph LR
    %% Pełna definicja stylów, w tym brakujący netsec
    classDef game fill:#e67e22,stroke:#fff,color:#fff;
    classDef core fill:#3498db,stroke:#fff,color:#fff;
    classDef subsystem fill:#2ecc71,stroke:#333,color:#000;
    classDef netsec fill:#c0392b,stroke:#fff,color:#fff;

    %% Zależności po lewej stronie
    subgraph "Zależności (Inputs)"
        Config["fa:fa-file-alt ConfigManager"]:::core;
        Assets["fa:fa-archive AssetManager"]:::subsystem;
        Network["fa:fa-network-wired NetworkClient"]:::netsec;
    end

    %% Proces w środku
    subgraph "Proces (Factory)"
        Factory["fa:fa-industry PlayerFactory"]:::core;
    end

    %% Wynik po prawej stronie
    subgraph "Wynik (Output)"
        Player["fa:fa-user-astronaut Player"]:::game;
    end

    %% --- Definicje Relacji ---
    %% Zależności "wpływają" do fabryki
    Config -- "config data" --> Factory;
    Assets -- "asset data" --> Factory;
    Network -- "connection" --> Factory;
    
    %% Fabryka "tworzy" produkt
    Factory -- "<strong>creates</strong>" --> Player;

    %% --- Stylizacja Linii ---
    %% Podkreślenie kluczowej relacji "creates"
    linkStyle 3 stroke:#2ecc71,stroke-width:4px;
```

---

### **Wariant 4: Wzorzec Kompaktowy (Wysoka Gęstość)**

*   **Kiedy stosować:** Gdy musimy pokazać grupę wielu małych, silnie powiązanych ze sobą klas (np. zestaw wyjątków, niestandardowe kontrolki UI). Użycie pełnych, dużych węzłów byłoby nieczytelne.
*   **Czego uczy:** Jak używać mniejszych węzłów (tylko nazwa i stereotyp) i orientacji `LR`, aby stworzyć zwarty, gęsty, ale wciąż czytelny diagram.
*   **Przykładowy Kod:**
```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    %% Definicja stylu dla warstwy UI
    classDef ui fill:#9b59b6,stroke:#fff,color:#fff;

    subgraph "Rodzina Widgetów UI"
        %% Klasa bazowa na górze
        Widget["fa:fa-puzzle-piece UIWidget"]:::ui;

        %% Klasy pochodne poniżej
        Button["StyledButton<br/><i>&lt;&lt;widget&gt;&gt;</i>"]:::ui;
        Panel["DraggablePanel<br/><i>&lt;&lt;widget&gt;&gt;</i>"]:::ui;
        
        %% Komponent zagnieżdżony jeszcze niżej
        Slider["ColorSlider<br/><i>&lt;&lt;widget&gt;&gt;</i>"]:::ui;
    end

    %% --- Definicje Relacji ---
    %% Strzałki idą OD klasy pochodnej DO klasy bazowej
    Button -- "[extends]" --> Widget;
    Panel -- "[extends]" --> Widget;
    Panel -- "[contains]" --> Slider;

    %% --- Stylizacja Linii ---
    linkStyle 0,1 stroke:#2ecc71,stroke-width:2px;
    %% Dziedziczenie = zielony
    linkStyle 2 stroke:#9b59b6,stroke-width:3px;
    %% Kompozycja = fioletowy
```

---


### Wzorzec Modelu Danych

Do wizualizacji modeli danych i schematów baz danych oferujemy dwa warianty, każdy dostosowany do innych potrzeb.

---

#### **Wariant 1: Szybki Szkic (`erDiagram`)**
*   **Kiedy stosować:** Do **szybkich, prostych szkiców**, gdzie liczy się tylko pokazanie encji i ich podstawowych relacji, a precyzyjny układ i stylizacja nie mają krytycznego znaczenia.
*   **Zalety:** Bardzo prosta i zwięzła składnia.
*   **Wady:** Brak kontroli nad układem, bardzo ograniczone możliwości stylizacji (nie wspiera naszego systemu `classDef`), co może prowadzić do nieczytelnego rozciągnięcia diagramu.
*   **Przykładowy Kod:**
    ```mermaid
    %%{init: {
      "theme": "dark",
      "themeVariables": {
        "primaryTextColor": "#e5e7eb", "secondaryColor": "#1f2937",
        "erEntityColor": "#0f172a", "erEntityTitleColor": "#9ca3af"
      }
    }}%%
    erDiagram
        CUSTOMER ||--|{ ORDER : places
        PRODUCT }|..|| LINE_ITEM : "is item for"
        ORDER ||--|{ LINE_ITEM : contains

        CUSTOMER {
            int id PK
            string name
            string email "unique"
        }
        ORDER {
            int id PK
            int customer_id FK
            datetime created_at
        }
        PRODUCT {
            int id PK
            string name
            decimal price "cannot be negative"
        }
        LINE_ITEM {
            int order_id FK
            int product_id FK
            int quantity
            decimal unit_price
        }
    ```

---

#### **Wariant 2: Zaawansowany Model (`graph` - Rekomendowany)**
*   **Kiedy stosować:** Zawsze, gdy **jakość wizualna, czytelność i precyzyjny układ mają znaczenie**. To jest nasz **oficjalny, rekomendowany wzorzec** dla finalnej, publicznej dokumentacji.
*   **Zalety:**
    *   **Pełna, manualna kontrola nad układem** za pomocą niewidzialnych linków.
    *   **Pełna integracja z naszym systemem `classDef`**, co pozwala na spójną stylizację.
    *   Możliwość użycia zaawansowanych funkcji, takich jak `linkStyle` i `click`.
*   **Wady:** Znacznie bardziej złożony i "gadatliwy" kod (użycie tabel HTML).
*   **Przykładowy Kod:**
    ```mermaid
    %%{init: {'theme': 'dark'}}%%
    graph TD
        %% Definicja stylu dla encji, spójna z estetyką erDiagram
        classDef entity fill:#0f172a,stroke:#9ca3af,color:#e5e7eb;

        %% --- Definicja Węzłów-Encji ---
        subgraph "Dane Klienta"
            CUSTOMER["
                <div style='padding:5px;'>
                    <div style='font-weight:bold; border-bottom:1px solid #9ca3af; margin-bottom:5px; text-align:center;'>CUSTOMER</div>
                    <table style='width:100%; text-align:left; font-size:14px;'>
                        <tr><td style='padding-right:10px;'><b>int id</b></td><td><i>PK</i></td></tr>
                        <tr><td>string name</td><td></td></tr>
                        <tr><td>string email</td><td><i>unique</i></td></tr>
                    </table>
                </div>
            "]:::entity;
        end;

        subgraph "Dane Produktu"
            PRODUCT["
                <div style='padding:5px;'>
                    <div style='font-weight:bold; border-bottom:1px solid #9ca3af; margin-bottom:5px; text-align:center;'>PRODUCT</div>
                    <table style='width:100%; text-align:left; font-size:14px;'>
                        <tr><td><b>int id</b></td><td><i>PK</i></td></tr>
                        <tr><td>string name</td><td></td></tr>
                        <tr><td>decimal price</td><td></td></tr>
                    </table>
                </div>
            "]:::entity;
        end;

        subgraph "Dane Zamówienia"
            ORDER["
                <div style='padding:5px;'>
                    <div style='font-weight:bold; border-bottom:1px solid #9ca3af; margin-bottom:5px; text-align:center;'>ORDER</div>
                    <table style='width:100%; text-align:left; font-size:14px;'>
                        <tr><td><b>int id</b></td><td><i>PK</i></td></tr>
                        <tr><td>int customer_id</td><td><i>FK</i></td></tr>
                        <tr><td>datetime created_at</td><td></td></tr>
                    </table>
                </div>
            "]:::entity;

            LINE_ITEM["
                <div style='padding:5px;'>
                    <div style='font-weight:bold; border-bottom:1px solid #9ca3af; margin-bottom:5px; text-align:center;'>LINE_ITEM</div>
                    <table style='width:100%; text-align:left; font-size:14px;'>
                        <tr><td>int order_id</td><td><i>FK</i></td></tr>
                        <tr><td>int product_id</td><td><i>FK</i></td></tr>
                        <tr><td>int quantity</td><td></td></tr>
                    </table>
                </div>
            "]:::entity;
        end;

        %% --- Niewidzialne Linki Sterujące Układem ---
        %% Tworzą "rusztowanie", które wymusza pozycje bloków obok siebie.
        CUSTOMER ~~~ PRODUCT;

        %% --- Widoczne Relacje ---
        CUSTOMER -- "places" --> ORDER;
        ORDER -- "contains" --> LINE_ITEM;
        PRODUCT -.->|"is item for"| LINE_ITEM;

        %% --- Interaktywność ---
        click CUSTOMER "#" "Przejdź do dokumentacji API Klienta";
    ```

---

### Wzorzec Mapy Myśli (`mindmap`)

**Kiedy:** Spis treści dokumentacji, moduły, funkcjonalności.

```mermaid
%%{init: {'theme': 'dark'}}%%
mindmap
  root((<font color="white">Documentation Structure</font>))
    %% --- Core ---
    "01 Core"("<font color='white'>fa:fa-cogs 01 Core</font>")
      ("<font color='white'>API</font>")
      ("<font color='white'>Runtime</font>")
    %% --- Game & Modules ---
    "02 Events"("<font color='white'>fa:fa-bolt 02 Events</font>")
      ("<font color='white'>Dispatch</font>")
      ("<font color='white'>Handlers</font>")
    "03 Modules"("<font color='white'>fa:fa-puzzle-piece 03 Modules</font>")
      ("<font color='white'>Loading</font>")
      ("<font color='white'>Dependencies</font>")
    %% --- UI ---
    "04 UI"("<font color='white'>fa:fa-desktop 04 UI</font>")
      ("<font color='white'>Layouts</font>")
      ("<font color='white'>Themes</font>")
```
