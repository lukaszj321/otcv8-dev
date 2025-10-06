<# 
 Split-ModulesDoc-Structured.ps1
 --------------------------------
 Splits the monolithic modules_Documentation.md into per-module files,
 cutting ONLY on headings like:
   "# Modul: `name`", "# Moduł: `name`", "# Module: `name`"
 Also supports a leading "¦" or "|" before the word.

 PowerShell 5.1+ compatible.

 Params:
   -InputFile  : path to input MD (UTF-8)
   -OutRoot    : output directory (default .\docs\modules\structured)
   -WhatIf     : dry run, prints actions only
#>

param(
  [Parameter(Mandatory=$true)]
  [string]$InputFile,

  [string]$OutRoot = ".\docs\modules\structured",

  [switch]$WhatIf
)

# ---------- helpers ----------
function Normalize-PathSafe {
  param([string]$Path)
  try {
    # Resolve-Path działa tylko gdy ścieżka istnieje
    $rp = Resolve-Path -LiteralPath $Path -ErrorAction Stop
    return $rp.Path
  } catch {
    # Jeśli już absolutna -> oddaj jak jest (nie doklejaj current dir)
    if ([System.IO.Path]::IsPathRooted($Path)) {
      return $Path
    }
    # Jeśli względna -> zrób absolutną względem CWD
    return (Join-Path (Get-Location).Path $Path)
  }
}

function New-ItemSafeDir {
  param([string]$Path)
  if ($WhatIf) {
    Write-Host "[DRY] mkdir $Path"
  } else {
    New-Item -ItemType Directory -Path $Path -Force | Out-Null
  }
}

function Out-FileUtf8 {
  param(
    [string]$Path,
    [string]$Content
  )
  if ($WhatIf) {
    Write-Host "[DRY] > $Path"
  } else {
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
  }
}

# ---------- input ----------
$InputFile = Normalize-PathSafe $InputFile
if (-not (Test-Path -LiteralPath $InputFile)) {
  throw "Input file not found: $InputFile"
}

$OutRoot = Normalize-PathSafe $OutRoot
if (-not $WhatIf) { New-ItemSafeDir -Path $OutRoot }

# read whole file as UTF-8
$raw = Get-Content -LiteralPath $InputFile -Raw -Encoding UTF8

# ---------- module heading regex ----------
# start of line, "#", optional "¦" (U+00A6) or "|" then "Modul/Moduł/Module" + ":"
$moduleHeaderRegex = '^\s*#\s*(?:[\|\u00A6]\s*)?(?:Modu(?:l|\u0142)|Module)\s*:'

# ---------- scan lines and build blocks ----------
$lines = ($raw -split "`n", 0)
$blocks = New-Object System.Collections.Generic.List[hashtable]
$current = $null
$currentContent = New-Object System.Text.StringBuilder
$introCaptured = $false

function Flush-Current {
  if ($null -ne $script:current) {
    $script:current['content'] = $script:currentContent.ToString()
    $script:blocks.Add($script:current) | Out-Null
  }
  $script:current = $null
  $script:currentContent = New-Object System.Text.StringBuilder
}

for ($i=0; $i -lt $lines.Count; $i++) {
  $line = $lines[$i]

  if ($line -match $moduleHeaderRegex) {
    if (-not $introCaptured) {
      $intro = @{
        title   = "00_overview"
        isIntro = $true
        content = $currentContent.ToString()
      }
      $blocks.Add($intro) | Out-Null
      $introCaptured = $true
      $currentContent = New-Object System.Text.StringBuilder
    }

    Flush-Current

    # strip leading "# " for display title (keep original line in content)
    $titleRaw = ($line -replace '^\s*#\s*', '').Trim()
    $current = @{ title = $titleRaw }
    [void]$currentContent.AppendLine($line)
    continue
  }

  [void]$currentContent.AppendLine($line)
}

Flush-Current

if ($blocks.Count -eq 0) {
  $blocks.Add(@{ title="00_overview"; isIntro=$true; content=$raw }) | Out-Null
}

Write-Host ("[INFO] Found {0} logical blocks (intro + modules by '# Modul:')." -f $blocks.Count)

# ---------- slug helpers ----------
$invalid = [string]::Join('', [System.IO.Path]::GetInvalidFileNameChars())
$invRe = "[{0}]" -f ([regex]::Escape($invalid))

function Get-Slug {
  param([string]$Text)
  $t = $Text

  # prefer text inside backticks
  $m = [regex]::Match($t, '`\s*([^`]+?)\s*`')
  if ($m.Success) { $t = $m.Groups[1].Value }

  # drop "¦ Modul:" / "| Modul:" / "Modul:" / "Moduł:" / "Module:"
  $t = ($t -replace '^(?:[\|\u00A6]\s*)?(?:Modu(?:l|\u0142)|Module)\s*:\s*', '')

  $t = $t.ToLowerInvariant()
  $t = ($t -replace $invRe, ' ')
  $t = ($t -replace '[^\p{L}\p{Nd}_\-\.\s/]', ' ')
  $t = ($t -replace '\s+', '-').Trim('-')
  if (-not $t) { $t = "modul" }
  return $t
}

