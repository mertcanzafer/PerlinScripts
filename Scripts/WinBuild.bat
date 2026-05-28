@echo off
setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
for %%I in ("%SCRIPT_DIR%..") do set "ROOT_DIR=%%~fI"
set "BUILD_DIR=%ROOT_DIR%\build"
set "KTX=%ROOT_DIR%\ThirdParty\ktx\bin\ktx.exe"
set "TEX=%ROOT_DIR%\Assets\Textures"

echo Checking texture conversions...

if not exist "%KTX%" (
    echo ERROR: ktx.exe not found:
    echo %KTX%
    pause
    exit /b 1
)

if not exist "%TEX%" (
    echo ERROR: Texture folder not found:
    echo %TEX%
    pause
    exit /b 1
)

set "FOUND_TEX=0"
for %%E in (png jpg jpeg) do (
    for %%F in ("%TEX%\*.%%E") do (
        set "FOUND_TEX=1"
        set "INPUT=%%~fF"
        set "OUTPUT=%%~dpnF.ktx2"
        set "NAME=%%~nxF"
        if not exist "!OUTPUT!" (
            echo Converting !NAME! ...
            "%KTX%" create --format R8G8B8A8_SRGB "!INPUT!" "!OUTPUT!"
            if errorlevel 1 (
                echo ERROR: Failed to convert !NAME!
                pause
                exit /b 1
            )
        ) else (
            echo Skipping !NAME!, %%~nF.ktx2 already exists.
        )
    )
)
if "%FOUND_TEX%"=="0" (
    echo No PNG or JPEG files found in:
    echo %TEX%
)

echo Texture conversion step complete.

if not exist "%BUILD_DIR%" (
    mkdir "%BUILD_DIR%"
    if errorlevel 1 (
        echo ERROR: Failed to create build directory.
        pause
        exit /b 1
    )
)

cd /d "%BUILD_DIR%"
cmake "%ROOT_DIR%" -DCMAKE_POLICY_VERSION_MINIMUM=3.5
if errorlevel 1 (
    echo ERROR: CMake configure failed.
    pause
    exit /b 1
)

echo Done.
pause
exit /b 0
