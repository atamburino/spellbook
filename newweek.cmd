@echo off
where py >nul 2>nul
if %errorlevel% equ 0 (
  py "%~dp0newweek.py" %*
) else (
  python "%~dp0newweek.py" %*
)
