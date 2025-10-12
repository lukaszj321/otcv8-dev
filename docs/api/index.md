# API (auto + surowe)

:::{admonition} Skąd pochodzą pliki?
- Sekcja **Auto‑generated**: tworzona przez skrypt CI (`scripts/extract-api.mjs`) ze źródeł repo.
- Sekcja **Surowe (z repo)**: ręcznie utrzymywane snapshoty.
:::

```{toctree}
:maxdepth: 2
:caption: Auto‑generated (CI)
:glob:

otcv8-full-api
schemas/index
external/cpp/*
```

```{toctree}
:maxdepth: 1
:caption: Surowe (z repo)

external/otcv8-full-api
external/lua/luafunctions_client
```

## Snippety

```lua
-- przykład użycia funkcji:
local res = otclient.doSomething{ param = 123 }
print(res)
```
