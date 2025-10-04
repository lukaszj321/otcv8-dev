<<<<<<< HEAD
[CmdletBinding(SupportsShouldProcess = $true)]
param()

try { [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false) } catch {}

function Say($tag, $msg, $color) { Write-Host "[$tag] $msg" -ForegroundColor $color }
function Ok($m) { Say 'OK' $m Green }
function Info($m) { Say 'i' $m Cyan }
function Warn($m) { Say '!' $m Yellow }
function Err($m) { Say 'x' $m Red }
function Skip($m) { Say '.' $m DarkGray }

# --- Kanonizacja: usunięcie diakrytyków (FormD + wywalenie NonSpacingMark), lower, wycięcie nie [a-z0-9]
function Normalize-Key([string]$s) {
  if (-not $s) { return "" }
  $nf = $s.Normalize([Text.NormalizationForm]::FormD)
  $sb = New-Object System.Text.StringBuilder
  foreach ($ch in $nf.ToCharArray()) {
    $cat = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch)
    if ($cat -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
      [void]$sb.Append($ch)
    }
  }
  $ascii = $sb.ToString().Normalize([Text.NormalizationForm]::FormC).ToLowerInvariant()
  return ($ascii -replace '[^a-z0-9]', '')
}

# Czy keyB zawiera wszystkie tokeny keyA w kolejności
function Key-Contains-In-Order([string]$hay, [string[]]$tokens) {
  $i = 0
  foreach ($t in $tokens) {
    $pos = $hay.IndexOf($t, $i)
    if ($pos -lt 0) { return $false }
    $i = $pos + $t.Length
  }
  return $true
}

function Ok-PatternTokens([string]$pattern) {
  $raw = ($pattern -replace '[\(\)\[\]\{\},]', ' ') -replace '[\s_\-\.]+', ' '
  $toks = $raw.Trim() -split '\s+'
  return $toks | ForEach-Object { Normalize-Key $_ } | Where-Object { $_ -ne '' }
}

$ScriptDir = $PSScriptRoot
$DocsRoot = (Get-Item $ScriptDir).Parent.FullName
$RepoRoot = (Get-Item $DocsRoot).Parent.FullName
Info "RepoRoot = $RepoRoot"
Info "DocsRoot = $DocsRoot"

# Katalogi docelowe
=======
<#
  Arrange-Docs.ps1
  Reorganizes files in docs/ to the target structure used by MkDocs.
  No commits here — commit/push in GitHub Desktop.
#>

[CmdletBinding(SupportsShouldProcess = $true)]
param()

# --- Console encoding to UTF8 (safe) ---
try { [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false) } catch {}

function Write-Info($msg) { Write-Host "[i] $msg" -ForegroundColor Cyan }
function Write-Ok($msg)   { Write-Host "[OK] $msg" -ForegroundColor Green }
function Write-Skip($msg) { Write-Host "[.] $msg" -ForegroundColor DarkGray }
function Write-Warn($msg) { Write-Host "[!] $msg" -ForegroundColor Yellow }
function Write-Err($msg)  { Write-Host "[x] $msg" -ForegroundColor Red }

# --- Locate repo paths based on script location ---
# Script path: <repo>\docs\tools\Arrange-Docs.ps1
$ScriptDir = $PSScriptRoot
$DocsRoot  = (Get-Item $ScriptDir).Parent.FullName
$RepoRoot  = (Get-Item $DocsRoot).Parent.FullName

Write-Info "RepoRoot = $RepoRoot"
Write-Info "DocsRoot = $DocsRoot"
Write-Info "ScriptDir = $ScriptDir"

# --- Ensure target folders exist ---
>>>>>>> b36387a71ba885d6b6d7edb88fa8f108651475c9
$Targets = @(
  'docs\architektura',
  'docs\modules',
  'docs\api\lua',
  'docs\api\engine',
  'docs\data'
)
<<<<<<< HEAD
foreach ($rel in $Targets) {
  $dst = Join-Path $RepoRoot $rel
  if (-not (Test-Path -LiteralPath $dst)) {
    if ($PSCmdlet.ShouldProcess($dst, 'mkdir')) { New-Item -ItemType Directory -Path $dst -Force | Out-Null }
    Ok "Created: $rel"
  }
  else { Skip "Exists:  $rel" }
}

