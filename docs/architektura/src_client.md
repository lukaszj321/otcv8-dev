?# otclientv8-dev/src/client

> NOTE: Wszystkie pliki w repozytorium sa objete licencja MIT (2010-2017 OTClient, autor Edubart).
# # Og�lny opis
Implementacja klasy `AnimatedText`, kt�ra odpowiada za renderowanie animowanego tekstu na mapie, takiego jak komunikaty o zadanych obrazeniach, leczeniu czy zdobytych punktach doswiadczenia. Plik zawiera logike animacji, rysowania oraz laczenia podobnych tekst�w w jeden.
# # Klasa `AnimatedText`
# # # Opis
Klasa `AnimatedText` dziedziczy po `Thing` i reprezentuje tekst, kt�ry pojawia sie w okreslonym miejscu na mapie, a nastepnie animuje swoje polozenie i przezroczystosc, by ostatecznie zniknac.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `AnimatedText()` | Konstruktor. Inicjalizuje domyslne wlasciwosci tekstu, takie jak czcionka i wyr�wnanie. |
| `drawText(const Point& dest, const Rect& visibleRect)` | Rysuje tekst w okreslonym miejscu, uwzgledniajac postep animacji. Animacja obejmuje ruch w g�re (i opcjonalnie po przekatnej) oraz stopniowe zanikanie. |
| `onAppear()` | Metoda wywolywana, gdy tekst pojawia sie na mapie. Resetuje timer animacji i planuje usuniecie obiektu po zakonczeniu animacji. |
| `setColor(int color)` | Ustawia kolor tekstu na podstawie 8-bitowej wartosci. |
| `setText(const std::string& text)` | Ustawia tresc tekstu. |
| `setFont(const std::string& fontName)` | Ustawia czcionke tekstu na podstawie nazwy. |
| `merge(const AnimatedTextPtr& other)` | Pr�buje polaczyc tekst z innym obiektem `AnimatedText`. Laczenie jest mozliwe, jesli oba teksty maja ten sam kolor, czcionke, a animacja obecnego tekstu nie jest zbyt zaawansowana. Teksty liczbowe sa sumowane. |
# # # Zaleznosci i powiazania
- **`map.h`**: Uzywa `g_map` do usuwania obiektu `AnimatedText` po zakonczeniu animacji.
- **`game.h`**: Uzywa `g_game` do sprawdzania, czy funkcja `GameDiagonalAnimatedText` jest wlaczona.
- **`framework/core/clock.h`**: Uzywa `g_clock` do pomiaru czasu animacji.
- **`framework/core/eventdispatcher.h`**: Uzywa `g_dispatcher` do planowania usuniecia obiektu.
- **`framework/graphics/graphics.h`**: Uzywa `g_fonts` do zarzadzania czcionkami.
# # # Przyklad uzycia
Obiekty `AnimatedText` sa tworzone przez `ProtocolGame` w odpowiedzi na komunikaty serwera (np. o obrazeniach) i dodawane do `g_map`, kt�ra zarzadza ich cyklem zycia i rysowaniem.

```cpp
// Przyklad tworzenia (logika w ProtocolGame::parseAnimatedText)
AnimatedTextPtr animatedText = AnimatedTextPtr(new AnimatedText);
animatedText->setColor(color);
animatedText->setText(text);
g_map.addThing(animatedText, position);
```
---
# ?? houses.h
# # Og�lny opis
Plik ten definiuje klasy `House` i `HouseManager`, kt�re sluza do zarzadzania informacjami o domach w grze. Zawiera definicje struktur przechowujacych atrybuty dom�w, takie jak nazwa, ID, wejscie, oraz metody do zarzadzania nimi.
# # Klasa `House`
# # # Opis
Reprezentuje pojedynczy dom w swiecie gry. Przechowuje jego atrybuty, liste przynaleznych do niego p�l (tiles) oraz drzwi.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `House(uint32 hId, ...)` | Konstruktor tworzacy dom o zadanym ID, nazwie i pozycji wejsciowej. |
| `setTile(const TilePtr& tile)` | Dodaje pole (tile) do domu. |
| `getTile(const Position& pos)` | Zwraca wskaznik do pola na podanej pozycji, jesli nalezy ono do domu. |
| `setName(const std::string& name)` | Ustawia nazwe domu. |
| `getName()` | Zwraca nazwe domu. |
| `setId(uint32 hId)` | Ustawia unikalne ID domu. |
| `getId()` | Zwraca ID domu. |
| `setTownId(uint32 tid)` | Ustawia ID miasta, w kt�rym znajduje sie dom. |
| `getTownId()` | Zwraca ID miasta. |
| `setSize(uint32 s)` | Ustawia rozmiar domu. |
| `getSize()` | Zwraca rozmiar domu. |
| `setRent(uint32 r)` | Ustawia cene wynajmu domu. |
| `getRent()` | Zwraca cene wynajmu. |
| `setEntry(const Position& p)` | Ustawia pozycje wejscia do domu. |
| `getEntry()` | Zwraca pozycje wejscia. |
| `addDoor(const ItemPtr& door)` | Dodaje drzwi do domu i przypisuje im unikalne ID. |
| `removeDoor(const ItemPtr& door)` | Usuwa drzwi z domu. |
| `removeDoorById(uint32 doorId)` | Usuwa drzwi na podstawie ich ID. |
# # Klasa `HouseManager`
# # # Opis
Singleton (`g_houses`) zarzadzajacy wszystkimi domami w grze. Odpowiada za ich dodawanie, usuwanie, wczytywanie i zapisywanie z plik�w XML.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `addHouse(const HousePtr& house)` | Dodaje nowy dom do listy. |
| `removeHouse(uint32 houseId)` | Usuwa dom o podanym ID. |
| `getHouse(uint32 houseId)` | Zwraca dom o podanym ID. |
| `getHouseByName(std::string name)` | Zwraca dom o podanej nazwie. |
| `load(const std::string& fileName)` | Wczytuje dane o domach z pliku XML. |
| `save(const std::string& fileName)` | Zapisuje dane o domach do pliku XML. |
| `sort()` | Sortuje liste dom�w alfabetycznie wedlug nazwy. |
| `clear()` | Czysci liste dom�w. |
| `getHouseList()` | Zwraca liste wszystkich dom�w. |
| `filterHouses(uint32 townId)` | Zwraca liste dom�w nalezacych do okreslonego miasta. |
# # # Zmienne globalne
- `HouseManager g_houses`: Globalna instancja managera dom�w.
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w wskaznik�w, takich jak `HousePtr` i `TilePtr`.
- **`tile.h`**: Uzywa obiekt�w `Tile` do okreslenia obszaru domu.
- **`item.h`**: Zarzadza drzwiami, kt�re sa obiektami typu `Item`.
- **`framework/luaengine/luaobject.h`**: Klasy sa eksponowane do Lua.

---
# ?? animatedtext.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `AnimatedText`. Definiuje interfejs klasy, kt�ra zarzadza animowanym tekstem na mapie.
# # Klasa `AnimatedText`
# # # Opis
Dziedziczy po `Thing`. Sluzy do wyswietlania tekstu, kt�ry porusza sie i zanika. Jest to obiekt "efemeryczny", kt�ry istnieje na mapie tylko przez czas trwania animacji.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `AnimatedText()` | Konstruktor. |
| `drawText(const Point& dest, const Rect& visibleRect)` | Rysuje tekst na ekranie z uwzglednieniem animacji. |
| `setColor(int color)` | Ustawia kolor tekstu. |
| `setText(const std::string& text)` | Ustawia tresc tekstu. |
| `setOffset(const Point& offset)` | Ustawia przesuniecie (offset) rysowania tekstu, uzywane do unikania nakladania sie tekst�w. |
| `setFont(const std::string& fontName)` | Ustawia czcionke tekstu. |
| `getColor()` | Zwraca kolor tekstu. |
| `getCachedText()` | Zwraca obiekt `CachedText` przechowujacy tekst i informacje o renderowaniu. |
| `getOffset()` | Zwraca aktualne przesuniecie tekstu. |
| `getTimer()` | Zwraca timer uzywany do animacji. |
| `merge(const AnimatedTextPtr& other)` | Funkcja do laczenia z innym `AnimatedText`. |
| `asAnimatedText()` | Rzutuje wskaznik na `AnimatedTextPtr`. |
| `isAnimatedText()` | Zwraca `true`. |
| `getText()` | Zwraca tresc tekstu. |
# # # Zaleznosci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/graphics/fontmanager.h`**: Zarzadzanie czcionkami.
- **`framework/core/timer.h`**: Pomiar czasu animacji.
- **`framework/graphics/cachedtext.h`**: Efektywne renderowanie tekstu.

---
# ?? animator.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Animator`, kt�ra zarzadza animacjami klatek dla obiekt�w w grze, takich jak przedmioty czy efekty.
# # Klasa `Animator`
# # # Opis
Klasa `Animator` kontroluje, kt�ra klatka animacji powinna byc wyswietlona w danym momencie. Obsluguje r�zne tryby animacji, takie jak petle, ping-pong, animacje asynchroniczne i losowe.
# # # Typy wyliczeniowe
- **`AnimationPhase`**: Okresla faze animacji (np. automatyczna, losowa, asynchroniczna).
- **`AnimationDirection`**: Okresla kierunek animacji (do przodu, do tylu).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `Animator()` | Konstruktor. |
| `unserialize(int animationPhases, const FileStreamPtr& fin)` | Wczytuje dane animatora ze strumienia. |
| `serialize(const FileStreamPtr& fin)` | Zapisuje dane animatora do strumienia. |
| `setPhase(int phase)` | Ustawia biezaca faze animacji. |
| `getPhase()` | Oblicza i zwraca biezaca faze animacji na podstawie czasu. |
| `getPhaseAt(Timer& timer, int lastPhase)` | Oblicza faze animacji w danym momencie czasu (uzywane przez `Effect` dla niezaleznych animacji). |
| `getStartPhase()` | Zwraca poczatkowa faze animacji. |
| `getAnimationPhases()` | Zwraca calkowita liczbe faz animacji. |
| `isAsync()` | Zwraca `true`, jesli animacja jest asynchroniczna. |
| `isComplete()` | Zwraca `true`, jesli animacja zostala zakonczona. |
| `getTotalDuration()` | Zwraca calkowity czas trwania animacji. |
| `resetAnimation()` | Resetuje stan animacji do poczatkowego. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`framework/core/timer.h`**: Uzywane do pomiaru czasu i synchronizacji animacji.

---
# ?? animator.cpp
# # Og�lny opis
Implementacja klasy `Animator`. Zawiera logike obliczania faz animacji w zaleznosci od czasu i trybu pracy.
# # Klasa `Animator`
# # # Opis
Plik implementuje logike dzialania animatora. Obliczenia fazy zaleza od tego, czy animacja jest synchroniczna (wszystkie obiekty tego samego typu animuja sie tak samo) czy asynchroniczna (kazdy obiekt animuje sie niezaleznie).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(...)` | Wczytuje z pliku binarnego liczbe faz, tryb `async`, liczbe petli, faze startowa oraz czas trwania kazdej klatki (min/max). |
| `serialize(...)` | Zapisuje dane animatora do pliku binarnego. |
| `setPhase(int phase)` | Ustawia aktualna faze animacji. Dla animacji asynchronicznych resetuje timer i ustawia czas trwania klatki. Dla synchronicznych przelicza faze na podstawie globalnego zegara. |
| `getPhase()` | Gl�wna metoda aktualizujaca. Na podstawie czasu, jaki uplynal od ostatniego wywolania, decyduje, czy nalezy przejsc do nastepnej klatki animacji. |
| `getPhaseAt(...)` | Metoda uzywana przez efekty (`Effect`) do uzyskania fazy animacji niezaleznie od innych obiekt�w tego samego typu. Uzywa wlasnego timera i pseudolosowego generatora do okreslenia czasu trwania klatek. |
| `getStartPhase()` | Zwraca faze startowa; jesli ustawiono na losowa, losuje ja z dostepnego zakresu. |
| `resetAnimation()` | Przywraca animator do stanu poczatkowego. |
| `getPingPongPhase()` | Oblicza nastepna faze dla animacji typu "ping-pong" (do przodu i do tylu). |
| `getLoopPhase()` | Oblicza nastepna faze dla animacji w petli. |
| `getPhaseDuration(int phase)` | Zwraca czas trwania danej klatki animacji (losowy w zakresie min-max). |
| `calculateSynchronous()` | Oblicza biezaca faze dla animacji synchronicznej, bazujac na globalnym czasie i sumarycznym czasie trwania wszystkich klatek. |
| `getTotalDuration()` | Zwraca sumaryczny czas trwania wszystkich klatek animacji. |
# # # Zaleznosci i powiazania
- **`framework/core/clock.h`**: Uzywa `g_clock` do synchronizacji animacji.
- **`framework/core/filestream.h`**: Do operacji serializacji/deserializacji.

---
# ?? client.cpp
# # Og�lny opis
Plik implementuje klase `Client`, kt�ra jest gl�wnym punktem wejscia i zarzadzania dla aplikacji klienckiej. Odpowiada za inicjalizacje i zamykanie kluczowych modul�w gry.
# # Klasa `Client`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `init(std::vector<std::string>& args)` | Inicjalizuje wszystkie gl�wne moduly klienta w odpowiedniej kolejnosci: rejestruje funkcje Lua, a nastepnie inicjalizuje `g_map`, `g_minimap`, `g_game`, `g_shaders`, `g_things`, `g_healthBars`. |
| `terminate()` | Zamyka wszystkie moduly w odwrotnej kolejnosci do inicjalizacji, zwalniajac zasoby. |
# # # Zmienne globalne
- `Client g_client`: Globalna instancja klasy `Client`.
# # # Zaleznosci i powiazania
- **`game.h`**: Inicjalizuje i zamyka `g_game`.
- **`map.h`**: Inicjalizuje i zamyka `g_map`.
- **`minimap.h`**: Inicjalizuje i zamyka `g_minimap`.
- **`spritemanager.h`**: Posrednio zarzadza `g_sprites` poprzez `g_things`.
- **`healthbars.h`**: Inicjalizuje i zamyka `g_healthBars`.
- **`framework/core/modulemanager.h`**: Uzywane do zarzadzania modulami.
- **`framework/graphics/shadermanager.h`**: Inicjalizuje i zamyka `g_shaders`.

---
# ?? client.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Client`. Deklaruje interfejs gl�wnej klasy aplikacji klienckiej.
# # Klasa `Client`
# # # Opis
Klasa `Client` jest odpowiedzialna za zarzadzanie cyklem zycia aplikacji klienckiej.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `init(std::vector<std::string>& args)` | Inicjalizuje aplikacje. |
| `terminate()` | Konczy dzialanie aplikacji, zwalniajac zasoby. |
| `registerLuaFunctions()` | Rejestruje funkcje C++ dostepne w srodowisku Lua. |
# # # Zmienne globalne
- `Client g_client`: Deklaracja zewnetrznej globalnej instancji klienta.
# # # Zaleznosci i powiazania
- **`global.h`**: Zawiera podstawowe definicje i stale uzywane w kliencie.

---
# ?? CMakeLists.txt
# # Og�lny opis
Plik konfiguracyjny systemu budowania CMake dla modulu klienta. Definiuje on, kt�re pliki zr�dlowe (`.cpp`, `.h`) zostana skompilowane i wlaczone do finalnej aplikacji klienckiej.
# # Struktura pliku
# # # Definicje preprocesora
- `add_definitions(-DCLIENT)`: Dodaje makro `CLIENT` do wszystkich kompilowanych plik�w, co pozwala na warunkowa kompilacje kodu specyficznego dla klienta.
# # # Lista plik�w zr�dlowych (`client_SOURCES`)
Plik zawiera jedna dluga liste wszystkich plik�w zr�dlowych i nagl�wkowych, kt�re skladaja sie na modul klienta. Pliki sa pogrupowane w logiczne kategorie za pomoca komentarzy:
- **`# client`**: Gl�wne pliki klienta.
- **`# core`**: Rdzen logiki gry (mapa, przedmioty, postacie, etc.).
- **`# lua`**: Pliki zwiazane z integracja z silnikiem Lua.
- **`# net`**: Logika sieciowa i protokoly.
- **`# ui`**: Niestandardowe widzety interfejsu uzytkownika.
- **`# util`**: Pomocnicze klasy i struktury, jak `Position`.
# # # Zaleznosci i powiazania
Ten plik jest kluczowy dla procesu budowania i definiuje, kt�re czesci kodu zr�dlowego sa ze soba powiazane i tworza aplikacje kliencka. Kazdy plik dodany do tej listy staje sie czescia projektu.

---
# ?? const.h
# # Og�lny opis
Plik nagl�wkowy zawierajacy globalne stale i typy wyliczeniowe uzywane w calej aplikacji klienckiej. Definiuje kluczowe wartosci, takie jak flagi rysowania, atrybuty przedmiot�w, tryby gry, a takze identyfikatory funkcji serwera (`GameFeature`).
# # Namespace `Otc`
# # # Typy wyliczeniowe
- **`enum` (anonimowy)**: Zawiera og�lne stale, takie jak `MAX_ELEVATION`, `SEA_FLOOR`, `MAX_Z`, czasy trwania animacji (`ANIMATED_TEXT_DURATION`) i inne.
- **`DepthConst`**: Stale zwiazane z glebokoscia renderowania.
- **`DrawFlags`**: Flagi okreslajace, kt�re elementy sceny maja byc rysowane (np. podloze, postacie, efekty).
- **`DatOpts`**: Atrybuty przedmiot�w wczytywane z plik�w `.dat`.
- **`InventorySlot`**: Identyfikatory slot�w ekwipunku.
- **`Statistic`**: Identyfikatory statystyk gracza (zycie, mana, doswiadczenie).
- **`Skill`**: Identyfikatory umiejetnosci gracza.
- **`Direction`**: Kierunki (p�lnoc, poludnie, etc.).
- **`FluidsColor`**, **`FluidsType`**: Kolory i typy plyn�w.
- **`FightModes`**, **`ChaseModes`**, **`PVPModes`**: Tryby walki, scigania i PvP.
- **`PlayerSkulls`**: Typy czaszek nad glowa gracza.
- **`PlayerShields`**: Typy tarcz imprezowych (party shields).
- **`PlayerEmblems`**: Emblematy gildii.
- **`CreatureIcons`**: Ikony nad postaciami NPC.
- **`PlayerStates`**: Stany gracza (zatrucie, podpalenie, etc.).
- **`MessageMode`**: Tryby wiadomosci w grze (say, whisper, yell, etc.).
- **`GameFeature`**: Flagi okreslajace, kt�re funkcje sa obslugiwane przez serwer. Jest to kluczowy enum dla zapewnienia kompatybilnosci z r�znymi wersjami serwer�w.
- **`PathFindResult`**: Wyniki algorytmu wyszukiwania sciezki.
- **`PathFindFlags`**: Flagi modyfikujace dzialanie algorytmu wyszukiwania sciezki.
- **`AutomapFlags`**: Ikony znacznik�w na minimapie.
- **`VipState`**: Stany graczy na liscie VIP.
- **`SpeedFormula`**: R�zne formuly obliczania predkosci postaci.
- **`Blessings`**: Blogoslawienstwa.
- **`DeathType`**: Typ smierci (zwykla, z blogoslawienstwem).
- **`StoreProductTypes`**, **`StoreErrorTypes`**, **`StoreStates`**: Typy zwiazane ze sklepem w grze (Store).
- **`Prey...`**: Enumeracje zwiazane z systemem Prey.
- **`MagicEffectsType_t`**: Typy operacji w zaawansowanych efektach magicznych.
# # # Zaleznosci i powiazania
Ten plik jest fundamentalny i jest dolaczany w wiekszosci plik�w projektu, poniewaz definiuje podstawowe "slownictwo" uzywane w logice gry.

---
# ?? container.cpp
# # Og�lny opis
Implementacja klasy `Container`, kt�ra reprezentuje pojemniki w grze, takie jak plecaki. Plik zawiera logike zarzadzania przedmiotami wewnatrz kontenera oraz obsluge zdarzen z nim zwiazanych.
# # Klasa `Container`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `Container(...)` | Konstruktor. Inicjalizuje kontener na podstawie danych otrzymanych z serwera. |
| `getItem(int slot)` | Zwraca przedmiot znajdujacy sie w danym slocie. |
| `onOpen(const ContainerPtr& previousContainer)` | Wywoluje callback Lua `onOpen`, gdy kontener jest otwierany. |
| `onClose()` | Oznacza kontener jako zamkniety i wywoluje callback Lua `onClose`. |
| `onAddItem(const ItemPtr& item, int slot)` | Dodaje przedmiot do kontenera. Jesli kontener ma strony (`hasPages`), a slot jest poza widocznym zakresem, jedynie aktualizuje rozmiar. W przeciwnym razie dodaje przedmiot do listy i wywoluje callbacki Lua `onSizeChange` i `onAddItem`. |
| `findItemById(uint itemId, int subType)` | Wyszukuje przedmiot w kontenerze po jego ID i opcjonalnie podtypie. |
| `onAddItems(const std::vector<ItemPtr>& items)` | Dodaje wiele przedmiot�w naraz (np. przy otwarciu kontenera). |
| `onUpdateItem(int slot, const ItemPtr& item)` | Aktualizuje przedmiot w danym slocie, zastepujac stary nowym. |
| `onRemoveItem(int slot, const ItemPtr& lastItem)` | Usuwa przedmiot z danego slota. Jesli `lastItem` jest podany (dla kontener�w ze stronami), jest on dodawany na koncu widocznej czesci kontenera. |
| `updateItemsPositions()` | Aktualizuje pozycje wszystkich przedmiot�w w kontenerze, aby odzwierciedlaly ich sloty. |
# # # Zaleznosci i powiazania
- **`item.h`**: Zarzadza obiektami typu `Item`.
- **`framework/luaengine/luaobject.h`**: Dziedziczy po `LuaObject`, aby umozliwic interakcje z Lua.

