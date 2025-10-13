# Authoring — landing

:::{admonition} Wskazówka: jakość diagramów
:class: tip
- Używamy `sphinxcontrib-mermaid` + `docs/_static/custom-dark-mermaid.css`, aby strzałki i etykiety były czytelne w dark/light mode.
- Węzły mają linki (`click <id> "<rel-url>" "otwórz"`), co poprawia nawigację w dokumentacji.
- Dla dużych diagramów użyj `:class: dropdown` aby były zwijane.
:::

```{{toctree}}
:maxdepth: 1
:caption: Authoring — spis
01_core/index
02_events/index
03_modules/index
04_ui/index
05_events/index
05_network/index
06_assets/index
07_settings_crypto/index
08_audio/index
09_logging/index
10_game_runtime/index
```
