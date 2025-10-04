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
$Targets = @(
  'docs\architektura',
  'docs\modules',
  'docs\api\lua',
  'docs\api\engine',
  'docs\data'
)

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
    }
  }
}

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