# ---------- category mapping ----------
function Map-Category {
  param([string]$Title)
  $slug = Get-Slug $Title

  if ($slug -match '^(client|corelib|gamelib|protocol|styles|things)(/|$)') { return "core" }
  if ($slug -match '^gamelib/ui') { return "ui" }
  if ($slug -match '^(ui|ui_widgets)') { return "ui" }

  if ($slug -match '^(game_(interface|market|console|containers|cooldown|healthinfo|hotkeys|imbuing|inventory|itemselector|minimap|modaldialog|npctrade|outfit|playerdeath|playermount|playertrade|prey|questlog|ruleviolation|shop|skills|spelllist|stats|textmessage|textwindow|topbar|unjustifiedpoints|viplist|walking|battle|actionbar))') {
    return "gameplay"
  }

  if ($slug -match '^game_bot') { return "bot_tools" }
  if ($slug -match '^(bot_|vbot|attackbot|healbot|botserver)') { return "bot_tools" }

  if ($slug -match '^(updater|crash_reporter|bugreport|feedback|locales|mobile|profiles|terminal|shaders|features)(/|$)') {
    return "dev_tools"
  }

  # default bucket
  return "dev_tools"
}

# ---------- prepare output dirs ----------
$dirCore      = Join-Path $OutRoot "core"
$dirUi        = Join-Path $OutRoot "ui"
$dirGameplay  = Join-Path $OutRoot "gameplay"
$dirBot       = Join-Path $OutRoot "bot_tools"
$dirDev       = Join-Path $OutRoot "dev_tools"

foreach ($d in @($dirCore,$dirUi,$dirGameplay,$dirBot,$dirDev)) {
  New-ItemSafeDir -Path $d
}

# ---------- write files ----------
$indexLines = New-Object System.Collections.Generic.List[string]
$indexLines.Add("# Modules - structured") | Out-Null
$indexLines.Add("") | Out-Null
$indexLines.Add("*This file was generated automatically.*") | Out-Null
$indexLines.Add("") | Out-Null
$indexLines.Add("## Contents") | Out-Null
$indexLines.Add("") | Out-Null

foreach ($b in $blocks) {
  if ($b.isIntro) {
    $introPath = Join-Path $OutRoot "README.md"
    $introContent = $b.content
    if (-not $introContent.Trim()) {
      $introContent = "# Technical Documentation: OTClient Modules`n"
    }
    Out-FileUtf8 -Path $introPath -Content $introContent
    continue
  }

  $cat  = Map-Category $b.title
  $slug = Get-Slug $b.title
  $fileName = "modul-{0}.md" -f $slug
  $outPath = Join-Path (Join-Path $OutRoot $cat) $fileName

  $docTitle = $b.title
  $content = $b.content
  if ($content -notmatch '^\s*#\s') {
    $content = "# " + $docTitle + "`n`n" + $content
  }

  Out-FileUtf8 -Path $outPath -Content $content

  $rel = "./{0}/{1}" -f $cat, $fileName
  $indexLines.Add( ("- **{0}** -> {1}" -f $slug, $rel) ) | Out-Null

  $label = "OK"
  if ($WhatIf) { $label = "DRY" }
  Write-Host ("[{0}] {1} -> {2}" -f $label, $b.title, $outPath)
}

# write index
$indexPath = Join-Path $OutRoot "INDEX.md"
Out-FileUtf8 -Path $indexPath -Content ($indexLines -join "`n")

# summary
Write-Host ""
if ($WhatIf) {
  Write-Host ("[DRY] Finished preview. Output root would be: {0}" -f $OutRoot)
  Write-Host "Tip: review docs/modules/structured/INDEX.md and wire it in mkdocs.yml nav."
} else {
  Write-Host ("[DONE] Files saved under: {0}" -f $OutRoot)
  Write-Host "Top files:"
  Write-Host ("  - {0}" -f (Join-Path $OutRoot "README.md"))
  Write-Host ("  - {0}" -f (Join-Path $OutRoot "INDEX.md"))
  Write-Host "  - Buckets:"
  Write-Host ("    - Core:      {0}" -f $dirCore)
  Write-Host ("    - UI:        {0}" -f $dirUi)
  Write-Host ("    - Gameplay:  {0}" -f $dirGameplay)
  Write-Host ("    - BotTools:  {0}" -f $dirBot)
  Write-Host ("    - DevTools:  {0}" -f $dirDev)
  Write-Host "Tip: review docs/modules/structured/INDEX.md and wire it in mkdocs.yml nav."
}
