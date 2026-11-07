@echo off
setlocal
title Portfolio Local Preview Server

:: Try python, py launcher, or standard Python installation path
where python >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=python"
    goto RUN
)

where py >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "PY_CMD=py"
    goto RUN
)

if exist "C:\Program Files\Python315\python.exe" (
    set "PY_CMD=C:\Program Files\Python315\python.exe"
    goto RUN
)

echo [ERROR] Python was not found on your system.
pause
exit /b 1

:RUN
cd /d "%~dp0"
"%PY_CMD%" "%~dp0serve.py"
if %ERRORLEVEL% neq 0 (
    pause
)
