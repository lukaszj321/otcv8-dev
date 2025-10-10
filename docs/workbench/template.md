# SZABLON: Nazwa skryptu

```{admonition} Instrukcja
:class: tip
Skopiuj ten plik do `docs/workbench/<twoj_skrypt>.md` i uzupełnij sekcje poniżej.
```

## Metadane

| Pole          | Wartość                      |
|---------------|------------------------------|
| Autor         | _Twoje imię_                 |
| Wersja        | 0.1.0                        |
| Kategoria     | _PvE/PvP/UI/Utility_         |
| Kompatybilność| OTClient v8.x                |
| Zależności    | _wypisz_                     |
| Plik źródłowy | `scripts/<nazwa>.lua`        |
| Licencja      | MIT                          |

## Opis

Krótki opis **co robi** skrypt, **dlaczego** i **kiedy** używać.

## Użycie

- Jak uruchomić (kroki)
- Parametry/konfiguracja
- Efekty uboczne / ograniczenia

## Checklist testowa

- [ ] Uruchamia się bez błędów
- [ ] Działa we wskazanym buildzie OTClient
- [ ] Zgodny z polityką logowania/bezpieczeństwa
- [ ] Pokryty scenariuszami z sekcji *Testy manualne*

## Kod

### Wklejony blok (szybko)
```lua
-- Wklej tu kod (tymczasowo). Zalecane: literalinclude poniżej.
```

### Automatyczne wczytanie pliku
```{code-block} rst
.. literalinclude:: ../../scripts/<nazwa>.lua
   :language: lua
   :linenos:
   :caption: <nazwa>.lua
```

## API powiązane

- [OTCV8 Full API](../api/external/otcv8-full-api.html)
- [Lua Client Functions](../api/external/lua/luafunctions_client.html)

## Diagram działania (Mermaid)

```{mermaid}
%%{init: {'theme': 'neutral'}}%%
flowchart LR
  Start([Start]) --> A[Hook: onCreatureAppear]
  A --> B{Warunek}
  B -- tak --> C[Akcja: castSpell]
  B -- nie --> D[Akcja: moveToSafeSpot]
  C --> End([End])
  D --> End([End])
```

## Testy manualne

1. Kroki testowe
2. Oczekiwane rezultaty
3. Edge cases

## Notatki / TODO

- [ ] Do zrobienia
- [ ] Dodać logowanie metryk

## Changelog

- 0.1.0 – pierwsza wersja