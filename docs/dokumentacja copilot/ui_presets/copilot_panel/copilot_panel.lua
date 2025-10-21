local M = {}
local rootWidget

-- Minimal glue to create/destroy the panel.
function M.show(parent)
  parent = parent or rootWidget or g_ui.getRootWidget()
  if not parent then return end
  if M.widget and not M.widget:isDestroyed() then
    M.widget:show()
    M.widget:raise()
    return M.widget
  end
  M.widget = g_ui.createWidget('CopilotPanel', parent)
  return M.widget
end

function M.hide()
  if M.widget and not M.widget:isDestroyed() then
    M.widget:destroy()
    M.widget = nil
  end
end

-- Example: bind to a common event if available
-- if g_game and connect then
--   connect(g_game, { onGameStart = function() if M.widget then M.widget:hide() end end })
-- end

return M
