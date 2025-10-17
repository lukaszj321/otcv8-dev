-- Auto-generated vBot macros

-- panel: example | group: Core | order: 1 | icon: icon-heal
macro(200, 'Auto Heal', function()
  if (function() return hppercent() < 50 end)() then
    say('exura')
  end
end, true)
