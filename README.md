# Guide d'utilisation avec Visual Studio / VS Code

## Adaptations effectuées

### 1. **Encodage UTF-8**
- Ajout de `# -*- coding: utf-8 -*-` en tête de tous les fichiers
- Toutes les opérations de fichiers JSON utilisent `encoding='utf-8'`

### 2. **Gestion des imports**
- Suppression des imports en double (`datetime` importé deux fois)
- Réorganisation logique des imports
- Imports absolus plutôt que relatifs

### 3. **Chemins de fichiers**
- Utilisation de `os.path.join()` à la place de concaténation avec `/`
- Compatible avec Windows, macOS et Linux
- Chemin dynamique pour les ressources (Agenda.png) : `os.path.dirname(os.path.abspath(__file__))`

### 4. **Gestion des fichiers JSON**
- Ajout de gestion d'erreur avec try/except
- Encodage UTF-8 explicite lors de la lecture/écriture
- Paramètre `ensure_ascii=False` pour préserver les caractères accentués

### 5. **Code formatage**
- Suppression des lignes vides inutiles
- Clarification des commentaires
- Amélioration de la lisibilité du code

## Installation et exécution

### Prérequis
```bash
pip install PyQt5
```

### Exécution avec Python
```bash
# Depuis le répertoire du projet
python Agenda_Demarage.py
# ou
python Ajout_Bureau.py
```

### Exécution avec VS Code
1. Ouvrir le dossier dans VS Code
2. Installer l'extension Python de Microsoft
3. Sélectionner l'interpréteur Python
4. Appuyer sur `F5` ou utiliser le bouton "Run"

### Exécution avec Visual Studio 2022+
1. Installer la charge de travail "Python development"
2. Ouvrir le dossier : File → Open → Folder
3. Clic droit sur `Agenda_Demarage.py` → Set as Startup Item
4. Appuyer sur `F5` ou Debug → Start Debugging

## Structure des fichiers

- `Agenda_Demarage.py` : Programme principal (affichage des événements)
- `Agenda_Demarage_Front.py` : Interface UI générée (ne pas modifier)
- `Ajout_Bureau.py` : Formulaire d'ajout d'événements
- `Ajout_Bureau_Front.py` : Interface UI générée (ne pas modifier)
- `Agenda_Terminator_JSON.json` : Base de données des événements
- `Agenda.png` : Icône de l'application

## Fichier JSON

Format du fichier `Agenda_Terminator_JSON.json` :
```json
[
    {
        "Jours": "25",
        "mois": "12",
        "annee": "2025",
        "Texte": "Noël"
    },
    {
        "Jours": "01",
        "mois": "01",
        "annee": "Repeat",
        "Texte": "Jour de l'an (répété chaque année)"
    }
]
```

## Dépannage

### Erreur : "FileNotFoundError: Agenda_Terminator_JSON.json"
→ Assurez-vous que le fichier JSON existe dans le même dossier que les scripts

### Erreur : "No module named 'PyQt5'"
→ Installez PyQt5 : `pip install PyQt5`

### Les accents ne s'affichent pas correctement
→ Les fichiers utilisent maintenant l'encodage UTF-8, ce problème devrait être résolu

### L'icône Agenda.png ne s'affiche pas
→ Placez le fichier Agenda.png dans le même répertoire que les scripts