---
# ?? creature.cpp
# # Og�lny opis
Implementacja klasy `Creature`, kt�ra jest podstawowa klasa dla wszystkich zywych istot w grze (graczy, potwor�w, NPC). Plik ten zawiera zlozona logike rysowania, animacji, poruszania sie, skakania oraz wyswietlania informacji o postaci.
# # Klasa `Creature`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Gl�wna funkcja rysujaca. Renderuje postac, jej ubi�r, kwadraty oznaczajace (np. cel ataku), a takze dodaje swiatlo do `LightView`. |
| `drawOutfit(...)` | Rysuje sam ubi�r postaci w zadanym prostokacie, uzywane gl�wnie w interfejsie uzytkownika. |
| `drawInformation(...)` | Rysuje pasek zycia, many, nazwe, ikony (czaszka, tarcza) nad postacia. |
| `turn(Otc::Direction direction)` | Zmienia kierunek, w kt�rym zwr�cona jest postac. |
| `walk(const Position& oldPos, const Position& newPos)` | Inicjuje proces chodzenia z `oldPos` do `newPos`, ustawiajac kierunek, timery i rozpoczynajac aktualizacje animacji. |
| `stopWalk()` | Natychmiastowo przerywa proces chodzenia. |
| `jump(int height, int duration)` | Rozpoczyna animacje skoku postaci. |
| `updateJump()` | Aktualizuje wysokosc skoku w kazdej klatce animacji. |
| `onAppear()` | Obsluguje pojawienie sie postaci na ekranie. Decyduje, czy postac przyszla, teleportowala sie, czy tylko sie obr�cila. |
| `onDisappear()` | Obsluguje znikniecie postaci z ekranu, planujac jej ostateczne usuniecie. |
| `onDeath()` | Wywoluje callback Lua `onDeath`. |
| `updateWalkAnimation(...)` | Aktualizuje faze animacji chodzenia na podstawie czasu i przebytych pikseli. |
| `updateWalkOffset(...)` | Oblicza przesuniecie postaci podczas chodzenia. |
| `updateWalkingTile()` | Aktualizuje, na kt�rym polu (`Tile`) postac jest obecnie rysowana podczas animacji chodzenia. |
| `nextWalkUpdate()` | Planuje nastepna aktualizacje stanu chodzenia. |
| `updateWalk()` | Gl�wna funkcja aktualizujaca stan chodzenia, wywolywana cyklicznie. |
| `terminateWalk()` | Konczy proces chodzenia, resetujac wszystkie zwiazane z nim zmienne. |
| `setHealthPercent(uint8 healthPercent)` | Ustawia procent zycia i aktualizuje kolor paska zycia. |
| `setOutfit(const Outfit& outfit)` | Zmienia ubi�r postaci. |
| `setSpeed(uint16 speed)` | Ustawia predkosc poruszania sie postaci. |
| `getStepDuration(...)` | Oblicza czas trwania jednego kroku w milisekundach na podstawie predkosci postaci, predkosci podloza i formul predkosci serwera. |
| `getDisplacement()` | Zwraca przesuniecie rysowania postaci, kt�re centruje ja na polu. |
| `addTopWidget(...)` / `addBottomWidget(...)` | Dodaje widzety, kt�re beda rysowane nad lub pod postacia. |
# # # Zmienne statyczne
- `m_speedFormula`: Tablica przechowujaca wsp�lczynniki do zaawansowanego obliczania predkosci.
# # # Zaleznosci i powiazania
- **`localplayer.h`**: Logika rysowania informacji o pasku many jest specyficzna dla lokalnego gracza.
- **`map.h`**, **`tile.h`**: Interakcje ze swiatem gry (pobieranie p�l, predkosci podloza).
- **`game.h`**: Dostep do globalnych ustawien gry i funkcji serwera.
- **`lightview.h`**: Dodawanie dynamicznego swiatla emitowanego przez postac.
- **`healthbars.h`**: Uzywa `g_healthBars` do pobierania niestandardowych tel dla pask�w zycia/many.
- **`spritemanager.h`**: Uzywa `g_sprites` do pobierania rozmiaru sprite'�w.

---
# ?? container.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Container`. Definiuje interfejs do zarzadzania pojemnikami w grze.
# # Klasa `Container`
# # # Opis
Klasa `Container` dziedziczy po `LuaObject`, co pozwala na jej uzycie w skryptach Lua. Reprezentuje obiekt w grze, kt�ry moze przechowywac inne przedmioty, jak plecak czy skrzynka.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `getItem(int slot)` | Zwraca wskaznik do przedmiotu w danym slocie. |
| `getItems()` | Zwraca kolekcje (`std::deque`) wszystkich przedmiot�w w kontenerze. |
| `getItemsCount()` | Zwraca liczbe przedmiot�w w kontenerze. |
| `getSlotPosition(int slot)` | Zwraca specjalnie zakodowana pozycje, kt�ra identyfikuje slot w tym kontenerze. |
| `getId()` | Zwraca ID kontenera. |
| `getCapacity()` | Zwraca pojemnosc kontenera. |
| `getContainerItem()` | Zwraca przedmiot, kt�ry reprezentuje ten kontener. |
| `getName()` | Zwraca nazwe kontenera. |
| `hasParent()` | Zwraca `true`, jesli kontener znajduje sie w innym kontenerze. |
| `isClosed()` | Zwraca `true`, jesli kontener zostal zamkniety. |
| `isUnlocked()` | Zwraca `true`, jesli mozna przesuwac w nim przedmioty. |
| `hasPages()` | Zwraca `true`, jesli kontener obsluguje paginacje. |
| `getSize()` | Zwraca calkowita liczbe przedmiot�w w kontenerze (moze byc wieksza niz pojemnosc, jesli ma strony). |
| `getFirstIndex()` | Zwraca indeks pierwszego przedmiotu na biezacej stronie. |
| `findItemById(uint itemId, int subType)` | Wyszukuje przedmiot po ID i opcjonalnym podtypie. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w, np. `ItemPtr`.
- **`item.h`**: Przechowuje obiekty `Item`.
- **`game.h`**: Klasa `Game` jest przyjacielem, co pozwala jej wywolywac chronione metody `onOpen`, `onClose`, etc.

---
# ?? creature.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Creature` oraz jej specjalizacji: `Npc` i `Monster`. Definiuje interfejs dla wszystkich istot w grze.
# # Klasa `Creature`
# # # Opis
Klasa bazowa dla wszystkich postaci w grze. Dziedziczy po `Thing`. Zawiera logike zwiazana z wygladem, ruchem, stanami i interakcjami.
# # # Typy wyliczeniowe
- **`enum` (anonimowy)**: Definiuje stale `SHIELD_BLINK_TICKS` i `VOLATILE_SQUARE_DURATION`.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje postac w danym miejscu na mapie. |
| `drawOutfit(...)` | Rysuje sam ubi�r postaci, uzywane w UI. |
| `drawInformation(...)` | Rysuje informacje nad postacia (nazwa, paski zycia/many, ikony). |
| `setId(uint32 id)` | Ustawia ID postaci. |
| `setName(const std::string& name)` | Ustawia nazwe postaci. |
| `setHealthPercent(uint8 healthPercent)` | Ustawia procent zycia. |
| `setDirection(Otc::Direction direction)` | Ustawia kierunek, w kt�rym postac jest zwr�cona. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubi�r postaci. |
| `setSpeed(uint16 speed)` | Ustawia predkosc poruszania sie. |
| `addTimedSquare(uint8 color)` | Wyswietla tymczasowy kolorowy kwadrat pod postacia. |
| `getStepDuration(...)` | Zwraca czas trwania jednego kroku. |
| `walk(const Position& oldPos, const Position& newPos)` | Inicjuje ruch postaci. |
| `stopWalk()` | Przerywa ruch postaci. |
| `isWalking()` | Zwraca `true`, jesli postac jest w trakcie chodu. |
| `isDead()` | Zwraca `true`, jesli postac ma 0% zycia. |
| `getThingType()` | Zwraca `ThingType` dla aktualnego ubioru postaci. |
| `addTopWidget(...)`, `addBottomWidget(...)` | Dodaje widzety do rysowania nad/pod postacia. |
# # Klasa `Npc`
# # # Opis
Specjalizacja `Creature` dla postaci niezaleznych (NPC).
# # Klasa `Monster`
# # # Opis
Specjalizacja `Creature` dla potwor�w.
# # # Zaleznosci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`outfit.h`**: Uzywa `Outfit` do zarzadzania wygladem.
- **`tile.h`**: Interakcje z polami mapy.
- **`mapview.h`**: Uzywana do rysowania w kontekscie widoku mapy.
- **`framework/ui/uiwidget.h`**: Dolaczanie widzet�w do postaci.

---
# ?? creatures.h
# # Og�lny opis
Plik nagl�wkowy definiujacy klasy do zarzadzania typami stworzen (`CreatureType`) oraz ich miejscami odradzania (`Spawn`). Jest to czesc systemu, kt�ry prawdopodobnie sluzy do edycji map lub dzialania jako serwer, a nie tylko do gry.
# # Typy wyliczeniowe
- **`CreatureAttr`**: Atrybuty typu stworzenia (pozycja, nazwa, ubi�r, etc.).
- **`CreatureRace`**: Rasa stworzenia (NPC, potw�r).
- **`SpawnAttr`**: Atrybuty spawnu (promien, srodek).
# # Klasa `Spawn`
# # # Opis
Reprezentuje obszar odradzania sie stworzen (spawn). Przechowuje informacje o srodku, promieniu oraz liste potwor�w/NPC, kt�re sie w nim pojawiaja.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setRadius(int32 r)` | Ustawia promien spawnu. |
| `getRadius()` | Zwraca promien spawnu. |
| `setCenterPos(const Position& pos)` | Ustawia centralna pozycje spawnu. |
| `getCenterPos()` | Zwraca centralna pozycje spawnu. |
| `getCreatures()` | Zwraca liste typ�w stworzen w tym spawnie. |
| `addCreature(const Position& placePos, const CreatureTypePtr& cType)` | Dodaje stworzenie do spawnu w okreslonym miejscu. |
| `removeCreature(const Position& pos)` | Usuwa stworzenie z danej pozycji. |
| `clear()` | Czysci liste stworzen. |
# # Klasa `CreatureType`
# # # Opis
Reprezentuje szablon (typ) stworzenia. Przechowuje domyslne wlasciwosci, takie jak nazwa, ubi�r czy kierunek, kt�re sa uzywane do tworzenia instancji `Creature`.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setSpawnTime(int32 spawnTime)` | Ustawia czas odradzania. |
| `getSpawnTime()` | Zwraca czas odradzania. |
| `setName(const std::string& name)` | Ustawia nazwe typu. |
| `getName()` | Zwraca nazwe. |
| `setOutfit(const Outfit& o)` | Ustawia domyslny ubi�r. |
| `getOutfit()` | Zwraca domyslny ubi�r. |
| `cast()` | Tworzy i zwraca instancje `Creature` na podstawie tego typu. |
# # Klasa `CreatureManager`
# # # Opis
Singleton (`g_creatures`) zarzadzajacy wszystkimi typami stworzen i spawnami. Wczytuje te dane z plik�w XML.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `loadMonsters(const std::string& file)` | Wczytuje dane o potworach z pliku. |
| `loadNpcs(const std::string& folder)` | Wczytuje dane o NPC z folderu. |
| `loadSpawns(const std::string& fileName)` | Wczytuje dane o spawnach. |
| `saveSpawns(const std::string& fileName)` | Zapisuje dane o spawnach. |
| `getCreatureByName(std::string name)` | Zwraca typ stworzenia po nazwie. |
| `getSpawn(const Position& centerPos)` | Zwraca spawn na podstawie jego centralnej pozycji. |
| `addSpawn(...)` | Dodaje nowy spawn. |
# # # Zmienne globalne
- `CreatureManager g_creatures`: Globalna instancja managera stworzen.
# # # Zaleznosci i powiazania
- **`declarations.h`**, **`outfit.h`**: Definicje typ�w.
- **`creature.h`**: `CreatureType::cast()` tworzy obiekty `Creature`.

---
# ?? declarations.h
# # Og�lny opis
Plik nagl�wkowy zawierajacy deklaracje wyprzedzajace (forward declarations) oraz definicje typ�w wskaznik�w i kolekcji uzywanych w calym module klienta. Jego gl�wnym celem jest przelamanie cyklicznych zaleznosci miedzy plikami nagl�wkowymi.
# # Zawartosc
# # # Deklaracje wyprzedzajace
Plik deklaruje istnienie klas bez koniecznosci dolaczania ich pelnych definicji. Obejmuje to klasy z r�znych modul�w:
- **Core**: `Map`, `Game`, `Tile`, `Thing`, `Item`, `Creature`, `LocalPlayer`, `Effect`, `House`, `Town` itp.
- **Net**: `ProtocolLogin`, `ProtocolGame`.
- **UI**: `UIItem`, `UICreature`, `UIMap`, `UIMinimap` itp.
- **Custom**: `HealthBar`.
# # # Definicje typ�w (`typedef`)
Definiuje inteligentne wskazniki (`shared_object_ptr`) dla wiekszosci zadeklarowanych klas, np.:
- `MapViewPtr`
- `TilePtr`
- `ThingPtr`
- `ItemPtr`
- `CreaturePtr`
- `LocalPlayerPtr`
# # # Definicje kolekcji (`typedef`)
Definiuje standardowe typy kolekcji dla zadeklarowanych obiekt�w, ulatwiajac ich uzycie w kodzie:
- `ThingList` (`std::vector<ThingPtr>`)
- `HouseList` (`std::list<HousePtr>`)
- `TileMap` (`std::unordered_map<Position, TilePtr, PositionHasher>`)
# # # Zaleznosci i powiazania
- **`global.h`**: Dolacza podstawowe definicje.
- Plik ten jest dolaczany przez niemal wszystkie inne pliki nagl�wkowe w module, aby zapewnic dostep do definicji typ�w wskaznik�w i uniknac problem�w z zaleznosciami.

---
# ?? creatures.cpp
# # Og�lny opis
Implementacja `CreatureManager` i `Spawn`, odpowiedzialnych za zarzadzanie typami stworzen i ich miejscami odradzania. Plik zawiera logike wczytywania i zapisywania danych z plik�w XML oraz zarzadzania stworzeniami na mapie.
# # Funkcje pomocnicze
- **`isInZone(...)`**: Sprawdza, czy dana pozycja znajduje sie w promieniu spawnu.
# # Klasa `Spawn`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `load(TiXmlElement* node)` | Wczytuje dane spawnu z wezla XML, w tym pozycje centralna, promien oraz liste stworzen z ich atrybutami. |
| `save(TiXmlElement* node)` | Zapisuje dane spawnu do wezla XML. |
| `addCreature(...)` | Dodaje stworzenie do spawnu. Najpierw tworzy instancje `Creature` na podstawie `CreatureType` za pomoca `cast()`, a nastepnie dodaje ja na mape (`g_map.addThing`). |
| `removeCreature(...)` | Usuwa stworzenie ze spawnu i z mapy. |
| `getCreatures()` | Zwraca liste wszystkich typ�w stworzen w tym spawnie. |
# # Klasa `CreatureType`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `cast()` | Tworzy nowa instancje `Creature`, ustawia jej nazwe, kierunek i ubi�r na podstawie danych z `CreatureType`, a nastepnie zwraca ja jako `CreaturePtr`. |
# # Klasa `CreatureManager`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `terminate()` | Czysci wszystkie dane managera. |
| `loadMonsters(const std::string& file)` | Wczytuje gl�wny plik XML z potworami, kt�ry zawiera odnosniki do pojedynczych plik�w XML dla kazdego potwora. |
| `loadSingleCreature(const std::string& file)` | Wczytuje dane pojedynczego stworzenia z pliku XML. |
| `loadNpcs(const std::string& folder)` | Wczytuje wszystkie pliki XML z danego folderu jako definicje NPC. |
| `loadSpawns(const std::string& fileName)` | Wczytuje plik XML ze spawnami i umieszcza stworzenia na mapie. |
| `saveSpawns(const std::string& fileName)` | Zapisuje aktualny stan spawn�w do pliku XML. |
| `internalLoadCreatureBuffer(...)` | Parsuje bufor XML z definicja stworzenia, tworzy obiekt `CreatureType` i dodaje go do listy. |
| `getCreatureByName(std::string name)` | Wyszukuje typ stworzenia po nazwie (z normalizacja wielkosci liter). |
| `getCreatureByLook(int look)` | Wyszukuje typ stworzenia po jego ID wygladu (outfit ID lub item ID). |
| `getSpawn(...)` / `getSpawnForPlacePos(...)` | Wyszukuje spawn na podstawie pozycji. |
| `addSpawn(...)` | Dodaje nowy spawn lub aktualizuje istniejacy. |
| `deleteSpawn(...)` | Usuwa spawn z managera. |
# # # Zaleznosci i powiazania
- **`map.h`**: Dodaje i usuwa stworzenia z mapy (`g_map`).
- **`creature.h`**: Tworzy instancje `Creature`.
- **`framework/xml/tinyxml.h`**: Uzywane do parsowania plik�w XML.
- **`framework/core/resourcemanager.h`**: Do odczytu plik�w z danymi.

---
# ?? effect.cpp
# # Og�lny opis
Implementacja klasy `Effect`, kt�ra odpowiada za renderowanie efekt�w wizualnych na mapie, takich jak eksplozje, efekty magiczne itp.
# # Klasa `Effect`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje efekt na ekranie. Oblicza aktualna faze animacji na podstawie czasu, kt�ry uplynal od pojawienia sie efektu. Jesli wlaczona jest funkcja `GameEnhancedAnimations`, uzywa `Animator::getPhaseAt` dla plynniejszej, niezaleznej animacji. |
| `onAppear()` | Metoda wywolywana, gdy efekt pojawia sie na mapie. Resetuje timer animacji i planuje automatyczne usuniecie efektu po zakonczeniu jego calkowitego czasu trwania. |
| `setId(uint32 id)` | Ustawia ID efektu, sprawdzajac jego poprawnosc w `g_things`. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla danego efektu. |
# # # Zaleznosci i powiazania
- **`map.h`**: Uzywa `g_map` do usuniecia efektu po zakonczeniu animacji.
- **`game.h`**: Sprawdza, czy wlaczona jest funkcja `GameEnhancedAnimations`.
- **`framework/core/eventdispatcher.h`**: Uzywa `g_dispatcher` do planowania usuniecia.

---
# ?? global.h
# # Og�lny opis
Plik nagl�wkowy, kt�ry pelni role centralnego punktu dolaczania najwazniejszych plik�w nagl�wkowych uzywanych w calym projekcie klienta.
# # Zawartosc
- **`#include <framework/global.h>`**: Dolacza globalne definicje z warstwy frameworka.
- **`#include "const.h"`**: Dolacza stale i typy wyliczeniowe specyficzne dla klienta gry.
- **`#include "position.h"`**: Dolacza definicje klasy `Position`.
# # # Cel
Celem tego pliku jest uproszczenie dolaczania nagl�wk�w w innych plikach. Zamiast dolaczac wiele podstawowych plik�w, wystarczy dolaczyc `global.h`.

---
# ?? effect.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Effect`, definiujacy jej interfejs.
# # Klasa `Effect`
# # # Opis
Klasa `Effect` dziedziczy po `Thing` i reprezentuje kr�tkotrwaly efekt wizualny na mapie.
# # # Stale
- **`EFFECT_TICKS_PER_FRAME`**: Domyslny czas trwania jednej klatki animacji efektu (75 ms).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje efekt w danym miejscu na mapie. |
| `setId(uint32 id)` | Ustawia ID (typ) efektu. |
| `getId()` | Zwraca ID efektu. |
| `asEffect()` | Rzutuje wskaznik na `EffectPtr`. |
| `isEffect()` | Zwraca `true`. |
| `getThingType()` | Zwraca `ThingType` dla tego efektu. |
# # # Zaleznosci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/core/timer.h`**: Uzywa `Timer` do sledzenia postepu animacji.

---
# ?? healthbars.cpp
# # Og�lny opis
Implementacja `HealthBars`, globalnego managera niestandardowych tel dla pask�w zycia i many. Umozliwia ladowanie i przypisywanie r�znych grafik do pask�w zdrowia w zaleznosci od ID ubioru postaci.
# # Klasa `HealthBars`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `init()` | Inicjalizuje wektory na paski zycia i many, rezerwujac miejsce i dodajac `nullptr` jako domyslny pasek (ID 0). |
| `terminate()` | Czysci wszystkie zaladowane tla pask�w. |
| `addHealthBackground(...)` | Dodaje nowe tlo dla paska zycia. Tworzy obiekt `HealthBar`, ustawia jego wlasciwosci (sciezka, tekstura, offsety, wysokosc) i dodaje go do wektora `m_healthBars`. |
| `addManaBackground(...)` | Dziala analogicznie do `addHealthBackground`, ale dla pask�w many. |
| `getHealthBarPath(int id)` | Zwraca sciezke do pliku graficznego dla paska zycia o danym ID. |
| `getManaBarPath(int id)` | Zwraca sciezke do pliku graficznego dla paska many o danym ID. |
| `getHealthBarOffset(int id)` | Zwraca przesuniecie tla dla paska zycia. |
| `getManaBarOffset(int id)` | Zwraca przesuniecie tla dla paska many. |
| `getHealthBarOffsetBar(int id)` | Zwraca przesuniecie samego paska (wypelnienia) wewnatrz tla. |
| `getManaBarOffsetBar(int id)` | Dziala analogicznie dla paska many. |
| `getHealthBarHeight(int id)` | Zwraca wysokosc paska zycia. |
| `getManaBarHeight(int id)` | Zwraca wysokosc paska many. |
# # Klasa `HealthBar`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setTexture(const std::string& path)` | Wczytuje teksture tla paska z podanej sciezki za pomoca `g_textures`. |
# # # Zmienne globalne
- `HealthBars g_healthBars`: Globalna instancja managera.
# # # Zaleznosci i powiazania
- **`framework/graphics/texturemanager.h`**: Uzywa `g_textures` do ladowania grafik.
- **`creature.cpp`**: Logika rysowania informacji o postaci (`drawInformation`) uzywa `g_healthBars` do pobierania niestandardowych tel pask�w.