# Zbieramy wszystkie .md
$AllMd = @(Get-ChildItem -LiteralPath $RepoRoot -Recurse -Include *.md -File)
Info "Found $($AllMd.Count) *.md files in repo"

# Cache kluczy
$FileIndex = @()
foreach ($f in $AllMd) {
  $key = Normalize-Key ($f.Name)
  $fullKey = Normalize-Key ($f.FullName)
  $FileIndex += [pscustomobject]@{
    File    = $f
    KeyName = $key
    KeyFull = $fullKey
  }
}

# Reguły: patterns (lista fraz) -> dst (docelowa ścieżka)
$Rules = @(
  # Architektura / przeglądy
  @{ patterns = @('framework_overview'); dst = 'docs\architektura\framework_overview.md' },
  @{ patterns = @('client_overview', 'cpp overview'); dst = 'docs\architektura\client_overview.md' },
  @{ patterns = @('src framework', 'framework src framework'); dst = 'docs\architektura\src_framework.md' },
  @{ patterns = @('src client', 'client src client'); dst = 'docs\architektura\src_client.md' },

  # Moduły
  @{ patterns = @('modules_core'); dst = 'docs\modules\modules_core.md' },
  @{ patterns = @('modules_game_1'); dst = 'docs\modules\modules_game_1.md' },
  @{ patterns = @('modules_game_2'); dst = 'docs\modules\modules_game_2.md' },
  @{ patterns = @('modules_misc'); dst = 'docs\modules\modules_misc.md' },
  @{ patterns = @('modules documentation', 'modules_documentation'); dst = 'docs\modules_Documentation.md' },

  # API Lua (uwzględnij nazwę z nawiasami)
  @{ patterns = @('otclient core lua functions', 'luafunctions_client'); dst = 'docs\api\lua\luafunctions_client.md' },

  # Engine / UI (przenosimy z docs/ui do api/engine)
  @{ patterns = @('specyfikacja ui', 'otclient v 8 specyfikacja ui'); dst = 'docs\api\engine\otclient_v_8_specyfikacja_ui.md' },
  @{ patterns = @('presety kanoniczne otui ts', 'otclient v 8 core otc core'); dst = 'docs\api\engine\presety_kanoniczne_otui_ts_otc_core.md' },
  @{ patterns = @('addendum', 'import z lua', 'strict', 'golden'); dst = 'docs\api\engine\otclient_v_8_addendum_import_z_lua_stringow_auto_strict_goldeny_expanded.md' },
  @{ patterns = @('walidator', 'macierze', 'ast', 'round trip'); dst = 'docs\api\engine\otclient_v_8_walidator_macierze_ast_i_round_trip_specyfikacja_techniczna.md' },

  # Data
  @{ patterns = @('data documentation'); dst = 'docs\data\Data_Documentation.md' }
)

function Find-Source {
  param([string[]]$patterns, [string]$dstAbs)

  if (Test-Path -LiteralPath $dstAbs) {
    return @{ status = 'at-destination'; file = (Get-Item -LiteralPath $dstAbs) }
  }

  foreach ($pat in $patterns) {
    $tokens = Ok-PatternTokens $pat
    foreach ($row in $FileIndex) {
      $hay = $row.KeyName
      $hay2 = $row.KeyFull
      if (Key-Contains-In-Order $hay $tokens -or Key-Contains-In-Order $hay2 $tokens) {
        return @{ status = 'found'; file = $row.File }
      }
    }
  }
  return @{ status = 'missing'; file = $null }
}

$done = 0; $miss = 0; $skipped = 0

