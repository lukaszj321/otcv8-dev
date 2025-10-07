# otclientv8-dev/src/client

> NOTE: Wszystkie pliki w repozytorium sa objete licencja MIT (2010-2017 OTClient, autor Edubart).
## Ogolny opis
Implementacja klasy `AnimatedText`, ktora odpowiada za renderowanie animowanego tekstu na mapie, takiego jak komunikaty o zadanych obraLLeniach, leczeniu czy zdobytych punktach doLwiadczenia. Plik zawiera logike animacji, rysowania oraz L'aczenia podobnych tekstow w jeden.
## Klasa `AnimatedText`
## Opis
Klasa `AnimatedText` dziedziczy po `Thing` i reprezentuje tekst, ktory pojawia sie w okreLlonym miejscu na mapie, a nastepnie animuje swoje poL'oLLenie i przezroczystoLc, by ostatecznie zniknac.
## Metody
| Nazwa | Opis |
| --- | --- |
| `AnimatedText()` | Konstruktor. Inicjalizuje domyLlne wL'aLciwoLci tekstu, takie jak czcionka i wyrownanie. |
| `drawText(const Point& dest, const Rect& visibleRect)` | Rysuje tekst w okreLlonym miejscu, uwzgledniajac postep animacji. Animacja obejmuje ruch w gore (i opcjonalnie po przekatnej) oraz stopniowe zanikanie. |
| `onAppear()` | Metoda wywoL'ywana, gdy tekst pojawia sie na mapie. Resetuje timer animacji i planuje usuniecie obiektu po zakoL"czeniu animacji. |
| `setColor(int color)` | Ustawia kolor tekstu na podstawie 8-bitowej wartoLci. |
| `setText(const std::string& text)` | Ustawia treLc tekstu. |
| `setFont(const std::string& fontName)` | Ustawia czcionke tekstu na podstawie nazwy. |
| `merge(const AnimatedTextPtr& other)` | Probuje poL'aczyc tekst z innym obiektem `AnimatedText`. Laczenie jest moLLliwe, jeLli oba teksty maja ten sam kolor, czcionke, a animacja obecnego tekstu nie jest zbyt zaawansowana. Teksty liczbowe sa sumowane. |
## ZaleLLnoLci i powiazania
- **`map.h`**: ULLywa `g_map` do usuwania obiektu `AnimatedText` po zakoL"czeniu animacji.
- **`game.h`**: ULLywa `g_game` do sprawdzania, czy funkcja `GameDiagonalAnimatedText` jest wL'aczona.
- **`framework/core/clock.h`**: ULLywa `g_clock` do pomiaru czasu animacji.
- **`framework/core/eventdispatcher.h`**: ULLywa `g_dispatcher` do planowania usuniecia obiektu.
- **`framework/graphics/graphics.h`**: ULLywa `g_fonts` do zarzadzania czcionkami.
## PrzykL'ad uLLycia
Obiekty `AnimatedText` sa tworzone przez `ProtocolGame` w odpowiedzi na komunikaty serwera (np. o obraLLeniach) i dodawane do `g_map`, ktora zarzadza ich cyklem LLycia i rysowaniem.

// PrzykL'ad tworzenia (logika w ProtocolGame::parseAnimatedText)
AnimatedTextPtr animatedText = AnimatedTextPtr(new AnimatedText);
animatedText->setColor(color);
animatedText->setText(text);
g_map.addThing(animatedText, position);
```
---
# z"" houses.h
## Ogolny opis
Plik ten definiuje klasy `House` i `HouseManager`, ktore sL'uLLa do zarzadzania informacjami o domach w grze. Zawiera definicje struktur przechowujacych atrybuty domow, takie jak nazwa, ID, wejLcie, oraz metody do zarzadzania nimi.
## Klasa `House`
## Opis
Reprezentuje pojedynczy dom w Lwiecie gry. Przechowuje jego atrybuty, liste przynaleLLnych do niego pol (tiles) oraz drzwi.
## Metody
| Nazwa | Opis |
| --- | --- |
| `House(uint32 hId, ...)` | Konstruktor tworzacy dom o zadanym ID, nazwie i pozycji wejLciowej. |
| `setTile(const TilePtr& tile)` | Dodaje pole (tile) do domu. |
| `getTile(const Position& pos)` | Zwraca wskaLsnik do pola na podanej pozycji, jeLli naleLLy ono do domu. |
| `setName(const std::string& name)` | Ustawia nazwe domu. |
| `getName()` | Zwraca nazwe domu. |
| `setId(uint32 hId)` | Ustawia unikalne ID domu. |
| `getId()` | Zwraca ID domu. |
| `setTownId(uint32 tid)` | Ustawia ID miasta, w ktorym znajduje sie dom. |
| `getTownId()` | Zwraca ID miasta. |
| `setSize(uint32 s)` | Ustawia rozmiar domu. |
| `getSize()` | Zwraca rozmiar domu. |
| `setRent(uint32 r)` | Ustawia cene wynajmu domu. |
| `getRent()` | Zwraca cene wynajmu. |
| `setEntry(const Position& p)` | Ustawia pozycje wejLcia do domu. |
| `getEntry()` | Zwraca pozycje wejLcia. |
| `addDoor(const ItemPtr& door)` | Dodaje drzwi do domu i przypisuje im unikalne ID. |
| `removeDoor(const ItemPtr& door)` | Usuwa drzwi z domu. |
| `removeDoorById(uint32 doorId)` | Usuwa drzwi na podstawie ich ID. |
## Klasa `HouseManager`
## Opis
Singleton (`g_houses`) zarzadzajacy wszystkimi domami w grze. Odpowiada za ich dodawanie, usuwanie, wczytywanie i zapisywanie z plikow XML.
## Metody
| Nazwa | Opis |
| --- | --- |
| `addHouse(const HousePtr& house)` | Dodaje nowy dom do listy. |
| `removeHouse(uint32 houseId)` | Usuwa dom o podanym ID. |
| `getHouse(uint32 houseId)` | Zwraca dom o podanym ID. |
| `getHouseByName(std::string name)` | Zwraca dom o podanej nazwie. |
| `load(const std::string& fileName)` | Wczytuje dane o domach z pliku XML. |
| `save(const std::string& fileName)` | Zapisuje dane o domach do pliku XML. |
| `sort()` | Sortuje liste domow alfabetycznie wedL'ug nazwy. |
| `clear()` | CzyLci liste domow. |
| `getHouseList()` | Zwraca liste wszystkich domow. |
| `filterHouses(uint32 townId)` | Zwraca liste domow naleLLacych do okreLlonego miasta. |
## Zmienne globalne
- `HouseManager g_houses`: Globalna instancja managera domow.
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow wskaLsnikow, takich jak `HousePtr` i `TilePtr`.
- **`tile.h`**: ULLywa obiektow `Tile` do okreLlenia obszaru domu.
- **`item.h`**: Zarzadza drzwiami, ktore sa obiektami typu `Item`.
- **`framework/luaengine/luaobject.h`**: Klasy sa eksponowane do Lua.

---
# z"" animatedtext.h
## Ogolny opis
Plik nagL'owkowy dla klasy `AnimatedText`. Definiuje interfejs klasy, ktora zarzadza animowanym tekstem na mapie.
## Klasa `AnimatedText`
## Opis
Dziedziczy po `Thing`. SL'uLLy do wyLwietlania tekstu, ktory porusza sie i zanika. Jest to obiekt "efemeryczny", ktory istnieje na mapie tylko przez czas trwania animacji.
## Metody
| Nazwa | Opis |
| --- | --- |
| `AnimatedText()` | Konstruktor. |
| `drawText(const Point& dest, const Rect& visibleRect)` | Rysuje tekst na ekranie z uwzglednieniem animacji. |
| `setColor(int color)` | Ustawia kolor tekstu. |
| `setText(const std::string& text)` | Ustawia treLc tekstu. |
| `setOffset(const Point& offset)` | Ustawia przesuniecie (offset) rysowania tekstu, uLLywane do unikania nakL'adania sie tekstow. |
| `setFont(const std::string& fontName)` | Ustawia czcionke tekstu. |
| `getColor()` | Zwraca kolor tekstu. |
| `getCachedText()` | Zwraca obiekt `CachedText` przechowujacy tekst i informacje o renderowaniu. |
| `getOffset()` | Zwraca aktualne przesuniecie tekstu. |
| `getTimer()` | Zwraca timer uLLywany do animacji. |
| `merge(const AnimatedTextPtr& other)` | Funkcja do L'aczenia z innym `AnimatedText`. |
| `asAnimatedText()` | Rzutuje wskaLsnik na `AnimatedTextPtr`. |
| `isAnimatedText()` | Zwraca `true`. |
| `getText()` | Zwraca treLc tekstu. |
## ZaleLLnoLci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/graphics/fontmanager.h`**: Zarzadzanie czcionkami.
- **`framework/core/timer.h`**: Pomiar czasu animacji.
- **`framework/graphics/cachedtext.h`**: Efektywne renderowanie tekstu.