---
# ?? game.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Game`, kt�ra jest centralnym punktem zarzadzania stanem gry. Definiuje interfejs do obslugi logowania, akcji gracza, komunikacji z serwerem oraz przechowywania stanu gry.
# # Klasa `Game`
# # # Opis
Singleton (`g_game`) pelniacy role fasady dla calej logiki gry. Zarzadza sesja gracza, protokolem sieciowym, stanem lokalnego gracza i interakcjami ze swiatem gry.
# # # Struktury
- **`UnjustifiedPoints`**: Przechowuje informacje o punktach za nieuzasadnione zab�jstwa w systemie PvP.
# # # Metody (Publiczne)
| Grupa | Metody | Opis |
| --- | --- | --- |
| **Zarzadzanie sesja** | `loginWorld`, `playRecord`, `cancelLogin`, `forceLogout`, `safeLogout` | Logowanie do swiata gry, odtwarzanie nagran, wylogowywanie. |
| **Akcje gracza** | `walk`, `autoWalk`, `turn`, `stop`, `look`, `move`, `use`, `useWith` | Wysylanie zadan akcji gracza do serwera. |
| **Kontenery** | `open`, `close`, `refreshContainer` | Zarzadzanie kontenerami. |
| **Walka** | `attack`, `follow`, `cancelAttackAndFollow` | Zarzadzanie atakiem i sledzeniem. |
| **Komunikacja** | `talk`, `talkChannel`, `talkPrivate` | Wysylanie wiadomosci. |
| **Zarzadzanie stanem** | `setProtocolVersion`, `setClientVersion`, `enableFeature`, `getFeature` | Konfiguracja klienta i obsluga funkcji serwera. |
| **Gettery** | `isOnline`, `isDead`, `getLocalPlayer`, `getProtocolGame`, `getPing` | Dostep do aktualnego stanu gry. |
# # # Metody (Chronione - Handlery Protokolu)
Plik definiuje r�wniez liczne metody `process...`, kt�re sa wywolywane przez `ProtocolGame` w odpowiedzi na otrzymane pakiety z serwera. Przyklady:
- `processLoginError`, `processEnterGame`
- `processTextMessage`, `processTalk`
- `processOpenContainer`, `processContainerAddItem`
- `processInventoryChange`
- `processWalkCancel`
# # # Zaleznosci i powiazania
- **`declarations.h`**: Uzywa wielu zadeklarowanych typ�w (`ItemPtr`, `CreaturePtr`, etc.).
- **`protocolgame.h`**: Scisle powiazana z protokolem sieciowym.
- **`localplayer.h`**: Zarzadza instancja `LocalPlayer`.
- **`container.h`**: Zarzadza kolekcja otwartych kontener�w.

---
# ?? healthbars.h
# # Og�lny opis
Plik nagl�wkowy definiujacy klasy `HealthBar` i `HealthBars` do zarzadzania niestandardowymi tlami pask�w zycia i many.
# # Klasa `HealthBar`
# # # Opis
Prosta klasa przechowujaca informacje o pojedynczym niestandardowym tle paska zdrowia lub many.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setPath(const std::string& path)` | Ustawia sciezke do pliku graficznego. |
| `getPath()` | Zwraca sciezke. |
| `setTexture(const std::string& path)` | Laduje teksture. |
| `getTexture()` | Zwraca wskaznik do tekstury. |
| `setOffset(int x, int y)` | Ustawia przesuniecie (offset) calego tla wzgledem punktu zaczepienia. |
| `getOffset()` | Zwraca przesuniecie. |
| `setBarOffset(int x, int y)` | Ustawia przesuniecie samego paska (wypelnienia) wewnatrz tla. |
| `getBarOffset()` | Zwraca przesuniecie paska. |
| `setHeight(int height)` | Ustawia wysokosc paska. |
| `getHeight()` | Zwraca wysokosc. |
# # Klasa `HealthBars`
# # # Opis
Singleton (`g_healthBars`) zarzadzajacy kolekcja obiekt�w `HealthBar`. Dziala jako repozytorium dla wszystkich niestandardowych tel pask�w.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `init()` | Inicjalizuje managera. |
| `terminate()` | Zwalnia zasoby. |
| `addHealthBackground(...)` | Dodaje nowe tlo dla paska zycia. |
| `addManaBackground(...)` | Dodaje nowe tlo dla paska many. |
| `getHealthBar(int id)` | Zwraca obiekt `HealthBar` dla paska zycia o danym ID. |
| `getManaBar(int id)` | Zwraca obiekt `HealthBar` dla paska many o danym ID. |
| `getHealthBarPath(int id)` | Zwraca sciezke do grafiki paska zycia. |
| `getManaBarPath(int id)` | Zwraca sciezke do grafiki paska many. |
| `...` | Gettery dla pozostalych wlasciwosci paska. |
# # # Zmienne globalne
- `HealthBars g_healthBars`: Deklaracja zewnetrznej instancji managera.
# # # Zaleznosci i powiazania
- **`declarations.h`**: Podstawowe definicje.
- **`framework/graphics/declarations.h`**: Deklaracje typ�w graficznych, np. `TexturePtr`.

---
# ?? houses.cpp
# # Og�lny opis
Implementacja klas `House` i `HouseManager`, kt�re zarzadzaja danymi o domach w grze. Plik zawiera logike wczytywania i zapisywania danych o domach z/do plik�w XML oraz zarzadzania ich stanem.
# # Klasa `House`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setTile(const TilePtr& tile)` | Dodaje pole do domu, ustawiajac na nim flage `TILESTATE_HOUSE` i ID domu. |
| `getTile(const Position& position)` | Zwraca pole na podanej pozycji, jesli nalezy ono do domu. |
| `addDoor(const ItemPtr& door)` | Dodaje drzwi do domu, przypisujac im unikalne, inkrementowane ID. |
| `removeDoorById(uint32 doorId)` | Usuwa drzwi o podanym ID (ustawia wskaznik na `nullptr` w wektorze). |
| `load(const TiXmlElement *elem)` | Wczytuje atrybuty domu (nazwa, czynsz, rozmiar, ID miasta, pozycja wejscia) z wezla XML. |
| `save(TiXmlElement* elem)` | Zapisuje atrybuty domu do wezla XML. |
# # Klasa `HouseManager`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `addHouse(const HousePtr& house)` | Dodaje dom do listy, jesli jeszcze nie istnieje. |
| `removeHouse(uint32 houseId)` | Usuwa dom o podanym ID. |
| `getHouse(uint32 houseId)` | Wyszukuje i zwraca dom po jego ID. |
| `getHouseByName(std::string name)` | Wyszukuje i zwraca dom po jego nazwie. |
| `load(const std::string& fileName)` | Wczytuje liste dom�w z pliku XML. Dla kazdego domu w pliku, jesli juz istnieje w menedzerze, aktualizuje jego dane; w przeciwnym razie tworzy nowy. |
| `save(const std::string& fileName)` | Zapisuje liste wszystkich dom�w do pliku XML. |
| `filterHouses(uint32 townId)` | Zwraca liste dom�w nalezacych do miasta o podanym ID. |
| `findHouse(uint32 houseId)` | Wewnetrzna metoda do wyszukiwania iteratora do domu na liscie. |
| `sort()` | Sortuje liste dom�w alfabetycznie wedlug nazwy. |
# # # Zmienne globalne
- `HouseManager g_houses`: Globalna instancja managera dom�w.
# # # Zaleznosci i powiazania
- **`map.h`**: Interakcje z obiektami `Tile` (`tile->setFlag(...)`).
- **`framework/core/resourcemanager.h`**: Do odczytu plik�w XML z danymi dom�w.

---
# ?? item.cpp
# # Og�lny opis
Implementacja klasy `Item`, kt�ra reprezentuje przedmioty w grze. Plik zawiera logike rysowania przedmiot�w, obsluge ich atrybut�w oraz serializacje/deserializacje do formatu binarnego (OTBM).
# # Klasa `Item`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `create(int id, int countOrSubtype)` | Statyczna metoda fabryczna do tworzenia przedmiotu na podstawie jego ID klienta. |
| `createFromOtb(int id)` | Statyczna metoda fabryczna do tworzenia przedmiotu na podstawie jego ID serwera (z plik�w OTB). |
| `getName()` | Zwraca nazwe przedmiotu na podstawie jego typu. |
| `draw(...)` | Rysuje przedmiot na ekranie. Oblicza faze animacji oraz wz�r (pattern) na podstawie jego wlasciwosci (np. liczba przedmiot�w w stosie, typ plynu). |
| `setId(uint32 id)` / `setOtbId(uint16 id)` | Ustawia ID przedmiotu, odpowiednio konwertujac miedzy ID klienta a serwera. |
| `unserializeItem(const BinaryTreePtr &in)` | Wczytuje atrybuty przedmiotu z binarnego drzewa (format OTBM). |
| `serializeItem(const OutputBinaryTreePtr& out)` | Zapisuje atrybuty przedmiotu do binarnego drzewa. |
| `getSubType()` | Zwraca podtyp przedmiotu (np. typ plynu). |
| `getCount()` | Zwraca liczbe przedmiot�w w stosie (jesli jest stackable). |
| `clone()` | Tworzy i zwraca gleboka kopie przedmiotu. |
| `calculatePatterns(...)` | Oblicza, kt�ry wz�r (pattern) sprite'a powinien byc uzyty, w zaleznosci od typu przedmiotu (stackable, hangable, fluid container). |
| `calculateAnimationPhase(bool animate)` | Oblicza biezaca klatke animacji. Obsluguje animacje synchroniczne i asynchroniczne. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla tego przedmiotu. |
# # # Zaleznosci i powiazania
- **`thingtypemanager.h`**: Uzywa `g_things` do uzyskiwania informacji o typach przedmiot�w.
- **`spritemanager.h`**: Uzywa `g_sprites` do pobierania danych o sprite'ach.
- **`game.h`**: Uzywa `g_game` do sprawdzania funkcji serwera (np. `GameNewFluids`).
- **`tile.h`**: Interakcje z polem, na kt�rym lezy przedmiot (np. do okreslenia, jak zawiesic przedmiot).

---
# ?? itemtype.cpp
# # Og�lny opis
Implementacja klasy `ItemType`, kt�ra reprezentuje szablon (typ) przedmiotu. Plik zawiera logike wczytywania definicji typ�w przedmiot�w z binarnego formatu OTB.
# # Klasa `ItemType`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(const BinaryTreePtr& node)` | Deserializuje dane typu przedmiotu z wezla binarnego drzewa. Odczytuje kategorie przedmiotu oraz liste jego atrybut�w, takich jak ID serwera, ID klienta, nazwa, czy jest zapisywalny itp. Obsluguje r�znice w formacie w zaleznosci od wersji klienta. |
# # # Logika serializacji
Metoda `unserialize` zawiera logike dostosowujaca wczytywanie atrybut�w do r�znych wersji klienta Tibii. Na przyklad, dla starszych wersji klienta, ID serwera musi byc dostosowane, aby poprawnie mapowac przedmioty.

> NOTE: Statyczna zmienna `lastId` jest uzywana do tworzenia "pustych" typ�w przedmiot�w, jesli w pliku OTB wystepuja luki w numeracji ID serwera. Jest to mechanizm zapewniajacy sp�jnosc indeksowania.
# # # Zaleznosci i powiazania
- **`thingtypemanager.h`**: Jest scisle powiazana z `ThingTypeManager`, kt�ry zarzadza wszystkimi typami przedmiot�w i wywoluje `unserialize`.
- **`game.h`**: Uzywa `g_game` do sprawdzania wersji klienta, co wplywa na logike parsowania.
- **`framework/core/binarytree.h`**: Uzywa `BinaryTree` do odczytu danych z formatu OTB.

---
# ?? item.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Item`, kt�ra reprezentuje konkretny przedmiot w grze.
# # Klasa `Item`
# # # Opis
Dziedziczy po `Thing`. Reprezentuje instancje przedmiotu, kt�ra moze znajdowac sie na mapie, w kontenerze lub w ekwipunku gracza. Posiada wlasciwosci takie jak ID, liczba/podtyp, kolor, a takze moze zawierac inne przedmioty, jesli jest kontenerem.
# # # Typy wyliczeniowe
- **`ItemAttr`**: Definiuje klucze atrybut�w, kt�re moga byc przypisane do przedmiotu (np. `ATTR_COUNT`, `ATTR_ACTION_ID`, `ATTR_TEXT`).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `create(int id, ...)` | Statyczna metoda fabryczna do tworzenia przedmiotu po ID klienta. |
| `createFromOtb(int id)` | Statyczna metoda fabryczna do tworzenia przedmiotu po ID serwera (OTB). |
| `draw(...)` | Rysuje przedmiot na ekranie. |
| `setId(uint32 id)` | Ustawia ID klienta przedmiotu. |
| `setOtbId(uint16 id)` | Ustawia ID serwera (OTB) przedmiotu. |
| `setCountOrSubType(int value)` | Ustawia liczbe (dla przedmiot�w stackowalnych) lub podtyp (dla plyn�w, etc.). |
| `getCount()` | Zwraca liczbe przedmiot�w. |
| `getSubType()` | Zwraca podtyp przedmiotu. |
| `getServerId()` | Zwraca ID serwera. |
| `unserializeItem(...)` | Wczytuje atrybuty przedmiotu z formatu binarnego. |
| `serializeItem(...)` | Zapisuje atrybuty przedmiotu do formatu binarnego. |
| `isContainer()` | Zwraca `true`, jesli przedmiot jest kontenerem. |
| `clone()` | Tworzy gleboka kopie przedmiotu. |
| `getContainerItems()` | Zwraca liste przedmiot�w wewnatrz, jesli jest kontenerem. |
| `setCustomAttribute(...)` | Ustawia niestandardowy atrybut przedmiotu (funkcja dla serwer�w niestandardowych). |
# # # Zaleznosci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`itemtype.h`**: Kazdy `Item` jest instancja jakiegos `ItemType`.

