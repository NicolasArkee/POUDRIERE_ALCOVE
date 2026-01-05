# 🎭 Video Masker pour Alcôve

Application Streamlit pour transformer vos vidéos en format 16:9 avec un masque personnalisé, idéal pour les projections en alcôve.

## ✨ Fonctionnalités

- **Upload facile**: Glissez-déposez votre vidéo et votre masque PNG
- **Conversion automatique**: Transforme n'importe quel ratio vidéo en 16:9
- **Masquage personnalisé**: Applique votre masque PNG avec transparence
- **Paramètres ajustables**: Résolution, qualité et vitesse d'encodage
- **Prévisualisation**: Visualisez le résultat avant de télécharger
- **Support multi-formats**: MP4, MOV, AVI, MKV, WebM

## 🚀 Déploiement en ligne (Streamlit Community Cloud)

### Étape 1: Préparer votre dépôt GitHub

1. Créez un nouveau dépôt sur GitHub (public ou privé)
2. Clonez ce projet et poussez-le sur votre dépôt:

```bash
git init
git add .
git commit -m "Initial commit - Video Masker App"
git branch -M main
git remote add origin https://github.com/VOTRE-USERNAME/VOTRE-REPO.git
git push -u origin main
```

### Étape 2: Déployer sur Streamlit Cloud

1. Allez sur [share.streamlit.io](https://share.streamlit.io/)
2. Connectez-vous avec votre compte GitHub
3. Cliquez sur **"New app"**
4. Sélectionnez:
   - **Repository**: Votre dépôt GitHub
   - **Branch**: main
   - **Main file path**: app.py
5. Cliquez sur **"Deploy"**

L'application sera accessible via une URL publique comme: `https://votre-app.streamlit.app`

### Étape 3: Configuration avancée (optionnel)

Si vous avez besoin de modifier les limites d'upload ou d'autres paramètres, vous pouvez éditer le fichier [.streamlit/config.toml](.streamlit/config.toml).

## 💻 Installation locale

Si vous préférez exécuter l'application en local:

### Prérequis

- Python 3.8 ou supérieur
- FFmpeg installé sur votre système

#### Installation de FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Téléchargez depuis [ffmpeg.org](https://ffmpeg.org/download.html) et ajoutez-le au PATH.

### Installation et lancement

```bash
# Cloner le projet
git clone https://github.com/VOTRE-USERNAME/VOTRE-REPO.git
cd VOTRE-REPO

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse: `http://localhost:8501`

## 📋 Structure du projet

```
.
├── app.py                    # Application Streamlit principale
├── requirements.txt          # Dépendances Python
├── packages.txt             # Dépendances système (pour Streamlit Cloud)
├── .streamlit/
│   └── config.toml          # Configuration Streamlit
└── README.md                # Ce fichier
```

## 🎨 Création d'un masque PNG

Pour créer votre masque PNG personnalisé:

1. Créez une image en résolution 16:9 (ex: 1920x1080)
2. Les zones **noires opaques** masqueront la vidéo
3. Les zones **transparentes** laisseront passer la vidéo
4. Exportez en PNG avec canal alpha (transparence)

Logiciels recommandés:
- Adobe Photoshop
- GIMP (gratuit)
- Affinity Photo
- Canva (en ligne)

## ⚙️ Paramètres disponibles

| Paramètre | Description | Valeurs recommandées |
|-----------|-------------|---------------------|
| **Résolution** | Taille de sortie de la vidéo | 1920x1080 pour Full HD |
| **Qualité (CRF)** | Compromis qualité/taille | 18-23 (18 = meilleure qualité) |
| **Vitesse d'encodage** | Rapidité vs compression | fast ou medium |

## 🔧 Comment ça fonctionne ?

L'application utilise FFmpeg avec les filtres suivants:

1. **Scale**: Redimensionne la vidéo pour qu'elle rentre dans le cadre 16:9
2. **Pad**: Ajoute des bandes noires si nécessaire (vidéos verticales ou 4:3)
3. **Overlay**: Applique le masque PNG par-dessus le résultat

```bash
ffmpeg -i video.mp4 -i masque.png \
  -filter_complex "[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,\
  pad=1920:1080:(ow-iw)/2:(oh-ih)/2[bg];[bg][1:v]overlay=0:0[out]" \
  -map "[out]" -c:v libx264 -crf 18 output.mp4
```

## 📊 Limites

### Streamlit Community Cloud (gratuit)

- **Taille d'upload**: 1 Go maximum (configurable dans config.toml)
- **RAM**: Limitée (peut crasher sur vidéos 4K très longues)
- **Vitesse**: Dépend des ressources partagées du cloud

### Solution pour vidéos très lourdes

Pour les vidéos de plus de 1 Go ou 4K très longues, privilégiez l'installation locale.

## 🛠️ Dépannage

### L'application plante lors du traitement

- Réduisez la résolution de sortie (essayez 1280x720)
- Utilisez un preset plus rapide (ultrafast)
- Compressez votre vidéo avant upload

### FFmpeg introuvable (local)

Vérifiez que FFmpeg est bien installé:
```bash
ffmpeg -version
```

### Le masque ne s'affiche pas correctement

- Vérifiez que votre PNG a bien un canal alpha (transparence)
- Assurez-vous que le ratio est bien 16:9

## 📝 Licence

Ce projet est open source. Vous êtes libre de l'utiliser et de le modifier selon vos besoins.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à:
- Reporter des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation

## 📧 Support

Pour toute question ou problème, ouvrez une issue sur GitHub.

---

**Fait avec ❤️ pour les projections en alcôve**
