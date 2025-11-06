# Przewodnik Projektowania Diagramów

Ten dokument definiuje oficjalne standardy wizualizacji dla wszystkich diagramów Mermaid w projekcie.

## System Kodowania Wizualnego

System opiera się na dwóch wymiarach: **kolorze** (reprezentującym Warstwę Architektoniczną) i **ikonie** (reprezentującej Typ Komponentu).

### Warstwy Architektoniczne (Kolor)

| Kolor | Warstwa | Opis i Katalogi |
| :--- | :--- | :--- |
| 🟦 | **Core Engine** | Niskopoziomowy silnik, framework i podstawowe API.<br/>*Katalogi: [`01_core`](./01_core/), [`01_runtime`](./01_runtime/), [`15_vc16`](./15_vc16/)* |
| 🟩 | **Subsystemy** | Wyspecjalizowane, niezależne podsystemy.<br/>*Katalogi: [`06_assets`](./06_assets/), [`08_audio`](./08_audio/), [`09_logging`](./09_logging/), [`11_data`](./11_data/)* |
| 🟧 | **Logika Gry & Moduły** | Logika specyficzna dla gry, system modułów i zdarzeń.<br/>*Katalogi: [`02_events`](./02_events/), [`03_modules`](./03_modules/), [`05_events`](./05_events/), [`10_game_runtime`](./10_game_runtime/), [`12_otmod`](./12_otmod/)* |
| 🟪 | **User Interface (UI)** | Komponenty interfejsu użytkownika, layouty i OTUI.<br/>*Katalogi: [`04_ui`](./04_ui/), [`13_layouts`](./13_layouts/)* |
| 🟥 | **Networking & Security** | Komunikacja sieciowa, protokoły i szyfrowanie.<br/>*Katalogi: [`05_network`](./05_network/), [`07_settings_crypto`](./07_settings_crypto/)* |
| 🔳 | **Platforma** | Kod specyficzny dla danej platformy.<br/>*Katalogi: [`14_android`](./14_android/)* |

### Typy Komponentów (Ikona)

| Ikona | Typ Komponentu | Opis |
| :--- | :--- | :--- |
| ⚙️ `fa-cogs` | **Menedżer** | Klasy zarządzające cyklem życia innych obiektów. |
| 🗃️ `fa-database` | **Dane/Struktura** | Klasy przechowujące i udostępniające dane. |
| ⚡ `fa-bolt` | **Zdarzenie/Sygnał** | Zdarzenia, sygnały, callbacki. |
| 🔌 `fa-plug` | **Interfejs/API** | Punkty styku między systemami, fasady. |
| 📄 `fa-file-alt` | **Plik/Zasób** | Reprezentacja plików lub zasobów z dysku. |
| ⚠️ `fa-exclamation-triangle` | **Błąd/Krytyczny** | Wyjątki, obsługa błędów, operacje krytyczne. |
