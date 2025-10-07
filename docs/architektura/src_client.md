# otclientv8-dev/src/client

> NOTE: Wszystkie pliki w repozytorium sÄ… objÄ™te licencjÄ… MIT (2010â€“2017 OTClient, autor Edubart).
## OgĂłlny opis
Implementacja klasy `AnimatedText`, ktĂłra odpowiada za renderowanie animowanego tekstu na mapie, takiego jak komunikaty o zadanych obraÄąÄ˝eniach, leczeniu czy zdobytych punktach doÄąâ€şwiadczenia. Plik zawiera logikÄ™ animacji, rysowania oraz Äąâ€šÄ…czenia podobnych tekstĂłw w jeden.
## Klasa `AnimatedText`
## Opis
Klasa `AnimatedText` dziedziczy po `Thing` i reprezentuje tekst, ktĂłry pojawia siÄ™ w okreÄąâ€şlonym miejscu na mapie, a nastÄ™pnie animuje swoje poÄąâ€šoÄąÄ˝enie i przezroczystoÄąâ€şÄ‡, by ostatecznie zniknÄ…Ä‡.
## Metody
| Nazwa | Opis |
| --- | --- |
| `AnimatedText()` | Konstruktor. Inicjalizuje domyÄąâ€şlne wÄąâ€šaÄąâ€şciwoÄąâ€şci tekstu, takie jak czcionka i wyrĂłwnanie. |
| `drawText(const Point& dest, const Rect& visibleRect)` | Rysuje tekst w okreÄąâ€şlonym miejscu, uwzglÄ™dniajÄ…c postÄ™p animacji. Animacja obejmuje ruch w gĂłrÄ™ (i opcjonalnie po przekÄ…tnej) oraz stopniowe zanikanie. |
| `onAppear()` | Metoda wywoÄąâ€šywana, gdy tekst pojawia siÄ™ na mapie. Resetuje timer animacji i planuje usuniÄ™cie obiektu po zakoÄąâ€žczeniu animacji. |
| `setColor(int color)` | Ustawia kolor tekstu na podstawie 8-bitowej wartoÄąâ€şci. |
| `setText(const std::string& text)` | Ustawia treÄąâ€şÄ‡ tekstu. |
| `setFont(const std::string& fontName)` | Ustawia czcionkÄ™ tekstu na podstawie nazwy. |
| `merge(const AnimatedTextPtr& other)` | PrĂłbuje poÄąâ€šÄ…czyÄ‡ tekst z innym obiektem `AnimatedText`. ÄąÂÄ…czenie jest moÄąÄ˝liwe, jeÄąâ€şli oba teksty majÄ… ten sam kolor, czcionkÄ™, a animacja obecnego tekstu nie jest zbyt zaawansowana. Teksty liczbowe sÄ… sumowane. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**: UÄąÄ˝ywa `g_map` do usuwania obiektu `AnimatedText` po zakoÄąâ€žczeniu animacji.
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania, czy funkcja `GameDiagonalAnimatedText` jest wÄąâ€šÄ…czona.
- **`framework/core/clock.h`**: UÄąÄ˝ywa `g_clock` do pomiaru czasu animacji.
- **`framework/core/eventdispatcher.h`**: UÄąÄ˝ywa `g_dispatcher` do planowania usuniÄ™cia obiektu.
- **`framework/graphics/graphics.h`**: UÄąÄ˝ywa `g_fonts` do zarzÄ…dzania czcionkami.
## PrzykÄąâ€šad uÄąÄ˝ycia
Obiekty `AnimatedText` sÄ… tworzone przez `ProtocolGame` w odpowiedzi na komunikaty serwera (np. o obraÄąÄ˝eniach) i dodawane do `g_map`, ktĂłra zarzÄ…dza ich cyklem ÄąÄ˝ycia i rysowaniem.

`$fenceInfo
// PrzykÄąâ€šad tworzenia (logika w ProtocolGame::parseAnimatedText)
AnimatedTextPtr animatedText = AnimatedTextPtr(new AnimatedText);
animatedText->setColor(color);
animatedText->setText(text);
g_map.addThing(animatedText, position);
```
---
# Ä‘Ĺşâ€śâ€ž houses.h
## OgĂłlny opis
Plik ten definiuje klasy `House` i `HouseManager`, ktĂłre sÄąâ€šuÄąÄ˝Ä… do zarzÄ…dzania informacjami o domach w grze. Zawiera definicje struktur przechowujÄ…cych atrybuty domĂłw, takie jak nazwa, ID, wejÄąâ€şcie, oraz metody do zarzÄ…dzania nimi.
## Klasa `House`
## Opis
Reprezentuje pojedynczy dom w Äąâ€şwiecie gry. Przechowuje jego atrybuty, listÄ™ przynaleÄąÄ˝nych do niego pĂłl (tiles) oraz drzwi.
## Metody
| Nazwa | Opis |
| --- | --- |
| `House(uint32 hId, ...)` | Konstruktor tworzÄ…cy dom o zadanym ID, nazwie i pozycji wejÄąâ€şciowej. |
| `setTile(const TilePtr& tile)` | Dodaje pole (tile) do domu. |
| `getTile(const Position& pos)` | Zwraca wskaÄąĹźnik do pola na podanej pozycji, jeÄąâ€şli naleÄąÄ˝y ono do domu. |
| `setName(const std::string& name)` | Ustawia nazwÄ™ domu. |
| `getName()` | Zwraca nazwÄ™ domu. |
| `setId(uint32 hId)` | Ustawia unikalne ID domu. |
| `getId()` | Zwraca ID domu. |
| `setTownId(uint32 tid)` | Ustawia ID miasta, w ktĂłrym znajduje siÄ™ dom. |
| `getTownId()` | Zwraca ID miasta. |
| `setSize(uint32 s)` | Ustawia rozmiar domu. |
| `getSize()` | Zwraca rozmiar domu. |
| `setRent(uint32 r)` | Ustawia cenÄ™ wynajmu domu. |
| `getRent()` | Zwraca cenÄ™ wynajmu. |
| `setEntry(const Position& p)` | Ustawia pozycjÄ™ wejÄąâ€şcia do domu. |
| `getEntry()` | Zwraca pozycjÄ™ wejÄąâ€şcia. |
| `addDoor(const ItemPtr& door)` | Dodaje drzwi do domu i przypisuje im unikalne ID. |
| `removeDoor(const ItemPtr& door)` | Usuwa drzwi z domu. |
| `removeDoorById(uint32 doorId)` | Usuwa drzwi na podstawie ich ID. |
## Klasa `HouseManager`
## Opis
Singleton (`g_houses`) zarzÄ…dzajÄ…cy wszystkimi domami w grze. Odpowiada za ich dodawanie, usuwanie, wczytywanie i zapisywanie z plikĂłw XML.
## Metody
| Nazwa | Opis |
| --- | --- |
| `addHouse(const HousePtr& house)` | Dodaje nowy dom do listy. |
| `removeHouse(uint32 houseId)` | Usuwa dom o podanym ID. |
| `getHouse(uint32 houseId)` | Zwraca dom o podanym ID. |
| `getHouseByName(std::string name)` | Zwraca dom o podanej nazwie. |
| `load(const std::string& fileName)` | Wczytuje dane o domach z pliku XML. |
| `save(const std::string& fileName)` | Zapisuje dane o domach do pliku XML. |
| `sort()` | Sortuje listÄ™ domĂłw alfabetycznie wedÄąâ€šug nazwy. |
| `clear()` | CzyÄąâ€şci listÄ™ domĂłw. |
| `getHouseList()` | Zwraca listÄ™ wszystkich domĂłw. |
| `filterHouses(uint32 townId)` | Zwraca listÄ™ domĂłw naleÄąÄ˝Ä…cych do okreÄąâ€şlonego miasta. |
## Zmienne globalne
- `HouseManager g_houses`: Globalna instancja managera domĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw wskaÄąĹźnikĂłw, takich jak `HousePtr` i `TilePtr`.
- **`tile.h`**: UÄąÄ˝ywa obiektĂłw `Tile` do okreÄąâ€şlenia obszaru domu.
- **`item.h`**: ZarzÄ…dza drzwiami, ktĂłre sÄ… obiektami typu `Item`.
- **`framework/luaengine/luaobject.h`**: Klasy sÄ… eksponowane do Lua.

---
# Ä‘Ĺşâ€śâ€ž animatedtext.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `AnimatedText`. Definiuje interfejs klasy, ktĂłra zarzÄ…dza animowanym tekstem na mapie.
## Klasa `AnimatedText`
## Opis
Dziedziczy po `Thing`. SÄąâ€šuÄąÄ˝y do wyÄąâ€şwietlania tekstu, ktĂłry porusza siÄ™ i zanika. Jest to obiekt "efemeryczny", ktĂłry istnieje na mapie tylko przez czas trwania animacji.
## Metody
| Nazwa | Opis |
| --- | --- |
| `AnimatedText()` | Konstruktor. |
| `drawText(const Point& dest, const Rect& visibleRect)` | Rysuje tekst na ekranie z uwzglÄ™dnieniem animacji. |
| `setColor(int color)` | Ustawia kolor tekstu. |
| `setText(const std::string& text)` | Ustawia treÄąâ€şÄ‡ tekstu. |
| `setOffset(const Point& offset)` | Ustawia przesuniÄ™cie (offset) rysowania tekstu, uÄąÄ˝ywane do unikania nakÄąâ€šadania siÄ™ tekstĂłw. |
| `setFont(const std::string& fontName)` | Ustawia czcionkÄ™ tekstu. |
| `getColor()` | Zwraca kolor tekstu. |
| `getCachedText()` | Zwraca obiekt `CachedText` przechowujÄ…cy tekst i informacje o renderowaniu. |
| `getOffset()` | Zwraca aktualne przesuniÄ™cie tekstu. |
| `getTimer()` | Zwraca timer uÄąÄ˝ywany do animacji. |
| `merge(const AnimatedTextPtr& other)` | Funkcja do Äąâ€šÄ…czenia z innym `AnimatedText`. |
| `asAnimatedText()` | Rzutuje wskaÄąĹźnik na `AnimatedTextPtr`. |
| `isAnimatedText()` | Zwraca `true`. |
| `getText()` | Zwraca treÄąâ€şÄ‡ tekstu. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thing.h`**: Klasa bazowa.
- **`framework/graphics/fontmanager.h`**: ZarzÄ…dzanie czcionkami.
- **`framework/core/timer.h`**: Pomiar czasu animacji.
- **`framework/graphics/cachedtext.h`**: Efektywne renderowanie tekstu.

---
# Ä‘Ĺşâ€śâ€ž animator.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Animator`, ktĂłra zarzÄ…dza animacjami klatek dla obiektĂłw w grze, takich jak przedmioty czy efekty.
## Klasa `Animator`
## Opis
Klasa `Animator` kontroluje, ktĂłra klatka animacji powinna byÄ‡ wyÄąâ€şwietlona w danym momencie. ObsÄąâ€šuguje rĂłÄąÄ˝ne tryby animacji, takie jak pÄ™tle, ping-pong, animacje asynchroniczne i losowe.
## Typy wyliczeniowe
- **`AnimationPhase`**: OkreÄąâ€şla fazÄ™ animacji (np. automatyczna, losowa, asynchroniczna).
- **`AnimationDirection`**: OkreÄąâ€şla kierunek animacji (do przodu, do tyÄąâ€šu).
## Metody
| Nazwa | Opis |
| --- | --- |
| `Animator()` | Konstruktor. |
| `unserialize(int animationPhases, const FileStreamPtr& fin)` | Wczytuje dane animatora ze strumienia. |
| `serialize(const FileStreamPtr& fin)` | Zapisuje dane animatora do strumienia. |
| `setPhase(int phase)` | Ustawia bieÄąÄ˝Ä…cÄ… fazÄ™ animacji. |
| `getPhase()` | Oblicza i zwraca bieÄąÄ˝Ä…cÄ… fazÄ™ animacji na podstawie czasu. |
| `getPhaseAt(Timer& timer, int lastPhase)` | Oblicza fazÄ™ animacji w danym momencie czasu (uÄąÄ˝ywane przez `Effect` dla niezaleÄąÄ˝nych animacji). |
| `getStartPhase()` | Zwraca poczÄ…tkowÄ… fazÄ™ animacji. |
| `getAnimationPhases()` | Zwraca caÄąâ€škowitÄ… liczbÄ™ faz animacji. |
| `isAsync()` | Zwraca `true`, jeÄąâ€şli animacja jest asynchroniczna. |
| `isComplete()` | Zwraca `true`, jeÄąâ€şli animacja zostaÄąâ€ša zakoÄąâ€žczona. |
| `getTotalDuration()` | Zwraca caÄąâ€škowity czas trwania animacji. |
| `resetAnimation()` | Resetuje stan animacji do poczÄ…tkowego. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`framework/core/timer.h`**: UÄąÄ˝ywane do pomiaru czasu i synchronizacji animacji.

---
# Ä‘Ĺşâ€śâ€ž animator.cpp
## OgĂłlny opis
Implementacja klasy `Animator`. Zawiera logikÄ™ obliczania faz animacji w zaleÄąÄ˝noÄąâ€şci od czasu i trybu pracy.
## Klasa `Animator`
## Opis
Plik implementuje logikÄ™ dziaÄąâ€šania animatora. Obliczenia fazy zaleÄąÄ˝Ä… od tego, czy animacja jest synchroniczna (wszystkie obiekty tego samego typu animujÄ… siÄ™ tak samo) czy asynchroniczna (kaÄąÄ˝dy obiekt animuje siÄ™ niezaleÄąÄ˝nie).
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(...)` | Wczytuje z pliku binarnego liczbÄ™ faz, tryb `async`, liczbÄ™ pÄ™tli, fazÄ™ startowÄ… oraz czas trwania kaÄąÄ˝dej klatki (min/max). |
| `serialize(...)` | Zapisuje dane animatora do pliku binarnego. |
| `setPhase(int phase)` | Ustawia aktualnÄ… fazÄ™ animacji. Dla animacji asynchronicznych resetuje timer i ustawia czas trwania klatki. Dla synchronicznych przelicza fazÄ™ na podstawie globalnego zegara. |
| `getPhase()` | GÄąâ€šĂłwna metoda aktualizujÄ…ca. Na podstawie czasu, jaki upÄąâ€šynÄ…Äąâ€š od ostatniego wywoÄąâ€šania, decyduje, czy naleÄąÄ˝y przejÄąâ€şÄ‡ do nastÄ™pnej klatki animacji. |
| `getPhaseAt(...)` | Metoda uÄąÄ˝ywana przez efekty (`Effect`) do uzyskania fazy animacji niezaleÄąÄ˝nie od innych obiektĂłw tego samego typu. UÄąÄ˝ywa wÄąâ€šasnego timera i pseudolosowego generatora do okreÄąâ€şlenia czasu trwania klatek. |
| `getStartPhase()` | Zwraca fazÄ™ startowÄ…; jeÄąâ€şli ustawiono na losowÄ…, losuje jÄ… z dostÄ™pnego zakresu. |
| `resetAnimation()` | Przywraca animator do stanu poczÄ…tkowego. |
| `getPingPongPhase()` | Oblicza nastÄ™pnÄ… fazÄ™ dla animacji typu "ping-pong" (do przodu i do tyÄąâ€šu). |
| `getLoopPhase()` | Oblicza nastÄ™pnÄ… fazÄ™ dla animacji w pÄ™tli. |
| `getPhaseDuration(int phase)` | Zwraca czas trwania danej klatki animacji (losowy w zakresie min-max). |
| `calculateSynchronous()` | Oblicza bieÄąÄ˝Ä…cÄ… fazÄ™ dla animacji synchronicznej, bazujÄ…c na globalnym czasie i sumarycznym czasie trwania wszystkich klatek. |
| `getTotalDuration()` | Zwraca sumaryczny czas trwania wszystkich klatek animacji. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/core/clock.h`**: UÄąÄ˝ywa `g_clock` do synchronizacji animacji.
- **`framework/core/filestream.h`**: Do operacji serializacji/deserializacji.

---
# Ä‘Ĺşâ€śâ€ž client.cpp
## OgĂłlny opis
Plik implementuje klasÄ™ `Client`, ktĂłra jest gÄąâ€šĂłwnym punktem wejÄąâ€şcia i zarzÄ…dzania dla aplikacji klienckiej. Odpowiada za inicjalizacjÄ™ i zamykanie kluczowych moduÄąâ€šĂłw gry.
## Klasa `Client`
## Metody
| Nazwa | Opis |
| --- | --- |
| `init(std::vector<std::string>& args)` | Inicjalizuje wszystkie gÄąâ€šĂłwne moduÄąâ€šy klienta w odpowiedniej kolejnoÄąâ€şci: rejestruje funkcje Lua, a nastÄ™pnie inicjalizuje `g_map`, `g_minimap`, `g_game`, `g_shaders`, `g_things`, `g_healthBars`. |
| `terminate()` | Zamyka wszystkie moduÄąâ€šy w odwrotnej kolejnoÄąâ€şci do inicjalizacji, zwalniajÄ…c zasoby. |
## Zmienne globalne
- `Client g_client`: Globalna instancja klasy `Client`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**: Inicjalizuje i zamyka `g_game`.
- **`map.h`**: Inicjalizuje i zamyka `g_map`.
- **`minimap.h`**: Inicjalizuje i zamyka `g_minimap`.
- **`spritemanager.h`**: PoÄąâ€şrednio zarzÄ…dza `g_sprites` poprzez `g_things`.
- **`healthbars.h`**: Inicjalizuje i zamyka `g_healthBars`.
- **`framework/core/modulemanager.h`**: UÄąÄ˝ywane do zarzÄ…dzania moduÄąâ€šami.
- **`framework/graphics/shadermanager.h`**: Inicjalizuje i zamyka `g_shaders`.

---
# Ä‘Ĺşâ€śâ€ž client.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Client`. Deklaruje interfejs gÄąâ€šĂłwnej klasy aplikacji klienckiej.
## Klasa `Client`
## Opis
Klasa `Client` jest odpowiedzialna za zarzÄ…dzanie cyklem ÄąÄ˝ycia aplikacji klienckiej.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init(std::vector<std::string>& args)` | Inicjalizuje aplikacjÄ™. |
| `terminate()` | KoÄąâ€žczy dziaÄąâ€šanie aplikacji, zwalniajÄ…c zasoby. |
| `registerLuaFunctions()` | Rejestruje funkcje C++ dostÄ™pne w Äąâ€şrodowisku Lua. |
## Zmienne globalne
- `Client g_client`: Deklaracja zewnÄ™trznej globalnej instancji klienta.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`global.h`**: Zawiera podstawowe definicje i staÄąâ€še uÄąÄ˝ywane w kliencie.

---
# Ä‘Ĺşâ€śâ€ž CMakeLists.txt
## OgĂłlny opis
Plik konfiguracyjny systemu budowania CMake dla moduÄąâ€šu klienta. Definiuje on, ktĂłre pliki ÄąĹźrĂłdÄąâ€šowe (`.cpp`, `.h`) zostanÄ… skompilowane i wÄąâ€šÄ…czone do finalnej aplikacji klienckiej.
## Struktura pliku
## Definicje preprocesora
- `add_definitions(-DCLIENT)`: Dodaje makro `CLIENT` do wszystkich kompilowanych plikĂłw, co pozwala na warunkowÄ… kompilacjÄ™ kodu specyficznego dla klienta.
## Lista plikĂłw ÄąĹźrĂłdÄąâ€šowych (`client_SOURCES`)
Plik zawiera jednÄ… dÄąâ€šugÄ… listÄ™ wszystkich plikĂłw ÄąĹźrĂłdÄąâ€šowych i nagÄąâ€šĂłwkowych, ktĂłre skÄąâ€šadajÄ… siÄ™ na moduÄąâ€š klienta. Pliki sÄ… pogrupowane w logiczne kategorie za pomocÄ… komentarzy:
- **`# client`**: GÄąâ€šĂłwne pliki klienta.
- **`# core`**: RdzeÄąâ€ž logiki gry (mapa, przedmioty, postacie, etc.).
- **`# lua`**: Pliki zwiÄ…zane z integracjÄ… z silnikiem Lua.
- **`# net`**: Logika sieciowa i protokoÄąâ€šy.
- **`# ui`**: Niestandardowe widÄąÄ˝ety interfejsu uÄąÄ˝ytkownika.
- **`# util`**: Pomocnicze klasy i struktury, jak `Position`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
Ten plik jest kluczowy dla procesu budowania i definiuje, ktĂłre czÄ™Äąâ€şci kodu ÄąĹźrĂłdÄąâ€šowego sÄ… ze sobÄ… powiÄ…zane i tworzÄ… aplikacjÄ™ klienckÄ…. KaÄąÄ˝dy plik dodany do tej listy staje siÄ™ czÄ™Äąâ€şciÄ… projektu.

---
# Ä‘Ĺşâ€śâ€ž const.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy zawierajÄ…cy globalne staÄąâ€še i typy wyliczeniowe uÄąÄ˝ywane w caÄąâ€šej aplikacji klienckiej. Definiuje kluczowe wartoÄąâ€şci, takie jak flagi rysowania, atrybuty przedmiotĂłw, tryby gry, a takÄąÄ˝e identyfikatory funkcji serwera (`GameFeature`).
## Namespace `Otc`
## Typy wyliczeniowe
- **`enum` (anonimowy)**: Zawiera ogĂłlne staÄąâ€še, takie jak `MAX_ELEVATION`, `SEA_FLOOR`, `MAX_Z`, czasy trwania animacji (`ANIMATED_TEXT_DURATION`) i inne.
- **`DepthConst`**: StaÄąâ€še zwiÄ…zane z gÄąâ€šÄ™bokoÄąâ€şciÄ… renderowania.
- **`DrawFlags`**: Flagi okreÄąâ€şlajÄ…ce, ktĂłre elementy sceny majÄ… byÄ‡ rysowane (np. podÄąâ€šoÄąÄ˝e, postacie, efekty).
- **`DatOpts`**: Atrybuty przedmiotĂłw wczytywane z plikĂłw `.dat`.
- **`InventorySlot`**: Identyfikatory slotĂłw ekwipunku.
- **`Statistic`**: Identyfikatory statystyk gracza (ÄąÄ˝ycie, mana, doÄąâ€şwiadczenie).
- **`Skill`**: Identyfikatory umiejÄ™tnoÄąâ€şci gracza.
- **`Direction`**: Kierunki (pĂłÄąâ€šnoc, poÄąâ€šudnie, etc.).
- **`FluidsColor`**, **`FluidsType`**: Kolory i typy pÄąâ€šynĂłw.
- **`FightModes`**, **`ChaseModes`**, **`PVPModes`**: Tryby walki, Äąâ€şcigania i PvP.
- **`PlayerSkulls`**: Typy czaszek nad gÄąâ€šowÄ… gracza.
- **`PlayerShields`**: Typy tarcz imprezowych (party shields).
- **`PlayerEmblems`**: Emblematy gildii.
- **`CreatureIcons`**: Ikony nad postaciami NPC.
- **`PlayerStates`**: Stany gracza (zatrucie, podpalenie, etc.).
- **`MessageMode`**: Tryby wiadomoÄąâ€şci w grze (say, whisper, yell, etc.).
- **`GameFeature`**: Flagi okreÄąâ€şlajÄ…ce, ktĂłre funkcje sÄ… obsÄąâ€šugiwane przez serwer. Jest to kluczowy enum dla zapewnienia kompatybilnoÄąâ€şci z rĂłÄąÄ˝nymi wersjami serwerĂłw.
- **`PathFindResult`**: Wyniki algorytmu wyszukiwania Äąâ€şcieÄąÄ˝ki.
- **`PathFindFlags`**: Flagi modyfikujÄ…ce dziaÄąâ€šanie algorytmu wyszukiwania Äąâ€şcieÄąÄ˝ki.
- **`AutomapFlags`**: Ikony znacznikĂłw na minimapie.
- **`VipState`**: Stany graczy na liÄąâ€şcie VIP.
- **`SpeedFormula`**: RĂłÄąÄ˝ne formuÄąâ€šy obliczania prÄ™dkoÄąâ€şci postaci.
- **`Blessings`**: BÄąâ€šogosÄąâ€šawieÄąâ€žstwa.
- **`DeathType`**: Typ Äąâ€şmierci (zwykÄąâ€ša, z bÄąâ€šogosÄąâ€šawieÄąâ€žstwem).
- **`StoreProductTypes`**, **`StoreErrorTypes`**, **`StoreStates`**: Typy zwiÄ…zane ze sklepem w grze (Store).
- **`Prey...`**: Enumeracje zwiÄ…zane z systemem Prey.
- **`MagicEffectsType_t`**: Typy operacji w zaawansowanych efektach magicznych.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
Ten plik jest fundamentalny i jest doÄąâ€šÄ…czany w wiÄ™kszoÄąâ€şci plikĂłw projektu, poniewaÄąÄ˝ definiuje podstawowe "sÄąâ€šownictwo" uÄąÄ˝ywane w logice gry.

---
# Ä‘Ĺşâ€śâ€ž container.cpp
## OgĂłlny opis
Implementacja klasy `Container`, ktĂłra reprezentuje pojemniki w grze, takie jak plecaki. Plik zawiera logikÄ™ zarzÄ…dzania przedmiotami wewnÄ…trz kontenera oraz obsÄąâ€šugÄ™ zdarzeÄąâ€ž z nim zwiÄ…zanych.
## Klasa `Container`
## Metody
| Nazwa | Opis |
| --- | --- |
| `Container(...)` | Konstruktor. Inicjalizuje kontener na podstawie danych otrzymanych z serwera. |
| `getItem(int slot)` | Zwraca przedmiot znajdujÄ…cy siÄ™ w danym slocie. |
| `onOpen(const ContainerPtr& previousContainer)` | WywoÄąâ€šuje callback Lua `onOpen`, gdy kontener jest otwierany. |
| `onClose()` | Oznacza kontener jako zamkniÄ™ty i wywoÄąâ€šuje callback Lua `onClose`. |
| `onAddItem(const ItemPtr& item, int slot)` | Dodaje przedmiot do kontenera. JeÄąâ€şli kontener ma strony (`hasPages`), a slot jest poza widocznym zakresem, jedynie aktualizuje rozmiar. W przeciwnym razie dodaje przedmiot do listy i wywoÄąâ€šuje callbacki Lua `onSizeChange` i `onAddItem`. |
| `findItemById(uint itemId, int subType)` | Wyszukuje przedmiot w kontenerze po jego ID i opcjonalnie podtypie. |
| `onAddItems(const std::vector<ItemPtr>& items)` | Dodaje wiele przedmiotĂłw naraz (np. przy otwarciu kontenera). |
| `onUpdateItem(int slot, const ItemPtr& item)` | Aktualizuje przedmiot w danym slocie, zastÄ™pujÄ…c stary nowym. |
| `onRemoveItem(int slot, const ItemPtr& lastItem)` | Usuwa przedmiot z danego slota. JeÄąâ€şli `lastItem` jest podany (dla kontenerĂłw ze stronami), jest on dodawany na koÄąâ€žcu widocznej czÄ™Äąâ€şci kontenera. |
| `updateItemsPositions()` | Aktualizuje pozycje wszystkich przedmiotĂłw w kontenerze, aby odzwierciedlaÄąâ€šy ich sloty. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`item.h`**: ZarzÄ…dza obiektami typu `Item`.
- **`framework/luaengine/luaobject.h`**: Dziedziczy po `LuaObject`, aby umoÄąÄ˝liwiÄ‡ interakcjÄ™ z Lua.