---
# z"" animator.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Animator`, ktora zarzadza animacjami klatek dla obiektow w grze, takich jak przedmioty czy efekty.
## Klasa `Animator`
## Opis
Klasa `Animator` kontroluje, ktora klatka animacji powinna byc wyLwietlona w danym momencie. ObsL'uguje roLLne tryby animacji, takie jak petle, ping-pong, animacje asynchroniczne i losowe.
## Typy wyliczeniowe
- **`AnimationPhase`**: OkreLla faze animacji (np. automatyczna, losowa, asynchroniczna).
- **`AnimationDirection`**: OkreLla kierunek animacji (do przodu, do tyL'u).
## Metody
| Nazwa | Opis |
| --- | --- |
| `Animator()` | Konstruktor. |
| `unserialize(int animationPhases, const FileStreamPtr& fin)` | Wczytuje dane animatora ze strumienia. |
| `serialize(const FileStreamPtr& fin)` | Zapisuje dane animatora do strumienia. |
| `setPhase(int phase)` | Ustawia bieLLaca faze animacji. |
| `getPhase()` | Oblicza i zwraca bieLLaca faze animacji na podstawie czasu. |
| `getPhaseAt(Timer& timer, int lastPhase)` | Oblicza faze animacji w danym momencie czasu (uLLywane przez `Effect` dla niezaleLLnych animacji). |
| `getStartPhase()` | Zwraca poczatkowa faze animacji. |
| `getAnimationPhases()` | Zwraca caL'kowita liczbe faz animacji. |
| `isAsync()` | Zwraca `true`, jeLli animacja jest asynchroniczna. |
| `isComplete()` | Zwraca `true`, jeLli animacja zostaL'a zakoL"czona. |
| `getTotalDuration()` | Zwraca caL'kowity czas trwania animacji. |
| `resetAnimation()` | Resetuje stan animacji do poczatkowego. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`framework/core/timer.h`**: ULLywane do pomiaru czasu i synchronizacji animacji.

---
# z"" animator.cpp
## Ogolny opis
Implementacja klasy `Animator`. Zawiera logike obliczania faz animacji w zaleLLnoLci od czasu i trybu pracy.
## Klasa `Animator`
## Opis
Plik implementuje logike dziaL'ania animatora. Obliczenia fazy zaleLLa od tego, czy animacja jest synchroniczna (wszystkie obiekty tego samego typu animuja sie tak samo) czy asynchroniczna (kaLLdy obiekt animuje sie niezaleLLnie).
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(...)` | Wczytuje z pliku binarnego liczbe faz, tryb `async`, liczbe petli, faze startowa oraz czas trwania kaLLdej klatki (min/max). |
| `serialize(...)` | Zapisuje dane animatora do pliku binarnego. |
| `setPhase(int phase)` | Ustawia aktualna faze animacji. Dla animacji asynchronicznych resetuje timer i ustawia czas trwania klatki. Dla synchronicznych przelicza faze na podstawie globalnego zegara. |
| `getPhase()` | GL'owna metoda aktualizujaca. Na podstawie czasu, jaki upL'ynaL' od ostatniego wywoL'ania, decyduje, czy naleLLy przejLc do nastepnej klatki animacji. |
| `getPhaseAt(...)` | Metoda uLLywana przez efekty (`Effect`) do uzyskania fazy animacji niezaleLLnie od innych obiektow tego samego typu. ULLywa wL'asnego timera i pseudolosowego generatora do okreLlenia czasu trwania klatek. |
| `getStartPhase()` | Zwraca faze startowa; jeLli ustawiono na losowa, losuje ja z dostepnego zakresu. |
| `resetAnimation()` | Przywraca animator do stanu poczatkowego. |
| `getPingPongPhase()` | Oblicza nastepna faze dla animacji typu "ping-pong" (do przodu i do tyL'u). |
| `getLoopPhase()` | Oblicza nastepna faze dla animacji w petli. |
| `getPhaseDuration(int phase)` | Zwraca czas trwania danej klatki animacji (losowy w zakresie min-max). |
| `calculateSynchronous()` | Oblicza bieLLaca faze dla animacji synchronicznej, bazujac na globalnym czasie i sumarycznym czasie trwania wszystkich klatek. |
| `getTotalDuration()` | Zwraca sumaryczny czas trwania wszystkich klatek animacji. |
## ZaleLLnoLci i powiazania
- **`framework/core/clock.h`**: ULLywa `g_clock` do synchronizacji animacji.
- **`framework/core/filestream.h`**: Do operacji serializacji/deserializacji.

---
# z"" client.cpp
## Ogolny opis
Plik implementuje klase `Client`, ktora jest gL'ownym punktem wejLcia i zarzadzania dla aplikacji klienckiej. Odpowiada za inicjalizacje i zamykanie kluczowych moduL'ow gry.
## Klasa `Client`
## Metody
| Nazwa | Opis |
| --- | --- |
| `init(std::vector<std::string>& args)` | Inicjalizuje wszystkie gL'owne moduL'y klienta w odpowiedniej kolejnoLci: rejestruje funkcje Lua, a nastepnie inicjalizuje `g_map`, `g_minimap`, `g_game`, `g_shaders`, `g_things`, `g_healthBars`. |
| `terminate()` | Zamyka wszystkie moduL'y w odwrotnej kolejnoLci do inicjalizacji, zwalniajac zasoby. |
## Zmienne globalne
- `Client g_client`: Globalna instancja klasy `Client`.
## ZaleLLnoLci i powiazania
- **`game.h`**: Inicjalizuje i zamyka `g_game`.
- **`map.h`**: Inicjalizuje i zamyka `g_map`.
- **`minimap.h`**: Inicjalizuje i zamyka `g_minimap`.
- **`spritemanager.h`**: PoLrednio zarzadza `g_sprites` poprzez `g_things`.
- **`healthbars.h`**: Inicjalizuje i zamyka `g_healthBars`.
- **`framework/core/modulemanager.h`**: ULLywane do zarzadzania moduL'ami.
- **`framework/graphics/shadermanager.h`**: Inicjalizuje i zamyka `g_shaders`.

---
# z"" client.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Client`. Deklaruje interfejs gL'ownej klasy aplikacji klienckiej.
## Klasa `Client`
## Opis
Klasa `Client` jest odpowiedzialna za zarzadzanie cyklem LLycia aplikacji klienckiej.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init(std::vector<std::string>& args)` | Inicjalizuje aplikacje. |
| `terminate()` | KoL"czy dziaL'anie aplikacji, zwalniajac zasoby. |
| `registerLuaFunctions()` | Rejestruje funkcje C++ dostepne w Lrodowisku Lua. |
## Zmienne globalne
- `Client g_client`: Deklaracja zewnetrznej globalnej instancji klienta.
## ZaleLLnoLci i powiazania
- **`global.h`**: Zawiera podstawowe definicje i staL'e uLLywane w kliencie.

---
# z"" CMakeLists.txt
## Ogolny opis
Plik konfiguracyjny systemu budowania CMake dla moduL'u klienta. Definiuje on, ktore pliki LsrodL'owe (`.cpp`, `.h`) zostana skompilowane i wL'aczone do finalnej aplikacji klienckiej.
## Struktura pliku
## Definicje preprocesora
- `add_definitions(-DCLIENT)`: Dodaje makro `CLIENT` do wszystkich kompilowanych plikow, co pozwala na warunkowa kompilacje kodu specyficznego dla klienta.
## Lista plikow LsrodL'owych (`client_SOURCES`)
Plik zawiera jedna dL'uga liste wszystkich plikow LsrodL'owych i nagL'owkowych, ktore skL'adaja sie na moduL' klienta. Pliki sa pogrupowane w logiczne kategorie za pomoca komentarzy:
- **`# client`**: GL'owne pliki klienta.
- **`# core`**: RdzeL" logiki gry (mapa, przedmioty, postacie, etc.).
- **`# lua`**: Pliki zwiazane z integracja z silnikiem Lua.
- **`# net`**: Logika sieciowa i protokoL'y.
- **`# ui`**: Niestandardowe widLLety interfejsu uLLytkownika.
- **`# util`**: Pomocnicze klasy i struktury, jak `Position`.
## ZaleLLnoLci i powiazania
Ten plik jest kluczowy dla procesu budowania i definiuje, ktore czeLci kodu LsrodL'owego sa ze soba powiazane i tworza aplikacje kliencka. KaLLdy plik dodany do tej listy staje sie czeLcia projektu.

---
# z"" const.h
## Ogolny opis
Plik nagL'owkowy zawierajacy globalne staL'e i typy wyliczeniowe uLLywane w caL'ej aplikacji klienckiej. Definiuje kluczowe wartoLci, takie jak flagi rysowania, atrybuty przedmiotow, tryby gry, a takLLe identyfikatory funkcji serwera (`GameFeature`).
## Namespace `Otc`
## Typy wyliczeniowe
- **`enum` (anonimowy)**: Zawiera ogolne staL'e, takie jak `MAX_ELEVATION`, `SEA_FLOOR`, `MAX_Z`, czasy trwania animacji (`ANIMATED_TEXT_DURATION`) i inne.
- **`DepthConst`**: StaL'e zwiazane z gL'ebokoLcia renderowania.
- **`DrawFlags`**: Flagi okreLlajace, ktore elementy sceny maja byc rysowane (np. podL'oLLe, postacie, efekty).
- **`DatOpts`**: Atrybuty przedmiotow wczytywane z plikow `.dat`.
- **`InventorySlot`**: Identyfikatory slotow ekwipunku.
- **`Statistic`**: Identyfikatory statystyk gracza (LLycie, mana, doLwiadczenie).
- **`Skill`**: Identyfikatory umiejetnoLci gracza.
- **`Direction`**: Kierunki (poL'noc, poL'udnie, etc.).
- **`FluidsColor`**, **`FluidsType`**: Kolory i typy pL'ynow.
- **`FightModes`**, **`ChaseModes`**, **`PVPModes`**: Tryby walki, Lcigania i PvP.
- **`PlayerSkulls`**: Typy czaszek nad gL'owa gracza.
- **`PlayerShields`**: Typy tarcz imprezowych (party shields).
- **`PlayerEmblems`**: Emblematy gildii.
- **`CreatureIcons`**: Ikony nad postaciami NPC.
- **`PlayerStates`**: Stany gracza (zatrucie, podpalenie, etc.).
- **`MessageMode`**: Tryby wiadomoLci w grze (say, whisper, yell, etc.).
- **`GameFeature`**: Flagi okreLlajace, ktore funkcje sa obsL'ugiwane przez serwer. Jest to kluczowy enum dla zapewnienia kompatybilnoLci z roLLnymi wersjami serwerow.
- **`PathFindResult`**: Wyniki algorytmu wyszukiwania LcieLLki.
- **`PathFindFlags`**: Flagi modyfikujace dziaL'anie algorytmu wyszukiwania LcieLLki.
- **`AutomapFlags`**: Ikony znacznikow na minimapie.
- **`VipState`**: Stany graczy na liLcie VIP.
- **`SpeedFormula`**: RoLLne formuL'y obliczania predkoLci postaci.
- **`Blessings`**: BL'ogosL'awieL"stwa.
- **`DeathType`**: Typ Lmierci (zwykL'a, z bL'ogosL'awieL"stwem).
- **`StoreProductTypes`**, **`StoreErrorTypes`**, **`StoreStates`**: Typy zwiazane ze sklepem w grze (Store).
- **`Prey...`**: Enumeracje zwiazane z systemem Prey.
- **`MagicEffectsType_t`**: Typy operacji w zaawansowanych efektach magicznych.
## ZaleLLnoLci i powiazania
Ten plik jest fundamentalny i jest doL'aczany w wiekszoLci plikow projektu, poniewaLL definiuje podstawowe "sL'ownictwo" uLLywane w logice gry.

---
# z"" container.cpp
## Ogolny opis
Implementacja klasy `Container`, ktora reprezentuje pojemniki w grze, takie jak plecaki. Plik zawiera logike zarzadzania przedmiotami wewnatrz kontenera oraz obsL'uge zdarzeL" z nim zwiazanych.
## Klasa `Container`
## Metody
| Nazwa | Opis |
| --- | --- |
| `Container(...)` | Konstruktor. Inicjalizuje kontener na podstawie danych otrzymanych z serwera. |
| `getItem(int slot)` | Zwraca przedmiot znajdujacy sie w danym slocie. |
| `onOpen(const ContainerPtr& previousContainer)` | WywoL'uje callback Lua `onOpen`, gdy kontener jest otwierany. |
| `onClose()` | Oznacza kontener jako zamkniety i wywoL'uje callback Lua `onClose`. |
| `onAddItem(const ItemPtr& item, int slot)` | Dodaje przedmiot do kontenera. JeLli kontener ma strony (`hasPages`), a slot jest poza widocznym zakresem, jedynie aktualizuje rozmiar. W przeciwnym razie dodaje przedmiot do listy i wywoL'uje callbacki Lua `onSizeChange` i `onAddItem`. |
| `findItemById(uint itemId, int subType)` | Wyszukuje przedmiot w kontenerze po jego ID i opcjonalnie podtypie. |
| `onAddItems(const std::vector<ItemPtr>& items)` | Dodaje wiele przedmiotow naraz (np. przy otwarciu kontenera). |
| `onUpdateItem(int slot, const ItemPtr& item)` | Aktualizuje przedmiot w danym slocie, zastepujac stary nowym. |
| `onRemoveItem(int slot, const ItemPtr& lastItem)` | Usuwa przedmiot z danego slota. JeLli `lastItem` jest podany (dla kontenerow ze stronami), jest on dodawany na koL"cu widocznej czeLci kontenera. |
| `updateItemsPositions()` | Aktualizuje pozycje wszystkich przedmiotow w kontenerze, aby odzwierciedlaL'y ich sloty. |
## ZaleLLnoLci i powiazania
- **`item.h`**: Zarzadza obiektami typu `Item`.
- **`framework/luaengine/luaobject.h`**: Dziedziczy po `LuaObject`, aby umoLLliwic interakcje z Lua.

---
# z"" creature.cpp
## Ogolny opis
Implementacja klasy `Creature`, ktora jest podstawowa klasa dla wszystkich LLywych istot w grze (graczy, potworow, NPC). Plik ten zawiera zL'oLLona logike rysowania, animacji, poruszania sie, skakania oraz wyLwietlania informacji o postaci.
## Klasa `Creature`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | GL'owna funkcja rysujaca. Renderuje postac, jej ubior, kwadraty oznaczajace (np. cel ataku), a takLLe dodaje LwiatL'o do `LightView`. |
| `drawOutfit(...)` | Rysuje sam ubior postaci w zadanym prostokacie, uLLywane gL'ownie w interfejsie uLLytkownika. |
| `drawInformation(...)` | Rysuje pasek LLycia, many, nazwe, ikony (czaszka, tarcza) nad postacia. |
| `turn(Otc::Direction direction)` | Zmienia kierunek, w ktorym zwrocona jest postac. |
| `walk(const Position& oldPos, const Position& newPos)` | Inicjuje proces chodzenia z `oldPos` do `newPos`, ustawiajac kierunek, timery i rozpoczynajac aktualizacje animacji. |
| `stopWalk()` | Natychmiastowo przerywa proces chodzenia. |
| `jump(int height, int duration)` | Rozpoczyna animacje skoku postaci. |
| `updateJump()` | Aktualizuje wysokoLc skoku w kaLLdej klatce animacji. |
| `onAppear()` | ObsL'uguje pojawienie sie postaci na ekranie. Decyduje, czy postac przyszL'a, teleportowaL'a sie, czy tylko sie obrociL'a. |
| `onDisappear()` | ObsL'uguje znikniecie postaci z ekranu, planujac jej ostateczne usuniecie. |
| `onDeath()` | WywoL'uje callback Lua `onDeath`. |
| `updateWalkAnimation(...)` | Aktualizuje faze animacji chodzenia na podstawie czasu i przebytych pikseli. |
| `updateWalkOffset(...)` | Oblicza przesuniecie postaci podczas chodzenia. |
| `updateWalkingTile()` | Aktualizuje, na ktorym polu (`Tile`) postac jest obecnie rysowana podczas animacji chodzenia. |
| `nextWalkUpdate()` | Planuje nastepna aktualizacje stanu chodzenia. |
| `updateWalk()` | GL'owna funkcja aktualizujaca stan chodzenia, wywoL'ywana cyklicznie. |
| `terminateWalk()` | KoL"czy proces chodzenia, resetujac wszystkie zwiazane z nim zmienne. |
| `setHealthPercent(uint8 healthPercent)` | Ustawia procent LLycia i aktualizuje kolor paska LLycia. |
| `setOutfit(const Outfit& outfit)` | Zmienia ubior postaci. |
| `setSpeed(uint16 speed)` | Ustawia predkoLc poruszania sie postaci. |
| `getStepDuration(...)` | Oblicza czas trwania jednego kroku w milisekundach na podstawie predkoLci postaci, predkoLci podL'oLLa i formuL' predkoLci serwera. |
| `getDisplacement()` | Zwraca przesuniecie rysowania postaci, ktore centruje ja na polu. |
| `addTopWidget(...)` / `addBottomWidget(...)` | Dodaje widLLety, ktore beda rysowane nad lub pod postacia. |
## Zmienne statyczne
- `m_speedFormula`: Tablica przechowujaca wspoL'czynniki do zaawansowanego obliczania predkoLci.
## ZaleLLnoLci i powiazania
- **`localplayer.h`**: Logika rysowania informacji o pasku many jest specyficzna dla lokalnego gracza.
- **`map.h`**, **`tile.h`**: Interakcje ze Lwiatem gry (pobieranie pol, predkoLci podL'oLLa).
- **`game.h`**: Dostep do globalnych ustawieL" gry i funkcji serwera.
- **`lightview.h`**: Dodawanie dynamicznego LwiatL'a emitowanego przez postac.
- **`healthbars.h`**: ULLywa `g_healthBars` do pobierania niestandardowych teL' dla paskow LLycia/many.
- **`spritemanager.h`**: ULLywa `g_sprites` do pobierania rozmiaru sprite'ow.

---
# z"" container.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Container`. Definiuje interfejs do zarzadzania pojemnikami w grze.
## Klasa `Container`
## Opis
Klasa `Container` dziedziczy po `LuaObject`, co pozwala na jej uLLycie w skryptach Lua. Reprezentuje obiekt w grze, ktory moLLe przechowywac inne przedmioty, jak plecak czy skrzynka.
## Metody
| Nazwa | Opis |
| --- | --- |
| `getItem(int slot)` | Zwraca wskaLsnik do przedmiotu w danym slocie. |
| `getItems()` | Zwraca kolekcje (`std::deque`) wszystkich przedmiotow w kontenerze. |
| `getItemsCount()` | Zwraca liczbe przedmiotow w kontenerze. |
| `getSlotPosition(int slot)` | Zwraca specjalnie zakodowana pozycje, ktora identyfikuje slot w tym kontenerze. |
| `getId()` | Zwraca ID kontenera. |
| `getCapacity()` | Zwraca pojemnoLc kontenera. |
| `getContainerItem()` | Zwraca przedmiot, ktory reprezentuje ten kontener. |
| `getName()` | Zwraca nazwe kontenera. |
| `hasParent()` | Zwraca `true`, jeLli kontener znajduje sie w innym kontenerze. |
| `isClosed()` | Zwraca `true`, jeLli kontener zostaL' zamkniety. |
| `isUnlocked()` | Zwraca `true`, jeLli moLLna przesuwac w nim przedmioty. |
| `hasPages()` | Zwraca `true`, jeLli kontener obsL'uguje paginacje. |
| `getSize()` | Zwraca caL'kowita liczbe przedmiotow w kontenerze (moLLe byc wieksza niLL pojemnoLc, jeLli ma strony). |
| `getFirstIndex()` | Zwraca indeks pierwszego przedmiotu na bieLLacej stronie. |
| `findItemById(uint itemId, int subType)` | Wyszukuje przedmiot po ID i opcjonalnym podtypie. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow, np. `ItemPtr`.
- **`item.h`**: Przechowuje obiekty `Item`.
- **`game.h`**: Klasa `Game` jest przyjacielem, co pozwala jej wywoL'ywac chronione metody `onOpen`, `onClose`, etc.

---
# z"" creature.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Creature` oraz jej specjalizacji: `Npc` i `Monster`. Definiuje interfejs dla wszystkich istot w grze.
## Klasa `Creature`
## Opis
Klasa bazowa dla wszystkich postaci w grze. Dziedziczy po `Thing`. Zawiera logike zwiazana z wygladem, ruchem, stanami i interakcjami.
## Typy wyliczeniowe
- **`enum` (anonimowy)**: Definiuje staL'e `SHIELD_BLINK_TICKS` i `VOLATILE_SQUARE_DURATION`.
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje postac w danym miejscu na mapie. |
| `drawOutfit(...)` | Rysuje sam ubior postaci, uLLywane w UI. |
| `drawInformation(...)` | Rysuje informacje nad postacia (nazwa, paski LLycia/many, ikony). |
| `setId(uint32 id)` | Ustawia ID postaci. |
| `setName(const std::string& name)` | Ustawia nazwe postaci. |
| `setHealthPercent(uint8 healthPercent)` | Ustawia procent LLycia. |
| `setDirection(Otc::Direction direction)` | Ustawia kierunek, w ktorym postac jest zwrocona. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubior postaci. |
| `setSpeed(uint16 speed)` | Ustawia predkoLc poruszania sie. |
| `addTimedSquare(uint8 color)` | WyLwietla tymczasowy kolorowy kwadrat pod postacia. |
| `getStepDuration(...)` | Zwraca czas trwania jednego kroku. |
| `walk(const Position& oldPos, const Position& newPos)` | Inicjuje ruch postaci. |
| `stopWalk()` | Przerywa ruch postaci. |
| `isWalking()` | Zwraca `true`, jeLli postac jest w trakcie chodu. |
| `isDead()` | Zwraca `true`, jeLli postac ma 0% LLycia. |
| `getThingType()` | Zwraca `ThingType` dla aktualnego ubioru postaci. |
| `addTopWidget(...)`, `addBottomWidget(...)` | Dodaje widLLety do rysowania nad/pod postacia. |
## Klasa `Npc`
## Opis
Specjalizacja `Creature` dla postaci niezaleLLnych (NPC).
## Klasa `Monster`
## Opis
Specjalizacja `Creature` dla potworow.
## ZaleLLnoLci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`outfit.h`**: ULLywa `Outfit` do zarzadzania wygladem.
- **`tile.h`**: Interakcje z polami mapy.
- **`mapview.h`**: ULLywana do rysowania w kontekLcie widoku mapy.
- **`framework/ui/uiwidget.h`**: DoL'aczanie widLLetow do postaci.

---
# z"" creatures.h
## Ogolny opis
Plik nagL'owkowy definiujacy klasy do zarzadzania typami stworzeL" (`CreatureType`) oraz ich miejscami odradzania (`Spawn`). Jest to czeLc systemu, ktory prawdopodobnie sL'uLLy do edycji map lub dziaL'ania jako serwer, a nie tylko do gry.
## Typy wyliczeniowe
- **`CreatureAttr`**: Atrybuty typu stworzenia (pozycja, nazwa, ubior, etc.).
- **`CreatureRace`**: Rasa stworzenia (NPC, potwor).
- **`SpawnAttr`**: Atrybuty spawnu (promieL", Lrodek).
## Klasa `Spawn`
## Opis
Reprezentuje obszar odradzania sie stworzeL" (spawn). Przechowuje informacje o Lrodku, promieniu oraz liste potworow/NPC, ktore sie w nim pojawiaja.
## Metody
| Nazwa | Opis |
| --- | --- |
| `setRadius(int32 r)` | Ustawia promieL" spawnu. |
| `getRadius()` | Zwraca promieL" spawnu. |
| `setCenterPos(const Position& pos)` | Ustawia centralna pozycje spawnu. |
| `getCenterPos()` | Zwraca centralna pozycje spawnu. |
| `getCreatures()` | Zwraca liste typow stworzeL" w tym spawnie. |
| `addCreature(const Position& placePos, const CreatureTypePtr& cType)` | Dodaje stworzenie do spawnu w okreLlonym miejscu. |
| `removeCreature(const Position& pos)` | Usuwa stworzenie z danej pozycji. |
| `clear()` | CzyLci liste stworzeL". |
## Klasa `CreatureType`
## Opis
Reprezentuje szablon (typ) stworzenia. Przechowuje domyLlne wL'aLciwoLci, takie jak nazwa, ubior czy kierunek, ktore sa uLLywane do tworzenia instancji `Creature`.
## Metody
| Nazwa | Opis |
| --- | --- |
| `setSpawnTime(int32 spawnTime)` | Ustawia czas odradzania. |
| `getSpawnTime()` | Zwraca czas odradzania. |
| `setName(const std::string& name)` | Ustawia nazwe typu. |
| `getName()` | Zwraca nazwe. |
| `setOutfit(const Outfit& o)` | Ustawia domyLlny ubior. |
| `getOutfit()` | Zwraca domyLlny ubior. |
| `cast()` | Tworzy i zwraca instancje `Creature` na podstawie tego typu. |
## Klasa `CreatureManager`
## Opis
Singleton (`g_creatures`) zarzadzajacy wszystkimi typami stworzeL" i spawnami. Wczytuje te dane z plikow XML.
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
- `CreatureManager g_creatures`: Globalna instancja managera stworzeL".
## ZaleLLnoLci i powiazania
- **`declarations.h`**, **`outfit.h`**: Definicje typow.
- **`creature.h`**: `CreatureType::cast()` tworzy obiekty `Creature`.

---
# z"" declarations.h
## Ogolny opis
Plik nagL'owkowy zawierajacy deklaracje wyprzedzajace (forward declarations) oraz definicje typow wskaLsnikow i kolekcji uLLywanych w caL'ym module klienta. Jego gL'ownym celem jest przeL'amanie cyklicznych zaleLLnoLci miedzy plikami nagL'owkowymi.
## ZawartoLc
## Deklaracje wyprzedzajace
Plik deklaruje istnienie klas bez koniecznoLci doL'aczania ich peL'nych definicji. Obejmuje to klasy z roLLnych moduL'ow:
- **Core**: `Map`, `Game`, `Tile`, `Thing`, `Item`, `Creature`, `LocalPlayer`, `Effect`, `House`, `Town` itp.
- **Net**: `ProtocolLogin`, `ProtocolGame`.
- **UI**: `UIItem`, `UICreature`, `UIMap`, `UIMinimap` itp.
- **Custom**: `HealthBar`.
## Definicje typow (`typedef`)
Definiuje inteligentne wskaLsniki (`shared_object_ptr`) dla wiekszoLci zadeklarowanych klas, np.:
- `MapViewPtr`
- `TilePtr`
- `ThingPtr`
- `ItemPtr`
- `CreaturePtr`
- `LocalPlayerPtr`
## Definicje kolekcji (`typedef`)
Definiuje standardowe typy kolekcji dla zadeklarowanych obiektow, uL'atwiajac ich uLLycie w kodzie:
- `ThingList` (`std::vector<ThingPtr>`)
- `HouseList` (`std::list<HousePtr>`)
- `TileMap` (`std::unordered_map<Position, TilePtr, PositionHasher>`)
## ZaleLLnoLci i powiazania
- **`global.h`**: DoL'acza podstawowe definicje.
- Plik ten jest doL'aczany przez niemal wszystkie inne pliki nagL'owkowe w module, aby zapewnic dostep do definicji typow wskaLsnikow i uniknac problemow z zaleLLnoLciami.

---
# z"" creatures.cpp
## Ogolny opis
Implementacja `CreatureManager` i `Spawn`, odpowiedzialnych za zarzadzanie typami stworzeL" i ich miejscami odradzania. Plik zawiera logike wczytywania i zapisywania danych z plikow XML oraz zarzadzania stworzeniami na mapie.
## Funkcje pomocnicze
- **`isInZone(...)`**: Sprawdza, czy dana pozycja znajduje sie w promieniu spawnu.
## Klasa `Spawn`
## Metody
| Nazwa | Opis |
| --- | --- |
| `load(TiXmlElement* node)` | Wczytuje dane spawnu z wezL'a XML, w tym pozycje centralna, promieL" oraz liste stworzeL" z ich atrybutami. |
| `save(TiXmlElement* node)` | Zapisuje dane spawnu do wezL'a XML. |
| `addCreature(...)` | Dodaje stworzenie do spawnu. Najpierw tworzy instancje `Creature` na podstawie `CreatureType` za pomoca `cast()`, a nastepnie dodaje ja na mape (`g_map.addThing`). |
| `removeCreature(...)` | Usuwa stworzenie ze spawnu i z mapy. |
| `getCreatures()` | Zwraca liste wszystkich typow stworzeL" w tym spawnie. |
## Klasa `CreatureType`
## Metody
| Nazwa | Opis |
| --- | --- |
| `cast()` | Tworzy nowa instancje `Creature`, ustawia jej nazwe, kierunek i ubior na podstawie danych z `CreatureType`, a nastepnie zwraca ja jako `CreaturePtr`. |
## Klasa `CreatureManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `terminate()` | CzyLci wszystkie dane managera. |
| `loadMonsters(const std::string& file)` | Wczytuje gL'owny plik XML z potworami, ktory zawiera odnoLniki do pojedynczych plikow XML dla kaLLdego potwora. |
| `loadSingleCreature(const std::string& file)` | Wczytuje dane pojedynczego stworzenia z pliku XML. |
| `loadNpcs(const std::string& folder)` | Wczytuje wszystkie pliki XML z danego folderu jako definicje NPC. |
| `loadSpawns(const std::string& fileName)` | Wczytuje plik XML ze spawnami i umieszcza stworzenia na mapie. |
| `saveSpawns(const std::string& fileName)` | Zapisuje aktualny stan spawnow do pliku XML. |
| `internalLoadCreatureBuffer(...)` | Parsuje bufor XML z definicja stworzenia, tworzy obiekt `CreatureType` i dodaje go do listy. |
| `getCreatureByName(std::string name)` | Wyszukuje typ stworzenia po nazwie (z normalizacja wielkoLci liter). |
| `getCreatureByLook(int look)` | Wyszukuje typ stworzenia po jego ID wygladu (outfit ID lub item ID). |
| `getSpawn(...)` / `getSpawnForPlacePos(...)` | Wyszukuje spawn na podstawie pozycji. |
| `addSpawn(...)` | Dodaje nowy spawn lub aktualizuje istniejacy. |
| `deleteSpawn(...)` | Usuwa spawn z managera. |
## ZaleLLnoLci i powiazania
- **`map.h`**: Dodaje i usuwa stworzenia z mapy (`g_map`).
- **`creature.h`**: Tworzy instancje `Creature`.
- **`framework/xml/tinyxml.h`**: ULLywane do parsowania plikow XML.
- **`framework/core/resourcemanager.h`**: Do odczytu plikow z danymi.

---
# z"" effect.cpp
## Ogolny opis
Implementacja klasy `Effect`, ktora odpowiada za renderowanie efektow wizualnych na mapie, takich jak eksplozje, efekty magiczne itp.
## Klasa `Effect`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje efekt na ekranie. Oblicza aktualna faze animacji na podstawie czasu, ktory upL'ynaL' od pojawienia sie efektu. JeLli wL'aczona jest funkcja `GameEnhancedAnimations`, uLLywa `Animator::getPhaseAt` dla pL'ynniejszej, niezaleLLnej animacji. |
| `onAppear()` | Metoda wywoL'ywana, gdy efekt pojawia sie na mapie. Resetuje timer animacji i planuje automatyczne usuniecie efektu po zakoL"czeniu jego caL'kowitego czasu trwania. |
| `setId(uint32 id)` | Ustawia ID efektu, sprawdzajac jego poprawnoLc w `g_things`. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla danego efektu. |
## ZaleLLnoLci i powiazania
- **`map.h`**: ULLywa `g_map` do usuniecia efektu po zakoL"czeniu animacji.
- **`game.h`**: Sprawdza, czy wL'aczona jest funkcja `GameEnhancedAnimations`.
- **`framework/core/eventdispatcher.h`**: ULLywa `g_dispatcher` do planowania usuniecia.

---
# z"" global.h
## Ogolny opis
Plik nagL'owkowy, ktory peL'ni role centralnego punktu doL'aczania najwaLLniejszych plikow nagL'owkowych uLLywanych w caL'ym projekcie klienta.
## ZawartoLc
- **`#include <framework/global.h>`**: DoL'acza globalne definicje z warstwy frameworka.
- **`#include "const.h"`**: DoL'acza staL'e i typy wyliczeniowe specyficzne dla klienta gry.
- **`#include "position.h"`**: DoL'acza definicje klasy `Position`.
## Cel
Celem tego pliku jest uproszczenie doL'aczania nagL'owkow w innych plikach. Zamiast doL'aczac wiele podstawowych plikow, wystarczy doL'aczyc `global.h`.

---
# z"" effect.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Effect`, definiujacy jej interfejs.
## Klasa `Effect`
## Opis
Klasa `Effect` dziedziczy po `Thing` i reprezentuje krotkotrwaL'y efekt wizualny na mapie.
## StaL'e
- **`EFFECT_TICKS_PER_FRAME`**: DomyLlny czas trwania jednej klatki animacji efektu (75 ms).
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje efekt w danym miejscu na mapie. |
| `setId(uint32 id)` | Ustawia ID (typ) efektu. |
| `getId()` | Zwraca ID efektu. |
| `asEffect()` | Rzutuje wskaLsnik na `EffectPtr`. |
| `isEffect()` | Zwraca `true`. |
| `getThingType()` | Zwraca `ThingType` dla tego efektu. |
## ZaleLLnoLci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/core/timer.h`**: ULLywa `Timer` do Lledzenia postepu animacji.

---
# z"" healthbars.cpp
## Ogolny opis
Implementacja `HealthBars`, globalnego managera niestandardowych teL' dla paskow LLycia i many. UmoLLliwia L'adowanie i przypisywanie roLLnych grafik do paskow zdrowia w zaleLLnoLci od ID ubioru postaci.
## Klasa `HealthBars`
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` | Inicjalizuje wektory na paski LLycia i many, rezerwujac miejsce i dodajac `nullptr` jako domyLlny pasek (ID 0). |
| `terminate()` | CzyLci wszystkie zaL'adowane tL'a paskow. |
| `addHealthBackground(...)` | Dodaje nowe tL'o dla paska LLycia. Tworzy obiekt `HealthBar`, ustawia jego wL'aLciwoLci (LcieLLka, tekstura, offsety, wysokoLc) i dodaje go do wektora `m_healthBars`. |
| `addManaBackground(...)` | DziaL'a analogicznie do `addHealthBackground`, ale dla paskow many. |
| `getHealthBarPath(int id)` | Zwraca LcieLLke do pliku graficznego dla paska LLycia o danym ID. |
| `getManaBarPath(int id)` | Zwraca LcieLLke do pliku graficznego dla paska many o danym ID. |
| `getHealthBarOffset(int id)` | Zwraca przesuniecie tL'a dla paska LLycia. |
| `getManaBarOffset(int id)` | Zwraca przesuniecie tL'a dla paska many. |
| `getHealthBarOffsetBar(int id)` | Zwraca przesuniecie samego paska (wypeL'nienia) wewnatrz tL'a. |
| `getManaBarOffsetBar(int id)` | DziaL'a analogicznie dla paska many. |
| `getHealthBarHeight(int id)` | Zwraca wysokoLc paska LLycia. |
| `getManaBarHeight(int id)` | Zwraca wysokoLc paska many. |
## Klasa `HealthBar`
## Metody
| Nazwa | Opis |
| --- | --- |
| `setTexture(const std::string& path)` | Wczytuje teksture tL'a paska z podanej LcieLLki za pomoca `g_textures`. |
## Zmienne globalne
- `HealthBars g_healthBars`: Globalna instancja managera.
## ZaleLLnoLci i powiazania
- **`framework/graphics/texturemanager.h`**: ULLywa `g_textures` do L'adowania grafik.
- **`creature.cpp`**: Logika rysowania informacji o postaci (`drawInformation`) uLLywa `g_healthBars` do pobierania niestandardowych teL' paskow.

---
# z"" game.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Game`, ktora jest centralnym punktem zarzadzania stanem gry. Definiuje interfejs do obsL'ugi logowania, akcji gracza, komunikacji z serwerem oraz przechowywania stanu gry.
## Klasa `Game`
## Opis
Singleton (`g_game`) peL'niacy role fasady dla caL'ej logiki gry. Zarzadza sesja gracza, protokoL'em sieciowym, stanem lokalnego gracza i interakcjami ze Lwiatem gry.
## Struktury
- **`UnjustifiedPoints`**: Przechowuje informacje o punktach za nieuzasadnione zabojstwa w systemie PvP.
## Metody (Publiczne)
| Grupa | Metody | Opis |
| --- | --- | --- |
| **Zarzadzanie sesja** | `loginWorld`, `playRecord`, `cancelLogin`, `forceLogout`, `safeLogout` | Logowanie do Lwiata gry, odtwarzanie nagraL", wylogowywanie. |
| **Akcje gracza** | `walk`, `autoWalk`, `turn`, `stop`, `look`, `move`, `use`, `useWith` | WysyL'anie LLadaL" akcji gracza do serwera. |
| **Kontenery** | `open`, `close`, `refreshContainer` | Zarzadzanie kontenerami. |
| **Walka** | `attack`, `follow`, `cancelAttackAndFollow` | Zarzadzanie atakiem i Lledzeniem. |
| **Komunikacja** | `talk`, `talkChannel`, `talkPrivate` | WysyL'anie wiadomoLci. |
| **Zarzadzanie stanem** | `setProtocolVersion`, `setClientVersion`, `enableFeature`, `getFeature` | Konfiguracja klienta i obsL'uga funkcji serwera. |
| **Gettery** | `isOnline`, `isDead`, `getLocalPlayer`, `getProtocolGame`, `getPing` | Dostep do aktualnego stanu gry. |
## Metody (Chronione - Handlery ProtokoL'u)
Plik definiuje rownieLL liczne metody `process...`, ktore sa wywoL'ywane przez `ProtocolGame` w odpowiedzi na otrzymane pakiety z serwera. PrzykL'ady:
- `processLoginError`, `processEnterGame`
- `processTextMessage`, `processTalk`
- `processOpenContainer`, `processContainerAddItem`
- `processInventoryChange`
- `processWalkCancel`
## ZaleLLnoLci i powiazania
- **`declarations.h`**: ULLywa wielu zadeklarowanych typow (`ItemPtr`, `CreaturePtr`, etc.).
- **`protocolgame.h`**: LsciLle powiazana z protokoL'em sieciowym.
- **`localplayer.h`**: Zarzadza instancja `LocalPlayer`.
- **`container.h`**: Zarzadza kolekcja otwartych kontenerow.

---
# z"" healthbars.h
## Ogolny opis
Plik nagL'owkowy definiujacy klasy `HealthBar` i `HealthBars` do zarzadzania niestandardowymi tL'ami paskow LLycia i many.
## Klasa `HealthBar`
## Opis
Prosta klasa przechowujaca informacje o pojedynczym niestandardowym tle paska zdrowia lub many.
## Metody
| Nazwa | Opis |
| --- | --- |
| `setPath(const std::string& path)` | Ustawia LcieLLke do pliku graficznego. |
| `getPath()` | Zwraca LcieLLke. |
| `setTexture(const std::string& path)` | Laduje teksture. |
| `getTexture()` | Zwraca wskaLsnik do tekstury. |
| `setOffset(int x, int y)` | Ustawia przesuniecie (offset) caL'ego tL'a wzgledem punktu zaczepienia. |
| `getOffset()` | Zwraca przesuniecie. |
| `setBarOffset(int x, int y)` | Ustawia przesuniecie samego paska (wypeL'nienia) wewnatrz tL'a. |
| `getBarOffset()` | Zwraca przesuniecie paska. |
| `setHeight(int height)` | Ustawia wysokoLc paska. |
| `getHeight()` | Zwraca wysokoLc. |
## Klasa `HealthBars`
## Opis
Singleton (`g_healthBars`) zarzadzajacy kolekcja obiektow `HealthBar`. DziaL'a jako repozytorium dla wszystkich niestandardowych teL' paskow.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` | Inicjalizuje managera. |
| `terminate()` | Zwalnia zasoby. |
| `addHealthBackground(...)` | Dodaje nowe tL'o dla paska LLycia. |
| `addManaBackground(...)` | Dodaje nowe tL'o dla paska many. |
| `getHealthBar(int id)` | Zwraca obiekt `HealthBar` dla paska LLycia o danym ID. |
| `getManaBar(int id)` | Zwraca obiekt `HealthBar` dla paska many o danym ID. |
| `getHealthBarPath(int id)` | Zwraca LcieLLke do grafiki paska LLycia. |
| `getManaBarPath(int id)` | Zwraca LcieLLke do grafiki paska many. |
| `...` | Gettery dla pozostaL'ych wL'aLciwoLci paska. |
## Zmienne globalne
- `HealthBars g_healthBars`: Deklaracja zewnetrznej instancji managera.
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Podstawowe definicje.
- **`framework/graphics/declarations.h`**: Deklaracje typow graficznych, np. `TexturePtr`.

---
# z"" houses.cpp
## Ogolny opis
Implementacja klas `House` i `HouseManager`, ktore zarzadzaja danymi o domach w grze. Plik zawiera logike wczytywania i zapisywania danych o domach z/do plikow XML oraz zarzadzania ich stanem.
## Klasa `House`
## Metody
| Nazwa | Opis |
| --- | --- |
| `setTile(const TilePtr& tile)` | Dodaje pole do domu, ustawiajac na nim flage `TILESTATE_HOUSE` i ID domu. |
| `getTile(const Position& position)` | Zwraca pole na podanej pozycji, jeLli naleLLy ono do domu. |
| `addDoor(const ItemPtr& door)` | Dodaje drzwi do domu, przypisujac im unikalne, inkrementowane ID. |
| `removeDoorById(uint32 doorId)` | Usuwa drzwi o podanym ID (ustawia wskaLsnik na `nullptr` w wektorze). |
| `load(const TiXmlElement *elem)` | Wczytuje atrybuty domu (nazwa, czynsz, rozmiar, ID miasta, pozycja wejLcia) z wezL'a XML. |
| `save(TiXmlElement* elem)` | Zapisuje atrybuty domu do wezL'a XML. |
## Klasa `HouseManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addHouse(const HousePtr& house)` | Dodaje dom do listy, jeLli jeszcze nie istnieje. |
| `removeHouse(uint32 houseId)` | Usuwa dom o podanym ID. |
| `getHouse(uint32 houseId)` | Wyszukuje i zwraca dom po jego ID. |
| `getHouseByName(std::string name)` | Wyszukuje i zwraca dom po jego nazwie. |
| `load(const std::string& fileName)` | Wczytuje liste domow z pliku XML. Dla kaLLdego domu w pliku, jeLli juLL istnieje w menedLLerze, aktualizuje jego dane; w przeciwnym razie tworzy nowy. |
| `save(const std::string& fileName)` | Zapisuje liste wszystkich domow do pliku XML. |
| `filterHouses(uint32 townId)` | Zwraca liste domow naleLLacych do miasta o podanym ID. |
| `findHouse(uint32 houseId)` | Wewnetrzna metoda do wyszukiwania iteratora do domu na liLcie. |
| `sort()` | Sortuje liste domow alfabetycznie wedL'ug nazwy. |
## Zmienne globalne
- `HouseManager g_houses`: Globalna instancja managera domow.
## ZaleLLnoLci i powiazania
- **`map.h`**: Interakcje z obiektami `Tile` (`tile->setFlag(...)`).
- **`framework/core/resourcemanager.h`**: Do odczytu plikow XML z danymi domow.

---
# z"" item.cpp
## Ogolny opis
Implementacja klasy `Item`, ktora reprezentuje przedmioty w grze. Plik zawiera logike rysowania przedmiotow, obsL'uge ich atrybutow oraz serializacje/deserializacje do formatu binarnego (OTBM).
## Klasa `Item`
## Metody
| Nazwa | Opis |
| --- | --- |
| `create(int id, int countOrSubtype)` | Statyczna metoda fabryczna do tworzenia przedmiotu na podstawie jego ID klienta. |
| `createFromOtb(int id)` | Statyczna metoda fabryczna do tworzenia przedmiotu na podstawie jego ID serwera (z plikow OTB). |
| `getName()` | Zwraca nazwe przedmiotu na podstawie jego typu. |
| `draw(...)` | Rysuje przedmiot na ekranie. Oblicza faze animacji oraz wzor (pattern) na podstawie jego wL'aLciwoLci (np. liczba przedmiotow w stosie, typ pL'ynu). |
| `setId(uint32 id)` / `setOtbId(uint16 id)` | Ustawia ID przedmiotu, odpowiednio konwertujac miedzy ID klienta a serwera. |
| `unserializeItem(const BinaryTreePtr &in)` | Wczytuje atrybuty przedmiotu z binarnego drzewa (format OTBM). |
| `serializeItem(const OutputBinaryTreePtr& out)` | Zapisuje atrybuty przedmiotu do binarnego drzewa. |
| `getSubType()` | Zwraca podtyp przedmiotu (np. typ pL'ynu). |
| `getCount()` | Zwraca liczbe przedmiotow w stosie (jeLli jest stackable). |
| `clone()` | Tworzy i zwraca gL'eboka kopie przedmiotu. |
| `calculatePatterns(...)` | Oblicza, ktory wzor (pattern) sprite'a powinien byc uLLyty, w zaleLLnoLci od typu przedmiotu (stackable, hangable, fluid container). |
| `calculateAnimationPhase(bool animate)` | Oblicza bieLLaca klatke animacji. ObsL'uguje animacje synchroniczne i asynchroniczne. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla tego przedmiotu. |
## ZaleLLnoLci i powiazania
- **`thingtypemanager.h`**: ULLywa `g_things` do uzyskiwania informacji o typach przedmiotow.
- **`spritemanager.h`**: ULLywa `g_sprites` do pobierania danych o sprite'ach.
- **`game.h`**: ULLywa `g_game` do sprawdzania funkcji serwera (np. `GameNewFluids`).
- **`tile.h`**: Interakcje z polem, na ktorym leLLy przedmiot (np. do okreLlenia, jak zawiesic przedmiot).

---
# z"" itemtype.cpp
## Ogolny opis
Implementacja klasy `ItemType`, ktora reprezentuje szablon (typ) przedmiotu. Plik zawiera logike wczytywania definicji typow przedmiotow z binarnego formatu OTB.
## Klasa `ItemType`
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(const BinaryTreePtr& node)` | Deserializuje dane typu przedmiotu z wezL'a binarnego drzewa. Odczytuje kategorie przedmiotu oraz liste jego atrybutow, takich jak ID serwera, ID klienta, nazwa, czy jest zapisywalny itp. ObsL'uguje roLLnice w formacie w zaleLLnoLci od wersji klienta. |
## Logika serializacji
Metoda `unserialize` zawiera logike dostosowujaca wczytywanie atrybutow do roLLnych wersji klienta Tibii. Na przykL'ad, dla starszych wersji klienta, ID serwera musi byc dostosowane, aby poprawnie mapowac przedmioty.

> NOTE: Statyczna zmienna `lastId` jest uLLywana do tworzenia "pustych" typow przedmiotow, jeLli w pliku OTB wystepuja luki w numeracji ID serwera. Jest to mechanizm zapewniajacy spojnoLc indeksowania.
## ZaleLLnoLci i powiazania
- **`thingtypemanager.h`**: Jest LciLle powiazana z `ThingTypeManager`, ktory zarzadza wszystkimi typami przedmiotow i wywoL'uje `unserialize`.
- **`game.h`**: ULLywa `g_game` do sprawdzania wersji klienta, co wpL'ywa na logike parsowania.
- **`framework/core/binarytree.h`**: ULLywa `BinaryTree` do odczytu danych z formatu OTB.

---
# z"" item.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Item`, ktora reprezentuje konkretny przedmiot w grze.
## Klasa `Item`
## Opis
Dziedziczy po `Thing`. Reprezentuje instancje przedmiotu, ktora moLLe znajdowac sie na mapie, w kontenerze lub w ekwipunku gracza. Posiada wL'aLciwoLci takie jak ID, liczba/podtyp, kolor, a takLLe moLLe zawierac inne przedmioty, jeLli jest kontenerem.
## Typy wyliczeniowe
- **`ItemAttr`**: Definiuje klucze atrybutow, ktore moga byc przypisane do przedmiotu (np. `ATTR_COUNT`, `ATTR_ACTION_ID`, `ATTR_TEXT`).
## Metody
| Nazwa | Opis |
| --- | --- |
| `create(int id, ...)` | Statyczna metoda fabryczna do tworzenia przedmiotu po ID klienta. |
| `createFromOtb(int id)` | Statyczna metoda fabryczna do tworzenia przedmiotu po ID serwera (OTB). |
| `draw(...)` | Rysuje przedmiot na ekranie. |
| `setId(uint32 id)` | Ustawia ID klienta przedmiotu. |
| `setOtbId(uint16 id)` | Ustawia ID serwera (OTB) przedmiotu. |
| `setCountOrSubType(int value)` | Ustawia liczbe (dla przedmiotow stackowalnych) lub podtyp (dla pL'ynow, etc.). |
| `getCount()` | Zwraca liczbe przedmiotow. |
| `getSubType()` | Zwraca podtyp przedmiotu. |
| `getServerId()` | Zwraca ID serwera. |
| `unserializeItem(...)` | Wczytuje atrybuty przedmiotu z formatu binarnego. |
| `serializeItem(...)` | Zapisuje atrybuty przedmiotu do formatu binarnego. |
| `isContainer()` | Zwraca `true`, jeLli przedmiot jest kontenerem. |
| `clone()` | Tworzy gL'eboka kopie przedmiotu. |
| `getContainerItems()` | Zwraca liste przedmiotow wewnatrz, jeLli jest kontenerem. |
| `setCustomAttribute(...)` | Ustawia niestandardowy atrybut przedmiotu (funkcja dla serwerow niestandardowych). |
## ZaleLLnoLci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`itemtype.h`**: KaLLdy `Item` jest instancja jakiegoL `ItemType`.

---
# z"" itemtype.h
## Ogolny opis
Plik nagL'owkowy dla klasy `ItemType`, ktora reprezentuje szablon (typ) przedmiotu.
## Klasa `ItemType`
## Opis
Przechowuje niezmienne wL'aLciwoLci dla danego typu przedmiotu, wczytywane z plikow OTB. Wszystkie instancje `Item` o tym samym ID dziela jeden obiekt `ItemType`.
## Typy wyliczeniowe
- **`ItemCategory`**: Kategorie przedmiotow (broL", zbroja, pojemnik itp.).
- **`ItemTypeAttr`**: Atrybuty typu przedmiotu wczytywane z OTB.
- **`ClientVersion`**: Wersje klienta, uLLywane do obsL'ugi roLLnic w formatach plikow.
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(const BinaryTreePtr& node)` | Wczytuje dane typu przedmiotu z binarnego formatu OTB. |
| `setServerId(uint16 serverId)` | Ustawia ID serwera. |
| `getServerId()` | Zwraca ID serwera. |
| `setClientId(uint16 clientId)` | Ustawia ID klienta. |
| `getClientId()` | Zwraca ID klienta. |
| `getCategory()` | Zwraca kategorie przedmiotu. |
| `getName()` | Zwraca nazwe przedmiotu. |
| `isWritable()` | Zwraca `true`, jeLli na przedmiocie moLLna pisac. |
## ZaleLLnoLci i powiazania
- **`framework/luaengine/luaobject.h`**: Dziedziczy z `LuaObject`, aby byc dostepnym z Lua.
- **`framework/xml/tinyxml.h`**: ULLywane do parsowania dodatkowych danych z `items.xml`.

---
# z"" lightview.cpp
## Ogolny opis
Implementacja klasy `LightView`, ktora zarzadza i renderuje dynamiczne oLwietlenie na mapie.
## Klasa `LightView`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addLight(const Point& pos, uint8_t color, uint8_t intensity)` | Dodaje nowe LsrodL'o LwiatL'a do sceny. JeLli w tym samym miejscu istnieje juLL LwiatL'o o tym samym kolorze, wybierana jest wieksza intensywnoLc. |
| `setFieldBrightness(...)` | Ustawia jasnoLc dla danego pola na mapie. Ta metoda nie jest w peL'ni zaimplementowana i jej rola wydaje sie ograniczona. |
| `draw()` | GL'owna funkcja renderujaca. Przebiega przez wszystkie pola widoczne na ekranie i dla kaLLdego piksela oblicza finalny kolor LwiatL'a, sumujac wpL'yw globalnego oLwietlenia i wszystkich pobliskich LsrodeL' LwiatL'a. Wynik jest zapisywany do bufora, a nastepnie przesyL'any do tekstury (`m_lightTexture`), ktora jest rysowana na ekranie z trybem mieszania `CompositionMode_Multiply`, aby przyciemnic scene. |
## Logika renderowania
1.  Tworzony jest bufor pikseli o rozmiarze widocznego obszaru mapy.
2.  KaLLdy piksel w buforze jest inicjalizowany globalnym LwiatL'em otoczenia.
3.  Dla kaLLdego piksela iteruje sie przez wszystkie LsrodL'a LwiatL'a.
4.  Obliczana jest odlegL'oLc piksela od LsrodL'a LwiatL'a, a na jej podstawie intensywnoLc LwiatL'a w tym punkcie.
5.  Kolor LwiatL'a jest mieszany z kolorem piksela w buforze (wybierany jest najjaLniejszy kanaL' R, G, B).
6.  Po przetworzeniu wszystkich pikseli, bufor jest L'adowany do tekstury.
7.  Tekstura LwiatL'a jest rysowana na wierzchu sceny, przyciemniajac ja.
## ZaleLLnoLci i powiazania
- **`spritemanager.h`**: ULLywa `g_sprites.spriteSize()` do obliczeL" zwiazanych z rozmiarami pol.
- **`framework/graphics/painter.h`**: ULLywa `g_painter` do rysowania finalnej tekstury LwiatL'a.

---
# z"" lightview.h
## Ogolny opis
Plik nagL'owkowy dla klasy `LightView`, ktora jest odpowiedzialna za system dynamicznego oLwietlenia w grze.
## Struktura `TileLight`
## Opis
Prosta struktura przechowujaca informacje o Lwietle dla pojedynczego pola mapy.
- `start`: Indeks poczatkowy w liLcie LwiateL', od ktorego naleLLy zaczac obliczenia dla tego pola.
- `color`: Kolor LwiatL'a.
## Klasa `LightView`
## Opis
Dziedziczy po `DrawQueueItem`, co oznacza, LLe obiekty tej klasy moga byc dodawane do kolejki rysowania. `LightView` agreguje wszystkie LsrodL'a LwiatL'a w widocznym obszarze i renderuje je do jednej tekstury, ktora nastepnie jest nakL'adana na scene.
## Metody
| Nazwa | Opis |
| --- | --- |
| `LightView(...)` | Konstruktor. Inicjalizuje widok LwiatL'a z podanym rozmiarem, tekstura docelowa, globalnym kolorem i intensywnoLcia LwiatL'a. |
| `addLight(...)` | Dodaje LsrodL'o LwiatL'a w danej pozycji. |
| `setFieldBrightness(...)` | Ustawia jasnoLc dla danego pola (obecnie nie w peL'ni wykorzystywane). |
| `size()` | Zwraca liczbe LsrodeL' LwiatL'a. |
| `draw()` | Metoda renderujaca, ktora wykonuje obliczenia oLwietlenia i rysuje finalna teksture. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`thingtype.h`**: ULLywa struktury `Light` zdefiniowanej w `thingtype.h`.
- **`framework/graphics/drawqueue.h`**: Jest elementem kolejki rysowania.

---
# z"" localplayer.cpp
## Ogolny opis
Implementacja klasy `LocalPlayer`, ktora reprezentuje postac sterowana przez gracza. Rozszerza klase `Player` o logike specyficzna dla lokalnego gracza, taka jak obsL'uga ruchu inicjowanego przez klienta (pre-walking), blokady chodzenia, auto-walking oraz zarzadzanie statystykami.
## Klasa `LocalPlayer`
## Metody
| Nazwa | Opis |
| --- | --- |
| `lockWalk(int millis)` | Blokuje moLLliwoLc chodzenia na okreLlony czas, np. po uLLyciu przedmiotu. |
| `canWalk(Otc::Direction direction, ...)` | Sprawdza, czy gracz moLLe wykonac krok w danym kierunku. Uwzglednia blokady, paraliLL, trwajacy ruch oraz limity "pre-walkingu". |
| `walk(const Position& oldPos, const Position& newPos)` | ObsL'uguje ruch potwierdzony przez serwer. JeLli ruch odpowiada wykonanemu "pre-walk", usuwa go z kolejki. JeLli nie, traktuje to jako ruch wymuszony przez serwer (np. odepchniecie). |
| `preWalk(Otc::Direction direction)` | Inicjuje "pre-walking" - ruch wykonywany przez klienta przed potwierdzeniem z serwera, aby zniwelowac opoLsnienie sieciowe. Dodaje nowa pozycje do kolejki `m_preWalking`. |
| `cancelNewWalk(Otc::Direction dir)` | Anuluje wszystkie ruchy "pre-walk" w odpowiedzi na pakiet "cancel walk" z serwera. MoLLe probowac ponowic auto-walking. |
| `predictiveCancelWalk(...)` | Anuluje ruchy "pre-walk" na podstawie predykcji, jeLli serwer odrzuci krok w poL'owie LcieLLki. |
| `autoWalk(Position destination, ...)` | Inicjuje automatyczne poruszanie sie do celu. Asynchronicznie wyszukuje LcieLLke i wysyL'a ja do serwera. |
| `stopAutoWalk()` | Przerywa auto-walking. |
| `stopWalk()` | Natychmiastowo zatrzymuje wszelki ruch, czyszczac kolejke "pre-walk". |
| `updateWalkOffset(...)` | Specjalna implementacja dla "pre-walk", gdzie offset jest liczony w przeciwnym kierunku niLL normalny ruch. |
| `updateWalk()` | Aktualizuje stan chodzenia; koL"czy krok, gdy upL'ynie jego czas trwania. |
| `terminateWalk()` | Finalizuje krok, resetuje stan chodzenia i wywoL'uje callback `onWalkFinish`. |
| `onPositionChange(...)` | ObsL'uguje zmiane pozycji; jeLli osiagnieto cel auto-walk, zatrzymuje go. |
| `set...(...)` | Szereg metod `set` (np. `setHealth`, `setSkill`, `setExperience`), ktore aktualizuja stan lokalnego gracza i wywoL'uja odpowiednie callbacki Lua, informujac o zmianach. |
| `hasSight(const Position& pos)` | Sprawdza, czy dana pozycja jest w zasiegu wzroku gracza. |
## ZaleLLnoLci i powiazania
- **`map.h`**, **`tile.h`**: Do sprawdzania, czy pola sa moLLliwe do przejLcia.
- **`game.h`**: Do komunikacji z serwerem i zatrzymywania akcji gry.
- **`framework/core/eventdispatcher.h`**: Do planowania ponownych prob auto-walkingu.

---
# z"" map.cpp
## Ogolny opis
Implementacja klasy `Map`, ktora jest centralnym repozytorium dla wszystkich danych o Lwiecie gry. Plik zawiera logike zarzadzania polami (`Tile`), umieszczania na nich obiektow (`Thing`), wyszukiwania LcieLLek oraz zarzadzania widocznym obszarem mapy.
## Klasa `Map`
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizuje i zwalnia zasoby mapy. |
| `addMapView(...)` / `removeMapView(...)` | Dodaje i usuwa widoki mapy (`MapView`), ktore beda renderowac dane. |
| `notificateTileUpdate(...)` | Powiadamia wszystkie `MapView` o aktualizacji danego pola, co powoduje jego przerysowanie. |
| `clean()` / `cleanDynamicThings()` | CzyLci mape ze wszystkich pol lub tylko z obiektow dynamicznych (stworzenia, efekty). |
| `addThing(...)` | Dodaje obiekt (`Thing`) na mape w danej pozycji. ObsL'uguje specjalne przypadki dla pociskow, animowanych i statycznych tekstow (np. L'aczenie tekstow o obraLLeniach). |
| `getThing(...)` / `removeThing(...)` | Pobiera lub usuwa obiekt z mapy. |
| `getOrCreateTile(...)` | Zwraca istniejace pole lub tworzy nowe, jeLli nie istnieje. |
| `getTiles(...)` | Zwraca liste wszystkich pol na danym pietrze lub na caL'ej mapie. |
| `cleanTile(...)` | Usuwa wszystkie obiekty z danego pola. |
| `setCentralPosition(...)` | Ustawia pozycje kamery, co powoduje usuniecie obiektow spoza nowego zasiegu widzenia. |
| `getSpectators(...)` | Zwraca liste stworzeL" w zasiegu widzenia. |
| `isAwareOfPosition(...)` | Sprawdza, czy dana pozycja jest w zasiegu widzenia kamery. |
| `findPath(...)` | Implementacja algorytmu wyszukiwania LcieLLki A*. |
| `newFindPath(...)` | Nowsza, asynchroniczna implementacja wyszukiwania LcieLLki. |
| `findPathAsync(...)` | Uruchamia `newFindPath` w osobnym watku. |
| `findEveryPath(...)` | Implementacja algorytmu Dijkstry do znalezienia wszystkich moLLliwych LcieLLek w danym zasiegu. |
## Struktura danych
- **`m_tileBlocks`**: Pola mapy sa przechowywane w blokach 32x32, co optymalizuje zuLLycie pamieci. `std::map<uint, TileBlock> m_tileBlocks[Otc::MAX_Z+1]` przechowuje te bloki dla kaLLdego pietra.
- **`m_knownCreatures`**: Mapa znanych stworzeL", indeksowana po ich ID.
## ZaleLLnoLci i powiazania
- **`game.h`**: Dostep do stanu gry, np. funkcji serwera (`GameFeature`).
- **`localplayer.h`**: Do centrowania kamery i aktualizacji pozycji gracza.
- **`tile.h`**: Zarzadza obiektami `Tile`.
- **`mapview.h`**: Powiadamia `MapView` o zmianach.
- **`minimap.h`**: Aktualizuje minimape przy zmianach na polach.

---
# z"" luavaluecasts_client.h
## Ogolny opis
Plik nagL'owkowy definiujacy funkcje do konwersji (rzutowania) niestandardowych typow danych C++ na wartoLci Lua i z powrotem. Jest to kluczowy element integracji logiki gry z silnikiem skryptowym Lua.
## Funkcje
| Nazwa | Opis |
| --- | --- |
| `push_luavalue(const Outfit& outfit)` | Konwertuje obiekt `Outfit` na tabele Lua i umieszcza ja na stosie. |
| `luavalue_cast(int index, Outfit& outfit)` | Odczytuje tabele Lua ze stosu i konwertuje ja na obiekt `Outfit`. |
| `push_luavalue(const Position& pos)` | Konwertuje obiekt `Position` na tabele Lua (`{x=, y=, z=}`). |
| `luavalue_cast(int index, Position& pos)` | Odczytuje tabele Lua i konwertuje ja na obiekt `Position`. |
| `push_luavalue(const MarketData& data)` | Konwertuje strukture `MarketData` na tabele Lua. |
| `luavalue_cast(int index, MarketData& data)` | Odczytuje tabele Lua i konwertuje ja na `MarketData`. |
| `push_luavalue(const StoreCategory& category)` | Konwertuje `StoreCategory` na tabele Lua. |
| `luavalue_cast(int index, StoreCategory& data)` | Konwertuje tabele Lua na `StoreCategory`. |
| `push_luavalue(const StoreOffer& offer)` | Konwertuje `StoreOffer` na tabele Lua. |
| `luavalue_cast(int index, StoreOffer& offer)` | Konwertuje tabele Lua na `StoreOffer`. |
| `push_luavalue(const Imbuement& offer)` | Konwertuje `Imbuement` na tabele Lua. |
| `push_luavalue(const Light& light)` | Konwertuje `Light` na tabele Lua. |
| `luavalue_cast(int index, Light& light)` | Konwertuje tabele Lua na `Light`. |
| `push_luavalue(const UnjustifiedPoints& unjustifiedPoints)` | Konwertuje `UnjustifiedPoints` na tabele Lua. |
| `luavalue_cast(int index, UnjustifiedPoints& unjustifiedPoints)` | Konwertuje tabele Lua na `UnjustifiedPoints`. |
## ZaleLLnoLci i powiazania
- **`global.h`**, **`game.h`**, **`outfit.h`**: Zawieraja definicje typow, ktore sa konwertowane.
- **`framework/luaengine/declarations.h`**: Deklaracje funkcji z silnika Lua.
- **`luavaluecasts_client.cpp`**: Zawiera implementacje tych funkcji.

---
# z"" mapio.cpp
## Ogolny opis
Plik ten zawiera implementacje metod klasy `Map` odpowiedzialnych za operacje wejLcia/wyjLcia, czyli wczytywanie i zapisywanie danych mapy w formatach OTBM (OpenTibia Binary Map) i OTCM (OTClient Map).
## Klasa `Map`
## Metody
| Nazwa | Opis |
| --- | --- |
| `loadOtbm(const std::string& fileName)` | Wczytuje mape z pliku binarnego `.otbm`. Parsuje nagL'owek, sprawdza wersje i sygnature, a nastepnie iteruje przez wezL'y binarnego drzewa, tworzac pola (`Tile`), przedmioty (`Item`) oraz wczytujac informacje o miastach, domach i punktach nawigacyjnych (waypoints). |
| `saveOtbm(const std::string& fileName)` | Zapisuje aktualny stan mapy do pliku `.otbm`. Tworzy strukture binarnego drzewa, zapisuje nagL'owek, a nastepnie serializuje wszystkie pola, przedmioty na nich, a takLLe informacje o miastach, domach i waypointach. |
| `loadOtcm(const std::string& fileName)` | Wczytuje mape z wL'asnego, prostszego formatu klienta (`.otcm`). Format ten jest mniej rozbudowany niLL OTBM i przechowuje gL'ownie informacje o polach i przedmiotach. |
| `saveOtcm(const std::string& fileName)` | Zapisuje mape do formatu `.otcm`. |
## Logika wczytywania OTBM
1.  Otwiera plik i weryfikuje jego sygnature (`OTBM`).
2.  Odczytuje nagL'owek, zawierajacy wymiary mapy i wersje OTB.
3.  Parsuje gL'owny wezeL' danych, odczytujac atrybuty takie jak opis mapy oraz LcieLLki do plikow z danymi o spawnach i domach.
4.  Iteruje przez wezL'y `OTBM_TILE_AREA`, ktore grupuja pola w blokach.
5.  Dla kaLLdego pola (`OTBM_TILE`) odczytuje jego atrybuty (flagi, przedmioty). Przedmioty, ktore sa kontenerami, sa parsowane rekurencyjnie.
6.  Wczytuje definicje miast (`OTBM_TOWNS`) i waypointow (`OTBM_WAYPOINTS`).
## ZaleLLnoLci i powiazania
- **`tile.h`**, **`item.h`**: Tworzy obiekty `Tile` i `Item` na podstawie wczytanych danych.
- **`game.h`**: ULLywa `g_game` do sprawdzania funkcji serwera, ktore moga wpL'ywac na sposob parsowania.
- **`houses.h`**, **`towns.h`**: WypeL'nia menedLLery `g_houses` i `g_towns` danymi z mapy.
- **`framework/core/filestream.h`**, **`framework/core/binarytree.h`**: Narzedzia do obsL'ugi plikow binarnych i struktury drzewa binarnego.

---
# z"" luavaluecasts_client.cpp
## Ogolny opis
Implementacja funkcji do konwersji (rzutowania) niestandardowych typow danych C++ na wartoLci Lua i z powrotem. Ten plik zawiera logike "tL'umaczenia" zL'oLLonych obiektow C++ na tabele Lua i odwrotnie.
## Funkcje
## `push_luavalue`
Te funkcje przyjmuja jako argument obiekt C++ i umieszczaja jego reprezentacje w Lua na stosie. ZL'oLLone obiekty sa zazwyczaj konwertowane na tabele Lua.
- **`push_luavalue(const Outfit& outfit)`**: Tworzy tabele Lua z polami `type`, `auxType`, `head`, `body`, `legs`, `feet`, `addons`, `mount` etc. i wypeL'nia ja danymi z obiektu `Outfit`.
- **`push_luavalue(const Position& pos)`**: Tworzy tabele `{x, y, z}`.
- **`push_luavalue(const MarketData& data)`**: Tworzy tabele z danymi rynkowymi.
- **`push_luavalue(const Imbuement& i)`**: Tworzy zL'oLLona, zagnieLLdLLona tabele reprezentujaca imbuement, wL'aczajac w to liste materiaL'ow.
## `luavalue_cast`
Te funkcje przyjmuja jako argument indeks na stosie Lua i referencje do obiektu C++. Odczytuja wartoLc ze stosu (zwykle tabele) i wypeL'niaja obiekt C++ odpowiednimi danymi.
- **`luavalue_cast(int index, Outfit& outfit)`**: Odczytuje pola z tabeli Lua i ustawia odpowiednie wL'aLciwoLci w obiekcie `Outfit`.
- **`luavalue_cast(int index, Position& pos)`**: Odczytuje pola `x`, `y`, `z` z tabeli.
- **`luavalue_cast(int index, MarketData& data)`**: WypeL'nia strukture `MarketData`.
## ZaleLLnoLci i powiazania
- **`framework/luaengine/luainterface.h`**: Dostep do funkcji `g_lua` do manipulacji stosem Lua.
- **`game.h`**: ULLywa `g_game` do sprawdzania, ktore `GameFeature` sa aktywne, co wpL'ywa na to, ktore pola obiektu `Outfit` sa serializowane/deserializowane (np. `GamePlayerMounts`).
- **`luavaluecasts_client.h`**: Deklaracje tych funkcji.

---
# z"" mapview.cpp
## Ogolny opis
Implementacja klasy `MapView`, ktora jest odpowiedzialna za renderowanie widoku mapy. Plik zawiera skomplikowana logike okreLlania, ktore pola sa widoczne, jak je rysowac w odpowiedniej kolejnoLci (z uwzglednieniem pieter i efektu paralaksy) oraz jak zarzadzac oLwietleniem i tekstami na mapie.
## Klasa `MapView`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawMapBackground(...)` | GL'owna funkcja rysujaca tL'o mapy. Przygotowuje bufor ramki (`FrameBuffer`), inicjalizuje `LightView` (jeLli oLwietlenie jest wL'aczone) i rysuje wszystkie widoczne pietra, zaczynajac od najniLLszego. |
| `drawFloor(...)` | Rysuje pojedyncze pietro. Iteruje po `m_cachedVisibleTiles` i wywoL'uje metody `drawGround`, `drawBottom`, `drawCreatures` i `drawTop` dla kaLLdego pola (`Tile`). |
| `drawMapForeground(...)` | Rysuje elementy pierwszego planu, takie jak paski zdrowia, nazwy postaci, teksty (statyczne i animowane) oraz ostatecznie nakL'ada warstwe oLwietlenia. |
| `updateVisibleTilesCache()` | Kluczowa metoda optymalizacyjna. Oblicza, ktore pola sa widoczne dla kamery, i zapisuje je w pamieci podrecznej (`m_cachedVisibleTiles`). Sortuje je w kolejnoLci rysowania (diagonalnie), aby zachowac poprawna perspektywe 2.5D. |
| `updateGeometry(...)` | Aktualizuje geometrie widoku, w tym wymiary widoczne i wymiary bufora ramki. |
| `onTileUpdate(...)` / `onMapCenterChange(...)` | Metody wywoL'ywane przez `g_map`, ktore oznaczaja, LLe pamiec podreczna widocznych pol musi zostac zaktualizowana. |
| `calcFirstVisibleFloor(...)` / `calcLastVisibleFloor(...)` | Oblicza, ktore pietra sa widoczne dla gracza na podstawie jego pozycji i otoczenia (np. dziury w podL'odze, okna). |
| `transformPositionTo2D(...)` | Konwertuje pozycje 3D (x, y, z) na wspoL'rzedne 2D na ekranie, uwzgledniajac perspektywe izometryczna. |
| `getCameraPosition()` | Zwraca aktualna pozycje kamery, ktora albo podaLLa za stworzeniem (`m_followingCreature`), albo jest ustawiona recznie. |
## ZaleLLnoLci i powiazania
- **`map.h`**, **`tile.h`**: Intensywnie korzysta z `g_map` do pobierania danych o polach i obiektach.
- **`game.h`**: Dostep do `g_game` w celu pobrania lokalnego gracza i sprawdzenia funkcji serwera.
- **`lightview.h`**: Tworzy i zarzadza obiektem `LightView` do renderowania oLwietlenia.
- **`framework/graphics/framebuffermanager.h`**: ULLywa buforow ramki do optymalizacji renderowania.

---
# z"" mapview.h
## Ogolny opis
Plik nagL'owkowy dla klasy `MapView`. Definiuje interfejs widoku mapy, ktory jest gL'ownym komponentem renderujacym Lwiat gry.
## Klasa `MapView`
## Opis
Klasa `MapView` zarzadza kamera, widocznym obszarem mapy, a takLLe koordynuje proces rysowania wszystkich elementow Lwiata gry. MoLLe istniec wiele instancji `MapView`, co pozwala na renderowanie mapy w roLLnych miejscach interfejsu.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawMapBackground(...)` | Rysuje tL'o mapy (pola, obiekty na ziemi). |
| `drawMapForeground(...)` | Rysuje pierwszy plan (postacie, teksty, oLwietlenie). |
| `lockFirstVisibleFloor(int floor)` | Wymusza, aby najniLLszym widocznym pietrem byL'o podane pietro. |
| `unlockFirstVisibleFloor()` | WyL'acza wymuszone pietro. |
| `setVisibleDimension(const Size& dim)` | Ustawia wymiary widocznego obszaru w jednostkach pol (np. 15x11). |
| `followCreature(const CreaturePtr& creature)` | Ustawia kamere, aby podaLLaL'a za danym stworzeniem. |
| `setCameraPosition(const Position& pos)` | Ustawia kamere na staL'a pozycje. |
| `getCameraPosition()` | Zwraca aktualna pozycje kamery. |
| `getPosition(const Point& point, ...)` | Konwertuje wspoL'rzedne ekranu na pozycje na mapie. |
| `setDrawFlags(Otc::DrawFlags flags)` | Ustawia flagi rysowania, okreLlajace, co ma byc renderowane. |
| `setAnimated(bool animated)` | WL'acza/wyL'acza animacje. |
| `setFloorFading(int value)` | Ustawia czas zanikania/pojawiania sie pieter. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow (`Position`, `CreaturePtr`).
- **`lightview.h`**: ULLywa `LightView` do rysowania LwiateL'.
- **`framework/luaengine/luaobject.h`**: Dziedziczy z `LuaObject`.

---
# z"" minimap.h
## Ogolny opis
Plik nagL'owkowy dla `Minimap` i powiazanych struktur. Definiuje interfejs do zarzadzania danymi minimapy i jej renderowania.
## Struktury i staL'e
- **`MMBLOCK_SIZE`**: Rozmiar bloku minimapy (64x64 piksele).
- **`MinimapTileFlags`**: Flagi dla kafelka minimapy (np. `MinimapTileWasSeen`, `MinimapTileNotPathable`).
- **`MinimapTile`**: Struktura przechowujaca dane pojedynczego piksela minimapy (kolor, flagi, predkoLc).
## Klasa `MinimapBlock`
## Opis
Reprezentuje pojedynczy blok (chunk) minimapy o rozmiarze `MMBLOCK_SIZE` x `MMBLOCK_SIZE`. KaLLdy blok ma wL'asna teksture, co optymalizuje renderowanie.
- `m_texture`: Tekstura generowana na podstawie danych z `m_tiles`.
- `m_tiles`: Tablica `MinimapTile` przechowujaca dane dla kaLLdego piksela w bloku.
- `m_mustUpdate`: Flaga informujaca, czy tekstura wymaga ponownego wygenerowania.
## Klasa `Minimap`
## Opis
Singleton (`g_minimap`) zarzadzajacy wszystkimi danymi minimapy. Przechowuje `MinimapBlock` dla kaLLdego pietra i koordynuje ich rysowanie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizacja i zamykanie managera. |
| `clean()` | CzyLci wszystkie dane minimapy. |
| `draw(...)` | Rysuje minimape na ekranie w danym prostokacie. |
| `getTilePoint(const Position& pos, ...)` | Konwertuje pozycje na mapie na wspoL'rzedne na widLLecie minimapy. |
| `getTilePosition(const Point& point, ...)` | Konwertuje wspoL'rzedne na widLLecie minimapy na pozycje na mapie. |
| `updateTile(const Position& pos, const TilePtr& tile)` | Aktualizuje dane piksela minimapy na podstawie danych z `Tile`. |
| `getTile(const Position& pos)` | Zwraca dane `MinimapTile` dla danej pozycji. |
| `loadImage(...)` | Wczytuje dane minimapy z pliku graficznego (np. PNG). |
| `saveImage(...)` | Zapisuje widoczny obszar minimapy do pliku graficznego. |
| `loadOtmm(...)` / `saveOtmm(...)` | Wczytuje/zapisuje dane minimapy w formacie `.otmm`. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`tile.h`**: `updateTile` pobiera dane z obiektu `Tile`.

---
# z"" missile.cpp
## Ogolny opis
Implementacja klasy `Missile`, ktora odpowiada za renderowanie pociskow w grze.
## Klasa `Missile`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje pocisk na ekranie. Oblicza jego pozycje na LcieLLce lotu na podstawie czasu, ktory upL'ynaL' (`m_animationTimer.ticksElapsed() / m_duration`). Wybiera odpowiedni wzor (pattern) sprite'a na podstawie kierunku lotu. |
| `setPath(const Position& fromPosition, const Position& toPosition)` | Ustawia LcieLLke lotu pocisku od pozycji poczatkowej do koL"cowej. Oblicza kierunek, czas trwania lotu i planuje automatyczne usuniecie pocisku po dotarciu do celu. |
| `setId(uint32 id)` | Ustawia ID (typ) pocisku, weryfikujac jego poprawnoLc. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla danego pocisku. |
## Logika animacji
Pozycja pocisku jest interpolowana liniowo miedzy punktem startowym a koL"cowym. Frakcja postepu `fraction` jest obliczana jako stosunek czasu, ktory upL'ynaL', do caL'kowitego czasu trwania lotu. Przesuniecie rysowania `m_delta * fraction` jest dodawane do pozycji poczatkowej.
## ZaleLLnoLci i powiazania
- **`map.h`**: ULLywa `g_map` do usuniecia pocisku po zakoL"czeniu lotu.
- **`spritemanager.h`**: ULLywa `g_sprites.spriteSize()` do skalowania przesuniecia.
- **`framework/core/eventdispatcher.h`**: ULLywa `g_dispatcher` do planowania usuniecia.

---
# z"" missile.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Missile`, ktora reprezentuje pociski i inne efekty dystansowe.
## Klasa `Missile`
## Opis
Dziedziczy po `Thing`. Reprezentuje obiekt, ktory przemieszcza sie od jednej pozycji do drugiej w okreLlonym czasie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje pocisk w jego aktualnej pozycji na LcieLLce. |
| `setId(uint32 id)` | Ustawia ID (typ) pocisku. |
| `setPath(const Position& from, const Position& to)` | Ustawia poczatek i koniec LcieLLki pocisku. |
| `getId()` | Zwraca ID pocisku. |
| `asMissile()` | Rzutuje wskaLsnik na `MissilePtr`. |
| `isMissile()` | Zwraca `true`. |
| `getThingType()` | Zwraca `ThingType` dla pocisku. |
| `getSource()` | Zwraca pozycje poczatkowa. |
| `getDestination()` | Zwraca pozycje koL"cowa. |
## ZaleLLnoLci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/core/timer.h`**: ULLywa `Timer` do animacji ruchu.

---
# z"" outfit.cpp
## Ogolny opis
Implementacja klasy `Outfit` oraz niestandardowych elementow kolejki rysowania `DrawQueueItemOutfit` i `DrawQueueItemOutfitWithShader`. Plik zawiera zL'oLLona logike rysowania ubioru postaci, w tym warstw, kolorow, dodatkow, wierzchowcow, skrzydeL', aury i shaderow.
## Klasa `Outfit`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(Point dest, ...)` | GL'owna funkcja rysujaca ubior. Wykonuje nastepujace kroki: <br> 1. Koryguje kierunek. <br> 2. Oblicza faze animacji (chodzenia, bezczynnoLci, UI). <br> 3. Rysuje aure (tylna warstwe, jeLli dotyczy). <br> 4. Rysuje wierzchowca. <br> 5. Rysuje skrzydL'a (w zaleLLnoLci od kierunku, przed lub za postacia). <br> 6. Rysuje poszczegolne warstwy ubioru (podstawe i dodatki), kolorujac je za pomoca specjalnego shadera (`DrawQueueItemOutfit`). <br> 7. Rysuje aure (przednia warstwe). |
| `draw(const Rect& dest, ...)` | Wersja rysujaca ubior przeskalowany do danego prostokata, uLLywana w UI. |
| `resetClothes()` | Resetuje wszystkie elementy ubioru (gL'owa, ciaL'o, etc.) do wartoLci domyLlnych (0). |
## Klasy `DrawQueueItem...`
## Opis
Niestandardowe elementy kolejki rysowania, ktore pozwalaja na zaawansowane renderowanie ubiorow.
- **`DrawQueueItemOutfit`**: ULLywa specjalnego shadera (`outfit.frag`), ktory na podstawie 32-bitowej liczby `m_colors` i tekstury z warstwami, koloruje kaLLda z czterech czeLci ubioru (gL'owa, ciaL'o, nogi, stopy) na odpowiedni kolor.
- **`DrawQueueItemOutfitWithShader`**: Rozszerza powyLLsza logike o dodatkowy, niestandardowy shader (np. efekt "ghost"), ktory jest nakL'adany na finalny obraz ubioru.
## ZaleLLnoLci i powiazania
- **`game.h`**: Sprawdza, ktore `GameFeature` sa aktywne, aby decydowac, ktore elementy ubioru rysowac (np. wierzchowce, skrzydL'a).
- **`thingtypemanager.h`**: ULLywa `g_things` do pobierania `ThingType` dla ubioru, wierzchowca, skrzydeL', aury.
- **`spritemanager.h`**: ULLywa `g_sprites` do skalowania i pozycjonowania.
- **`framework/graphics/drawqueue.h`**: Dodaje niestandardowe elementy do kolejki rysowania.
- **`framework/graphics/shadermanager.h`**: Zarzadza i uLLywa shaderow do kolorowania i efektow.

---
# z"" outfit.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Outfit` oraz powiazanych struktur do rysowania.
## Klasa `Outfit`
## Opis
Reprezentuje wyglad (ubior) postaci. Przechowuje informacje o ID wygladu, kolorach poszczegolnych czeLci ciaL'a, dodatkach, wierzchowcu, skrzydL'ach, aurze i niestandardowym shaderze.
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Dwie przeciaLLone wersje funkcji rysujacej ubior: jedna w punkcie (na mapie), druga w prostokacie (w UI). |
| `setId(int id)` | Ustawia ID ubioru (dla potworow) lub przedmiotu (dla niewidzialnoLci). |
| `setHead(int head)` | Ustawia kolor gL'owy. |
| `setBody(int body)` | Ustawia kolor torsu. |
| `setLegs(int legs)` | Ustawia kolor nog. |
| `setFeet(int feet)` | Ustawia kolor stop. |
| `setAddons(int addons)` | Ustawia dodatki (bitmaska). |
| `setMount(int mount)` | Ustawia ID wierzchowca. |
| `setWings(int wings)` | Ustawia ID skrzydeL'. |
| `setAura(int aura)` | Ustawia ID aury. |
| `setShader(const std::string& shader)` | Ustawia nazwe niestandardowego shadera. |
## Struktury `DrawQueueItem...`
## Opis
Definicje niestandardowych elementow kolejki rysowania, ktore obsL'uguja zaawansowane renderowanie ubiorow.
- **`DrawQueueItemOutfit`**: Renderuje ubior z dynamicznym kolorowaniem poszczegolnych czeLci.
- **`DrawQueueItemOutfitWithShader`**: Dodaje obsL'uge niestandardowego shadera efektow specjalnych.
## ZaleLLnoLci i powiazania
- **`thingtypemanager.h`**: ULLywa `ThingCategory` i `ThingType`.
- **`framework/graphics/drawqueue.h`**: Dziedzicza z `DrawQueueItemTexturedRect`.

---
# z"" player.cpp
## Ogolny opis
Ten plik jest obecnie pusty, co oznacza, LLe klasa `Player` nie posiada LLadnej dodatkowej implementacji poza tym, co dziedziczy z klasy `Creature`.
## Klasa `Player`
## Opis
Klasa `Player` jest specjalizacja `Creature`. SL'uLLy do reprezentowania postaci graczy w grze. W przyszL'oLci moLLe zawierac logike specyficzna tylko dla graczy, ktora nie dotyczy potworow czy NPC.
## ZaleLLnoLci i powiazania
- **`player.h`**: Plik nagL'owkowy dla tej implementacji.

---
# z"" player.h
## Ogolny opis
Plik nagL'owkowy dla klasy `Player`, ktora jest specjalizacja klasy `Creature`.
## Klasa `Player`
## Opis
Dziedziczy po `Creature`. Reprezentuje postac gracza (niekoniecznie lokalnego). Nie dodaje LLadnych nowych pol ani metod, ale sL'uLLy do rozroLLnienia typow stworzeL" w systemie typow C++.
## Metody
| Nazwa | Opis |
| --- | --- |
| `asPlayer()` | Rzutuje wskaLsnik na `PlayerPtr`. |
| `isPlayer()` | Zwraca `true`. |
## ZaleLLnoLci i powiazania
- **`creature.h`**: Klasa bazowa.

---
# z"" protocolcodes.cpp
## Ogolny opis
Implementacja funkcji pomocniczych zadeklarowanych w `protocolcodes.h`. GL'ownym zadaniem tego pliku jest zarzadzanie mapowaniem trybow wiadomoLci (`Otc::MessageMode`) na ich liczbowe odpowiedniki uLLywane w protokole sieciowym, ktore moga sie roLLnic w zaleLLnoLci od wersji klienta.
## Namespace `Proto`
## Zmienne globalne
- **`std::map<uint8, uint8> messageModesMap`**: Mapa przechowujaca powiazanie miedzy wewnetrznym enumem `Otc::MessageMode` a wartoLcia liczbowa wysyL'ana/odbierana z serwera.
## Funkcje
| Nazwa | Opis |
| --- | --- |
| `buildMessageModesMap(int version)` | WypeL'nia `messageModesMap` na podstawie podanej wersji protokoL'u. Zawiera bloki `if/else if` dla roLLnych zakresow wersji, definiujac odpowiednie mapowania. Jest to kluczowe dla zachowania kompatybilnoLci wstecznej. |
| `translateMessageModeFromServer(uint8 mode)` | TL'umaczy liczbowy tryb wiadomoLci otrzymany z serwera na wewnetrzny enum `Otc::MessageMode`. |
| `translateMessageModeToServer(Otc::MessageMode mode)` | TL'umaczy wewnetrzny enum `Otc::MessageMode` na jego liczbowy odpowiednik, ktory zostanie wysL'any do serwera. |
## ZaleLLnoLci i powiazania
- **`protocolcodes.h`**: Deklaracje funkcji i enumow.
- **`game.cpp`**: `Game::setProtocolVersion` wywoL'uje `buildMessageModesMap`, aby zaktualizowac mapowania po zmianie wersji protokoL'u.

---
# z"" minimap.cpp
## Ogolny opis
Implementacja `Minimap` i `MinimapBlock`, ktore razem tworza system minimapy w grze. Plik zawiera logike renderowania, aktualizacji danych, a takLLe wczytywania i zapisywania minimapy w formatach `.otmm` i graficznych.
## Klasa `MinimapBlock`
## Metody
| Nazwa | Opis |
| --- | --- |
| `clean()` | Resetuje wszystkie dane w bloku do stanu poczatkowego. |
| `update()` | JeLli blok zostaL' zmodyfikowany (`m_mustUpdate`), generuje nowa teksture na podstawie danych z `m_tiles`. Tworzy obiekt `Image`, wypeL'nia go kolorami pikseli, a nastepnie tworzy z niego teksture. |
| `updateTile(...)` | Aktualizuje dane pojedynczego piksela w bloku i ustawia flage `m_mustUpdate`. |
## Klasa `Minimap`
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje minimape na ekranie. Oblicza, ktore bloki (`MinimapBlock`) sa widoczne, aktualizuje ich tekstury (jeLli to konieczne), a nastepnie rysuje je w odpowiednich pozycjach. |
| `getTilePoint(...)` / `getTilePosition(...)` | Funkcje pomocnicze do konwersji miedzy pozycja na mapie a wspoL'rzednymi na widLLecie minimapy. |
| `updateTile(const Position& pos, const TilePtr& tile)` | Pobiera kolor i flagi z `Tile` i aktualizuje odpowiadajacy mu piksel w `MinimapBlock`. |
| `getTile(const Position& pos)` | Zwraca dane `MinimapTile` dla danej pozycji. |
| `threadGetTile(...)` | Wersja `getTile` bezpieczna dla watkow, uLLywana przez asynchroniczne wyszukiwanie LcieLLki. |
| `loadImage(...)` | Wczytuje dane minimapy z pliku graficznego, analizujac kolory pikseli w celu okreLlenia wL'aLciwoLci (np. czy pole jest moLLliwe do przejLcia). |
| `saveOtmm(...)` / `loadOtmm(...)` | ObsL'uguje serializacje/deserializacje danych minimapy do/z formatu `.otmm`, ktory uLLywa kompresji zlib dla kaLLdego bloku. |
## Struktura danych
- `m_tileBlocks`: Tablica map `std::unordered_map<uint, MinimapBlock_ptr>`, gdzie kaLLdy element tablicy odpowiada jednemu pietru (`z`). Mapa przechowuje bloki minimapy, indeksowane przez skrot ich pozycji.
## ZaleLLnoLci i powiazania
- **`tile.h`**: Pobiera dane do aktualizacji minimapy z obiektow `Tile`.
- **`game.h`**: ULLywa `g_game` do sprawdzania funkcji, np. `GameDontCacheFiles`.
- **`framework/graphics/...`**: ULLywa klas `Image`, `Texture`, `Painter` do operacji graficznych.
- **`framework/core/resourcemanager.h`**: Do operacji na plikach.
- **`zlib.h`**: Do kompresji/dekompresji danych w formacie `.otmm`.

---
# z"" position.h
## Ogolny opis
Plik nagL'owkowy definiujacy strukture `Position` oraz powiazane z nia funkcje pomocnicze. Jest to fundamentalna struktura uLLywana w caL'ym projekcie do reprezentowania wspoL'rzednych w trojwymiarowym Lwiecie gry.
## Struktura `Position`
## Pola
- `int x`, `int y`: WspoL'rzedne na pL'aszczyLsnie poziomej.
- `short z`: WspoL'rzedna pietra.
## Metody
| Nazwa | Opis |
| --- | --- |
| `Position(uint16 x, uint16 y, uint8 z)` | Konstruktor. |
| `translatedToDirection(Otc::Direction direction)` | Zwraca nowa pozycje przesunieta o jedno pole w danym kierunku. |
| `translatedToReverseDirection(...)` | Zwraca nowa pozycje przesunieta w kierunku przeciwnym. |
| `translatedToDirections(...)` | Przetwarza liste kierunkow i zwraca liste kolejnych pozycji na LcieLLce. |
| `getAngleFromPositions(from, to)` | Statyczna metoda obliczajaca kat (w radianach) miedzy dwiema pozycjami. |
| `getDirectionFromPositions(from, to)` | Statyczna metoda zwracajaca kierunek (`Otc::Direction`) z jednej pozycji do drugiej. |
| `isMapPosition()` | Sprawdza, czy pozycja jest poprawna pozycja na mapie. |
| `isValid()` | Sprawdza, czy pozycja jest "waLLna" (roLLna od pozycji specjalnej 65535, 65535, 255). |
| `distance(const Position& pos)` | Oblicza dystans euklidesowy. |
| `manhattanDistance(const Position& pos)` | Oblicza odlegL'oLc w metryce taksowkowej. |
| `up()`, `down()`, `coveredUp()`, `coveredDown()` | Metody do przemieszczania sie miedzy pietrami z uwzglednieniem perspektywy izometrycznej. |
| `toString()` | Zwraca pozycje w formacie "x,y,z". |
| `operator==`, `operator!=`, `operator<` | Operatory porownania. |
| `operator+`, `operator-` | Operatory arytmetyczne. |
## Struktura `PositionHasher`
## Opis
Funktor uLLywany do haszowania obiektow `Position`, co pozwala na uLLywanie ich jako kluczy w kontenerach `std::unordered_map`.
## ZaleLLnoLci i powiazania
- **`const.h`**: Definicje `Otc::Direction` i `Otc::MAX_Z`.
- Plik ten jest doL'aczany w niemal kaLLdym pliku, ktory operuje na logice Lwiata gry.

---
# z"" protocolcodes.h
## Ogolny opis
Plik nagL'owkowy definiujacy kody operacyjne (opcodes) uLLywane w protokole sieciowym miedzy klientem a serwerem gry. Zawiera rownieLL definicje typow stworzeL" i mapowanie trybow wiadomoLci.
## Namespace `Proto`
## Typy wyliczeniowe
- **`LoginServerOpts`**: Kody operacyjne uLLywane podczas komunikacji z serwerem logowania.
- **`ItemOpcode`**: Specjalne ID uLLywane do identyfikacji stworzeL" i tekstow w strumieniu danych o polach mapy.
- **`GameServerOpcodes`**: Kody operacyjne dla pakietow wysyL'anych z serwera do klienta. Lista jest dL'uga i zawiera kody dla wszystkich akcji w grze, takich jak logowanie, ruch postaci, aktualizacje mapy, wiadomoLci, handel itp.
- **`ClientOpcodes`**: Kody operacyjne dla pakietow wysyL'anych z klienta do serwera.
- **`CreatureType`**: Typy stworzeL" (gracz, potwor, NPC).
- **`CreaturesIdRange`**: Zakresy ID dla roLLnych typow stworzeL".
## Funkcje
- **`buildMessageModesMap(int version)`**: Buduje mape tL'umaczaca wewnetrzne tryby wiadomoLci na kody protokoL'u dla danej wersji.
- **`translateMessageModeFromServer(uint8 mode)`**: Konwertuje kod z serwera na `Otc::MessageMode`.
- **`translateMessageModeToServer(Otc::MessageMode mode)`**: Konwertuje `Otc::MessageMode` na kod dla serwera.

> NOTE: Lista opkodow zawiera zarowno standardowe kody z protokoL'u Tibii, jak i niestandardowe kody specyficzne dla OTClient (`OTClientV8 64-79`) i rozszerzone opkody (`GameServerExtendedOpcode`).
## ZaleLLnoLci i powiazania
- **`global.h`**: Podstawowe definicje.
- Ten plik jest kluczowy dla `ProtocolGame`, ktory uLLywa tych kodow do identyfikacji i parsowania pakietow sieciowych.

---
# z"" protocolgame.cpp
## Ogolny opis
Implementacja czeLci klasy `ProtocolGame` odpowiedzialnej za zarzadzanie poL'aczeniem i podstawowa obsL'uge zdarzeL" sieciowych.
## Klasa `ProtocolGame`
## Metody
| Nazwa | Opis |
| --- | --- |
| `login(...)` | Inicjuje proces logowania, zapisujac dane uwierzytelniajace i dane Lwiata, a nastepnie nawiazuje poL'aczenie z serwerem. |
| `onConnect()` | Metoda wywoL'ywana po pomyLlnym nawiazaniu poL'aczenia. WL'acza odpowiednie funkcje protokoL'u (np. sumy kontrolne, szyfrowanie, duLLe pakiety) w zaleLLnoLci od `GameFeature` i wysyL'a pierwszy pakiet logowania. |
| `onRecv(const InputMessagePtr& inputMessage)` | GL'owna petla odbioru danych. WywoL'ywana za kaLLdym razem, gdy nadejdzie nowy pakiet. Weryfikuje rozmiar wiadomoLci (jeLli `GameMessageSizeCheck` jest aktywne), a nastepnie przekazuje pakiet do `parseMessage` w celu przetworzenia. Po przetworzeniu planuje odbior kolejnego pakietu. |
| `onError(const boost::system::error_code& error)` | ObsL'uguje bL'edy poL'aczenia. Powiadamia `g_game` o bL'edzie i rozL'acza klienta. |
## ZaleLLnoLci i powiazania
- **`game.h`**: LsciLle wspoL'pracuje z `g_game`, informujac go o stanie poL'aczenia i przekazujac przetworzone dane.
- **`player.h`**, **`localplayer.h`**: Ustawia instancje `LocalPlayer` na poczatku poL'aczenia.
- **`framework/net/protocol.h`**: Dziedziczy z `Protocol` i wykorzystuje jego mechanizmy do obsL'ugi poL'aczenia TCP.

---
# z"" protocolgame.h
## Ogolny opis
Plik nagL'owkowy dla klasy `ProtocolGame`. Definiuje interfejs protokoL'u sieciowego uLLywanego do komunikacji z serwerem gry. Zawiera deklaracje funkcji do wysyL'ania pakietow oraz parsowania odpowiedzi z serwera.
## Klasa `ProtocolGame`
## Opis
Dziedziczy po `Protocol`. Jest to centralny punkt obsL'ugi komunikacji sieciowej w grze.
## Metody (WysyL'anie)
Plik deklaruje duLLa liczbe metod `send...`, z ktorych kaLLda odpowiada za wysL'anie konkretnego pakietu do serwera. PrzykL'ady:
- `sendLoginPacket(...)`: WysyL'a pakiet logowania.
- `sendWalkNorth()`: WysyL'a LLadanie ruchu na poL'noc.
- `sendMove(...)`: WysyL'a LLadanie przesuniecia przedmiotu.
- `sendTalk(...)`: WysyL'a wiadomoLc czatu.
- `sendAttack(...)`: WysyL'a LLadanie ataku.
## Metody (Parsowanie)
Deklaruje rownieLL metody `parse...`, ktore sa wywoL'ywane w `protocolgameparse.cpp` do przetwarzania pakietow przychodzacych z serwera. PrzykL'ady:
- `parseMapDescription(...)`: Parsuje peL'ny opis mapy.
- `parseCreatureHealth(...)`: Parsuje aktualizacje LLycia stworzenia.
- `parseTextMessage(...)`: Parsuje wiadomoLc tekstowa.
## Metody (Pomocnicze)
- `getThing(...)`, `getItem(...)`, `getCreature(...)`, `getPosition(...)`: Funkcje pomocnicze do odczytywania zL'oLLonych typow danych ze strumienia `InputMessage`.
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow (`Position`, `CreaturePtr`, etc.).
- **`protocolcodes.h`**: ULLywa kodow operacyjnych zdefiniowanych w tym pliku.
- **`framework/net/protocol.h`**: Klasa bazowa.

---
# z"" spritemanager.cpp
## Ogolny opis
Implementacja `SpriteManager`, klasy odpowiedzialnej za zarzadzanie plikami sprite'ow (`.spr`, `.cwm`). Plik zawiera logike wczytywania, zapisywania, a takLLe deszyfrowania i dekompresji danych sprite'ow.
## Klasa `SpriteManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `loadSpr(std::string file)` | GL'owna funkcja wczytujaca. Sprawdza, czy istnieje plik `.cwm` (HD mod) lub `.spr` i wywoL'uje odpowiednia metode wczytujaca. |
| `saveSpr(...)` / `saveSpr64(...)` | Metody do zapisywania sprite'ow w formacie `.spr` (32x32 lub 64x64). Wymaga `WITH_ENCRYPTION`. |
| `encryptSprites(...)` | Zapisuje sprite'y w niestandardowym, zaszyfrowanym formacie OTV8. |
| `dumpSprites(...)` | Zapisuje wszystkie sprite'y jako pojedyncze pliki PNG do danego folderu (funkcja deweloperska). |
| `unload()` | Zwalnia wszystkie zasoby zwiazane ze sprite'ami. |
| `getSpriteImage(int id)` | GL'owna metoda do pobierania obrazu sprite'a. WywoL'uje odpowiednia implementacje w zaleLLnoLci od tego, czy zaL'adowano mod HD (`.cwm`) czy standardowy plik (`.spr`). |
| `loadCasualSpr(...)` | Wczytuje standardowy plik `.spr`. Odczytuje sygnature i liczbe sprite'ow. ObsL'uguje rownieLL zaszyfrowany format OTV8. |
| `loadCwmSpr(...)` | Wczytuje plik `.cwm`, ktory jest zbiorem skompresowanych danych PNG. ULLywa `PngUnpacker` do rozpakowania wszystkich sprite'ow do pamieci. |
| `getSpriteImageCasual(int id)` | Pobiera obraz sprite'a z pliku `.spr`. Odczytuje adres sprite'a z tablicy offsetow, a nastepnie dekompresuje dane pikseli, ktore sa zapisane w formacie RLE (run-length encoding) z przezroczystymi i kolorowymi pikselami. |
| `getSpriteImageHd(int id)` | Pobiera obraz sprite'a z pamieci podrecznej wczytanej z pliku `.cwm`. Dekoduje dane PNG dla danego sprite'a. |
## ZaleLLnoLci i powiazania
- **`game.h`**: ULLywa `g_game` do sprawdzania `GameFeature`, ktore wpL'ywaja na format pliku `.spr`.
- **`framework/core/resourcemanager.h`**: Do operacji na plikach.
- **`framework/graphics/image.h`**: Zwraca obiekty `ImagePtr`.
- **`framework/util/crypt.h`**: Do deszyfrowania formatu OTV8.
- **`framework/util/pngunpacker.h`**: Do rozpakowywania plikow `.cwm`.

---
# z"" protocolgamesend.cpp
## Ogolny opis
Plik ten zawiera implementacje metod klasy `ProtocolGame` odpowiedzialnych za **wysyL'anie** pakietow do serwera gry. KaLLda metoda odpowiada za stworzenie i wysL'anie konkretnego komunikatu zgodnie z protokoL'em sieciowym.
## Klasa `ProtocolGame`
## Metody
| Nazwa | Opis |
| --- | --- |
| `send(const OutputMessagePtr& outputMessage, ...)` | WysyL'a przygotowany pakiet, sprawdzajac uprzednio zabezpieczenia anty-botowe (`g_game.checkBotProtection()`). |
| `sendLoginPacket(...)` | Tworzy i wysyL'a pakiet logowania. Zawiera logike szyfrowania RSA, dodawania klucza XTEA, a takLLe wysyL'ania dodatkowych danych identyfikacyjnych klienta (nazwa uLLytkownika, CPU, adresy MAC), jeLli serwer to obsL'uguje. |
| `sendWalkNorth()`, `sendWalkEast()`, etc. | WysyL'aja jednobajtowe pakiety z LLadaniem ruchu w danym kierunku. |
| `sendAutoWalk(...)` | WysyL'a sekwencje kierunkow dla automatycznego poruszania sie. |
| `sendNewWalk(...)` | WysyL'a pakiet dla nowego systemu chodzenia, zawierajacy ID kroku, ID predykcji, pozycje i LcieLLke. |
| `sendMove(...)` | WysyL'a LLadanie przesuniecia przedmiotu/stworzenia. |
| `sendUseItem(...)`, `sendUseItemWith(...)` | WysyL'aja LLadania uLLycia przedmiotow. |
| `sendTalk(...)` | WysyL'a wiadomoLc czatu. Konstruuje pakiet w zaleLLnoLci od trybu wiadomoLci (publiczny, prywatny, kanaL'). |
| `sendAttack(...)`, `sendFollow(...)` | WysyL'aja LLadania ataku lub Lledzenia stworzenia, zawierajac sekwencyjny numer identyfikujacy akcje. |
| `sendChangeOutfit(...)` | WysyL'a nowy ubior gracza, uwzgledniajac wszystkie jego elementy (kolory, dodatki, wierzchowiec, etc.) w zaleLLnoLci od wspieranych przez serwer funkcji. |
| `addPosition(const OutputMessagePtr& msg, ...)` | Pomocnicza metoda do dodawania wspoL'rzednych `Position` do pakietu. |
## Logika
WiekszoLc funkcji w tym pliku ma prosta strukture:
1.  Stworz nowy `OutputMessage`.
2.  Dodaj kod operacyjny (opcode) za pomoca `msg->addU8(...)`.
3.  Dodaj kolejne dane (ID, pozycje, stringi) zgodnie ze specyfikacja protokoL'u.
4.  WyLlij pakiet za pomoca `send(msg)`.
## ZaleLLnoLci i powiazania
- **`game.h`**: ULLywa `g_game` do sprawdzania funkcji serwera (`GameFeature`), ktore determinuja format wysyL'anych pakietow.
- **`localplayer.h`**: ULLywa pozycji lokalnego gracza w niektorych pakietach (np. `sendTalk`).
- **`framework/util/crypt.h`**: ULLywa `g_crypt` do szyfrowania RSA.
- **`framework/platform/platform.h`**: Pobiera informacje o systemie do wysL'ania w pakiecie logowania.

---
# z"" localplayer.h
## Ogolny opis
Plik nagL'owkowy dla klasy `LocalPlayer`, ktora reprezentuje postac sterowana przez gracza. Jest to specjalizacja klasy `Player`.
## Klasa `LocalPlayer`
## Opis
Dziedziczy po `Player`. Dodaje funkcjonalnoLci specyficzne dla gracza, ktory jest kontrolowany przez klienta, takie jak:
-   **Pre-walking**: Przewidywanie ruchu przed otrzymaniem odpowiedzi z serwera.
-   **Auto-walking**: Automatyczne poruszanie sie do celu.
-   **Zarzadzanie stanem**: Przechowuje szczegoL'owe statystyki (LLycie, mana, umiejetnoLci, etc.).
## Metody
| Nazwa | Opis |
| --- | --- |
| `lockWalk(int millis)` | Blokuje moLLliwoLc chodzenia na okreLlony czas. |
| `stopAutoWalk()` | Przerywa auto-walking. |
| `autoWalk(Position destination, ...)` | Rozpoczyna auto-walking do celu. |
| `canWalk(...)` | Sprawdza, czy gracz moLLe sie poruszyc. |
| `isPreWalking()` | Zwraca `true`, jeLli gracz wykonuje ruch "pre-walk". |
| `getPrewalkingPosition(...)` | Zwraca pozycje, na ktorej gracz znajdzie sie po zakoL"czeniu wszystkich ruchow "pre-walk". |
| `setHealth(...)`, `setMana(...)`, etc. | Metody do ustawiania statystyk gracza. |
| `getHealth()`, `getMana()`, etc. | Metody do pobierania statystyk. |
| `hasSight(const Position& pos)` | Sprawdza, czy pozycja jest w zasiegu wzroku. |
## ZaleLLnoLci i powiazania
- **`player.h`**: Klasa bazowa.
- **`walkmatrix.h`**: ULLywa `WalkMatrix` do Lledzenia predykcji ruchu.

---
# z"" towns.cpp
## Ogolny opis
Implementacja `Town` i `TownManager`, ktore sL'uLLa do zarzadzania danymi o miastach w grze.
## Klasa `Town`
## Metody
- **`Town(uint32 tid, ...)`**: Konstruktor, ktory inicjalizuje miasto z podanym ID, nazwa i pozycja (zwykle Lwiatyni).
## Klasa `TownManager`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addTown(const TownPtr &town)` | Dodaje nowe miasto do listy, jeLli jeszcze nie istnieje. |
| `removeTown(uint32 townId)` | Usuwa miasto o podanym ID. |
| `getTown(uint32 townId)` | Zwraca miasto po jego ID. |
| `getTownByName(std::string name)` | Zwraca miasto po jego nazwie. |
| `findTown(uint32 townId)` | Wewnetrzna metoda do wyszukiwania iteratora do miasta. |
| `sort()` | Sortuje liste miast alfabetycznie wedL'ug nazwy. |
## Zmienne globalne
- **`TownManager g_towns`**: Globalna instancja managera miast.
## ZaleLLnoLci i powiazania
- **`mapio.cpp`**: MenedLLer `g_towns` jest wypeL'niany danymi podczas wczytywania mapy w formacie OTBM.

---
# z"" spritemanager.h
## Ogolny opis
Plik nagL'owkowy dla `SpriteManager`, singletonu odpowiedzialnego za zarzadzanie plikami sprite'ow (`.spr`).
## Klasa `SpriteManager`
## Opis
Centralny punkt dostepu do danych graficznych sprite'ow. Odpowiada za wczytywanie, deszyfrowanie, dekompresje i dostarczanie obrazow poszczegolnych sprite'ow.
## Metody
| Nazwa | Opis |
| --- | --- |
| `loadSpr(std::string file)` | Wczytuje plik sprite'ow (automatycznie wykrywa format: `.spr`, `.cwm`, OTV8). |
| `unload()` | Zwalnia wszystkie zaL'adowane dane sprite'ow. |
| `saveSpr(...)` / `encryptSprites(...)` | Metody (dostepne z `WITH_ENCRYPTION`) do zapisywania i szyfrowania plikow sprite'ow. |
| `getSignature()` | Zwraca sygnature wczytanego pliku `.spr`. |
| `getSpritesCount()` | Zwraca liczbe sprite'ow w pliku. |
| `getSpriteImage(int id)` | GL'owna metoda do pobierania obrazu sprite'a o danym ID. |
| `isLoaded()` | Zwraca `true`, jeLli plik sprite'ow jest zaL'adowany. |
| `spriteSize()` | Zwraca rozmiar boku pojedynczego sprite'a (np. 32 lub 64 piksele). |
| `getOffsetFactor()` | Zwraca wspoL'czynnik skalowania dla przemieszczeL" (displacement) w zaleLLnoLci od `spriteSize`. |
| `isHdMod()` | Zwraca `true`, jeLli zaL'adowano modyfikacje HD (`.cwm`). |
## Zmienne globalne
- **`SpriteManager g_sprites`**: Globalna instancja managera sprite'ow.
## ZaleLLnoLci i powiazania
- **`framework/core/declarations.h`**: Podstawowe deklaracje.
- **`framework/graphics/declarations.h`**: Deklaracje typow graficznych.
- Niemal kaLLda klasa renderujaca obiekty w grze (np. `ThingType`, `Item`, `Creature`) zaleLLy od `SpriteManager`.

---
# z"" tile.cpp
## Ogolny opis
Implementacja klasy `Tile`, ktora reprezentuje pojedyncze pole na mapie gry. Plik zawiera logike rysowania pola i wszystkich znajdujacych sie na nim obiektow, zarzadzania stosem obiektow oraz dostarczania informacji o wL'aLciwoLciach pola.
## Klasa `Tile`
## Metody
## Rysowanie
| Nazwa | Opis |
| --- | --- |
| `drawGround(...)` | Rysuje podL'oLLe i obiekty na najniLLszej warstwie. Oblicza `m_drawElevation` (przesuniecie w pionie dla obiektow o wysokoLci > 1). |
| `drawBottom(...)` | Rysuje przedmioty, ktore znajduja sie na spodzie, ale nad podL'oLLem (np. Lciany). |
| `drawCreatures(...)` | Rysuje stworzenia na tym polu oraz stworzenia, ktore na nie wchodza. |
| `drawTop(...)` | Rysuje przedmioty na wierzchu, efekty oraz ponownie stworzenia, aby obsL'uLLyc przypadki nakL'adania sie. |
| `drawTexts(...)` | Rysuje tekst przypisany do pola (np. timer). |
| `drawWidget(...)` | Rysuje przypisany do pola widLLet. |
## Zarzadzanie obiektami
| Nazwa | Opis |
| --- | --- |
| `addThing(...)` | Dodaje obiekt (`Thing`) na stos w odpowiedniej pozycji, uwzgledniajac jego priorytet (ziemia, przedmioty, stworzenia). |
| `removeThing(...)` | Usuwa obiekt ze stosu. |
| `addWalkingCreature(...)` | Dodaje stworzenie do listy "przechodzacych" przez to pole, ktore sa rysowane osobno. |
| `getThing(...)` | Zwraca obiekt z danej pozycji na stosie. |
| `getTopThing()`, `getTopCreature()`, etc. | Zwracaja "najwaLLniejszy" obiekt danego typu na polu, uwzgledniajac logike gry (np. na co patrzy gracz, czego uLLywa). |
| `getItems()`, `getCreatures()` | Zwracaja listy wszystkich przedmiotow lub stworzeL" na polu. |
## WL'aLciwoLci
| Nazwa | Opis |
| --- | --- |
| `isWalkable(...)` | Sprawdza, czy po polu moLLna chodzic (czy nie ma blokujacych przedmiotow lub stworzeL"). |
| `isPathable()` | Sprawdza, czy algorytm wyszukiwania LcieLLki moLLe uLLywac tego pola. |
| `isFullGround()` | Sprawdza, czy podL'oLLe caL'kowicie zakrywa pole pod nim. |
| `getGroundSpeed()` | Zwraca predkoLc poruszania sie po tym polu. |
## ZaleLLnoLci i powiazania
- **`map.h`**: ULLywa `g_map` do pobierania sasiednich pol (np. przy korekcji zwL'ok).
- **`game.h`**: Dostep do `g_game` w celu sprawdzania `GameFeature`.
- **`thing.h`**, **`item.h`**, **`creature.h`**: Zarzadza tymi obiektami.
- **`lightview.h`**: Przekazuje `LightView` do metod rysujacych obiekty, aby mogL'y dodac swoje LwiatL'o.

---
# z"" statictext.h
## Ogolny opis
Plik nagL'owkowy dla klasy `StaticText`, ktora reprezentuje tekst pojawiajacy sie nad gL'owami stworzeL" lub na polach mapy.
## Struktura `StaticTextMessage`
-   **`texts`**: Wektor par `std::string`, gdzie pierwsza to treLc, a druga to kolor w formacie hex.
-   **`time`**: Czas (w tickach), po ktorym wiadomoLc powinna zniknac.
## Klasa `StaticText`
## Opis
Dziedziczy po `Thing`. Zarzadza kolejka wiadomoLci, ktore sa wyLwietlane jedna po drugiej. Jest uLLywana do mowy postaci, potworow, a takLLe do niestandardowych tekstow na mapie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawText(...)` | Rysuje aktualnie wyLwietlana wiadomoLc. |
| `getName()` | Zwraca nazwe postaci mowiacej. |
| `getText()` | Zwraca aktualnie wyLwietlany tekst. |
| `getMessageMode()` | Zwraca tryb wiadomoLci (np. `Say`, `Yell`). |
| `addMessage(...)` / `addColoredMessage(...)` | Dodaje nowa wiadomoLc do kolejki. Oblicza czas jej wyLwietlania na podstawie dL'ugoLci. |
| `setText(...)` / `setFont(...)` | Ustawia surowy tekst i czcionke (gL'ownie dla niestandardowych tekstow). |
| `isYell()` | Zwraca `true`, jeLli tryb wiadomoLci to krzyk. |
## ZaleLLnoLci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/graphics/cachedtext.h`**: ULLywa `CachedText` do efektywnego renderowania tekstu.
- **`framework/core/timer.h`**: ULLywane do zarzadzania czasem LLycia wiadomoLci.

---
# z"" uimapanchorlayout.cpp
## Ogolny opis
Implementacja `UIPositionAnchor` i `UIMapAnchorLayout`, ktore rozszerzaja standardowy system kotwic (`UIAnchorLayout`) o moLLliwoLc przypinania widLLetow do konkretnych pozycji na minimapie.
## Klasa `UIPositionAnchor`
## Metody
| Nazwa | Opis |
| --- | --- |
| `getHookedPoint(...)` | Kluczowa metoda, ktora oblicza wspoL'rzedna (X lub Y) na ekranie na podstawie `m_hookedPosition`. Pobiera `UIMinimap`, prosi go o prostokat (`Rect`) odpowiadajacy danemu polu na mapie (`getTileRect`), a nastepnie zwraca odpowiednia krawedLs tego prostokata (np. `left`, `top`, `horizontalCenter`). |
## Klasa `UIMapAnchorLayout`
## Metody
| Nazwa | Opis |
| --- | --- |
| `addPositionAnchor(...)` | Tworzy nowy obiekt `UIPositionAnchor` i dodaje go do grupy kotwic dla danego widLLetu. |
| `centerInPosition(...)` | Funkcja pomocnicza, ktora dodaje dwie kotwice (`HorizontalCenter` i `VerticalCenter`), aby wyLrodkowac widLLet na danym polu mapy. |
| `fillPosition(...)` | Funkcja pomocnicza, ktora dodaje cztery kotwice (`Left`, `Right`, `Top`, `Bottom`), aby widLLet wypeL'niL' obszar danego pola na mapie. |
## ZaleLLnoLci i powiazania
- **`uiminimap.h`**: `UIPositionAnchor` rzutuje widLLet-rodzica na `UIMinimap`, aby uzyskac dostep do metody `getTileRect`.
- **`framework/ui/uiwidget.h`**: WspoL'pracuje z widLLetami.
- **`framework/ui/uianchorlayout.h`**: Rozszerza standardowy layout kotwic.

---
# z"" thing.h
## Ogolny opis
Plik nagL'owkowy dla `Thing`, abstrakcyjnej klasy bazowej dla wszystkich obiektow, ktore moga pojawic sie na mapie w grze.
## Klasa `Thing`
## Opis
Dziedziczy po `LuaObject`. Definiuje wspolny interfejs dla przedmiotow, stworzeL", efektow, pociskow i tekstow. KaLLdy obiekt `Thing` ma pozycje i naleLLy do okreLlonego typu (`ThingType`).
## Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Wirtualna metoda do rysowania obiektu. |
| `setPosition(const Position& position)` | Ustawia pozycje obiektu. |
| `getPosition()` | Zwraca pozycje obiektu. |
| `getStackPriority()` | Zwraca priorytet na stosie, ktory decyduje o kolejnoLci rysowania i interakcji. |
| `getTile()` | Zwraca wskaLsnik do pola (`Tile`), na ktorym znajduje sie obiekt. |
| `getStackPos()` | Zwraca pozycje obiektu na stosie wewnatrz pola. |
| `isItem()`, `isCreature()`, etc. | Wirtualne metody do identyfikacji typu obiektu. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla tego obiektu. |
| `getSize()`, `getWidth()`, `getHeight()`, etc. | Metody-skroty do wL'aLciwoLci z `ThingType`. |
| `onPositionChange(...)`, `onAppear()`, `onDisappear()` | Wirtualne metody wywoL'ywane w kluczowych momentach cyklu LLycia obiektu. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow, np. `TilePtr`.
- **`thingtype.h`**: KaLLdy `Thing` ma swoj `ThingType`.
- **`framework/luaengine/luaobject.h`**: Klasa bazowa.

---
# z"" uiitem.h
## Ogolny opis
Plik nagL'owkowy dla `UIItem`, widLLetu interfejsu uLLytkownika przeznaczonego do wyLwietlania przedmiotow (`Item`).
## Klasa `UIItem`
## Opis
Dziedziczy po `UIWidget`. SL'uLLy do renderowania przedmiotow w UI, np. w ekwipunku, kontenerach, oknach handlu.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje tL'o, obraz, a nastepnie sam przedmiot (`m_item->draw(...)`), liczbe sztuk (jeLli dotyczy) i ramke. |
| `setItemId(int id)` | Ustawia przedmiot do wyLwietlenia na podstawie jego ID. |
| `setItemCount(int count)` | Ustawia liczbe sztuk przedmiotu. |
| `setItem(const ItemPtr& item)` | Ustawia przedmiot do wyLwietlenia na podstawie istniejacego obiektu `Item`. |
| `setVirtual(bool virt)` | Oznacza, czy przedmiot jest "wirtualny" (nie jest prawdziwa instancja, tylko reprezentacja wizualna). |
| `setShowCount(bool value)` | WL'acza/wyL'acza wyLwietlanie liczby sztuk. |
| `setItemShader(const std::string& str)` | Ustawia niestandardowy shader dla przedmiotu. |
| `getItem()` | Zwraca obiekt `Item` powiazany z widLLetem. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.
- **`item.h`**: Przechowuje i rysuje obiekt `Item`.

---
# z"" thing.cpp
## Ogolny opis
Implementacja klasy bazowej `Thing`. Zawiera podstawowa logike wspolna dla wszystkich obiektow na mapie.
## Klasa `Thing`
## Metody
| Nazwa | Opis |
| --- | --- |
| `setPosition(const Position& position)` | Aktualizuje pozycje obiektu i wywoL'uje wirtualna metode `onPositionChange`. |
| `getStackPriority()` | Zwraca priorytet obiektu na stosie wewnatrz pola. KolejnoLc jest LciLle zdefiniowana: ziemia, obramowanie ziemi, obiekty na dole (np. Lciany), obiekty na gorze (np. dywany), stworzenia, a na koL"cu zwykL'e przedmioty. |
| `getTile()` | Zwraca wskaLsnik do pola, na ktorym znajduje sie obiekt, uLLywajac `g_map`. |
| `getParentContainer()` | JeLli obiekt znajduje sie w kontenerze, zwraca wskaLsnik do tego kontenera. Pozycja w kontenerze jest specjalnie kodowana. |
| `getStackPos()` | Zwraca pozycje na stosie: albo wewnatrz kontenera, albo na polu mapy. |
| `getThingType()` / `rawGetThingType()` | Zwracaja domyLlny, "pusty" `ThingType`. Musza byc nadpisane przez klasy pochodne. |
| `updatedMarkedColor()` | Aktualizuje kolor i przezroczystoLc znacznika (jeLli jest ustawiony), tworzac efekt pulsowania. |
## ZaleLLnoLci i powiazania
- **`spritemanager.h`**, **`thingtypemanager.h`**: Podstawowe zaleLLnoLci.
- **`map.h`**: Do pobierania `Tile`.
- **`game.h`**: Do pobierania kontenerow.

---
# z"" uimap.cpp
## Ogolny opis
Implementacja `UIMap`, widLLetu interfejsu uLLytkownika, ktory renderuje gL'owny widok mapy gry.
## Klasa `UIMap`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | GL'owna funkcja rysujaca. Jest wywoL'ywana trzykrotnie dla roLLnych "warstw" (`DrawPane`): <br> 1. `MapBackgroundPane`: Rysuje tL'o mapy (`m_mapView->drawMapBackground`). <br> 2. `MapForegroundPane`: Rysuje pierwszy plan (`m_mapView->drawMapForeground`). <br> 3. `ForegroundPane`: Rysuje obramowanie wokoL' mapy. |
| `setZoom(int zoom)` | Ustawia poziom przybliLLenia, co wpL'ywa na `m_mapView->setVisibleDimension`. |
| `zoomIn()` / `zoomOut()` | Zmienia poziom przybliLLenia o staL'a wartoLc. |
| `setVisibleDimension(...)` | Ustawia widoczny wymiar w `m_mapView` i aktualizuje proporcje. |
| `setKeepAspectRatio(bool enable)` | WL'acza/wyL'acza zachowanie staL'ych proporcji widoku mapy. |
| `getPosition(const Point& mousePos)` | Konwertuje pozycje kursora na ekranie na pozycje (`Position`) w Lwiecie gry. |
| `getTile(const Point& mousePos)` | Zwraca pole (`Tile`) pod kursorem, przeszukujac widoczne pietra od gory do doL'u w poszukiwaniu klikalnego obiektu. |
| `updateVisibleDimension()` | Przelicza i ustawia widoczny wymiar w `m_mapView` na podstawie aktualnego zoomu i proporcji. |
| `updateMapSize()` | Dopasowuje rozmiar i pozycje prostokata rysowania mapy (`m_mapRect`) do rozmiaru widLLetu, zachowujac proporcje, jeLli to wymagane. |
## ZaleLLnoLci i powiazania
- **`game.h`**, **`map.h`**: Dostep do globalnych obiektow gry i mapy.
- **`mapview.h`**: `UIMap` jest "opakowaniem" dla `MapView`, przekazujac mu zadania renderowania.
- **`framework/otml/otml.h`**: Parsuje wL'aLciwoLci z plikow OTML, takie jak `multifloor` czy `animated`.

---
# z"" statictext.cpp
## Ogolny opis
Implementacja `StaticText`, klasy odpowiedzialnej za wyLwietlanie mowy postaci i innych tekstow na mapie.
## Klasa `StaticText`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawText(...)` | Rysuje tekst na ekranie, centrujac go i dopasowujac do prostokata nadrzednego. |
| `addMessage(...)` / `addColoredMessage(...)` | Dodaje nowa wiadomoLc do kolejki. JeLli jest to pierwsza wiadomoLc, ustawia tryb (np. `Say`, `Yell`) i nazwe mowiacego. JeLli kolejne wiadomoLci pasuja do poprzednich (ten sam mowiacy i tryb), sa dodawane do kolejki. Oblicza czas wyLwietlania na podstawie dL'ugoLci tekstu. |
| `update()` | Metoda wywoL'ywana po upL'ynieciu czasu wyLwietlania wiadomoLci. Usuwa najstarsza wiadomoLc z kolejki. JeLli kolejka jest pusta, planuje usuniecie caL'ego obiektu `StaticText` z mapy. |
| `scheduleUpdate()` | Planuje wywoL'anie `update()` po czasie rownym czasowi LLycia najstarszej wiadomoLci w kolejce. |
| `compose()` | Tworzy sformatowany tekst do wyLwietlenia. Laczy wszystkie wiadomoLci z kolejki, dodaje nagL'owki (np. "Player says:"), ustawia kolory i zawija tekst, jeLli jest zbyt dL'ugi. |
## Logika dziaL'ania
`StaticText` dziaL'a jak kolejka FIFO dla wiadomoLci. KaLLda nowa wiadomoLc jest dodawana na koniec. `compose` tworzy jeden ciagL'y, sformatowany tekst ze wszystkich wiadomoLci w kolejce, ktory jest nastepnie rysowany przez `drawText`. `scheduleUpdate` i `update` zapewniaja, LLe wiadomoLci znikaja po okreLlonym czasie, a caL'y obiekt jest usuwany, gdy nie ma juLL nic do wyLwietlenia.
## ZaleLLnoLci i powiazania
- **`map.h`**: ULLywa `g_map` do usuniecia obiektu po zakoL"czeniu.
- **`framework/core/eventdispatcher.h`**: ULLywa `g_dispatcher` do planowania aktualizacji.
- **`framework/graphics/fontmanager.h`**: ULLywa `g_fonts` do zarzadzania czcionkami.

---
# z"" uiitem.cpp
## Ogolny opis
Implementacja `UIItem`, widLLetu do wyLwietlania przedmiotow w interfejsie uLLytkownika.
## Klasa `UIItem`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widLLet. Renderuje tL'o, obraz, a nastepnie sam przedmiot (`m_item->draw(...)`), uLLywajac prostokata `getPaddingRect()`. JeLli `m_showCount` jest wL'aczone, rysuje rownieLL liczbe przedmiotow w prawym dolnym rogu. |
| `setItemId(int id)` | Tworzy nowy obiekt `Item` (jeLli go nie byL'o) lub aktualizuje ID istniejacego. |
| `setItemCount(int count)` | Ustawia liczbe przedmiotow i aktualizuje tekst licznika. |
| `setItem(const ItemPtr& item)` | Ustawia przedmiot na podstawie gotowego obiektu `ItemPtr`. |
| `setItemShader(const std::string& str)` | Ustawia niestandardowy shader dla renderowanego przedmiotu. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `item-id`, `item-count`, `virtual`. |
| `cacheCountText()` | Formatuje tekst licznika. Dla liczb >= 1000 uLLywa skrotu "k" (np. "1.2k"), jeLli funkcja `GameCountU16` jest aktywna. |
## ZaleLLnoLci i powiazania
- **`spritemanager.h`**: ULLywany przez `Item` do pobierania sprite'ow.
- **`game.h`**: Sprawdza `GameFeature`, np. `GameCountU16`.
- **`framework/otml/otml.h`**: Do parsowania stylow.
- **`framework/graphics/graphics.h`**: Do operacji rysowania.

---
# z"" thingstype.h
## Ogolny opis
Plik nagL'owkowy dla klasy `ThingsType` (bL'ad w nazwie, prawdopodobnie powinno byc `ThingTypeManager`). Definiuje interfejs singletonu, ktory zarzadza wszystkimi typami obiektow (`ThingType`) w grze, wczytywanymi z plikow `.dat`.

> NOTE: Nazwa klasy `ThingsType` jest mylaca. W rzeczywistoLci jest to menedLLer, ktory przechowuje i zarzadza obiektami `ThingType`. W innych plikach jest on nazywany `ThingTypeManager`.
## Klasa `ThingsType`
## Typy wyliczeniowe
- **`Categories`**: Kategorie obiektow (Przedmiot, Stworzenie, Efekt, Pocisk).
## Metody
| Nazwa | Opis |
| --- | --- |
| `load(const std::string& file)` | Wczytuje i parsuje plik `.dat`. |
| `unload()` | Zwalnia zaL'adowane dane. |
| `parseThingType(...)` | Parsuje dane pojedynczego typu obiektu ze strumienia pliku. |
| `getEmptyThingType()` | Zwraca pusty, domyLlny obiekt `ThingType`. |
| `getThingType(uint16 id, Categories category)` | Zwraca `ThingType` dla danego ID i kategorii. |
| `getSignature()` | Zwraca sygnature wczytanego pliku `.dat`. |
| `isLoaded()` | Zwraca `true`, jeLli plik `.dat` jest zaL'adowany. |
| `isValidItemId(int id)` | Sprawdza, czy ID przedmiotu jest w prawidL'owym zakresie. |
## Zmienne globalne
- **`ThingsType g_thingsType`**: Globalna instancja managera (poLsniej w kodzie uLLywane jest `g_things`).
## ZaleLLnoLci i powiazania
- **`thingtype.h`**: Zarzadza obiektami `ThingType`.
- **`framework/core/declarations.h`**: Podstawowe deklaracje.

---
# z"" uigraph.h
## Ogolny opis
Plik nagL'owkowy dla `UIGraph`, widLLetu sL'uLLacego do rysowania prostych wykresow liniowych.
## Klasa `UIGraph`
## Opis
Dziedziczy po `UIWidget`. Przechowuje kolejke wartoLci i renderuje je jako wykres liniowy.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje wykres. Oblicza skale, przygotowuje punkty i rysuje linie za pomoca `g_drawQueue->addLine`. |
| `clear()` | CzyLci wszystkie wartoLci z wykresu. |
| `addValue(int value, ...)` | Dodaje nowa wartoLc do wykresu. JeLli liczba wartoLci przekroczy pojemnoLc, najstarsza jest usuwana. |
| `setLineWidth(int width)` | Ustawia gruboLc linii wykresu. |
| `setCapacity(int capacity)` | Ustawia maksymalna liczbe wartoLci przechowywanych przez wykres. |
| `setTitle(const std::string& title)` | Ustawia tytuL' wyLwietlany nad wykresem. |
| `setShowLabels(bool value)` | WL'acza/wyL'acza wyLwietlanie etykiet (wartoLc min, max, aktualna). |
## ZaleLLnoLci i powiazania
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# z"" uicreature.h
## Ogolny opis
Plik nagL'owkowy dla `UICreature`, widLLetu interfejsu uLLytkownika do wyLwietlania stworzeL".
## Klasa `UICreature`
## Opis
Dziedziczy po `UIWidget`. UmoLLliwia renderowanie postaci (jej ubioru) w elementach UI, takich jak okno ekwipunku, battle list, czy okno wyboru stroju.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje postac za pomoca `m_creature->drawOutfit(...)`. ObsL'uguje automatyczne obracanie postaci, jeLli jest wL'aczone. |
| `setCreature(const CreaturePtr& creature)` | Ustawia stworzenie do wyLwietlenia. |
| `setFixedCreatureSize(bool fixed)` | Ustawia, czy rozmiar renderowanej postaci ma byc staL'y, czy skalowany do rozmiaru widLLetu. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubior do wyLwietlenia. JeLli nie ma przypisanego stworzenia, tworzy nowe. |
| `setAutoRotating(bool value)` | WL'acza/wyL'acza automatyczne obracanie sie postaci. |
| `setDirection(Otc::Direction direction)` | Ustawia staL'y kierunek, w ktorym postac jest zwrocona. |
| `setScale(float scale)` | Ustawia skale rysowania postaci. |
| `setAnimate(bool value)` | WL'acza/wyL'acza animacje postaci. |
| `setCenter(bool value)` | WL'acza/wyL'acza centrowanie outfitu. |
| `setOldScaling(bool value)` | ULLywa starego algorytmu skalowania. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.
- **`creature.h`**: Przechowuje i rysuje obiekt `Creature`.

---
# z"" thingtype.cpp
## Ogolny opis
Implementacja klasy `ThingType`, ktora reprezentuje szablon dla wszystkich obiektow w grze. Plik zawiera logike serializacji, deserializacji, a przede wszystkim renderowania obiektow danego typu.
## Klasa `ThingType`
## Metody
## Serializacja / Deserializacja
| Nazwa | Opis |
| --- | --- |
| `serialize(...)` | Zapisuje atrybuty `ThingType` do strumienia binarnego, zgodnie z formatem plikow `.dat`. |
| `unserialize(...)` | Wczytuje atrybuty `ThingType` ze strumienia. Zawiera zL'oLLona logike do obsL'ugi roLLnic w formatach `.dat` miedzy roLLnymi wersjami klienta Tibii, mapujac stare atrybuty na nowe. |
| `unserializeOtml(...)` | Wczytuje dodatkowe, niestandardowe atrybuty z plikow OTML, takie jak przezroczystoLc czy niestandardowe obrazy. |
## Rysowanie
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | GL'owna metoda rysujaca. Pobiera teksture dla danej fazy animacji, oblicza, ktory jej fragment (`Rect`) odpowiada danemu wzorowi (pattern) i warstwie, a nastepnie dodaje go do kolejki rysowania. |
| `drawOutfit(...)` | Specjalna wersja do rysowania ubiorow, ktora zwraca parametry potrzebne do renderowania z dynamicznym kolorowaniem przez `DrawQueueItemOutfit`. |
| `drawWithShader(...)` | Wersja rysujaca z uLLyciem niestandardowego shadera. |
## Zarzadzanie teksturami
| Nazwa | Opis |
| --- | --- |
| `getTexture(int animationPhase)` | Zwraca teksture dla danej fazy animacji. JeLli tekstura nie zostaL'a jeszcze utworzona, generuje ja "w locie": <br> 1. Tworzy duLLy obraz (atlas). <br> 2. SkL'ada go z pojedynczych sprite'ow pobranych z `g_sprites`. <br> 3. Tworzy z niego obiekt `Texture` i przechowuje go w pamieci podrecznej. <br> 4. Zapisuje rownieLL prostokaty (`Rect`) i przesuniecia dla kaLLdej klatki na tej teksturze. |
| `unload()` | Zwalnia wygenerowane tekstury z pamieci, aby oszczedzac zasoby. Sa one ponownie generowane przy nastepnym uLLyciu. |
| `getBestTextureDimension(...)` | Oblicza optymalny rozmiar tekstury-atlasu, aby pomieLcic wszystkie klatki animacji. |
## ZaleLLnoLci i powiazania
- **`spritemanager.h`**: ULLywa `g_sprites` do pobierania obrazow pojedynczych sprite'ow.
- **`game.h`**: Sprawdza `GameFeature`, co wpL'ywa na logike deserializacji i animacji.
- **`lightview.h`**: Przekazuje `LightView` do dodawania LwiatL'a, jeLli obiekt je emituje.
- **`framework/graphics/...`**: Intensywnie korzysta z klas `Texture`, `Image`, `Painter` i `DrawQueue`.

---
# z"" towns.h
## Ogolny opis
Plik nagL'owkowy definiujacy klasy `Town` i `TownManager` do zarzadzania miastami w grze.
## Klasa `Town`
## Opis
Prosta klasa przechowujaca dane o pojedynczym mieLcie: ID, nazwe i pozycje (zazwyczaj Lwiatyni).
## Metody
| Nazwa | Opis |
| --- | --- |
| `setId(uint32 tid)` | Ustawia ID miasta. |
| `setName(const std::string& name)` | Ustawia nazwe miasta. |
| `setPos(const Position& pos)` | Ustawia pozycje miasta. |
| `getId()` / `getName()` / `getPos()` | Zwracaja odpowiednie wL'aLciwoLci. |
## Klasa `TownManager`
## Opis
Singleton (`g_towns`) zarzadzajacy kolekcja wszystkich miast.
## Metody
| Nazwa | Opis |
| --- | --- |
| `addTown(const TownPtr& town)` | Dodaje miasto do listy. |
| `removeTown(uint32 townId)` | Usuwa miasto po ID. |
| `getTown(uint32 townId)` | Zwraca miasto po ID. |
| `getTownByName(std::string name)` | Zwraca miasto po nazwie. |
| `sort()` | Sortuje liste miast alfabetycznie. |
| `getTowns()` | Zwraca liste wszystkich miast. |
| `clear()` | CzyLci liste miast. |
## Zmienne globalne
- **`TownManager g_towns`**: Globalna instancja managera miast.
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow, np. `TownPtr`, `Position`.

---
# z"" thingtype.h
## Ogolny opis
Plik nagL'owkowy dla klasy `ThingType`, ktora jest szablonem dla wszystkich obiektow w grze. Definiuje ona ich wspolne, niezmienne wL'aLciwoLci.
## Klasa `ThingType`
## Opis
Dziedziczy po `LuaObject`. Przechowuje dane wczytane z plikow `.dat` i `.otml`, takie jak wymiary, wzory, animacje, atrybuty (np. czy jest blokujacy, czy Lwieci). Wszystkie instancje `Thing` o tym samym ID wspoL'dziela jeden obiekt `ThingType`.
## Typy wyliczeniowe
- **`ThingCategory`**: Kategorie obiektow (przedmiot, stworzenie, etc.).
- **`ThingAttr`**: Atrybuty obiektu (np. `ThingAttrGround`, `ThingAttrNotWalkable`).
## Struktury
- **`MarketData`**: Dane rynkowe przedmiotu.
- **`Light`**: Parametry emitowanego LwiatL'a.
- **`DrawOutfitParams`**: Parametry potrzebne do narysowania ubioru.
## Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(...)` | Wczytuje dane z binarnego formatu `.dat`. |
| `unserializeOtml(...)` | Wczytuje dodatkowe dane z formatu `.otml`. |
| `draw(...)` | Renderuje obiekt. |
| `drawOutfit(...)` | Specjalna funkcja do renderowania ubiorow. |
| `getId()` | Zwraca ID klienta. |
| `getCategory()` | Zwraca kategorie. |
| `getSize()`, `getWidth()`, `getHeight()` | Zwracaja wymiary w jednostkach pol. |
| `getAnimationPhases()` | Zwraca liczbe klatek animacji. |
| `getAnimator()` | Zwraca animator, jeLli jest dostepny. |
| `hasAttr(ThingAttr attr)` | Sprawdza, czy obiekt posiada dany atrybut. |
| `isGround()`, `isNotWalkable()`, etc. | Funkcje pomocnicze sprawdzajace konkretne atrybuty. |
## ZaleLLnoLci i powiazania
- **`animator.h`**: MoLLe posiadac `Animator` do zarzadzania animacjami.
- **`framework/graphics/...`**: ULLywa `Texture`, `DrawQueue` do renderowania.
- **`framework/luaengine/luaobject.h`**: Klasa bazowa.

---
# z"" uicreature.cpp
## Ogolny opis
Implementacja `UICreature`, widLLetu do wyLwietlania stworzeL" w interfejsie uLLytkownika.
## Klasa `UICreature`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widLLet. JeLli przypisano stworzenie (`m_creature`), wywoL'uje jego metode `drawOutfit`, aby narysowac jego wyglad w prostokacie widLLetu. ObsL'uguje automatyczne obracanie postaci, jeLli opcja `m_autoRotating` jest wL'aczona. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubior do wyLwietlenia. JeLli widLLet nie ma jeszcze przypisanego obiektu `Creature`, tworzy nowa, pusta instancje. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `outfit-id`, `outfit-head`, `outfit-body` itp., i na ich podstawie konfiguruje wyLwietlany ubior. |
| `setCenter(bool value)` | Ustawia flage centrowania w obiekcie `Outfit`, co wpL'ywa na sposob jego rysowania. |
## ZaleLLnoLci i powiazania
- **`spritemanager.h`**: ULLywane przez `Creature::drawOutfit`.
- **`framework/otml/otml.h`**: Do parsowania stylow.
- **`framework/graphics/drawqueue.h`**: Do dodawania operacji rysowania.

---
# z"" thingtypemanager.h
## Ogolny opis
Plik nagL'owkowy dla `ThingTypeManager`, singletonu zarzadzajacego wszystkimi typami obiektow (`ThingType`) i przedmiotow (`ItemType`).
## Klasa `ThingTypeManager`
## Opis
Centralne repozytorium dla definicji wszystkich obiektow w grze. Odpowiada za wczytywanie plikow `.dat`, `.otb` i `.xml`, ktore zawieraja te definicje, oraz za dostarczanie ich na LLadanie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizacja i zamykanie managera. |
| `check()` | Okresowo wywoL'ywana metoda, ktora zwalnia z pamieci tekstury nieuLLywanych `ThingType`, aby oszczedzac zasoby. |
| `loadDat(...)`, `loadOtml(...)`, `loadOtb(...)`, `loadXml(...)` | Metody do wczytywania roLLnych formatow plikow z danymi o obiektach. |
| `getThingType(id, category)` | Zwraca `ThingType` dla danego ID klienta i kategorii. |
| `getItemType(id)` | Zwraca `ItemType` dla danego ID serwera (OTB). |
| `findItemTypeByClientId(id)` | Wyszukuje `ItemType` po jego ID klienta. |
| `findItemTypeByName(name)` | Wyszukuje `ItemType` po nazwie. |
| `isDatLoaded()`, `isOtbLoaded()` | Sprawdzaja, czy odpowiednie pliki zostaL'y zaL'adowane. |
| `getDatSignature()` | Zwraca sygnature pliku `.dat`. |
## Zmienne globalne
- **`ThingTypeManager g_things`**: Globalna instancja managera.
## ZaleLLnoLci i powiazania
- **`thingtype.h`**, **`itemtype.h`**: Zarzadza obiektami tych klas.
- Jest to jedna z najbardziej fundamentalnych klas w kliencie, uLLywana przez niemal kaLLdy moduL', ktory ma do czynienia z obiektami w grze.

---
# z"" uigraph.cpp
## Ogolny opis
Implementacja `UIGraph`, widLLetu do rysowania wykresow liniowych.
## Klasa `UIGraph`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje wykres. Oblicza minimalna i maksymalna wartoLc w widocznym zakresie, aby przeskalowac wykres do wysokoLci widLLetu. Nastepnie tworzy liste punktow i rysuje miedzy nimi linie za pomoca `g_drawQueue->addLine`. Rysuje rownieLL tytuL' i etykiety (min, max, aktualna wartoLc), jeLli sa wL'aczone. |
| `clear()` | CzyLci wszystkie dane z wykresu. |
| `addValue(int value, ...)` | Dodaje nowa wartoLc do kolejki `m_values`. JeLli kolejka przekroczy pojemnoLc (`m_capacity`), najstarsza wartoLc jest usuwana. Opcjonalnie ignoruje maL'e, powtarzajace sie wartoLci, aby uniknac "szumu" na wykresie. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `line-width`, `capacity`, `title`. |
## ZaleLLnoLci i powiazania
- **`framework/graphics/drawqueue.h`**: Do rysowania linii i tekstu.
- **`framework/otml/otml.h`**: Do parsowania stylow.

---
# z"" uimap.h
## Ogolny opis
Plik nagL'owkowy dla `UIMap`, widLLetu UI, ktory jest odpowiedzialny za wyLwietlanie mapy gry.
## Klasa `UIMap`
## Opis
Dziedziczy po `UIWidget`. DziaL'a jako "okno" na Lwiat gry, wykorzystujac `MapView` do faktycznego renderowania. UmoLLliwia interakcje z mapa, taka jak przesuwanie, przybliLLanie i pobieranie informacji o tym, co znajduje sie pod kursorem.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje mape w trzech przejLciach (tL'o, pierwszy plan, interfejs). |
| `movePixels(int x, int y)` | Przesuwa widok kamery o zadana liczbe pikseli. |
| `setZoom(int zoom)` / `zoomIn()` / `zoomOut()` | Zarzadza poziomem przybliLLenia mapy. |
| `followCreature(...)` | Ustawia kamere, aby podaLLaL'a za stworzeniem. |
| `setCameraPosition(...)` | Ustawia kamere na staL'a pozycje. |
| `getPosition(const Point& mousePos)` | Zwraca pozycje na mapie (`Position`) odpowiadajaca danym wspoL'rzednym myszy na widLLecie. |
| `getTile(const Point& mousePos)` | Zwraca `Tile` pod kursorem. |
| `setKeepAspectRatio(bool enable)` | WL'acza/wyL'acza zachowanie staL'ych proporcji mapy. |
| `setVisibleDimension(...)` | Ustawia rozmiar widocznego obszaru mapy w polach. |
## ZaleLLnoLci i powiazania
- **`mapview.h`**: ULLywa `MapView` do renderowania.
- **`tile.h`**: Metoda `getTile` zwraca obiekt `Tile`.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# z"" uiminimap.cpp
## Ogolny opis
Implementacja `UIMinimap`, widLLetu interfejsu uLLytkownika do wyLwietlania minimapy.
## Klasa `UIMinimap`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widLLet. WywoL'uje `g_minimap.draw`, przekazujac prostokat widLLetu, pozycje kamery i skale, aby narysowac odpowiedni fragment minimapy. |
| `setZoom(int zoom)` | Ustawia poziom przybliLLenia minimapy. WartoLc zoom jest konwertowana na wspoL'czynnik skali (`m_scale`). |
| `setCameraPosition(const Position& pos)` | Ustawia centralna pozycje, wokoL' ktorej rysowana jest minimapa. |
| `floorUp()` / `floorDown()` | Zmienia aktualnie wyLwietlane pietro. |
| `getTilePoint(...)` / `getTilePosition(...)` | Konwertuja pozycje na mapie na wspoL'rzedne na widLLecie i odwrotnie. |
| `anchorPosition(...)` / `fillPosition(...)` / `centerInPosition(...)` | Metody do przypinania innych widLLetow do konkretnych pozycji na minimapie za pomoca `UIMapAnchorLayout`. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `zoom`, `min-zoom`, `max-zoom`. |
## ZaleLLnoLci i powiazania
- **`minimap.h`**: ULLywa `g_minimap` do renderowania danych.
- **`uimapanchorlayout.h`**: Posiada `UIMapAnchorLayout` do zarzadzania przypietymi widLLetami.
- **`game.h`**: Dostep do globalnych obiektow.

---
# z"" uiprogressrect.cpp
## Ogolny opis
Implementacja `UIProgressRect`, niestandardowego widLLetu, ktory wizualizuje postep za pomoca wypeL'niajacego sie okregu (lub kwadratu) w sposob radialny.
## Klasa `UIProgressRect`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widLLet. Zamiast standardowego paska postepu, rysuje serie trojkatow, ktorych wierzchoL'ki rozchodza sie od Lrodka prostokata, tworzac efekt radialnego wypeL'nienia. WypeL'nienie jest podzielone na 4 cwiartki, a kaLLda z nich na dwa segmenty, co daje 8 krokow animacji. |
| `setPercent(float percent)` | Ustawia procent wypeL'nienia (od 0.0 do 100.0). |
| `onStyleApply(...)` | Parsuje atrybut `percent` z OTML. |
## Logika rysowania
WypeL'nienie jest realizowane przez rysowanie trojkatow. KaLLdy trojkat ma jeden wierzchoL'ek w Lrodku prostokata, a dwa pozostaL'e na jego krawedziach. W miare wzrostu `m_percent`, kolejne trojkaty sa rysowane, tworzac iluzje pL'ynnego, okreLLnego wypeL'nienia.
## ZaleLLnoLci i powiazania
- **`framework/otml/otml.h`**: Do parsowania stylow.
- **`framework/graphics/graphics.h`**: Do operacji rysowania.

---
# z"" uimapanchorlayout.h
## Ogolny opis
Plik nagL'owkowy definiujacy `UIPositionAnchor` i `UIMapAnchorLayout`. Rozszerzaja one standardowy system kotwic o moLLliwoLc przypinania widLLetow do dynamicznych pozycji na `UIMinimap`.
## Klasa `UIPositionAnchor`
## Opis
Dziedziczy po `UIAnchor`. Zamiast przypinac sie do krawedzi innego widLLetu, przypina sie do pozycji (`Position`) na mapie.
-   `m_hookedPosition`: Pozycja na mapie, do ktorej kotwica jest przypieta.
## Metody
-   **`getHookedPoint(...)`**: Nadpisana metoda, ktora oblicza pozycje na ekranie, pobierajac z `UIMinimap` prostokat odpowiadajacy `m_hookedPosition`.
## Klasa `UIMapAnchorLayout`
## Opis
Dziedziczy po `UIAnchorLayout`. Specjalizuje layout kotwic do pracy z `UIMinimap`.
## Metody
-   **`addPositionAnchor(...)`**: Dodaje kotwice typu `UIPositionAnchor`.
-   **`centerInPosition(...)`**, **`fillPosition(...)`**: Funkcje pomocnicze do L'atwego centrowania lub wypeL'niania obszaru pola na mapie przez inny widLLet.
## ZaleLLnoLci i powiazania
- **`framework/ui/uianchorlayout.h`**: Klasa bazowa.
- **`uiminimap.h`**: Layout jest przeznaczony do uLLycia z `UIMinimap`.

---
# z"" uiminimap.h
## Ogolny opis
Plik nagL'owkowy dla `UIMinimap`, widLLetu do wyLwietlania minimapy.
## Klasa `UIMinimap`
## Opis
Dziedziczy po `UIWidget`. Renderuje dane z `Minimap` i pozwala na interakcje, takie jak zmiana pietra czy przybliLLenia. Posiada rownieLL `UIMapAnchorLayout` do pozycjonowania innych widLLetow wzgledem pozycji na minimapie.
## Metody
| Nazwa | Opis |
| --- | --- |
| `zoomIn()` / `zoomOut()` / `setZoom(int zoom)` | Zarzadzaja poziomem przybliLLenia. |
| `setCameraPosition(const Position& pos)` | Ustawia pozycje, ktora ma byc w centrum minimapy. |
| `floorUp()` / `floorDown()` | Zmienia wyLwietlane pietro. |
| `getTilePoint(...)` / `getTileRect(...)` | Zwracaja wspoL'rzedne ekranowe dla danego pola na mapie. |
| `getTilePosition(...)` | Konwertuje wspoL'rzedne ekranowe na pozycje na mapie. |
| `anchorPosition(...)` | Przypina inny widLLet do pozycji na minimapie. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# z"" uiprogressrect.h
## Ogolny opis
Plik nagL'owkowy dla `UIProgressRect`, widLLetu do wyLwietlania paska postepu w formie radialnej.
## Klasa `UIProgressRect`
## Opis
Dziedziczy po `UIWidget`. Zamiast typowego paska, rysuje wypeL'nienie w sposob okreLLny.
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje widLLet. |
| `setPercent(float percent)` | Ustawia procent postepu (0-100). |
| `getPercent()` | Zwraca aktualny procent. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# z"" uisprite.cpp
## Ogolny opis
Implementacja `UISprite`, widLLetu do wyLwietlania pojedynczego sprite'a z plikow `.spr`.
## Klasa `UISprite`
## Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widLLet. JeLli `m_sprite` jest zaL'adowany, rysuje go wewnatrz prostokata widLLetu z uwzglednieniem paddingu. |
| `setSpriteId(uint32 id)` | Ustawia ID sprite'a do wyLwietlenia. Pobiera obraz z `g_sprites`, a nastepnie tworzy z niego teksture. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `sprite-id`, `sprite-color`. |
## ZaleLLnoLci i powiazania
- **`spritemanager.h`**: ULLywa `g_sprites` do pobierania obrazow sprite'ow.
- **`framework/otml/otml.h`**: Do parsowania stylow.
- **`framework/graphics/graphics.h`**: Do operacji rysowania i zarzadzania teksturami.

---
# z"" uisprite.h
## Ogolny opis
Plik nagL'owkowy dla `UISprite`, widLLetu do wyLwietlania pojedynczego sprite'a.
## Klasa `UISprite`
## Opis
Dziedziczy po `UIWidget`. Prosty widLLet, ktorego jedynym celem jest wyLwietlenie obrazu sprite'a o danym ID.
## Metody
| Nazwa | Opis |
| --- | --- |
| `setSpriteId(uint32 id)` | Ustawia ID sprite'a do wyLwietlenia. |
| `getSpriteId()` | Zwraca ID sprite'a. |
| `setSpriteColor(Color color)` | Ustawia kolor, w jakim sprite ma byc renderowany. |
| `hasSprite()` | Zwraca `true`, jeLli sprite jest zaL'adowany. |
## ZaleLLnoLci i powiazania
- **`declarations.h`**: Definicje typow.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# z"" walkmatrix.h
## Ogolny opis
Plik nagL'owkowy definiujacy klase `WalkMatrix`, ktora jest uLLywana do Lledzenia i zarzadzania predykcjami krokow lokalnego gracza w nowym systemie chodzenia (`GameNewWalking`).
## Klasa `WalkMatrix`
## Opis
Jest to macierz 7x7, ktora przechowuje wartoLci (liczniki lub ID predykcji) dla pol w zasiegu 3x3 wokoL' aktualnej pozycji gracza. SL'uLLy do synchronizacji krokow miedzy klientem a serwerem.
## Metody
| Nazwa | Opis |
| --- | --- |
| `updatePosition(const Position& newPos)` | Aktualizuje wewnetrzna pozycje gracza i przesuwa zawartoLc macierzy, aby odzwierciedlic ruch. Stare, odlegL'e wartoLci sa zerowane. |
| `inRange(const Position& pos2)` | Sprawdza, czy dana pozycja mieLci sie w zasiegu macierzy (3x3 wokoL' gracza). |
| `update(const Position& pos2, int32_t value)` | Ustawia wartoLc w macierzy dla danej pozycji. JeLli `value` nie jest podane, uLLywa inkrementowanego licznika. Zwraca ustawiona wartoLc, ktora sL'uLLy jako ID predykcji. |
| `get(const Position& pos2)` | Zwraca wartoLc z macierzy dla danej pozycji. |
| `clear()` | Zeruje caL'a macierz. |
| `reset(uint32_t value)` | WypeL'nia caL'a macierz dana wartoLcia. |
| `dump()` | Zwraca tekstowa reprezentacje macierzy do celow debugowania. |
## ZaleLLnoLci i powiazania
- **`position.h`**: ULLywa `Position` do operacji na wspoL'rzednych.
- **`localplayer.cpp`**: Obiekt `WalkMatrix` jest polem klasy `LocalPlayer` i jest uLLywany w logice pre-walkingu.

---
# z"" protocolgameparse.cpp
## Ogolny opis
Plik ten zawiera implementacje metod klasy `ProtocolGame` odpowiedzialnych za **parsowanie** pakietow przychodzacych z serwera gry. Jest to serce logiki sieciowej po stronie klienta.
## Klasa `ProtocolGame`
## Metody
## `parseMessage(const InputMessagePtr& msg)`
GL'owna funkcja-dyspozytor. Odczytuje jednobajtowy kod operacyjny (opcode) z wiadomoLci, a nastepnie wywoL'uje odpowiednia metode `parse...` do przetworzenia reszty pakietu. ObsL'uguje rownieLL niestandardowe opkody i przekazywanie ich do Lua.
## Metody `parse...`
KaLLda metoda `parse...` jest odpowiedzialna za odczytanie danych z `InputMessage` dla konkretnego opkodu i zaktualizowanie stanu gry. PrzykL'ady:
- **`parseMapDescription(...)`**: Parsuje peL'ny opis widocznego obszaru mapy, tworzac pola i obiekty.
- **`parseTileAddThing(...)`**: Dodaje nowy obiekt na mape.
- **`parseCreatureMove(...)`**: Aktualizuje pozycje stworzenia na mapie.
- **`parseCreatureHealth(...)`**: Aktualizuje procent LLycia stworzenia.
- **`parseTalk(...)`**: Przetwarza wiadomoLc czatu i przekazuje ja do `g_game`.
- **`parseOpenContainer(...)`**: Tworzy nowy kontener i wypeL'nia go przedmiotami.
- **`parsePlayerStats(...)`**: Aktualizuje statystyki lokalnego gracza.
- **`parseCancelWalk(...)`**: Informuje `g_game` o anulowaniu kroku.
## Metody pomocnicze `get...`
- **`getThing(...)`**, **`getItem(...)`**, **`getCreature(...)`**, **`getPosition(...)`**: Funkcje pomocnicze, ktore odczytuja zL'oLLone typy danych (jak `Item` czy `Creature`) z `InputMessage`, uwzgledniajac roLLnice w formacie zaleLLne od `GameFeature`. `getCreature`, na przykL'ad, decyduje, czy stworzyc nowy obiekt `Creature`, czy zaktualizowac istniejacy.
## ZaleLLnoLci i powiazania
- **`game.h`**, **`map.h`**, **`localplayer.h`**: LsciLle wspoL'pracuje z tymi klasami, wywoL'ujac ich metody w celu aktualizacji stanu gry.
- **`thingtypemanager.h`**: ULLywa `g_things` do weryfikacji ID przedmiotow i efektow.
- **`luavaluecasts_client.h`**: ULLywane do przekazywania zL'oLLonych obiektow do Lua.
- **`protocolcodes.h`**: ULLywa zdefiniowanych tam kodow operacyjnych.

---
# z"' Spis treLci

- [z"" animatedtext.cpp](#-animatedtextcpp)
  - [Klasa `AnimatedText`](#-klasa-animatedtext)
- [z"" houses.h](#-housesh)
  - [Klasa `House`](#-klasa-house)
  - [Klasa `HouseManager`](#-klasa-housemanager)
- [z"" animatedtext.h](#-animatedtexth)
  - [Klasa `AnimatedText`](#-klasa-animatedtext-1)
- [z"" animator.h](#-animatorh)
  - [Klasa `Animator`](#-klasa-animator)
- [z"" animator.cpp](#-animatorcpp)
  - [Klasa `Animator`](#-klasa-animator-1)
- [z"" client.cpp](#-clientcpp)
  - [Klasa `Client`](#-klasa-client)
- [z"" client.h](#-clienth)
  - [Klasa `Client`](#-klasa-client-1)
- [z"" CMakeLists.txt](#-cmakeliststxt)
- [z"" const.h](#-consth)
  - [Namespace `Otc`](#-namespace-otc)
- [z"" container.cpp](#-containercpp)
  - [Klasa `Container`](#-klasa-container)
- [z"" creature.cpp](#-creaturecpp)
  - [Klasa `Creature`](#-klasa-creature)
- [z"" container.h](#-containerh)
  - [Klasa `Container`](#-klasa-container-1)
- [z"" creature.h](#-creatureh)
  - [Klasa `Creature`](#-klasa-creature-1)
  - [Klasa `Npc`](#-klasa-npc)
  - [Klasa `Monster`](#-klasa-monster)
- [z"" creatures.h](#-creaturesh)
  - [Klasa `Spawn`](#-klasa-spawn)
  - [Klasa `CreatureType`](#-klasa-creaturetype)
  - [Klasa `CreatureManager`](#-klasa-creaturemanager)
- [z"" declarations.h](#-declarationsh)
- [z"" creatures.cpp](#-creaturescpp)
  - [Klasa `Spawn`](#-klasa-spawn-1)
  - [Klasa `CreatureType`](#-klasa-creaturetype-1)
  - [Klasa `CreatureManager`](#-klasa-creaturemanager-1)
- [z"" effect.cpp](#-effectcpp)
  - [Klasa `Effect`](#-klasa-effect)
- [z"" global.h](#-globalh)
- [z"" effect.h](#-effecth)
  - [Klasa `Effect`](#-klasa-effect-1)
- [z"" healthbars.cpp](#-healthbarscpp)
  - [Klasa `HealthBars`](#-klasa-healthbars)
  - [Klasa `HealthBar`](#-klasa-healthbar)
- [z"" game.h](#-gameh)
  - [Klasa `Game`](#-klasa-game)
- [z"" healthbars.h](#-healthbarsh)
  - [Klasa `HealthBar`](#-klasa-healthbar-1)
  - [Klasa `HealthBars`](#-klasa-healthbars-1)
- [z"" houses.cpp](#-housescpp)
  - [Klasa `House`](#-klasa-house-1)
  - [Klasa `HouseManager`](#-klasa-housemanager-1)
- [z"" item.cpp](#-itemcpp)
  - [Klasa `Item`](#-klasa-item)
- [z"" itemtype.cpp](#-itemtypecpp)
  - [Klasa `ItemType`](#-klasa-itemtype)
- [z"" item.h](#-itemh)
  - [Klasa `Item`](#-klasa-item-1)
- [z"" itemtype.h](#-itemtypeh)
  - [Klasa `ItemType`](#-klasa-itemtype-1)
- [z"" lightview.cpp](#-lightviewcpp)
  - [Klasa `LightView`](#-klasa-lightview)
- [z"" lightview.h](#-lightviewh)
  - [Klasa `LightView`](#-klasa-lightview-1)
- [z"" localplayer.cpp](#-localplayercpp)
  - [Klasa `LocalPlayer`](#-klasa-localplayer)
- [z"" map.cpp](#-mapcpp)
  - [Klasa `Map`](#-klasa-map)
- [z"" map.h](#-maph)
  - [Klasa `Map`](#-klasa-map-1)
- [z"" luavaluecasts_client.h](#-luavaluecasts_clienth)
- [z"" mapio.cpp](#-mapiocpp)
  - [Klasa `Map`](#-klasa-map-2)
- [z"" luavaluecasts_client.cpp](#-luavaluecasts_clientcpp)
- [z"" mapview.cpp](#-mapviewcpp)
  - [Klasa `MapView`](#-klasa-mapview)
- [z"" mapview.h](#-mapviewh)
  - [Klasa `MapView`](#-klasa-mapview-1)
- [z"" minimap.h](#-minimaph)
  - [Klasa `MinimapBlock`](#-klasa-minimapblock)
  - [Klasa `Minimap`](#-klasa-minimap)
- [z"" missile.cpp](#-missilecpp)
  - [Klasa `Missile`](#-klasa-missile)
- [z"" missile.h](#-missileh)
  - [Klasa `Missile`](#-klasa-missile-1)
- [z"" outfit.cpp](#-outfitcpp)
  - [Klasa `Outfit`](#-klasa-outfit)
- [z"" outfit.h](#-outfith)
  - [Klasa `Outfit`](#-klasa-outfit-1)
- [z"" player.cpp](#-playercpp)
  - [Klasa `Player`](#-klasa-player)
- [z"" player.h](#-playerh)
  - [Klasa `Player`](#-klasa-player-1)
- [z"" protocolcodes.cpp](#-protocolcodescpp)
  - [Namespace `Proto`](#-namespace-proto)
- [z"" minimap.cpp](#-minimapcpp)
  - [Klasa `MinimapBlock`](#-klasa-minimapblock-1)
  - [Klasa `Minimap`](#-klasa-minimap-1)
- [z"" position.h](#-positionh)
  - [Struktura `Position`](#-struktura-position)
  - [Struktura `PositionHasher`](#-struktura-positionhasher)
- [z"" protocolcodes.h](#-protocolcodesh)
  - [Namespace `Proto`](#-namespace-proto-1)
- [z"" protocolgame.cpp](#-protocolgamecpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame)
- [z"" protocolgame.h](#-protocolgameh)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-1)
- [z"" spritemanager.cpp](#-spritemanagercpp)
  - [Klasa `SpriteManager`](#-klasa-spritemanager)
- [z"" protocolgamesend.cpp](#-protocolgamesendcpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-2)
- [z"" localplayer.h](#-localplayerh)
  - [Klasa `LocalPlayer`](#-klasa-localplayer-1)
- [z"" towns.cpp](#-townscpp)
  - [Klasa `Town`](#-klasa-town)
  - [Klasa `TownManager`](#-klasa-townmanager)
- [z"" spritemanager.h](#-spritemanagerh)
  - [Klasa `SpriteManager`](#-klasa-spritemanager-1)
- [z"" tile.cpp](#-tilecpp)
  - [Klasa `Tile`](#-klasa-tile)
- [z"" statictext.h](#-statictexth)
  - [Klasa `StaticText`](#-klasa-statictext)
- [z"" uimapanchorlayout.cpp](#-uimapanchorlayoutcpp)
  - [Klasa `UIPositionAnchor`](#-klasa-uipositionanchor)
  - [Klasa `UIMapAnchorLayout`](#-klasa-uimapanchorlayout)
- [z"" thing.h](#-thingh)
  - [Klasa `Thing`](#-klasa-thing)
- [z"" uiitem.h](#-uiitemh)
  - [Klasa `UIItem`](#-klasa-uiitem)
- [z"" thing.cpp](#-thingcpp)
  - [Klasa `Thing`](#-klasa-thing-1)
- [z"" uimap.cpp](#-uimapcpp)
  - [Klasa `UIMap`](#-klasa-uimap)
- [z"" thingstype.h](#-thingstypeh)
  - [Klasa `ThingsType`](#-klasa-thingstype)
- [z"" uigraph.h](#-uigraphh)
  - [Klasa `UIGraph`](#-klasa-uigraph)
- [z"" uicreature.h](#-uicreatureh)
  - [Klasa `UICreature`](#-klasa-uicreature)
- [z"" thingtype.cpp](#-thingtypecpp)
  - [Klasa `ThingType`](#-klasa-thingtype)
- [z"" towns.h](#-townsh)
  - [Klasa `Town`](#-klasa-town-1)
  - [Klasa `TownManager`](#-klasa-townmanager-1)
- [z"" thingtype.h](#-thingtypeh)
  - [Klasa `ThingType`](#-klasa-thingtype-1)
- [z"" uicreature.cpp](#-uicreaturecpp)
  - [Klasa `UICreature`](#-klasa-uicreature-1)
- [z"" thingtypemanager.h](#-thingtypemanagerh)
  - [Klasa `ThingTypeManager`](#-klasa-thingtypemanager)
- [z"" thingtypemanager.cpp](#-thingtypemanagercpp)
  - [Klasa `ThingTypeManager`](#-klasa-thingtypemanager-1)
- [z"" tile.h](#-tileh)
  - [Klasa `Tile`](#-klasa-tile-1)
- [z"" uimap.h](#-uimaph)
  - [Klasa `UIMap`](#-klasa-uimap-1)
- [z"" uiminimap.cpp](#-uiminimappp)
  - [Klasa `UIMinimap`](#-klasa-uiminimap)
- [z"" uiprogressrect.cpp](#-uiprogressrectcpp)
  - [Klasa `UIProgressRect`](#-klasa-uiprogressrect)
- [z"" uimapanchorlayout.h](#-uimapanchorlayouth)
  - [Klasa `UIPositionAnchor`](#-klasa-uipositionanchor-1)
  - [Klasa `UIMapAnchorLayout`](#-klasa-uimapanchorlayout-1)
- [z"" uiminimap.h](#-uiminimaph)
  - [Klasa `UIMinimap`](#-klasa-uiminimap-1)
- [z"" game.cpp](#-gamecpp)
  - [Klasa `Game`](#-klasa-game-1)
- [z"" uiprogressrect.h](#-uiprogressrecth)
  - [Klasa `UIProgressRect`](#-klasa-uiprogressrect-1)
- [z"" uisprite.cpp](#-uispritecpp)
  - [Klasa `UISprite`](#-klasa-uisprite)
- [z"" uisprite.h](#-uispriteh)
  - [Klasa `UISprite`](#-klasa-uisprite-1)
- [z"" walkmatrix.h](#-walkmatrixh)
  - [Klasa `WalkMatrix`](#-klasa-walkmatrix)
- [z"" protocolgameparse.cpp](#-protocolgameparsecpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-3)
- [z"" luafunctions_client.cpp](#-luafunctions_clientcpp)
# z"T Indeks funkcji/metod
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
# z Mapa zaleLLnoLci
PoniLLszy diagram przedstawia gL'owne zaleLLnoLci i przepL'yw informacji miedzy kluczowymi moduL'ami systemu.

graph TD
    subgraph "Aplikacja i UI"
        Client[Client] -->|inicjalizuje| Game
        Client -->|inicjalizuje| Map
        Client -->|inicjalizuje| ThingTypeManager
        UIMap[UIMap] -->|renderuje| MapView
        MapView -->|odczytuje dane| Map
        UICreature[UICreature] -->|wyLwietla| Creature
        UIItem[UIItem] -->|wyLwietla| Item
    end

    subgraph "Logika Gry"
        Game[Game] -->|wysyL'a akcje| ProtocolGame
        Game -->|zarzadza| LocalPlayer
        Game -->|zarzadza| Map
        LocalPlayer[LocalPlayer] -->|dziedziczy| Player
        Player -->|dziedziczy| Creature
        Creature -->|dziedziczy| Thing
        Item -->|dziedziczy| Thing
        Thing -->|ma| ThingType
    end

    subgraph "Siec"
        ProtocolGame[ProtocolGame] -->|parsuje pakiety| Game
        ProtocolGame -->|wysyL'a pakiety| TCPSocket
    end

    subgraph "Dane i Zasoby"
        ThingTypeManager[ThingTypeManager] -->|wczytuje| DAT["things.dat"]
        ThingTypeManager -->|wczytuje| OTB["items.otb"]
        SpriteManager[SpriteManager] -->|wczytuje| SPR["sprites.spr"]
        Map -->|wczytuje| OTBM["map.otbm"]
        Minimap -->|wczytuje| OTMM["minimap.otmm"]
        ThingType -->|uLLywa| SpriteManager
    end

    MapView --> Creature
    MapView --> Item
    Map --> Tile
    Tile --> Thing
```

**Opis zaleLLnoLci:**
-   **Client** jest punktem startowym, ktory inicjalizuje wszystkie gL'owne moduL'y (`Game`, `Map`, `ThingTypeManager`).
-   **Game** jest centralnym "mozgiem" aplikacji, zarzadzajacym stanem gry, lokalnym graczem i komunikacja sieciowa poprzez `ProtocolGame`.
-   **ProtocolGame** jest odpowiedzialny za serializacje i deserializacje danych przesyL'anych do i z serwera. Aktualizuje stan `Game` na podstawie otrzymanych pakietow.
-   **Map** przechowuje wszystkie dane o Lwiecie gry, w tym `Tile` (pola) i `Thing` (obiekty).
-   **MapView** jest odpowiedzialny za renderowanie danych z `Map` na ekranie. Jest to warstwa wizualizacyjna dla danych mapy.
-   **ThingTypeManager** i **SpriteManager** to menedLLery zasobow, ktore wczytuja dane z plikow `.dat`, `.otb` i `.spr`, dostarczajac definicje i grafiki dla wszystkich obiektow w grze.
-   Hierarchia dziedziczenia obiektow: `Thing` jest baza dla `Item` i `Creature`. `Creature` jest baza dla `Player`, a `Player` dla `LocalPlayer`.
-   WidLLety UI (`UIMap`, `UICreature`, `UIItem`) sa wyspecjalizowanymi komponentami do wyLwietlania odpowiednich elementow logiki gry.
# z Architektura systemu
System jest zbudowany w oparciu o architekture warstwowa, gdzie kaLLda warstwa ma jasno zdefiniowane obowiazki. MoLLna wyroLLnic nastepujace gL'owne komponenty:

1.  **Framework (Warstwa podstawowa)**
    -   **Core**: Zarzadzanie aplikacja, petla gL'owna, zdarzeniami (`EventDispatcher`), zasobami (`ResourceManager`), czasem (`Clock`).
    -   **Graphics**: Nisko-poziomowe renderowanie, zarzadzanie teksturami (`TextureManager`), shaderami (`ShaderManager`), czcionkami (`FontManager`) i kolejka rysowania (`DrawQueue`).
    -   **UI**: System interfejsu uLLytkownika oparty na widLLetach (`UIWidget`) i stylach OTML.
    -   **LuaEngine**: Integracja z silnikiem skryptowym Lua, umoLLliwiajaca rozszerzanie logiki gry.
    -   **Net**: Nisko-poziomowa obsL'uga poL'aczeL" sieciowych (`Protocol`, `Connection`).

2.  **Client (Warstwa aplikacji)**
    -   **Zarzadzanie stanem gry (`Game`)**: Centralny singleton, ktory zarzadza sesja gry, stanem lokalnego gracza, interakcjami i komunikacja z serwerem. DziaL'a jak fasada dla reszty systemu.
    -   **ObsL'uga protokoL'u (`ProtocolGame`)**: Implementacja protokoL'u sieciowego. TL'umaczy akcje gracza na pakiety i pakiety z serwera na zmiany w stanie gry.
    -   **Reprezentacja Lwiata gry (`Map`, `Tile`, `Thing`)**: Obiektowy model Lwiata gry. `Map` przechowuje kolekcje `Tile`, a kaLLdy `Tile` przechowuje stos `Thing` (przedmiotow, stworzeL", etc.).
    -   **Zarzadzanie zasobami gry (`ThingTypeManager`, `SpriteManager`)**: Singletony odpowiedzialne za wczytywanie i dostarczanie definicji i grafik dla wszystkich obiektow w grze z plikow `.dat`, `.otb`, `.spr`.
    -   **Renderowanie (`MapView`, `Minimap`)**: Klasy odpowiedzialne za wizualizacje danych z `Map`. `MapView` renderuje gL'owny widok gry, a `Minimap` - minimape. Wykorzystuja one `DrawQueue` z warstwy frameworka.
    -   **UI klienta (`UIMap`, `UIItem`, `UICreature`)**: Wyspecjalizowane widLLety, ktore L'acza dane z logiki gry (np. `Item`, `Creature`) z systemem UI frameworka.
## PrzepL'yw danych i zdarzeL"
-   **WejLcie uLLytkownika**: Zdarzenia wejLcia (mysz, klawiatura) sa przechwytywane przez `UIWidget`. JeLli akcja dotyczy gry (np. klikniecie na mapie), wywoL'ywana jest odpowiednia metoda w `Game` (np. `g_game.walk()`).
-   **WysyL'anie danych**: `Game` wywoL'uje metode w `ProtocolGame` (np. `sendWalkNorth()`), ktora tworzy pakiet i wysyL'a go na serwer.
-   **Odbieranie danych**: `ProtocolGame` odbiera pakiet, `parseMessage` identyfikuje jego typ na podstawie opkodu i wywoL'uje odpowiednia metode `parse...`.
-   **Aktualizacja stanu**: Metoda `parse...` (np. `parseCreatureMove`) odczytuje dane z pakietu i wywoL'uje metody w `Game` lub `Map` (np. `g_map.addThing(...)`), ktore modyfikuja stan gry.
-   **Renderowanie**: W kaLLdej klatce, `UIMap` wywoL'uje `MapView::drawMapBackground` i `drawMapForeground`. `MapView` pobiera aktualny stan z `g_map` (widoczne `Tile` i `Thing`), a nastepnie rysuje je na ekranie, uLLywajac `ThingTypeManager` i `SpriteManager` do uzyskania odpowiednich grafik.

Ta architektura oddziela logike gry od renderowania i obsL'ugi sieci, co uL'atwia zarzadzanie kodem i jego rozbudowe. ULLycie Lua pozwala na dynamiczne modyfikowanie zachowaL" interfejsu i logiki bez potrzeby rekompilacji caL'ego klienta.