---
# ?? itemtype.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `ItemType`, kt�ra reprezentuje szablon (typ) przedmiotu.
# # Klasa `ItemType`
# # # Opis
Przechowuje niezmienne wlasciwosci dla danego typu przedmiotu, wczytywane z plik�w OTB. Wszystkie instancje `Item` o tym samym ID dziela jeden obiekt `ItemType`.
# # # Typy wyliczeniowe
- **`ItemCategory`**: Kategorie przedmiot�w (bron, zbroja, pojemnik itp.).
- **`ItemTypeAttr`**: Atrybuty typu przedmiotu wczytywane z OTB.
- **`ClientVersion`**: Wersje klienta, uzywane do obslugi r�znic w formatach plik�w.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(const BinaryTreePtr& node)` | Wczytuje dane typu przedmiotu z binarnego formatu OTB. |
| `setServerId(uint16 serverId)` | Ustawia ID serwera. |
| `getServerId()` | Zwraca ID serwera. |
| `setClientId(uint16 clientId)` | Ustawia ID klienta. |
| `getClientId()` | Zwraca ID klienta. |
| `getCategory()` | Zwraca kategorie przedmiotu. |
| `getName()` | Zwraca nazwe przedmiotu. |
| `isWritable()` | Zwraca `true`, jesli na przedmiocie mozna pisac. |
# # # Zaleznosci i powiazania
- **`framework/luaengine/luaobject.h`**: Dziedziczy z `LuaObject`, aby byc dostepnym z Lua.
- **`framework/xml/tinyxml.h`**: Uzywane do parsowania dodatkowych danych z `items.xml`.

---
# ?? lightview.cpp
# # Og�lny opis
Implementacja klasy `LightView`, kt�ra zarzadza i renderuje dynamiczne oswietlenie na mapie.
# # Klasa `LightView`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `addLight(const Point& pos, uint8_t color, uint8_t intensity)` | Dodaje nowe zr�dlo swiatla do sceny. Jesli w tym samym miejscu istnieje juz swiatlo o tym samym kolorze, wybierana jest wieksza intensywnosc. |
| `setFieldBrightness(...)` | Ustawia jasnosc dla danego pola na mapie. Ta metoda nie jest w pelni zaimplementowana i jej rola wydaje sie ograniczona. |
| `draw()` | Gl�wna funkcja renderujaca. Przebiega przez wszystkie pola widoczne na ekranie i dla kazdego piksela oblicza finalny kolor swiatla, sumujac wplyw globalnego oswietlenia i wszystkich pobliskich zr�del swiatla. Wynik jest zapisywany do bufora, a nastepnie przesylany do tekstury (`m_lightTexture`), kt�ra jest rysowana na ekranie z trybem mieszania `CompositionMode_Multiply`, aby przyciemnic scene. |
# # # Logika renderowania
1.  Tworzony jest bufor pikseli o rozmiarze widocznego obszaru mapy.
2.  Kazdy piksel w buforze jest inicjalizowany globalnym swiatlem otoczenia.
3.  Dla kazdego piksela iteruje sie przez wszystkie zr�dla swiatla.
4.  Obliczana jest odleglosc piksela od zr�dla swiatla, a na jej podstawie intensywnosc swiatla w tym punkcie.
5.  Kolor swiatla jest mieszany z kolorem piksela w buforze (wybierany jest najjasniejszy kanal R, G, B).
6.  Po przetworzeniu wszystkich pikseli, bufor jest ladowany do tekstury.
7.  Tekstura swiatla jest rysowana na wierzchu sceny, przyciemniajac ja.
# # # Zaleznosci i powiazania
- **`spritemanager.h`**: Uzywa `g_sprites.spriteSize()` do obliczen zwiazanych z rozmiarami p�l.
- **`framework/graphics/painter.h`**: Uzywa `g_painter` do rysowania finalnej tekstury swiatla.

---
# ?? lightview.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `LightView`, kt�ra jest odpowiedzialna za system dynamicznego oswietlenia w grze.
# # Struktura `TileLight`
# # # Opis
Prosta struktura przechowujaca informacje o swietle dla pojedynczego pola mapy.
- `start`: Indeks poczatkowy w liscie swiatel, od kt�rego nalezy zaczac obliczenia dla tego pola.
- `color`: Kolor swiatla.
# # Klasa `LightView`
# # # Opis
Dziedziczy po `DrawQueueItem`, co oznacza, ze obiekty tej klasy moga byc dodawane do kolejki rysowania. `LightView` agreguje wszystkie zr�dla swiatla w widocznym obszarze i renderuje je do jednej tekstury, kt�ra nastepnie jest nakladana na scene.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `LightView(...)` | Konstruktor. Inicjalizuje widok swiatla z podanym rozmiarem, tekstura docelowa, globalnym kolorem i intensywnoscia swiatla. |
| `addLight(...)` | Dodaje zr�dlo swiatla w danej pozycji. |
| `setFieldBrightness(...)` | Ustawia jasnosc dla danego pola (obecnie nie w pelni wykorzystywane). |
| `size()` | Zwraca liczbe zr�del swiatla. |
| `draw()` | Metoda renderujaca, kt�ra wykonuje obliczenia oswietlenia i rysuje finalna teksture. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`thingtype.h`**: Uzywa struktury `Light` zdefiniowanej w `thingtype.h`.
- **`framework/graphics/drawqueue.h`**: Jest elementem kolejki rysowania.

---
# ?? localplayer.cpp
# # Og�lny opis
Implementacja klasy `LocalPlayer`, kt�ra reprezentuje postac sterowana przez gracza. Rozszerza klase `Player` o logike specyficzna dla lokalnego gracza, taka jak obsluga ruchu inicjowanego przez klienta (pre-walking), blokady chodzenia, auto-walking oraz zarzadzanie statystykami.
# # Klasa `LocalPlayer`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `lockWalk(int millis)` | Blokuje mozliwosc chodzenia na okreslony czas, np. po uzyciu przedmiotu. |
| `canWalk(Otc::Direction direction, ...)` | Sprawdza, czy gracz moze wykonac krok w danym kierunku. Uwzglednia blokady, paraliz, trwajacy ruch oraz limity "pre-walkingu". |
| `walk(const Position& oldPos, const Position& newPos)` | Obsluguje ruch potwierdzony przez serwer. Jesli ruch odpowiada wykonanemu "pre-walk", usuwa go z kolejki. Jesli nie, traktuje to jako ruch wymuszony przez serwer (np. odepchniecie). |
| `preWalk(Otc::Direction direction)` | Inicjuje "pre-walking" - ruch wykonywany przez klienta przed potwierdzeniem z serwera, aby zniwelowac op�znienie sieciowe. Dodaje nowa pozycje do kolejki `m_preWalking`. |
| `cancelNewWalk(Otc::Direction dir)` | Anuluje wszystkie ruchy "pre-walk" w odpowiedzi na pakiet "cancel walk" z serwera. Moze pr�bowac ponowic auto-walking. |
| `predictiveCancelWalk(...)` | Anuluje ruchy "pre-walk" na podstawie predykcji, jesli serwer odrzuci krok w polowie sciezki. |
| `autoWalk(Position destination, ...)` | Inicjuje automatyczne poruszanie sie do celu. Asynchronicznie wyszukuje sciezke i wysyla ja do serwera. |
| `stopAutoWalk()` | Przerywa auto-walking. |
| `stopWalk()` | Natychmiastowo zatrzymuje wszelki ruch, czyszczac kolejke "pre-walk". |
| `updateWalkOffset(...)` | Specjalna implementacja dla "pre-walk", gdzie offset jest liczony w przeciwnym kierunku niz normalny ruch. |
| `updateWalk()` | Aktualizuje stan chodzenia; konczy krok, gdy uplynie jego czas trwania. |
| `terminateWalk()` | Finalizuje krok, resetuje stan chodzenia i wywoluje callback `onWalkFinish`. |
| `onPositionChange(...)` | Obsluguje zmiane pozycji; jesli osiagnieto cel auto-walk, zatrzymuje go. |
| `set...(...)` | Szereg metod `set` (np. `setHealth`, `setSkill`, `setExperience`), kt�re aktualizuja stan lokalnego gracza i wywoluja odpowiednie callbacki Lua, informujac o zmianach. |
| `hasSight(const Position& pos)` | Sprawdza, czy dana pozycja jest w zasiegu wzroku gracza. |
# # # Zaleznosci i powiazania
- **`map.h`**, **`tile.h`**: Do sprawdzania, czy pola sa mozliwe do przejscia.
- **`game.h`**: Do komunikacji z serwerem i zatrzymywania akcji gry.
- **`framework/core/eventdispatcher.h`**: Do planowania ponownych pr�b auto-walkingu.

---
# ?? map.cpp
# # Og�lny opis
Implementacja klasy `Map`, kt�ra jest centralnym repozytorium dla wszystkich danych o swiecie gry. Plik zawiera logike zarzadzania polami (`Tile`), umieszczania na nich obiekt�w (`Thing`), wyszukiwania sciezek oraz zarzadzania widocznym obszarem mapy.
# # Klasa `Map`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizuje i zwalnia zasoby mapy. |
| `addMapView(...)` / `removeMapView(...)` | Dodaje i usuwa widoki mapy (`MapView`), kt�re beda renderowac dane. |
| `notificateTileUpdate(...)` | Powiadamia wszystkie `MapView` o aktualizacji danego pola, co powoduje jego przerysowanie. |
| `clean()` / `cleanDynamicThings()` | Czysci mape ze wszystkich p�l lub tylko z obiekt�w dynamicznych (stworzenia, efekty). |
| `addThing(...)` | Dodaje obiekt (`Thing`) na mape w danej pozycji. Obsluguje specjalne przypadki dla pocisk�w, animowanych i statycznych tekst�w (np. laczenie tekst�w o obrazeniach). |
| `getThing(...)` / `removeThing(...)` | Pobiera lub usuwa obiekt z mapy. |
| `getOrCreateTile(...)` | Zwraca istniejace pole lub tworzy nowe, jesli nie istnieje. |
| `getTiles(...)` | Zwraca liste wszystkich p�l na danym pietrze lub na calej mapie. |
| `cleanTile(...)` | Usuwa wszystkie obiekty z danego pola. |
| `setCentralPosition(...)` | Ustawia pozycje kamery, co powoduje usuniecie obiekt�w spoza nowego zasiegu widzenia. |
| `getSpectators(...)` | Zwraca liste stworzen w zasiegu widzenia. |
| `isAwareOfPosition(...)` | Sprawdza, czy dana pozycja jest w zasiegu widzenia kamery. |
| `findPath(...)` | Implementacja algorytmu wyszukiwania sciezki A*. |
| `newFindPath(...)` | Nowsza, asynchroniczna implementacja wyszukiwania sciezki. |
| `findPathAsync(...)` | Uruchamia `newFindPath` w osobnym watku. |
| `findEveryPath(...)` | Implementacja algorytmu Dijkstry do znalezienia wszystkich mozliwych sciezek w danym zasiegu. |
# # # Struktura danych
- **`m_tileBlocks`**: Pola mapy sa przechowywane w blokach 32x32, co optymalizuje zuzycie pamieci. `std::map<uint, TileBlock> m_tileBlocks[Otc::MAX_Z+1]` przechowuje te bloki dla kazdego pietra.
- **`m_knownCreatures`**: Mapa znanych stworzen, indeksowana po ich ID.
# # # Zaleznosci i powiazania
- **`game.h`**: Dostep do stanu gry, np. funkcji serwera (`GameFeature`).
- **`localplayer.h`**: Do centrowania kamery i aktualizacji pozycji gracza.
- **`tile.h`**: Zarzadza obiektami `Tile`.
- **`mapview.h`**: Powiadamia `MapView` o zmianach.
- **`minimap.h`**: Aktualizuje minimape przy zmianach na polach.

---
# ?? luavaluecasts_client.h
# # Og�lny opis
Plik nagl�wkowy definiujacy funkcje do konwersji (rzutowania) niestandardowych typ�w danych C++ na wartosci Lua i z powrotem. Jest to kluczowy element integracji logiki gry z silnikiem skryptowym Lua.
# # Funkcje
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
# # # Zaleznosci i powiazania
- **`global.h`**, **`game.h`**, **`outfit.h`**: Zawieraja definicje typ�w, kt�re sa konwertowane.
- **`framework/luaengine/declarations.h`**: Deklaracje funkcji z silnika Lua.
- **`luavaluecasts_client.cpp`**: Zawiera implementacje tych funkcji.

---
# ?? mapio.cpp
# # Og�lny opis
Plik ten zawiera implementacje metod klasy `Map` odpowiedzialnych za operacje wejscia/wyjscia, czyli wczytywanie i zapisywanie danych mapy w formatach OTBM (OpenTibia Binary Map) i OTCM (OTClient Map).
# # Klasa `Map`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `loadOtbm(const std::string& fileName)` | Wczytuje mape z pliku binarnego `.otbm`. Parsuje nagl�wek, sprawdza wersje i sygnature, a nastepnie iteruje przez wezly binarnego drzewa, tworzac pola (`Tile`), przedmioty (`Item`) oraz wczytujac informacje o miastach, domach i punktach nawigacyjnych (waypoints). |
| `saveOtbm(const std::string& fileName)` | Zapisuje aktualny stan mapy do pliku `.otbm`. Tworzy strukture binarnego drzewa, zapisuje nagl�wek, a nastepnie serializuje wszystkie pola, przedmioty na nich, a takze informacje o miastach, domach i waypointach. |
| `loadOtcm(const std::string& fileName)` | Wczytuje mape z wlasnego, prostszego formatu klienta (`.otcm`). Format ten jest mniej rozbudowany niz OTBM i przechowuje gl�wnie informacje o polach i przedmiotach. |
| `saveOtcm(const std::string& fileName)` | Zapisuje mape do formatu `.otcm`. |
# # # Logika wczytywania OTBM
1.  Otwiera plik i weryfikuje jego sygnature (`OTBM`).
2.  Odczytuje nagl�wek, zawierajacy wymiary mapy i wersje OTB.
3.  Parsuje gl�wny wezel danych, odczytujac atrybuty takie jak opis mapy oraz sciezki do plik�w z danymi o spawnach i domach.
4.  Iteruje przez wezly `OTBM_TILE_AREA`, kt�re grupuja pola w blokach.
5.  Dla kazdego pola (`OTBM_TILE`) odczytuje jego atrybuty (flagi, przedmioty). Przedmioty, kt�re sa kontenerami, sa parsowane rekurencyjnie.
6.  Wczytuje definicje miast (`OTBM_TOWNS`) i waypoint�w (`OTBM_WAYPOINTS`).
# # # Zaleznosci i powiazania
- **`tile.h`**, **`item.h`**: Tworzy obiekty `Tile` i `Item` na podstawie wczytanych danych.
- **`game.h`**: Uzywa `g_game` do sprawdzania funkcji serwera, kt�re moga wplywac na spos�b parsowania.
- **`houses.h`**, **`towns.h`**: Wypelnia menedzery `g_houses` i `g_towns` danymi z mapy.
- **`framework/core/filestream.h`**, **`framework/core/binarytree.h`**: Narzedzia do obslugi plik�w binarnych i struktury drzewa binarnego.

---
# ?? luavaluecasts_client.cpp
# # Og�lny opis
Implementacja funkcji do konwersji (rzutowania) niestandardowych typ�w danych C++ na wartosci Lua i z powrotem. Ten plik zawiera logike "tlumaczenia" zlozonych obiekt�w C++ na tabele Lua i odwrotnie.
# # Funkcje
# # # `push_luavalue`
Te funkcje przyjmuja jako argument obiekt C++ i umieszczaja jego reprezentacje w Lua na stosie. Zlozone obiekty sa zazwyczaj konwertowane na tabele Lua.
- **`push_luavalue(const Outfit& outfit)`**: Tworzy tabele Lua z polami `type`, `auxType`, `head`, `body`, `legs`, `feet`, `addons`, `mount` etc. i wypelnia ja danymi z obiektu `Outfit`.
- **`push_luavalue(const Position& pos)`**: Tworzy tabele `{x, y, z}`.
- **`push_luavalue(const MarketData& data)`**: Tworzy tabele z danymi rynkowymi.
- **`push_luavalue(const Imbuement& i)`**: Tworzy zlozona, zagniezdzona tabele reprezentujaca imbuement, wlaczajac w to liste material�w.
# # # `luavalue_cast`
Te funkcje przyjmuja jako argument indeks na stosie Lua i referencje do obiektu C++. Odczytuja wartosc ze stosu (zwykle tabele) i wypelniaja obiekt C++ odpowiednimi danymi.
- **`luavalue_cast(int index, Outfit& outfit)`**: Odczytuje pola z tabeli Lua i ustawia odpowiednie wlasciwosci w obiekcie `Outfit`.
- **`luavalue_cast(int index, Position& pos)`**: Odczytuje pola `x`, `y`, `z` z tabeli.
- **`luavalue_cast(int index, MarketData& data)`**: Wypelnia strukture `MarketData`.
# # # Zaleznosci i powiazania
- **`framework/luaengine/luainterface.h`**: Dostep do funkcji `g_lua` do manipulacji stosem Lua.
- **`game.h`**: Uzywa `g_game` do sprawdzania, kt�re `GameFeature` sa aktywne, co wplywa na to, kt�re pola obiektu `Outfit` sa serializowane/deserializowane (np. `GamePlayerMounts`).
- **`luavaluecasts_client.h`**: Deklaracje tych funkcji.

---
# ?? mapview.cpp
# # Og�lny opis
Implementacja klasy `MapView`, kt�ra jest odpowiedzialna za renderowanie widoku mapy. Plik zawiera skomplikowana logike okreslania, kt�re pola sa widoczne, jak je rysowac w odpowiedniej kolejnosci (z uwzglednieniem pieter i efektu paralaksy) oraz jak zarzadzac oswietleniem i tekstami na mapie.
# # Klasa `MapView`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawMapBackground(...)` | Gl�wna funkcja rysujaca tlo mapy. Przygotowuje bufor ramki (`FrameBuffer`), inicjalizuje `LightView` (jesli oswietlenie jest wlaczone) i rysuje wszystkie widoczne pietra, zaczynajac od najnizszego. |
| `drawFloor(...)` | Rysuje pojedyncze pietro. Iteruje po `m_cachedVisibleTiles` i wywoluje metody `drawGround`, `drawBottom`, `drawCreatures` i `drawTop` dla kazdego pola (`Tile`). |
| `drawMapForeground(...)` | Rysuje elementy pierwszego planu, takie jak paski zdrowia, nazwy postaci, teksty (statyczne i animowane) oraz ostatecznie naklada warstwe oswietlenia. |
| `updateVisibleTilesCache()` | Kluczowa metoda optymalizacyjna. Oblicza, kt�re pola sa widoczne dla kamery, i zapisuje je w pamieci podrecznej (`m_cachedVisibleTiles`). Sortuje je w kolejnosci rysowania (diagonalnie), aby zachowac poprawna perspektywe 2.5D. |
| `updateGeometry(...)` | Aktualizuje geometrie widoku, w tym wymiary widoczne i wymiary bufora ramki. |
| `onTileUpdate(...)` / `onMapCenterChange(...)` | Metody wywolywane przez `g_map`, kt�re oznaczaja, ze pamiec podreczna widocznych p�l musi zostac zaktualizowana. |
| `calcFirstVisibleFloor(...)` / `calcLastVisibleFloor(...)` | Oblicza, kt�re pietra sa widoczne dla gracza na podstawie jego pozycji i otoczenia (np. dziury w podlodze, okna). |
| `transformPositionTo2D(...)` | Konwertuje pozycje 3D (x, y, z) na wsp�lrzedne 2D na ekranie, uwzgledniajac perspektywe izometryczna. |
| `getCameraPosition()` | Zwraca aktualna pozycje kamery, kt�ra albo podaza za stworzeniem (`m_followingCreature`), albo jest ustawiona recznie. |
# # # Zaleznosci i powiazania
- **`map.h`**, **`tile.h`**: Intensywnie korzysta z `g_map` do pobierania danych o polach i obiektach.
- **`game.h`**: Dostep do `g_game` w celu pobrania lokalnego gracza i sprawdzenia funkcji serwera.
- **`lightview.h`**: Tworzy i zarzadza obiektem `LightView` do renderowania oswietlenia.
- **`framework/graphics/framebuffermanager.h`**: Uzywa bufor�w ramki do optymalizacji renderowania.

---
# ?? mapview.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `MapView`. Definiuje interfejs widoku mapy, kt�ry jest gl�wnym komponentem renderujacym swiat gry.
# # Klasa `MapView`
# # # Opis
Klasa `MapView` zarzadza kamera, widocznym obszarem mapy, a takze koordynuje proces rysowania wszystkich element�w swiata gry. Moze istniec wiele instancji `MapView`, co pozwala na renderowanie mapy w r�znych miejscach interfejsu.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawMapBackground(...)` | Rysuje tlo mapy (pola, obiekty na ziemi). |
| `drawMapForeground(...)` | Rysuje pierwszy plan (postacie, teksty, oswietlenie). |
| `lockFirstVisibleFloor(int floor)` | Wymusza, aby najnizszym widocznym pietrem bylo podane pietro. |
| `unlockFirstVisibleFloor()` | Wylacza wymuszone pietro. |
| `setVisibleDimension(const Size& dim)` | Ustawia wymiary widocznego obszaru w jednostkach p�l (np. 15x11). |
| `followCreature(const CreaturePtr& creature)` | Ustawia kamere, aby podazala za danym stworzeniem. |
| `setCameraPosition(const Position& pos)` | Ustawia kamere na stala pozycje. |
| `getCameraPosition()` | Zwraca aktualna pozycje kamery. |
| `getPosition(const Point& point, ...)` | Konwertuje wsp�lrzedne ekranu na pozycje na mapie. |
| `setDrawFlags(Otc::DrawFlags flags)` | Ustawia flagi rysowania, okreslajace, co ma byc renderowane. |
| `setAnimated(bool animated)` | Wlacza/wylacza animacje. |
| `setFloorFading(int value)` | Ustawia czas zanikania/pojawiania sie pieter. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w (`Position`, `CreaturePtr`).
- **`lightview.h`**: Uzywa `LightView` do rysowania swiatel.
- **`framework/luaengine/luaobject.h`**: Dziedziczy z `LuaObject`.

---
# ?? minimap.h
# # Og�lny opis
Plik nagl�wkowy dla `Minimap` i powiazanych struktur. Definiuje interfejs do zarzadzania danymi minimapy i jej renderowania.
# # Struktury i stale
- **`MMBLOCK_SIZE`**: Rozmiar bloku minimapy (64x64 piksele).
- **`MinimapTileFlags`**: Flagi dla kafelka minimapy (np. `MinimapTileWasSeen`, `MinimapTileNotPathable`).
- **`MinimapTile`**: Struktura przechowujaca dane pojedynczego piksela minimapy (kolor, flagi, predkosc).
# # Klasa `MinimapBlock`
# # # Opis
Reprezentuje pojedynczy blok (chunk) minimapy o rozmiarze `MMBLOCK_SIZE` x `MMBLOCK_SIZE`. Kazdy blok ma wlasna teksture, co optymalizuje renderowanie.
- `m_texture`: Tekstura generowana na podstawie danych z `m_tiles`.
- `m_tiles`: Tablica `MinimapTile` przechowujaca dane dla kazdego piksela w bloku.
- `m_mustUpdate`: Flaga informujaca, czy tekstura wymaga ponownego wygenerowania.
# # Klasa `Minimap`
# # # Opis
Singleton (`g_minimap`) zarzadzajacy wszystkimi danymi minimapy. Przechowuje `MinimapBlock` dla kazdego pietra i koordynuje ich rysowanie.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizacja i zamykanie managera. |
| `clean()` | Czysci wszystkie dane minimapy. |
| `draw(...)` | Rysuje minimape na ekranie w danym prostokacie. |
| `getTilePoint(const Position& pos, ...)` | Konwertuje pozycje na mapie na wsp�lrzedne na widzecie minimapy. |
| `getTilePosition(const Point& point, ...)` | Konwertuje wsp�lrzedne na widzecie minimapy na pozycje na mapie. |
| `updateTile(const Position& pos, const TilePtr& tile)` | Aktualizuje dane piksela minimapy na podstawie danych z `Tile`. |
| `getTile(const Position& pos)` | Zwraca dane `MinimapTile` dla danej pozycji. |
| `loadImage(...)` | Wczytuje dane minimapy z pliku graficznego (np. PNG). |
| `saveImage(...)` | Zapisuje widoczny obszar minimapy do pliku graficznego. |
| `loadOtmm(...)` / `saveOtmm(...)` | Wczytuje/zapisuje dane minimapy w formacie `.otmm`. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`tile.h`**: `updateTile` pobiera dane z obiektu `Tile`.

---
# ?? missile.cpp
# # Og�lny opis
Implementacja klasy `Missile`, kt�ra odpowiada za renderowanie pocisk�w w grze.
# # Klasa `Missile`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje pocisk na ekranie. Oblicza jego pozycje na sciezce lotu na podstawie czasu, kt�ry uplynal (`m_animationTimer.ticksElapsed() / m_duration`). Wybiera odpowiedni wz�r (pattern) sprite'a na podstawie kierunku lotu. |
| `setPath(const Position& fromPosition, const Position& toPosition)` | Ustawia sciezke lotu pocisku od pozycji poczatkowej do koncowej. Oblicza kierunek, czas trwania lotu i planuje automatyczne usuniecie pocisku po dotarciu do celu. |
| `setId(uint32 id)` | Ustawia ID (typ) pocisku, weryfikujac jego poprawnosc. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla danego pocisku. |
# # # Logika animacji
Pozycja pocisku jest interpolowana liniowo miedzy punktem startowym a koncowym. Frakcja postepu `fraction` jest obliczana jako stosunek czasu, kt�ry uplynal, do calkowitego czasu trwania lotu. Przesuniecie rysowania `m_delta * fraction` jest dodawane do pozycji poczatkowej.
# # # Zaleznosci i powiazania
- **`map.h`**: Uzywa `g_map` do usuniecia pocisku po zakonczeniu lotu.
- **`spritemanager.h`**: Uzywa `g_sprites.spriteSize()` do skalowania przesuniecia.
- **`framework/core/eventdispatcher.h`**: Uzywa `g_dispatcher` do planowania usuniecia.

---
# ?? missile.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Missile`, kt�ra reprezentuje pociski i inne efekty dystansowe.
# # Klasa `Missile`
# # # Opis
Dziedziczy po `Thing`. Reprezentuje obiekt, kt�ry przemieszcza sie od jednej pozycji do drugiej w okreslonym czasie.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje pocisk w jego aktualnej pozycji na sciezce. |
| `setId(uint32 id)` | Ustawia ID (typ) pocisku. |
| `setPath(const Position& from, const Position& to)` | Ustawia poczatek i koniec sciezki pocisku. |
| `getId()` | Zwraca ID pocisku. |
| `asMissile()` | Rzutuje wskaznik na `MissilePtr`. |
| `isMissile()` | Zwraca `true`. |
| `getThingType()` | Zwraca `ThingType` dla pocisku. |
| `getSource()` | Zwraca pozycje poczatkowa. |
| `getDestination()` | Zwraca pozycje koncowa. |
# # # Zaleznosci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/core/timer.h`**: Uzywa `Timer` do animacji ruchu.

---
# ?? outfit.cpp
# # Og�lny opis
Implementacja klasy `Outfit` oraz niestandardowych element�w kolejki rysowania `DrawQueueItemOutfit` i `DrawQueueItemOutfitWithShader`. Plik zawiera zlozona logike rysowania ubioru postaci, w tym warstw, kolor�w, dodatk�w, wierzchowc�w, skrzydel, aury i shader�w.
# # Klasa `Outfit`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(Point dest, ...)` | Gl�wna funkcja rysujaca ubi�r. Wykonuje nastepujace kroki: <br> 1. Koryguje kierunek. <br> 2. Oblicza faze animacji (chodzenia, bezczynnosci, UI). <br> 3. Rysuje aure (tylna warstwe, jesli dotyczy). <br> 4. Rysuje wierzchowca. <br> 5. Rysuje skrzydla (w zaleznosci od kierunku, przed lub za postacia). <br> 6. Rysuje poszczeg�lne warstwy ubioru (podstawe i dodatki), kolorujac je za pomoca specjalnego shadera (`DrawQueueItemOutfit`). <br> 7. Rysuje aure (przednia warstwe). |
| `draw(const Rect& dest, ...)` | Wersja rysujaca ubi�r przeskalowany do danego prostokata, uzywana w UI. |
| `resetClothes()` | Resetuje wszystkie elementy ubioru (glowa, cialo, etc.) do wartosci domyslnych (0). |
# # Klasy `DrawQueueItem...`
# # # Opis
Niestandardowe elementy kolejki rysowania, kt�re pozwalaja na zaawansowane renderowanie ubior�w.
- **`DrawQueueItemOutfit`**: Uzywa specjalnego shadera (`outfit.frag`), kt�ry na podstawie 32-bitowej liczby `m_colors` i tekstury z warstwami, koloruje kazda z czterech czesci ubioru (glowa, cialo, nogi, stopy) na odpowiedni kolor.
- **`DrawQueueItemOutfitWithShader`**: Rozszerza powyzsza logike o dodatkowy, niestandardowy shader (np. efekt "ghost"), kt�ry jest nakladany na finalny obraz ubioru.
# # # Zaleznosci i powiazania
- **`game.h`**: Sprawdza, kt�re `GameFeature` sa aktywne, aby decydowac, kt�re elementy ubioru rysowac (np. wierzchowce, skrzydla).
- **`thingtypemanager.h`**: Uzywa `g_things` do pobierania `ThingType` dla ubioru, wierzchowca, skrzydel, aury.
- **`spritemanager.h`**: Uzywa `g_sprites` do skalowania i pozycjonowania.
- **`framework/graphics/drawqueue.h`**: Dodaje niestandardowe elementy do kolejki rysowania.
- **`framework/graphics/shadermanager.h`**: Zarzadza i uzywa shader�w do kolorowania i efekt�w.

---
# ?? outfit.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Outfit` oraz powiazanych struktur do rysowania.
# # Klasa `Outfit`
# # # Opis
Reprezentuje wyglad (ubi�r) postaci. Przechowuje informacje o ID wygladu, kolorach poszczeg�lnych czesci ciala, dodatkach, wierzchowcu, skrzydlach, aurze i niestandardowym shaderze.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Dwie przeciazone wersje funkcji rysujacej ubi�r: jedna w punkcie (na mapie), druga w prostokacie (w UI). |
| `setId(int id)` | Ustawia ID ubioru (dla potwor�w) lub przedmiotu (dla niewidzialnosci). |
| `setHead(int head)` | Ustawia kolor glowy. |
| `setBody(int body)` | Ustawia kolor torsu. |
| `setLegs(int legs)` | Ustawia kolor n�g. |
| `setFeet(int feet)` | Ustawia kolor st�p. |
| `setAddons(int addons)` | Ustawia dodatki (bitmaska). |
| `setMount(int mount)` | Ustawia ID wierzchowca. |
| `setWings(int wings)` | Ustawia ID skrzydel. |
| `setAura(int aura)` | Ustawia ID aury. |
| `setShader(const std::string& shader)` | Ustawia nazwe niestandardowego shadera. |
# # Struktury `DrawQueueItem...`
# # # Opis
Definicje niestandardowych element�w kolejki rysowania, kt�re obsluguja zaawansowane renderowanie ubior�w.
- **`DrawQueueItemOutfit`**: Renderuje ubi�r z dynamicznym kolorowaniem poszczeg�lnych czesci.
- **`DrawQueueItemOutfitWithShader`**: Dodaje obsluge niestandardowego shadera efekt�w specjalnych.
# # # Zaleznosci i powiazania
- **`thingtypemanager.h`**: Uzywa `ThingCategory` i `ThingType`.
- **`framework/graphics/drawqueue.h`**: Dziedzicza z `DrawQueueItemTexturedRect`.

