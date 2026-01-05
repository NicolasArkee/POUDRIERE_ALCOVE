# 🎨 Guide de création de masque PNG

## Qu'est-ce qu'un masque pour alcôve ?

Un masque est une image PNG avec transparence qui se superpose à votre vidéo pour créer un effet de cadre ou de forme personnalisée. Les zones opaques (noires) cachent la vidéo, tandis que les zones transparentes laissent passer l'image.

## Spécifications techniques

### Dimensions requises
- **Ratio**: 16:9 obligatoire
- **Résolutions recommandées**:
  - Full HD: 1920x1080 pixels
  - HD: 1280x720 pixels
  - 4K: 3840x2160 pixels

### Format
- **Type**: PNG
- **Canal alpha**: Obligatoire (transparence)
- **Profondeur**: 8 bits minimum

## Exemples d'utilisation

### 1. Masque circulaire/ovale (projection en alcôve)
```
┌─────────────────────────┐
│ ███████████████████████ │  ← Zone opaque (noire)
│ ████╔═══════════╗█████ │
│ ███║             ║████ │
│ ███║  TRANSPARENT ║████ │  ← Zone transparente (vidéo visible)
│ ███║             ║████ │
│ ████╚═══════════╝█████ │
│ ███████████████████████ │
└─────────────────────────┘
```

### 2. Masque avec bordure décorative
```
┌─────────────────────────┐
│ ╔═══════════════════╗   │  ← Bordure opaque
│ ║                   ║   │
│ ║   TRANSPARENT     ║   │  ← Vidéo visible au centre
│ ║                   ║   │
│ ╚═══════════════════╝   │
└─────────────────────────┘
```

### 3. Masque asymétrique (effet architectural)
```
┌─────────────────────────┐
│ ████╔══════════════════╗│
│ ███║                   ║│
│ ██║   TRANSPARENT      ║│
│ █║                     ║│
│ ║                      ║│
│ ╚══════════════════════╝│
└─────────────────────────┘
```

## Tutoriel: Créer un masque avec GIMP (gratuit)

### Étape 1: Créer le document
1. Ouvrir GIMP
2. Fichier → Nouvelle image
3. Taille: 1920x1080 pixels
4. Options avancées → Remplir avec: Transparence
5. Cliquer sur "Valider"

### Étape 2: Ajouter un calque noir
1. Calque → Nouveau calque
2. Nom: "Masque"
3. Remplir avec: Noir
4. Cliquer sur "Valider"

### Étape 3: Créer la zone transparente
1. Sélectionner l'outil Ellipse (ou Rectangle)
2. Dessiner la forme où la vidéo sera visible
3. Édition → Effacer (touche Suppr)
4. La zone devient transparente (damier gris/blanc)

### Étape 4: Adoucir les bords (optionnel)
1. Sélection → Adoucir
2. Rayon: 20-50 pixels
3. Édition → Effacer

### Étape 5: Exporter
1. Fichier → Exporter sous
2. Nom: `masque_alcove.png`
3. Type: PNG
4. Cocher "Enregistrer le canal alpha"
5. Exporter

## Tutoriel: Créer un masque avec Photoshop

### Étape 1: Créer le document
1. Fichier → Nouveau
2. Largeur: 1920 px, Hauteur: 1080 px
3. Contenu de l'arrière-plan: Transparent

### Étape 2: Ajouter le masque noir
1. Nouveau calque
2. Remplir avec du noir (Alt + Backspace)

### Étape 3: Créer la zone transparente
1. Outil Ellipse de sélection (M)
2. Dessiner la forme
3. Touche Suppr pour effacer

### Étape 4: Adoucir (optionnel)
1. Sélection → Modifier → Contour progressif
2. Rayon: 20-50 px

### Étape 5: Exporter
1. Fichier → Enregistrer sous
2. Format: PNG
3. Cocher "Transparence"

## Astuces et conseils

### ✅ Bonnes pratiques

- **Tester d'abord en basse résolution** (720p) pour itérer rapidement
- **Prévoir une marge de sécurité** de 5-10% sur les bords
- **Utiliser un contour progressif** pour un rendu plus doux
- **Vérifier la transparence** en plaçant un fond coloré temporaire

### ❌ Erreurs courantes

- **Oublier le canal alpha**: Le masque doit être en PNG avec transparence
- **Mauvais ratio**: Respecter le 16:9 sinon le masque sera déformé
- **Zones grises**: Utiliser du noir pur (0,0,0) pour les zones opaques
- **Fichier trop lourd**: Optimiser le PNG (pas besoin de 4K pour un masque simple)

## Outils en ligne (sans installation)

### Photopea (gratuit)
- URL: https://www.photopea.com
- Clone de Photoshop dans le navigateur
- Supporte PNG avec transparence

### Canva (freemium)
- URL: https://www.canva.com
- Plus simple mais moins de contrôle
- Télécharger en PNG avec transparence

## Ressources et templates

### Formes géométriques de base
- Cercle parfait: Maintenir Shift pendant le tracé
- Ovale horizontal: Plus large que haut
- Ovale vertical: Plus haut que large
- Rectangle arrondi: Utiliser l'outil Rectangle avec coins arrondis

### Effets avancés
- **Dégradé de transparence**: Masque qui s'estompe progressivement
- **Bordure lumineuse**: Ajouter un liseré blanc semi-transparent
- **Effet vignette**: Assombrir les coins

## Validation de votre masque

Avant d'utiliser votre masque dans l'application, vérifiez:

1. ✅ **Dimensions**: 16:9 (ex: 1920x1080)
2. ✅ **Format**: PNG
3. ✅ **Transparence**: Canal alpha présent
4. ✅ **Zones noires**: Bien opaques (alpha = 255)
5. ✅ **Zones transparentes**: Bien transparentes (alpha = 0)

### Test rapide
Ouvrez votre masque dans un éditeur d'image et placez un fond coloré derrière:
- Les zones colorées visibles = vidéo visible
- Les zones noires = vidéo cachée

---

**Besoin d'aide ?** Testez d'abord avec un masque simple (cercle noir avec trou transparent au centre) pour comprendre le principe.
