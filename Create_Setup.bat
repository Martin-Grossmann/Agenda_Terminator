@echo off
REM Script pour générer le Setup Inno Setup automatiquement et le copier sur le Desktop

setlocal enabledelayedexpansion

set "SCRIPT_DIR=%~dp0"
set "ISS_FILE=%SCRIPT_DIR%Setup_Ajout_Bureau.iss"
set "INNO_PATH=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
set "DESKTOP=%USERPROFILE%\Desktop"

echo ================================================================================
echo GENERATION DU SETUP AVEC INNO SETUP
echo ================================================================================

REM Vérifier que le fichier .iss existe
if not exist "%ISS_FILE%" (
    echo ❌ Erreur: %ISS_FILE% non trouvé
    exit /b 1
)

REM Vérifier que Inno Setup est installé
if not exist "%INNO_PATH%" (
    echo ❌ Erreur: Inno Setup n'est pas installé
    echo    Télécharge-le depuis: https://jrsoftware.org/isdl.php
    exit /b 1
)

echo ✓ Fichier ISS: %ISS_FILE%
echo ✓ Inno Setup: %INNO_PATH%
echo ✓ Desktop: %DESKTOP%

echo.
echo ================================================================================
echo Lancement de la compilation...
echo ================================================================================

REM Compiler le Setup
"%INNO_PATH%" "%ISS_FILE%"

if errorlevel 1 (
    echo ❌ Erreur lors de la compilation du Setup
    exit /b 1
)

echo.
echo ================================================================================
echo Copie du Setup sur le Desktop...
echo ================================================================================

REM Copier le Setup sur le Desktop
for /r "%SCRIPT_DIR%Output_Setup" %%F in (*.exe) do (
    echo Copie: %%~nxF vers le Desktop
    copy "%%F" "%DESKTOP%\%%~nxF"
    if errorlevel 1 (
        echo ❌ Erreur lors de la copie
        exit /b 1
    )
)

echo.
echo ✅ Setup créé et copié avec succès sur le Desktop!
echo.
pause
