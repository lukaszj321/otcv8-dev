# Filozofia Projektowania Diagramów

## 1. Cel Tego Dokumentu

Ten dokument definiuje **zasady myślowe** i **wysokopoziomowe cele** stojące za każdym diagramem w tym projekcie. Nie jest to specyfikacja techniczna, lecz **przewodnik po procesie twórczym**. Ma on na celu zapewnienie, że każdy diagram jest nie tylko technicznie poprawny, ale przede wszystkim **użyteczny, klarowny i celowy**.

Każdy diagram jest traktowany jak produkt: interfejs użytkownika, którego zadaniem jest efektywne przekazywanie złożonej wiedzy.

## 2. Trzy Fundamentalne Zasady

### Zasada #1: Opowiadaj Jedną, Spójną Historię
Każdy diagram musi mieć jeden, jasno zdefiniowany cel i opowiadać jedną, spójną historię. Przed rozpoczęciem pracy, zdefiniuj tę historię w jednym zdaniu (np. "Ten diagram pokazuje, jak dane wejściowe są szyfrowane i przekształcane w dane wyjściowe"). Jeśli diagram próbuje opowiedzieć kilka historii naraz, jest to sygnał, że należy go podzielić.

### Zasada #2: Optymalizuj pod Kątem Zrozumienia w 5 Sekund
Diagram musi być zaprojektowany tak, aby kluczowe komponenty i ich relacje były zrozumiałe na pierwszy rzut oka. Nowy deweloper, patrząc na diagram, powinien w ciągu kilku sekund zrozumieć ogólną rolę i kontekst danego komponentu, nawet bez czytania szczegółowych etykiet. Przejrzystość ma absolutny priorytet nad zagęszczeniem informacji.

### Zasada #3: Wizualizuj To, Czego Nie Widać w Kodzie
Diagramy nie są graficzną reprezentacją listy metod klasy. Ich celem jest wizualizacja **ukrytej złożoności**:
*   **Architektury i relacji** między komponentami.
*   **Przepływów danych i sterowania**, które wymagają śledzenia wielu wywołań funkcji.
*   **Maszyn stanów** i cykli życia obiektów.
*   **Interakcji z systemami zewnętrznymi**.

## 3. Zarządzanie Złożonością

**Złota Reguła:** Nigdy nie twórz "Boskiego Diagramu" (God Diagram), który próbuje pokazać wszystko.

Złożoność jest wrogiem przejrzystości. Zamiast tworzyć jeden duży, skomplikowany diagram, zawsze dąż do dzielenia go na kilka mniejszych, skupionych na jednym zadaniu i połączonych ze sobą diagramów.

**Kiedy należy podzielić diagram?**
*   Gdy miesza różne poziomy abstrakcji (np. widok architektury z implementacją funkcji).
*   Gdy linie połączeń zaczynają przypominać "spaghetti".
*   Gdy opowiada więcej niż jedną historię (patrz Zasada #1).

**Jak to zrobić?** Stwórz diagram wysokopoziomowy ("overview"), a w nim umieść węzły, które działają jak hiperłącza do stron z bardziej szczegółowymi diagramami ("details").