foreach ($rule in $Rules) {
  $dstRel = $rule.dst
  $dstAbs = Join-Path $RepoRoot $dstRel
  $dstDir = Split-Path -Path $dstAbs -Parent

  $res = Find-Source -patterns $rule.patterns -dstAbs $dstAbs
  switch ($res.status) {
    'at-destination' {
      Skip "Already at destination: $dstRel"
      $skipped++
    }
    'missing' {
      Warn "Not found for patterns: $($rule.patterns -join ' | ') -> $dstRel"
      $miss++
    }
    'found' {
      $src = $res.file
      $canSkip = $false
      if (Test-Path -LiteralPath $dstAbs) {
        try {
          $h1 = (Get-FileHash -LiteralPath $src.FullName).Hash
          $h2 = (Get-FileHash -LiteralPath $dstAbs).Hash
          if ($h1 -eq $h2) { $canSkip = $true }
        }
        catch {}
      }
      if ($canSkip) {
        Skip "Identical: '$($src.Name)' -> '$dstRel' (skip)"
        $skipped++
        continue
      }

      if ($PSCmdlet.ShouldProcess($dstRel, "MOVE from '$($src.FullName)'")) {
        if (-not (Test-Path -LiteralPath $dstDir)) { New-Item -ItemType Directory -Path $dstDir -Force | Out-Null }
        try {
          if (Test-Path -LiteralPath $dstAbs) { Remove-Item -LiteralPath $dstAbs -Force }
          Move-Item -LiteralPath $src.FullName -Destination $dstAbs -Force
          Ok "Moved: '$($src.Name)' -> '$dstRel'"
          $done++
        }
        catch {
          Err "Move failed -> $dstRel : $($_.Exception.Message)"
        }
      }
=======

foreach ($rel in $Targets) {
  $dest = Join-Path $RepoRoot $rel
  if (-not (Test-Path -LiteralPath $dest)) {
    if ($PSCmdlet.ShouldProcess($dest, 'mkdir')) {
      New-Item -ItemType Directory -Path $dest -Force | Out-Null
    }
    Write-Ok "Created: $rel"
  } else {
    Write-Skip "Exists:  $rel"
  }
}

# --- Mapping: source (relative to docs/ or repo root) -> destination (relative to repo root) ---
$Moves = @(
  @{ src = 'client_overview.md';                                                        dst = 'docs\architektura\client_overview.md' },
  @{ src = 'framework_overview.md';                                                     dst = 'docs\architektura\framework_overview.md' },

  @{ src = 'modules_core.md';                                                           dst = 'docs\modules\modules_core.md' },
  @{ src = 'modules_game_1.md';                                                         dst = 'docs\modules\modules_game_1.md' },
  @{ src = 'modules_game_2.md';                                                         dst = 'docs\modules\modules_game_2.md' },
  @{ src = 'modules_misc.md';                                                           dst = 'docs\modules\modules_misc.md' },
  @{ src = 'modules_Documentation.md';                                                  dst = 'docs\modules_Documentation.md' },

  @{ src = 'OTClient Core Lua Functions (luafunctions_client.cpp).md';                  dst = 'docs\api\lua\luafunctions_client.md' },

  @{ src = 'otclient_v_8_specyfikacja_ui.md';                                           dst = 'docs\api\engine\otclient_v_8_specyfikacja_ui.md' },
  @{ src = 'presety_kanoniczne_otui_ts_otc_core.md';                                    dst = 'docs\api\engine\presety_kanoniczne_otui_ts_otc_core.md' },
  @{ src = 'otclient_v_8_addendum_import_z_lua_stringow_auto_strict_goldeny_expanded.md'; dst = 'docs\api\engine\otclient_v_8_addendum_import_z_lua_stringow_auto_strict_goldeny_expanded.md' },
  @{ src = 'otclient_v_8_walidator_macierze_ast_i_round_trip_specyfikacja_techniczna.md'; dst = 'docs\api\engine\otclient_v_8_walidator_macierze_ast_i_round_trip_specyfikacja_techniczna.md' },

  @{ src = 'Data_Documentation.md';                                                     dst = 'docs\data\Data_Documentation.md' }
)

function Resolve-SourcePath {
  param([string]$Rel)
  $p1 = Join-Path $DocsRoot $Rel
  if (Test-Path -LiteralPath $p1) { return $p1 }
  $p2 = Join-Path $RepoRoot $Rel
  if (Test-Path -LiteralPath $p2) { return $p2 }
  return $null
}

# --- Move/Rename files if needed ---
foreach ($m in $Moves) {
  $srcRel = $m.src
  $dstRel = $m.dst
  $srcAbs = Resolve-SourcePath -Rel $srcRel

  if (-not $srcAbs) {
    Write-Skip "Missing source: $srcRel (skip)"
    continue
  }

  $dstAbs = Join-Path $RepoRoot $dstRel
  $dstDir = Split-Path -Path $dstAbs -Parent

  # skip if identical
  $canSkip = $false
  if (Test-Path -LiteralPath $dstAbs) {
    try {
      $same = (Get-FileHash -LiteralPath $srcAbs).Hash -eq (Get-FileHash -LiteralPath $dstAbs).Hash
      if ($same) { $canSkip = $true }
    } catch {}
  }

  if ($canSkip) {
    Write-Skip "Identical: '$srcRel' -> '$dstRel' (skip)"
    continue
  }

  if ($PSCmdlet.ShouldProcess($dstRel, "MOVE from $srcRel")) {
    if (-not (Test-Path -LiteralPath $dstDir)) {
      New-Item -ItemType Directory -Path $dstDir -Force | Out-Null
    }
    try {
      if (Test-Path -LiteralPath $dstAbs) { Remove-Item -LiteralPath $dstAbs -Force }
      Move-Item -LiteralPath $srcAbs -Destination $dstAbs -Force
      Write-Ok "Moved: '$srcRel' -> '$dstRel'"
    } catch {
      Write-Err "Move failed: '$srcRel' -> '$dstRel' : $($_.Exception.Message)"
      continue
>>>>>>> b36387a71ba885d6b6d7edb88fa8f108651475c9
    }
  }
}

<<<<<<< HEAD
Skip "mkdocs.yml left untouched"
Write-Host ""
Info "Summary: moved=$done, skipped=$skipped, missing=$miss"
=======
# --- Create minimal mkdocs.yml if missing ---
$MkdocsPath = Join-Path $RepoRoot 'mkdocs.yml'
if (-not (Test-Path -LiteralPath $MkdocsPath)) {
  $mk = @"
site_name: OTCv8 Dev — Dokumentacja
site_url: https://lukaszj321.github.io/otcv8-dev/
repo_url: https://github.com/lukaszj321/otcv8-dev
theme:
  name: material
  features:
    - navigation.sections
    - navigation.indexes
    - content.code.copy
markdown_extensions:
  - admonition
  - toc:
      permalink: true
  - pymdownx.highlight
  - pymdownx.superfences

nav:
  - Start: index.md
  - Architektura:
      - Przeglad frameworka: architektura/framework_overview.md
      - Przeglad klienta: architektura/client_overview.md
  - Moduly:
      - Core: modules/modules_core.md
      - Game (1): modules/modules_game_1.md
      - Game (2): modules/modules_game_2.md
      - Misc: modules/modules_misc.md
      - Przewodnik (zbiorczy): modules_Documentation.md
  - API:
      - Lua:
          - Funkcje klienta: api/lua/luafunctions_client.md
      - Engine:
          - Specyfikacja UI: api/engine/otclient_v_8_specyfikacja_ui.md
          - Presety OTUI/TS: api/engine/presety_kanoniczne_otui_ts_otc_core.md
          - Addendum (import z Lua): api/engine/otclient_v_8_addendum_import_z_lua_stringow_auto_strict_goldeny_expanded.md
          - Walidator/AST/Round-trip: api/engine/otclient_v_8_walidator_macierze_ast_i_round_trip_specyfikacja_techniczna.md
  - Zasoby (data/): data/Data_Documentation.md
"@
  if ($PSCmdlet.ShouldProcess($MkdocsPath, 'create mkdocs.yml')) {
    $mk | Out-File -LiteralPath $MkdocsPath -Encoding UTF8 -Force
    Write-Ok "Created mkdocs.yml (minimal)"
  }
} else {
  Write-Skip "mkdocs.yml already exists (leave as-is)"
}

# --- Summary ---
Write-Host ""
Write-Info "Current tree under docs/:"
Get-ChildItem -LiteralPath $DocsRoot -Recurse | Select-Object FullName

Write-Host ""
Write-Ok "Done. Open GitHub Desktop and commit/push."
>>>>>>> b36387a71ba885d6b6d7edb88fa8f108651475c9
