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
$Targets = @(
  'docs\architektura',
  'docs\modules',
  'docs\api\lua',
  'docs\api\engine',
  'docs\data'
)
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
    }
  }
}

Skip "mkdocs.yml left untouched"
Write-Host ""
Info "Summary: moved=$done, skipped=$skipped, missing=$miss"
