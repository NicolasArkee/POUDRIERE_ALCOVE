# 🚀 Guide de déploiement complet

Ce guide vous accompagne pas à pas pour déployer votre application Video Masker en ligne, gratuitement.

## Option 1: Streamlit Community Cloud (Recommandé - Gratuit)

### Avantages
- ✅ Gratuit et illimité
- ✅ Déploiement automatique depuis GitHub
- ✅ HTTPS inclus
- ✅ Mises à jour automatiques
- ✅ Aucune configuration serveur

### Prérequis
- Un compte GitHub (gratuit)
- Un compte Streamlit (gratuit, connexion via GitHub)

---

## Étape 1: Créer un dépôt GitHub

### 1.1 Créer le dépôt en ligne
1. Allez sur [github.com](https://github.com)
2. Cliquez sur le bouton "+" en haut à droite
3. Sélectionnez "New repository"
4. Remplissez:
   - **Repository name**: `video-masker-alcove` (ou autre nom)
   - **Description**: "Application de masquage vidéo pour projections en alcôve"
   - **Visibilité**: Public ou Private (les deux fonctionnent)
   - **NE PAS** cocher "Add a README file"
5. Cliquez sur "Create repository"

### 1.2 Pousser votre code sur GitHub

Ouvrez un terminal dans le dossier de votre projet et exécutez:

```bash
# Initialiser le dépôt Git
git init

# Ajouter tous les fichiers
git add .

# Créer le premier commit
git commit -m "Initial commit - Video Masker App"

# Renommer la branche en 'main'
git branch -M main

# Ajouter le dépôt distant (remplacez par votre URL)
git remote add origin https://github.com/VOTRE-USERNAME/video-masker-alcove.git

# Pousser le code
git push -u origin main
```

**Note**: Remplacez `VOTRE-USERNAME` par votre nom d'utilisateur GitHub et `video-masker-alcove` par le nom de votre dépôt.

---

## Étape 2: Déployer sur Streamlit Cloud

### 2.1 Accéder à Streamlit Cloud
1. Allez sur [share.streamlit.io](https://share.streamlit.io/)
2. Cliquez sur "Sign up" ou "Sign in"
3. Choisissez "Continue with GitHub"
4. Autorisez Streamlit à accéder à vos dépôts

### 2.2 Créer une nouvelle application
1. Cliquez sur le bouton **"New app"** (ou "Create app")
2. Remplissez le formulaire:
   - **Repository**: Sélectionnez `VOTRE-USERNAME/video-masker-alcove`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Cliquez sur **"Deploy!"**

### 2.3 Attendre le déploiement
- Le déploiement prend 2-5 minutes
- Vous verrez les logs en temps réel
- Une fois terminé, vous obtiendrez une URL comme: `https://video-masker-alcove.streamlit.app`

---

## Étape 3: Configuration avancée (optionnel)

### 3.1 Personnaliser l'URL
1. Dans Streamlit Cloud, allez dans les paramètres de votre app
2. Section "General"
3. Modifiez le champ "App URL"

### 3.2 Ajouter des secrets (si nécessaire)
Si vous avez besoin de clés API ou mots de passe:
1. Allez dans les paramètres de votre app
2. Section "Secrets"
3. Ajoutez vos secrets au format TOML:
```toml
API_KEY = "votre-cle-secrete"
```

### 3.3 Augmenter les limites de ressources
Dans [.streamlit/config.toml](.streamlit/config.toml), vous pouvez modifier:
```toml
[server]
maxUploadSize = 1000  # Taille max en MB (défaut: 200)

[browser]
gatherUsageStats = false  # Désactiver les stats
```

---

## Étape 4: Mettre à jour l'application

Pour déployer une nouvelle version:

```bash
# Modifier vos fichiers localement
# puis:

git add .
git commit -m "Description de vos modifications"
git push
```

Streamlit Cloud détectera automatiquement les changements et redéploiera l'app en 1-2 minutes.

---

## Option 2: Autres plateformes de déploiement

### Hugging Face Spaces (Alternative gratuite)

**Avantages**: GPU gratuit disponible, communauté ML

**Étapes**:
1. Créez un compte sur [huggingface.co](https://huggingface.co)
2. Créez un nouveau Space
3. Choisissez "Streamlit" comme SDK
4. Uploadez vos fichiers ou connectez à GitHub

### Render (Freemium)

**Avantages**: Plus de ressources, PostgreSQL gratuit

**Limites**: 750h/mois gratuit, puis payant

**Étapes**:
1. Créez un compte sur [render.com](https://render.com)
2. Créez un nouveau "Web Service"
3. Connectez votre dépôt GitHub
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `streamlit run app.py --server.port $PORT`

### Railway (Freemium)

**Avantages**: Très simple, déploiement rapide

**Limites**: 5$ de crédit gratuit/mois

**Étapes**:
1. Créez un compte sur [railway.app](https://railway.app)
2. Créez un nouveau projet depuis GitHub
3. Railway détecte automatiquement Streamlit

---

## Résolution de problèmes

### ❌ Erreur: "FFmpeg not found"
**Solution**: Vérifiez que `packages.txt` contient bien `ffmpeg`

### ❌ Erreur: "File too large"
**Solution**: Augmentez `maxUploadSize` dans `.streamlit/config.toml`

### ❌ L'application crash lors du traitement
**Solutions**:
- Réduisez la résolution de sortie (1280x720 au lieu de 1920x1080)
- Utilisez un preset plus rapide (`ultrafast` au lieu de `fast`)
- Compressez la vidéo avant upload

### ❌ Le déploiement échoue
**Vérifications**:
1. `requirements.txt` est bien présent
2. `packages.txt` contient `ffmpeg`
3. `app.py` est à la racine du projet
4. Pas d'erreurs de syntaxe Python

### ❌ Les vidéos ne se téléchargent pas
**Solution**: Vérifiez que votre navigateur autorise les téléchargements depuis le site

---

## Monitoring et logs

### Accéder aux logs
1. Dans Streamlit Cloud, ouvrez votre app
2. Cliquez sur "Manage app" (en bas à droite)
3. Onglet "Logs"

### Surveiller l'utilisation
- Streamlit Cloud vous envoie un email si l'app crash
- Consultez les métriques dans le dashboard

---

## Sécurité et bonnes pratiques

### ✅ À faire
- Validez les types de fichiers uploadés
- Limitez la taille des uploads
- Nettoyez les fichiers temporaires après traitement
- Utilisez HTTPS (inclus par défaut sur Streamlit Cloud)

### ❌ À éviter
- Ne committez JAMAIS de clés API dans le code
- N'acceptez pas de fichiers non vidéo dans l'upload vidéo
- Ne stockez pas les vidéos des utilisateurs

---

## Personnalisation de l'URL et branding

### Nom de domaine personnalisé
Streamlit Cloud gratuit ne permet pas de domaine personnalisé, mais vous pouvez:
1. Utiliser un redirecteur d'URL gratuit (bit.ly, tinyurl)
2. Passer à Streamlit Cloud Teams (payant) pour un domaine custom

### Personnaliser l'apparence
Modifiez [.streamlit/config.toml](.streamlit/config.toml):
```toml
[theme]
primaryColor = "#FF4B4B"        # Couleur principale
backgroundColor = "#0E1117"      # Fond
secondaryBackgroundColor = "#262730"  # Fond secondaire
textColor = "#FAFAFA"           # Texte
font = "sans serif"             # Police
```

---

## Coûts et limitations

### Streamlit Community Cloud (Gratuit)
- **Apps**: Illimitées
- **Stockage**: 1 GB par app
- **RAM**: ~1 GB
- **CPU**: Partagé
- **Bande passante**: Illimitée

### Si vous avez besoin de plus
- **Streamlit Cloud Teams**: 250$/mois (ressources dédiées)
- **Auto-hébergement**: Sur votre propre serveur (AWS, DigitalOcean, etc.)

---

## Support et communauté

### Obtenir de l'aide
- **Forum Streamlit**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **GitHub Issues**: Pour reporter des bugs

### Partager votre app
Une fois déployée, partagez simplement l'URL:
```
https://votre-app.streamlit.app
```

---

## Checklist finale avant déploiement

- [ ] Tous les fichiers sont dans le dépôt GitHub
- [ ] `requirements.txt` contient `streamlit`
- [ ] `packages.txt` contient `ffmpeg`
- [ ] `.streamlit/config.toml` est configuré
- [ ] Le code fonctionne en local (`streamlit run app.py`)
- [ ] Les fichiers sensibles sont dans `.gitignore`
- [ ] Le README est à jour

---

**Félicitations !** Votre application est maintenant accessible au monde entier 🎉

Pour toute question, consultez la [documentation Streamlit](https://docs.streamlit.io/streamlit-community-cloud/get-started) ou ouvrez une issue sur GitHub.
