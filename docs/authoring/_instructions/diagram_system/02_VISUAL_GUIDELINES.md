# Specyfikacja Wizualna Diagramów

## 1. Cel Dokumentu

Ten dokument jest **ścisłą specyfikacją techniczną** wszystkich dozwolonych elementów wizualnych w diagramach Mermaid. Działa jako autorytatywna biblioteka stylów i jedyne źródło prawdy dla kolorów, ikon, linii i kształtów. Każdy element wizualny ma przypisane znaczenie semantyczne.

## 2. Wymiar 1: Warstwy Architektoniczne (Kolor)

Kolor węzła reprezentuje jego przynależność do jednej z predefiniowanych warstw architektonicznych.

| Warstwa Architektoniczna | Kolor | `classDef` | Odpowiedzialność i Katalogi |
| :--- | :--- | :--- | :--- |
| **Core Engine** | 🟦 Niebieski | `core` | Niskopoziomowy silnik, framework, runtime, podstawowe API.<br/>*Katalogi: [`../01_core/`](../01_core/), [`../01_runtime/`](../01_runtime/), [`../15_vc16/`](../15_vc16/)* |
| **Subsystemy** | 🟩 Zielony | `subsystem` | Wyspecjalizowane, niezależne podsystemy.<br/>*Katalogi: [`../06_assets/`](../06_assets/), [`../08_audio/`](../08_audio/), [`../09_logging/`](../09_logging/), [`../11_data/`](../11_data/)* |
| **Logika Gry & Moduły** | 🟧 Pomarańczowy | `game` | Logika specyficzna dla gry, system modułów i zdarzeń.<br/>*Katalogi: [`../02_events/`](../02_events/), [`../03_modules/`](../03_modules/), [`../05_events/`](../05_events/), [`../10_game_runtime/`](../10_game_runtime/), [`../12_otmod/`](../12_otmod/)* |
| **User Interface (UI)** | 🟪 Fioletowy | `ui` | Komponenty interfejsu użytkownika, layouty i OTUI.<br/>*Katalogi: [`../04_ui/`](../04_ui/), [`../13_layouts/`](../13_layouts/)* |
| **Networking & Security** | 🟥 Czerwony | `netsec` | Komunikacja sieciowa, protokoły i szyfrowanie.<br/>*Katalogi: [`../05_network/`](../05_network/), [`../07_settings_crypto/`](../07_settings_crypto/)* |
| **Platforma** | 🔳 Szary | `platform` | Kod specyficzny dla danej platformy.<br/>*Katalogi: [`../14_android/`](../14_android/)* |

**Definicje CSS-podobne (`classDef`):**
```mermaid
classDef core fill:#3498db,stroke:#fff,color:#fff
classDef subsystem fill:#2ecc71,stroke:#fff,color:#fff
classDef game fill:#e67e22,stroke:#fff,color:#fff
classDef ui fill:#9b59b6,stroke:#fff,color:#fff
classDef netsec fill:#c0392b,stroke:#fff,color:#fff
classDef platform fill:#7f8c8d,stroke:#fff,color:#fff
classDef critical fill:#e74c3c,stroke:#fff,color:#fff
```

## 3. Wymiar 2: Typy Komponentów (Ikona)

Ikona wewnątrz węzła reprezentuje jego techniczną rolę.

| Ikona | Typ Komponentu | Opis |
| :--- | :--- | :--- |
| ⚙️ `fa-cogs` | **Menedżer** | Klasy zarządzające cyklem życia innych obiektów. |
| 🗃️ `fa-database` | **Dane/Struktura** | Klasy, których głównym celem jest przechowywanie i udostępnianie danych. |
| ⚡ `fa-bolt` | **Zdarzenie/Sygnał** | Zdarzenia, sygnały, callbacki i ich dyspozytorzy. |
| 🔌 `fa-plug` | **Interfejs/API** | Punkty styku między systemami; fasady upraszczające użycie. |
| 📄 `fa-file-alt` | **Plik/Zasób** | Reprezentacja plików, zasobów lub danych ładowanych z dysku. |
| ⚠️ `fa-exclamation-triangle` | **Błąd/Krytyczny** | Wyjątki, obsługa błędów, operacje krytyczne (używać z `classDef critical`). |

## 4. Style Linii (Rodzaj Połączenia)

Styl linii między węzłami precyzuje naturę interakcji.

| Styl | Składnia Mermaid | Znaczenie |
| :--- | :--- | :--- |
| **Ciągła** | `-->` | **Wywołanie synchroniczne.** Bezpośrednie wywołanie funkcji/metody; przepływ blokujący. |
| **Przerywana** | `-.->` | **Wywołanie asynchroniczne.** Zdarzenie, callback, komunikat; przepływ nieblokujący. |
| **Pogrubiona** | `==>` | **Kluczowy przepływ danych.** Reprezentuje główną ścieżkę danych w diagramie. |

## 5. Linki (`click`)

Każdy węzeł reprezentujący konkretną klasę lub komponent musi zawierać interaktywny link (`click`) do odpowiedniej strony dokumentacji API. Link musi być jak najbardziej precyzyjny.