---
# ?? player.cpp
# # Og�lny opis
Ten plik jest obecnie pusty, co oznacza, ze klasa `Player` nie posiada zadnej dodatkowej implementacji poza tym, co dziedziczy z klasy `Creature`.
# # Klasa `Player`
# # # Opis
Klasa `Player` jest specjalizacja `Creature`. Sluzy do reprezentowania postaci graczy w grze. W przyszlosci moze zawierac logike specyficzna tylko dla graczy, kt�ra nie dotyczy potwor�w czy NPC.
# # # Zaleznosci i powiazania
- **`player.h`**: Plik nagl�wkowy dla tej implementacji.

---
# ?? player.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `Player`, kt�ra jest specjalizacja klasy `Creature`.
# # Klasa `Player`
# # # Opis
Dziedziczy po `Creature`. Reprezentuje postac gracza (niekoniecznie lokalnego). Nie dodaje zadnych nowych p�l ani metod, ale sluzy do rozr�znienia typ�w stworzen w systemie typ�w C++.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `asPlayer()` | Rzutuje wskaznik na `PlayerPtr`. |
| `isPlayer()` | Zwraca `true`. |
# # # Zaleznosci i powiazania
- **`creature.h`**: Klasa bazowa.

---
# ?? protocolcodes.cpp
# # Og�lny opis
Implementacja funkcji pomocniczych zadeklarowanych w `protocolcodes.h`. Gl�wnym zadaniem tego pliku jest zarzadzanie mapowaniem tryb�w wiadomosci (`Otc::MessageMode`) na ich liczbowe odpowiedniki uzywane w protokole sieciowym, kt�re moga sie r�znic w zaleznosci od wersji klienta.
# # Namespace `Proto`
# # # Zmienne globalne
- **`std::map<uint8, uint8> messageModesMap`**: Mapa przechowujaca powiazanie miedzy wewnetrznym enumem `Otc::MessageMode` a wartoscia liczbowa wysylana/odbierana z serwera.
# # # Funkcje
| Nazwa | Opis |
| --- | --- |
| `buildMessageModesMap(int version)` | Wypelnia `messageModesMap` na podstawie podanej wersji protokolu. Zawiera bloki `if/else if` dla r�znych zakres�w wersji, definiujac odpowiednie mapowania. Jest to kluczowe dla zachowania kompatybilnosci wstecznej. |
| `translateMessageModeFromServer(uint8 mode)` | Tlumaczy liczbowy tryb wiadomosci otrzymany z serwera na wewnetrzny enum `Otc::MessageMode`. |
| `translateMessageModeToServer(Otc::MessageMode mode)` | Tlumaczy wewnetrzny enum `Otc::MessageMode` na jego liczbowy odpowiednik, kt�ry zostanie wyslany do serwera. |
# # # Zaleznosci i powiazania
- **`protocolcodes.h`**: Deklaracje funkcji i enum�w.
- **`game.cpp`**: `Game::setProtocolVersion` wywoluje `buildMessageModesMap`, aby zaktualizowac mapowania po zmianie wersji protokolu.

---
# ?? minimap.cpp
# # Og�lny opis
Implementacja `Minimap` i `MinimapBlock`, kt�re razem tworza system minimapy w grze. Plik zawiera logike renderowania, aktualizacji danych, a takze wczytywania i zapisywania minimapy w formatach `.otmm` i graficznych.
# # Klasa `MinimapBlock`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `clean()` | Resetuje wszystkie dane w bloku do stanu poczatkowego. |
| `update()` | Jesli blok zostal zmodyfikowany (`m_mustUpdate`), generuje nowa teksture na podstawie danych z `m_tiles`. Tworzy obiekt `Image`, wypelnia go kolorami pikseli, a nastepnie tworzy z niego teksture. |
| `updateTile(...)` | Aktualizuje dane pojedynczego piksela w bloku i ustawia flage `m_mustUpdate`. |
# # Klasa `Minimap`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Rysuje minimape na ekranie. Oblicza, kt�re bloki (`MinimapBlock`) sa widoczne, aktualizuje ich tekstury (jesli to konieczne), a nastepnie rysuje je w odpowiednich pozycjach. |
| `getTilePoint(...)` / `getTilePosition(...)` | Funkcje pomocnicze do konwersji miedzy pozycja na mapie a wsp�lrzednymi na widzecie minimapy. |
| `updateTile(const Position& pos, const TilePtr& tile)` | Pobiera kolor i flagi z `Tile` i aktualizuje odpowiadajacy mu piksel w `MinimapBlock`. |
| `getTile(const Position& pos)` | Zwraca dane `MinimapTile` dla danej pozycji. |
| `threadGetTile(...)` | Wersja `getTile` bezpieczna dla watk�w, uzywana przez asynchroniczne wyszukiwanie sciezki. |
| `loadImage(...)` | Wczytuje dane minimapy z pliku graficznego, analizujac kolory pikseli w celu okreslenia wlasciwosci (np. czy pole jest mozliwe do przejscia). |
| `saveOtmm(...)` / `loadOtmm(...)` | Obsluguje serializacje/deserializacje danych minimapy do/z formatu `.otmm`, kt�ry uzywa kompresji zlib dla kazdego bloku. |
# # # Struktura danych
- `m_tileBlocks`: Tablica map `std::unordered_map<uint, MinimapBlock_ptr>`, gdzie kazdy element tablicy odpowiada jednemu pietru (`z`). Mapa przechowuje bloki minimapy, indeksowane przez skr�t ich pozycji.
# # # Zaleznosci i powiazania
- **`tile.h`**: Pobiera dane do aktualizacji minimapy z obiekt�w `Tile`.
- **`game.h`**: Uzywa `g_game` do sprawdzania funkcji, np. `GameDontCacheFiles`.
- **`framework/graphics/...`**: Uzywa klas `Image`, `Texture`, `Painter` do operacji graficznych.
- **`framework/core/resourcemanager.h`**: Do operacji na plikach.
- **`zlib.h`**: Do kompresji/dekompresji danych w formacie `.otmm`.

---
# ?? position.h
# # Og�lny opis
Plik nagl�wkowy definiujacy strukture `Position` oraz powiazane z nia funkcje pomocnicze. Jest to fundamentalna struktura uzywana w calym projekcie do reprezentowania wsp�lrzednych w tr�jwymiarowym swiecie gry.
# # Struktura `Position`
# # # Pola
- `int x`, `int y`: Wsp�lrzedne na plaszczyznie poziomej.
- `short z`: Wsp�lrzedna pietra.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `Position(uint16 x, uint16 y, uint8 z)` | Konstruktor. |
| `translatedToDirection(Otc::Direction direction)` | Zwraca nowa pozycje przesunieta o jedno pole w danym kierunku. |
| `translatedToReverseDirection(...)` | Zwraca nowa pozycje przesunieta w kierunku przeciwnym. |
| `translatedToDirections(...)` | Przetwarza liste kierunk�w i zwraca liste kolejnych pozycji na sciezce. |
| `getAngleFromPositions(from, to)` | Statyczna metoda obliczajaca kat (w radianach) miedzy dwiema pozycjami. |
| `getDirectionFromPositions(from, to)` | Statyczna metoda zwracajaca kierunek (`Otc::Direction`) z jednej pozycji do drugiej. |
| `isMapPosition()` | Sprawdza, czy pozycja jest poprawna pozycja na mapie. |
| `isValid()` | Sprawdza, czy pozycja jest "wazna" (r�zna od pozycji specjalnej 65535, 65535, 255). |
| `distance(const Position& pos)` | Oblicza dystans euklidesowy. |
| `manhattanDistance(const Position& pos)` | Oblicza odleglosc w metryce taks�wkowej. |
| `up()`, `down()`, `coveredUp()`, `coveredDown()` | Metody do przemieszczania sie miedzy pietrami z uwzglednieniem perspektywy izometrycznej. |
| `toString()` | Zwraca pozycje w formacie "x,y,z". |
| `operator==`, `operator!=`, `operator<` | Operatory por�wnania. |
| `operator+`, `operator-` | Operatory arytmetyczne. |
# # Struktura `PositionHasher`
# # # Opis
Funktor uzywany do haszowania obiekt�w `Position`, co pozwala na uzywanie ich jako kluczy w kontenerach `std::unordered_map`.
# # # Zaleznosci i powiazania
- **`const.h`**: Definicje `Otc::Direction` i `Otc::MAX_Z`.
- Plik ten jest dolaczany w niemal kazdym pliku, kt�ry operuje na logice swiata gry.

---
# ?? protocolcodes.h
# # Og�lny opis
Plik nagl�wkowy definiujacy kody operacyjne (opcodes) uzywane w protokole sieciowym miedzy klientem a serwerem gry. Zawiera r�wniez definicje typ�w stworzen i mapowanie tryb�w wiadomosci.
# # Namespace `Proto`
# # # Typy wyliczeniowe
- **`LoginServerOpts`**: Kody operacyjne uzywane podczas komunikacji z serwerem logowania.
- **`ItemOpcode`**: Specjalne ID uzywane do identyfikacji stworzen i tekst�w w strumieniu danych o polach mapy.
- **`GameServerOpcodes`**: Kody operacyjne dla pakiet�w wysylanych z serwera do klienta. Lista jest dluga i zawiera kody dla wszystkich akcji w grze, takich jak logowanie, ruch postaci, aktualizacje mapy, wiadomosci, handel itp.
- **`ClientOpcodes`**: Kody operacyjne dla pakiet�w wysylanych z klienta do serwera.
- **`CreatureType`**: Typy stworzen (gracz, potw�r, NPC).
- **`CreaturesIdRange`**: Zakresy ID dla r�znych typ�w stworzen.
# # # Funkcje
- **`buildMessageModesMap(int version)`**: Buduje mape tlumaczaca wewnetrzne tryby wiadomosci na kody protokolu dla danej wersji.
- **`translateMessageModeFromServer(uint8 mode)`**: Konwertuje kod z serwera na `Otc::MessageMode`.
- **`translateMessageModeToServer(Otc::MessageMode mode)`**: Konwertuje `Otc::MessageMode` na kod dla serwera.

> NOTE: Lista opkod�w zawiera zar�wno standardowe kody z protokolu Tibii, jak i niestandardowe kody specyficzne dla OTClient (`OTClientV8 64-79`) i rozszerzone opkody (`GameServerExtendedOpcode`).
# # # Zaleznosci i powiazania
- **`global.h`**: Podstawowe definicje.
- Ten plik jest kluczowy dla `ProtocolGame`, kt�ry uzywa tych kod�w do identyfikacji i parsowania pakiet�w sieciowych.

---
# ?? protocolgame.cpp
# # Og�lny opis
Implementacja czesci klasy `ProtocolGame` odpowiedzialnej za zarzadzanie polaczeniem i podstawowa obsluge zdarzen sieciowych.
# # Klasa `ProtocolGame`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `login(...)` | Inicjuje proces logowania, zapisujac dane uwierzytelniajace i dane swiata, a nastepnie nawiazuje polaczenie z serwerem. |
| `onConnect()` | Metoda wywolywana po pomyslnym nawiazaniu polaczenia. Wlacza odpowiednie funkcje protokolu (np. sumy kontrolne, szyfrowanie, duze pakiety) w zaleznosci od `GameFeature` i wysyla pierwszy pakiet logowania. |
| `onRecv(const InputMessagePtr& inputMessage)` | Gl�wna petla odbioru danych. Wywolywana za kazdym razem, gdy nadejdzie nowy pakiet. Weryfikuje rozmiar wiadomosci (jesli `GameMessageSizeCheck` jest aktywne), a nastepnie przekazuje pakiet do `parseMessage` w celu przetworzenia. Po przetworzeniu planuje odbi�r kolejnego pakietu. |
| `onError(const boost::system::error_code& error)` | Obsluguje bledy polaczenia. Powiadamia `g_game` o bledzie i rozlacza klienta. |
# # # Zaleznosci i powiazania
- **`game.h`**: Scisle wsp�lpracuje z `g_game`, informujac go o stanie polaczenia i przekazujac przetworzone dane.
- **`player.h`**, **`localplayer.h`**: Ustawia instancje `LocalPlayer` na poczatku polaczenia.
- **`framework/net/protocol.h`**: Dziedziczy z `Protocol` i wykorzystuje jego mechanizmy do obslugi polaczenia TCP.

---
# ?? protocolgame.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `ProtocolGame`. Definiuje interfejs protokolu sieciowego uzywanego do komunikacji z serwerem gry. Zawiera deklaracje funkcji do wysylania pakiet�w oraz parsowania odpowiedzi z serwera.
# # Klasa `ProtocolGame`
# # # Opis
Dziedziczy po `Protocol`. Jest to centralny punkt obslugi komunikacji sieciowej w grze.
# # # Metody (Wysylanie)
Plik deklaruje duza liczbe metod `send...`, z kt�rych kazda odpowiada za wyslanie konkretnego pakietu do serwera. Przyklady:
- `sendLoginPacket(...)`: Wysyla pakiet logowania.
- `sendWalkNorth()`: Wysyla zadanie ruchu na p�lnoc.
- `sendMove(...)`: Wysyla zadanie przesuniecia przedmiotu.
- `sendTalk(...)`: Wysyla wiadomosc czatu.
- `sendAttack(...)`: Wysyla zadanie ataku.
# # # Metody (Parsowanie)
Deklaruje r�wniez metody `parse...`, kt�re sa wywolywane w `protocolgameparse.cpp` do przetwarzania pakiet�w przychodzacych z serwera. Przyklady:
- `parseMapDescription(...)`: Parsuje pelny opis mapy.
- `parseCreatureHealth(...)`: Parsuje aktualizacje zycia stworzenia.
- `parseTextMessage(...)`: Parsuje wiadomosc tekstowa.
# # # Metody (Pomocnicze)
- `getThing(...)`, `getItem(...)`, `getCreature(...)`, `getPosition(...)`: Funkcje pomocnicze do odczytywania zlozonych typ�w danych ze strumienia `InputMessage`.
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w (`Position`, `CreaturePtr`, etc.).
- **`protocolcodes.h`**: Uzywa kod�w operacyjnych zdefiniowanych w tym pliku.
- **`framework/net/protocol.h`**: Klasa bazowa.

---
# ?? spritemanager.cpp
# # Og�lny opis
Implementacja `SpriteManager`, klasy odpowiedzialnej za zarzadzanie plikami sprite'�w (`.spr`, `.cwm`). Plik zawiera logike wczytywania, zapisywania, a takze deszyfrowania i dekompresji danych sprite'�w.
# # Klasa `SpriteManager`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `loadSpr(std::string file)` | Gl�wna funkcja wczytujaca. Sprawdza, czy istnieje plik `.cwm` (HD mod) lub `.spr` i wywoluje odpowiednia metode wczytujaca. |
| `saveSpr(...)` / `saveSpr64(...)` | Metody do zapisywania sprite'�w w formacie `.spr` (32x32 lub 64x64). Wymaga `WITH_ENCRYPTION`. |
| `encryptSprites(...)` | Zapisuje sprite'y w niestandardowym, zaszyfrowanym formacie OTV8. |
| `dumpSprites(...)` | Zapisuje wszystkie sprite'y jako pojedyncze pliki PNG do danego folderu (funkcja deweloperska). |
| `unload()` | Zwalnia wszystkie zasoby zwiazane ze sprite'ami. |
| `getSpriteImage(int id)` | Gl�wna metoda do pobierania obrazu sprite'a. Wywoluje odpowiednia implementacje w zaleznosci od tego, czy zaladowano mod HD (`.cwm`) czy standardowy plik (`.spr`). |
| `loadCasualSpr(...)` | Wczytuje standardowy plik `.spr`. Odczytuje sygnature i liczbe sprite'�w. Obsluguje r�wniez zaszyfrowany format OTV8. |
| `loadCwmSpr(...)` | Wczytuje plik `.cwm`, kt�ry jest zbiorem skompresowanych danych PNG. Uzywa `PngUnpacker` do rozpakowania wszystkich sprite'�w do pamieci. |
| `getSpriteImageCasual(int id)` | Pobiera obraz sprite'a z pliku `.spr`. Odczytuje adres sprite'a z tablicy offset�w, a nastepnie dekompresuje dane pikseli, kt�re sa zapisane w formacie RLE (run-length encoding) z przezroczystymi i kolorowymi pikselami. |
| `getSpriteImageHd(int id)` | Pobiera obraz sprite'a z pamieci podrecznej wczytanej z pliku `.cwm`. Dekoduje dane PNG dla danego sprite'a. |
# # # Zaleznosci i powiazania
- **`game.h`**: Uzywa `g_game` do sprawdzania `GameFeature`, kt�re wplywaja na format pliku `.spr`.
- **`framework/core/resourcemanager.h`**: Do operacji na plikach.
- **`framework/graphics/image.h`**: Zwraca obiekty `ImagePtr`.
- **`framework/util/crypt.h`**: Do deszyfrowania formatu OTV8.
- **`framework/util/pngunpacker.h`**: Do rozpakowywania plik�w `.cwm`.

---
# ?? protocolgamesend.cpp
# # Og�lny opis
Plik ten zawiera implementacje metod klasy `ProtocolGame` odpowiedzialnych za **wysylanie** pakiet�w do serwera gry. Kazda metoda odpowiada za stworzenie i wyslanie konkretnego komunikatu zgodnie z protokolem sieciowym.
# # Klasa `ProtocolGame`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `send(const OutputMessagePtr& outputMessage, ...)` | Wysyla przygotowany pakiet, sprawdzajac uprzednio zabezpieczenia anty-botowe (`g_game.checkBotProtection()`). |
| `sendLoginPacket(...)` | Tworzy i wysyla pakiet logowania. Zawiera logike szyfrowania RSA, dodawania klucza XTEA, a takze wysylania dodatkowych danych identyfikacyjnych klienta (nazwa uzytkownika, CPU, adresy MAC), jesli serwer to obsluguje. |
| `sendWalkNorth()`, `sendWalkEast()`, etc. | Wysylaja jednobajtowe pakiety z zadaniem ruchu w danym kierunku. |
| `sendAutoWalk(...)` | Wysyla sekwencje kierunk�w dla automatycznego poruszania sie. |
| `sendNewWalk(...)` | Wysyla pakiet dla nowego systemu chodzenia, zawierajacy ID kroku, ID predykcji, pozycje i sciezke. |
| `sendMove(...)` | Wysyla zadanie przesuniecia przedmiotu/stworzenia. |
| `sendUseItem(...)`, `sendUseItemWith(...)` | Wysylaja zadania uzycia przedmiot�w. |
| `sendTalk(...)` | Wysyla wiadomosc czatu. Konstruuje pakiet w zaleznosci od trybu wiadomosci (publiczny, prywatny, kanal). |
| `sendAttack(...)`, `sendFollow(...)` | Wysylaja zadania ataku lub sledzenia stworzenia, zawierajac sekwencyjny numer identyfikujacy akcje. |
| `sendChangeOutfit(...)` | Wysyla nowy ubi�r gracza, uwzgledniajac wszystkie jego elementy (kolory, dodatki, wierzchowiec, etc.) w zaleznosci od wspieranych przez serwer funkcji. |
| `addPosition(const OutputMessagePtr& msg, ...)` | Pomocnicza metoda do dodawania wsp�lrzednych `Position` do pakietu. |
# # # Logika
Wiekszosc funkcji w tym pliku ma prosta strukture:
1.  Stw�rz nowy `OutputMessage`.
2.  Dodaj kod operacyjny (opcode) za pomoca `msg->addU8(...)`.
3.  Dodaj kolejne dane (ID, pozycje, stringi) zgodnie ze specyfikacja protokolu.
4.  Wyslij pakiet za pomoca `send(msg)`.
# # # Zaleznosci i powiazania
- **`game.h`**: Uzywa `g_game` do sprawdzania funkcji serwera (`GameFeature`), kt�re determinuja format wysylanych pakiet�w.
- **`localplayer.h`**: Uzywa pozycji lokalnego gracza w niekt�rych pakietach (np. `sendTalk`).
- **`framework/util/crypt.h`**: Uzywa `g_crypt` do szyfrowania RSA.
- **`framework/platform/platform.h`**: Pobiera informacje o systemie do wyslania w pakiecie logowania.

---
# ?? localplayer.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `LocalPlayer`, kt�ra reprezentuje postac sterowana przez gracza. Jest to specjalizacja klasy `Player`.
# # Klasa `LocalPlayer`
# # # Opis
Dziedziczy po `Player`. Dodaje funkcjonalnosci specyficzne dla gracza, kt�ry jest kontrolowany przez klienta, takie jak:
-   **Pre-walking**: Przewidywanie ruchu przed otrzymaniem odpowiedzi z serwera.
-   **Auto-walking**: Automatyczne poruszanie sie do celu.
-   **Zarzadzanie stanem**: Przechowuje szczeg�lowe statystyki (zycie, mana, umiejetnosci, etc.).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `lockWalk(int millis)` | Blokuje mozliwosc chodzenia na okreslony czas. |
| `stopAutoWalk()` | Przerywa auto-walking. |
| `autoWalk(Position destination, ...)` | Rozpoczyna auto-walking do celu. |
| `canWalk(...)` | Sprawdza, czy gracz moze sie poruszyc. |
| `isPreWalking()` | Zwraca `true`, jesli gracz wykonuje ruch "pre-walk". |
| `getPrewalkingPosition(...)` | Zwraca pozycje, na kt�rej gracz znajdzie sie po zakonczeniu wszystkich ruch�w "pre-walk". |
| `setHealth(...)`, `setMana(...)`, etc. | Metody do ustawiania statystyk gracza. |
| `getHealth()`, `getMana()`, etc. | Metody do pobierania statystyk. |
| `hasSight(const Position& pos)` | Sprawdza, czy pozycja jest w zasiegu wzroku. |
# # # Zaleznosci i powiazania
- **`player.h`**: Klasa bazowa.
- **`walkmatrix.h`**: Uzywa `WalkMatrix` do sledzenia predykcji ruchu.

