# 🚀 Démarrage rapide

## Test local (2 minutes)

### macOS / Linux
```bash
./run_local.sh
```

### Windows
Double-cliquez sur `run_local.bat`

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

---

## Déploiement en ligne (10 minutes)

### 1. Créer un dépôt GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/VOTRE-USERNAME/VOTRE-REPO.git
git push -u origin main
```

### 2. Déployer sur Streamlit Cloud

1. Allez sur [share.streamlit.io](https://share.streamlit.io/)
2. Connectez-vous avec GitHub
3. Cliquez sur "New app"
4. Sélectionnez votre dépôt et le fichier `app.py`
5. Cliquez sur "Deploy"

Votre app sera accessible via une URL publique en 2-5 minutes !

---

## Prochaines étapes

- 📖 Lisez le [README.md](README.md) pour plus de détails
- 🎨 Consultez le [GUIDE_MASQUE.md](GUIDE_MASQUE.md) pour créer vos masques
- 🚀 Consultez le [DEPLOIEMENT.md](DEPLOIEMENT.md) pour le guide complet

---

## Besoin d'aide ?

Vérifiez que vous avez bien:
- [ ] Python 3.8+ installé
- [ ] FFmpeg installé (`brew install ffmpeg` sur macOS)
- [ ] Les dépendances installées (`pip install -r requirements.txt`)

**Installation de FFmpeg:**
- macOS: `brew install ffmpeg`
- Ubuntu/Debian: `sudo apt install ffmpeg`
- Windows: [Télécharger ici](https://ffmpeg.org/download.html)
