[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [string]$Path,
  [switch]$Apply
)

function Fix-File($file){
  $lines = [System.Collections.Generic.List[string]]::new()
  [void]$lines.AddRange([System.IO.File]::ReadAllLines($file))

  $changed = $false
  $inFence = $false
  $fenceStart = -1
  $needsRaw = $false

  function IsFence([string]$s){
    return ($s -match '^\s*```')
  }

  function HasRawBefore([System.Collections.Generic.List[string]]$arr, [int]$idx){
    if($idx -gt 0){
      return ($arr[$idx-1] -match '^\s*\{\%\s*raw\s*\%\}\s*$')
    }
    return $false
  }

  function HasEndRawAfter([System.Collections.Generic.List[string]]$arr, [int]$idx){
    if($idx -lt $arr.Count-1){
      return ($arr[$idx+1] -match '^\s*\{\%\s*endraw\s*\%\}\s*$')
    }
    return $false
  }

  $i = 0
  while($i -lt $lines.Count){
    $line = $lines[$i]

    if(IsFence($line)){
      if(-not $inFence){
        # start code fence
        $inFence = $true
        $fenceStart = $i
        $needsRaw = $false
      } else {
        # end code fence
        if($needsRaw){
          # wstaw {% raw %} przed otwierającym fence (jeśli brak)
          if(-not (HasRawBefore $lines $fenceStart)){
            $lines.Insert($fenceStart, '{% raw %}')
            $changed = $true
            $i++              # przesuwamy indeks bo wstawiliśmy linię przed
            $fenceStart++     # start fence przesunął się o 1
          }
          # wstaw {% endraw %} po zamykającym fence (jeśli brak)
          if(-not (HasEndRawAfter $lines $i)){
            $lines.Insert($i+1, '{% endraw %}')
            $changed = $true
          }
        }
        $inFence = $false
        $fenceStart = -1
        $needsRaw = $false
      }
    } else {
      # zwykła linia
      if($inFence){
        if(($line -match '\{\{') -or ($line -match '\{\%')){
          $needsRaw = $true
        }
      }
    }
    $i++
  }

  if($Apply -and $changed){
    [System.IO.File]::WriteAllLines($file, $lines, [System.Text.UTF8Encoding]::new($true))
  }
  return $changed
}

# === MAIN ===
$files = Get-ChildItem -Path $Path -Recurse -Filter *.md | Sort-Object FullName
[int]$checked = 0; [int]$changed = 0; [int]$unchanged = 0
$changedList = @()

foreach($f in $files){
  $checked++
  $was = Fix-File -file $f.FullName
  if($was){
    $changed++
    $changedList += $f.FullName
  } else {
    $unchanged++
  }
}

if($Apply){
  Write-Host ""
  Write-Host "Checked: $checked"
  Write-Host "Changed: $changed"
  Write-Host "Unchanged: $unchanged"
  if($changedList.Count){
    Write-Host "`nChanged files:"; $changedList | ForEach-Object { Write-Host " - $_" }
  }
} else {
  Write-Host ""
  Write-Host "Preview mode. Use -Apply to write changes (creates no backups)."
  Write-Host "Checked: $checked"
  Write-Host "Would change: $changed"
  if($changedList.Count){
    Write-Host "`nWould change files:"; $changedList | ForEach-Object { Write-Host " - $_" }
  }
}
