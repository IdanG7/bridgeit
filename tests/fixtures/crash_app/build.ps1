# Build the crash_app test fixture.
# Uses cmake + Visual Studio 2022 generator. Produces:
#   build/Debug/crash_app.exe
#   build/Debug/crash_app.pdb

$ErrorActionPreference = "Stop"

$here = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $here

if (-not (Test-Path "build")) { New-Item -ItemType Directory -Path "build" | Out-Null }

cmake -S . -B build -G "Visual Studio 17 2022" -A x64
if ($LASTEXITCODE -ne 0) { throw "cmake configure failed" }

cmake --build build --config Debug
if ($LASTEXITCODE -ne 0) { throw "cmake build failed" }

Write-Host ""
Write-Host "Built: $here\build\Debug\crash_app.exe" -ForegroundColor Green
