﻿# ¦ Modul: `game_bot/default_configs/cavebot_1.3/cavebot_configs`

```text

goto:1033,1044,7

goto:1031,1038,7

goto:1030,1038,7

goto:1157,985,7

goto:1161,981,7

goto:1033,1042,7

goto:1034,1038,7

goto:1169,985,7

goto:1175,985,7

goto:1176,983,7

goto:756,846,7

goto:756,846,7

config:{"walk":100,"walk2":false}

extensions:[[

{

  "Depositer": [

],

  "Supply": [

]

}

]]

```

---
# fast_walking.cfg

```text

goto:84,112,6

goto:95,108,6

config:{"mapClickDelay":100,"walkDelay":10,"ping":250,"ignoreFields":false,"useDelay":400,"mapClick":false}

extensions:[[

{

  "Depositer": [

],

  "Supply": [

]

}

]]

```

---
# test_src.cfg

```text

goto:93,129,7

goto:96,123,7

goto:96,117,7

goto:101,114,7

goto:95,111,6

goto:89,111,6

goto:83,108,6

goto:80,102,6

goto:80,96,6

goto:85,90,6

goto:88,92,6

goto:91,86,7

goto:97,85,7

goto:103,84,7

function:[[

TargetBot.enableLuring()

return true

]]

goto:109,79,7

goto:112,79,7

goto:112,79,8

function:[[

TargetBot.disableLuring()

return true

]]

goto:112,79,7

goto:106,84,8

goto:100,80,8

goto:100,74,8

goto:99,80,8

goto:105,83,8

function:[[

TargetBot.setOff()

return true

]]

goto:111,82,8

goto:112,79,8

goto:106,82,7

goto:100,85,7

goto:94,85,7

goto:91,91,7

goto:89,92,7

goto:83,90,6

function:[[

TargetBot.setOff()

return true

]]

goto:77,94,6

goto:75,95,6

goto:69,96,7

goto:63,100,7

goto:61,102,7

goto:62,96,8

use:61,102,8

goto:62,101,8

goto:68,99,7

goto:74,95,7

goto:75,95,7

goto:79,101,6

goto:81,107,6

goto:87,109,6

goto:93,112,6

function:[[

TargetBot.disableLuring()

return true

]]

goto:99,116,6

use:102,114,6

goto:101,115,6

use:100,116,5

goto:101,115,5

goto:100,116,4

goto:102,114,5

goto:101,114,6

goto:96,120,7

goto:95,126,7

function:[[

g_game.safeLogout()

delay(1000)

return "retry"

]]

config:{"useDelay":400,"mapClickDelay":100,"walkDelay":20,"ping":150,"ignoreFields":false,"skipBlocked":true,"mapClick":false}

extensions:[[

{

  "Depositer": [

],

  "Supply": [

]

}

]]

```

---
