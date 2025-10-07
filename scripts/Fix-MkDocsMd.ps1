<#!
Fix-MkDocsMd.ps1
- Skupia się WYŁĄCZNIE na plikach .md w podanym katalogu.
- Tryb podglądu (domyślny) pokazuje co byłoby zmienione.
- Tryb zapisu (-Apply) tworzy obok oryginału kopię .bak i nadpisuje plik.
- Naprawy:
  1) Usuwa artefakty: BOM, ZERO-WIDTH, SOFT HYPHEN, "¶", dziwne CR/LF.
  2) Normalizuje nagłówki: usuwa podwójne prefiksy "# # Tytuł" -> "## Tytuł",
     scala wielokrotne #/spacje do formy "# Tytuł" / "## Tytuł" itd.
  3) Ratuje bloki Jinja: paruje "{% raw %}" z "{% endraw %}".
     Jeśli plik ZACZYNA SIĘ od "{% raw %}" a zaraz potem jest nagłówek,
     usuwa to pierwsze "{% raw %}" (bo połykało H1).
  4) Domyka nieparzystą liczbę potrójnych backticków ``` (dodaje zamknięcie na końcu).
  5) Redukuje >2 pustych linii do maks 2 pod rząd.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [switch]$Apply,

    # Katalogi do pominięcia
    [string[]]$ExcludeDirs = @(
        '.git', 'site', '_site', 'node_modules', 'venv', '.venv',
        '.python', '__pycache__', '.cache', '.github'
    )
)

function Get-MdFiles {
    param([string]$Root, [string[]]$Skip)
    $rootFull = (Resolve-Path -Path $Root).Path
    Get-ChildItem -Path $rootFull -Recurse -File -Filter '*.md' |
    Where-Object {
        $rel = $_.FullName.Substring($rootFull.Length).TrimStart('\', '/')
        # odfiltruj po pierwszym segmentu ścieżki
        $firstSeg = ($rel -split '[\\/]')[0]
        ($Skip -notcontains $firstSeg)
    }
}

function Fix-Content {
    param([string]$Text)

    $orig = $Text

    # --- 1) Artefakty i whitespace ---
    # usuń BOM z początku
    $Text = $Text -replace '^\uFEFF', ''
    # zamień CRLF na LF, a potem wróć do CRLF na samym końcu (Windows)
    $Text = $Text -replace "`r`n", "`n"
    # usuń zero-width / soft hyphen / nietypowe znaki łamiące layout
    $zw = '[\u200B\u200C\u200D\u2060\uFEFF]'
    $Text = $Text -replace $zw, ''
    $Text = $Text -replace '\u00AD', ''  # soft hyphen
    $Text = $Text -replace '¶', ''       # paragraf z exportów
    # czasem markdown eksportuje spacje niełamliwe
    $Text = $Text -replace '\u00A0', ' '

    # --- 2) Normalizacja nagłówków ---
    $lines = $Text -split "`n", -1
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $ln = $lines[$i]

        # Usuwanie "podwójnego" prefiksu np. "# # Tytuł" -> "## Tytuł"
        if ($ln -match '^\s*#\s+#\s+(.+)$') {
            $lines[$i] = '## ' + $Matches[1]
            continue
        }
        if ($ln -match '^\s*#\s+##\s+(.+)$') {
            $lines[$i] = '### ' + $Matches[1]
            continue
        }
        if ($ln -match '^\s*#\s+###\s+(.+)$') {
            $lines[$i] = '#### ' + $Matches[1]
            continue
        }

        # Ściśnij nadmiar spacji między kratkami a tytułem: "##   T" -> "## T"
        if ($ln -match '^\s*#{1,6}\s+.+$') {
            $ln = $ln -replace '^(\s*#{1,6})\s+', '$1 '
        }

        # Ujednolicenie: jeśli ktoś zrobił "#    #    Tytuł" itp.
        $ln = $ln -replace '^\s*(#{1,6})\s+(#+)\s+', '${1}${2} '
        $lines[$i] = $ln
    }
    $Text = ($lines -join "`n")

    # --- 3) Bloki {% raw %} / {% endraw %} ---
    # a) jeśli plik zaczyna się od "{% raw %}" i następna niepusta linia to nagłówek,
    #    usuń to pierwsze "{% raw %}" (częsty powód „pustych” H1).
    $lines = $Text -split "`n", -1
    if ($lines.Count -gt 0 -and $lines[0].Trim() -eq '{% raw %}') {
        # znajdź pierwszą niepustą pozycję
        $idx = ($lines | Select-String -Pattern '\S' -SimpleMatch | Select-Object -First 1).LineNumber
        if ($idx -gt 1) {
            $firstNonEmpty = $lines[$idx - 1].Trim()
            if ($firstNonEmpty -match '^#{1,6}\s+.+') {
                # usuń leading "{% raw %}"
                $lines = $lines[1..($lines.Count - 1)]
            }
        }
    }
    $Text = ($lines -join "`n")

    # b) zrównoważ liczbę raw/endraw
    $rawCount = ([regex]::Matches($Text, '\{\%\s*raw\s*\%\}')).Count
    $endrawCount = ([regex]::Matches($Text, '\{\%\s*endraw\s*\%\}')).Count
    if ($rawCount -gt $endrawCount) {
        $Text = $Text.TrimEnd() + [Environment]::NewLine + '{% endraw %}' + [Environment]::NewLine
    }
    elseif ($endrawCount -gt $rawCount) {
        # zbyt dużo endraw – usuń nadmiarowy na końcu
        $diff = $endrawCount - $rawCount
        while ($diff -gt 0 -and $Text -match '(?s)(.*)\{\%\s*endraw\s*\%\}\s*$') {
            $Text = $Matches[1]
            $diff--
        }
        $Text += [Environment]::NewLine
    }

    # --- 4) Domykanie ``` fences ---
    $fenceCount = ([regex]::Matches($Text, '(?m)^\s*```')).Count
    if ($fenceCount % 2 -ne 0) {
        $Text = $Text.TrimEnd() + [Environment]::NewLine + '```' + [Environment]::NewLine
    }

    # --- 5) Redukcja nadmiarowych pustych linii (>2) ---
    # (zachowujemy max 2 puste linie pod rząd)
    # Zamień wystąpienia 3 lub więcej kolejnych LF na dokładnie dwa LF
    $Text = $Text -replace '(\n){3,}', "`n`n"

    # przywróć CRLF
    $Text = $Text -replace "`n", "`r`n"

    return @{ Changed = ($Text -ne $orig); NewText = $Text }
}

