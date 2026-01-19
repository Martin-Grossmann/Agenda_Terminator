# -*- coding: utf-8 -*-
"""
Script de compilation PyInstaller pour créer l'EXE Agenda_Demarage
"""

import os
import shutil
import subprocess
import sys

# Chemins
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENDA_DEMARAGE = os.path.join(SCRIPT_DIR, "Agenda Demarrage", "Agenda_Demarage.py")
ICON_PATH = os.path.join(SCRIPT_DIR, "Agenda Bureau", "Compilation", "Annexes", "Agenda.ico")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "dist")
DESKTOP = os.path.expanduser("~\\Desktop")

print("=" * 80)
print("COMPILATION AGENDA_DEMARAGE AVEC PYINSTALLER")
print("=" * 80)

# Vérifier que les fichiers existent
if not os.path.exists(AGENDA_DEMARAGE):
    print(f"❌ Erreur : {AGENDA_DEMARAGE} non trouvé")
    sys.exit(1)

if not os.path.exists(ICON_PATH):
    print(f"❌ Erreur : {ICON_PATH} non trouvé")
    sys.exit(1)

print(f"✓ Script Python : {AGENDA_DEMARAGE}")
print(f"✓ Icône : {ICON_PATH}")
print(f"✓ Sortie : {OUTPUT_DIR}")

# Commande PyInstaller
cmd = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",                          # Crée un seul fichier .exe
    "--windowed",                         # Sans console
    f"--icon={ICON_PATH}",               # Icône
    f"--distpath={OUTPUT_DIR}",          # Dossier dist
    f"--workpath={os.path.join(SCRIPT_DIR, 'build')}",
    f"--specpath={SCRIPT_DIR}",
    "--name=Agenda_Demarage",            # Nom du .exe
    f"--add-data={os.path.join(SCRIPT_DIR, 'Agenda.png')};.",  # Inclure Agenda.png
    AGENDA_DEMARAGE
]

print("\n" + "=" * 80)
print("Lancement de la compilation...")
print("=" * 80)

result = subprocess.run(cmd, cwd=SCRIPT_DIR)

if result.returncode == 0:
    print("\n" + "=" * 80)
    print("✅ COMPILATION RÉUSSIE !")
    print("=" * 80)
    
    exe_path = os.path.join(OUTPUT_DIR, "Agenda_Demarage.exe")
    if os.path.exists(exe_path):
        print(f"✓ EXE créé : {exe_path}")
        
        # Copier vers le desktop
        desktop_dest = os.path.join(DESKTOP, "Agenda_Demarage.exe")
        try:
            shutil.copy(exe_path, desktop_dest)
            print(f"✓ EXE copié sur le Desktop : {desktop_dest}")
        except Exception as e:
            print(f"⚠ Impossible de copier sur le Desktop : {e}")
    else:
        print("❌ L'EXE n'a pas été créé")
        sys.exit(1)
else:
    print("\n" + "=" * 80)
    print("❌ ERREUR DE COMPILATION")
    print("=" * 80)
    sys.exit(1)

print("\n✅ Terminé ! Vous pouvez maintenant utiliser Agenda_Demarage.exe")
