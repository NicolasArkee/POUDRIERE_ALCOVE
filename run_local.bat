@echo off
echo 🎭 Video Masker pour Alcôve - Lancement local
echo ==============================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python n'est pas installé. Veuillez l'installer d'abord.
    pause
    exit /b 1
)

REM Vérifier si FFmpeg est installé
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ FFmpeg n'est pas installé.
    echo Téléchargez-le depuis: https://ffmpeg.org/download.html
    pause
    exit /b 1
)

echo ✅ Python et FFmpeg détectés
echo.

REM Créer un environnement virtuel si nécessaire
if not exist "venv" (
    echo 📦 Création de l'environnement virtuel...
    python -m venv venv
)

REM Activer l'environnement virtuel
echo 🔧 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances
echo 📥 Installation des dépendances...
pip install -q -r requirements.txt

echo.
echo 🚀 Lancement de l'application Streamlit...
echo    L'application s'ouvrira dans votre navigateur
echo    Appuyez sur Ctrl+C pour arrêter
echo.

REM Lancer Streamlit
streamlit run app.py

pause
