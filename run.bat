@echo off
REM === Path to QGIS's Python launcher ===
set QGIS_PY="C:\Program Files\QGIS 3.42.1\bin\python-qgis.bat"

REM === Check if the launcher exists ===
echo Checking for QGIS Python launcher at %QGIS_PY%
IF NOT EXIST %QGIS_PY% (
    echo ❌ ERROR: QGIS Python launcher not found!
    timeout /t 60
    exit /b 1
)

REM === Run the Python GUI script ===
echo ✅ Launching the Python script with GUI...
%QGIS_PY% "%~dp0program.py"

REM === Display completion message and keep window open ===
echo.
echo ✅ Script finished. Close this window when ready.
timeout /t 60