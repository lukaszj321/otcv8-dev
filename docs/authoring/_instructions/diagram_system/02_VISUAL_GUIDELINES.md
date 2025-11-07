# Specyfikacja Wizualna Diagramów

## 1. Wprowadzenie i Zasady Nadrzędne

### 1.1. Cel Dokumentu
Ten dokument jest **ścisłą specyfikacją techniczną** i jedynym źródłem prawdy dla wszystkich elementów wizualnych w diagramach Mermaid. Każdy element ma przypisane znaczenie semantyczne, a celem jest zapewnienie, aby wszystkie diagramy w projekcie "mówiły tym samym językiem wizualnym".

### 1.2. Zasady Nadrzędne
*   **Zakaz Tworzenia Własnych Styli:** Nie definiujemy własnych kolorów i klas poza tym, co jest opisane w tym dokumencie. Jeśli potrzebujesz nowego znaczenia wizualnego, najpierw zaktualizuj ten dokument.
*   **Obowiązek Stosowania Systemu:** Diagramy w repozytorium **muszą** używać zdefiniowanych `classDef` (dla `graph`) lub motywów z Sekcji 3 (dla typów bez `classDef`).
*   **Hierarchia Dokumentów:** Ten dokument definiuje "Jak ma wyglądać?". Filozofię "Dlaczego?" opisuje **[01_DESIGN_PHILOSOPHY.md](./01_DESIGN_PHILOSOPHY.md)**, a praktyczne przykłady "Jak to zrobić?" znajdują się w **[Bibliotece Wzorców](./03_DESIGN_PATTERNS/)**.
*   **Diagram niezgodny ze specyfikacją jest traktowany jak błąd w dokumentacji.**

### 1.3. Globalny Blok Inicjalizujący
Każdy diagram Mermaid w projekcie powinien zaczynać się od standardowego bloku inicjalizującego. Zapewnia to spójność motywu, tekstu i czcionek.
```plaintext
%%{init: {
  "theme": "dark",
  "themeVariables": {
    "primaryTextColor": "#e5e7eb",
    "lineColor": "#4b5563",
    "fontFamily": "Inter, system-ui, sans-serif"
  }
}}%%
```
Odstępstwa są dozwolone tylko dla typów diagramów, które wymagają specyficznych `themeVariables`, co jest opisane w Sekcji 3 tego dokumentu.

---

## 2. Podstawowy System Stylizacji (`graph` / `flowchart`)

Poniższe wytyczne dotyczą głównie diagramów typu `graph`, które są naszym podstawowym i najbardziej elastycznym narzędziem do wizualizacji.

### 2.1. Wymiar 1: Warstwy Architektoniczne (Kolor Tła)
Kolor tła węzła (`fill`) reprezentuje jego przynależność do jednej z predefiniowanych warstw architektonicznych.

#### Warstwy Architektoniczne (Kolor)

| Kolor | Warstwa | Opis i Katalogi |
| :--- | :--- | :--- |
| 🟦 | **Core Engine** | Niskopoziomowy silnik, framework i podstawowe API.<br/>*Katalogi: [`01_core`](./01_core/), [`01_runtime`](./01_runtime/), [`15_vc16`](./15_vc16/)* |
| 🟩 | **Subsystemy** | Wyspecjalizowane, niezależne podsystemy.<br/>*Katalogi: [`06_assets`](./06_assets/), [`08_audio`](./08_audio/), [`09_logging`](./09_logging/), [`11_data`](./11_data/)* |
| 🟧 | **Logika Gry & Moduły** | Logika specyficzna dla gry, system modułów i zdarzeń.<br/>*Katalogi: [`02_events`](./02_events/), [`03_modules`](./03_modules/), [`05_events`](./05_events/), [`10_game_runtime`](./10_game_runtime/), [`12_otmod`](./12_otmod/)* |
| 🟪 | **User Interface (UI)** | Komponenty interfejsu użytkownika, layouty i OTUI.<br/>*Katalogi: [`04_ui`](./04_ui/), [`13_layouts`](./13_layouts/)* |
| 🟥 | **Networking & Security** | Komunikacja sieciowa, protokoły i szyfrowanie.<br/>*Katalogi: [`05_network`](./05_network/), [`07_settings_crypto`](./07_settings_crypto/)* |
| 🔳 | **Platforma** | Kod specyficzny dla danej platformy.<br/>*Katalogi: [`14_android`](./14_android/)* |