---
# ?? towns.cpp
# # Og�lny opis
Implementacja `Town` i `TownManager`, kt�re sluza do zarzadzania danymi o miastach w grze.
# # Klasa `Town`
# # # Metody
- **`Town(uint32 tid, ...)`**: Konstruktor, kt�ry inicjalizuje miasto z podanym ID, nazwa i pozycja (zwykle swiatyni).
# # Klasa `TownManager`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `addTown(const TownPtr &town)` | Dodaje nowe miasto do listy, jesli jeszcze nie istnieje. |
| `removeTown(uint32 townId)` | Usuwa miasto o podanym ID. |
| `getTown(uint32 townId)` | Zwraca miasto po jego ID. |
| `getTownByName(std::string name)` | Zwraca miasto po jego nazwie. |
| `findTown(uint32 townId)` | Wewnetrzna metoda do wyszukiwania iteratora do miasta. |
| `sort()` | Sortuje liste miast alfabetycznie wedlug nazwy. |
# # # Zmienne globalne
- **`TownManager g_towns`**: Globalna instancja managera miast.
# # # Zaleznosci i powiazania
- **`mapio.cpp`**: Menedzer `g_towns` jest wypelniany danymi podczas wczytywania mapy w formacie OTBM.

---
# ?? spritemanager.h
# # Og�lny opis
Plik nagl�wkowy dla `SpriteManager`, singletonu odpowiedzialnego za zarzadzanie plikami sprite'�w (`.spr`).
# # Klasa `SpriteManager`
# # # Opis
Centralny punkt dostepu do danych graficznych sprite'�w. Odpowiada za wczytywanie, deszyfrowanie, dekompresje i dostarczanie obraz�w poszczeg�lnych sprite'�w.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `loadSpr(std::string file)` | Wczytuje plik sprite'�w (automatycznie wykrywa format: `.spr`, `.cwm`, OTV8). |
| `unload()` | Zwalnia wszystkie zaladowane dane sprite'�w. |
| `saveSpr(...)` / `encryptSprites(...)` | Metody (dostepne z `WITH_ENCRYPTION`) do zapisywania i szyfrowania plik�w sprite'�w. |
| `getSignature()` | Zwraca sygnature wczytanego pliku `.spr`. |
| `getSpritesCount()` | Zwraca liczbe sprite'�w w pliku. |
| `getSpriteImage(int id)` | Gl�wna metoda do pobierania obrazu sprite'a o danym ID. |
| `isLoaded()` | Zwraca `true`, jesli plik sprite'�w jest zaladowany. |
| `spriteSize()` | Zwraca rozmiar boku pojedynczego sprite'a (np. 32 lub 64 piksele). |
| `getOffsetFactor()` | Zwraca wsp�lczynnik skalowania dla przemieszczen (displacement) w zaleznosci od `spriteSize`. |
| `isHdMod()` | Zwraca `true`, jesli zaladowano modyfikacje HD (`.cwm`). |
# # # Zmienne globalne
- **`SpriteManager g_sprites`**: Globalna instancja managera sprite'�w.
# # # Zaleznosci i powiazania
- **`framework/core/declarations.h`**: Podstawowe deklaracje.
- **`framework/graphics/declarations.h`**: Deklaracje typ�w graficznych.
- Niemal kazda klasa renderujaca obiekty w grze (np. `ThingType`, `Item`, `Creature`) zalezy od `SpriteManager`.

---
# ?? tile.cpp
# # Og�lny opis
Implementacja klasy `Tile`, kt�ra reprezentuje pojedyncze pole na mapie gry. Plik zawiera logike rysowania pola i wszystkich znajdujacych sie na nim obiekt�w, zarzadzania stosem obiekt�w oraz dostarczania informacji o wlasciwosciach pola.
# # Klasa `Tile`
# # # Metody
# # # # Rysowanie
| Nazwa | Opis |
| --- | --- |
| `drawGround(...)` | Rysuje podloze i obiekty na najnizszej warstwie. Oblicza `m_drawElevation` (przesuniecie w pionie dla obiekt�w o wysokosci > 1). |
| `drawBottom(...)` | Rysuje przedmioty, kt�re znajduja sie na spodzie, ale nad podlozem (np. sciany). |
| `drawCreatures(...)` | Rysuje stworzenia na tym polu oraz stworzenia, kt�re na nie wchodza. |
| `drawTop(...)` | Rysuje przedmioty na wierzchu, efekty oraz ponownie stworzenia, aby obsluzyc przypadki nakladania sie. |
| `drawTexts(...)` | Rysuje tekst przypisany do pola (np. timer). |
| `drawWidget(...)` | Rysuje przypisany do pola widzet. |
# # # # Zarzadzanie obiektami
| Nazwa | Opis |
| --- | --- |
| `addThing(...)` | Dodaje obiekt (`Thing`) na stos w odpowiedniej pozycji, uwzgledniajac jego priorytet (ziemia, przedmioty, stworzenia). |
| `removeThing(...)` | Usuwa obiekt ze stosu. |
| `addWalkingCreature(...)` | Dodaje stworzenie do listy "przechodzacych" przez to pole, kt�re sa rysowane osobno. |
| `getThing(...)` | Zwraca obiekt z danej pozycji na stosie. |
| `getTopThing()`, `getTopCreature()`, etc. | Zwracaja "najwazniejszy" obiekt danego typu na polu, uwzgledniajac logike gry (np. na co patrzy gracz, czego uzywa). |
| `getItems()`, `getCreatures()` | Zwracaja listy wszystkich przedmiot�w lub stworzen na polu. |
# # # # Wlasciwosci
| Nazwa | Opis |
| --- | --- |
| `isWalkable(...)` | Sprawdza, czy po polu mozna chodzic (czy nie ma blokujacych przedmiot�w lub stworzen). |
| `isPathable()` | Sprawdza, czy algorytm wyszukiwania sciezki moze uzywac tego pola. |
| `isFullGround()` | Sprawdza, czy podloze calkowicie zakrywa pole pod nim. |
| `getGroundSpeed()` | Zwraca predkosc poruszania sie po tym polu. |
# # # Zaleznosci i powiazania
- **`map.h`**: Uzywa `g_map` do pobierania sasiednich p�l (np. przy korekcji zwlok).
- **`game.h`**: Dostep do `g_game` w celu sprawdzania `GameFeature`.
- **`thing.h`**, **`item.h`**, **`creature.h`**: Zarzadza tymi obiektami.
- **`lightview.h`**: Przekazuje `LightView` do metod rysujacych obiekty, aby mogly dodac swoje swiatlo.

---
# ?? statictext.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `StaticText`, kt�ra reprezentuje tekst pojawiajacy sie nad glowami stworzen lub na polach mapy.
# # Struktura `StaticTextMessage`
-   **`texts`**: Wektor par `std::string`, gdzie pierwsza to tresc, a druga to kolor w formacie hex.
-   **`time`**: Czas (w tickach), po kt�rym wiadomosc powinna zniknac.
# # Klasa `StaticText`
# # # Opis
Dziedziczy po `Thing`. Zarzadza kolejka wiadomosci, kt�re sa wyswietlane jedna po drugiej. Jest uzywana do mowy postaci, potwor�w, a takze do niestandardowych tekst�w na mapie.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawText(...)` | Rysuje aktualnie wyswietlana wiadomosc. |
| `getName()` | Zwraca nazwe postaci m�wiacej. |
| `getText()` | Zwraca aktualnie wyswietlany tekst. |
| `getMessageMode()` | Zwraca tryb wiadomosci (np. `Say`, `Yell`). |
| `addMessage(...)` / `addColoredMessage(...)` | Dodaje nowa wiadomosc do kolejki. Oblicza czas jej wyswietlania na podstawie dlugosci. |
| `setText(...)` / `setFont(...)` | Ustawia surowy tekst i czcionke (gl�wnie dla niestandardowych tekst�w). |
| `isYell()` | Zwraca `true`, jesli tryb wiadomosci to krzyk. |
# # # Zaleznosci i powiazania
- **`thing.h`**: Klasa bazowa.
- **`framework/graphics/cachedtext.h`**: Uzywa `CachedText` do efektywnego renderowania tekstu.
- **`framework/core/timer.h`**: Uzywane do zarzadzania czasem zycia wiadomosci.

---
# ?? uimapanchorlayout.cpp
# # Og�lny opis
Implementacja `UIPositionAnchor` i `UIMapAnchorLayout`, kt�re rozszerzaja standardowy system kotwic (`UIAnchorLayout`) o mozliwosc przypinania widzet�w do konkretnych pozycji na minimapie.
# # Klasa `UIPositionAnchor`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `getHookedPoint(...)` | Kluczowa metoda, kt�ra oblicza wsp�lrzedna (X lub Y) na ekranie na podstawie `m_hookedPosition`. Pobiera `UIMinimap`, prosi go o prostokat (`Rect`) odpowiadajacy danemu polu na mapie (`getTileRect`), a nastepnie zwraca odpowiednia krawedz tego prostokata (np. `left`, `top`, `horizontalCenter`). |
# # Klasa `UIMapAnchorLayout`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `addPositionAnchor(...)` | Tworzy nowy obiekt `UIPositionAnchor` i dodaje go do grupy kotwic dla danego widzetu. |
| `centerInPosition(...)` | Funkcja pomocnicza, kt�ra dodaje dwie kotwice (`HorizontalCenter` i `VerticalCenter`), aby wysrodkowac widzet na danym polu mapy. |
| `fillPosition(...)` | Funkcja pomocnicza, kt�ra dodaje cztery kotwice (`Left`, `Right`, `Top`, `Bottom`), aby widzet wypelnil obszar danego pola na mapie. |
# # # Zaleznosci i powiazania
- **`uiminimap.h`**: `UIPositionAnchor` rzutuje widzet-rodzica na `UIMinimap`, aby uzyskac dostep do metody `getTileRect`.
- **`framework/ui/uiwidget.h`**: Wsp�lpracuje z widzetami.
- **`framework/ui/uianchorlayout.h`**: Rozszerza standardowy layout kotwic.

---
# ?? thing.h
# # Og�lny opis
Plik nagl�wkowy dla `Thing`, abstrakcyjnej klasy bazowej dla wszystkich obiekt�w, kt�re moga pojawic sie na mapie w grze.
# # Klasa `Thing`
# # # Opis
Dziedziczy po `LuaObject`. Definiuje wsp�lny interfejs dla przedmiot�w, stworzen, efekt�w, pocisk�w i tekst�w. Kazdy obiekt `Thing` ma pozycje i nalezy do okreslonego typu (`ThingType`).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Wirtualna metoda do rysowania obiektu. |
| `setPosition(const Position& position)` | Ustawia pozycje obiektu. |
| `getPosition()` | Zwraca pozycje obiektu. |
| `getStackPriority()` | Zwraca priorytet na stosie, kt�ry decyduje o kolejnosci rysowania i interakcji. |
| `getTile()` | Zwraca wskaznik do pola (`Tile`), na kt�rym znajduje sie obiekt. |
| `getStackPos()` | Zwraca pozycje obiektu na stosie wewnatrz pola. |
| `isItem()`, `isCreature()`, etc. | Wirtualne metody do identyfikacji typu obiektu. |
| `getThingType()` / `rawGetThingType()` | Zwracaja `ThingType` dla tego obiektu. |
| `getSize()`, `getWidth()`, `getHeight()`, etc. | Metody-skr�ty do wlasciwosci z `ThingType`. |
| `onPositionChange(...)`, `onAppear()`, `onDisappear()` | Wirtualne metody wywolywane w kluczowych momentach cyklu zycia obiektu. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w, np. `TilePtr`.
- **`thingtype.h`**: Kazdy `Thing` ma sw�j `ThingType`.
- **`framework/luaengine/luaobject.h`**: Klasa bazowa.

---
# ?? uiitem.h
# # Og�lny opis
Plik nagl�wkowy dla `UIItem`, widzetu interfejsu uzytkownika przeznaczonego do wyswietlania przedmiot�w (`Item`).
# # Klasa `UIItem`
# # # Opis
Dziedziczy po `UIWidget`. Sluzy do renderowania przedmiot�w w UI, np. w ekwipunku, kontenerach, oknach handlu.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje tlo, obraz, a nastepnie sam przedmiot (`m_item->draw(...)`), liczbe sztuk (jesli dotyczy) i ramke. |
| `setItemId(int id)` | Ustawia przedmiot do wyswietlenia na podstawie jego ID. |
| `setItemCount(int count)` | Ustawia liczbe sztuk przedmiotu. |
| `setItem(const ItemPtr& item)` | Ustawia przedmiot do wyswietlenia na podstawie istniejacego obiektu `Item`. |
| `setVirtual(bool virt)` | Oznacza, czy przedmiot jest "wirtualny" (nie jest prawdziwa instancja, tylko reprezentacja wizualna). |
| `setShowCount(bool value)` | Wlacza/wylacza wyswietlanie liczby sztuk. |
| `setItemShader(const std::string& str)` | Ustawia niestandardowy shader dla przedmiotu. |
| `getItem()` | Zwraca obiekt `Item` powiazany z widzetem. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.
- **`item.h`**: Przechowuje i rysuje obiekt `Item`.

---
# ?? thing.cpp
# # Og�lny opis
Implementacja klasy bazowej `Thing`. Zawiera podstawowa logike wsp�lna dla wszystkich obiekt�w na mapie.
# # Klasa `Thing`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setPosition(const Position& position)` | Aktualizuje pozycje obiektu i wywoluje wirtualna metode `onPositionChange`. |
| `getStackPriority()` | Zwraca priorytet obiektu na stosie wewnatrz pola. Kolejnosc jest scisle zdefiniowana: ziemia, obramowanie ziemi, obiekty na dole (np. sciany), obiekty na g�rze (np. dywany), stworzenia, a na koncu zwykle przedmioty. |
| `getTile()` | Zwraca wskaznik do pola, na kt�rym znajduje sie obiekt, uzywajac `g_map`. |
| `getParentContainer()` | Jesli obiekt znajduje sie w kontenerze, zwraca wskaznik do tego kontenera. Pozycja w kontenerze jest specjalnie kodowana. |
| `getStackPos()` | Zwraca pozycje na stosie: albo wewnatrz kontenera, albo na polu mapy. |
| `getThingType()` / `rawGetThingType()` | Zwracaja domyslny, "pusty" `ThingType`. Musza byc nadpisane przez klasy pochodne. |
| `updatedMarkedColor()` | Aktualizuje kolor i przezroczystosc znacznika (jesli jest ustawiony), tworzac efekt pulsowania. |
# # # Zaleznosci i powiazania
- **`spritemanager.h`**, **`thingtypemanager.h`**: Podstawowe zaleznosci.
- **`map.h`**: Do pobierania `Tile`.
- **`game.h`**: Do pobierania kontener�w.

---
# ?? uimap.cpp
# # Og�lny opis
Implementacja `UIMap`, widzetu interfejsu uzytkownika, kt�ry renderuje gl�wny widok mapy gry.
# # Klasa `UIMap`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Gl�wna funkcja rysujaca. Jest wywolywana trzykrotnie dla r�znych "warstw" (`DrawPane`): <br> 1. `MapBackgroundPane`: Rysuje tlo mapy (`m_mapView->drawMapBackground`). <br> 2. `MapForegroundPane`: Rysuje pierwszy plan (`m_mapView->drawMapForeground`). <br> 3. `ForegroundPane`: Rysuje obramowanie wok�l mapy. |
| `setZoom(int zoom)` | Ustawia poziom przyblizenia, co wplywa na `m_mapView->setVisibleDimension`. |
| `zoomIn()` / `zoomOut()` | Zmienia poziom przyblizenia o stala wartosc. |
| `setVisibleDimension(...)` | Ustawia widoczny wymiar w `m_mapView` i aktualizuje proporcje. |
| `setKeepAspectRatio(bool enable)` | Wlacza/wylacza zachowanie stalych proporcji widoku mapy. |
| `getPosition(const Point& mousePos)` | Konwertuje pozycje kursora na ekranie na pozycje (`Position`) w swiecie gry. |
| `getTile(const Point& mousePos)` | Zwraca pole (`Tile`) pod kursorem, przeszukujac widoczne pietra od g�ry do dolu w poszukiwaniu klikalnego obiektu. |
| `updateVisibleDimension()` | Przelicza i ustawia widoczny wymiar w `m_mapView` na podstawie aktualnego zoomu i proporcji. |
| `updateMapSize()` | Dopasowuje rozmiar i pozycje prostokata rysowania mapy (`m_mapRect`) do rozmiaru widzetu, zachowujac proporcje, jesli to wymagane. |
# # # Zaleznosci i powiazania
- **`game.h`**, **`map.h`**: Dostep do globalnych obiekt�w gry i mapy.
- **`mapview.h`**: `UIMap` jest "opakowaniem" dla `MapView`, przekazujac mu zadania renderowania.
- **`framework/otml/otml.h`**: Parsuje wlasciwosci z plik�w OTML, takie jak `multifloor` czy `animated`.

---
# ?? statictext.cpp
# # Og�lny opis
Implementacja `StaticText`, klasy odpowiedzialnej za wyswietlanie mowy postaci i innych tekst�w na mapie.
# # Klasa `StaticText`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawText(...)` | Rysuje tekst na ekranie, centrujac go i dopasowujac do prostokata nadrzednego. |
| `addMessage(...)` / `addColoredMessage(...)` | Dodaje nowa wiadomosc do kolejki. Jesli jest to pierwsza wiadomosc, ustawia tryb (np. `Say`, `Yell`) i nazwe m�wiacego. Jesli kolejne wiadomosci pasuja do poprzednich (ten sam m�wiacy i tryb), sa dodawane do kolejki. Oblicza czas wyswietlania na podstawie dlugosci tekstu. |
| `update()` | Metoda wywolywana po uplynieciu czasu wyswietlania wiadomosci. Usuwa najstarsza wiadomosc z kolejki. Jesli kolejka jest pusta, planuje usuniecie calego obiektu `StaticText` z mapy. |
| `scheduleUpdate()` | Planuje wywolanie `update()` po czasie r�wnym czasowi zycia najstarszej wiadomosci w kolejce. |
| `compose()` | Tworzy sformatowany tekst do wyswietlenia. Laczy wszystkie wiadomosci z kolejki, dodaje nagl�wki (np. "Player says:"), ustawia kolory i zawija tekst, jesli jest zbyt dlugi. |
# # # Logika dzialania
`StaticText` dziala jak kolejka FIFO dla wiadomosci. Kazda nowa wiadomosc jest dodawana na koniec. `compose` tworzy jeden ciagly, sformatowany tekst ze wszystkich wiadomosci w kolejce, kt�ry jest nastepnie rysowany przez `drawText`. `scheduleUpdate` i `update` zapewniaja, ze wiadomosci znikaja po okreslonym czasie, a caly obiekt jest usuwany, gdy nie ma juz nic do wyswietlenia.
# # # Zaleznosci i powiazania
- **`map.h`**: Uzywa `g_map` do usuniecia obiektu po zakonczeniu.
- **`framework/core/eventdispatcher.h`**: Uzywa `g_dispatcher` do planowania aktualizacji.
- **`framework/graphics/fontmanager.h`**: Uzywa `g_fonts` do zarzadzania czcionkami.

---
# ?? uiitem.cpp
# # Og�lny opis
Implementacja `UIItem`, widzetu do wyswietlania przedmiot�w w interfejsie uzytkownika.
# # Klasa `UIItem`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widzet. Renderuje tlo, obraz, a nastepnie sam przedmiot (`m_item->draw(...)`), uzywajac prostokata `getPaddingRect()`. Jesli `m_showCount` jest wlaczone, rysuje r�wniez liczbe przedmiot�w w prawym dolnym rogu. |
| `setItemId(int id)` | Tworzy nowy obiekt `Item` (jesli go nie bylo) lub aktualizuje ID istniejacego. |
| `setItemCount(int count)` | Ustawia liczbe przedmiot�w i aktualizuje tekst licznika. |
| `setItem(const ItemPtr& item)` | Ustawia przedmiot na podstawie gotowego obiektu `ItemPtr`. |
| `setItemShader(const std::string& str)` | Ustawia niestandardowy shader dla renderowanego przedmiotu. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `item-id`, `item-count`, `virtual`. |
| `cacheCountText()` | Formatuje tekst licznika. Dla liczb >= 1000 uzywa skr�tu "k" (np. "1.2k"), jesli funkcja `GameCountU16` jest aktywna. |
# # # Zaleznosci i powiazania
- **`spritemanager.h`**: Uzywany przez `Item` do pobierania sprite'�w.
- **`game.h`**: Sprawdza `GameFeature`, np. `GameCountU16`.
- **`framework/otml/otml.h`**: Do parsowania styl�w.
- **`framework/graphics/graphics.h`**: Do operacji rysowania.

---
# ?? thingstype.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `ThingsType` (blad w nazwie, prawdopodobnie powinno byc `ThingTypeManager`). Definiuje interfejs singletonu, kt�ry zarzadza wszystkimi typami obiekt�w (`ThingType`) w grze, wczytywanymi z plik�w `.dat`.

> NOTE: Nazwa klasy `ThingsType` jest mylaca. W rzeczywistosci jest to menedzer, kt�ry przechowuje i zarzadza obiektami `ThingType`. W innych plikach jest on nazywany `ThingTypeManager`.
# # Klasa `ThingsType`
# # # Typy wyliczeniowe
- **`Categories`**: Kategorie obiekt�w (Przedmiot, Stworzenie, Efekt, Pocisk).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `load(const std::string& file)` | Wczytuje i parsuje plik `.dat`. |
| `unload()` | Zwalnia zaladowane dane. |
| `parseThingType(...)` | Parsuje dane pojedynczego typu obiektu ze strumienia pliku. |
| `getEmptyThingType()` | Zwraca pusty, domyslny obiekt `ThingType`. |
| `getThingType(uint16 id, Categories category)` | Zwraca `ThingType` dla danego ID i kategorii. |
| `getSignature()` | Zwraca sygnature wczytanego pliku `.dat`. |
| `isLoaded()` | Zwraca `true`, jesli plik `.dat` jest zaladowany. |
| `isValidItemId(int id)` | Sprawdza, czy ID przedmiotu jest w prawidlowym zakresie. |
# # # Zmienne globalne
- **`ThingsType g_thingsType`**: Globalna instancja managera (p�zniej w kodzie uzywane jest `g_things`).
# # # Zaleznosci i powiazania
- **`thingtype.h`**: Zarzadza obiektami `ThingType`.
- **`framework/core/declarations.h`**: Podstawowe deklaracje.

