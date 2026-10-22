@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

set "PY=%~dp0..\..\.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"

echo.
echo ============================================================
echo   测试本作业
echo   目录: %~dp0
echo ============================================================
echo.
echo   提示: 想只测某一题，可在此文件后加参数，例如:
echo     测试本作业.bat -q hailstone
echo.

"%PY%" "%~dp0ok" --local %*

echo.
pause