---
# Ä‘Ĺşâ€śâ€ž creature.cpp
## OgĂłlny opis
Implementacja klasy `Creature`, ktĂłra jest podstawowÄ… klasÄ… dla wszystkich ÄąÄ˝ywych istot w grze (graczy, potworĂłw, NPC). Plik ten zawiera zÄąâ€šoÄąÄ˝onÄ… logikÄ™ rysowania, animacji, poruszania siÄ™, skakania oraz wyÄąâ€şwietlania informacji o postaci.
## Klasa `Creature`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | GÄąâ€šĂłwna funkcja rysujÄ…ca. Renderuje postaÄ‡, jej ubiĂłr, kwadraty oznaczajÄ…ce (np. cel ataku), a takÄąÄ˝e dodaje Äąâ€şwiatÄąâ€šo do `LightView`. |
| `drawOutfit(...)` | Rysuje sam ubiĂłr postaci w zadanym prostokÄ…cie, uÄąÄ˝ywane gÄąâ€šĂłwnie w interfejsie uÄąÄ˝ytkownika. |
| `drawInformation(...)` | Rysuje pasek ÄąÄ˝ycia, many, nazwÄ™, ikony (czaszka, tarcza) nad postaciÄ…. |
| `turn(Otc::Direction direction)` | Zmienia kierunek, w ktĂłrym zwrĂłcona jest postaÄ‡. |
| `walk(const Position& oldPos, const Position& newPos)` | Inicjuje proces chodzenia z `oldPos` do `newPos`, ustawiajÄ…c kierunek, timery i rozpoczynajÄ…c aktualizacjÄ™ animacji. |
| `stopWalk()` | Natychmiastowo przerywa proces chodzenia. |
| `jump(int height, int duration)` | Rozpoczyna animacjÄ™ skoku postaci. |
| `updateJump()` | Aktualizuje wysokoÄąâ€şÄ‡ skoku w kaÄąÄ˝dej klatce animacji. |
| `onAppear()` | ObsÄąâ€šuguje pojawienie siÄ™ postaci na ekranie. Decyduje, czy postaÄ‡ przyszÄąâ€ša, teleportowaÄąâ€ša siÄ™, czy tylko siÄ™ obrĂłciÄąâ€ša. |
| `onDisappear()` | ObsÄąâ€šuguje znikniÄ™cie postaci z ekranu, planujÄ…c jej ostateczne usuniÄ™cie. |
| `onDeath()` | WywoÄąâ€šuje callback Lua `onDeath`. |
| `updateWalkAnimation(...)` | Aktualizuje fazÄ™ animacji chodzenia na podstawie czasu i przebytych pikseli. |
| `updateWalkOffset(...)` | Oblicza przesuniÄ™cie postaci podczas chodzenia. |
| `updateWalkingTile()` | Aktualizuje, na ktĂłrym polu (`Tile`) postaÄ‡ jest obecnie rysowana podczas animacji chodzenia. |
| `nextWalkUpdate()` | Planuje nastÄ™pnÄ… aktualizacjÄ™ stanu chodzenia. |
| `updateWalk()` | GÄąâ€šĂłwna funkcja aktualizujÄ…ca stan chodzenia, wywoÄąâ€šywana cyklicznie. |
| `terminateWalk()` | KoÄąâ€žczy proces chodzenia, resetujÄ…c wszystkie zwiÄ…zane z nim zmienne. |
| `setHealthPercent(uint8 healthPercent)` | Ustawia procent ÄąÄ˝ycia i aktualizuje kolor paska ÄąÄ˝ycia. |
| `setOutfit(const Outfit& outfit)` | Zmienia ubiĂłr postaci. |
| `setSpeed(uint16 speed)` | Ustawia prÄ™dkoÄąâ€şÄ‡ poruszania siÄ™ postaci. |
| `getStepDuration(...)` | Oblicza czas trwania jednego kroku w milisekundach na podstawie prÄ™dkoÄąâ€şci postaci, prÄ™dkoÄąâ€şci podÄąâ€šoÄąÄ˝a i formuÄąâ€š prÄ™dkoÄąâ€şci serwera. |
| `getDisplacement()` | Zwraca przesuniÄ™cie rysowania postaci, ktĂłre centruje jÄ… na polu. |
| `addTopWidget(...)` / `addBottomWidget(...)` | Dodaje widÄąÄ˝ety, ktĂłre bÄ™dÄ… rysowane nad lub pod postaciÄ…. |
## Zmienne statyczne
- `m_speedFormula`: Tablica przechowujÄ…ca wspĂłÄąâ€šczynniki do zaawansowanego obliczania prÄ™dkoÄąâ€şci.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`localplayer.h`**: Logika rysowania informacji o pasku many jest specyficzna dla lokalnego gracza.
- **`map.h`**, **`tile.h`**: Interakcje ze Äąâ€şwiatem gry (pobieranie pĂłl, prÄ™dkoÄąâ€şci podÄąâ€šoÄąÄ˝a).
- **`game.h`**: DostÄ™p do globalnych ustawieÄąâ€ž gry i funkcji serwera.
- **`lightview.h`**: Dodawanie dynamicznego Äąâ€şwiatÄąâ€ša emitowanego przez postaÄ‡.
- **`healthbars.h`**: UÄąÄ˝ywa `g_healthBars` do pobierania niestandardowych teÄąâ€š dla paskĂłw ÄąÄ˝ycia/many.
- **`spritemanager.h`**: UÄąÄ˝ywa `g_sprites` do pobierania rozmiaru sprite'Ăłw.

---
# Ä‘Ĺşâ€śâ€ž container.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Container`. Definiuje interfejs do zarzÄ…dzania pojemnikami w grze.
## Klasa `Container`
## Opis
Klasa `Container` dziedziczy po `LuaObject`, co pozwala na jej uÄąÄ˝ycie w skryptach Lua. Reprezentuje obiekt w grze, ktĂłry moÄąÄ˝e przechowywaÄ‡ inne przedmioty, jak plecak czy skrzynka.
## Metody
| Nazwa | Opis |
| --- | --- |
| `getItem(int slot)` | Zwraca wskaÄąĹźnik do przedmiotu w danym slocie. |
| `getItems()` | Zwraca kolekcjÄ™ (`std::deque`) wszystkich przedmiotĂłw w kontenerze. |
| `getItemsCount()` | Zwraca liczbÄ™ przedmiotĂłw w kontenerze. |
| `getSlotPosition(int slot)` | Zwraca specjalnie zakodowanÄ… pozycjÄ™, ktĂłra identyfikuje slot w tym kontenerze. |
| `getId()` | Zwraca ID kontenera. |
| `getCapacity()` | Zwraca pojemnoÄąâ€şÄ‡ kontenera. |
| `getContainerItem()` | Zwraca przedmiot, ktĂłry reprezentuje ten kontener. |
| `getName()` | Zwraca nazwÄ™ kontenera. |
| `hasParent()` | Zwraca `true`, jeÄąâ€şli kontener znajduje siÄ™ w innym kontenerze. |
| `isClosed()` | Zwraca `true`, jeÄąâ€şli kontener zostaÄąâ€š zamkniÄ™ty. |
| `isUnlocked()` | Zwraca `true`, jeÄąâ€şli moÄąÄ˝na przesuwaÄ‡ w nim przedmioty. |
| `hasPages()` | Zwraca `true`, jeÄąâ€şli kontener obsÄąâ€šuguje paginacjÄ™. |
| `getSize()` | Zwraca caÄąâ€škowitÄ… liczbÄ™ przedmiotĂłw w kontenerze (moÄąÄ˝e byÄ‡ wiÄ™ksza niÄąÄ˝ pojemnoÄąâ€şÄ‡, jeÄąâ€şli ma strony). |
| `getFirstIndex()` | Zwraca indeks pierwszego przedmiotu na bieÄąÄ˝Ä…cej stronie. |
| `findItemById(uint itemId, int subType)` | Wyszukuje przedmiot po ID i opcjonalnym podtypie. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw, np. `ItemPtr`.
- **`item.h`**: Przechowuje obiekty `Item`.
- **`game.h`**: Klasa `Game` jest przyjacielem, co pozwala jej wywoÄąâ€šywaÄ‡ chronione metody `onOpen`, `onClose`, etc.

---
# Ä‘Ĺşâ€śâ€ž creature.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Creature` oraz jej specjalizacji: `Npc` i `Monster`. Definiuje interfejs dla wszystkich istot w grze.
## Klasa `Creature`
## Opis
Klasa bazowa dla wszystkich postaci w grze. Dziedziczy po `Thing`. Zawiera logikÄ™ zwiÄ…zanÄ… z wyglÄ…dem, ruchem, stanami i interakcjami.
## Typy wyliczeniowe
- **`enum` (anonimowy)**: Definiuje staÄąâ€še `SHIELD_BLINK_TICKS` i `VOLATILE_SQUARE_DURATION`.
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje postaÄ‡ w danym miejscu na mapie. |
| `drawOutfit(...)` | Rysuje sam ubiĂłr postaci, uÄąÄ˝ywane w UI. |
| `drawInformation(...)` | Rysuje informacje nad postaciÄ… (nazwa, paski ÄąÄ˝ycia/many, ikony). |
| `setId(uint32 id)` | Ustawia ID postaci. |
| `setName(const std::string& name)` | Ustawia nazwÄ™ postaci. |
| `setHealthPercent(uint8 healthPercent)` | Ustawia procent ÄąÄ˝ycia. |
| `setDirection(Otc::Direction direction)` | Ustawia kierunek, w ktĂłrym postaÄ‡ jest zwrĂłcona. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubiĂłr postaci. |
| `setSpeed(uint16 speed)` | Ustawia prÄ™dkoÄąâ€şÄ‡ poruszania siÄ™. |
| `addTimedSquare(uint8 color)` | WyÄąâ€şwietla tymczasowy kolorowy kwadrat pod postaciÄ…. |
| `getStepDuration(...)` | Zwraca czas trwania jednego kroku. |
| `walk(const Position& oldPos, const Position& newPos)` | Inicjuje ruch postaci. |
| `stopWalk()` | Przerywa ruch postaci. |
| `isWalking()` | Zwraca `true`, jeÄąâ€şli postaÄ‡ jest w trakcie chodu. |
| `isDead()` | Zwraca `true`, jeÄąâ€şli postaÄ‡ ma 0% ÄąÄ˝ycia. |
| `getThingType()` | Zwraca `ThingType` dla aktualnego ubioru postaci. |
| `addTopWidget(...)`, `addBottomWidget(...)` | Dodaje widÄąÄ˝ety do rysowania nad/pod postaciÄ…. |
## Klasa `Npc`
## Opis
Specjalizacja `Creature` dla postaci niezaleÄąÄ˝nych (NPC).
## Klasa `Monster`
## Opis
Specjalizacja `Creature` dla potworĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thing.h`**: Klasa bazowa.
- **`outfit.h`**: UÄąÄ˝ywa `Outfit` do zarzÄ…dzania wyglÄ…dem.
- **`tile.h`**: Interakcje z polami mapy.
- **`mapview.h`**: UÄąÄ˝ywana do rysowania w kontekÄąâ€şcie widoku mapy.
- **`framework/ui/uiwidget.h`**: DoÄąâ€šÄ…czanie widÄąÄ˝etĂłw do postaci.

---
# Ä‘Ĺşâ€śâ€ž creatures.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy klasy do zarzÄ…dzania typami stworzeÄąâ€ž (`CreatureType`) oraz ich miejscami odradzania (`Spawn`). Jest to czÄ™Äąâ€şÄ‡ systemu, ktĂłry prawdopodobnie sÄąâ€šuÄąÄ˝y do edycji map lub dziaÄąâ€šania jako serwer, a nie tylko do gry.
## Typy wyliczeniowe
- **`CreatureAttr`**: Atrybuty typu stworzenia (pozycja, nazwa, ubiĂłr, etc.).
- **`CreatureRace`**: Rasa stworzenia (NPC, potwĂłr).
- **`SpawnAttr`**: Atrybuty spawnu (promieÄąâ€ž, Äąâ€şrodek).
## Klasa `Spawn`
## Opis
Reprezentuje obszar odradzania siÄ™ stworzeÄąâ€ž (spawn). Przechowuje informacje o Äąâ€şrodku, promieniu oraz listÄ™ potworĂłw/NPC, ktĂłre siÄ™ w nim pojawiajÄ….
## Metody
| Nazwa | Opis |
| --- | --- |
| `setRadius(int32 r)` | Ustawia promieÄąâ€ž spawnu. |
| `getRadius()` | Zwraca promieÄąâ€ž spawnu. |
| `setCenterPos(const Position& pos)` | Ustawia centralnÄ… pozycjÄ™ spawnu. |
| `getCenterPos()` | Zwraca centralnÄ… pozycjÄ™ spawnu. |
| `getCreatures()` | Zwraca listÄ™ typĂłw stworzeÄąâ€ž w tym spawnie. |
| `addCreature(const Position& placePos, const CreatureTypePtr& cType)` | Dodaje stworzenie do spawnu w okreÄąâ€şlonym miejscu. |
| `removeCreature(const Position& pos)` | Usuwa stworzenie z danej pozycji. |
| `clear()` | CzyÄąâ€şci listÄ™ stworzeÄąâ€ž. |
## Klasa `CreatureType`
## Opis
Reprezentuje szablon (typ) stworzenia. Przechowuje domyÄąâ€şlne wÄąâ€šaÄąâ€şciwoÄąâ€şci, takie jak nazwa, ubiĂłr czy kierunek, ktĂłre sÄ… uÄąÄ˝ywane do tworzenia instancji `Creature`.
## Metody
| Nazwa | Opis |
| --- | --- |
| `setSpawnTime(int32 spawnTime)` | Ustawia czas odradzania. |
| `getSpawnTime()` | Zwraca czas odradzania. |
| `setName(const std::string& name)` | Ustawia nazwÄ™ typu. |
| `getName()` | Zwraca nazwÄ™. |
| `setOutfit(const Outfit& o)` | Ustawia domyÄąâ€şlny ubiĂłr. |
| `getOutfit()` | Zwraca domyÄąâ€şlny ubiĂłr. |
| `cast()` | Tworzy i zwraca instancjÄ™ `Creature` na podstawie tego typu. |
## Klasa `CreatureManager`
## Opis
Singleton (`g_creatures`) zarzÄ…dzajÄ…cy wszystkimi typami stworzeÄąâ€ž i spawnami. Wczytuje te dane z plikĂłw XML.
## Metody
| Nazwa | Opis |
| --- | --- |
| `loadMonsters(const std::string& file)` | Wczytuje dane o potworach z pliku. |
| `loadNpcs(const std::string& folder)` | Wczytuje dane o NPC z folderu. |
| `loadSpawns(const std::string& fileName)` | Wczytuje dane o spawnach. |
| `saveSpawns(const std::string& fileName)` | Zapisuje dane o spawnach. |
| `getCreatureByName(std::string name)` | Zwraca typ stworzenia po nazwie. |
| `getSpawn(const Position& centerPos)` | Zwraca spawn na podstawie jego centralnej pozycji. |
| `addSpawn(...)` | Dodaje nowy spawn. |
## Zmienne globalne
- `CreatureManager g_creatures`: Globalna instancja managera stworzeÄąâ€ž.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**, **`outfit.h`**: Definicje typĂłw.
- **`creature.h`**: `CreatureType::cast()` tworzy obiekty `Creature`.

---
# Ä‘Ĺşâ€śâ€ž declarations.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy zawierajÄ…cy deklaracje wyprzedzajÄ…ce (forward declarations) oraz definicje typĂłw wskaÄąĹźnikĂłw i kolekcji uÄąÄ˝ywanych w caÄąâ€šym module klienta. Jego gÄąâ€šĂłwnym celem jest przeÄąâ€šamanie cyklicznych zaleÄąÄ˝noÄąâ€şci miÄ™dzy plikami nagÄąâ€šĂłwkowymi.
## ZawartoÄąâ€şÄ‡
## Deklaracje wyprzedzajÄ…ce
Plik deklaruje istnienie klas bez koniecznoÄąâ€şci doÄąâ€šÄ…czania ich peÄąâ€šnych definicji. Obejmuje to klasy z rĂłÄąÄ˝nych moduÄąâ€šĂłw:
- **Core**: `Map`, `Game`, `Tile`, `Thing`, `Item`, `Creature`, `LocalPlayer`, `Effect`, `House`, `Town` itp.
- **Net**: `ProtocolLogin`, `ProtocolGame`.
- **UI**: `UIItem`, `UICreature`, `UIMap`, `UIMinimap` itp.
- **Custom**: `HealthBar`.
## Definicje typĂłw (`typedef`)
Definiuje inteligentne wskaÄąĹźniki (`shared_object_ptr`) dla wiÄ™kszoÄąâ€şci zadeklarowanych klas, np.:
- `MapViewPtr`
- `TilePtr`
- `ThingPtr`
- `ItemPtr`
- `CreaturePtr`
- `LocalPlayerPtr`
## Definicje kolekcji (`typedef`)
Definiuje standardowe typy kolekcji dla zadeklarowanych obiektĂłw, uÄąâ€šatwiajÄ…c ich uÄąÄ˝ycie w kodzie:
- `ThingList` (`std::vector<ThingPtr>`)
- `HouseList` (`std::list<HousePtr>`)
- `TileMap` (`std::unordered_map<Position, TilePtr, PositionHasher>`)
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`global.h`**: DoÄąâ€šÄ…cza podstawowe definicje.
- Plik ten jest doÄąâ€šÄ…czany przez niemal wszystkie inne pliki nagÄąâ€šĂłwkowe w module, aby zapewniÄ‡ dostÄ™p do definicji typĂłw wskaÄąĹźnikĂłw i uniknÄ…Ä‡ problemĂłw z zaleÄąÄ˝noÄąâ€şciami.

---
# Ä‘Ĺşâ€śâ€ž creatures.cpp
## OgĂłlny opis
Implementacja `CreatureManager` i `Spawn`, odpowiedzialnych za zarzÄ…dzanie typami stworzeÄąâ€ž i ich miejscami odradzania. Plik zawiera logikÄ™ wczytywania i zapisywania danych z plikĂłw XML oraz zarzÄ…dzania stworzeniami na mapie.
## Funkcje pomocnicze
- **`isInZone(...)`**: Sprawdza, czy dana pozycja znajduje siÄ™ w promieniu spawnu.
## Klasa `Spawn`
## Metody
| Nazwa | Opis |
| --- | --- |
| `load(TiXmlElement* node)` | Wczytuje dane spawnu z wÄ™zÄąâ€ša XML, w tym pozycjÄ™ centralnÄ…, promieÄąâ€ž oraz listÄ™ stworzeÄąâ€ž z ich atrybutami. |
| `save(TiXmlElement* node)` | Zapisuje dane spawnu do wÄ™zÄąâ€ša XML. |
| `addCreature(...)` | Dodaje stworzenie do spawnu. Najpierw tworzy instancjÄ™ `Creature` na podstawie `CreatureType` za pomocÄ… `cast()`, a nastÄ™pnie dodaje jÄ… na mapÄ™ (`g_map.addThing`). |
| `removeCreature(...)` | Usuwa stworzenie ze spawnu i z mapy. |
| `getCreatures()` | Zwraca listÄ™ wszystkich typĂłw stworzeÄąâ€ž w tym spawnie. |
## Klasa `CreatureType`
## Metody
| Nazwa | Opis |
| --- | --- |
| `cast()` | Tworzy nowÄ… instancjÄ™ `Creature`, ustawia jej nazwÄ™, kierunek i ubiĂłr na podstawie danych z `CreatureType`, a nastÄ™pnie zwraca jÄ… jako `CreaturePtr`. |
## Klasa `CreatureManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `terminate()` | CzyÄąâ€şci wszystkie dane managera. |
| `loadMonsters(const std::string& file)` | Wczytuje gÄąâ€šĂłwny plik XML z potworami, ktĂłry zawiera odnoÄąâ€şniki do pojedynczych plikĂłw XML dla kaÄąÄ˝dego potwora. |
| `loadSingleCreature(const std::string& file)` | Wczytuje dane pojedynczego stworzenia z pliku XML. |
| `loadNpcs(const std::string& folder)` | Wczytuje wszystkie pliki XML z danego folderu jako definicje NPC. |
| `loadSpawns(const std::string& fileName)` | Wczytuje plik XML ze spawnami i umieszcza stworzenia na mapie. |
| `saveSpawns(const std::string& fileName)` | Zapisuje aktualny stan spawnĂłw do pliku XML. |
| `internalLoadCreatureBuffer(...)` | Parsuje bufor XML z definicjÄ… stworzenia, tworzy obiekt `CreatureType` i dodaje go do listy. |
| `getCreatureByName(std::string name)` | Wyszukuje typ stworzenia po nazwie (z normalizacjÄ… wielkoÄąâ€şci liter). |
| `getCreatureByLook(int look)` | Wyszukuje typ stworzenia po jego ID wyglÄ…du (outfit ID lub item ID). |
| `getSpawn(...)` / `getSpawnForPlacePos(...)` | Wyszukuje spawn na podstawie pozycji. |
| `addSpawn(...)` | Dodaje nowy spawn lub aktualizuje istniejÄ…cy. |
| `deleteSpawn(...)` | Usuwa spawn z managera. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**: Dodaje i usuwa stworzenia z mapy (`g_map`).
- **`creature.h`**: Tworzy instancje `Creature`.
- **`framework/xml/tinyxml.h`**: UÄąÄ˝ywane do parsowania plikĂłw XML.
- **`framework/core/resourcemanager.h`**: Do odczytu plikĂłw z danymi.

---
# Ä‘Ĺşâ€śâ€ž effect.cpp
## OgĂłlny opis
Implementacja klasy `Effect`, ktĂłra odpowiada za renderowanie efektĂłw wizualnych na mapie, takich jak eksplozje, efekty magiczne itp.
## Klasa `Effect`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje efekt na ekranie. Oblicza aktualnÄ… fazÄ™ animacji na podstawie czasu, ktĂłry upÄąâ€šynÄ…Äąâ€š od pojawienia siÄ™ efektu. JeÄąâ€şli wÄąâ€šÄ…czona jest funkcja `GameEnhancedAnimations`, uÄąÄ˝ywa `Animator::getPhaseAt` dla pÄąâ€šynniejszej, niezaleÄąÄ˝nej animacji. |
| `onAppear()` | Metoda wywoÄąâ€šywana, gdy efekt pojawia siÄ™ na mapie. Resetuje timer animacji i planuje automatyczne usuniÄ™cie efektu po zakoÄąâ€žczeniu jego caÄąâ€škowitego czasu trwania. |
| `setId(uint32 id)` | Ustawia ID efektu, sprawdzajÄ…c jego poprawnoÄąâ€şÄ‡ w `g_things`. |
| `getThingType()` / `rawGetThingType()` | ZwracajÄ… `ThingType` dla danego efektu. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**: UÄąÄ˝ywa `g_map` do usuniÄ™cia efektu po zakoÄąâ€žczeniu animacji.
- **`game.h`**: Sprawdza, czy wÄąâ€šÄ…czona jest funkcja `GameEnhancedAnimations`.
- **`framework/core/eventdispatcher.h`**: UÄąÄ˝ywa `g_dispatcher` do planowania usuniÄ™cia.

---
# Ä‘Ĺşâ€śâ€ž global.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy, ktĂłry peÄąâ€šni rolÄ™ centralnego punktu doÄąâ€šÄ…czania najwaÄąÄ˝niejszych plikĂłw nagÄąâ€šĂłwkowych uÄąÄ˝ywanych w caÄąâ€šym projekcie klienta.
## ZawartoÄąâ€şÄ‡
- **`#include <framework/global.h>`**: DoÄąâ€šÄ…cza globalne definicje z warstwy frameworka.
- **`#include "const.h"`**: DoÄąâ€šÄ…cza staÄąâ€še i typy wyliczeniowe specyficzne dla klienta gry.
- **`#include "position.h"`**: DoÄąâ€šÄ…cza definicjÄ™ klasy `Position`.
## Cel
Celem tego pliku jest uproszczenie doÄąâ€šÄ…czania nagÄąâ€šĂłwkĂłw w innych plikach. Zamiast doÄąâ€šÄ…czaÄ‡ wiele podstawowych plikĂłw, wystarczy doÄąâ€šÄ…czyÄ‡ `global.h`.

---
# Ä‘Ĺşâ€śâ€ž effect.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Effect`, definiujÄ…cy jej interfejs.
## Klasa `Effect`
## Opis
Klasa `Effect` dziedziczy po `Thing` i reprezentuje krĂłtkotrwaÄąâ€šy efekt wizualny na mapie.
## StaÄąâ€še
- **`EFFECT_TICKS_PER_FRAME`**: DomyÄąâ€şlny czas trwania jednej klatki animacji efektu (75 ms).
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje efekt w danym miejscu na mapie. |
| `setId(uint32 id)` | Ustawia ID (typ) efektu. |
| `getId()` | Zwraca ID efektu. |
| `asEffect()` | Rzutuje wskaÄąĹźnik na `EffectPtr`. |
| `isEffect()` | Zwraca `true`. |
| `getThingType()` | Zwraca `ThingType` dla tego efektu. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thing.h`**: Klasa bazowa.
- **`framework/core/timer.h`**: UÄąÄ˝ywa `Timer` do Äąâ€şledzenia postÄ™pu animacji.

---
# Ä‘Ĺşâ€śâ€ž healthbars.cpp
## OgĂłlny opis
Implementacja `HealthBars`, globalnego managera niestandardowych teÄąâ€š dla paskĂłw ÄąÄ˝ycia i many. UmoÄąÄ˝liwia Äąâ€šadowanie i przypisywanie rĂłÄąÄ˝nych grafik do paskĂłw zdrowia w zaleÄąÄ˝noÄąâ€şci od ID ubioru postaci.
## Klasa `HealthBars`
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` | Inicjalizuje wektory na paski ÄąÄ˝ycia i many, rezerwujÄ…c miejsce i dodajÄ…c `nullptr` jako domyÄąâ€şlny pasek (ID 0). |
| `terminate()` | CzyÄąâ€şci wszystkie zaÄąâ€šadowane tÄąâ€ša paskĂłw. |
| `addHealthBackground(...)` | Dodaje nowe tÄąâ€šo dla paska ÄąÄ˝ycia. Tworzy obiekt `HealthBar`, ustawia jego wÄąâ€šaÄąâ€şciwoÄąâ€şci (Äąâ€şcieÄąÄ˝ka, tekstura, offsety, wysokoÄąâ€şÄ‡) i dodaje go do wektora `m_healthBars`. |
| `addManaBackground(...)` | DziaÄąâ€ša analogicznie do `addHealthBackground`, ale dla paskĂłw many. |
| `getHealthBarPath(int id)` | Zwraca Äąâ€şcieÄąÄ˝kÄ™ do pliku graficznego dla paska ÄąÄ˝ycia o danym ID. |
| `getManaBarPath(int id)` | Zwraca Äąâ€şcieÄąÄ˝kÄ™ do pliku graficznego dla paska many o danym ID. |
| `getHealthBarOffset(int id)` | Zwraca przesuniÄ™cie tÄąâ€ša dla paska ÄąÄ˝ycia. |
| `getManaBarOffset(int id)` | Zwraca przesuniÄ™cie tÄąâ€ša dla paska many. |
| `getHealthBarOffsetBar(int id)` | Zwraca przesuniÄ™cie samego paska (wypeÄąâ€šnienia) wewnÄ…trz tÄąâ€ša. |
| `getManaBarOffsetBar(int id)` | DziaÄąâ€ša analogicznie dla paska many. |
| `getHealthBarHeight(int id)` | Zwraca wysokoÄąâ€şÄ‡ paska ÄąÄ˝ycia. |
| `getManaBarHeight(int id)` | Zwraca wysokoÄąâ€şÄ‡ paska many. |
## Klasa `HealthBar`
## Metody
| Nazwa | Opis |
| --- | --- |
| `setTexture(const std::string& path)` | Wczytuje teksturÄ™ tÄąâ€ša paska z podanej Äąâ€şcieÄąÄ˝ki za pomocÄ… `g_textures`. |
## Zmienne globalne
- `HealthBars g_healthBars`: Globalna instancja managera.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/graphics/texturemanager.h`**: UÄąÄ˝ywa `g_textures` do Äąâ€šadowania grafik.
- **`creature.cpp`**: Logika rysowania informacji o postaci (`drawInformation`) uÄąÄ˝ywa `g_healthBars` do pobierania niestandardowych teÄąâ€š paskĂłw.

---
# Ä‘Ĺşâ€śâ€ž game.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Game`, ktĂłra jest centralnym punktem zarzÄ…dzania stanem gry. Definiuje interfejs do obsÄąâ€šugi logowania, akcji gracza, komunikacji z serwerem oraz przechowywania stanu gry.
## Klasa `Game`
## Opis
Singleton (`g_game`) peÄąâ€šniÄ…cy rolÄ™ fasady dla caÄąâ€šej logiki gry. ZarzÄ…dza sesjÄ… gracza, protokoÄąâ€šem sieciowym, stanem lokalnego gracza i interakcjami ze Äąâ€şwiatem gry.
## Struktury
- **`UnjustifiedPoints`**: Przechowuje informacje o punktach za nieuzasadnione zabĂłjstwa w systemie PvP.
## Metody (Publiczne)
| Grupa | Metody | Opis |
| --- | --- | --- |
| **ZarzÄ…dzanie sesjÄ…** | `loginWorld`, `playRecord`, `cancelLogin`, `forceLogout`, `safeLogout` | Logowanie do Äąâ€şwiata gry, odtwarzanie nagraÄąâ€ž, wylogowywanie. |
| **Akcje gracza** | `walk`, `autoWalk`, `turn`, `stop`, `look`, `move`, `use`, `useWith` | WysyÄąâ€šanie ÄąÄ˝Ä…daÄąâ€ž akcji gracza do serwera. |
| **Kontenery** | `open`, `close`, `refreshContainer` | ZarzÄ…dzanie kontenerami. |
| **Walka** | `attack`, `follow`, `cancelAttackAndFollow` | ZarzÄ…dzanie atakiem i Äąâ€şledzeniem. |
| **Komunikacja** | `talk`, `talkChannel`, `talkPrivate` | WysyÄąâ€šanie wiadomoÄąâ€şci. |
| **ZarzÄ…dzanie stanem** | `setProtocolVersion`, `setClientVersion`, `enableFeature`, `getFeature` | Konfiguracja klienta i obsÄąâ€šuga funkcji serwera. |
| **Gettery** | `isOnline`, `isDead`, `getLocalPlayer`, `getProtocolGame`, `getPing` | DostÄ™p do aktualnego stanu gry. |
## Metody (Chronione - Handlery ProtokoÄąâ€šu)
Plik definiuje rĂłwnieÄąÄ˝ liczne metody `process...`, ktĂłre sÄ… wywoÄąâ€šywane przez `ProtocolGame` w odpowiedzi na otrzymane pakiety z serwera. PrzykÄąâ€šady:
- `processLoginError`, `processEnterGame`
- `processTextMessage`, `processTalk`
- `processOpenContainer`, `processContainerAddItem`
- `processInventoryChange`
- `processWalkCancel`
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: UÄąÄ˝ywa wielu zadeklarowanych typĂłw (`ItemPtr`, `CreaturePtr`, etc.).
- **`protocolgame.h`**: ÄąĹˇciÄąâ€şle powiÄ…zana z protokoÄąâ€šem sieciowym.
- **`localplayer.h`**: ZarzÄ…dza instancjÄ… `LocalPlayer`.
- **`container.h`**: ZarzÄ…dza kolekcjÄ… otwartych kontenerĂłw.

