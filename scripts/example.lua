-- Example Lua Script for OTClient v8
-- Reference commit: 84add321aea1031e8700b9a4db4b5025ef0b1396
--
-- This is an example script demonstrating basic OTClient Lua functionality.

-- Example: Simple module initialization
function init()
    print("Example module initialized")
end

function terminate()
    print("Example module terminated")
end

-- Example: Event handler
function onGameStart()
    print("Game started!")
end

-- Example: UI interaction
function onButtonClick()
    local playerName = g_game.getLocalPlayer():getName()
    print("Button clicked by: " .. playerName)
end

-- Example: Scheduled task
scheduleEvent(function()
    print("This runs after 1 second")
end, 1000)
