<# 
Fix-MkDocsMd.ps1
Użycie:
  # podgląd (bez zapisu)
  powershell -NoProfile -File ".\scripts\Fix-MkDocsMd.ps1" -Path ".\docs"

  # zapisz zmiany (tworzy *.bak obok plików)
  powershell -NoProfile -File ".\scripts\Fix-MkDocsMd.ps1" -Path ".\docs" -Apply
#>

[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [string]$Path,

  [switch]$Apply
)

# --- Pomocnicze -------------------------------------------------------------

function Get-MdFiles {
  param([string]$Root)
  if (-not (Test-Path -LiteralPath $Root)) {
    throw "Ścieżka nie istnieje: $Root"
  }
  Get-ChildItem -LiteralPath $Root -Recurse -File -Include *.md
}

function Read-TextUtf8 {
  param([string]$File)
  # Zawsze zwróć JEDEN string (nie tablica linii)
  return [System.IO.File]::ReadAllText($File,[System.Text.Encoding]::UTF8)
}

function Write-TextUtf8 {
  param([string]$File,[string]$Text)
  # Pisz jako UTF-8 (bez BOM)
  [System.IO.File]::WriteAllText($File,$Text,[System.Text.Encoding]::UTF8)
}

# --- Transformacje ----------------------------------------------------------

function Remove-InvisibleChars {
  param([string]$Text)
  $zwsp = [char]0x200B  # Zero-Width Space
  $shy  = [char]0x00AD  # Soft Hyphen
  $bom  = [char]0xFEFF  # BOM w środku pliku
  $Text = $Text -replace [regex]::Escape("$bom"), ""
  $Text = $Text -replace [regex]::Escape("$zwsp"), ""
  $Text = $Text -replace [regex]::Escape("$shy"), ""
  return $Text
}

function Normalize-Headings {
  param([string]$Text)
  # Uporządkuj # do ###### + pojedyncza spacja po kratkach
  $Text = $Text -replace '(?m)^\s*######\s*', '###### '
  $Text = $Text -replace '(?m)^\s*#####\s*',  '##### '
  $Text = $Text -replace '(?m)^\s*####\s*',   '#### '
  $Text = $Text -replace '(?m)^\s*###\s*',    '### '
  $Text = $Text -replace '(?m)^\s*##\s*',     '## '
  $Text = $Text -replace '(?m)^\s*#\s*',      '# '
  # Wyrównaj: "#    Tytuł" -> "# Tytuł" (pojedyncza spacja)
  $Text = $Text -replace '(?m)^(\#{1,6})\s+(.*)$', '$1 $2'
  return $Text
}

function Join-OneCharLines {
  param([string]$Text)

  # Heurystyka: jeżeli występuje blok >= 6 kolejnych linii,
  # gdzie każda linia ma 1–2 widoczne znaki (litera/cyfra/punktacja),
  # to sklej to w jedną linię (bez spacji w środku),
  # zachowując ewentualne nawiasy/łączniki.
  $lines = $Text -split "`r?`n",-1
  $out = New-Object System.Collections.Generic.List[string]
  $buffer = New-Object System.Collections.Generic.List[string]

  function Flush-Buffer {
    param([System.Collections.Generic.List[string]]$buf,
          [System.Collections.Generic.List[string]]$dst)
    if ($buf.Count -ge 6) {
      # sklej znaki bez separatora, a potem zredukuj wielokrotne spacje
      $joined = ($buf -join '') -replace '\s{2,}',' '
      $dst.Add($joined)
    } else {
      foreach ($b in $buf) { $dst.Add($b) }
    }
    $buf.Clear()
  }

  foreach ($ln in $lines) {
    $trim = $ln.Trim()
    # Dopuszczamy 1–2 znaki (litery/cyfry/punktacja), ewentualnie pojedynczą spację
    if ($trim -match '^[\p{L}\p{N}\p{P}]{1,2}$') {
      $buffer.Add($trim)
    } else {
      if ($buffer.Count -gt 0) { Flush-Buffer -buf $buffer -dst $out }
      $out.Add($ln)
    }
  }
  if ($buffer.Count -gt 0) { Flush-Buffer -buf $buffer -dst $out }

  return ($out -join "`r`n")
}

function Fix-RawBlocks {
  param([string]$Text)
  $open  = ([regex]'{%\s*raw\s*%}').Matches($Text).Count
  $close = ([regex]'{%\s*endraw\s*%}').Matches($Text).Count
  if ($open -gt $close) {
    $missing = $open - $close
    $Text = $Text.TrimEnd() + "`r`n" + ("{% endraw %}`r`n" * $missing)
  }
  return $Text
}

function Normalize-BlankLines {
  param([string]$Text)
  # Usuń linie z samymi białymi znakami, ujednolić CRLF
  $Text = ($Text -replace '(?m)^\s+$','').TrimEnd()
  # wymuś CRLF jako separator
  $Text = ($Text -split "`r?`n") -join "`r`n"
  return $Text + "`r`n"
}

# --- Główna logika ----------------------------------------------------------

$files = Get-MdFiles -Root $Path

$checked = 0
$changed = 0
$unchanged = 0
$changedList = @()

foreach ($f in $files) {
  $checked++

  $orig = Read-TextUtf8 -File $f.FullName
  $txt  = $orig

  $txt = Remove-InvisibleChars  -Text $txt
  $txt = Normalize-Headings     -Text $txt
  $txt = Join-OneCharLines      -Text $txt
  $txt = Fix-RawBlocks          -Text $txt
  $txt = Normalize-BlankLines   -Text $txt

  if ($txt -ne $orig) {
    $changed++
    $changedList += $f.FullName

    if ($Apply) {
      # backup
      Copy-Item -LiteralPath $f.FullName -Destination ($f.FullName + ".bak") -Force
      Write-TextUtf8 -File $f.FullName -Text $txt
      Write-Host "Fix: $($f.FullName)" -ForegroundColor Cyan
    }
  } else {
    $unchanged++
  }
}

Write-Host ""
Write-Host "Checked: $checked files" -ForegroundColor Yellow
Write-Host "Changed: $changed" -ForegroundColor Green
Write-Host "Unchanged: $unchanged" -ForegroundColor Gray
Write-Host ""

if ($Apply) {
  Write-Host "Apply mode. Changes written. Backups *.bak created next to files." -ForegroundColor Green
} else {
  Write-Host "Preview mode. Use -Apply to write changes (creates .bak)." -ForegroundColor Yellow
}

if ($changedList.Count -gt 0) {
  Write-Host ""
  Write-Host "Changed files:" -ForegroundColor Yellow
  $changedList | ForEach-Object { Write-Host " - $_" }
}
