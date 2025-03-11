@echo off

:: %~1 is the first parameter, which is the file path of the dragged file
if "%~1"=="" (
    echo Please drag and drop a video file onto this script.
    pause
    exit /b
)

set "filename=%~1"

:: Make use of external "auto-subtitle" python script to generate the srt file
:: https://github.com/m1guelpf/auto-subtitle
:: Only English is needed for now, and `small.en` model seems to work the best
:: Larger models tend to generate weird subtitles containing only a bunch of dots
auto_subtitle --srt_only true --model "small.en" "%filename%"

pause
