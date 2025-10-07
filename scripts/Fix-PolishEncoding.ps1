# scripts/Fix-PolishEncoding.ps1
param(
    [Parameter(Mandatory = $true)][string]$Path,
    [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-Bytes($file) { [IO.File]::ReadAllBytes($file) }
function Write-Utf8NoBom($file, [string]$text) {
    $enc = [Text.UTF8Encoding]::new($false)  # no BOM
    [IO.File]::WriteAllBytes($file, $enc.GetBytes($text))
}

function Is-ValidUtf8([byte[]]$bytes) {
    try { [void][Text.UTF8Encoding]::new($true, $true).GetString($bytes); $true } catch { $false }
}

# Zestaw polskich liter (małe + wielkie), zbudowany z kodów unicode
$PolishChars = [char[]]@(
    0x0105, 0x0107, 0x0119, 0x0142, 0x0144, 0x00F3, 0x015B, 0x017A, 0x017C, # ąćęłńóśźż
    0x0104, 0x0106, 0x0118, 0x0141, 0x0143, 0x00D3, 0x015A, 0x0179, 0x017B  # ĄĆĘŁŃÓŚŹŻ
)
function Contains-Polish([string]$s) {
    if ([string]::IsNullOrEmpty($s)) { return $false }
    return $s.IndexOfAny($PolishChars) -ge 0
}

# Typowe „krzaczkowe” markery mojibake: 'Ã'(C3), 'Â'(C2), 'Ä'(C4), 'Ĺ'(0139)
$JunkMarkers = [char[]]@(0x00C3, 0x00C2, 0x00C4, 0x0139)
function Looks-Mojibake([string]$s) {
    if ([string]::IsNullOrEmpty($s)) { return $false }
    return $s.IndexOfAny($JunkMarkers) -ge 0
}

# Od-„mojibakowanie”: potraktuj zły tekst jako bajty w 1250/1252 i zdekoduj UTF-8
function Undo-Mojibake([string]$s) {
    $enc1250 = [Text.Encoding]::GetEncoding(1250)
    $enc1252 = [Text.Encoding]::GetEncoding(1252)
    $utf8 = [Text.Encoding]::UTF8

    if (-not (Looks-Mojibake $s)) { return $s }

    # próba 1: 1250 -> UTF8
    try {
        $b1250 = $enc1250.GetBytes($s)
        $t1 = $utf8.GetString($b1250)
        if (Contains-Polish $t1) { return $t1 }
    }
    catch {}

    # próba 2: 1252 -> UTF8
    try {
        $b1252 = $enc1252.GetBytes($s)
        $t2 = $utf8.GetString($b1252)
        if (Contains-Polish $t2) { return $t2 }
    }
    catch {}

    return $s
}

# Naprawa nagłówków typu "# ¦ Modul: ..." (0x00A6 to '¦')
$BrokenBar = [char]0x00A6
function Cleanup-Headers([string]$text) {
    $lines = ($text -replace "`r`n", "`n").Split("`n")
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        if ($line -match '^\s*#') {
            # zamień "#  ¦  Modul:" -> "# Modul:"
            $line = $line -replace ('^\s*#\s*' + [Regex]::Escape($BrokenBar) + '\s*Modul\s*:'), '# Modul:'
        }
        $lines[$i] = $line
    }
    # koniec linii LF + końcowy newline
    return ([string]::Join("`n", $lines)).TrimEnd() + "`n"
}

$files = Get-ChildItem -Path $Path -Recurse -File -Filter *.md
$changed = @()
$checked = 0

foreach ($f in $files) {
    $checked++

    $bytes = Get-Bytes $f.FullName
    $utf8Strict = [Text.UTF8Encoding]::new($true, $true)
    $utf8Loose = [Text.Encoding]::UTF8
    $cp1250 = [Text.Encoding]::GetEncoding(1250)

    $finalText = $null
    $mode = $null

    if (Is-ValidUtf8 $bytes) {
        # Prawidłowe UTF-8, ale mogło utrwalić mojibake w samym tekście
        $t = $utf8Loose.GetString($bytes)
        if (Looks-Mojibake $t) {
            $fixed = Undo-Mojibake $t
            if ($fixed -ne $t) {
                $finalText = $fixed
                $mode = 'utf8(mojibake)->utf8'
            }
        }
    }
    else {
        # Nie-UTF8 -> spróbuj CP-1250
        try {
            $t1250 = $cp1250.GetString($bytes)
            $finalText = $t1250
            $mode = 'cp1250->utf8'
        }
        catch {}
    }

    if (-not $finalText) {
        continue
    }

    # Porządki: nagłówki + LF + końcowy newline
    $finalText = Cleanup-Headers $finalText

    if ($Apply) {
        $bak = "$($f.FullName).bak"
        if (-not (Test-Path $bak)) { Copy-Item $f.FullName $bak }
        Write-Utf8NoBom $f.FullName $finalText
        $changed += , ([pscustomobject]@{ File = $f.FullName; Mode = $mode })
    }
    else {
        $changed += , ([pscustomobject]@{ File = $f.FullName; Mode = "$mode (preview)" })
    }
}

"{0}: {1}" -f 'Checked', $checked
$status = if ($Apply) { 'Changed' } else { 'Would change' }
"{0}: {1}" -f $status, $changed.Count

if ($changed.Count) {
    # print header with newline
    "{0} files:`n" -f $status | Write-Output
    foreach ($item in $changed) {
        ' - ' + $item.File + '  [' + $item.Mode + ']'
    }
}
else {
    "`nNo changes needed."
}