---
# Ä‘Ĺşâ€śâ€ž healthbars.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy klasy `HealthBar` i `HealthBars` do zarzÄ…dzania niestandardowymi tÄąâ€šami paskĂłw ÄąÄ˝ycia i many.
## Klasa `HealthBar`
## Opis
Prosta klasa przechowujÄ…ca informacje o pojedynczym niestandardowym tle paska zdrowia lub many.
## Metody
| Nazwa | Opis |
| --- | --- |
| `setPath(const std::string& path)` | Ustawia Äąâ€şcieÄąÄ˝kÄ™ do pliku graficznego. |
| `getPath()` | Zwraca Äąâ€şcieÄąÄ˝kÄ™. |
| `setTexture(const std::string& path)` | ÄąÂaduje teksturÄ™. |
| `getTexture()` | Zwraca wskaÄąĹźnik do tekstury. |
| `setOffset(int x, int y)` | Ustawia przesuniÄ™cie (offset) caÄąâ€šego tÄąâ€ša wzglÄ™dem punktu zaczepienia. |
| `getOffset()` | Zwraca przesuniÄ™cie. |
| `setBarOffset(int x, int y)` | Ustawia przesuniÄ™cie samego paska (wypeÄąâ€šnienia) wewnÄ…trz tÄąâ€ša. |
| `getBarOffset()` | Zwraca przesuniÄ™cie paska. |
| `setHeight(int height)` | Ustawia wysokoÄąâ€şÄ‡ paska. |
| `getHeight()` | Zwraca wysokoÄąâ€şÄ‡. |
## Klasa `HealthBars`
## Opis
Singleton (`g_healthBars`) zarzÄ…dzajÄ…cy kolekcjÄ… obiektĂłw `HealthBar`. DziaÄąâ€ša jako repozytorium dla wszystkich niestandardowych teÄąâ€š paskĂłw.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` | Inicjalizuje managera. |
| `terminate()` | Zwalnia zasoby. |
| `addHealthBackground(...)` | Dodaje nowe tÄąâ€šo dla paska ÄąÄ˝ycia. |
| `addManaBackground(...)` | Dodaje nowe tÄąâ€šo dla paska many. |
| `getHealthBar(int id)` | Zwraca obiekt `HealthBar` dla paska ÄąÄ˝ycia o danym ID. |
| `getManaBar(int id)` | Zwraca obiekt `HealthBar` dla paska many o danym ID. |
| `getHealthBarPath(int id)` | Zwraca Äąâ€şcieÄąÄ˝kÄ™ do grafiki paska ÄąÄ˝ycia. |
| `getManaBarPath(int id)` | Zwraca Äąâ€şcieÄąÄ˝kÄ™ do grafiki paska many. |
| `...` | Gettery dla pozostaÄąâ€šych wÄąâ€šaÄąâ€şciwoÄąâ€şci paska. |
## Zmienne globalne
- `HealthBars g_healthBars`: Deklaracja zewnÄ™trznej instancji managera.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Podstawowe definicje.
- **`framework/graphics/declarations.h`**: Deklaracje typĂłw graficznych, np. `TexturePtr`.

---
# Ä‘Ĺşâ€śâ€ž houses.cpp
## OgĂłlny opis
Implementacja klas `House` i `HouseManager`, ktĂłre zarzÄ…dzajÄ… danymi o domach w grze. Plik zawiera logikÄ™ wczytywania i zapisywania danych o domach z/do plikĂłw XML oraz zarzÄ…dzania ich stanem.
## Klasa `House`
## Metody
| Nazwa | Opis |
| --- | --- |
| `setTile(const TilePtr& tile)` | Dodaje pole do domu, ustawiajÄ…c na nim flagÄ™ `TILESTATE_HOUSE` i ID domu. |
| `getTile(const Position& position)` | Zwraca pole na podanej pozycji, jeÄąâ€şli naleÄąÄ˝y ono do domu. |
| `addDoor(const ItemPtr& door)` | Dodaje drzwi do domu, przypisujÄ…c im unikalne, inkrementowane ID. |
| `removeDoorById(uint32 doorId)` | Usuwa drzwi o podanym ID (ustawia wskaÄąĹźnik na `nullptr` w wektorze). |
| `load(const TiXmlElement *elem)` | Wczytuje atrybuty domu (nazwa, czynsz, rozmiar, ID miasta, pozycja wejÄąâ€şcia) z wÄ™zÄąâ€ša XML. |
| `save(TiXmlElement* elem)` | Zapisuje atrybuty domu do wÄ™zÄąâ€ša XML. |
## Klasa `HouseManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addHouse(const HousePtr& house)` | Dodaje dom do listy, jeÄąâ€şli jeszcze nie istnieje. |
| `removeHouse(uint32 houseId)` | Usuwa dom o podanym ID. |
| `getHouse(uint32 houseId)` | Wyszukuje i zwraca dom po jego ID. |
| `getHouseByName(std::string name)` | Wyszukuje i zwraca dom po jego nazwie. |
| `load(const std::string& fileName)` | Wczytuje listÄ™ domĂłw z pliku XML. Dla kaÄąÄ˝dego domu w pliku, jeÄąâ€şli juÄąÄ˝ istnieje w menedÄąÄ˝erze, aktualizuje jego dane; w przeciwnym razie tworzy nowy. |
| `save(const std::string& fileName)` | Zapisuje listÄ™ wszystkich domĂłw do pliku XML. |
| `filterHouses(uint32 townId)` | Zwraca listÄ™ domĂłw naleÄąÄ˝Ä…cych do miasta o podanym ID. |
| `findHouse(uint32 houseId)` | WewnÄ™trzna metoda do wyszukiwania iteratora do domu na liÄąâ€şcie. |
| `sort()` | Sortuje listÄ™ domĂłw alfabetycznie wedÄąâ€šug nazwy. |
## Zmienne globalne
- `HouseManager g_houses`: Globalna instancja managera domĂłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**: Interakcje z obiektami `Tile` (`tile->setFlag(...)`).
- **`framework/core/resourcemanager.h`**: Do odczytu plikĂłw XML z danymi domĂłw.

---
# Ä‘Ĺşâ€śâ€ž item.cpp
## OgĂłlny opis
Implementacja klasy `Item`, ktĂłra reprezentuje przedmioty w grze. Plik zawiera logikÄ™ rysowania przedmiotĂłw, obsÄąâ€šugÄ™ ich atrybutĂłw oraz serializacjÄ™/deserializacjÄ™ do formatu binarnego (OTBM).
## Klasa `Item`
## Metody
| Nazwa | Opis |
| --- | --- |
| `create(int id, int countOrSubtype)` | Statyczna metoda fabryczna do tworzenia przedmiotu na podstawie jego ID klienta. |
| `createFromOtb(int id)` | Statyczna metoda fabryczna do tworzenia przedmiotu na podstawie jego ID serwera (z plikĂłw OTB). |
| `getName()` | Zwraca nazwÄ™ przedmiotu na podstawie jego typu. |
| `draw(...)` | Rysuje przedmiot na ekranie. Oblicza fazÄ™ animacji oraz wzĂłr (pattern) na podstawie jego wÄąâ€šaÄąâ€şciwoÄąâ€şci (np. liczba przedmiotĂłw w stosie, typ pÄąâ€šynu). |
| `setId(uint32 id)` / `setOtbId(uint16 id)` | Ustawia ID przedmiotu, odpowiednio konwertujÄ…c miÄ™dzy ID klienta a serwera. |
| `unserializeItem(const BinaryTreePtr &in)` | Wczytuje atrybuty przedmiotu z binarnego drzewa (format OTBM). |
| `serializeItem(const OutputBinaryTreePtr& out)` | Zapisuje atrybuty przedmiotu do binarnego drzewa. |
| `getSubType()` | Zwraca podtyp przedmiotu (np. typ pÄąâ€šynu). |
| `getCount()` | Zwraca liczbÄ™ przedmiotĂłw w stosie (jeÄąâ€şli jest stackable). |
| `clone()` | Tworzy i zwraca gÄąâ€šÄ™bokÄ… kopiÄ™ przedmiotu. |
| `calculatePatterns(...)` | Oblicza, ktĂłry wzĂłr (pattern) sprite'a powinien byÄ‡ uÄąÄ˝yty, w zaleÄąÄ˝noÄąâ€şci od typu przedmiotu (stackable, hangable, fluid container). |
| `calculateAnimationPhase(bool animate)` | Oblicza bieÄąÄ˝Ä…cÄ… klatkÄ™ animacji. ObsÄąâ€šuguje animacje synchroniczne i asynchroniczne. |
| `getThingType()` / `rawGetThingType()` | ZwracajÄ… `ThingType` dla tego przedmiotu. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thingtypemanager.h`**: UÄąÄ˝ywa `g_things` do uzyskiwania informacji o typach przedmiotĂłw.
- **`spritemanager.h`**: UÄąÄ˝ywa `g_sprites` do pobierania danych o sprite'ach.
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania funkcji serwera (np. `GameNewFluids`).
- **`tile.h`**: Interakcje z polem, na ktĂłrym leÄąÄ˝y przedmiot (np. do okreÄąâ€şlenia, jak zawiesiÄ‡ przedmiot).

---
# Ä‘Ĺşâ€śâ€ž itemtype.cpp
## OgĂłlny opis
Implementacja klasy `ItemType`, ktĂłra reprezentuje szablon (typ) przedmiotu. Plik zawiera logikÄ™ wczytywania definicji typĂłw przedmiotĂłw z binarnego formatu OTB.
## Klasa `ItemType`
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(const BinaryTreePtr& node)` | Deserializuje dane typu przedmiotu z wÄ™zÄąâ€ša binarnego drzewa. Odczytuje kategoriÄ™ przedmiotu oraz listÄ™ jego atrybutĂłw, takich jak ID serwera, ID klienta, nazwa, czy jest zapisywalny itp. ObsÄąâ€šuguje rĂłÄąÄ˝nice w formacie w zaleÄąÄ˝noÄąâ€şci od wersji klienta. |
## Logika serializacji
Metoda `unserialize` zawiera logikÄ™ dostosowujÄ…cÄ… wczytywanie atrybutĂłw do rĂłÄąÄ˝nych wersji klienta Tibii. Na przykÄąâ€šad, dla starszych wersji klienta, ID serwera musi byÄ‡ dostosowane, aby poprawnie mapowaÄ‡ przedmioty.

> NOTE: Statyczna zmienna `lastId` jest uÄąÄ˝ywana do tworzenia "pustych" typĂłw przedmiotĂłw, jeÄąâ€şli w pliku OTB wystÄ™pujÄ… luki w numeracji ID serwera. Jest to mechanizm zapewniajÄ…cy spĂłjnoÄąâ€şÄ‡ indeksowania.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thingtypemanager.h`**: Jest Äąâ€şciÄąâ€şle powiÄ…zana z `ThingTypeManager`, ktĂłry zarzÄ…dza wszystkimi typami przedmiotĂłw i wywoÄąâ€šuje `unserialize`.
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania wersji klienta, co wpÄąâ€šywa na logikÄ™ parsowania.
- **`framework/core/binarytree.h`**: UÄąÄ˝ywa `BinaryTree` do odczytu danych z formatu OTB.

---
# Ä‘Ĺşâ€śâ€ž item.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Item`, ktĂłra reprezentuje konkretny przedmiot w grze.
## Klasa `Item`
## Opis
Dziedziczy po `Thing`. Reprezentuje instancjÄ™ przedmiotu, ktĂłra moÄąÄ˝e znajdowaÄ‡ siÄ™ na mapie, w kontenerze lub w ekwipunku gracza. Posiada wÄąâ€šaÄąâ€şciwoÄąâ€şci takie jak ID, liczba/podtyp, kolor, a takÄąÄ˝e moÄąÄ˝e zawieraÄ‡ inne przedmioty, jeÄąâ€şli jest kontenerem.
## Typy wyliczeniowe
- **`ItemAttr`**: Definiuje klucze atrybutĂłw, ktĂłre mogÄ… byÄ‡ przypisane do przedmiotu (np. `ATTR_COUNT`, `ATTR_ACTION_ID`, `ATTR_TEXT`).
## Metody
| Nazwa | Opis |
| --- | --- |
| `create(int id, ...)` | Statyczna metoda fabryczna do tworzenia przedmiotu po ID klienta. |
| `createFromOtb(int id)` | Statyczna metoda fabryczna do tworzenia przedmiotu po ID serwera (OTB). |
| `draw(...)` | Rysuje przedmiot na ekranie. |
| `setId(uint32 id)` | Ustawia ID klienta przedmiotu. |
| `setOtbId(uint16 id)` | Ustawia ID serwera (OTB) przedmiotu. |
| `setCountOrSubType(int value)` | Ustawia liczbÄ™ (dla przedmiotĂłw stackowalnych) lub podtyp (dla pÄąâ€šynĂłw, etc.). |
| `getCount()` | Zwraca liczbÄ™ przedmiotĂłw. |
| `getSubType()` | Zwraca podtyp przedmiotu. |
| `getServerId()` | Zwraca ID serwera. |
| `unserializeItem(...)` | Wczytuje atrybuty przedmiotu z formatu binarnego. |
| `serializeItem(...)` | Zapisuje atrybuty przedmiotu do formatu binarnego. |
| `isContainer()` | Zwraca `true`, jeÄąâ€şli przedmiot jest kontenerem. |
| `clone()` | Tworzy gÄąâ€šÄ™bokÄ… kopiÄ™ przedmiotu. |
| `getContainerItems()` | Zwraca listÄ™ przedmiotĂłw wewnÄ…trz, jeÄąâ€şli jest kontenerem. |
| `setCustomAttribute(...)` | Ustawia niestandardowy atrybut przedmiotu (funkcja dla serwerĂłw niestandardowych). |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thing.h`**: Klasa bazowa.
- **`itemtype.h`**: KaÄąÄ˝dy `Item` jest instancjÄ… jakiegoÄąâ€ş `ItemType`.

---
# Ä‘Ĺşâ€śâ€ž itemtype.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `ItemType`, ktĂłra reprezentuje szablon (typ) przedmiotu.
## Klasa `ItemType`
## Opis
Przechowuje niezmienne wÄąâ€šaÄąâ€şciwoÄąâ€şci dla danego typu przedmiotu, wczytywane z plikĂłw OTB. Wszystkie instancje `Item` o tym samym ID dzielÄ… jeden obiekt `ItemType`.
## Typy wyliczeniowe
- **`ItemCategory`**: Kategorie przedmiotĂłw (broÄąâ€ž, zbroja, pojemnik itp.).
- **`ItemTypeAttr`**: Atrybuty typu przedmiotu wczytywane z OTB.
- **`ClientVersion`**: Wersje klienta, uÄąÄ˝ywane do obsÄąâ€šugi rĂłÄąÄ˝nic w formatach plikĂłw.
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(const BinaryTreePtr& node)` | Wczytuje dane typu przedmiotu z binarnego formatu OTB. |
| `setServerId(uint16 serverId)` | Ustawia ID serwera. |
| `getServerId()` | Zwraca ID serwera. |
| `setClientId(uint16 clientId)` | Ustawia ID klienta. |
| `getClientId()` | Zwraca ID klienta. |
| `getCategory()` | Zwraca kategoriÄ™ przedmiotu. |
| `getName()` | Zwraca nazwÄ™ przedmiotu. |
| `isWritable()` | Zwraca `true`, jeÄąâ€şli na przedmiocie moÄąÄ˝na pisaÄ‡. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/luaengine/luaobject.h`**: Dziedziczy z `LuaObject`, aby byÄ‡ dostÄ™pnym z Lua.
- **`framework/xml/tinyxml.h`**: UÄąÄ˝ywane do parsowania dodatkowych danych z `items.xml`.

---
# Ä‘Ĺşâ€śâ€ž lightview.cpp
## OgĂłlny opis
Implementacja klasy `LightView`, ktĂłra zarzÄ…dza i renderuje dynamiczne oÄąâ€şwietlenie na mapie.
## Klasa `LightView`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addLight(const Point& pos, uint8_t color, uint8_t intensity)` | Dodaje nowe ÄąĹźrĂłdÄąâ€šo Äąâ€şwiatÄąâ€ša do sceny. JeÄąâ€şli w tym samym miejscu istnieje juÄąÄ˝ Äąâ€şwiatÄąâ€šo o tym samym kolorze, wybierana jest wiÄ™ksza intensywnoÄąâ€şÄ‡. |
| `setFieldBrightness(...)` | Ustawia jasnoÄąâ€şÄ‡ dla danego pola na mapie. Ta metoda nie jest w peÄąâ€šni zaimplementowana i jej rola wydaje siÄ™ ograniczona. |
| `draw()` | GÄąâ€šĂłwna funkcja renderujÄ…ca. Przebiega przez wszystkie pola widoczne na ekranie i dla kaÄąÄ˝dego piksela oblicza finalny kolor Äąâ€şwiatÄąâ€ša, sumujÄ…c wpÄąâ€šyw globalnego oÄąâ€şwietlenia i wszystkich pobliskich ÄąĹźrĂłdeÄąâ€š Äąâ€şwiatÄąâ€ša. Wynik jest zapisywany do bufora, a nastÄ™pnie przesyÄąâ€šany do tekstury (`m_lightTexture`), ktĂłra jest rysowana na ekranie z trybem mieszania `CompositionMode_Multiply`, aby przyciemniÄ‡ scenÄ™. |
## Logika renderowania
1.  Tworzony jest bufor pikseli o rozmiarze widocznego obszaru mapy.
2.  KaÄąÄ˝dy piksel w buforze jest inicjalizowany globalnym Äąâ€şwiatÄąâ€šem otoczenia.
3.  Dla kaÄąÄ˝dego piksela iteruje siÄ™ przez wszystkie ÄąĹźrĂłdÄąâ€ša Äąâ€şwiatÄąâ€ša.
4.  Obliczana jest odlegÄąâ€šoÄąâ€şÄ‡ piksela od ÄąĹźrĂłdÄąâ€ša Äąâ€şwiatÄąâ€ša, a na jej podstawie intensywnoÄąâ€şÄ‡ Äąâ€şwiatÄąâ€ša w tym punkcie.
5.  Kolor Äąâ€şwiatÄąâ€ša jest mieszany z kolorem piksela w buforze (wybierany jest najjaÄąâ€şniejszy kanaÄąâ€š R, G, B).
6.  Po przetworzeniu wszystkich pikseli, bufor jest Äąâ€šadowany do tekstury.
7.  Tekstura Äąâ€şwiatÄąâ€ša jest rysowana na wierzchu sceny, przyciemniajÄ…c jÄ….
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`spritemanager.h`**: UÄąÄ˝ywa `g_sprites.spriteSize()` do obliczeÄąâ€ž zwiÄ…zanych z rozmiarami pĂłl.
- **`framework/graphics/painter.h`**: UÄąÄ˝ywa `g_painter` do rysowania finalnej tekstury Äąâ€şwiatÄąâ€ša.

---
# Ä‘Ĺşâ€śâ€ž lightview.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `LightView`, ktĂłra jest odpowiedzialna za system dynamicznego oÄąâ€şwietlenia w grze.
## Struktura `TileLight`
## Opis
Prosta struktura przechowujÄ…ca informacje o Äąâ€şwietle dla pojedynczego pola mapy.
- `start`: Indeks poczÄ…tkowy w liÄąâ€şcie Äąâ€şwiateÄąâ€š, od ktĂłrego naleÄąÄ˝y zaczÄ…Ä‡ obliczenia dla tego pola.
- `color`: Kolor Äąâ€şwiatÄąâ€ša.
## Klasa `LightView`
## Opis
Dziedziczy po `DrawQueueItem`, co oznacza, ÄąÄ˝e obiekty tej klasy mogÄ… byÄ‡ dodawane do kolejki rysowania. `LightView` agreguje wszystkie ÄąĹźrĂłdÄąâ€ša Äąâ€şwiatÄąâ€ša w widocznym obszarze i renderuje je do jednej tekstury, ktĂłra nastÄ™pnie jest nakÄąâ€šadana na scenÄ™.
## Metody
| Nazwa | Opis |
| --- | --- |
| `LightView(...)` | Konstruktor. Inicjalizuje widok Äąâ€şwiatÄąâ€ša z podanym rozmiarem, teksturÄ… docelowÄ…, globalnym kolorem i intensywnoÄąâ€şciÄ… Äąâ€şwiatÄąâ€ša. |
| `addLight(...)` | Dodaje ÄąĹźrĂłdÄąâ€šo Äąâ€şwiatÄąâ€ša w danej pozycji. |
| `setFieldBrightness(...)` | Ustawia jasnoÄąâ€şÄ‡ dla danego pola (obecnie nie w peÄąâ€šni wykorzystywane). |
| `size()` | Zwraca liczbÄ™ ÄąĹźrĂłdeÄąâ€š Äąâ€şwiatÄąâ€ša. |
| `draw()` | Metoda renderujÄ…ca, ktĂłra wykonuje obliczenia oÄąâ€şwietlenia i rysuje finalnÄ… teksturÄ™. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`thingtype.h`**: UÄąÄ˝ywa struktury `Light` zdefiniowanej w `thingtype.h`.
- **`framework/graphics/drawqueue.h`**: Jest elementem kolejki rysowania.

---
# Ä‘Ĺşâ€śâ€ž localplayer.cpp
## OgĂłlny opis
Implementacja klasy `LocalPlayer`, ktĂłra reprezentuje postaÄ‡ sterowanÄ… przez gracza. Rozszerza klasÄ™ `Player` o logikÄ™ specyficznÄ… dla lokalnego gracza, takÄ… jak obsÄąâ€šuga ruchu inicjowanego przez klienta (pre-walking), blokady chodzenia, auto-walking oraz zarzÄ…dzanie statystykami.
## Klasa `LocalPlayer`
## Metody
| Nazwa | Opis |
| --- | --- |
| `lockWalk(int millis)` | Blokuje moÄąÄ˝liwoÄąâ€şÄ‡ chodzenia na okreÄąâ€şlony czas, np. po uÄąÄ˝yciu przedmiotu. |
| `canWalk(Otc::Direction direction, ...)` | Sprawdza, czy gracz moÄąÄ˝e wykonaÄ‡ krok w danym kierunku. UwzglÄ™dnia blokady, paraliÄąÄ˝, trwajÄ…cy ruch oraz limity "pre-walkingu". |
| `walk(const Position& oldPos, const Position& newPos)` | ObsÄąâ€šuguje ruch potwierdzony przez serwer. JeÄąâ€şli ruch odpowiada wykonanemu "pre-walk", usuwa go z kolejki. JeÄąâ€şli nie, traktuje to jako ruch wymuszony przez serwer (np. odepchniÄ™cie). |
| `preWalk(Otc::Direction direction)` | Inicjuje "pre-walking" â€“ ruch wykonywany przez klienta przed potwierdzeniem z serwera, aby zniwelowaÄ‡ opĂłÄąĹźnienie sieciowe. Dodaje nowÄ… pozycjÄ™ do kolejki `m_preWalking`. |
| `cancelNewWalk(Otc::Direction dir)` | Anuluje wszystkie ruchy "pre-walk" w odpowiedzi na pakiet "cancel walk" z serwera. MoÄąÄ˝e prĂłbowaÄ‡ ponowiÄ‡ auto-walking. |
| `predictiveCancelWalk(...)` | Anuluje ruchy "pre-walk" na podstawie predykcji, jeÄąâ€şli serwer odrzuci krok w poÄąâ€šowie Äąâ€şcieÄąÄ˝ki. |
| `autoWalk(Position destination, ...)` | Inicjuje automatyczne poruszanie siÄ™ do celu. Asynchronicznie wyszukuje Äąâ€şcieÄąÄ˝kÄ™ i wysyÄąâ€ša jÄ… do serwera. |
| `stopAutoWalk()` | Przerywa auto-walking. |
| `stopWalk()` | Natychmiastowo zatrzymuje wszelki ruch, czyszczÄ…c kolejkÄ™ "pre-walk". |
| `updateWalkOffset(...)` | Specjalna implementacja dla "pre-walk", gdzie offset jest liczony w przeciwnym kierunku niÄąÄ˝ normalny ruch. |
| `updateWalk()` | Aktualizuje stan chodzenia; koÄąâ€žczy krok, gdy upÄąâ€šynie jego czas trwania. |
| `terminateWalk()` | Finalizuje krok, resetuje stan chodzenia i wywoÄąâ€šuje callback `onWalkFinish`. |
| `onPositionChange(...)` | ObsÄąâ€šuguje zmianÄ™ pozycji; jeÄąâ€şli osiÄ…gniÄ™to cel auto-walk, zatrzymuje go. |
| `set...(...)` | Szereg metod `set` (np. `setHealth`, `setSkill`, `setExperience`), ktĂłre aktualizujÄ… stan lokalnego gracza i wywoÄąâ€šujÄ… odpowiednie callbacki Lua, informujÄ…c o zmianach. |
| `hasSight(const Position& pos)` | Sprawdza, czy dana pozycja jest w zasiÄ™gu wzroku gracza. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**, **`tile.h`**: Do sprawdzania, czy pola sÄ… moÄąÄ˝liwe do przejÄąâ€şcia.
- **`game.h`**: Do komunikacji z serwerem i zatrzymywania akcji gry.
- **`framework/core/eventdispatcher.h`**: Do planowania ponownych prĂłb auto-walkingu.

---
# Ä‘Ĺşâ€śâ€ž map.cpp
## OgĂłlny opis
Implementacja klasy `Map`, ktĂłra jest centralnym repozytorium dla wszystkich danych o Äąâ€şwiecie gry. Plik zawiera logikÄ™ zarzÄ…dzania polami (`Tile`), umieszczania na nich obiektĂłw (`Thing`), wyszukiwania Äąâ€şcieÄąÄ˝ek oraz zarzÄ…dzania widocznym obszarem mapy.
## Klasa `Map`
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizuje i zwalnia zasoby mapy. |
| `addMapView(...)` / `removeMapView(...)` | Dodaje i usuwa widoki mapy (`MapView`), ktĂłre bÄ™dÄ… renderowaÄ‡ dane. |
| `notificateTileUpdate(...)` | Powiadamia wszystkie `MapView` o aktualizacji danego pola, co powoduje jego przerysowanie. |
| `clean()` / `cleanDynamicThings()` | CzyÄąâ€şci mapÄ™ ze wszystkich pĂłl lub tylko z obiektĂłw dynamicznych (stworzenia, efekty). |
| `addThing(...)` | Dodaje obiekt (`Thing`) na mapÄ™ w danej pozycji. ObsÄąâ€šuguje specjalne przypadki dla pociskĂłw, animowanych i statycznych tekstĂłw (np. Äąâ€šÄ…czenie tekstĂłw o obraÄąÄ˝eniach). |
| `getThing(...)` / `removeThing(...)` | Pobiera lub usuwa obiekt z mapy. |
| `getOrCreateTile(...)` | Zwraca istniejÄ…ce pole lub tworzy nowe, jeÄąâ€şli nie istnieje. |
| `getTiles(...)` | Zwraca listÄ™ wszystkich pĂłl na danym piÄ™trze lub na caÄąâ€šej mapie. |
| `cleanTile(...)` | Usuwa wszystkie obiekty z danego pola. |
| `setCentralPosition(...)` | Ustawia pozycjÄ™ kamery, co powoduje usuniÄ™cie obiektĂłw spoza nowego zasiÄ™gu widzenia. |
| `getSpectators(...)` | Zwraca listÄ™ stworzeÄąâ€ž w zasiÄ™gu widzenia. |
| `isAwareOfPosition(...)` | Sprawdza, czy dana pozycja jest w zasiÄ™gu widzenia kamery. |
| `findPath(...)` | Implementacja algorytmu wyszukiwania Äąâ€şcieÄąÄ˝ki A*. |
| `newFindPath(...)` | Nowsza, asynchroniczna implementacja wyszukiwania Äąâ€şcieÄąÄ˝ki. |
| `findPathAsync(...)` | Uruchamia `newFindPath` w osobnym wÄ…tku. |
| `findEveryPath(...)` | Implementacja algorytmu Dijkstry do znalezienia wszystkich moÄąÄ˝liwych Äąâ€şcieÄąÄ˝ek w danym zasiÄ™gu. |
## Struktura danych
- **`m_tileBlocks`**: Pola mapy sÄ… przechowywane w blokach 32x32, co optymalizuje zuÄąÄ˝ycie pamiÄ™ci. `std::map<uint, TileBlock> m_tileBlocks[Otc::MAX_Z+1]` przechowuje te bloki dla kaÄąÄ˝dego piÄ™tra.
- **`m_knownCreatures`**: Mapa znanych stworzeÄąâ€ž, indeksowana po ich ID.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**: DostÄ™p do stanu gry, np. funkcji serwera (`GameFeature`).
- **`localplayer.h`**: Do centrowania kamery i aktualizacji pozycji gracza.
- **`tile.h`**: ZarzÄ…dza obiektami `Tile`.
- **`mapview.h`**: Powiadamia `MapView` o zmianach.
- **`minimap.h`**: Aktualizuje minimapÄ™ przy zmianach na polach.

---
# Ä‘Ĺşâ€śâ€ž luavaluecasts_client.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy funkcje do konwersji (rzutowania) niestandardowych typĂłw danych C++ na wartoÄąâ€şci Lua i z powrotem. Jest to kluczowy element integracji logiki gry z silnikiem skryptowym Lua.
## Funkcje
| Nazwa | Opis |
| --- | --- |
| `push_luavalue(const Outfit& outfit)` | Konwertuje obiekt `Outfit` na tabelÄ™ Lua i umieszcza jÄ… na stosie. |
| `luavalue_cast(int index, Outfit& outfit)` | Odczytuje tabelÄ™ Lua ze stosu i konwertuje jÄ… na obiekt `Outfit`. |
| `push_luavalue(const Position& pos)` | Konwertuje obiekt `Position` na tabelÄ™ Lua (`{x=, y=, z=}`). |
| `luavalue_cast(int index, Position& pos)` | Odczytuje tabelÄ™ Lua i konwertuje jÄ… na obiekt `Position`. |
| `push_luavalue(const MarketData& data)` | Konwertuje strukturÄ™ `MarketData` na tabelÄ™ Lua. |
| `luavalue_cast(int index, MarketData& data)` | Odczytuje tabelÄ™ Lua i konwertuje jÄ… na `MarketData`. |
| `push_luavalue(const StoreCategory& category)` | Konwertuje `StoreCategory` na tabelÄ™ Lua. |
| `luavalue_cast(int index, StoreCategory& data)` | Konwertuje tabelÄ™ Lua na `StoreCategory`. |
| `push_luavalue(const StoreOffer& offer)` | Konwertuje `StoreOffer` na tabelÄ™ Lua. |
| `luavalue_cast(int index, StoreOffer& offer)` | Konwertuje tabelÄ™ Lua na `StoreOffer`. |
| `push_luavalue(const Imbuement& offer)` | Konwertuje `Imbuement` na tabelÄ™ Lua. |
| `push_luavalue(const Light& light)` | Konwertuje `Light` na tabelÄ™ Lua. |
| `luavalue_cast(int index, Light& light)` | Konwertuje tabelÄ™ Lua na `Light`. |
| `push_luavalue(const UnjustifiedPoints& unjustifiedPoints)` | Konwertuje `UnjustifiedPoints` na tabelÄ™ Lua. |
| `luavalue_cast(int index, UnjustifiedPoints& unjustifiedPoints)` | Konwertuje tabelÄ™ Lua na `UnjustifiedPoints`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`global.h`**, **`game.h`**, **`outfit.h`**: ZawierajÄ… definicje typĂłw, ktĂłre sÄ… konwertowane.
- **`framework/luaengine/declarations.h`**: Deklaracje funkcji z silnika Lua.
- **`luavaluecasts_client.cpp`**: Zawiera implementacje tych funkcji.

