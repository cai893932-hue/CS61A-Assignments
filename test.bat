@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

set "PY=%~dp0.venv\Scripts\python.exe"
if not exist "%PY%" set "PY=python"

echo.
echo ============================================================
echo   CS61A 测试 - 自动检测你正在编辑的作业
echo ============================================================
echo.

"%PY%" "%~dp0test.py" %*

echo.
echo ============================================================
echo   常用命令:
echo     test.bat              自动检测并跑全部测试
echo     test.bat hw01         跑指定作业
echo     test.bat hw01 hailstone  只跑某一题
echo     test.bat --list       列出所有作业
echo ============================================================
echo.

if "%~1"=="" pause