# --- Wykonanie ---
$files = Get-MdFiles -Root $Path -Skip $ExcludeDirs
if (-not $files) {
  Write-Host "Brak plików .md w '$Path' (po odfiltrowaniu katalogów)." -ForegroundColor Yellow
  exit 0
}

[int]$checked = 0
[int]$changed = 0
$changedList = New-Object System.Collections.Generic.List[string]

foreach ($f in $files) {
  $checked++
  $raw = Get-Content -LiteralPath $f.FullName -Raw -Encoding Byte
  # Wymuś odczyt jako UTF8 (bez BOM), bez ryzyka utraty bajtów
  $text = [System.Text.Encoding]::UTF8.GetString($raw)

  $res = Fix-Content -Text $text
  if ($res.Changed) {
    $changed++
    $changedList.Add($f.FullName)
    if ($Apply) {
      $bak = "$($f.FullName).bak"
      if (-not (Test-Path -LiteralPath $bak)) {
        [System.IO.File]::WriteAllBytes($bak, $raw)
      }
      Set-Content -LiteralPath $f.FullName -Value $res.NewText -Encoding UTF8
      Write-Host "Fix: $($f.FullName)" -ForegroundColor Green
    }
  }
}

Write-Host ""
Write-Host ("Checked: {0}" -f $checked)
Write-Host ("Changed: {0}" -f $changed)
Write-Host ("Unchanged: {0}" -f ($checked - $changed))
Write-Host ""

if (-not $Apply) {
  Write-Host "Preview mode. Use -Apply to write changes (creates .bak)." -ForegroundColor Yellow
  if ($changed -gt 0) {
    Write-Host "`nChanged files:" -ForegroundColor Cyan
    $changedList | ForEach-Object { Write-Host " - $($_)" }
  }
} else {
  Write-Host "Apply mode. Changes written. Backups *.bak created next to files." -ForegroundColor Cyan
  if ($changed -gt 0) {
    Write-Host "`nChanged files:" -ForegroundColor Cyan
    $changedList | ForEach-Object { Write-Host " - $($_)" }
  }
}
