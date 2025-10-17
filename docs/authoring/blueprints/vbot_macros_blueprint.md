---
title: "vBot Macros Blueprint"
updated: "2025-10-17T20:02:11Z"
---

# vBot Macros Blueprint

Struktura do definiowania makr dla `modules/game_bot` (vBot).

## CSV mapping

| Pole               | Typ     | Wymagane | Opis |
|--------------------|---------|----------|------|
| module             | string  | tak      | Nazwa modułu, do którego należą makra |
| macro_id           | string  | tak      | Unikalny identyfikator makra |
| title              | string  | tak      | Tytuł wyświetlany w UI |
| description        | string  | nie      | Opis |
| interval_ms        | int     | tak      | Co ile makro jest wykonywane |
| enabled_by_default | bool    | nie      | Czy włączone domyślnie |
| condition_lua      | string  | nie      | Warunek (Lua), powinien zwracać bool |
| action_lua         | string  | tak      | Akcja (Lua) wykonywana w makrze |
| hotkey             | string  | nie      | Skrót klawiszowy |
| storage_key        | string  | nie      | Klucz w `storage` do zapisu stanu |
| panel_id           | string  | nie      | Docelowy panel/zakładka UI bota |
| macro_group        | string  | nie      | Grupa w obrębie panelu |
| panel_order        | int     | nie      | Kolejność makra w panelu |
| macro_icon         | string  | nie      | Ikona makra (`/images/...` lub alias `icon-*`) |