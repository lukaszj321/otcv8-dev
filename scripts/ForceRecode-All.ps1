param([string]$Root = ".\docs")

$encLatin1   = [Text.Encoding]::GetEncoding(28591)
$encUtf8     = New-Object Text.UTF8Encoding($false)

$files = Get-ChildItem $Root -Recurse -Include *.md -File
foreach($f in $files){
  $rawUtf8 = [IO.File]::ReadAllBytes($f.FullName)
  $asText  = [Text.Encoding]::UTF8.GetString($rawUtf8)
  # BEZWZGLĘDNE przekodowanie Latin1->UTF8 (wymuszone)
  $forced  = [Text.Encoding]::UTF8.GetString($encLatin1.GetBytes($asText))
  $forced  = $forced -replace "`r`n","`n"
  [IO.File]::WriteAllText($f.FullName, $forced, $encUtf8)
  Write-Host ("Rewrote: {0}" -f $f.FullName)
}