---
# Ä‘Ĺşâ€śâ€ž mapio.cpp
## OgĂłlny opis
Plik ten zawiera implementacjÄ™ metod klasy `Map` odpowiedzialnych za operacje wejÄąâ€şcia/wyjÄąâ€şcia, czyli wczytywanie i zapisywanie danych mapy w formatach OTBM (OpenTibia Binary Map) i OTCM (OTClient Map).
## Klasa `Map`
## Metody
| Nazwa | Opis |
| --- | --- |
| `loadOtbm(const std::string& fileName)` | Wczytuje mapÄ™ z pliku binarnego `.otbm`. Parsuje nagÄąâ€šĂłwek, sprawdza wersjÄ™ i sygnaturÄ™, a nastÄ™pnie iteruje przez wÄ™zÄąâ€šy binarnego drzewa, tworzÄ…c pola (`Tile`), przedmioty (`Item`) oraz wczytujÄ…c informacje o miastach, domach i punktach nawigacyjnych (waypoints). |
| `saveOtbm(const std::string& fileName)` | Zapisuje aktualny stan mapy do pliku `.otbm`. Tworzy strukturÄ™ binarnego drzewa, zapisuje nagÄąâ€šĂłwek, a nastÄ™pnie serializuje wszystkie pola, przedmioty na nich, a takÄąÄ˝e informacje o miastach, domach i waypointach. |
| `loadOtcm(const std::string& fileName)` | Wczytuje mapÄ™ z wÄąâ€šasnego, prostszego formatu klienta (`.otcm`). Format ten jest mniej rozbudowany niÄąÄ˝ OTBM i przechowuje gÄąâ€šĂłwnie informacje o polach i przedmiotach. |
| `saveOtcm(const std::string& fileName)` | Zapisuje mapÄ™ do formatu `.otcm`. |
## Logika wczytywania OTBM
1.  Otwiera plik i weryfikuje jego sygnaturÄ™ (`OTBM`).
2.  Odczytuje nagÄąâ€šĂłwek, zawierajÄ…cy wymiary mapy i wersje OTB.
3.  Parsuje gÄąâ€šĂłwny wÄ™zeÄąâ€š danych, odczytujÄ…c atrybuty takie jak opis mapy oraz Äąâ€şcieÄąÄ˝ki do plikĂłw z danymi o spawnach i domach.
4.  Iteruje przez wÄ™zÄąâ€šy `OTBM_TILE_AREA`, ktĂłre grupujÄ… pola w blokach.
5.  Dla kaÄąÄ˝dego pola (`OTBM_TILE`) odczytuje jego atrybuty (flagi, przedmioty). Przedmioty, ktĂłre sÄ… kontenerami, sÄ… parsowane rekurencyjnie.
6.  Wczytuje definicje miast (`OTBM_TOWNS`) i waypointĂłw (`OTBM_WAYPOINTS`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`tile.h`**, **`item.h`**: Tworzy obiekty `Tile` i `Item` na podstawie wczytanych danych.
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania funkcji serwera, ktĂłre mogÄ… wpÄąâ€šywaÄ‡ na sposĂłb parsowania.
- **`houses.h`**, **`towns.h`**: WypeÄąâ€šnia menedÄąÄ˝ery `g_houses` i `g_towns` danymi z mapy.
- **`framework/core/filestream.h`**, **`framework/core/binarytree.h`**: NarzÄ™dzia do obsÄąâ€šugi plikĂłw binarnych i struktury drzewa binarnego.

---
# Ä‘Ĺşâ€śâ€ž luavaluecasts_client.cpp
## OgĂłlny opis
Implementacja funkcji do konwersji (rzutowania) niestandardowych typĂłw danych C++ na wartoÄąâ€şci Lua i z powrotem. Ten plik zawiera logikÄ™ "tÄąâ€šumaczenia" zÄąâ€šoÄąÄ˝onych obiektĂłw C++ na tabele Lua i odwrotnie.
## Funkcje
## `push_luavalue`
Te funkcje przyjmujÄ… jako argument obiekt C++ i umieszczajÄ… jego reprezentacjÄ™ w Lua na stosie. ZÄąâ€šoÄąÄ˝one obiekty sÄ… zazwyczaj konwertowane na tabele Lua.
- **`push_luavalue(const Outfit& outfit)`**: Tworzy tabelÄ™ Lua z polami `type`, `auxType`, `head`, `body`, `legs`, `feet`, `addons`, `mount` etc. i wypeÄąâ€šnia jÄ… danymi z obiektu `Outfit`.
- **`push_luavalue(const Position& pos)`**: Tworzy tabelÄ™ `{x, y, z}`.
- **`push_luavalue(const MarketData& data)`**: Tworzy tabelÄ™ z danymi rynkowymi.
- **`push_luavalue(const Imbuement& i)`**: Tworzy zÄąâ€šoÄąÄ˝onÄ…, zagnieÄąÄ˝dÄąÄ˝onÄ… tabelÄ™ reprezentujÄ…cÄ… imbuement, wÄąâ€šÄ…czajÄ…c w to listÄ™ materiaÄąâ€šĂłw.
## `luavalue_cast`
Te funkcje przyjmujÄ… jako argument indeks na stosie Lua i referencjÄ™ do obiektu C++. OdczytujÄ… wartoÄąâ€şÄ‡ ze stosu (zwykle tabelÄ™) i wypeÄąâ€šniajÄ… obiekt C++ odpowiednimi danymi.
- **`luavalue_cast(int index, Outfit& outfit)`**: Odczytuje pola z tabeli Lua i ustawia odpowiednie wÄąâ€šaÄąâ€şciwoÄąâ€şci w obiekcie `Outfit`.
- **`luavalue_cast(int index, Position& pos)`**: Odczytuje pola `x`, `y`, `z` z tabeli.
- **`luavalue_cast(int index, MarketData& data)`**: WypeÄąâ€šnia strukturÄ™ `MarketData`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/luaengine/luainterface.h`**: DostÄ™p do funkcji `g_lua` do manipulacji stosem Lua.
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania, ktĂłre `GameFeature` sÄ… aktywne, co wpÄąâ€šywa na to, ktĂłre pola obiektu `Outfit` sÄ… serializowane/deserializowane (np. `GamePlayerMounts`).
- **`luavaluecasts_client.h`**: Deklaracje tych funkcji.

---
# Ä‘Ĺşâ€śâ€ž mapview.cpp
## OgĂłlny opis
Implementacja klasy `MapView`, ktĂłra jest odpowiedzialna za renderowanie widoku mapy. Plik zawiera skomplikowanÄ… logikÄ™ okreÄąâ€şlania, ktĂłre pola sÄ… widoczne, jak je rysowaÄ‡ w odpowiedniej kolejnoÄąâ€şci (z uwzglÄ™dnieniem piÄ™ter i efektu paralaksy) oraz jak zarzÄ…dzaÄ‡ oÄąâ€şwietleniem i tekstami na mapie.
## Klasa `MapView`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawMapBackground(...)` | GÄąâ€šĂłwna funkcja rysujÄ…ca tÄąâ€šo mapy. Przygotowuje bufor ramki (`FrameBuffer`), inicjalizuje `LightView` (jeÄąâ€şli oÄąâ€şwietlenie jest wÄąâ€šÄ…czone) i rysuje wszystkie widoczne piÄ™tra, zaczynajÄ…c od najniÄąÄ˝szego. |
| `drawFloor(...)` | Rysuje pojedyncze piÄ™tro. Iteruje po `m_cachedVisibleTiles` i wywoÄąâ€šuje metody `drawGround`, `drawBottom`, `drawCreatures` i `drawTop` dla kaÄąÄ˝dego pola (`Tile`). |
| `drawMapForeground(...)` | Rysuje elementy pierwszego planu, takie jak paski zdrowia, nazwy postaci, teksty (statyczne i animowane) oraz ostatecznie nakÄąâ€šada warstwÄ™ oÄąâ€şwietlenia. |
| `updateVisibleTilesCache()` | Kluczowa metoda optymalizacyjna. Oblicza, ktĂłre pola sÄ… widoczne dla kamery, i zapisuje je w pamiÄ™ci podrÄ™cznej (`m_cachedVisibleTiles`). Sortuje je w kolejnoÄąâ€şci rysowania (diagonalnie), aby zachowaÄ‡ poprawnÄ… perspektywÄ™ 2.5D. |
| `updateGeometry(...)` | Aktualizuje geometriÄ™ widoku, w tym wymiary widoczne i wymiary bufora ramki. |
| `onTileUpdate(...)` / `onMapCenterChange(...)` | Metody wywoÄąâ€šywane przez `g_map`, ktĂłre oznaczajÄ…, ÄąÄ˝e pamiÄ™Ä‡ podrÄ™czna widocznych pĂłl musi zostaÄ‡ zaktualizowana. |
| `calcFirstVisibleFloor(...)` / `calcLastVisibleFloor(...)` | Oblicza, ktĂłre piÄ™tra sÄ… widoczne dla gracza na podstawie jego pozycji i otoczenia (np. dziury w podÄąâ€šodze, okna). |
| `transformPositionTo2D(...)` | Konwertuje pozycjÄ™ 3D (x, y, z) na wspĂłÄąâ€šrzÄ™dne 2D na ekranie, uwzglÄ™dniajÄ…c perspektywÄ™ izometrycznÄ…. |
| `getCameraPosition()` | Zwraca aktualnÄ… pozycjÄ™ kamery, ktĂłra albo podÄ…ÄąÄ˝a za stworzeniem (`m_followingCreature`), albo jest ustawiona rÄ™cznie. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**, **`tile.h`**: Intensywnie korzysta z `g_map` do pobierania danych o polach i obiektach.
- **`game.h`**: DostÄ™p do `g_game` w celu pobrania lokalnego gracza i sprawdzenia funkcji serwera.
- **`lightview.h`**: Tworzy i zarzÄ…dza obiektem `LightView` do renderowania oÄąâ€şwietlenia.
- **`framework/graphics/framebuffermanager.h`**: UÄąÄ˝ywa buforĂłw ramki do optymalizacji renderowania.

---
# Ä‘Ĺşâ€śâ€ž mapview.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `MapView`. Definiuje interfejs widoku mapy, ktĂłry jest gÄąâ€šĂłwnym komponentem renderujÄ…cym Äąâ€şwiat gry.
## Klasa `MapView`
## Opis
Klasa `MapView` zarzÄ…dza kamerÄ…, widocznym obszarem mapy, a takÄąÄ˝e koordynuje proces rysowania wszystkich elementĂłw Äąâ€şwiata gry. MoÄąÄ˝e istnieÄ‡ wiele instancji `MapView`, co pozwala na renderowanie mapy w rĂłÄąÄ˝nych miejscach interfejsu.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawMapBackground(...)` | Rysuje tÄąâ€šo mapy (pola, obiekty na ziemi). |
| `drawMapForeground(...)` | Rysuje pierwszy plan (postacie, teksty, oÄąâ€şwietlenie). |
| `lockFirstVisibleFloor(int floor)` | Wymusza, aby najniÄąÄ˝szym widocznym piÄ™trem byÄąâ€šo podane piÄ™tro. |
| `unlockFirstVisibleFloor()` | WyÄąâ€šÄ…cza wymuszone piÄ™tro. |
| `setVisibleDimension(const Size& dim)` | Ustawia wymiary widocznego obszaru w jednostkach pĂłl (np. 15x11). |
| `followCreature(const CreaturePtr& creature)` | Ustawia kamerÄ™, aby podÄ…ÄąÄ˝aÄąâ€ša za danym stworzeniem. |
| `setCameraPosition(const Position& pos)` | Ustawia kamerÄ™ na staÄąâ€šÄ… pozycjÄ™. |
| `getCameraPosition()` | Zwraca aktualnÄ… pozycjÄ™ kamery. |
| `getPosition(const Point& point, ...)` | Konwertuje wspĂłÄąâ€šrzÄ™dne ekranu na pozycjÄ™ na mapie. |
| `setDrawFlags(Otc::DrawFlags flags)` | Ustawia flagi rysowania, okreÄąâ€şlajÄ…ce, co ma byÄ‡ renderowane. |
| `setAnimated(bool animated)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza animacje. |
| `setFloorFading(int value)` | Ustawia czas zanikania/pojawiania siÄ™ piÄ™ter. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw (`Position`, `CreaturePtr`).
- **`lightview.h`**: UÄąÄ˝ywa `LightView` do rysowania Äąâ€şwiateÄąâ€š.
- **`framework/luaengine/luaobject.h`**: Dziedziczy z `LuaObject`.

---
# Ä‘Ĺşâ€śâ€ž minimap.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `Minimap` i powiÄ…zanych struktur. Definiuje interfejs do zarzÄ…dzania danymi minimapy i jej renderowania.
## Struktury i staÄąâ€še
- **`MMBLOCK_SIZE`**: Rozmiar bloku minimapy (64x64 piksele).
- **`MinimapTileFlags`**: Flagi dla kafelka minimapy (np. `MinimapTileWasSeen`, `MinimapTileNotPathable`).
- **`MinimapTile`**: Struktura przechowujÄ…ca dane pojedynczego piksela minimapy (kolor, flagi, prÄ™dkoÄąâ€şÄ‡).
## Klasa `MinimapBlock`
## Opis
Reprezentuje pojedynczy blok (chunk) minimapy o rozmiarze `MMBLOCK_SIZE` x `MMBLOCK_SIZE`. KaÄąÄ˝dy blok ma wÄąâ€šasnÄ… teksturÄ™, co optymalizuje renderowanie.
- `m_texture`: Tekstura generowana na podstawie danych z `m_tiles`.
- `m_tiles`: Tablica `MinimapTile` przechowujÄ…ca dane dla kaÄąÄ˝dego piksela w bloku.
- `m_mustUpdate`: Flaga informujÄ…ca, czy tekstura wymaga ponownego wygenerowania.
## Klasa `Minimap`
## Opis
Singleton (`g_minimap`) zarzÄ…dzajÄ…cy wszystkimi danymi minimapy. Przechowuje `MinimapBlock` dla kaÄąÄ˝dego piÄ™tra i koordynuje ich rysowanie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizacja i zamykanie managera. |
| `clean()` | CzyÄąâ€şci wszystkie dane minimapy. |
| `draw(...)` | Rysuje minimapÄ™ na ekranie w danym prostokÄ…cie. |
| `getTilePoint(const Position& pos, ...)` | Konwertuje pozycjÄ™ na mapie na wspĂłÄąâ€šrzÄ™dne na widÄąÄ˝ecie minimapy. |
| `getTilePosition(const Point& point, ...)` | Konwertuje wspĂłÄąâ€šrzÄ™dne na widÄąÄ˝ecie minimapy na pozycjÄ™ na mapie. |
| `updateTile(const Position& pos, const TilePtr& tile)` | Aktualizuje dane piksela minimapy na podstawie danych z `Tile`. |
| `getTile(const Position& pos)` | Zwraca dane `MinimapTile` dla danej pozycji. |
| `loadImage(...)` | Wczytuje dane minimapy z pliku graficznego (np. PNG). |
| `saveImage(...)` | Zapisuje widoczny obszar minimapy do pliku graficznego. |
| `loadOtmm(...)` / `saveOtmm(...)` | Wczytuje/zapisuje dane minimapy w formacie `.otmm`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`tile.h`**: `updateTile` pobiera dane z obiektu `Tile`.

---
# Ä‘Ĺşâ€śâ€ž missile.cpp
## OgĂłlny opis
Implementacja klasy `Missile`, ktĂłra odpowiada za renderowanie pociskĂłw w grze.
## Klasa `Missile`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje pocisk na ekranie. Oblicza jego pozycjÄ™ na Äąâ€şcieÄąÄ˝ce lotu na podstawie czasu, ktĂłry upÄąâ€šynÄ…Äąâ€š (`m_animationTimer.ticksElapsed() / m_duration`). Wybiera odpowiedni wzĂłr (pattern) sprite'a na podstawie kierunku lotu. |
| `setPath(const Position& fromPosition, const Position& toPosition)` | Ustawia Äąâ€şcieÄąÄ˝kÄ™ lotu pocisku od pozycji poczÄ…tkowej do koÄąâ€žcowej. Oblicza kierunek, czas trwania lotu i planuje automatyczne usuniÄ™cie pocisku po dotarciu do celu. |
| `setId(uint32 id)` | Ustawia ID (typ) pocisku, weryfikujÄ…c jego poprawnoÄąâ€şÄ‡. |
| `getThingType()` / `rawGetThingType()` | ZwracajÄ… `ThingType` dla danego pocisku. |
## Logika animacji
Pozycja pocisku jest interpolowana liniowo miÄ™dzy punktem startowym a koÄąâ€žcowym. Frakcja postÄ™pu `fraction` jest obliczana jako stosunek czasu, ktĂłry upÄąâ€šynÄ…Äąâ€š, do caÄąâ€škowitego czasu trwania lotu. PrzesuniÄ™cie rysowania `m_delta * fraction` jest dodawane do pozycji poczÄ…tkowej.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**: UÄąÄ˝ywa `g_map` do usuniÄ™cia pocisku po zakoÄąâ€žczeniu lotu.
- **`spritemanager.h`**: UÄąÄ˝ywa `g_sprites.spriteSize()` do skalowania przesuniÄ™cia.
- **`framework/core/eventdispatcher.h`**: UÄąÄ˝ywa `g_dispatcher` do planowania usuniÄ™cia.

---
# Ä‘Ĺşâ€śâ€ž missile.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Missile`, ktĂłra reprezentuje pociski i inne efekty dystansowe.
## Klasa `Missile`
## Opis
Dziedziczy po `Thing`. Reprezentuje obiekt, ktĂłry przemieszcza siÄ™ od jednej pozycji do drugiej w okreÄąâ€şlonym czasie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje pocisk w jego aktualnej pozycji na Äąâ€şcieÄąÄ˝ce. |
| `setId(uint32 id)` | Ustawia ID (typ) pocisku. |
| `setPath(const Position& from, const Position& to)` | Ustawia poczÄ…tek i koniec Äąâ€şcieÄąÄ˝ki pocisku. |
| `getId()` | Zwraca ID pocisku. |
| `asMissile()` | Rzutuje wskaÄąĹźnik na `MissilePtr`. |
| `isMissile()` | Zwraca `true`. |
| `getThingType()` | Zwraca `ThingType` dla pocisku. |
| `getSource()` | Zwraca pozycjÄ™ poczÄ…tkowÄ…. |
| `getDestination()` | Zwraca pozycjÄ™ koÄąâ€žcowÄ…. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thing.h`**: Klasa bazowa.
- **`framework/core/timer.h`**: UÄąÄ˝ywa `Timer` do animacji ruchu.

---
# Ä‘Ĺşâ€śâ€ž outfit.cpp
## OgĂłlny opis
Implementacja klasy `Outfit` oraz niestandardowych elementĂłw kolejki rysowania `DrawQueueItemOutfit` i `DrawQueueItemOutfitWithShader`. Plik zawiera zÄąâ€šoÄąÄ˝onÄ… logikÄ™ rysowania ubioru postaci, w tym warstw, kolorĂłw, dodatkĂłw, wierzchowcĂłw, skrzydeÄąâ€š, aury i shaderĂłw.
## Klasa `Outfit`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(Point dest, ...)` | GÄąâ€šĂłwna funkcja rysujÄ…ca ubiĂłr. Wykonuje nastÄ™pujÄ…ce kroki: <br> 1. Koryguje kierunek. <br> 2. Oblicza fazÄ™ animacji (chodzenia, bezczynnoÄąâ€şci, UI). <br> 3. Rysuje aurÄ™ (tylnÄ… warstwÄ™, jeÄąâ€şli dotyczy). <br> 4. Rysuje wierzchowca. <br> 5. Rysuje skrzydÄąâ€ša (w zaleÄąÄ˝noÄąâ€şci od kierunku, przed lub za postaciÄ…). <br> 6. Rysuje poszczegĂłlne warstwy ubioru (podstawÄ™ i dodatki), kolorujÄ…c je za pomocÄ… specjalnego shadera (`DrawQueueItemOutfit`). <br> 7. Rysuje aurÄ™ (przedniÄ… warstwÄ™). |
| `draw(const Rect& dest, ...)` | Wersja rysujÄ…ca ubiĂłr przeskalowany do danego prostokÄ…ta, uÄąÄ˝ywana w UI. |
| `resetClothes()` | Resetuje wszystkie elementy ubioru (gÄąâ€šowa, ciaÄąâ€šo, etc.) do wartoÄąâ€şci domyÄąâ€şlnych (0). |
## Klasy `DrawQueueItem...`
## Opis
Niestandardowe elementy kolejki rysowania, ktĂłre pozwalajÄ… na zaawansowane renderowanie ubiorĂłw.
- **`DrawQueueItemOutfit`**: UÄąÄ˝ywa specjalnego shadera (`outfit.frag`), ktĂłry na podstawie 32-bitowej liczby `m_colors` i tekstury z warstwami, koloruje kaÄąÄ˝dÄ… z czterech czÄ™Äąâ€şci ubioru (gÄąâ€šowa, ciaÄąâ€šo, nogi, stopy) na odpowiedni kolor.
- **`DrawQueueItemOutfitWithShader`**: Rozszerza powyÄąÄ˝szÄ… logikÄ™ o dodatkowy, niestandardowy shader (np. efekt "ghost"), ktĂłry jest nakÄąâ€šadany na finalny obraz ubioru.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**: Sprawdza, ktĂłre `GameFeature` sÄ… aktywne, aby decydowaÄ‡, ktĂłre elementy ubioru rysowaÄ‡ (np. wierzchowce, skrzydÄąâ€ša).
- **`thingtypemanager.h`**: UÄąÄ˝ywa `g_things` do pobierania `ThingType` dla ubioru, wierzchowca, skrzydeÄąâ€š, aury.
- **`spritemanager.h`**: UÄąÄ˝ywa `g_sprites` do skalowania i pozycjonowania.
- **`framework/graphics/drawqueue.h`**: Dodaje niestandardowe elementy do kolejki rysowania.
- **`framework/graphics/shadermanager.h`**: ZarzÄ…dza i uÄąÄ˝ywa shaderĂłw do kolorowania i efektĂłw.

---
# Ä‘Ĺşâ€śâ€ž outfit.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Outfit` oraz powiÄ…zanych struktur do rysowania.
## Klasa `Outfit`
## Opis
Reprezentuje wyglÄ…d (ubiĂłr) postaci. Przechowuje informacje o ID wyglÄ…du, kolorach poszczegĂłlnych czÄ™Äąâ€şci ciaÄąâ€ša, dodatkach, wierzchowcu, skrzydÄąâ€šach, aurze i niestandardowym shaderze.
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Dwie przeciÄ…ÄąÄ˝one wersje funkcji rysujÄ…cej ubiĂłr: jedna w punkcie (na mapie), druga w prostokÄ…cie (w UI). |
| `setId(int id)` | Ustawia ID ubioru (dla potworĂłw) lub przedmiotu (dla niewidzialnoÄąâ€şci). |
| `setHead(int head)` | Ustawia kolor gÄąâ€šowy. |
| `setBody(int body)` | Ustawia kolor torsu. |
| `setLegs(int legs)` | Ustawia kolor nĂłg. |
| `setFeet(int feet)` | Ustawia kolor stĂłp. |
| `setAddons(int addons)` | Ustawia dodatki (bitmaska). |
| `setMount(int mount)` | Ustawia ID wierzchowca. |
| `setWings(int wings)` | Ustawia ID skrzydeÄąâ€š. |
| `setAura(int aura)` | Ustawia ID aury. |
| `setShader(const std::string& shader)` | Ustawia nazwÄ™ niestandardowego shadera. |
## Struktury `DrawQueueItem...`
## Opis
Definicje niestandardowych elementĂłw kolejki rysowania, ktĂłre obsÄąâ€šugujÄ… zaawansowane renderowanie ubiorĂłw.
- **`DrawQueueItemOutfit`**: Renderuje ubiĂłr z dynamicznym kolorowaniem poszczegĂłlnych czÄ™Äąâ€şci.
- **`DrawQueueItemOutfitWithShader`**: Dodaje obsÄąâ€šugÄ™ niestandardowego shadera efektĂłw specjalnych.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thingtypemanager.h`**: UÄąÄ˝ywa `ThingCategory` i `ThingType`.
- **`framework/graphics/drawqueue.h`**: DziedziczÄ… z `DrawQueueItemTexturedRect`.

---
# Ä‘Ĺşâ€śâ€ž player.cpp
## OgĂłlny opis
Ten plik jest obecnie pusty, co oznacza, ÄąÄ˝e klasa `Player` nie posiada ÄąÄ˝adnej dodatkowej implementacji poza tym, co dziedziczy z klasy `Creature`.
## Klasa `Player`
## Opis
Klasa `Player` jest specjalizacjÄ… `Creature`. SÄąâ€šuÄąÄ˝y do reprezentowania postaci graczy w grze. W przyszÄąâ€šoÄąâ€şci moÄąÄ˝e zawieraÄ‡ logikÄ™ specyficznÄ… tylko dla graczy, ktĂłra nie dotyczy potworĂłw czy NPC.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`player.h`**: Plik nagÄąâ€šĂłwkowy dla tej implementacji.

---
# Ä‘Ĺşâ€śâ€ž player.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `Player`, ktĂłra jest specjalizacjÄ… klasy `Creature`.
## Klasa `Player`
## Opis
Dziedziczy po `Creature`. Reprezentuje postaÄ‡ gracza (niekoniecznie lokalnego). Nie dodaje ÄąÄ˝adnych nowych pĂłl ani metod, ale sÄąâ€šuÄąÄ˝y do rozrĂłÄąÄ˝nienia typĂłw stworzeÄąâ€ž w systemie typĂłw C++.
## Metody
| Nazwa | Opis |
| --- | --- |
| `asPlayer()` | Rzutuje wskaÄąĹźnik na `PlayerPtr`. |
| `isPlayer()` | Zwraca `true`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`creature.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž protocolcodes.cpp
## OgĂłlny opis
Implementacja funkcji pomocniczych zadeklarowanych w `protocolcodes.h`. GÄąâ€šĂłwnym zadaniem tego pliku jest zarzÄ…dzanie mapowaniem trybĂłw wiadomoÄąâ€şci (`Otc::MessageMode`) na ich liczbowe odpowiedniki uÄąÄ˝ywane w protokole sieciowym, ktĂłre mogÄ… siÄ™ rĂłÄąÄ˝niÄ‡ w zaleÄąÄ˝noÄąâ€şci od wersji klienta.
## Namespace `Proto`
## Zmienne globalne
- **`std::map<uint8, uint8> messageModesMap`**: Mapa przechowujÄ…ca powiÄ…zanie miÄ™dzy wewnÄ™trznym enumem `Otc::MessageMode` a wartoÄąâ€şciÄ… liczbowÄ… wysyÄąâ€šanÄ…/odbieranÄ… z serwera.
## Funkcje
| Nazwa | Opis |
| --- | --- |
| `buildMessageModesMap(int version)` | WypeÄąâ€šnia `messageModesMap` na podstawie podanej wersji protokoÄąâ€šu. Zawiera bloki `if/else if` dla rĂłÄąÄ˝nych zakresĂłw wersji, definiujÄ…c odpowiednie mapowania. Jest to kluczowe dla zachowania kompatybilnoÄąâ€şci wstecznej. |
| `translateMessageModeFromServer(uint8 mode)` | TÄąâ€šumaczy liczbowy tryb wiadomoÄąâ€şci otrzymany z serwera na wewnÄ™trzny enum `Otc::MessageMode`. |
| `translateMessageModeToServer(Otc::MessageMode mode)` | TÄąâ€šumaczy wewnÄ™trzny enum `Otc::MessageMode` na jego liczbowy odpowiednik, ktĂłry zostanie wysÄąâ€šany do serwera. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`protocolcodes.h`**: Deklaracje funkcji i enumĂłw.
- **`game.cpp`**: `Game::setProtocolVersion` wywoÄąâ€šuje `buildMessageModesMap`, aby zaktualizowaÄ‡ mapowania po zmianie wersji protokoÄąâ€šu.

---
# Ä‘Ĺşâ€śâ€ž minimap.cpp
## OgĂłlny opis
Implementacja `Minimap` i `MinimapBlock`, ktĂłre razem tworzÄ… system minimapy w grze. Plik zawiera logikÄ™ renderowania, aktualizacji danych, a takÄąÄ˝e wczytywania i zapisywania minimapy w formatach `.otmm` i graficznych.
## Klasa `MinimapBlock`
## Metody
| Nazwa | Opis |
| --- | --- |
| `clean()` | Resetuje wszystkie dane w bloku do stanu poczÄ…tkowego. |
| `update()` | JeÄąâ€şli blok zostaÄąâ€š zmodyfikowany (`m_mustUpdate`), generuje nowÄ… teksturÄ™ na podstawie danych z `m_tiles`. Tworzy obiekt `Image`, wypeÄąâ€šnia go kolorami pikseli, a nastÄ™pnie tworzy z niego teksturÄ™. |
| `updateTile(...)` | Aktualizuje dane pojedynczego piksela w bloku i ustawia flagÄ™ `m_mustUpdate`. |
## Klasa `Minimap`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje minimapÄ™ na ekranie. Oblicza, ktĂłre bloki (`MinimapBlock`) sÄ… widoczne, aktualizuje ich tekstury (jeÄąâ€şli to konieczne), a nastÄ™pnie rysuje je w odpowiednich pozycjach. |
| `getTilePoint(...)` / `getTilePosition(...)` | Funkcje pomocnicze do konwersji miÄ™dzy pozycjÄ… na mapie a wspĂłÄąâ€šrzÄ™dnymi na widÄąÄ˝ecie minimapy. |
| `updateTile(const Position& pos, const TilePtr& tile)` | Pobiera kolor i flagi z `Tile` i aktualizuje odpowiadajÄ…cy mu piksel w `MinimapBlock`. |
| `getTile(const Position& pos)` | Zwraca dane `MinimapTile` dla danej pozycji. |
| `threadGetTile(...)` | Wersja `getTile` bezpieczna dla wÄ…tkĂłw, uÄąÄ˝ywana przez asynchroniczne wyszukiwanie Äąâ€şcieÄąÄ˝ki. |
| `loadImage(...)` | Wczytuje dane minimapy z pliku graficznego, analizujÄ…c kolory pikseli w celu okreÄąâ€şlenia wÄąâ€šaÄąâ€şciwoÄąâ€şci (np. czy pole jest moÄąÄ˝liwe do przejÄąâ€şcia). |
| `saveOtmm(...)` / `loadOtmm(...)` | ObsÄąâ€šuguje serializacjÄ™/deserializacjÄ™ danych minimapy do/z formatu `.otmm`, ktĂłry uÄąÄ˝ywa kompresji zlib dla kaÄąÄ˝dego bloku. |
## Struktura danych
- `m_tileBlocks`: Tablica map `std::unordered_map<uint, MinimapBlock_ptr>`, gdzie kaÄąÄ˝dy element tablicy odpowiada jednemu piÄ™tru (`z`). Mapa przechowuje bloki minimapy, indeksowane przez skrĂłt ich pozycji.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`tile.h`**: Pobiera dane do aktualizacji minimapy z obiektĂłw `Tile`.
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania funkcji, np. `GameDontCacheFiles`.
- **`framework/graphics/...`**: UÄąÄ˝ywa klas `Image`, `Texture`, `Painter` do operacji graficznych.
- **`framework/core/resourcemanager.h`**: Do operacji na plikach.
- **`zlib.h`**: Do kompresji/dekompresji danych w formacie `.otmm`.

---
# Ä‘Ĺşâ€śâ€ž position.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy strukturÄ™ `Position` oraz powiÄ…zane z niÄ… funkcje pomocnicze. Jest to fundamentalna struktura uÄąÄ˝ywana w caÄąâ€šym projekcie do reprezentowania wspĂłÄąâ€šrzÄ™dnych w trĂłjwymiarowym Äąâ€şwiecie gry.
## Struktura `Position`
## Pola
- `int x`, `int y`: WspĂłÄąâ€šrzÄ™dne na pÄąâ€šaszczyÄąĹźnie poziomej.
- `short z`: WspĂłÄąâ€šrzÄ™dna piÄ™tra.
## Metody
| Nazwa | Opis |
| --- | --- |
| `Position(uint16 x, uint16 y, uint8 z)` | Konstruktor. |
| `translatedToDirection(Otc::Direction direction)` | Zwraca nowÄ… pozycjÄ™ przesuniÄ™tÄ… o jedno pole w danym kierunku. |
| `translatedToReverseDirection(...)` | Zwraca nowÄ… pozycjÄ™ przesuniÄ™tÄ… w kierunku przeciwnym. |
| `translatedToDirections(...)` | Przetwarza listÄ™ kierunkĂłw i zwraca listÄ™ kolejnych pozycji na Äąâ€şcieÄąÄ˝ce. |
| `getAngleFromPositions(from, to)` | Statyczna metoda obliczajÄ…ca kÄ…t (w radianach) miÄ™dzy dwiema pozycjami. |
| `getDirectionFromPositions(from, to)` | Statyczna metoda zwracajÄ…ca kierunek (`Otc::Direction`) z jednej pozycji do drugiej. |
| `isMapPosition()` | Sprawdza, czy pozycja jest poprawnÄ… pozycjÄ… na mapie. |
| `isValid()` | Sprawdza, czy pozycja jest "waÄąÄ˝na" (rĂłÄąÄ˝na od pozycji specjalnej 65535, 65535, 255). |
| `distance(const Position& pos)` | Oblicza dystans euklidesowy. |
| `manhattanDistance(const Position& pos)` | Oblicza odlegÄąâ€šoÄąâ€şÄ‡ w metryce taksĂłwkowej. |
| `up()`, `down()`, `coveredUp()`, `coveredDown()` | Metody do przemieszczania siÄ™ miÄ™dzy piÄ™trami z uwzglÄ™dnieniem perspektywy izometrycznej. |
| `toString()` | Zwraca pozycjÄ™ w formacie "x,y,z". |
| `operator==`, `operator!=`, `operator<` | Operatory porĂłwnania. |
| `operator+`, `operator-` | Operatory arytmetyczne. |
## Struktura `PositionHasher`
## Opis
Funktor uÄąÄ˝ywany do haszowania obiektĂłw `Position`, co pozwala na uÄąÄ˝ywanie ich jako kluczy w kontenerach `std::unordered_map`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`const.h`**: Definicje `Otc::Direction` i `Otc::MAX_Z`.
- Plik ten jest doÄąâ€šÄ…czany w niemal kaÄąÄ˝dym pliku, ktĂłry operuje na logice Äąâ€şwiata gry.

---
# Ä‘Ĺşâ€śâ€ž protocolcodes.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy kody operacyjne (opcodes) uÄąÄ˝ywane w protokole sieciowym miÄ™dzy klientem a serwerem gry. Zawiera rĂłwnieÄąÄ˝ definicje typĂłw stworzeÄąâ€ž i mapowanie trybĂłw wiadomoÄąâ€şci.
## Namespace `Proto`
## Typy wyliczeniowe
- **`LoginServerOpts`**: Kody operacyjne uÄąÄ˝ywane podczas komunikacji z serwerem logowania.
- **`ItemOpcode`**: Specjalne ID uÄąÄ˝ywane do identyfikacji stworzeÄąâ€ž i tekstĂłw w strumieniu danych o polach mapy.
- **`GameServerOpcodes`**: Kody operacyjne dla pakietĂłw wysyÄąâ€šanych z serwera do klienta. Lista jest dÄąâ€šuga i zawiera kody dla wszystkich akcji w grze, takich jak logowanie, ruch postaci, aktualizacje mapy, wiadomoÄąâ€şci, handel itp.
- **`ClientOpcodes`**: Kody operacyjne dla pakietĂłw wysyÄąâ€šanych z klienta do serwera.
- **`CreatureType`**: Typy stworzeÄąâ€ž (gracz, potwĂłr, NPC).
- **`CreaturesIdRange`**: Zakresy ID dla rĂłÄąÄ˝nych typĂłw stworzeÄąâ€ž.
## Funkcje
- **`buildMessageModesMap(int version)`**: Buduje mapÄ™ tÄąâ€šumaczÄ…cÄ… wewnÄ™trzne tryby wiadomoÄąâ€şci na kody protokoÄąâ€šu dla danej wersji.
- **`translateMessageModeFromServer(uint8 mode)`**: Konwertuje kod z serwera na `Otc::MessageMode`.
- **`translateMessageModeToServer(Otc::MessageMode mode)`**: Konwertuje `Otc::MessageMode` na kod dla serwera.

> NOTE: Lista opkodĂłw zawiera zarĂłwno standardowe kody z protokoÄąâ€šu Tibii, jak i niestandardowe kody specyficzne dla OTClient (`OTClientV8 64-79`) i rozszerzone opkody (`GameServerExtendedOpcode`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`global.h`**: Podstawowe definicje.
- Ten plik jest kluczowy dla `ProtocolGame`, ktĂłry uÄąÄ˝ywa tych kodĂłw do identyfikacji i parsowania pakietĂłw sieciowych.

---
# Ä‘Ĺşâ€śâ€ž protocolgame.cpp
## OgĂłlny opis
Implementacja czÄ™Äąâ€şci klasy `ProtocolGame` odpowiedzialnej za zarzÄ…dzanie poÄąâ€šÄ…czeniem i podstawowÄ… obsÄąâ€šugÄ™ zdarzeÄąâ€ž sieciowych.
## Klasa `ProtocolGame`
## Metody
| Nazwa | Opis |
| --- | --- |
| `login(...)` | Inicjuje proces logowania, zapisujÄ…c dane uwierzytelniajÄ…ce i dane Äąâ€şwiata, a nastÄ™pnie nawiÄ…zuje poÄąâ€šÄ…czenie z serwerem. |
| `onConnect()` | Metoda wywoÄąâ€šywana po pomyÄąâ€şlnym nawiÄ…zaniu poÄąâ€šÄ…czenia. WÄąâ€šÄ…cza odpowiednie funkcje protokoÄąâ€šu (np. sumy kontrolne, szyfrowanie, duÄąÄ˝e pakiety) w zaleÄąÄ˝noÄąâ€şci od `GameFeature` i wysyÄąâ€ša pierwszy pakiet logowania. |
| `onRecv(const InputMessagePtr& inputMessage)` | GÄąâ€šĂłwna pÄ™tla odbioru danych. WywoÄąâ€šywana za kaÄąÄ˝dym razem, gdy nadejdzie nowy pakiet. Weryfikuje rozmiar wiadomoÄąâ€şci (jeÄąâ€şli `GameMessageSizeCheck` jest aktywne), a nastÄ™pnie przekazuje pakiet do `parseMessage` w celu przetworzenia. Po przetworzeniu planuje odbiĂłr kolejnego pakietu. |
| `onError(const boost::system::error_code& error)` | ObsÄąâ€šuguje bÄąâ€šÄ™dy poÄąâ€šÄ…czenia. Powiadamia `g_game` o bÄąâ€šÄ™dzie i rozÄąâ€šÄ…cza klienta. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**: ÄąĹˇciÄąâ€şle wspĂłÄąâ€špracuje z `g_game`, informujÄ…c go o stanie poÄąâ€šÄ…czenia i przekazujÄ…c przetworzone dane.
- **`player.h`**, **`localplayer.h`**: Ustawia instancjÄ™ `LocalPlayer` na poczÄ…tku poÄąâ€šÄ…czenia.
- **`framework/net/protocol.h`**: Dziedziczy z `Protocol` i wykorzystuje jego mechanizmy do obsÄąâ€šugi poÄąâ€šÄ…czenia TCP.

---
# Ä‘Ĺşâ€śâ€ž protocolgame.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `ProtocolGame`. Definiuje interfejs protokoÄąâ€šu sieciowego uÄąÄ˝ywanego do komunikacji z serwerem gry. Zawiera deklaracje funkcji do wysyÄąâ€šania pakietĂłw oraz parsowania odpowiedzi z serwera.
## Klasa `ProtocolGame`
## Opis
Dziedziczy po `Protocol`. Jest to centralny punkt obsÄąâ€šugi komunikacji sieciowej w grze.
## Metody (WysyÄąâ€šanie)
Plik deklaruje duÄąÄ˝Ä… liczbÄ™ metod `send...`, z ktĂłrych kaÄąÄ˝da odpowiada za wysÄąâ€šanie konkretnego pakietu do serwera. PrzykÄąâ€šady:
- `sendLoginPacket(...)`: WysyÄąâ€ša pakiet logowania.
- `sendWalkNorth()`: WysyÄąâ€ša ÄąÄ˝Ä…danie ruchu na pĂłÄąâ€šnoc.
- `sendMove(...)`: WysyÄąâ€ša ÄąÄ˝Ä…danie przesuniÄ™cia przedmiotu.
- `sendTalk(...)`: WysyÄąâ€ša wiadomoÄąâ€şÄ‡ czatu.
- `sendAttack(...)`: WysyÄąâ€ša ÄąÄ˝Ä…danie ataku.
## Metody (Parsowanie)
Deklaruje rĂłwnieÄąÄ˝ metody `parse...`, ktĂłre sÄ… wywoÄąâ€šywane w `protocolgameparse.cpp` do przetwarzania pakietĂłw przychodzÄ…cych z serwera. PrzykÄąâ€šady:
- `parseMapDescription(...)`: Parsuje peÄąâ€šny opis mapy.
- `parseCreatureHealth(...)`: Parsuje aktualizacjÄ™ ÄąÄ˝ycia stworzenia.
- `parseTextMessage(...)`: Parsuje wiadomoÄąâ€şÄ‡ tekstowÄ….
## Metody (Pomocnicze)
- `getThing(...)`, `getItem(...)`, `getCreature(...)`, `getPosition(...)`: Funkcje pomocnicze do odczytywania zÄąâ€šoÄąÄ˝onych typĂłw danych ze strumienia `InputMessage`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw (`Position`, `CreaturePtr`, etc.).
- **`protocolcodes.h`**: UÄąÄ˝ywa kodĂłw operacyjnych zdefiniowanych w tym pliku.
- **`framework/net/protocol.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž spritemanager.cpp
## OgĂłlny opis
Implementacja `SpriteManager`, klasy odpowiedzialnej za zarzÄ…dzanie plikami sprite'Ăłw (`.spr`, `.cwm`). Plik zawiera logikÄ™ wczytywania, zapisywania, a takÄąÄ˝e deszyfrowania i dekompresji danych sprite'Ăłw.
## Klasa `SpriteManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `loadSpr(std::string file)` | GÄąâ€šĂłwna funkcja wczytujÄ…ca. Sprawdza, czy istnieje plik `.cwm` (HD mod) lub `.spr` i wywoÄąâ€šuje odpowiedniÄ… metodÄ™ wczytujÄ…cÄ…. |
| `saveSpr(...)` / `saveSpr64(...)` | Metody do zapisywania sprite'Ăłw w formacie `.spr` (32x32 lub 64x64). Wymaga `WITH_ENCRYPTION`. |
| `encryptSprites(...)` | Zapisuje sprite'y w niestandardowym, zaszyfrowanym formacie OTV8. |
| `dumpSprites(...)` | Zapisuje wszystkie sprite'y jako pojedyncze pliki PNG do danego folderu (funkcja deweloperska). |
| `unload()` | Zwalnia wszystkie zasoby zwiÄ…zane ze sprite'ami. |
| `getSpriteImage(int id)` | GÄąâ€šĂłwna metoda do pobierania obrazu sprite'a. WywoÄąâ€šuje odpowiedniÄ… implementacjÄ™ w zaleÄąÄ˝noÄąâ€şci od tego, czy zaÄąâ€šadowano mod HD (`.cwm`) czy standardowy plik (`.spr`). |
| `loadCasualSpr(...)` | Wczytuje standardowy plik `.spr`. Odczytuje sygnaturÄ™ i liczbÄ™ sprite'Ăłw. ObsÄąâ€šuguje rĂłwnieÄąÄ˝ zaszyfrowany format OTV8. |
| `loadCwmSpr(...)` | Wczytuje plik `.cwm`, ktĂłry jest zbiorem skompresowanych danych PNG. UÄąÄ˝ywa `PngUnpacker` do rozpakowania wszystkich sprite'Ăłw do pamiÄ™ci. |
| `getSpriteImageCasual(int id)` | Pobiera obraz sprite'a z pliku `.spr`. Odczytuje adres sprite'a z tablicy offsetĂłw, a nastÄ™pnie dekompresuje dane pikseli, ktĂłre sÄ… zapisane w formacie RLE (run-length encoding) z przezroczystymi i kolorowymi pikselami. |
| `getSpriteImageHd(int id)` | Pobiera obraz sprite'a z pamiÄ™ci podrÄ™cznej wczytanej z pliku `.cwm`. Dekoduje dane PNG dla danego sprite'a. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania `GameFeature`, ktĂłre wpÄąâ€šywajÄ… na format pliku `.spr`.
- **`framework/core/resourcemanager.h`**: Do operacji na plikach.
- **`framework/graphics/image.h`**: Zwraca obiekty `ImagePtr`.
- **`framework/util/crypt.h`**: Do deszyfrowania formatu OTV8.
- **`framework/util/pngunpacker.h`**: Do rozpakowywania plikĂłw `.cwm`.

---
# Ä‘Ĺşâ€śâ€ž protocolgamesend.cpp
## OgĂłlny opis
Plik ten zawiera implementacjÄ™ metod klasy `ProtocolGame` odpowiedzialnych za **wysyÄąâ€šanie** pakietĂłw do serwera gry. KaÄąÄ˝da metoda odpowiada za stworzenie i wysÄąâ€šanie konkretnego komunikatu zgodnie z protokoÄąâ€šem sieciowym.
## Klasa `ProtocolGame`
## Metody
| Nazwa | Opis |
| --- | --- |
| `send(const OutputMessagePtr& outputMessage, ...)` | WysyÄąâ€ša przygotowany pakiet, sprawdzajÄ…c uprzednio zabezpieczenia anty-botowe (`g_game.checkBotProtection()`). |
| `sendLoginPacket(...)` | Tworzy i wysyÄąâ€ša pakiet logowania. Zawiera logikÄ™ szyfrowania RSA, dodawania klucza XTEA, a takÄąÄ˝e wysyÄąâ€šania dodatkowych danych identyfikacyjnych klienta (nazwa uÄąÄ˝ytkownika, CPU, adresy MAC), jeÄąâ€şli serwer to obsÄąâ€šuguje. |
| `sendWalkNorth()`, `sendWalkEast()`, etc. | WysyÄąâ€šajÄ… jednobajtowe pakiety z ÄąÄ˝Ä…daniem ruchu w danym kierunku. |
| `sendAutoWalk(...)` | WysyÄąâ€ša sekwencjÄ™ kierunkĂłw dla automatycznego poruszania siÄ™. |
| `sendNewWalk(...)` | WysyÄąâ€ša pakiet dla nowego systemu chodzenia, zawierajÄ…cy ID kroku, ID predykcji, pozycjÄ™ i Äąâ€şcieÄąÄ˝kÄ™. |
| `sendMove(...)` | WysyÄąâ€ša ÄąÄ˝Ä…danie przesuniÄ™cia przedmiotu/stworzenia. |
| `sendUseItem(...)`, `sendUseItemWith(...)` | WysyÄąâ€šajÄ… ÄąÄ˝Ä…dania uÄąÄ˝ycia przedmiotĂłw. |
| `sendTalk(...)` | WysyÄąâ€ša wiadomoÄąâ€şÄ‡ czatu. Konstruuje pakiet w zaleÄąÄ˝noÄąâ€şci od trybu wiadomoÄąâ€şci (publiczny, prywatny, kanaÄąâ€š). |
| `sendAttack(...)`, `sendFollow(...)` | WysyÄąâ€šajÄ… ÄąÄ˝Ä…dania ataku lub Äąâ€şledzenia stworzenia, zawierajÄ…c sekwencyjny numer identyfikujÄ…cy akcjÄ™. |
| `sendChangeOutfit(...)` | WysyÄąâ€ša nowy ubiĂłr gracza, uwzglÄ™dniajÄ…c wszystkie jego elementy (kolory, dodatki, wierzchowiec, etc.) w zaleÄąÄ˝noÄąâ€şci od wspieranych przez serwer funkcji. |
| `addPosition(const OutputMessagePtr& msg, ...)` | Pomocnicza metoda do dodawania wspĂłÄąâ€šrzÄ™dnych `Position` do pakietu. |
## Logika
WiÄ™kszoÄąâ€şÄ‡ funkcji w tym pliku ma prostÄ… strukturÄ™:
1.  StwĂłrz nowy `OutputMessage`.
2.  Dodaj kod operacyjny (opcode) za pomocÄ… `msg->addU8(...)`.
3.  Dodaj kolejne dane (ID, pozycje, stringi) zgodnie ze specyfikacjÄ… protokoÄąâ€šu.
4.  WyÄąâ€şlij pakiet za pomocÄ… `send(msg)`.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**: UÄąÄ˝ywa `g_game` do sprawdzania funkcji serwera (`GameFeature`), ktĂłre determinujÄ… format wysyÄąâ€šanych pakietĂłw.
- **`localplayer.h`**: UÄąÄ˝ywa pozycji lokalnego gracza w niektĂłrych pakietach (np. `sendTalk`).
- **`framework/util/crypt.h`**: UÄąÄ˝ywa `g_crypt` do szyfrowania RSA.
- **`framework/platform/platform.h`**: Pobiera informacje o systemie do wysÄąâ€šania w pakiecie logowania.

---
# Ä‘Ĺşâ€śâ€ž localplayer.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `LocalPlayer`, ktĂłra reprezentuje postaÄ‡ sterowanÄ… przez gracza. Jest to specjalizacja klasy `Player`.
## Klasa `LocalPlayer`
## Opis
Dziedziczy po `Player`. Dodaje funkcjonalnoÄąâ€şci specyficzne dla gracza, ktĂłry jest kontrolowany przez klienta, takie jak:
-   **Pre-walking**: Przewidywanie ruchu przed otrzymaniem odpowiedzi z serwera.
-   **Auto-walking**: Automatyczne poruszanie siÄ™ do celu.
-   **ZarzÄ…dzanie stanem**: Przechowuje szczegĂłÄąâ€šowe statystyki (ÄąÄ˝ycie, mana, umiejÄ™tnoÄąâ€şci, etc.).
## Metody
| Nazwa | Opis |
| --- | --- |
| `lockWalk(int millis)` | Blokuje moÄąÄ˝liwoÄąâ€şÄ‡ chodzenia na okreÄąâ€şlony czas. |
| `stopAutoWalk()` | Przerywa auto-walking. |
| `autoWalk(Position destination, ...)` | Rozpoczyna auto-walking do celu. |
| `canWalk(...)` | Sprawdza, czy gracz moÄąÄ˝e siÄ™ poruszyÄ‡. |
| `isPreWalking()` | Zwraca `true`, jeÄąâ€şli gracz wykonuje ruch "pre-walk". |
| `getPrewalkingPosition(...)` | Zwraca pozycjÄ™, na ktĂłrej gracz znajdzie siÄ™ po zakoÄąâ€žczeniu wszystkich ruchĂłw "pre-walk". |
| `setHealth(...)`, `setMana(...)`, etc. | Metody do ustawiania statystyk gracza. |
| `getHealth()`, `getMana()`, etc. | Metody do pobierania statystyk. |
| `hasSight(const Position& pos)` | Sprawdza, czy pozycja jest w zasiÄ™gu wzroku. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`player.h`**: Klasa bazowa.
- **`walkmatrix.h`**: UÄąÄ˝ywa `WalkMatrix` do Äąâ€şledzenia predykcji ruchu.

---
# Ä‘Ĺşâ€śâ€ž towns.cpp
## OgĂłlny opis
Implementacja `Town` i `TownManager`, ktĂłre sÄąâ€šuÄąÄ˝Ä… do zarzÄ…dzania danymi o miastach w grze.
## Klasa `Town`
## Metody
- **`Town(uint32 tid, ...)`**: Konstruktor, ktĂłry inicjalizuje miasto z podanym ID, nazwÄ… i pozycjÄ… (zwykle Äąâ€şwiÄ…tyni).
## Klasa `TownManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addTown(const TownPtr &town)` | Dodaje nowe miasto do listy, jeÄąâ€şli jeszcze nie istnieje. |
| `removeTown(uint32 townId)` | Usuwa miasto o podanym ID. |
| `getTown(uint32 townId)` | Zwraca miasto po jego ID. |
| `getTownByName(std::string name)` | Zwraca miasto po jego nazwie. |
| `findTown(uint32 townId)` | WewnÄ™trzna metoda do wyszukiwania iteratora do miasta. |
| `sort()` | Sortuje listÄ™ miast alfabetycznie wedÄąâ€šug nazwy. |
## Zmienne globalne
- **`TownManager g_towns`**: Globalna instancja managera miast.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`mapio.cpp`**: MenedÄąÄ˝er `g_towns` jest wypeÄąâ€šniany danymi podczas wczytywania mapy w formacie OTBM.

---
# Ä‘Ĺşâ€śâ€ž spritemanager.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `SpriteManager`, singletonu odpowiedzialnego za zarzÄ…dzanie plikami sprite'Ăłw (`.spr`).
## Klasa `SpriteManager`
## Opis
Centralny punkt dostÄ™pu do danych graficznych sprite'Ăłw. Odpowiada za wczytywanie, deszyfrowanie, dekompresjÄ™ i dostarczanie obrazĂłw poszczegĂłlnych sprite'Ăłw.
## Metody
| Nazwa | Opis |
| --- | --- |
| `loadSpr(std::string file)` | Wczytuje plik sprite'Ăłw (automatycznie wykrywa format: `.spr`, `.cwm`, OTV8). |
| `unload()` | Zwalnia wszystkie zaÄąâ€šadowane dane sprite'Ăłw. |
| `saveSpr(...)` / `encryptSprites(...)` | Metody (dostÄ™pne z `WITH_ENCRYPTION`) do zapisywania i szyfrowania plikĂłw sprite'Ăłw. |
| `getSignature()` | Zwraca sygnaturÄ™ wczytanego pliku `.spr`. |
| `getSpritesCount()` | Zwraca liczbÄ™ sprite'Ăłw w pliku. |
| `getSpriteImage(int id)` | GÄąâ€šĂłwna metoda do pobierania obrazu sprite'a o danym ID. |
| `isLoaded()` | Zwraca `true`, jeÄąâ€şli plik sprite'Ăłw jest zaÄąâ€šadowany. |
| `spriteSize()` | Zwraca rozmiar boku pojedynczego sprite'a (np. 32 lub 64 piksele). |
| `getOffsetFactor()` | Zwraca wspĂłÄąâ€šczynnik skalowania dla przemieszczeÄąâ€ž (displacement) w zaleÄąÄ˝noÄąâ€şci od `spriteSize`. |
| `isHdMod()` | Zwraca `true`, jeÄąâ€şli zaÄąâ€šadowano modyfikacjÄ™ HD (`.cwm`). |
## Zmienne globalne
- **`SpriteManager g_sprites`**: Globalna instancja managera sprite'Ăłw.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/core/declarations.h`**: Podstawowe deklaracje.
- **`framework/graphics/declarations.h`**: Deklaracje typĂłw graficznych.
- Niemal kaÄąÄ˝da klasa renderujÄ…ca obiekty w grze (np. `ThingType`, `Item`, `Creature`) zaleÄąÄ˝y od `SpriteManager`.

---
# Ä‘Ĺşâ€śâ€ž tile.cpp
## OgĂłlny opis
Implementacja klasy `Tile`, ktĂłra reprezentuje pojedyncze pole na mapie gry. Plik zawiera logikÄ™ rysowania pola i wszystkich znajdujÄ…cych siÄ™ na nim obiektĂłw, zarzÄ…dzania stosem obiektĂłw oraz dostarczania informacji o wÄąâ€šaÄąâ€şciwoÄąâ€şciach pola.
## Klasa `Tile`
## Metody
## Rysowanie
| Nazwa | Opis |
| --- | --- |
| `drawGround(...)` | Rysuje podÄąâ€šoÄąÄ˝e i obiekty na najniÄąÄ˝szej warstwie. Oblicza `m_drawElevation` (przesuniÄ™cie w pionie dla obiektĂłw o wysokoÄąâ€şci > 1). |
| `drawBottom(...)` | Rysuje przedmioty, ktĂłre znajdujÄ… siÄ™ na spodzie, ale nad podÄąâ€šoÄąÄ˝em (np. Äąâ€şciany). |
| `drawCreatures(...)` | Rysuje stworzenia na tym polu oraz stworzenia, ktĂłre na nie wchodzÄ…. |
| `drawTop(...)` | Rysuje przedmioty na wierzchu, efekty oraz ponownie stworzenia, aby obsÄąâ€šuÄąÄ˝yÄ‡ przypadki nakÄąâ€šadania siÄ™. |
| `drawTexts(...)` | Rysuje tekst przypisany do pola (np. timer). |
| `drawWidget(...)` | Rysuje przypisany do pola widÄąÄ˝et. |
## ZarzÄ…dzanie obiektami
| Nazwa | Opis |
| --- | --- |
| `addThing(...)` | Dodaje obiekt (`Thing`) na stos w odpowiedniej pozycji, uwzglÄ™dniajÄ…c jego priorytet (ziemia, przedmioty, stworzenia). |
| `removeThing(...)` | Usuwa obiekt ze stosu. |
| `addWalkingCreature(...)` | Dodaje stworzenie do listy "przechodzÄ…cych" przez to pole, ktĂłre sÄ… rysowane osobno. |
| `getThing(...)` | Zwraca obiekt z danej pozycji na stosie. |
| `getTopThing()`, `getTopCreature()`, etc. | ZwracajÄ… "najwaÄąÄ˝niejszy" obiekt danego typu na polu, uwzglÄ™dniajÄ…c logikÄ™ gry (np. na co patrzy gracz, czego uÄąÄ˝ywa). |
| `getItems()`, `getCreatures()` | ZwracajÄ… listy wszystkich przedmiotĂłw lub stworzeÄąâ€ž na polu. |
## WÄąâ€šaÄąâ€şciwoÄąâ€şci
| Nazwa | Opis |
| --- | --- |
| `isWalkable(...)` | Sprawdza, czy po polu moÄąÄ˝na chodziÄ‡ (czy nie ma blokujÄ…cych przedmiotĂłw lub stworzeÄąâ€ž). |
| `isPathable()` | Sprawdza, czy algorytm wyszukiwania Äąâ€şcieÄąÄ˝ki moÄąÄ˝e uÄąÄ˝ywaÄ‡ tego pola. |
| `isFullGround()` | Sprawdza, czy podÄąâ€šoÄąÄ˝e caÄąâ€škowicie zakrywa pole pod nim. |
| `getGroundSpeed()` | Zwraca prÄ™dkoÄąâ€şÄ‡ poruszania siÄ™ po tym polu. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**: UÄąÄ˝ywa `g_map` do pobierania sÄ…siednich pĂłl (np. przy korekcji zwÄąâ€šok).
- **`game.h`**: DostÄ™p do `g_game` w celu sprawdzania `GameFeature`.
- **`thing.h`**, **`item.h`**, **`creature.h`**: ZarzÄ…dza tymi obiektami.
- **`lightview.h`**: Przekazuje `LightView` do metod rysujÄ…cych obiekty, aby mogÄąâ€šy dodaÄ‡ swoje Äąâ€şwiatÄąâ€šo.

---
# Ä‘Ĺşâ€śâ€ž statictext.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `StaticText`, ktĂłra reprezentuje tekst pojawiajÄ…cy siÄ™ nad gÄąâ€šowami stworzeÄąâ€ž lub na polach mapy.
## Struktura `StaticTextMessage`
-   **`texts`**: Wektor par `std::string`, gdzie pierwsza to treÄąâ€şÄ‡, a druga to kolor w formacie hex.
-   **`time`**: Czas (w tickach), po ktĂłrym wiadomoÄąâ€şÄ‡ powinna zniknÄ…Ä‡.
## Klasa `StaticText`
## Opis
Dziedziczy po `Thing`. ZarzÄ…dza kolejkÄ… wiadomoÄąâ€şci, ktĂłre sÄ… wyÄąâ€şwietlane jedna po drugiej. Jest uÄąÄ˝ywana do mowy postaci, potworĂłw, a takÄąÄ˝e do niestandardowych tekstĂłw na mapie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawText(...)` | Rysuje aktualnie wyÄąâ€şwietlanÄ… wiadomoÄąâ€şÄ‡. |
| `getName()` | Zwraca nazwÄ™ postaci mĂłwiÄ…cej. |
| `getText()` | Zwraca aktualnie wyÄąâ€şwietlany tekst. |
| `getMessageMode()` | Zwraca tryb wiadomoÄąâ€şci (np. `Say`, `Yell`). |
| `addMessage(...)` / `addColoredMessage(...)` | Dodaje nowÄ… wiadomoÄąâ€şÄ‡ do kolejki. Oblicza czas jej wyÄąâ€şwietlania na podstawie dÄąâ€šugoÄąâ€şci. |
| `setText(...)` / `setFont(...)` | Ustawia surowy tekst i czcionkÄ™ (gÄąâ€šĂłwnie dla niestandardowych tekstĂłw). |
| `isYell()` | Zwraca `true`, jeÄąâ€şli tryb wiadomoÄąâ€şci to krzyk. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thing.h`**: Klasa bazowa.
- **`framework/graphics/cachedtext.h`**: UÄąÄ˝ywa `CachedText` do efektywnego renderowania tekstu.
- **`framework/core/timer.h`**: UÄąÄ˝ywane do zarzÄ…dzania czasem ÄąÄ˝ycia wiadomoÄąâ€şci.

---
# Ä‘Ĺşâ€śâ€ž uimapanchorlayout.cpp
## OgĂłlny opis
Implementacja `UIPositionAnchor` i `UIMapAnchorLayout`, ktĂłre rozszerzajÄ… standardowy system kotwic (`UIAnchorLayout`) o moÄąÄ˝liwoÄąâ€şÄ‡ przypinania widÄąÄ˝etĂłw do konkretnych pozycji na minimapie.
## Klasa `UIPositionAnchor`
## Metody
| Nazwa | Opis |
| --- | --- |
| `getHookedPoint(...)` | Kluczowa metoda, ktĂłra oblicza wspĂłÄąâ€šrzÄ™dnÄ… (X lub Y) na ekranie na podstawie `m_hookedPosition`. Pobiera `UIMinimap`, prosi go o prostokÄ…t (`Rect`) odpowiadajÄ…cy danemu polu na mapie (`getTileRect`), a nastÄ™pnie zwraca odpowiedniÄ… krawÄ™dÄąĹź tego prostokÄ…ta (np. `left`, `top`, `horizontalCenter`). |
## Klasa `UIMapAnchorLayout`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addPositionAnchor(...)` | Tworzy nowy obiekt `UIPositionAnchor` i dodaje go do grupy kotwic dla danego widÄąÄ˝etu. |
| `centerInPosition(...)` | Funkcja pomocnicza, ktĂłra dodaje dwie kotwice (`HorizontalCenter` i `VerticalCenter`), aby wyÄąâ€şrodkowaÄ‡ widÄąÄ˝et na danym polu mapy. |
| `fillPosition(...)` | Funkcja pomocnicza, ktĂłra dodaje cztery kotwice (`Left`, `Right`, `Top`, `Bottom`), aby widÄąÄ˝et wypeÄąâ€šniÄąâ€š obszar danego pola na mapie. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`uiminimap.h`**: `UIPositionAnchor` rzutuje widÄąÄ˝et-rodzica na `UIMinimap`, aby uzyskaÄ‡ dostÄ™p do metody `getTileRect`.
- **`framework/ui/uiwidget.h`**: WspĂłÄąâ€špracuje z widÄąÄ˝etami.
- **`framework/ui/uianchorlayout.h`**: Rozszerza standardowy layout kotwic.

---
# Ä‘Ĺşâ€śâ€ž thing.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `Thing`, abstrakcyjnej klasy bazowej dla wszystkich obiektĂłw, ktĂłre mogÄ… pojawiÄ‡ siÄ™ na mapie w grze.
## Klasa `Thing`
## Opis
Dziedziczy po `LuaObject`. Definiuje wspĂłlny interfejs dla przedmiotĂłw, stworzeÄąâ€ž, efektĂłw, pociskĂłw i tekstĂłw. KaÄąÄ˝dy obiekt `Thing` ma pozycjÄ™ i naleÄąÄ˝y do okreÄąâ€şlonego typu (`ThingType`).
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Wirtualna metoda do rysowania obiektu. |
| `setPosition(const Position& position)` | Ustawia pozycjÄ™ obiektu. |
| `getPosition()` | Zwraca pozycjÄ™ obiektu. |
| `getStackPriority()` | Zwraca priorytet na stosie, ktĂłry decyduje o kolejnoÄąâ€şci rysowania i interakcji. |
| `getTile()` | Zwraca wskaÄąĹźnik do pola (`Tile`), na ktĂłrym znajduje siÄ™ obiekt. |
| `getStackPos()` | Zwraca pozycjÄ™ obiektu na stosie wewnÄ…trz pola. |
| `isItem()`, `isCreature()`, etc. | Wirtualne metody do identyfikacji typu obiektu. |
| `getThingType()` / `rawGetThingType()` | ZwracajÄ… `ThingType` dla tego obiektu. |
| `getSize()`, `getWidth()`, `getHeight()`, etc. | Metody-skrĂłty do wÄąâ€šaÄąâ€şciwoÄąâ€şci z `ThingType`. |
| `onPositionChange(...)`, `onAppear()`, `onDisappear()` | Wirtualne metody wywoÄąâ€šywane w kluczowych momentach cyklu ÄąÄ˝ycia obiektu. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw, np. `TilePtr`.
- **`thingtype.h`**: KaÄąÄ˝dy `Thing` ma swĂłj `ThingType`.
- **`framework/luaengine/luaobject.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž uiitem.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `UIItem`, widÄąÄ˝etu interfejsu uÄąÄ˝ytkownika przeznaczonego do wyÄąâ€şwietlania przedmiotĂłw (`Item`).
## Klasa `UIItem`
## Opis
Dziedziczy po `UIWidget`. SÄąâ€šuÄąÄ˝y do renderowania przedmiotĂłw w UI, np. w ekwipunku, kontenerach, oknach handlu.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje tÄąâ€šo, obraz, a nastÄ™pnie sam przedmiot (`m_item->draw(...)`), liczbÄ™ sztuk (jeÄąâ€şli dotyczy) i ramkÄ™. |
| `setItemId(int id)` | Ustawia przedmiot do wyÄąâ€şwietlenia na podstawie jego ID. |
| `setItemCount(int count)` | Ustawia liczbÄ™ sztuk przedmiotu. |
| `setItem(const ItemPtr& item)` | Ustawia przedmiot do wyÄąâ€şwietlenia na podstawie istniejÄ…cego obiektu `Item`. |
| `setVirtual(bool virt)` | Oznacza, czy przedmiot jest "wirtualny" (nie jest prawdziwÄ… instancjÄ…, tylko reprezentacjÄ… wizualnÄ…). |
| `setShowCount(bool value)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza wyÄąâ€şwietlanie liczby sztuk. |
| `setItemShader(const std::string& str)` | Ustawia niestandardowy shader dla przedmiotu. |
| `getItem()` | Zwraca obiekt `Item` powiÄ…zany z widÄąÄ˝etem. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.
- **`item.h`**: Przechowuje i rysuje obiekt `Item`.

---
# Ä‘Ĺşâ€śâ€ž thing.cpp
## OgĂłlny opis
Implementacja klasy bazowej `Thing`. Zawiera podstawowÄ… logikÄ™ wspĂłlnÄ… dla wszystkich obiektĂłw na mapie.
## Klasa `Thing`
## Metody
| Nazwa | Opis |
| --- | --- |
| `setPosition(const Position& position)` | Aktualizuje pozycjÄ™ obiektu i wywoÄąâ€šuje wirtualnÄ… metodÄ™ `onPositionChange`. |
| `getStackPriority()` | Zwraca priorytet obiektu na stosie wewnÄ…trz pola. KolejnoÄąâ€şÄ‡ jest Äąâ€şciÄąâ€şle zdefiniowana: ziemia, obramowanie ziemi, obiekty na dole (np. Äąâ€şciany), obiekty na gĂłrze (np. dywany), stworzenia, a na koÄąâ€žcu zwykÄąâ€še przedmioty. |
| `getTile()` | Zwraca wskaÄąĹźnik do pola, na ktĂłrym znajduje siÄ™ obiekt, uÄąÄ˝ywajÄ…c `g_map`. |
| `getParentContainer()` | JeÄąâ€şli obiekt znajduje siÄ™ w kontenerze, zwraca wskaÄąĹźnik do tego kontenera. Pozycja w kontenerze jest specjalnie kodowana. |
| `getStackPos()` | Zwraca pozycjÄ™ na stosie: albo wewnÄ…trz kontenera, albo na polu mapy. |
| `getThingType()` / `rawGetThingType()` | ZwracajÄ… domyÄąâ€şlny, "pusty" `ThingType`. MuszÄ… byÄ‡ nadpisane przez klasy pochodne. |
| `updatedMarkedColor()` | Aktualizuje kolor i przezroczystoÄąâ€şÄ‡ znacznika (jeÄąâ€şli jest ustawiony), tworzÄ…c efekt pulsowania. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`spritemanager.h`**, **`thingtypemanager.h`**: Podstawowe zaleÄąÄ˝noÄąâ€şci.
- **`map.h`**: Do pobierania `Tile`.
- **`game.h`**: Do pobierania kontenerĂłw.

---
# Ä‘Ĺşâ€śâ€ž uimap.cpp
## OgĂłlny opis
Implementacja `UIMap`, widÄąÄ˝etu interfejsu uÄąÄ˝ytkownika, ktĂłry renderuje gÄąâ€šĂłwny widok mapy gry.
## Klasa `UIMap`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | GÄąâ€šĂłwna funkcja rysujÄ…ca. Jest wywoÄąâ€šywana trzykrotnie dla rĂłÄąÄ˝nych "warstw" (`DrawPane`): <br> 1. `MapBackgroundPane`: Rysuje tÄąâ€šo mapy (`m_mapView->drawMapBackground`). <br> 2. `MapForegroundPane`: Rysuje pierwszy plan (`m_mapView->drawMapForeground`). <br> 3. `ForegroundPane`: Rysuje obramowanie wokĂłÄąâ€š mapy. |
| `setZoom(int zoom)` | Ustawia poziom przybliÄąÄ˝enia, co wpÄąâ€šywa na `m_mapView->setVisibleDimension`. |
| `zoomIn()` / `zoomOut()` | Zmienia poziom przybliÄąÄ˝enia o staÄąâ€šÄ… wartoÄąâ€şÄ‡. |
| `setVisibleDimension(...)` | Ustawia widoczny wymiar w `m_mapView` i aktualizuje proporcje. |
| `setKeepAspectRatio(bool enable)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza zachowanie staÄąâ€šych proporcji widoku mapy. |
| `getPosition(const Point& mousePos)` | Konwertuje pozycjÄ™ kursora na ekranie na pozycjÄ™ (`Position`) w Äąâ€şwiecie gry. |
| `getTile(const Point& mousePos)` | Zwraca pole (`Tile`) pod kursorem, przeszukujÄ…c widoczne piÄ™tra od gĂłry do doÄąâ€šu w poszukiwaniu klikalnego obiektu. |
| `updateVisibleDimension()` | Przelicza i ustawia widoczny wymiar w `m_mapView` na podstawie aktualnego zoomu i proporcji. |
| `updateMapSize()` | Dopasowuje rozmiar i pozycjÄ™ prostokÄ…ta rysowania mapy (`m_mapRect`) do rozmiaru widÄąÄ˝etu, zachowujÄ…c proporcje, jeÄąâ€şli to wymagane. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**, **`map.h`**: DostÄ™p do globalnych obiektĂłw gry i mapy.
- **`mapview.h`**: `UIMap` jest "opakowaniem" dla `MapView`, przekazujÄ…c mu zadania renderowania.
- **`framework/otml/otml.h`**: Parsuje wÄąâ€šaÄąâ€şciwoÄąâ€şci z plikĂłw OTML, takie jak `multifloor` czy `animated`.

---
# Ä‘Ĺşâ€śâ€ž statictext.cpp
## OgĂłlny opis
Implementacja `StaticText`, klasy odpowiedzialnej za wyÄąâ€şwietlanie mowy postaci i innych tekstĂłw na mapie.
## Klasa `StaticText`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawText(...)` | Rysuje tekst na ekranie, centrujÄ…c go i dopasowujÄ…c do prostokÄ…ta nadrzÄ™dnego. |
| `addMessage(...)` / `addColoredMessage(...)` | Dodaje nowÄ… wiadomoÄąâ€şÄ‡ do kolejki. JeÄąâ€şli jest to pierwsza wiadomoÄąâ€şÄ‡, ustawia tryb (np. `Say`, `Yell`) i nazwÄ™ mĂłwiÄ…cego. JeÄąâ€şli kolejne wiadomoÄąâ€şci pasujÄ… do poprzednich (ten sam mĂłwiÄ…cy i tryb), sÄ… dodawane do kolejki. Oblicza czas wyÄąâ€şwietlania na podstawie dÄąâ€šugoÄąâ€şci tekstu. |
| `update()` | Metoda wywoÄąâ€šywana po upÄąâ€šyniÄ™ciu czasu wyÄąâ€şwietlania wiadomoÄąâ€şci. Usuwa najstarszÄ… wiadomoÄąâ€şÄ‡ z kolejki. JeÄąâ€şli kolejka jest pusta, planuje usuniÄ™cie caÄąâ€šego obiektu `StaticText` z mapy. |
| `scheduleUpdate()` | Planuje wywoÄąâ€šanie `update()` po czasie rĂłwnym czasowi ÄąÄ˝ycia najstarszej wiadomoÄąâ€şci w kolejce. |
| `compose()` | Tworzy sformatowany tekst do wyÄąâ€şwietlenia. ÄąÂÄ…czy wszystkie wiadomoÄąâ€şci z kolejki, dodaje nagÄąâ€šĂłwki (np. "Player says:"), ustawia kolory i zawija tekst, jeÄąâ€şli jest zbyt dÄąâ€šugi. |
## Logika dziaÄąâ€šania
`StaticText` dziaÄąâ€ša jak kolejka FIFO dla wiadomoÄąâ€şci. KaÄąÄ˝da nowa wiadomoÄąâ€şÄ‡ jest dodawana na koniec. `compose` tworzy jeden ciÄ…gÄąâ€šy, sformatowany tekst ze wszystkich wiadomoÄąâ€şci w kolejce, ktĂłry jest nastÄ™pnie rysowany przez `drawText`. `scheduleUpdate` i `update` zapewniajÄ…, ÄąÄ˝e wiadomoÄąâ€şci znikajÄ… po okreÄąâ€şlonym czasie, a caÄąâ€šy obiekt jest usuwany, gdy nie ma juÄąÄ˝ nic do wyÄąâ€şwietlenia.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`map.h`**: UÄąÄ˝ywa `g_map` do usuniÄ™cia obiektu po zakoÄąâ€žczeniu.
- **`framework/core/eventdispatcher.h`**: UÄąÄ˝ywa `g_dispatcher` do planowania aktualizacji.
- **`framework/graphics/fontmanager.h`**: UÄąÄ˝ywa `g_fonts` do zarzÄ…dzania czcionkami.

---
# Ä‘Ĺşâ€śâ€ž uiitem.cpp
## OgĂłlny opis
Implementacja `UIItem`, widÄąÄ˝etu do wyÄąâ€şwietlania przedmiotĂłw w interfejsie uÄąÄ˝ytkownika.
## Klasa `UIItem`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widÄąÄ˝et. Renderuje tÄąâ€šo, obraz, a nastÄ™pnie sam przedmiot (`m_item->draw(...)`), uÄąÄ˝ywajÄ…c prostokÄ…ta `getPaddingRect()`. JeÄąâ€şli `m_showCount` jest wÄąâ€šÄ…czone, rysuje rĂłwnieÄąÄ˝ liczbÄ™ przedmiotĂłw w prawym dolnym rogu. |
| `setItemId(int id)` | Tworzy nowy obiekt `Item` (jeÄąâ€şli go nie byÄąâ€šo) lub aktualizuje ID istniejÄ…cego. |
| `setItemCount(int count)` | Ustawia liczbÄ™ przedmiotĂłw i aktualizuje tekst licznika. |
| `setItem(const ItemPtr& item)` | Ustawia przedmiot na podstawie gotowego obiektu `ItemPtr`. |
| `setItemShader(const std::string& str)` | Ustawia niestandardowy shader dla renderowanego przedmiotu. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `item-id`, `item-count`, `virtual`. |
| `cacheCountText()` | Formatuje tekst licznika. Dla liczb >= 1000 uÄąÄ˝ywa skrĂłtu "k" (np. "1.2k"), jeÄąâ€şli funkcja `GameCountU16` jest aktywna. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`spritemanager.h`**: UÄąÄ˝ywany przez `Item` do pobierania sprite'Ăłw.
- **`game.h`**: Sprawdza `GameFeature`, np. `GameCountU16`.
- **`framework/otml/otml.h`**: Do parsowania stylĂłw.
- **`framework/graphics/graphics.h`**: Do operacji rysowania.

---
# Ä‘Ĺşâ€śâ€ž thingstype.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `ThingsType` (bÄąâ€šÄ…d w nazwie, prawdopodobnie powinno byÄ‡ `ThingTypeManager`). Definiuje interfejs singletonu, ktĂłry zarzÄ…dza wszystkimi typami obiektĂłw (`ThingType`) w grze, wczytywanymi z plikĂłw `.dat`.

> NOTE: Nazwa klasy `ThingsType` jest mylÄ…ca. W rzeczywistoÄąâ€şci jest to menedÄąÄ˝er, ktĂłry przechowuje i zarzÄ…dza obiektami `ThingType`. W innych plikach jest on nazywany `ThingTypeManager`.
## Klasa `ThingsType`
## Typy wyliczeniowe
- **`Categories`**: Kategorie obiektĂłw (Przedmiot, Stworzenie, Efekt, Pocisk).
## Metody
| Nazwa | Opis |
| --- | --- |
| `load(const std::string& file)` | Wczytuje i parsuje plik `.dat`. |
| `unload()` | Zwalnia zaÄąâ€šadowane dane. |
| `parseThingType(...)` | Parsuje dane pojedynczego typu obiektu ze strumienia pliku. |
| `getEmptyThingType()` | Zwraca pusty, domyÄąâ€şlny obiekt `ThingType`. |
| `getThingType(uint16 id, Categories category)` | Zwraca `ThingType` dla danego ID i kategorii. |
| `getSignature()` | Zwraca sygnaturÄ™ wczytanego pliku `.dat`. |
| `isLoaded()` | Zwraca `true`, jeÄąâ€şli plik `.dat` jest zaÄąâ€šadowany. |
| `isValidItemId(int id)` | Sprawdza, czy ID przedmiotu jest w prawidÄąâ€šowym zakresie. |
## Zmienne globalne
- **`ThingsType g_thingsType`**: Globalna instancja managera (pĂłÄąĹźniej w kodzie uÄąÄ˝ywane jest `g_things`).
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thingtype.h`**: ZarzÄ…dza obiektami `ThingType`.
- **`framework/core/declarations.h`**: Podstawowe deklaracje.

---
# Ä‘Ĺşâ€śâ€ž uigraph.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `UIGraph`, widÄąÄ˝etu sÄąâ€šuÄąÄ˝Ä…cego do rysowania prostych wykresĂłw liniowych.
## Klasa `UIGraph`
## Opis
Dziedziczy po `UIWidget`. Przechowuje kolejkÄ™ wartoÄąâ€şci i renderuje je jako wykres liniowy.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje wykres. Oblicza skalÄ™, przygotowuje punkty i rysuje liniÄ™ za pomocÄ… `g_drawQueue->addLine`. |
| `clear()` | CzyÄąâ€şci wszystkie wartoÄąâ€şci z wykresu. |
| `addValue(int value, ...)` | Dodaje nowÄ… wartoÄąâ€şÄ‡ do wykresu. JeÄąâ€şli liczba wartoÄąâ€şci przekroczy pojemnoÄąâ€şÄ‡, najstarsza jest usuwana. |
| `setLineWidth(int width)` | Ustawia gruboÄąâ€şÄ‡ linii wykresu. |
| `setCapacity(int capacity)` | Ustawia maksymalnÄ… liczbÄ™ wartoÄąâ€şci przechowywanych przez wykres. |
| `setTitle(const std::string& title)` | Ustawia tytuÄąâ€š wyÄąâ€şwietlany nad wykresem. |
| `setShowLabels(bool value)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza wyÄąâ€şwietlanie etykiet (wartoÄąâ€şÄ‡ min, max, aktualna). |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž uicreature.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `UICreature`, widÄąÄ˝etu interfejsu uÄąÄ˝ytkownika do wyÄąâ€şwietlania stworzeÄąâ€ž.
## Klasa `UICreature`
## Opis
Dziedziczy po `UIWidget`. UmoÄąÄ˝liwia renderowanie postaci (jej ubioru) w elementach UI, takich jak okno ekwipunku, battle list, czy okno wyboru stroju.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje postaÄ‡ za pomocÄ… `m_creature->drawOutfit(...)`. ObsÄąâ€šuguje automatyczne obracanie postaci, jeÄąâ€şli jest wÄąâ€šÄ…czone. |
| `setCreature(const CreaturePtr& creature)` | Ustawia stworzenie do wyÄąâ€şwietlenia. |
| `setFixedCreatureSize(bool fixed)` | Ustawia, czy rozmiar renderowanej postaci ma byÄ‡ staÄąâ€šy, czy skalowany do rozmiaru widÄąÄ˝etu. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubiĂłr do wyÄąâ€şwietlenia. JeÄąâ€şli nie ma przypisanego stworzenia, tworzy nowe. |
| `setAutoRotating(bool value)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza automatyczne obracanie siÄ™ postaci. |
| `setDirection(Otc::Direction direction)` | Ustawia staÄąâ€šy kierunek, w ktĂłrym postaÄ‡ jest zwrĂłcona. |
| `setScale(float scale)` | Ustawia skalÄ™ rysowania postaci. |
| `setAnimate(bool value)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza animacjÄ™ postaci. |
| `setCenter(bool value)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza centrowanie outfitu. |
| `setOldScaling(bool value)` | UÄąÄ˝ywa starego algorytmu skalowania. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.
- **`creature.h`**: Przechowuje i rysuje obiekt `Creature`.

---
# Ä‘Ĺşâ€śâ€ž thingtype.cpp
## OgĂłlny opis
Implementacja klasy `ThingType`, ktĂłra reprezentuje szablon dla wszystkich obiektĂłw w grze. Plik zawiera logikÄ™ serializacji, deserializacji, a przede wszystkim renderowania obiektĂłw danego typu.
## Klasa `ThingType`
## Metody
## Serializacja / Deserializacja
| Nazwa | Opis |
| --- | --- |
| `serialize(...)` | Zapisuje atrybuty `ThingType` do strumienia binarnego, zgodnie z formatem plikĂłw `.dat`. |
| `unserialize(...)` | Wczytuje atrybuty `ThingType` ze strumienia. Zawiera zÄąâ€šoÄąÄ˝onÄ… logikÄ™ do obsÄąâ€šugi rĂłÄąÄ˝nic w formatach `.dat` miÄ™dzy rĂłÄąÄ˝nymi wersjami klienta Tibii, mapujÄ…c stare atrybuty na nowe. |
| `unserializeOtml(...)` | Wczytuje dodatkowe, niestandardowe atrybuty z plikĂłw OTML, takie jak przezroczystoÄąâ€şÄ‡ czy niestandardowe obrazy. |
## Rysowanie
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | GÄąâ€šĂłwna metoda rysujÄ…ca. Pobiera teksturÄ™ dla danej fazy animacji, oblicza, ktĂłry jej fragment (`Rect`) odpowiada danemu wzorowi (pattern) i warstwie, a nastÄ™pnie dodaje go do kolejki rysowania. |
| `drawOutfit(...)` | Specjalna wersja do rysowania ubiorĂłw, ktĂłra zwraca parametry potrzebne do renderowania z dynamicznym kolorowaniem przez `DrawQueueItemOutfit`. |
| `drawWithShader(...)` | Wersja rysujÄ…ca z uÄąÄ˝yciem niestandardowego shadera. |
## ZarzÄ…dzanie teksturami
| Nazwa | Opis |
| --- | --- |
| `getTexture(int animationPhase)` | Zwraca teksturÄ™ dla danej fazy animacji. JeÄąâ€şli tekstura nie zostaÄąâ€ša jeszcze utworzona, generuje jÄ… "w locie": <br> 1. Tworzy duÄąÄ˝y obraz (atlas). <br> 2. SkÄąâ€šada go z pojedynczych sprite'Ăłw pobranych z `g_sprites`. <br> 3. Tworzy z niego obiekt `Texture` i przechowuje go w pamiÄ™ci podrÄ™cznej. <br> 4. Zapisuje rĂłwnieÄąÄ˝ prostokÄ…ty (`Rect`) i przesuniÄ™cia dla kaÄąÄ˝dej klatki na tej teksturze. |
| `unload()` | Zwalnia wygenerowane tekstury z pamiÄ™ci, aby oszczÄ™dzaÄ‡ zasoby. SÄ… one ponownie generowane przy nastÄ™pnym uÄąÄ˝yciu. |
| `getBestTextureDimension(...)` | Oblicza optymalny rozmiar tekstury-atlasu, aby pomieÄąâ€şciÄ‡ wszystkie klatki animacji. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`spritemanager.h`**: UÄąÄ˝ywa `g_sprites` do pobierania obrazĂłw pojedynczych sprite'Ăłw.
- **`game.h`**: Sprawdza `GameFeature`, co wpÄąâ€šywa na logikÄ™ deserializacji i animacji.
- **`lightview.h`**: Przekazuje `LightView` do dodawania Äąâ€şwiatÄąâ€ša, jeÄąâ€şli obiekt je emituje.
- **`framework/graphics/...`**: Intensywnie korzysta z klas `Texture`, `Image`, `Painter` i `DrawQueue`.

---
# Ä‘Ĺşâ€śâ€ž towns.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy klasy `Town` i `TownManager` do zarzÄ…dzania miastami w grze.
## Klasa `Town`
## Opis
Prosta klasa przechowujÄ…ca dane o pojedynczym mieÄąâ€şcie: ID, nazwÄ™ i pozycjÄ™ (zazwyczaj Äąâ€şwiÄ…tyni).
## Metody
| Nazwa | Opis |
| --- | --- |
| `setId(uint32 tid)` | Ustawia ID miasta. |
| `setName(const std::string& name)` | Ustawia nazwÄ™ miasta. |
| `setPos(const Position& pos)` | Ustawia pozycjÄ™ miasta. |
| `getId()` / `getName()` / `getPos()` | ZwracajÄ… odpowiednie wÄąâ€šaÄąâ€şciwoÄąâ€şci. |
## Klasa `TownManager`
## Opis
Singleton (`g_towns`) zarzÄ…dzajÄ…cy kolekcjÄ… wszystkich miast.
## Metody
| Nazwa | Opis |
| --- | --- |
| `addTown(const TownPtr& town)` | Dodaje miasto do listy. |
| `removeTown(uint32 townId)` | Usuwa miasto po ID. |
| `getTown(uint32 townId)` | Zwraca miasto po ID. |
| `getTownByName(std::string name)` | Zwraca miasto po nazwie. |
| `sort()` | Sortuje listÄ™ miast alfabetycznie. |
| `getTowns()` | Zwraca listÄ™ wszystkich miast. |
| `clear()` | CzyÄąâ€şci listÄ™ miast. |
## Zmienne globalne
- **`TownManager g_towns`**: Globalna instancja managera miast.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw, np. `TownPtr`, `Position`.

---
# Ä‘Ĺşâ€śâ€ž thingtype.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla klasy `ThingType`, ktĂłra jest szablonem dla wszystkich obiektĂłw w grze. Definiuje ona ich wspĂłlne, niezmienne wÄąâ€šaÄąâ€şciwoÄąâ€şci.
## Klasa `ThingType`
## Opis
Dziedziczy po `LuaObject`. Przechowuje dane wczytane z plikĂłw `.dat` i `.otml`, takie jak wymiary, wzory, animacje, atrybuty (np. czy jest blokujÄ…cy, czy Äąâ€şwieci). Wszystkie instancje `Thing` o tym samym ID wspĂłÄąâ€šdzielÄ… jeden obiekt `ThingType`.
## Typy wyliczeniowe
- **`ThingCategory`**: Kategorie obiektĂłw (przedmiot, stworzenie, etc.).
- **`ThingAttr`**: Atrybuty obiektu (np. `ThingAttrGround`, `ThingAttrNotWalkable`).
## Struktury
- **`MarketData`**: Dane rynkowe przedmiotu.
- **`Light`**: Parametry emitowanego Äąâ€şwiatÄąâ€ša.
- **`DrawOutfitParams`**: Parametry potrzebne do narysowania ubioru.
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(...)` | Wczytuje dane z binarnego formatu `.dat`. |
| `unserializeOtml(...)` | Wczytuje dodatkowe dane z formatu `.otml`. |
| `draw(...)` | Renderuje obiekt. |
| `drawOutfit(...)` | Specjalna funkcja do renderowania ubiorĂłw. |
| `getId()` | Zwraca ID klienta. |
| `getCategory()` | Zwraca kategoriÄ™. |
| `getSize()`, `getWidth()`, `getHeight()` | ZwracajÄ… wymiary w jednostkach pĂłl. |
| `getAnimationPhases()` | Zwraca liczbÄ™ klatek animacji. |
| `getAnimator()` | Zwraca animator, jeÄąâ€şli jest dostÄ™pny. |
| `hasAttr(ThingAttr attr)` | Sprawdza, czy obiekt posiada dany atrybut. |
| `isGround()`, `isNotWalkable()`, etc. | Funkcje pomocnicze sprawdzajÄ…ce konkretne atrybuty. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`animator.h`**: MoÄąÄ˝e posiadaÄ‡ `Animator` do zarzÄ…dzania animacjami.
- **`framework/graphics/...`**: UÄąÄ˝ywa `Texture`, `DrawQueue` do renderowania.
- **`framework/luaengine/luaobject.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž uicreature.cpp
## OgĂłlny opis
Implementacja `UICreature`, widÄąÄ˝etu do wyÄąâ€şwietlania stworzeÄąâ€ž w interfejsie uÄąÄ˝ytkownika.
## Klasa `UICreature`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widÄąÄ˝et. JeÄąâ€şli przypisano stworzenie (`m_creature`), wywoÄąâ€šuje jego metodÄ™ `drawOutfit`, aby narysowaÄ‡ jego wyglÄ…d w prostokÄ…cie widÄąÄ˝etu. ObsÄąâ€šuguje automatyczne obracanie postaci, jeÄąâ€şli opcja `m_autoRotating` jest wÄąâ€šÄ…czona. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubiĂłr do wyÄąâ€şwietlenia. JeÄąâ€şli widÄąÄ˝et nie ma jeszcze przypisanego obiektu `Creature`, tworzy nowÄ…, pustÄ… instancjÄ™. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `outfit-id`, `outfit-head`, `outfit-body` itp., i na ich podstawie konfiguruje wyÄąâ€şwietlany ubiĂłr. |
| `setCenter(bool value)` | Ustawia flagÄ™ centrowania w obiekcie `Outfit`, co wpÄąâ€šywa na sposĂłb jego rysowania. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`spritemanager.h`**: UÄąÄ˝ywane przez `Creature::drawOutfit`.
- **`framework/otml/otml.h`**: Do parsowania stylĂłw.
- **`framework/graphics/drawqueue.h`**: Do dodawania operacji rysowania.

---
# Ä‘Ĺşâ€śâ€ž thingtypemanager.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `ThingTypeManager`, singletonu zarzÄ…dzajÄ…cego wszystkimi typami obiektĂłw (`ThingType`) i przedmiotĂłw (`ItemType`).
## Klasa `ThingTypeManager`
## Opis
Centralne repozytorium dla definicji wszystkich obiektĂłw w grze. Odpowiada za wczytywanie plikĂłw `.dat`, `.otb` i `.xml`, ktĂłre zawierajÄ… te definicje, oraz za dostarczanie ich na ÄąÄ˝Ä…danie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizacja i zamykanie managera. |
| `check()` | Okresowo wywoÄąâ€šywana metoda, ktĂłra zwalnia z pamiÄ™ci tekstury nieuÄąÄ˝ywanych `ThingType`, aby oszczÄ™dzaÄ‡ zasoby. |
| `loadDat(...)`, `loadOtml(...)`, `loadOtb(...)`, `loadXml(...)` | Metody do wczytywania rĂłÄąÄ˝nych formatĂłw plikĂłw z danymi o obiektach. |
| `getThingType(id, category)` | Zwraca `ThingType` dla danego ID klienta i kategorii. |
| `getItemType(id)` | Zwraca `ItemType` dla danego ID serwera (OTB). |
| `findItemTypeByClientId(id)` | Wyszukuje `ItemType` po jego ID klienta. |
| `findItemTypeByName(name)` | Wyszukuje `ItemType` po nazwie. |
| `isDatLoaded()`, `isOtbLoaded()` | SprawdzajÄ…, czy odpowiednie pliki zostaÄąâ€šy zaÄąâ€šadowane. |
| `getDatSignature()` | Zwraca sygnaturÄ™ pliku `.dat`. |
## Zmienne globalne
- **`ThingTypeManager g_things`**: Globalna instancja managera.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`thingtype.h`**, **`itemtype.h`**: ZarzÄ…dza obiektami tych klas.
- Jest to jedna z najbardziej fundamentalnych klas w kliencie, uÄąÄ˝ywana przez niemal kaÄąÄ˝dy moduÄąâ€š, ktĂłry ma do czynienia z obiektami w grze.

---
# Ä‘Ĺşâ€śâ€ž uigraph.cpp
## OgĂłlny opis
Implementacja `UIGraph`, widÄąÄ˝etu do rysowania wykresĂłw liniowych.
## Klasa `UIGraph`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje wykres. Oblicza minimalnÄ… i maksymalnÄ… wartoÄąâ€şÄ‡ w widocznym zakresie, aby przeskalowaÄ‡ wykres do wysokoÄąâ€şci widÄąÄ˝etu. NastÄ™pnie tworzy listÄ™ punktĂłw i rysuje miÄ™dzy nimi linie za pomocÄ… `g_drawQueue->addLine`. Rysuje rĂłwnieÄąÄ˝ tytuÄąâ€š i etykiety (min, max, aktualna wartoÄąâ€şÄ‡), jeÄąâ€şli sÄ… wÄąâ€šÄ…czone. |
| `clear()` | CzyÄąâ€şci wszystkie dane z wykresu. |
| `addValue(int value, ...)` | Dodaje nowÄ… wartoÄąâ€şÄ‡ do kolejki `m_values`. JeÄąâ€şli kolejka przekroczy pojemnoÄąâ€şÄ‡ (`m_capacity`), najstarsza wartoÄąâ€şÄ‡ jest usuwana. Opcjonalnie ignoruje maÄąâ€še, powtarzajÄ…ce siÄ™ wartoÄąâ€şci, aby uniknÄ…Ä‡ "szumu" na wykresie. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `line-width`, `capacity`, `title`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/graphics/drawqueue.h`**: Do rysowania linii i tekstu.
- **`framework/otml/otml.h`**: Do parsowania stylĂłw.

---
# Ä‘Ĺşâ€śâ€ž uimap.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `UIMap`, widÄąÄ˝etu UI, ktĂłry jest odpowiedzialny za wyÄąâ€şwietlanie mapy gry.
## Klasa `UIMap`
## Opis
Dziedziczy po `UIWidget`. DziaÄąâ€ša jako "okno" na Äąâ€şwiat gry, wykorzystujÄ…c `MapView` do faktycznego renderowania. UmoÄąÄ˝liwia interakcjÄ™ z mapÄ…, takÄ… jak przesuwanie, przybliÄąÄ˝anie i pobieranie informacji o tym, co znajduje siÄ™ pod kursorem.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje mapÄ™ w trzech przejÄąâ€şciach (tÄąâ€šo, pierwszy plan, interfejs). |
| `movePixels(int x, int y)` | Przesuwa widok kamery o zadanÄ… liczbÄ™ pikseli. |
| `setZoom(int zoom)` / `zoomIn()` / `zoomOut()` | ZarzÄ…dza poziomem przybliÄąÄ˝enia mapy. |
| `followCreature(...)` | Ustawia kamerÄ™, aby podÄ…ÄąÄ˝aÄąâ€ša za stworzeniem. |
| `setCameraPosition(...)` | Ustawia kamerÄ™ na staÄąâ€šÄ… pozycjÄ™. |
| `getPosition(const Point& mousePos)` | Zwraca pozycjÄ™ na mapie (`Position`) odpowiadajÄ…cÄ… danym wspĂłÄąâ€šrzÄ™dnym myszy na widÄąÄ˝ecie. |
| `getTile(const Point& mousePos)` | Zwraca `Tile` pod kursorem. |
| `setKeepAspectRatio(bool enable)` | WÄąâ€šÄ…cza/wyÄąâ€šÄ…cza zachowanie staÄąâ€šych proporcji mapy. |
| `setVisibleDimension(...)` | Ustawia rozmiar widocznego obszaru mapy w polach. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`mapview.h`**: UÄąÄ˝ywa `MapView` do renderowania.
- **`tile.h`**: Metoda `getTile` zwraca obiekt `Tile`.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž uiminimap.cpp
## OgĂłlny opis
Implementacja `UIMinimap`, widÄąÄ˝etu interfejsu uÄąÄ˝ytkownika do wyÄąâ€şwietlania minimapy.
## Klasa `UIMinimap`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widÄąÄ˝et. WywoÄąâ€šuje `g_minimap.draw`, przekazujÄ…c prostokÄ…t widÄąÄ˝etu, pozycjÄ™ kamery i skalÄ™, aby narysowaÄ‡ odpowiedni fragment minimapy. |
| `setZoom(int zoom)` | Ustawia poziom przybliÄąÄ˝enia minimapy. WartoÄąâ€şÄ‡ zoom jest konwertowana na wspĂłÄąâ€šczynnik skali (`m_scale`). |
| `setCameraPosition(const Position& pos)` | Ustawia centralnÄ… pozycjÄ™, wokĂłÄąâ€š ktĂłrej rysowana jest minimapa. |
| `floorUp()` / `floorDown()` | Zmienia aktualnie wyÄąâ€şwietlane piÄ™tro. |
| `getTilePoint(...)` / `getTilePosition(...)` | KonwertujÄ… pozycjÄ™ na mapie na wspĂłÄąâ€šrzÄ™dne na widÄąÄ˝ecie i odwrotnie. |
| `anchorPosition(...)` / `fillPosition(...)` / `centerInPosition(...)` | Metody do przypinania innych widÄąÄ˝etĂłw do konkretnych pozycji na minimapie za pomocÄ… `UIMapAnchorLayout`. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `zoom`, `min-zoom`, `max-zoom`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`minimap.h`**: UÄąÄ˝ywa `g_minimap` do renderowania danych.
- **`uimapanchorlayout.h`**: Posiada `UIMapAnchorLayout` do zarzÄ…dzania przypiÄ™tymi widÄąÄ˝etami.
- **`game.h`**: DostÄ™p do globalnych obiektĂłw.

---
# Ä‘Ĺşâ€śâ€ž uiprogressrect.cpp
## OgĂłlny opis
Implementacja `UIProgressRect`, niestandardowego widÄąÄ˝etu, ktĂłry wizualizuje postÄ™p za pomocÄ… wypeÄąâ€šniajÄ…cego siÄ™ okrÄ™gu (lub kwadratu) w sposĂłb radialny.
## Klasa `UIProgressRect`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widÄąÄ˝et. Zamiast standardowego paska postÄ™pu, rysuje seriÄ™ trĂłjkÄ…tĂłw, ktĂłrych wierzchoÄąâ€ški rozchodzÄ… siÄ™ od Äąâ€şrodka prostokÄ…ta, tworzÄ…c efekt radialnego wypeÄąâ€šnienia. WypeÄąâ€šnienie jest podzielone na 4 Ä‡wiartki, a kaÄąÄ˝da z nich na dwa segmenty, co daje 8 krokĂłw animacji. |
| `setPercent(float percent)` | Ustawia procent wypeÄąâ€šnienia (od 0.0 do 100.0). |
| `onStyleApply(...)` | Parsuje atrybut `percent` z OTML. |
## Logika rysowania
WypeÄąâ€šnienie jest realizowane przez rysowanie trĂłjkÄ…tĂłw. KaÄąÄ˝dy trĂłjkÄ…t ma jeden wierzchoÄąâ€šek w Äąâ€şrodku prostokÄ…ta, a dwa pozostaÄąâ€še na jego krawÄ™dziach. W miarÄ™ wzrostu `m_percent`, kolejne trĂłjkÄ…ty sÄ… rysowane, tworzÄ…c iluzjÄ™ pÄąâ€šynnego, okrÄ™ÄąÄ˝nego wypeÄąâ€šnienia.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/otml/otml.h`**: Do parsowania stylĂłw.
- **`framework/graphics/graphics.h`**: Do operacji rysowania.

---
# Ä‘Ĺşâ€śâ€ž uimapanchorlayout.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy `UIPositionAnchor` i `UIMapAnchorLayout`. RozszerzajÄ… one standardowy system kotwic o moÄąÄ˝liwoÄąâ€şÄ‡ przypinania widÄąÄ˝etĂłw do dynamicznych pozycji na `UIMinimap`.
## Klasa `UIPositionAnchor`
## Opis
Dziedziczy po `UIAnchor`. Zamiast przypinaÄ‡ siÄ™ do krawÄ™dzi innego widÄąÄ˝etu, przypina siÄ™ do pozycji (`Position`) na mapie.
-   `m_hookedPosition`: Pozycja na mapie, do ktĂłrej kotwica jest przypiÄ™ta.
## Metody
-   **`getHookedPoint(...)`**: Nadpisana metoda, ktĂłra oblicza pozycjÄ™ na ekranie, pobierajÄ…c z `UIMinimap` prostokÄ…t odpowiadajÄ…cy `m_hookedPosition`.
## Klasa `UIMapAnchorLayout`
## Opis
Dziedziczy po `UIAnchorLayout`. Specjalizuje layout kotwic do pracy z `UIMinimap`.
## Metody
-   **`addPositionAnchor(...)`**: Dodaje kotwicÄ™ typu `UIPositionAnchor`.
-   **`centerInPosition(...)`**, **`fillPosition(...)`**: Funkcje pomocnicze do Äąâ€šatwego centrowania lub wypeÄąâ€šniania obszaru pola na mapie przez inny widÄąÄ˝et.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`framework/ui/uianchorlayout.h`**: Klasa bazowa.
- **`uiminimap.h`**: Layout jest przeznaczony do uÄąÄ˝ycia z `UIMinimap`.

---
# Ä‘Ĺşâ€śâ€ž uiminimap.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `UIMinimap`, widÄąÄ˝etu do wyÄąâ€şwietlania minimapy.
## Klasa `UIMinimap`
## Opis
Dziedziczy po `UIWidget`. Renderuje dane z `Minimap` i pozwala na interakcje, takie jak zmiana piÄ™tra czy przybliÄąÄ˝enia. Posiada rĂłwnieÄąÄ˝ `UIMapAnchorLayout` do pozycjonowania innych widÄąÄ˝etĂłw wzglÄ™dem pozycji na minimapie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `zoomIn()` / `zoomOut()` / `setZoom(int zoom)` | ZarzÄ…dzajÄ… poziomem przybliÄąÄ˝enia. |
| `setCameraPosition(const Position& pos)` | Ustawia pozycjÄ™, ktĂłra ma byÄ‡ w centrum minimapy. |
| `floorUp()` / `floorDown()` | Zmienia wyÄąâ€şwietlane piÄ™tro. |
| `getTilePoint(...)` / `getTileRect(...)` | ZwracajÄ… wspĂłÄąâ€šrzÄ™dne ekranowe dla danego pola na mapie. |
| `getTilePosition(...)` | Konwertuje wspĂłÄąâ€šrzÄ™dne ekranowe na pozycjÄ™ na mapie. |
| `anchorPosition(...)` | Przypina inny widÄąÄ˝et do pozycji na minimapie. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž uiprogressrect.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `UIProgressRect`, widÄąÄ˝etu do wyÄąâ€şwietlania paska postÄ™pu w formie radialnej.
## Klasa `UIProgressRect`
## Opis
Dziedziczy po `UIWidget`. Zamiast typowego paska, rysuje wypeÄąâ€šnienie w sposĂłb okrÄ™ÄąÄ˝ny.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje widÄąÄ˝et. |
| `setPercent(float percent)` | Ustawia procent postÄ™pu (0-100). |
| `getPercent()` | Zwraca aktualny procent. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž uisprite.cpp
## OgĂłlny opis
Implementacja `UISprite`, widÄąÄ˝etu do wyÄąâ€şwietlania pojedynczego sprite'a z plikĂłw `.spr`.
## Klasa `UISprite`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widÄąÄ˝et. JeÄąâ€şli `m_sprite` jest zaÄąâ€šadowany, rysuje go wewnÄ…trz prostokÄ…ta widÄąÄ˝etu z uwzglÄ™dnieniem paddingu. |
| `setSpriteId(uint32 id)` | Ustawia ID sprite'a do wyÄąâ€şwietlenia. Pobiera obraz z `g_sprites`, a nastÄ™pnie tworzy z niego teksturÄ™. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `sprite-id`, `sprite-color`. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`spritemanager.h`**: UÄąÄ˝ywa `g_sprites` do pobierania obrazĂłw sprite'Ăłw.
- **`framework/otml/otml.h`**: Do parsowania stylĂłw.
- **`framework/graphics/graphics.h`**: Do operacji rysowania i zarzÄ…dzania teksturami.

---
# Ä‘Ĺşâ€śâ€ž uisprite.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy dla `UISprite`, widÄąÄ˝etu do wyÄąâ€şwietlania pojedynczego sprite'a.
## Klasa `UISprite`
## Opis
Dziedziczy po `UIWidget`. Prosty widÄąÄ˝et, ktĂłrego jedynym celem jest wyÄąâ€şwietlenie obrazu sprite'a o danym ID.
## Metody
| Nazwa | Opis |
| --- | --- |
| `setSpriteId(uint32 id)` | Ustawia ID sprite'a do wyÄąâ€şwietlenia. |
| `getSpriteId()` | Zwraca ID sprite'a. |
| `setSpriteColor(Color color)` | Ustawia kolor, w jakim sprite ma byÄ‡ renderowany. |
| `hasSprite()` | Zwraca `true`, jeÄąâ€şli sprite jest zaÄąâ€šadowany. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`declarations.h`**: Definicje typĂłw.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# Ä‘Ĺşâ€śâ€ž walkmatrix.h
## OgĂłlny opis
Plik nagÄąâ€šĂłwkowy definiujÄ…cy klasÄ™ `WalkMatrix`, ktĂłra jest uÄąÄ˝ywana do Äąâ€şledzenia i zarzÄ…dzania predykcjami krokĂłw lokalnego gracza w nowym systemie chodzenia (`GameNewWalking`).
## Klasa `WalkMatrix`
## Opis
Jest to macierz 7x7, ktĂłra przechowuje wartoÄąâ€şci (liczniki lub ID predykcji) dla pĂłl w zasiÄ™gu 3x3 wokĂłÄąâ€š aktualnej pozycji gracza. SÄąâ€šuÄąÄ˝y do synchronizacji krokĂłw miÄ™dzy klientem a serwerem.
## Metody
| Nazwa | Opis |
| --- | --- |
| `updatePosition(const Position& newPos)` | Aktualizuje wewnÄ™trznÄ… pozycjÄ™ gracza i przesuwa zawartoÄąâ€şÄ‡ macierzy, aby odzwierciedliÄ‡ ruch. Stare, odlegÄąâ€še wartoÄąâ€şci sÄ… zerowane. |
| `inRange(const Position& pos2)` | Sprawdza, czy dana pozycja mieÄąâ€şci siÄ™ w zasiÄ™gu macierzy (3x3 wokĂłÄąâ€š gracza). |
| `update(const Position& pos2, int32_t value)` | Ustawia wartoÄąâ€şÄ‡ w macierzy dla danej pozycji. JeÄąâ€şli `value` nie jest podane, uÄąÄ˝ywa inkrementowanego licznika. Zwraca ustawionÄ… wartoÄąâ€şÄ‡, ktĂłra sÄąâ€šuÄąÄ˝y jako ID predykcji. |
| `get(const Position& pos2)` | Zwraca wartoÄąâ€şÄ‡ z macierzy dla danej pozycji. |
| `clear()` | Zeruje caÄąâ€šÄ… macierz. |
| `reset(uint32_t value)` | WypeÄąâ€šnia caÄąâ€šÄ… macierz danÄ… wartoÄąâ€şciÄ…. |
| `dump()` | Zwraca tekstowÄ… reprezentacjÄ™ macierzy do celĂłw debugowania. |
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`position.h`**: UÄąÄ˝ywa `Position` do operacji na wspĂłÄąâ€šrzÄ™dnych.
- **`localplayer.cpp`**: Obiekt `WalkMatrix` jest polem klasy `LocalPlayer` i jest uÄąÄ˝ywany w logice pre-walkingu.

---
# Ä‘Ĺşâ€śâ€ž protocolgameparse.cpp
## OgĂłlny opis
Plik ten zawiera implementacjÄ™ metod klasy `ProtocolGame` odpowiedzialnych za **parsowanie** pakietĂłw przychodzÄ…cych z serwera gry. Jest to serce logiki sieciowej po stronie klienta.
## Klasa `ProtocolGame`
## Metody
## `parseMessage(const InputMessagePtr& msg)`
GÄąâ€šĂłwna funkcja-dyspozytor. Odczytuje jednobajtowy kod operacyjny (opcode) z wiadomoÄąâ€şci, a nastÄ™pnie wywoÄąâ€šuje odpowiedniÄ… metodÄ™ `parse...` do przetworzenia reszty pakietu. ObsÄąâ€šuguje rĂłwnieÄąÄ˝ niestandardowe opkody i przekazywanie ich do Lua.
## Metody `parse...`
KaÄąÄ˝da metoda `parse...` jest odpowiedzialna za odczytanie danych z `InputMessage` dla konkretnego opkodu i zaktualizowanie stanu gry. PrzykÄąâ€šady:
- **`parseMapDescription(...)`**: Parsuje peÄąâ€šny opis widocznego obszaru mapy, tworzÄ…c pola i obiekty.
- **`parseTileAddThing(...)`**: Dodaje nowy obiekt na mapÄ™.
- **`parseCreatureMove(...)`**: Aktualizuje pozycjÄ™ stworzenia na mapie.
- **`parseCreatureHealth(...)`**: Aktualizuje procent ÄąÄ˝ycia stworzenia.
- **`parseTalk(...)`**: Przetwarza wiadomoÄąâ€şÄ‡ czatu i przekazuje jÄ… do `g_game`.
- **`parseOpenContainer(...)`**: Tworzy nowy kontener i wypeÄąâ€šnia go przedmiotami.
- **`parsePlayerStats(...)`**: Aktualizuje statystyki lokalnego gracza.
- **`parseCancelWalk(...)`**: Informuje `g_game` o anulowaniu kroku.
## Metody pomocnicze `get...`
- **`getThing(...)`**, **`getItem(...)`**, **`getCreature(...)`**, **`getPosition(...)`**: Funkcje pomocnicze, ktĂłre odczytujÄ… zÄąâ€šoÄąÄ˝one typy danych (jak `Item` czy `Creature`) z `InputMessage`, uwzglÄ™dniajÄ…c rĂłÄąÄ˝nice w formacie zaleÄąÄ˝ne od `GameFeature`. `getCreature`, na przykÄąâ€šad, decyduje, czy stworzyÄ‡ nowy obiekt `Creature`, czy zaktualizowaÄ‡ istniejÄ…cy.
## ZaleÄąÄ˝noÄąâ€şci i powiÄ…zania
- **`game.h`**, **`map.h`**, **`localplayer.h`**: ÄąĹˇciÄąâ€şle wspĂłÄąâ€špracuje z tymi klasami, wywoÄąâ€šujÄ…c ich metody w celu aktualizacji stanu gry.
- **`thingtypemanager.h`**: UÄąÄ˝ywa `g_things` do weryfikacji ID przedmiotĂłw i efektĂłw.
- **`luavaluecasts_client.h`**: UÄąÄ˝ywane do przekazywania zÄąâ€šoÄąÄ˝onych obiektĂłw do Lua.
- **`protocolcodes.h`**: UÄąÄ˝ywa zdefiniowanych tam kodĂłw operacyjnych.

---
# Ä‘Ĺşâ€śâ€ Spis treÄąâ€şci

- [Ä‘Ĺşâ€śâ€ž animatedtext.cpp](#-animatedtextcpp)
  - [Klasa `AnimatedText`](#-klasa-animatedtext)
- [Ä‘Ĺşâ€śâ€ž houses.h](#-housesh)
  - [Klasa `House`](#-klasa-house)
  - [Klasa `HouseManager`](#-klasa-housemanager)
- [Ä‘Ĺşâ€śâ€ž animatedtext.h](#-animatedtexth)
  - [Klasa `AnimatedText`](#-klasa-animatedtext-1)
- [Ä‘Ĺşâ€śâ€ž animator.h](#-animatorh)
  - [Klasa `Animator`](#-klasa-animator)
- [Ä‘Ĺşâ€śâ€ž animator.cpp](#-animatorcpp)
  - [Klasa `Animator`](#-klasa-animator-1)
- [Ä‘Ĺşâ€śâ€ž client.cpp](#-clientcpp)
  - [Klasa `Client`](#-klasa-client)
- [Ä‘Ĺşâ€śâ€ž client.h](#-clienth)
  - [Klasa `Client`](#-klasa-client-1)
- [Ä‘Ĺşâ€śâ€ž CMakeLists.txt](#-cmakeliststxt)
- [Ä‘Ĺşâ€śâ€ž const.h](#-consth)
  - [Namespace `Otc`](#-namespace-otc)
- [Ä‘Ĺşâ€śâ€ž container.cpp](#-containercpp)
  - [Klasa `Container`](#-klasa-container)
- [Ä‘Ĺşâ€śâ€ž creature.cpp](#-creaturecpp)
  - [Klasa `Creature`](#-klasa-creature)
- [Ä‘Ĺşâ€śâ€ž container.h](#-containerh)
  - [Klasa `Container`](#-klasa-container-1)
- [Ä‘Ĺşâ€śâ€ž creature.h](#-creatureh)
  - [Klasa `Creature`](#-klasa-creature-1)
  - [Klasa `Npc`](#-klasa-npc)
  - [Klasa `Monster`](#-klasa-monster)
- [Ä‘Ĺşâ€śâ€ž creatures.h](#-creaturesh)
  - [Klasa `Spawn`](#-klasa-spawn)
  - [Klasa `CreatureType`](#-klasa-creaturetype)
  - [Klasa `CreatureManager`](#-klasa-creaturemanager)
- [Ä‘Ĺşâ€śâ€ž declarations.h](#-declarationsh)
- [Ä‘Ĺşâ€śâ€ž creatures.cpp](#-creaturescpp)
  - [Klasa `Spawn`](#-klasa-spawn-1)
  - [Klasa `CreatureType`](#-klasa-creaturetype-1)
  - [Klasa `CreatureManager`](#-klasa-creaturemanager-1)
- [Ä‘Ĺşâ€śâ€ž effect.cpp](#-effectcpp)
  - [Klasa `Effect`](#-klasa-effect)
- [Ä‘Ĺşâ€śâ€ž global.h](#-globalh)
- [Ä‘Ĺşâ€śâ€ž effect.h](#-effecth)
  - [Klasa `Effect`](#-klasa-effect-1)
- [Ä‘Ĺşâ€śâ€ž healthbars.cpp](#-healthbarscpp)
  - [Klasa `HealthBars`](#-klasa-healthbars)
  - [Klasa `HealthBar`](#-klasa-healthbar)
- [Ä‘Ĺşâ€śâ€ž game.h](#-gameh)
  - [Klasa `Game`](#-klasa-game)
- [Ä‘Ĺşâ€śâ€ž healthbars.h](#-healthbarsh)
  - [Klasa `HealthBar`](#-klasa-healthbar-1)
  - [Klasa `HealthBars`](#-klasa-healthbars-1)
- [Ä‘Ĺşâ€śâ€ž houses.cpp](#-housescpp)
  - [Klasa `House`](#-klasa-house-1)
  - [Klasa `HouseManager`](#-klasa-housemanager-1)
- [Ä‘Ĺşâ€śâ€ž item.cpp](#-itemcpp)
  - [Klasa `Item`](#-klasa-item)
- [Ä‘Ĺşâ€śâ€ž itemtype.cpp](#-itemtypecpp)
  - [Klasa `ItemType`](#-klasa-itemtype)
- [Ä‘Ĺşâ€śâ€ž item.h](#-itemh)
  - [Klasa `Item`](#-klasa-item-1)
- [Ä‘Ĺşâ€śâ€ž itemtype.h](#-itemtypeh)
  - [Klasa `ItemType`](#-klasa-itemtype-1)
- [Ä‘Ĺşâ€śâ€ž lightview.cpp](#-lightviewcpp)
  - [Klasa `LightView`](#-klasa-lightview)
- [Ä‘Ĺşâ€śâ€ž lightview.h](#-lightviewh)
  - [Klasa `LightView`](#-klasa-lightview-1)
- [Ä‘Ĺşâ€śâ€ž localplayer.cpp](#-localplayercpp)
  - [Klasa `LocalPlayer`](#-klasa-localplayer)
- [Ä‘Ĺşâ€śâ€ž map.cpp](#-mapcpp)
  - [Klasa `Map`](#-klasa-map)
- [Ä‘Ĺşâ€śâ€ž map.h](#-maph)
  - [Klasa `Map`](#-klasa-map-1)
- [Ä‘Ĺşâ€śâ€ž luavaluecasts_client.h](#-luavaluecasts_clienth)
- [Ä‘Ĺşâ€śâ€ž mapio.cpp](#-mapiocpp)
  - [Klasa `Map`](#-klasa-map-2)
- [Ä‘Ĺşâ€śâ€ž luavaluecasts_client.cpp](#-luavaluecasts_clientcpp)
- [Ä‘Ĺşâ€śâ€ž mapview.cpp](#-mapviewcpp)
  - [Klasa `MapView`](#-klasa-mapview)
- [Ä‘Ĺşâ€śâ€ž mapview.h](#-mapviewh)
  - [Klasa `MapView`](#-klasa-mapview-1)
- [Ä‘Ĺşâ€śâ€ž minimap.h](#-minimaph)
  - [Klasa `MinimapBlock`](#-klasa-minimapblock)
  - [Klasa `Minimap`](#-klasa-minimap)
- [Ä‘Ĺşâ€śâ€ž missile.cpp](#-missilecpp)
  - [Klasa `Missile`](#-klasa-missile)
- [Ä‘Ĺşâ€śâ€ž missile.h](#-missileh)
  - [Klasa `Missile`](#-klasa-missile-1)
- [Ä‘Ĺşâ€śâ€ž outfit.cpp](#-outfitcpp)
  - [Klasa `Outfit`](#-klasa-outfit)
- [Ä‘Ĺşâ€śâ€ž outfit.h](#-outfith)
  - [Klasa `Outfit`](#-klasa-outfit-1)
- [Ä‘Ĺşâ€śâ€ž player.cpp](#-playercpp)
  - [Klasa `Player`](#-klasa-player)
- [Ä‘Ĺşâ€śâ€ž player.h](#-playerh)
  - [Klasa `Player`](#-klasa-player-1)
- [Ä‘Ĺşâ€śâ€ž protocolcodes.cpp](#-protocolcodescpp)
  - [Namespace `Proto`](#-namespace-proto)
- [Ä‘Ĺşâ€śâ€ž minimap.cpp](#-minimapcpp)
  - [Klasa `MinimapBlock`](#-klasa-minimapblock-1)
  - [Klasa `Minimap`](#-klasa-minimap-1)
- [Ä‘Ĺşâ€śâ€ž position.h](#-positionh)
  - [Struktura `Position`](#-struktura-position)
  - [Struktura `PositionHasher`](#-struktura-positionhasher)
- [Ä‘Ĺşâ€śâ€ž protocolcodes.h](#-protocolcodesh)
  - [Namespace `Proto`](#-namespace-proto-1)
- [Ä‘Ĺşâ€śâ€ž protocolgame.cpp](#-protocolgamecpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame)
- [Ä‘Ĺşâ€śâ€ž protocolgame.h](#-protocolgameh)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-1)
- [Ä‘Ĺşâ€śâ€ž spritemanager.cpp](#-spritemanagercpp)
  - [Klasa `SpriteManager`](#-klasa-spritemanager)
- [Ä‘Ĺşâ€śâ€ž protocolgamesend.cpp](#-protocolgamesendcpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-2)
- [Ä‘Ĺşâ€śâ€ž localplayer.h](#-localplayerh)
  - [Klasa `LocalPlayer`](#-klasa-localplayer-1)
- [Ä‘Ĺşâ€śâ€ž towns.cpp](#-townscpp)
  - [Klasa `Town`](#-klasa-town)
  - [Klasa `TownManager`](#-klasa-townmanager)
- [Ä‘Ĺşâ€śâ€ž spritemanager.h](#-spritemanagerh)
  - [Klasa `SpriteManager`](#-klasa-spritemanager-1)
- [Ä‘Ĺşâ€śâ€ž tile.cpp](#-tilecpp)
  - [Klasa `Tile`](#-klasa-tile)
- [Ä‘Ĺşâ€śâ€ž statictext.h](#-statictexth)
  - [Klasa `StaticText`](#-klasa-statictext)
- [Ä‘Ĺşâ€śâ€ž uimapanchorlayout.cpp](#-uimapanchorlayoutcpp)
  - [Klasa `UIPositionAnchor`](#-klasa-uipositionanchor)
  - [Klasa `UIMapAnchorLayout`](#-klasa-uimapanchorlayout)
- [Ä‘Ĺşâ€śâ€ž thing.h](#-thingh)
  - [Klasa `Thing`](#-klasa-thing)
- [Ä‘Ĺşâ€śâ€ž uiitem.h](#-uiitemh)
  - [Klasa `UIItem`](#-klasa-uiitem)
- [Ä‘Ĺşâ€śâ€ž thing.cpp](#-thingcpp)
  - [Klasa `Thing`](#-klasa-thing-1)
- [Ä‘Ĺşâ€śâ€ž uimap.cpp](#-uimapcpp)
  - [Klasa `UIMap`](#-klasa-uimap)
- [Ä‘Ĺşâ€śâ€ž thingstype.h](#-thingstypeh)
  - [Klasa `ThingsType`](#-klasa-thingstype)
- [Ä‘Ĺşâ€śâ€ž uigraph.h](#-uigraphh)
  - [Klasa `UIGraph`](#-klasa-uigraph)
- [Ä‘Ĺşâ€śâ€ž uicreature.h](#-uicreatureh)
  - [Klasa `UICreature`](#-klasa-uicreature)
- [Ä‘Ĺşâ€śâ€ž thingtype.cpp](#-thingtypecpp)
  - [Klasa `ThingType`](#-klasa-thingtype)
- [Ä‘Ĺşâ€śâ€ž towns.h](#-townsh)
  - [Klasa `Town`](#-klasa-town-1)
  - [Klasa `TownManager`](#-klasa-townmanager-1)
- [Ä‘Ĺşâ€śâ€ž thingtype.h](#-thingtypeh)
  - [Klasa `ThingType`](#-klasa-thingtype-1)
- [Ä‘Ĺşâ€śâ€ž uicreature.cpp](#-uicreaturecpp)
  - [Klasa `UICreature`](#-klasa-uicreature-1)
- [Ä‘Ĺşâ€śâ€ž thingtypemanager.h](#-thingtypemanagerh)
  - [Klasa `ThingTypeManager`](#-klasa-thingtypemanager)
- [Ä‘Ĺşâ€śâ€ž thingtypemanager.cpp](#-thingtypemanagercpp)
  - [Klasa `ThingTypeManager`](#-klasa-thingtypemanager-1)
- [Ä‘Ĺşâ€śâ€ž tile.h](#-tileh)
  - [Klasa `Tile`](#-klasa-tile-1)
- [Ä‘Ĺşâ€śâ€ž uimap.h](#-uimaph)
  - [Klasa `UIMap`](#-klasa-uimap-1)
- [Ä‘Ĺşâ€śâ€ž uiminimap.cpp](#-uiminimappp)
  - [Klasa `UIMinimap`](#-klasa-uiminimap)
- [Ä‘Ĺşâ€śâ€ž uiprogressrect.cpp](#-uiprogressrectcpp)
  - [Klasa `UIProgressRect`](#-klasa-uiprogressrect)
- [Ä‘Ĺşâ€śâ€ž uimapanchorlayout.h](#-uimapanchorlayouth)
  - [Klasa `UIPositionAnchor`](#-klasa-uipositionanchor-1)
  - [Klasa `UIMapAnchorLayout`](#-klasa-uimapanchorlayout-1)
- [Ä‘Ĺşâ€śâ€ž uiminimap.h](#-uiminimaph)
  - [Klasa `UIMinimap`](#-klasa-uiminimap-1)
- [Ä‘Ĺşâ€śâ€ž game.cpp](#-gamecpp)
  - [Klasa `Game`](#-klasa-game-1)
- [Ä‘Ĺşâ€śâ€ž uiprogressrect.h](#-uiprogressrecth)
  - [Klasa `UIProgressRect`](#-klasa-uiprogressrect-1)
- [Ä‘Ĺşâ€śâ€ž uisprite.cpp](#-uispritecpp)
  - [Klasa `UISprite`](#-klasa-uisprite)
- [Ä‘Ĺşâ€śâ€ž uisprite.h](#-uispriteh)
  - [Klasa `UISprite`](#-klasa-uisprite-1)
- [Ä‘Ĺşâ€śâ€ž walkmatrix.h](#-walkmatrixh)
  - [Klasa `WalkMatrix`](#-klasa-walkmatrix)
- [Ä‘Ĺşâ€śâ€ž protocolgameparse.cpp](#-protocolgameparsecpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-3)
- [Ä‘Ĺşâ€śâ€ž luafunctions_client.cpp](#-luafunctions_clientcpp)
# Ä‘Ĺşâ€ťĹ¤ Indeks funkcji/metod
- `AnimatedText::AnimatedText()`
- `AnimatedText::drawText(const Point&, const Rect&)`
- `AnimatedText::merge(const AnimatedTextPtr&)`
- `AnimatedText::onAppear()`
- `AnimatedText::setColor(int)`
- `AnimatedText::setFont(const std::string&)`
- `AnimatedText::setText(const std::string&)`
- `Animator::Animator()`
- `Animator::calculateSynchronous()`
- `Animator::getLoopPhase()`
- `Animator::getPhase()`
- `Animator::getPhaseAt(Timer&, int)`
- `Animator::getPhaseDuration(int)`
- `Animator::getPingPongPhase()`
- `Animator::getStartPhase()`
- `Animator::getTotalDuration()`
- `Animator::resetAnimation()`
- `Animator::serialize(const FileStreamPtr&)`
- `Animator::setPhase(int)`
- `Animator::unserialize(int, const FileStreamPtr&)`
- `Client::init(std::vector<std::string>&)`
- `Client::registerLuaFunctions()`
- `Client::terminate()`
- `Container::Container(...)`
- `Container::findItemById(uint, int)`
- `Container::getItem(int)`
- `Container::onAddItem(const ItemPtr&, int)`
- `Container::onAddItems(const std::vector<ItemPtr>&)`
- `Container::onClose()`
- `Container::onOpen(const ContainerPtr&)`
- `Container::onRemoveItem(int, const ItemPtr&)`
- `Container::onUpdateItem(int, const ItemPtr&)`
- `Container::updateItemsPositions()`
- `Creature::addBottomWidget(const UIWidgetPtr&)`
- `Creature::addDirectionalWidget(const UIWidgetPtr&)`
- `Creature::addTopWidget(const UIWidgetPtr&)`
- `Creature::canShoot(int)`
- `Creature::Creature()`
- `Creature::draw(...)`
- `Creature::drawInformation(...)`
- `Creature::drawOutfit(const Rect&, Otc::Direction, const Color&, bool, bool, bool)`
- `Creature::getDisplacement()`
- `Creature::getStepDuration(...)`
- `Creature::getThingType()`
- `Creature::jump(int, int)`
- `Creature::nextWalkUpdate()`
- `Creature::onAppear()`
- `Creature::onDeath()`
- `Creature::onDisappear()`
- `Creature::onPositionChange(const Position&, const Position&)`
- `Creature::rawGetThingType()`
- `Creature::setHealthPercent(uint8)`
- `Creature::setOutfit(const Outfit&)`
- `Creature::setSpeed(uint16)`
- `Creature::stopWalk()`
- `Creature::terminateWalk()`
- `Creature::turn(Otc::Direction)`
- `Creature::updateJump()`
- `Creature::updateWalk()`
- `Creature::updateWalkAnimation(...)`
- `Creature::updateWalkOffset(...)`
- `Creature::updateWalkingTile()`
- `Creature::walk(const Position&, const Position&)`
- `CreatureManager::addSpawn(const Position&, int)`
- `CreatureManager::deleteSpawn(const SpawnPtr&)`
- `CreatureManager::getCreatureByName(std::string)`
- `CreatureManager::getCreatureByLook(int)`
- `CreatureManager::getSpawn(const Position&)`
- `CreatureManager::getSpawnForPlacePos(const Position&)`
- `CreatureManager::internalLoadCreatureBuffer(...)`
- `CreatureManager::loadMonsters(const std::string&)`
- `CreatureManager::loadNpcs(const std::string&)`
- `CreatureManager::loadSingleCreature(const std::string&)`
- `CreatureManager::loadSpawns(const std::string&)`
- `CreatureManager::saveSpawns(const std::string&)`
- `CreatureManager::terminate()`
- `CreatureType::cast()`
- `Effect::draw(...)`
- `Effect::getId()`
- `Effect::onAppear()`
- `Effect::setId(uint32)`
- `Game::autoWalk(const std::vector<Otc::Direction>&, Position)`
- `Game::cancelLogin()`
- `Game::forceLogout()`
- `Game::init()`
- `Game::loginWorld(...)`
- `Game::processAttackCancel(uint)`
- `Game::processCloseContainer(int)`
- `Game::processConnectionError(const boost::system::error_code&)`
- `Game::processContainerAddItem(int, const ItemPtr&, int)`
- `Game::processContainerRemoveItem(int, int, const ItemPtr&)`
- `Game::processContainerUpdateItem(int, int, const ItemPtr&)`
- `Game::processDisconnect()`
- `Game::processEnterGame()`
- `Game::processGameEnd()`
- `Game::processGameStart()`
- `Game::processInventoryChange(int, const ItemPtr&)`
- `Game::processLogin()`
- `Game::processLoginError(const std::string&)`
- `Game::processOpenContainer(...)`
- `Game::processPendingGame()`
- `Game::processPing()`
- `Game::processPingBack()`
- `Game::processTalk(...)`
- `Game::processTextMessage(Otc::MessageMode, const std::string&)`
- `Game::processWalkCancel(Otc::Direction)`
- `Game::resetGameStates()`
- `Game::safeLogout()`
- `Game::setAttackingCreature(const CreaturePtr&)`
- `Game::setFollowingCreature(const CreaturePtr&)`
- `Game::setProtocolVersion(int)`
- `Game::stop()`
- `Game::terminate()`
- `Game::walk(Otc::Direction, bool)`
- `HealthBars::addHealthBackground(...)`
- `HealthBars::addManaBackground(...)`
- `HealthBars::init()`
- `HealthBars::terminate()`
- `House::addDoor(const ItemPtr&)`
- `House::load(const TiXmlElement*)`
- `House::removeDoorById(uint32)`
- `House::save(TiXmlElement*)`
- `House::setTile(const TilePtr&)`
- `HouseManager::addHouse(const HousePtr&)`
- `HouseManager::filterHouses(uint32)`
- `HouseManager::getHouse(uint32)`
- `HouseManager::getHouseByName(std::string)`
- `HouseManager::load(const std::string&)`
- `HouseManager::removeHouse(uint32)`
- `HouseManager::save(const std::string&)`
- `HouseManager::sort()`
- `Item::calculateAnimationPhase(bool)`
- `Item::calculatePatterns(int&, int&, int&)`
- `Item::clone()`
- `Item::create(int, int)`
- `Item::createFromOtb(int)`
- `Item::draw(const Point&, bool, LightView*)`
- `Item::draw(const Rect&, bool)`
- `Item::getCount()`
- `Item::getSubType()`
- `Item::getThingType()`
- `Item::rawGetThingType()`
- `Item::serializeItem(const OutputBinaryTreePtr&)`
- `Item::setId(uint32)`
- `Item::setOtbId(uint16)`
- `Item::unserializeItem(const BinaryTreePtr&)`
- `ItemType::unserialize(const BinaryTreePtr&)`
- `LightView::addLight(const Point&, uint8_t, uint8_t)`
- `LightView::draw()`
- `LocalPlayer::autoWalk(Position, bool)`
- `LocalPlayer::canWalk(Otc::Direction, bool)`
- `LocalPlayer::cancelNewWalk(Otc::Direction)`
- `LocalPlayer::cancelWalk(Otc::Direction)`
- `LocalPlayer::lockWalk(int)`
- `LocalPlayer::onPositionChange(const Position&, const Position&)`
- `LocalPlayer::preWalk(Otc::Direction)`
- `LocalPlayer::predictiveCancelWalk(const Position&, uint32_t, Otc::Direction)`
- `LocalPlayer::setHealth(double, double)`
- `LocalPlayer::stopAutoWalk()`
- `LocalPlayer::stopWalk()`
- `LocalPlayer::terminateWalk()`
- `LocalPlayer::updateWalk()`
- `LocalPlayer::updateWalkOffset(...)`
- `LocalPlayer::walk(const Position&, const Position&)`
- `Map::addThing(const ThingPtr&, const Position&, int)`
- `Map::clean()`
- `Map::cleanDynamicThings()`
- `Map::createTile(const Position&)`
- `Map::findPath(...)`
- `Map::getOrCreateTile(const Position&)`
- `Map::getSpectators(...)`
- `Map::getTile(const Position&)`
- `Map::init()`
- `Map::isAwareOfPosition(const Position&, bool)`
- `Map::loadOtbm(const std::string&)`
- `Map::notificateTileUpdate(const Position&, bool)`
- `Map::removeThing(const ThingPtr&)`
- `Map::saveOtbm(const std::string&)`
- `Map::setCentralPosition(const Position&)`
- `Map::terminate()`
- `MapView::calcFirstVisibleFloor(bool)`
- `MapView::calcLastVisibleFloor()`
- `MapView::drawMapBackground(const Rect&, const TilePtr&)`
- `MapView::drawMapForeground(const Rect&)`
- `MapView::getCameraPosition()`
- `MapView::getPosition(const Point&, const Size&)`
- `MapView::getTile(const Point&)`
- `MapView::onMapCenterChange(const Position&)`
- `MapView::onTileUpdate(const Position&)`
- `MapView::updateVisibleTilesCache()`
- `Minimap::clean()`
- `Minimap::draw(...)`
- `Minimap::getTile(const Position&)`
- `Minimap::loadOtmm(const std::string&)`
- `Minimap::saveOtmm(const std::string&)`
- `Minimap::updateTile(const Position&, const TilePtr&)`
- `MinimapBlock::update()`
- `MinimapBlock::updateTile(int, int, const MinimapTile&)`
- `Missile::draw(const Point&, bool, LightView*)`
- `Missile::setPath(const Position&, const Position&)`
- `Outfit::draw(Point, Otc::Direction, uint, bool, LightView*, bool)`
- `Outfit::draw(const Rect&, Otc::Direction, uint, bool, bool, bool)`
- `Outfit::resetClothes()`
- `Player::isPlayer()`
- `Position::getDirectionFromPositions(const Position&, const Position&)`
- `Position::translatedToDirection(Otc::Direction)`
- `Proto::buildMessageModesMap(int)`
- `Proto::translateMessageModeFromServer(uint8)`
- `Proto::translateMessageModeToServer(Otc::MessageMode)`
- `ProtocolGame::onConnect()`
- `ProtocolGame::onError(const boost::system::error_code&)`
- `ProtocolGame::onRecv(const InputMessagePtr&)`
- `ProtocolGame::parseMessage(const InputMessagePtr&)`
- `ProtocolGame::send(const OutputMessagePtr&, bool)`
- `ProtocolGame::sendLoginPacket(...)`
- `SpriteManager::getSpriteImage(int)`
- `SpriteManager::loadSpr(std::string)`
- `SpriteManager::terminate()`
- `SpriteManager::unload()`
- `StaticText::addMessage(const std::string&, Otc::MessageMode, const std::string&)`
- `StaticText::compose()`
- `StaticText::drawText(const Point&, const Rect&)`
- `StaticText::scheduleUpdate()`
- `StaticText::update()`
- `Thing::getStackPos()`
- `Thing::getStackPriority()`
- `Thing::getTile()`
- `Thing::setPosition(const Position&)`
- `ThingType::draw(const Point&, ...)`
- `ThingType::getTexture(int)`
- `ThingType::serialize(const FileStreamPtr&)`
- `ThingType::unserialize(uint16, ThingCategory, const FileStreamPtr&)`
- `ThingTypeManager::addItemType(const ItemTypePtr&)`
- `ThingTypeManager::check()`
- `ThingTypeManager::findItemTypeByClientId(uint16)`
- `ThingTypeManager::getItemType(uint16)`
- `ThingTypeManager::getThingType(uint16, ThingCategory)`
- `ThingTypeManager::init()`
- `ThingTypeManager::loadDat(std::string)`
- `ThingTypeManager::loadOtb(const std::string&)`
- `ThingTypeManager::loadXml(const std::string&)`
- `ThingTypeManager::parseItemType(uint16, TiXmlElement*)`
- `ThingTypeManager::terminate()`
- `Tile::addThing(const ThingPtr&, int)`
- `Tile::clean()`
- `Tile::drawBottom(const Point&, LightView*)`
- `Tile::drawCreatures(const Point&, LightView*)`
- `Tile::drawGround(const Point&, LightView*)`
- `Tile::drawTop(const Point&, LightView*)`
- `Tile::getGround()`
- `Tile::getItems()`
- `Tile::getTopCreature()`
- `Tile::getTopLookThing()`
- `Tile::getTopUseThing()`
- `Tile::isWalkable(bool)`
- `Tile::removeThing(ThingPtr)`
- `TownManager::addTown(const TownPtr&)`
- `TownManager::getTown(uint32)`
- `TownManager::sort()`
- `UICreature::drawSelf(Fw::DrawPane)`
- `UICreature::setOutfit(const Outfit&)`
- `UIGraph::addValue(int, bool)`
- `UIGraph::drawSelf(Fw::DrawPane)`
- `UIItem::drawSelf(Fw::DrawPane)`
- `UIItem::setItem(const ItemPtr&)`
- `UIItem::setItemId(int)`
- `UIMap::drawSelf(Fw::DrawPane)`
- `UIMap::getPosition(const Point&)`
- `UIMap::getTile(const Point&)`
- `UIMap::setZoom(int)`
- `UIMap::updateVisibleDimension()`
- `UIMapAnchorLayout::addPositionAnchor(...)`
- `UIMinimap::drawSelf(Fw::DrawPane)`
- `UIMinimap::setCameraPosition(const Position&)`
- `UIMinimap::setZoom(int)`
- `UIPositionAnchor::getHookedPoint(const UIWidgetPtr&, const UIWidgetPtr&)`
- `UIProgressRect::drawSelf(Fw::DrawPane)`
- `UIProgressRect::setPercent(float)`
- `UISprite::drawSelf(Fw::DrawPane)`
- `UISprite::setSpriteId(uint32)`
- `WalkMatrix::update(const Position&, int32_t)`
- `WalkMatrix::updatePosition(const Position&)`
# Ä‘ĹşÂ§Â­ Mapa zaleÄąÄ˝noÄąâ€şci
PoniÄąÄ˝szy diagram przedstawia gÄąâ€šĂłwne zaleÄąÄ˝noÄąâ€şci i przepÄąâ€šyw informacji miÄ™dzy kluczowymi moduÄąâ€šami systemu.

`$fenceInfo
graph TD
    subgraph "Aplikacja i UI"
        Client[Client] -->|inicjalizuje| Game
        Client -->|inicjalizuje| Map
        Client -->|inicjalizuje| ThingTypeManager
        UIMap[UIMap] -->|renderuje| MapView
        MapView -->|odczytuje dane| Map
        UICreature[UICreature] -->|wyÄąâ€şwietla| Creature
        UIItem[UIItem] -->|wyÄąâ€şwietla| Item
    end

    subgraph "Logika Gry"
        Game[Game] -->|wysyÄąâ€ša akcje| ProtocolGame
        Game -->|zarzÄ…dza| LocalPlayer
        Game -->|zarzÄ…dza| Map
        LocalPlayer[LocalPlayer] -->|dziedziczy| Player
        Player -->|dziedziczy| Creature
        Creature -->|dziedziczy| Thing
        Item -->|dziedziczy| Thing
        Thing -->|ma| ThingType
    end

    subgraph "SieÄ‡"
        ProtocolGame[ProtocolGame] -->|parsuje pakiety| Game
        ProtocolGame -->|wysyÄąâ€ša pakiety| TCPSocket
    end

    subgraph "Dane i Zasoby"
        ThingTypeManager[ThingTypeManager] -->|wczytuje| DAT["things.dat"]
        ThingTypeManager -->|wczytuje| OTB["items.otb"]
        SpriteManager[SpriteManager] -->|wczytuje| SPR["sprites.spr"]
        Map -->|wczytuje| OTBM["map.otbm"]
        Minimap -->|wczytuje| OTMM["minimap.otmm"]
        ThingType -->|uÄąÄ˝ywa| SpriteManager
    end

    MapView --> Creature
    MapView --> Item
    Map --> Tile
    Tile --> Thing
```

**Opis zaleÄąÄ˝noÄąâ€şci:**
-   **Client** jest punktem startowym, ktĂłry inicjalizuje wszystkie gÄąâ€šĂłwne moduÄąâ€šy (`Game`, `Map`, `ThingTypeManager`).
-   **Game** jest centralnym "mĂłzgiem" aplikacji, zarzÄ…dzajÄ…cym stanem gry, lokalnym graczem i komunikacjÄ… sieciowÄ… poprzez `ProtocolGame`.
-   **ProtocolGame** jest odpowiedzialny za serializacjÄ™ i deserializacjÄ™ danych przesyÄąâ€šanych do i z serwera. Aktualizuje stan `Game` na podstawie otrzymanych pakietĂłw.
-   **Map** przechowuje wszystkie dane o Äąâ€şwiecie gry, w tym `Tile` (pola) i `Thing` (obiekty).
-   **MapView** jest odpowiedzialny za renderowanie danych z `Map` na ekranie. Jest to warstwa wizualizacyjna dla danych mapy.
-   **ThingTypeManager** i **SpriteManager** to menedÄąÄ˝ery zasobĂłw, ktĂłre wczytujÄ… dane z plikĂłw `.dat`, `.otb` i `.spr`, dostarczajÄ…c definicje i grafiki dla wszystkich obiektĂłw w grze.
-   Hierarchia dziedziczenia obiektĂłw: `Thing` jest bazÄ… dla `Item` i `Creature`. `Creature` jest bazÄ… dla `Player`, a `Player` dla `LocalPlayer`.
-   WidÄąÄ˝ety UI (`UIMap`, `UICreature`, `UIItem`) sÄ… wyspecjalizowanymi komponentami do wyÄąâ€şwietlania odpowiednich elementĂłw logiki gry.
# Ä‘ĹşÂ§Â± Architektura systemu
System jest zbudowany w oparciu o architekturÄ™ warstwowÄ…, gdzie kaÄąÄ˝da warstwa ma jasno zdefiniowane obowiÄ…zki. MoÄąÄ˝na wyrĂłÄąÄ˝niÄ‡ nastÄ™pujÄ…ce gÄąâ€šĂłwne komponenty:

1.  **Framework (Warstwa podstawowa)**
    -   **Core**: ZarzÄ…dzanie aplikacjÄ…, pÄ™tlÄ… gÄąâ€šĂłwnÄ…, zdarzeniami (`EventDispatcher`), zasobami (`ResourceManager`), czasem (`Clock`).
    -   **Graphics**: Nisko-poziomowe renderowanie, zarzÄ…dzanie teksturami (`TextureManager`), shaderami (`ShaderManager`), czcionkami (`FontManager`) i kolejkÄ… rysowania (`DrawQueue`).
    -   **UI**: System interfejsu uÄąÄ˝ytkownika oparty na widÄąÄ˝etach (`UIWidget`) i stylach OTML.
    -   **LuaEngine**: Integracja z silnikiem skryptowym Lua, umoÄąÄ˝liwiajÄ…ca rozszerzanie logiki gry.
    -   **Net**: Nisko-poziomowa obsÄąâ€šuga poÄąâ€šÄ…czeÄąâ€ž sieciowych (`Protocol`, `Connection`).

2.  **Client (Warstwa aplikacji)**
    -   **ZarzÄ…dzanie stanem gry (`Game`)**: Centralny singleton, ktĂłry zarzÄ…dza sesjÄ… gry, stanem lokalnego gracza, interakcjami i komunikacjÄ… z serwerem. DziaÄąâ€ša jak fasada dla reszty systemu.
    -   **ObsÄąâ€šuga protokoÄąâ€šu (`ProtocolGame`)**: Implementacja protokoÄąâ€šu sieciowego. TÄąâ€šumaczy akcje gracza na pakiety i pakiety z serwera na zmiany w stanie gry.
    -   **Reprezentacja Äąâ€şwiata gry (`Map`, `Tile`, `Thing`)**: Obiektowy model Äąâ€şwiata gry. `Map` przechowuje kolekcjÄ™ `Tile`, a kaÄąÄ˝dy `Tile` przechowuje stos `Thing` (przedmiotĂłw, stworzeÄąâ€ž, etc.).
    -   **ZarzÄ…dzanie zasobami gry (`ThingTypeManager`, `SpriteManager`)**: Singletony odpowiedzialne za wczytywanie i dostarczanie definicji i grafik dla wszystkich obiektĂłw w grze z plikĂłw `.dat`, `.otb`, `.spr`.
    -   **Renderowanie (`MapView`, `Minimap`)**: Klasy odpowiedzialne za wizualizacjÄ™ danych z `Map`. `MapView` renderuje gÄąâ€šĂłwny widok gry, a `Minimap` - minimapÄ™. WykorzystujÄ… one `DrawQueue` z warstwy frameworka.
    -   **UI klienta (`UIMap`, `UIItem`, `UICreature`)**: Wyspecjalizowane widÄąÄ˝ety, ktĂłre Äąâ€šÄ…czÄ… dane z logiki gry (np. `Item`, `Creature`) z systemem UI frameworka.
## PrzepÄąâ€šyw danych i zdarzeÄąâ€ž
-   **WejÄąâ€şcie uÄąÄ˝ytkownika**: Zdarzenia wejÄąâ€şcia (mysz, klawiatura) sÄ… przechwytywane przez `UIWidget`. JeÄąâ€şli akcja dotyczy gry (np. klikniÄ™cie na mapie), wywoÄąâ€šywana jest odpowiednia metoda w `Game` (np. `g_game.walk()`).
-   **WysyÄąâ€šanie danych**: `Game` wywoÄąâ€šuje metodÄ™ w `ProtocolGame` (np. `sendWalkNorth()`), ktĂłra tworzy pakiet i wysyÄąâ€ša go na serwer.
-   **Odbieranie danych**: `ProtocolGame` odbiera pakiet, `parseMessage` identyfikuje jego typ na podstawie opkodu i wywoÄąâ€šuje odpowiedniÄ… metodÄ™ `parse...`.
-   **Aktualizacja stanu**: Metoda `parse...` (np. `parseCreatureMove`) odczytuje dane z pakietu i wywoÄąâ€šuje metody w `Game` lub `Map` (np. `g_map.addThing(...)`), ktĂłre modyfikujÄ… stan gry.
-   **Renderowanie**: W kaÄąÄ˝dej klatce, `UIMap` wywoÄąâ€šuje `MapView::drawMapBackground` i `drawMapForeground`. `MapView` pobiera aktualny stan z `g_map` (widoczne `Tile` i `Thing`), a nastÄ™pnie rysuje je na ekranie, uÄąÄ˝ywajÄ…c `ThingTypeManager` i `SpriteManager` do uzyskania odpowiednich grafik.

Ta architektura oddziela logikÄ™ gry od renderowania i obsÄąâ€šugi sieci, co uÄąâ€šatwia zarzÄ…dzanie kodem i jego rozbudowÄ™. UÄąÄ˝ycie Lua pozwala na dynamiczne modyfikowanie zachowaÄąâ€ž interfejsu i logiki bez potrzeby rekompilacji caÄąâ€šego klienta.



