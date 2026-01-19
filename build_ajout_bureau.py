# -*- coding: utf-8 -*-
"""
Script de compilation PyInstaller simplifié pour Ajout_Bureau
"""

import os
import shutil
import subprocess
import sys

# Chemins
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AJOUT_BUREAU = os.path.join(SCRIPT_DIR, "Agenda Bureau", "Ajout_Bureau.py")
ICON_PATH = os.path.join(SCRIPT_DIR, "Agenda Bureau", "Compilation", "Annexes", "Agenda.ico")
DESKTOP = os.path.expanduser("~\\Desktop")
OUTPUT_DIR = os.path.join(DESKTOP, "Ajout_Bureau_build")  # Sortie sur le Desktop

print("=" * 80)
print("COMPILATION AJOUT_BUREAU")
print("=" * 80)

# 🗑️ NETTOYER LES DOSSIERS DE BUILD AVANT COMPILATION
print("\n🗑️  Nettoyage des anciens fichiers...")
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    print(f"✓ Dossier supprimé : {OUTPUT_DIR}")

# Vérifier les fichiers
if not os.path.exists(AJOUT_BUREAU):
    print(f"❌ Erreur : {AJOUT_BUREAU} non trouvé")
    sys.exit(1)

if not os.path.exists(ICON_PATH):
    print(f"❌ Erreur : {ICON_PATH} non trouvé")
    sys.exit(1)

print(f"✓ Script : {AJOUT_BUREAU}")
print(f"✓ Icône : {ICON_PATH}")

# Commande PyInstaller - VERSION SIMPLE SANS --add-data
cmd = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--windowed",
    f"--icon={ICON_PATH}",
    f"--distpath={OUTPUT_DIR}",
    f"--workpath={os.path.join(SCRIPT_DIR, 'build')}",
    f"--specpath={SCRIPT_DIR}",
    "--name=Ajout_Bureau",
    "--noupx",  # Désactiver UPX qui peut causer des problèmes
    AJOUT_BUREAU
]

print("\n" + "=" * 80)
print("Lancement de la compilation...")
print("=" * 80 + "\n")

result = subprocess.run(cmd, cwd=SCRIPT_DIR)

if result.returncode == 0:
    print("\n" + "=" * 80)
    print("✅ COMPILATION RÉUSSIE !")
    print("=" * 80)
    
    exe_path = os.path.join(OUTPUT_DIR, "Ajout_Bureau.exe")
    if os.path.exists(exe_path):
        print(f"✓ EXE créé : {exe_path}")
        # Déplacer vers le Desktop directement
        desktop_dest = os.path.join(DESKTOP, "Ajout_Bureau.exe")
        try:
            if os.path.exists(desktop_dest):
                os.remove(desktop_dest)
            shutil.move(exe_path, desktop_dest)
            print(f"✓ EXE déplacé sur le Desktop")
            # Nettoyer le dossier temporaire
            shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
        except Exception as e:
            print(f"⚠ {e}")
    else:
        print("❌ L'EXE n'a pas été créé")
        sys.exit(1)
else:
    print("\n" + "=" * 80)
    print("❌ ERREUR DE COMPILATION")
    print("=" * 80)
    sys.exit(1)

print("\n✅ Terminé !")

