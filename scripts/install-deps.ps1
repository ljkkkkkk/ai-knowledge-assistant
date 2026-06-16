$ErrorActionPreference = "Stop"

$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$TmpDir = Join-Path $ProjectRoot ".tmp"
$PipCacheDir = Join-Path $TmpDir ".pip-cache"

New-Item -ItemType Directory -Force -Path $TmpDir | Out-Null
New-Item -ItemType Directory -Force -Path $PipCacheDir | Out-Null

$env:TEMP = $TmpDir
$env:TMP = $TmpDir
$env:PIP_CACHE_DIR = $PipCacheDir

& (Join-Path $ProjectRoot ".venv\Scripts\python.exe") -m pip install --cache-dir $PipCacheDir -r (Join-Path $ProjectRoot "requirements.txt")

