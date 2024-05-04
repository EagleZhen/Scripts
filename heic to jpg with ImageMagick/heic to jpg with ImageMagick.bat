@echo off
setlocal enabledelayedexpansion

:: Check if ImageMagick is installed
where magick >nul 2>&1
if %errorlevel% neq 0 (
    echo ImageMagick not found. Please install it from https://imagemagick.org/script/download.php and add it to PATH first.
    pause
    exit /b
)

:: Loop through each file dragged onto the script
for %%f in (%*) do (
    echo Processing: %%f
    magick convert "%%f" "%%~dpnf.jpg"
    echo Converted: %%f to %%~dpnf.jpg
)

echo All files have been processed.
pause
