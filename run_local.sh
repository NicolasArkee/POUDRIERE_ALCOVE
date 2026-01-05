#!/bin/bash

echo "🎭 Video Masker pour Alcôve - Lancement local"
echo "=============================================="
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si FFmpeg est installé
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg n'est pas installé."
    echo "Installation:"
    echo "  macOS: brew install ffmpeg"
    echo "  Ubuntu/Debian: sudo apt install ffmpeg"
    exit 1
fi

echo "✅ Python et FFmpeg détectés"
echo ""

# Créer un environnement virtuel si nécessaire
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances
echo "📥 Installation des dépendances..."
pip install -q -r requirements.txt

echo ""
echo "🚀 Lancement de l'application Streamlit..."
echo "   L'application s'ouvrira dans votre navigateur"
echo "   Appuyez sur Ctrl+C pour arrêter"
echo ""

# Lancer Streamlit
streamlit run app.py
