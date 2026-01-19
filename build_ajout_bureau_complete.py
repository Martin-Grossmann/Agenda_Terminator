# -*- coding: utf-8 -*-
"""
Script de compilation PyInstaller pour créer l'EXE Ajout_Bureau
avec Setup Inno Setup qui préserve les fichiers JSON existants
"""

import os
import shutil
import subprocess
import sys

# Chemins
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENDA_BUREAU = os.path.join(SCRIPT_DIR, "Agenda Bureau", "Ajout_Bureau.py")
ICON_PATH = os.path.join(SCRIPT_DIR, "Agenda Bureau", "Compilation", "Annexes", "Agenda.ico")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "dist")
DESKTOP = os.path.expanduser("~\\Desktop")

print("=" * 80)
print("COMPILATION AJOUT_BUREAU AVEC PYINSTALLER")
print("=" * 80)

# Vérifier que les fichiers existent
if not os.path.exists(AGENDA_BUREAU):
    print(f"❌ Erreur : {AGENDA_BUREAU} non trouvé")
    sys.exit(1)

if not os.path.exists(ICON_PATH):
    print(f"❌ Erreur : {ICON_PATH} non trouvé")
    sys.exit(1)

print(f"✓ Script Python : {AGENDA_BUREAU}")
print(f"✓ Icône : {ICON_PATH}")
print(f"✓ Sortie : {OUTPUT_DIR}")

# Nettoyer les anciens builds
if os.path.exists(OUTPUT_DIR):
    print(f"\n🧹 Nettoyage du dossier {OUTPUT_DIR}...")
    shutil.rmtree(OUTPUT_DIR)

# Commande PyInstaller
cmd = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",                          # Crée un seul fichier .exe
    "--windowed",                         # Sans console
    f"--icon={ICON_PATH}",               # Icône
    f"--distpath={OUTPUT_DIR}",          # Dossier dist
    f"--workpath={os.path.join(SCRIPT_DIR, 'build')}",
    f"--specpath={SCRIPT_DIR}",
    "--name=Ajout_Bureau",               # Nom du .exe
    f"--add-data={os.path.join(SCRIPT_DIR, 'Agenda.png')};.",  # Inclure Agenda.png
    f"--add-data={os.path.join(SCRIPT_DIR, 'Agenda_Terminator_JSON.json')};.",  # Inclure JSON
    AGENDA_BUREAU
]

print("\n" + "=" * 80)
print("Lancement de la compilation PyInstaller...")
print("=" * 80)

result = subprocess.run(cmd, cwd=SCRIPT_DIR)

if result.returncode == 0:
    print("\n✅ Compilation terminée avec succès!")
    print(f"📦 Fichier EXE créé : {os.path.join(OUTPUT_DIR, 'Ajout_Bureau.exe')}")
else:
    print("\n❌ Erreur lors de la compilation")
    sys.exit(1)

print("\n" + "=" * 80)
print("Construction terminée!")
print("=" * 80)