**Oficjalne definicje `classDef` do skopiowania:**
```plaintext
classDef core fill:#3498db,stroke:#fff,color:#fff
classDef subsystem fill:#2ecc71,stroke:#111827,color:#111827
classDef game fill:#e67e22,stroke:#fff,color:#fff
classDef ui fill:#9b59b6,stroke:#fff,color:#fff
classDef netsec fill:#c0392b,stroke:#fff,color:#fff
classDef platform fill:#7f8c8d,stroke:#fff,color:#fff
classDef critical fill:#e74c3c,stroke:#fff,color:#fff
classDef note fill:#4b5563,color:#e5e7eb,stroke:#9ca3af,stroke-dasharray:3 3
```
> **Uwaga:** Dla `subsystem` (zielony) używamy ciemnego tekstu (`#111827`) dla lepszego kontrastu.

### 2.2. Wymiar 2: Typy Komponentów (Ikona)
Ikona wewnątrz węzła reprezentuje jego techniczną rolę. Używamy ikon z [Font Awesome 4.7](https://fontawesome.com/v4.7.0/icons/).

#### Typy Komponentów (Ikona)

| Ikona | Typ Komponentu | Opis |
| :--- | :--- | :--- |
| ⚙️ `fa-cogs` | **Menedżer** | Klasy zarządzające cyklem życia innych obiektów. |
| 🗃️ `fa-database` | **Dane/Struktura** | Klasy przechowujące i udostępniające dane. |
| ⚡ `fa-bolt` | **Zdarzenie/Sygnał** | Zdarzenia, sygnały, callbacki. |
| 🔌 `fa-plug` | **Interfejs/API** | Punkty styku między systemami, fasady. |
| 📄 `fa-file-alt` | **Plik/Zasób** | Reprezentacja plików lub zasobów z dysku. |
| ⚠️ `fa-exclamation-triangle` | **Błąd/Krytyczny** | Wyjątki, obsługa błędów, operacje krytyczne. |

### 2.3. Wymiar 3: Kształt Węzła
Kształt węzła dodaje kolejną warstwę informacji o jego naturze.

| Kształt         | Składnia     | Znaczenie Semantyczne                                                         |
| :-------------- | :----------- | :---------------------------------------------------------------------------- |
| **Prostokąt**   | `A["Tekst"]` | **Domyślny kształt.** Używany dla większości komponentów, klas i aktorów.     |
| **Zaokrąglony** | `B("Tekst")` | **Proces / Akcja.** Używany do oznaczania kroków w procesie lub funkcji.      |
| **Romb**        | `C{"Tekst"}` | **Decyzja / Warunek.** Używany do pokazywania rozgałęzień logiki (`if/else`). |

### 2.4. Modyfikatory Stanu (`stateDiagram-v2`)
W diagramach stanów, **kolor tła** nadal reprezentuje warstwę. **Stan** jest komunikowany przez **styl obramowania**.

**Oficjalne modyfikatory `classDef` dla stanów:**
```plaintext
classDef stateActive stroke-width:3px,stroke:#2ecc71
classDef stateInactive stroke-dasharray:5 5,stroke-width:2px,stroke:#ef4444
classDef stateTransition stroke-width:2px,stroke:#3b82f6
```

### 2.5. Style Linii i Połączeń (`graph`)
| Typ                             | Składnia | Znaczenie Semantyczne                                                   |
| :------------------------------ | :------- | :---------------------------------------------------------------------- |
| **Wywołanie synchroniczne**     | `-->`    | Przepływ blokujący lub twarda zależność.                                |
| **Wywołanie asynchroniczne**    | `-.->`   | Zdarzenie, callback, przepływ nieblokujący.                             |
| **Kluczowy przepływ danych**    | `==>`    | Główna ścieżka danych w diagramie.                                      |
| **Niewidzialny link sterujący** | `~~~`    | Używany do **manualnego kontrolowania układu** i pozycjonowania węzłów. |

Do kolorowania linii należy używać `linkStyle`, zgodnie z przykładami w **[Bibliotece Wzorców](./03_DESIGN_PATTERNS/)**.

---

## 3. Stylizacja Innych Typów Diagramów (Obejścia Ograniczeń)

Wiele typów diagramów **nie wspiera** `classDef` w rendererze GitHuba. W takich przypadkach należy używać ustandaryzowanych motywów w bloku `init` lub stylizacji wbudowanej.

### 3.1. `sequenceDiagram`
*   **Problem:** Nie wspiera `classDef`.
*   **Rozwiązanie:** Użyj globalnych `themeVariables` w bloku `init`.
*   **Standardowy Motyw:**
    ```plaintext
    %%{init: {
      'theme': 'dark', 'themeVariables': { 'actorBorder': '#9b59b6', 'signalColor': '#2ecc71' }
    }}%%
    ```

### 3.2. `erDiagram`
*   **Problem:** Nie wspiera `classDef`.
*   **Rozwiązanie:** Użyj globalnych `themeVariables` do stylizacji encji.
*   **Standardowy Motyw:**
    ```plaintext
    %%{init: {
      'theme':'dark', 'themeVariables':{ 'primaryTextColor':'#e5e7eb',
        'erEntityFill':'#111827', 'erEntityStroke':'#9ca3af', 'erEntityTextColor':'#e5e7eb' }
    }}%%
    ```

### 3.3. `mindmap`
*   **Problem:** Nie wspiera stylizacji w rendererze GitHuba.
*   **Rozwiązanie:** Użyj prostego HTML (`<font color='white'>`) jako **obejścia (hacka)**, aby zapewnić czytelność tekstu. Ten hack służy **tylko do czytelności** i nie wprowadza nowych znaczeń semantycznych.

### 3.4. `timeline`, `gantt`, `pie`, `quadrantChart`
*   **Problem:** Minimalne lub żadne wsparcie dla zaawansowanej stylizacji.
*   **Rozwiązanie:** Polegaj na domyślnym motywie `dark` z globalnego bloku `init` i skup się na klarowności danych.

---

## 4. Linki, Kompozycja i "Pułapki" Składni

### 4.1. Linki i Interaktywność (`click` i `link`)
*   `click` jest **dozwolony i rekomendowany** tylko w diagramach `graph` / `flowchart` i `mindmap`.
*   Linki powinny prowadzić do plików `.md` w repozytorium lub do konkretnych nagłówków (anchorów).
*   **Jeśli `click` lub `link` psuje renderowanie, priorytetem jest poprawny diagram, nie klikalność.**

### 4.2. Kompozycja i Dzielenie Diagramów
*   Zamiast jednego, przeładowanego diagramu, **zawsze preferuj system połączonych wizualizacji**: jeden diagram `overview` + kilka diagramów szczegółowych.
*   Ta technika jest szczegółowo opisana jako **[Złożony Wzorzec Wizualizacji](./03_DESIGN_PATTERNS/E_Advanced_Techniques.md)** i jest fundamentem naszego podejścia.

### 4.3. Antywzorce i "Pułapki" Składni (Czego Unikamy)
*   **Nie używamy `classDef`** w typach, które go nie wspierają stabilnie (`sequenceDiagram`, `mindmap`, `erDiagram` itp.).
*   **Nie używamy cudzysłowów (`"`)** wewnątrz etykiet na liniach połączeń (np. `|log("message")|`). Używaj bezpiecznej alternatywy (np. `|log: message|`).
*   **Nie używamy niestandardowych grotów strzałek** w diagramach `graph` (np. `--|>`). Używaj standardowych strzałek (`-->`, `-.->`) z etykietą tekstową.
*   **Nie rysujemy:**
    *   Historii Git jako `flowchart`, jeśli można użyć `gitGraph`.
    *   Proporcji bez liczb (diagram `sankey-beta` bez jednostki jest błędem).
