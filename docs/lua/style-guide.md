# Przewodnik po stylu kodowania Lua

Ponizsze zasady maja na celu zapewnienie sp�jnosci i wysokiej czytelnosci kodu Lua w calym projekcie OTCv8.

### 1. Nazewnictwo

- **Zmienne i funkcje**: Uzywaj `snake_case`. Nazwy powinny byc opisowe i w jezyku angielskim.
  ```lua
  local player_name = "Gandalf"
  function get_player_items(player)
    -- ...
  end
  ```
- **Stale**: Uzywaj `UPPER_SNAKE_CASE` dla wartosci, kt�re nie powinny sie zmieniac.
  ```lua
  local MAX_CONNECTIONS = 10
  ```
- **Zmienne "prywatne"**: Poprzedzaj nazwe podkreslnikiem (`_`), jesli zmienna lub funkcja nie powinna byc uzywana poza modulem.
  ```lua
  local function _private_helper()
    -- ...
  end
  ```

### 2. Struktura Kodu

- **Struktura modulu**: Kazdy plik powinien dzialac jak modul. Zwracaj tabele z publicznym API na koncu pliku.
  ```lua
  local M = {} -- 'M' od 'Module'

  function M.public_function()
    -- ...
  end

  return M
  ```
- **Czystosc `require`**: Wywolanie `require` powinno byc wolne od efekt�w ubocznych. Powinno jedynie zaladowac i zwr�cic modul, a nie modyfikowac globalny stan.

- **Rozmiar**:
  - **Pliki**: Staraj sie, aby pliki nie przekraczaly 300 linii.
  - **Funkcje**: Daz do tego, by funkcje mialy maksymalnie 50 linii. Dluzsze funkcje nalezy dzielic na mniejsze, pomocnicze.

### 3. Obsluga Bled�w i Logowanie

- **Krytyczne sciezki**: Uzywaj `pcall()` lub `xpcall()` do obslugi operacji, kt�re moga zakonczyc sie bledem (np. odczyt plik�w, zapytania sieciowe).
  ```lua
  local status, result = pcall(function()
    return risky_operation()
  end)

  if not status then
    log_error("Operacja nie powiodla sie: " .. tostring(result))
  end
  ```
- **Logowanie**: Implementuj logowanie warunkowe, kontrolowane przez globalna flage `DEBUG`, aby uniknac zasmiecania konsoli w wersji produkcyjnej.
  ```lua
  if DEBUG then
    print("Wartosc x:", x)
  end
  ```