---
# ?? uigraph.h
# # Og�lny opis
Plik nagl�wkowy dla `UIGraph`, widzetu sluzacego do rysowania prostych wykres�w liniowych.
# # Klasa `UIGraph`
# # # Opis
Dziedziczy po `UIWidget`. Przechowuje kolejke wartosci i renderuje je jako wykres liniowy.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje wykres. Oblicza skale, przygotowuje punkty i rysuje linie za pomoca `g_drawQueue->addLine`. |
| `clear()` | Czysci wszystkie wartosci z wykresu. |
| `addValue(int value, ...)` | Dodaje nowa wartosc do wykresu. Jesli liczba wartosci przekroczy pojemnosc, najstarsza jest usuwana. |
| `setLineWidth(int width)` | Ustawia grubosc linii wykresu. |
| `setCapacity(int capacity)` | Ustawia maksymalna liczbe wartosci przechowywanych przez wykres. |
| `setTitle(const std::string& title)` | Ustawia tytul wyswietlany nad wykresem. |
| `setShowLabels(bool value)` | Wlacza/wylacza wyswietlanie etykiet (wartosc min, max, aktualna). |
# # # Zaleznosci i powiazania
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# ?? uicreature.h
# # Og�lny opis
Plik nagl�wkowy dla `UICreature`, widzetu interfejsu uzytkownika do wyswietlania stworzen.
# # Klasa `UICreature`
# # # Opis
Dziedziczy po `UIWidget`. Umozliwia renderowanie postaci (jej ubioru) w elementach UI, takich jak okno ekwipunku, battle list, czy okno wyboru stroju.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje postac za pomoca `m_creature->drawOutfit(...)`. Obsluguje automatyczne obracanie postaci, jesli jest wlaczone. |
| `setCreature(const CreaturePtr& creature)` | Ustawia stworzenie do wyswietlenia. |
| `setFixedCreatureSize(bool fixed)` | Ustawia, czy rozmiar renderowanej postaci ma byc staly, czy skalowany do rozmiaru widzetu. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubi�r do wyswietlenia. Jesli nie ma przypisanego stworzenia, tworzy nowe. |
| `setAutoRotating(bool value)` | Wlacza/wylacza automatyczne obracanie sie postaci. |
| `setDirection(Otc::Direction direction)` | Ustawia staly kierunek, w kt�rym postac jest zwr�cona. |
| `setScale(float scale)` | Ustawia skale rysowania postaci. |
| `setAnimate(bool value)` | Wlacza/wylacza animacje postaci. |
| `setCenter(bool value)` | Wlacza/wylacza centrowanie outfitu. |
| `setOldScaling(bool value)` | Uzywa starego algorytmu skalowania. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.
- **`creature.h`**: Przechowuje i rysuje obiekt `Creature`.

---
# ?? thingtype.cpp
# # Og�lny opis
Implementacja klasy `ThingType`, kt�ra reprezentuje szablon dla wszystkich obiekt�w w grze. Plik zawiera logike serializacji, deserializacji, a przede wszystkim renderowania obiekt�w danego typu.
# # Klasa `ThingType`
# # # Metody
# # # # Serializacja / Deserializacja
| Nazwa | Opis |
| --- | --- |
| `serialize(...)` | Zapisuje atrybuty `ThingType` do strumienia binarnego, zgodnie z formatem plik�w `.dat`. |
| `unserialize(...)` | Wczytuje atrybuty `ThingType` ze strumienia. Zawiera zlozona logike do obslugi r�znic w formatach `.dat` miedzy r�znymi wersjami klienta Tibii, mapujac stare atrybuty na nowe. |
| `unserializeOtml(...)` | Wczytuje dodatkowe, niestandardowe atrybuty z plik�w OTML, takie jak przezroczystosc czy niestandardowe obrazy. |
# # # # Rysowanie
| Nazwa | Opis |
| --- | --- |
| `draw(...)` | Gl�wna metoda rysujaca. Pobiera teksture dla danej fazy animacji, oblicza, kt�ry jej fragment (`Rect`) odpowiada danemu wzorowi (pattern) i warstwie, a nastepnie dodaje go do kolejki rysowania. |
| `drawOutfit(...)` | Specjalna wersja do rysowania ubior�w, kt�ra zwraca parametry potrzebne do renderowania z dynamicznym kolorowaniem przez `DrawQueueItemOutfit`. |
| `drawWithShader(...)` | Wersja rysujaca z uzyciem niestandardowego shadera. |
# # # # Zarzadzanie teksturami
| Nazwa | Opis |
| --- | --- |
| `getTexture(int animationPhase)` | Zwraca teksture dla danej fazy animacji. Jesli tekstura nie zostala jeszcze utworzona, generuje ja "w locie": <br> 1. Tworzy duzy obraz (atlas). <br> 2. Sklada go z pojedynczych sprite'�w pobranych z `g_sprites`. <br> 3. Tworzy z niego obiekt `Texture` i przechowuje go w pamieci podrecznej. <br> 4. Zapisuje r�wniez prostokaty (`Rect`) i przesuniecia dla kazdej klatki na tej teksturze. |
| `unload()` | Zwalnia wygenerowane tekstury z pamieci, aby oszczedzac zasoby. Sa one ponownie generowane przy nastepnym uzyciu. |
| `getBestTextureDimension(...)` | Oblicza optymalny rozmiar tekstury-atlasu, aby pomiescic wszystkie klatki animacji. |
# # # Zaleznosci i powiazania
- **`spritemanager.h`**: Uzywa `g_sprites` do pobierania obraz�w pojedynczych sprite'�w.
- **`game.h`**: Sprawdza `GameFeature`, co wplywa na logike deserializacji i animacji.
- **`lightview.h`**: Przekazuje `LightView` do dodawania swiatla, jesli obiekt je emituje.
- **`framework/graphics/...`**: Intensywnie korzysta z klas `Texture`, `Image`, `Painter` i `DrawQueue`.

---
# ?? towns.h
# # Og�lny opis
Plik nagl�wkowy definiujacy klasy `Town` i `TownManager` do zarzadzania miastami w grze.
# # Klasa `Town`
# # # Opis
Prosta klasa przechowujaca dane o pojedynczym miescie: ID, nazwe i pozycje (zazwyczaj swiatyni).
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setId(uint32 tid)` | Ustawia ID miasta. |
| `setName(const std::string& name)` | Ustawia nazwe miasta. |
| `setPos(const Position& pos)` | Ustawia pozycje miasta. |
| `getId()` / `getName()` / `getPos()` | Zwracaja odpowiednie wlasciwosci. |
# # Klasa `TownManager`
# # # Opis
Singleton (`g_towns`) zarzadzajacy kolekcja wszystkich miast.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `addTown(const TownPtr& town)` | Dodaje miasto do listy. |
| `removeTown(uint32 townId)` | Usuwa miasto po ID. |
| `getTown(uint32 townId)` | Zwraca miasto po ID. |
| `getTownByName(std::string name)` | Zwraca miasto po nazwie. |
| `sort()` | Sortuje liste miast alfabetycznie. |
| `getTowns()` | Zwraca liste wszystkich miast. |
| `clear()` | Czysci liste miast. |
# # # Zmienne globalne
- **`TownManager g_towns`**: Globalna instancja managera miast.
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w, np. `TownPtr`, `Position`.

---
# ?? thingtype.h
# # Og�lny opis
Plik nagl�wkowy dla klasy `ThingType`, kt�ra jest szablonem dla wszystkich obiekt�w w grze. Definiuje ona ich wsp�lne, niezmienne wlasciwosci.
# # Klasa `ThingType`
# # # Opis
Dziedziczy po `LuaObject`. Przechowuje dane wczytane z plik�w `.dat` i `.otml`, takie jak wymiary, wzory, animacje, atrybuty (np. czy jest blokujacy, czy swieci). Wszystkie instancje `Thing` o tym samym ID wsp�ldziela jeden obiekt `ThingType`.
# # # Typy wyliczeniowe
- **`ThingCategory`**: Kategorie obiekt�w (przedmiot, stworzenie, etc.).
- **`ThingAttr`**: Atrybuty obiektu (np. `ThingAttrGround`, `ThingAttrNotWalkable`).
# # # Struktury
- **`MarketData`**: Dane rynkowe przedmiotu.
- **`Light`**: Parametry emitowanego swiatla.
- **`DrawOutfitParams`**: Parametry potrzebne do narysowania ubioru.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `unserialize(...)` | Wczytuje dane z binarnego formatu `.dat`. |
| `unserializeOtml(...)` | Wczytuje dodatkowe dane z formatu `.otml`. |
| `draw(...)` | Renderuje obiekt. |
| `drawOutfit(...)` | Specjalna funkcja do renderowania ubior�w. |
| `getId()` | Zwraca ID klienta. |
| `getCategory()` | Zwraca kategorie. |
| `getSize()`, `getWidth()`, `getHeight()` | Zwracaja wymiary w jednostkach p�l. |
| `getAnimationPhases()` | Zwraca liczbe klatek animacji. |
| `getAnimator()` | Zwraca animator, jesli jest dostepny. |
| `hasAttr(ThingAttr attr)` | Sprawdza, czy obiekt posiada dany atrybut. |
| `isGround()`, `isNotWalkable()`, etc. | Funkcje pomocnicze sprawdzajace konkretne atrybuty. |
# # # Zaleznosci i powiazania
- **`animator.h`**: Moze posiadac `Animator` do zarzadzania animacjami.
- **`framework/graphics/...`**: Uzywa `Texture`, `DrawQueue` do renderowania.
- **`framework/luaengine/luaobject.h`**: Klasa bazowa.

---
# ?? uicreature.cpp
# # Og�lny opis
Implementacja `UICreature`, widzetu do wyswietlania stworzen w interfejsie uzytkownika.
# # Klasa `UICreature`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widzet. Jesli przypisano stworzenie (`m_creature`), wywoluje jego metode `drawOutfit`, aby narysowac jego wyglad w prostokacie widzetu. Obsluguje automatyczne obracanie postaci, jesli opcja `m_autoRotating` jest wlaczona. |
| `setOutfit(const Outfit& outfit)` | Ustawia ubi�r do wyswietlenia. Jesli widzet nie ma jeszcze przypisanego obiektu `Creature`, tworzy nowa, pusta instancje. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `outfit-id`, `outfit-head`, `outfit-body` itp., i na ich podstawie konfiguruje wyswietlany ubi�r. |
| `setCenter(bool value)` | Ustawia flage centrowania w obiekcie `Outfit`, co wplywa na spos�b jego rysowania. |
# # # Zaleznosci i powiazania
- **`spritemanager.h`**: Uzywane przez `Creature::drawOutfit`.
- **`framework/otml/otml.h`**: Do parsowania styl�w.
- **`framework/graphics/drawqueue.h`**: Do dodawania operacji rysowania.

---
# ?? thingtypemanager.h
# # Og�lny opis
Plik nagl�wkowy dla `ThingTypeManager`, singletonu zarzadzajacego wszystkimi typami obiekt�w (`ThingType`) i przedmiot�w (`ItemType`).
# # Klasa `ThingTypeManager`
# # # Opis
Centralne repozytorium dla definicji wszystkich obiekt�w w grze. Odpowiada za wczytywanie plik�w `.dat`, `.otb` i `.xml`, kt�re zawieraja te definicje, oraz za dostarczanie ich na zadanie.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `init()` / `terminate()` | Inicjalizacja i zamykanie managera. |
| `check()` | Okresowo wywolywana metoda, kt�ra zwalnia z pamieci tekstury nieuzywanych `ThingType`, aby oszczedzac zasoby. |
| `loadDat(...)`, `loadOtml(...)`, `loadOtb(...)`, `loadXml(...)` | Metody do wczytywania r�znych format�w plik�w z danymi o obiektach. |
| `getThingType(id, category)` | Zwraca `ThingType` dla danego ID klienta i kategorii. |
| `getItemType(id)` | Zwraca `ItemType` dla danego ID serwera (OTB). |
| `findItemTypeByClientId(id)` | Wyszukuje `ItemType` po jego ID klienta. |
| `findItemTypeByName(name)` | Wyszukuje `ItemType` po nazwie. |
| `isDatLoaded()`, `isOtbLoaded()` | Sprawdzaja, czy odpowiednie pliki zostaly zaladowane. |
| `getDatSignature()` | Zwraca sygnature pliku `.dat`. |
# # # Zmienne globalne
- **`ThingTypeManager g_things`**: Globalna instancja managera.
# # # Zaleznosci i powiazania
- **`thingtype.h`**, **`itemtype.h`**: Zarzadza obiektami tych klas.
- Jest to jedna z najbardziej fundamentalnych klas w kliencie, uzywana przez niemal kazdy modul, kt�ry ma do czynienia z obiektami w grze.

---
# ?? uigraph.cpp
# # Og�lny opis
Implementacja `UIGraph`, widzetu do rysowania wykres�w liniowych.
# # Klasa `UIGraph`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje wykres. Oblicza minimalna i maksymalna wartosc w widocznym zakresie, aby przeskalowac wykres do wysokosci widzetu. Nastepnie tworzy liste punkt�w i rysuje miedzy nimi linie za pomoca `g_drawQueue->addLine`. Rysuje r�wniez tytul i etykiety (min, max, aktualna wartosc), jesli sa wlaczone. |
| `clear()` | Czysci wszystkie dane z wykresu. |
| `addValue(int value, ...)` | Dodaje nowa wartosc do kolejki `m_values`. Jesli kolejka przekroczy pojemnosc (`m_capacity`), najstarsza wartosc jest usuwana. Opcjonalnie ignoruje male, powtarzajace sie wartosci, aby uniknac "szumu" na wykresie. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `line-width`, `capacity`, `title`. |
# # # Zaleznosci i powiazania
- **`framework/graphics/drawqueue.h`**: Do rysowania linii i tekstu.
- **`framework/otml/otml.h`**: Do parsowania styl�w.

---
# ?? uimap.h
# # Og�lny opis
Plik nagl�wkowy dla `UIMap`, widzetu UI, kt�ry jest odpowiedzialny za wyswietlanie mapy gry.
# # Klasa `UIMap`
# # # Opis
Dziedziczy po `UIWidget`. Dziala jako "okno" na swiat gry, wykorzystujac `MapView` do faktycznego renderowania. Umozliwia interakcje z mapa, taka jak przesuwanie, przyblizanie i pobieranie informacji o tym, co znajduje sie pod kursorem.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje mape w trzech przejsciach (tlo, pierwszy plan, interfejs). |
| `movePixels(int x, int y)` | Przesuwa widok kamery o zadana liczbe pikseli. |
| `setZoom(int zoom)` / `zoomIn()` / `zoomOut()` | Zarzadza poziomem przyblizenia mapy. |
| `followCreature(...)` | Ustawia kamere, aby podazala za stworzeniem. |
| `setCameraPosition(...)` | Ustawia kamere na stala pozycje. |
| `getPosition(const Point& mousePos)` | Zwraca pozycje na mapie (`Position`) odpowiadajaca danym wsp�lrzednym myszy na widzecie. |
| `getTile(const Point& mousePos)` | Zwraca `Tile` pod kursorem. |
| `setKeepAspectRatio(bool enable)` | Wlacza/wylacza zachowanie stalych proporcji mapy. |
| `setVisibleDimension(...)` | Ustawia rozmiar widocznego obszaru mapy w polach. |
# # # Zaleznosci i powiazania
- **`mapview.h`**: Uzywa `MapView` do renderowania.
- **`tile.h`**: Metoda `getTile` zwraca obiekt `Tile`.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# ?? uiminimap.cpp
# # Og�lny opis
Implementacja `UIMinimap`, widzetu interfejsu uzytkownika do wyswietlania minimapy.
# # Klasa `UIMinimap`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widzet. Wywoluje `g_minimap.draw`, przekazujac prostokat widzetu, pozycje kamery i skale, aby narysowac odpowiedni fragment minimapy. |
| `setZoom(int zoom)` | Ustawia poziom przyblizenia minimapy. Wartosc zoom jest konwertowana na wsp�lczynnik skali (`m_scale`). |
| `setCameraPosition(const Position& pos)` | Ustawia centralna pozycje, wok�l kt�rej rysowana jest minimapa. |
| `floorUp()` / `floorDown()` | Zmienia aktualnie wyswietlane pietro. |
| `getTilePoint(...)` / `getTilePosition(...)` | Konwertuja pozycje na mapie na wsp�lrzedne na widzecie i odwrotnie. |
| `anchorPosition(...)` / `fillPosition(...)` / `centerInPosition(...)` | Metody do przypinania innych widzet�w do konkretnych pozycji na minimapie za pomoca `UIMapAnchorLayout`. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `zoom`, `min-zoom`, `max-zoom`. |
# # # Zaleznosci i powiazania
- **`minimap.h`**: Uzywa `g_minimap` do renderowania danych.
- **`uimapanchorlayout.h`**: Posiada `UIMapAnchorLayout` do zarzadzania przypietymi widzetami.
- **`game.h`**: Dostep do globalnych obiekt�w.

---
# ?? uiprogressrect.cpp
# # Og�lny opis
Implementacja `UIProgressRect`, niestandardowego widzetu, kt�ry wizualizuje postep za pomoca wypelniajacego sie okregu (lub kwadratu) w spos�b radialny.
# # Klasa `UIProgressRect`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widzet. Zamiast standardowego paska postepu, rysuje serie tr�jkat�w, kt�rych wierzcholki rozchodza sie od srodka prostokata, tworzac efekt radialnego wypelnienia. Wypelnienie jest podzielone na 4 cwiartki, a kazda z nich na dwa segmenty, co daje 8 krok�w animacji. |
| `setPercent(float percent)` | Ustawia procent wypelnienia (od 0.0 do 100.0). |
| `onStyleApply(...)` | Parsuje atrybut `percent` z OTML. |
# # # Logika rysowania
Wypelnienie jest realizowane przez rysowanie tr�jkat�w. Kazdy tr�jkat ma jeden wierzcholek w srodku prostokata, a dwa pozostale na jego krawedziach. W miare wzrostu `m_percent`, kolejne tr�jkaty sa rysowane, tworzac iluzje plynnego, okreznego wypelnienia.
# # # Zaleznosci i powiazania
- **`framework/otml/otml.h`**: Do parsowania styl�w.
- **`framework/graphics/graphics.h`**: Do operacji rysowania.

---
# ?? uimapanchorlayout.h
# # Og�lny opis
Plik nagl�wkowy definiujacy `UIPositionAnchor` i `UIMapAnchorLayout`. Rozszerzaja one standardowy system kotwic o mozliwosc przypinania widzet�w do dynamicznych pozycji na `UIMinimap`.
# # Klasa `UIPositionAnchor`
# # # Opis
Dziedziczy po `UIAnchor`. Zamiast przypinac sie do krawedzi innego widzetu, przypina sie do pozycji (`Position`) na mapie.
-   `m_hookedPosition`: Pozycja na mapie, do kt�rej kotwica jest przypieta.
# # # Metody
-   **`getHookedPoint(...)`**: Nadpisana metoda, kt�ra oblicza pozycje na ekranie, pobierajac z `UIMinimap` prostokat odpowiadajacy `m_hookedPosition`.
# # Klasa `UIMapAnchorLayout`
# # # Opis
Dziedziczy po `UIAnchorLayout`. Specjalizuje layout kotwic do pracy z `UIMinimap`.
# # # Metody
-   **`addPositionAnchor(...)`**: Dodaje kotwice typu `UIPositionAnchor`.
-   **`centerInPosition(...)`**, **`fillPosition(...)`**: Funkcje pomocnicze do latwego centrowania lub wypelniania obszaru pola na mapie przez inny widzet.
# # # Zaleznosci i powiazania
- **`framework/ui/uianchorlayout.h`**: Klasa bazowa.
- **`uiminimap.h`**: Layout jest przeznaczony do uzycia z `UIMinimap`.

---
# ?? uiminimap.h
# # Og�lny opis
Plik nagl�wkowy dla `UIMinimap`, widzetu do wyswietlania minimapy.
# # Klasa `UIMinimap`
# # # Opis
Dziedziczy po `UIWidget`. Renderuje dane z `Minimap` i pozwala na interakcje, takie jak zmiana pietra czy przyblizenia. Posiada r�wniez `UIMapAnchorLayout` do pozycjonowania innych widzet�w wzgledem pozycji na minimapie.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `zoomIn()` / `zoomOut()` / `setZoom(int zoom)` | Zarzadzaja poziomem przyblizenia. |
| `setCameraPosition(const Position& pos)` | Ustawia pozycje, kt�ra ma byc w centrum minimapy. |
| `floorUp()` / `floorDown()` | Zmienia wyswietlane pietro. |
| `getTilePoint(...)` / `getTileRect(...)` | Zwracaja wsp�lrzedne ekranowe dla danego pola na mapie. |
| `getTilePosition(...)` | Konwertuje wsp�lrzedne ekranowe na pozycje na mapie. |
| `anchorPosition(...)` | Przypina inny widzet do pozycji na minimapie. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# ?? uiprogressrect.h
# # Og�lny opis
Plik nagl�wkowy dla `UIProgressRect`, widzetu do wyswietlania paska postepu w formie radialnej.
# # Klasa `UIProgressRect`
# # # Opis
Dziedziczy po `UIWidget`. Zamiast typowego paska, rysuje wypelnienie w spos�b okrezny.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(...)` | Rysuje widzet. |
| `setPercent(float percent)` | Ustawia procent postepu (0-100). |
| `getPercent()` | Zwraca aktualny procent. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# ?? uisprite.cpp
# # Og�lny opis
Implementacja `UISprite`, widzetu do wyswietlania pojedynczego sprite'a z plik�w `.spr`.
# # Klasa `UISprite`
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `drawSelf(Fw::DrawPane drawPane)` | Rysuje widzet. Jesli `m_sprite` jest zaladowany, rysuje go wewnatrz prostokata widzetu z uwzglednieniem paddingu. |
| `setSpriteId(uint32 id)` | Ustawia ID sprite'a do wyswietlenia. Pobiera obraz z `g_sprites`, a nastepnie tworzy z niego teksture. |
| `onStyleApply(...)` | Parsuje niestandardowe atrybuty z OTML, takie jak `sprite-id`, `sprite-color`. |
# # # Zaleznosci i powiazania
- **`spritemanager.h`**: Uzywa `g_sprites` do pobierania obraz�w sprite'�w.
- **`framework/otml/otml.h`**: Do parsowania styl�w.
- **`framework/graphics/graphics.h`**: Do operacji rysowania i zarzadzania teksturami.

