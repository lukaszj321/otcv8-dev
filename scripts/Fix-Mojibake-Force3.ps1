param([string]$Root = ".\docs")

$targets = @(
  "api\engine\otclient_v_8_walidator_macierze_ast_i_round_trip_specyfikacja_techniczna.md",
  "build\android.md",
  "lua\api.md"
) | ForEach-Object { Join-Path $Root $_ }

$encLatin1   = [Text.Encoding]::GetEncoding(28591)
$encUtf8     = New-Object Text.UTF8Encoding($false)
$nbad = { param($s) ([regex]::Matches($s, "[\u00C2\u00C3\u00E2]")).Count } # Â Ã â

foreach($f in $targets){
  if(-not (Test-Path $f)){ Write-Host "SKIP (brak): $f"; continue }
  $bytes   = [IO.File]::ReadAllBytes($f)
  $asUtf8  = [Text.Encoding]::UTF8.GetString($bytes)
  $asFix   = [Text.Encoding]::UTF8.GetString($encLatin1.GetBytes($asUtf8))
  $asFix   = $asFix -replace "`r`n","`n"

  if((&$nbad $asFix) -lt (&$nbad $asUtf8)){
    [IO.File]::WriteAllText($f, $asFix, $encUtf8)
    Write-Host "FIX: $f"
  } else {
    Write-Host "OK : $f"
  }
}
