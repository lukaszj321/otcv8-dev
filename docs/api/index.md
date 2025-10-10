# API (surowe i zewnętrzne)

:::{admonition} Skąd pochodzą pliki?
Te pliki są **kopiowane** z repo (`api/otcv8-full-api.md`, `api/lua/luafunctions_client.md`) przez job CI (patrz fragment w ISSUE).
:::

```{toctree}
:maxdepth: 1
:caption: API
external/otcv8-full-api
external/lua/luafunctions_client
```

## Snippety

```lua
-- przykład użycia funkcji:
local res = otclient.doSomething{ param = 123 }
print(res)
```