---
# ?? uisprite.h
# # Og�lny opis
Plik nagl�wkowy dla `UISprite`, widzetu do wyswietlania pojedynczego sprite'a.
# # Klasa `UISprite`
# # # Opis
Dziedziczy po `UIWidget`. Prosty widzet, kt�rego jedynym celem jest wyswietlenie obrazu sprite'a o danym ID.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `setSpriteId(uint32 id)` | Ustawia ID sprite'a do wyswietlenia. |
| `getSpriteId()` | Zwraca ID sprite'a. |
| `setSpriteColor(Color color)` | Ustawia kolor, w jakim sprite ma byc renderowany. |
| `hasSprite()` | Zwraca `true`, jesli sprite jest zaladowany. |
# # # Zaleznosci i powiazania
- **`declarations.h`**: Definicje typ�w.
- **`framework/ui/uiwidget.h`**: Klasa bazowa.

---
# ?? walkmatrix.h
# # Og�lny opis
Plik nagl�wkowy definiujacy klase `WalkMatrix`, kt�ra jest uzywana do sledzenia i zarzadzania predykcjami krok�w lokalnego gracza w nowym systemie chodzenia (`GameNewWalking`).
# # Klasa `WalkMatrix`
# # # Opis
Jest to macierz 7x7, kt�ra przechowuje wartosci (liczniki lub ID predykcji) dla p�l w zasiegu 3x3 wok�l aktualnej pozycji gracza. Sluzy do synchronizacji krok�w miedzy klientem a serwerem.
# # # Metody
| Nazwa | Opis |
| --- | --- |
| `updatePosition(const Position& newPos)` | Aktualizuje wewnetrzna pozycje gracza i przesuwa zawartosc macierzy, aby odzwierciedlic ruch. Stare, odlegle wartosci sa zerowane. |
| `inRange(const Position& pos2)` | Sprawdza, czy dana pozycja miesci sie w zasiegu macierzy (3x3 wok�l gracza). |
| `update(const Position& pos2, int32_t value)` | Ustawia wartosc w macierzy dla danej pozycji. Jesli `value` nie jest podane, uzywa inkrementowanego licznika. Zwraca ustawiona wartosc, kt�ra sluzy jako ID predykcji. |
| `get(const Position& pos2)` | Zwraca wartosc z macierzy dla danej pozycji. |
| `clear()` | Zeruje cala macierz. |
| `reset(uint32_t value)` | Wypelnia cala macierz dana wartoscia. |
| `dump()` | Zwraca tekstowa reprezentacje macierzy do cel�w debugowania. |
# # # Zaleznosci i powiazania
- **`position.h`**: Uzywa `Position` do operacji na wsp�lrzednych.
- **`localplayer.cpp`**: Obiekt `WalkMatrix` jest polem klasy `LocalPlayer` i jest uzywany w logice pre-walkingu.

---
# ?? protocolgameparse.cpp
# # Og�lny opis
Plik ten zawiera implementacje metod klasy `ProtocolGame` odpowiedzialnych za **parsowanie** pakiet�w przychodzacych z serwera gry. Jest to serce logiki sieciowej po stronie klienta.
# # Klasa `ProtocolGame`
# # # Metody
# # # # `parseMessage(const InputMessagePtr& msg)`
Gl�wna funkcja-dyspozytor. Odczytuje jednobajtowy kod operacyjny (opcode) z wiadomosci, a nastepnie wywoluje odpowiednia metode `parse...` do przetworzenia reszty pakietu. Obsluguje r�wniez niestandardowe opkody i przekazywanie ich do Lua.
# # # # Metody `parse...`
Kazda metoda `parse...` jest odpowiedzialna za odczytanie danych z `InputMessage` dla konkretnego opkodu i zaktualizowanie stanu gry. Przyklady:
- **`parseMapDescription(...)`**: Parsuje pelny opis widocznego obszaru mapy, tworzac pola i obiekty.
- **`parseTileAddThing(...)`**: Dodaje nowy obiekt na mape.
- **`parseCreatureMove(...)`**: Aktualizuje pozycje stworzenia na mapie.
- **`parseCreatureHealth(...)`**: Aktualizuje procent zycia stworzenia.
- **`parseTalk(...)`**: Przetwarza wiadomosc czatu i przekazuje ja do `g_game`.
- **`parseOpenContainer(...)`**: Tworzy nowy kontener i wypelnia go przedmiotami.
- **`parsePlayerStats(...)`**: Aktualizuje statystyki lokalnego gracza.
- **`parseCancelWalk(...)`**: Informuje `g_game` o anulowaniu kroku.
# # # # Metody pomocnicze `get...`
- **`getThing(...)`**, **`getItem(...)`**, **`getCreature(...)`**, **`getPosition(...)`**: Funkcje pomocnicze, kt�re odczytuja zlozone typy danych (jak `Item` czy `Creature`) z `InputMessage`, uwzgledniajac r�znice w formacie zalezne od `GameFeature`. `getCreature`, na przyklad, decyduje, czy stworzyc nowy obiekt `Creature`, czy zaktualizowac istniejacy.
# # # Zaleznosci i powiazania
- **`game.h`**, **`map.h`**, **`localplayer.h`**: Scisle wsp�lpracuje z tymi klasami, wywolujac ich metody w celu aktualizacji stanu gry.
- **`thingtypemanager.h`**: Uzywa `g_things` do weryfikacji ID przedmiot�w i efekt�w.
- **`luavaluecasts_client.h`**: Uzywane do przekazywania zlozonych obiekt�w do Lua.
- **`protocolcodes.h`**: Uzywa zdefiniowanych tam kod�w operacyjnych.

---
# ?? Spis tresci

- [?? animatedtext.cpp](#-animatedtextcpp)
  - [Klasa `AnimatedText`](#-klasa-animatedtext)
- [?? houses.h](#-housesh)
  - [Klasa `House`](#-klasa-house)
  - [Klasa `HouseManager`](#-klasa-housemanager)
- [?? animatedtext.h](#-animatedtexth)
  - [Klasa `AnimatedText`](#-klasa-animatedtext-1)
- [?? animator.h](#-animatorh)
  - [Klasa `Animator`](#-klasa-animator)
- [?? animator.cpp](#-animatorcpp)
  - [Klasa `Animator`](#-klasa-animator-1)
- [?? client.cpp](#-clientcpp)
  - [Klasa `Client`](#-klasa-client)
- [?? client.h](#-clienth)
  - [Klasa `Client`](#-klasa-client-1)
- [?? CMakeLists.txt](#-cmakeliststxt)
- [?? const.h](#-consth)
  - [Namespace `Otc`](#-namespace-otc)
- [?? container.cpp](#-containercpp)
  - [Klasa `Container`](#-klasa-container)
- [?? creature.cpp](#-creaturecpp)
  - [Klasa `Creature`](#-klasa-creature)
- [?? container.h](#-containerh)
  - [Klasa `Container`](#-klasa-container-1)
- [?? creature.h](#-creatureh)
  - [Klasa `Creature`](#-klasa-creature-1)
  - [Klasa `Npc`](#-klasa-npc)
  - [Klasa `Monster`](#-klasa-monster)
- [?? creatures.h](#-creaturesh)
  - [Klasa `Spawn`](#-klasa-spawn)
  - [Klasa `CreatureType`](#-klasa-creaturetype)
  - [Klasa `CreatureManager`](#-klasa-creaturemanager)
- [?? declarations.h](#-declarationsh)
- [?? creatures.cpp](#-creaturescpp)
  - [Klasa `Spawn`](#-klasa-spawn-1)
  - [Klasa `CreatureType`](#-klasa-creaturetype-1)
  - [Klasa `CreatureManager`](#-klasa-creaturemanager-1)
- [?? effect.cpp](#-effectcpp)
  - [Klasa `Effect`](#-klasa-effect)
- [?? global.h](#-globalh)
- [?? effect.h](#-effecth)
  - [Klasa `Effect`](#-klasa-effect-1)
- [?? healthbars.cpp](#-healthbarscpp)
  - [Klasa `HealthBars`](#-klasa-healthbars)
  - [Klasa `HealthBar`](#-klasa-healthbar)
- [?? game.h](#-gameh)
  - [Klasa `Game`](#-klasa-game)
- [?? healthbars.h](#-healthbarsh)
  - [Klasa `HealthBar`](#-klasa-healthbar-1)
  - [Klasa `HealthBars`](#-klasa-healthbars-1)
- [?? houses.cpp](#-housescpp)
  - [Klasa `House`](#-klasa-house-1)
  - [Klasa `HouseManager`](#-klasa-housemanager-1)
- [?? item.cpp](#-itemcpp)
  - [Klasa `Item`](#-klasa-item)
- [?? itemtype.cpp](#-itemtypecpp)
  - [Klasa `ItemType`](#-klasa-itemtype)
- [?? item.h](#-itemh)
  - [Klasa `Item`](#-klasa-item-1)
- [?? itemtype.h](#-itemtypeh)
  - [Klasa `ItemType`](#-klasa-itemtype-1)
- [?? lightview.cpp](#-lightviewcpp)
  - [Klasa `LightView`](#-klasa-lightview)
- [?? lightview.h](#-lightviewh)
  - [Klasa `LightView`](#-klasa-lightview-1)
- [?? localplayer.cpp](#-localplayercpp)
  - [Klasa `LocalPlayer`](#-klasa-localplayer)
- [?? map.cpp](#-mapcpp)
  - [Klasa `Map`](#-klasa-map)
- [?? map.h](#-maph)
  - [Klasa `Map`](#-klasa-map-1)
- [?? luavaluecasts_client.h](#-luavaluecasts_clienth)
- [?? mapio.cpp](#-mapiocpp)
  - [Klasa `Map`](#-klasa-map-2)
- [?? luavaluecasts_client.cpp](#-luavaluecasts_clientcpp)
- [?? mapview.cpp](#-mapviewcpp)
  - [Klasa `MapView`](#-klasa-mapview)
- [?? mapview.h](#-mapviewh)
  - [Klasa `MapView`](#-klasa-mapview-1)
- [?? minimap.h](#-minimaph)
  - [Klasa `MinimapBlock`](#-klasa-minimapblock)
  - [Klasa `Minimap`](#-klasa-minimap)
- [?? missile.cpp](#-missilecpp)
  - [Klasa `Missile`](#-klasa-missile)
- [?? missile.h](#-missileh)
  - [Klasa `Missile`](#-klasa-missile-1)
- [?? outfit.cpp](#-outfitcpp)
  - [Klasa `Outfit`](#-klasa-outfit)
- [?? outfit.h](#-outfith)
  - [Klasa `Outfit`](#-klasa-outfit-1)
- [?? player.cpp](#-playercpp)
  - [Klasa `Player`](#-klasa-player)
- [?? player.h](#-playerh)
  - [Klasa `Player`](#-klasa-player-1)
- [?? protocolcodes.cpp](#-protocolcodescpp)
  - [Namespace `Proto`](#-namespace-proto)
- [?? minimap.cpp](#-minimapcpp)
  - [Klasa `MinimapBlock`](#-klasa-minimapblock-1)
  - [Klasa `Minimap`](#-klasa-minimap-1)
- [?? position.h](#-positionh)
  - [Struktura `Position`](#-struktura-position)
  - [Struktura `PositionHasher`](#-struktura-positionhasher)
- [?? protocolcodes.h](#-protocolcodesh)
  - [Namespace `Proto`](#-namespace-proto-1)
- [?? protocolgame.cpp](#-protocolgamecpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame)
- [?? protocolgame.h](#-protocolgameh)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-1)
- [?? spritemanager.cpp](#-spritemanagercpp)
  - [Klasa `SpriteManager`](#-klasa-spritemanager)
- [?? protocolgamesend.cpp](#-protocolgamesendcpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-2)
- [?? localplayer.h](#-localplayerh)
  - [Klasa `LocalPlayer`](#-klasa-localplayer-1)
- [?? towns.cpp](#-townscpp)
  - [Klasa `Town`](#-klasa-town)
  - [Klasa `TownManager`](#-klasa-townmanager)
- [?? spritemanager.h](#-spritemanagerh)
  - [Klasa `SpriteManager`](#-klasa-spritemanager-1)
- [?? tile.cpp](#-tilecpp)
  - [Klasa `Tile`](#-klasa-tile)
- [?? statictext.h](#-statictexth)
  - [Klasa `StaticText`](#-klasa-statictext)
- [?? uimapanchorlayout.cpp](#-uimapanchorlayoutcpp)
  - [Klasa `UIPositionAnchor`](#-klasa-uipositionanchor)
  - [Klasa `UIMapAnchorLayout`](#-klasa-uimapanchorlayout)
- [?? thing.h](#-thingh)
  - [Klasa `Thing`](#-klasa-thing)
- [?? uiitem.h](#-uiitemh)
  - [Klasa `UIItem`](#-klasa-uiitem)
- [?? thing.cpp](#-thingcpp)
  - [Klasa `Thing`](#-klasa-thing-1)
- [?? uimap.cpp](#-uimapcpp)
  - [Klasa `UIMap`](#-klasa-uimap)
- [?? thingstype.h](#-thingstypeh)
  - [Klasa `ThingsType`](#-klasa-thingstype)
- [?? uigraph.h](#-uigraphh)
  - [Klasa `UIGraph`](#-klasa-uigraph)
- [?? uicreature.h](#-uicreatureh)
  - [Klasa `UICreature`](#-klasa-uicreature)
- [?? thingtype.cpp](#-thingtypecpp)
  - [Klasa `ThingType`](#-klasa-thingtype)
- [?? towns.h](#-townsh)
  - [Klasa `Town`](#-klasa-town-1)
  - [Klasa `TownManager`](#-klasa-townmanager-1)
- [?? thingtype.h](#-thingtypeh)
  - [Klasa `ThingType`](#-klasa-thingtype-1)
- [?? uicreature.cpp](#-uicreaturecpp)
  - [Klasa `UICreature`](#-klasa-uicreature-1)
- [?? thingtypemanager.h](#-thingtypemanagerh)
  - [Klasa `ThingTypeManager`](#-klasa-thingtypemanager)
- [?? thingtypemanager.cpp](#-thingtypemanagercpp)
  - [Klasa `ThingTypeManager`](#-klasa-thingtypemanager-1)
- [?? tile.h](#-tileh)
  - [Klasa `Tile`](#-klasa-tile-1)
- [?? uimap.h](#-uimaph)
  - [Klasa `UIMap`](#-klasa-uimap-1)
- [?? uiminimap.cpp](#-uiminimappp)
  - [Klasa `UIMinimap`](#-klasa-uiminimap)
- [?? uiprogressrect.cpp](#-uiprogressrectcpp)
  - [Klasa `UIProgressRect`](#-klasa-uiprogressrect)
- [?? uimapanchorlayout.h](#-uimapanchorlayouth)
  - [Klasa `UIPositionAnchor`](#-klasa-uipositionanchor-1)
  - [Klasa `UIMapAnchorLayout`](#-klasa-uimapanchorlayout-1)
- [?? uiminimap.h](#-uiminimaph)
  - [Klasa `UIMinimap`](#-klasa-uiminimap-1)
- [?? game.cpp](#-gamecpp)
  - [Klasa `Game`](#-klasa-game-1)
- [?? uiprogressrect.h](#-uiprogressrecth)
  - [Klasa `UIProgressRect`](#-klasa-uiprogressrect-1)
- [?? uisprite.cpp](#-uispritecpp)
  - [Klasa `UISprite`](#-klasa-uisprite)
- [?? uisprite.h](#-uispriteh)
  - [Klasa `UISprite`](#-klasa-uisprite-1)
- [?? walkmatrix.h](#-walkmatrixh)
  - [Klasa `WalkMatrix`](#-klasa-walkmatrix)
- [?? protocolgameparse.cpp](#-protocolgameparsecpp)
  - [Klasa `ProtocolGame`](#-klasa-protocolgame-3)
- [?? luafunctions_client.cpp](#-luafunctions_clientcpp)
# ?? Indeks funkcji/metod
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
# ?? Mapa zaleznosci
Ponizszy diagram przedstawia gl�wne zaleznosci i przeplyw informacji miedzy kluczowymi modulami systemu.

```mermaid
graph TD
    subgraph "Aplikacja i UI"
        Client[Client] -->|inicjalizuje| Game
        Client -->|inicjalizuje| Map
        Client -->|inicjalizuje| ThingTypeManager
        UIMap[UIMap] -->|renderuje| MapView
        MapView -->|odczytuje dane| Map
        UICreature[UICreature] -->|wyswietla| Creature
        UIItem[UIItem] -->|wyswietla| Item
    end

    subgraph "Logika Gry"
        Game[Game] -->|wysyla akcje| ProtocolGame
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
        ProtocolGame -->|wysyla pakiety| TCPSocket
    end

    subgraph "Dane i Zasoby"
        ThingTypeManager[ThingTypeManager] -->|wczytuje| DAT["things.dat"]
        ThingTypeManager -->|wczytuje| OTB["items.otb"]
        SpriteManager[SpriteManager] -->|wczytuje| SPR["sprites.spr"]
        Map -->|wczytuje| OTBM["map.otbm"]
        Minimap -->|wczytuje| OTMM["minimap.otmm"]
        ThingType -->|uzywa| SpriteManager
    end

    MapView --> Creature
    MapView --> Item
    Map --> Tile
    Tile --> Thing
```

**Opis zaleznosci:**
-   **Client** jest punktem startowym, kt�ry inicjalizuje wszystkie gl�wne moduly (`Game`, `Map`, `ThingTypeManager`).
-   **Game** jest centralnym "m�zgiem" aplikacji, zarzadzajacym stanem gry, lokalnym graczem i komunikacja sieciowa poprzez `ProtocolGame`.
-   **ProtocolGame** jest odpowiedzialny za serializacje i deserializacje danych przesylanych do i z serwera. Aktualizuje stan `Game` na podstawie otrzymanych pakiet�w.
-   **Map** przechowuje wszystkie dane o swiecie gry, w tym `Tile` (pola) i `Thing` (obiekty).
-   **MapView** jest odpowiedzialny za renderowanie danych z `Map` na ekranie. Jest to warstwa wizualizacyjna dla danych mapy.
-   **ThingTypeManager** i **SpriteManager** to menedzery zasob�w, kt�re wczytuja dane z plik�w `.dat`, `.otb` i `.spr`, dostarczajac definicje i grafiki dla wszystkich obiekt�w w grze.
-   Hierarchia dziedziczenia obiekt�w: `Thing` jest baza dla `Item` i `Creature`. `Creature` jest baza dla `Player`, a `Player` dla `LocalPlayer`.
-   Widzety UI (`UIMap`, `UICreature`, `UIItem`) sa wyspecjalizowanymi komponentami do wyswietlania odpowiednich element�w logiki gry.
# ?? Architektura systemu
System jest zbudowany w oparciu o architekture warstwowa, gdzie kazda warstwa ma jasno zdefiniowane obowiazki. Mozna wyr�znic nastepujace gl�wne komponenty:

1.  **Framework (Warstwa podstawowa)**
    -   **Core**: Zarzadzanie aplikacja, petla gl�wna, zdarzeniami (`EventDispatcher`), zasobami (`ResourceManager`), czasem (`Clock`).
    -   **Graphics**: Nisko-poziomowe renderowanie, zarzadzanie teksturami (`TextureManager`), shaderami (`ShaderManager`), czcionkami (`FontManager`) i kolejka rysowania (`DrawQueue`).
    -   **UI**: System interfejsu uzytkownika oparty na widzetach (`UIWidget`) i stylach OTML.
    -   **LuaEngine**: Integracja z silnikiem skryptowym Lua, umozliwiajaca rozszerzanie logiki gry.
    -   **Net**: Nisko-poziomowa obsluga polaczen sieciowych (`Protocol`, `Connection`).

2.  **Client (Warstwa aplikacji)**
    -   **Zarzadzanie stanem gry (`Game`)**: Centralny singleton, kt�ry zarzadza sesja gry, stanem lokalnego gracza, interakcjami i komunikacja z serwerem. Dziala jak fasada dla reszty systemu.
    -   **Obsluga protokolu (`ProtocolGame`)**: Implementacja protokolu sieciowego. Tlumaczy akcje gracza na pakiety i pakiety z serwera na zmiany w stanie gry.
    -   **Reprezentacja swiata gry (`Map`, `Tile`, `Thing`)**: Obiektowy model swiata gry. `Map` przechowuje kolekcje `Tile`, a kazdy `Tile` przechowuje stos `Thing` (przedmiot�w, stworzen, etc.).
    -   **Zarzadzanie zasobami gry (`ThingTypeManager`, `SpriteManager`)**: Singletony odpowiedzialne za wczytywanie i dostarczanie definicji i grafik dla wszystkich obiekt�w w grze z plik�w `.dat`, `.otb`, `.spr`.
    -   **Renderowanie (`MapView`, `Minimap`)**: Klasy odpowiedzialne za wizualizacje danych z `Map`. `MapView` renderuje gl�wny widok gry, a `Minimap` - minimape. Wykorzystuja one `DrawQueue` z warstwy frameworka.
    -   **UI klienta (`UIMap`, `UIItem`, `UICreature`)**: Wyspecjalizowane widzety, kt�re lacza dane z logiki gry (np. `Item`, `Creature`) z systemem UI frameworka.
# # # Przeplyw danych i zdarzen
-   **Wejscie uzytkownika**: Zdarzenia wejscia (mysz, klawiatura) sa przechwytywane przez `UIWidget`. Jesli akcja dotyczy gry (np. klikniecie na mapie), wywolywana jest odpowiednia metoda w `Game` (np. `g_game.walk()`).
-   **Wysylanie danych**: `Game` wywoluje metode w `ProtocolGame` (np. `sendWalkNorth()`), kt�ra tworzy pakiet i wysyla go na serwer.
-   **Odbieranie danych**: `ProtocolGame` odbiera pakiet, `parseMessage` identyfikuje jego typ na podstawie opkodu i wywoluje odpowiednia metode `parse...`.
-   **Aktualizacja stanu**: Metoda `parse...` (np. `parseCreatureMove`) odczytuje dane z pakietu i wywoluje metody w `Game` lub `Map` (np. `g_map.addThing(...)`), kt�re modyfikuja stan gry.
-   **Renderowanie**: W kazdej klatce, `UIMap` wywoluje `MapView::drawMapBackground` i `drawMapForeground`. `MapView` pobiera aktualny stan z `g_map` (widoczne `Tile` i `Thing`), a nastepnie rysuje je na ekranie, uzywajac `ThingTypeManager` i `SpriteManager` do uzyskania odpowiednich grafik.

Ta architektura oddziela logike gry od renderowania i obslugi sieci, co ulatwia zarzadzanie kodem i jego rozbudowe. Uzycie Lua pozwala na dynamiczne modyfikowanie zachowan interfejsu i logiki bez potrzeby rekompilacji calego klienta.
