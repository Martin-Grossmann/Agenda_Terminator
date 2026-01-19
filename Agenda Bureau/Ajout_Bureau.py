# -*- coding: utf-8 -*-
import sys
import os
import json
from datetime import datetime

from PyQt5.QtWidgets import (QMainWindow, QApplication, QDialog, QMessageBox,
                              QTableWidget, QTableWidgetItem, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QRect, QSize

from Ajout_Bureau_Front import Ui_Dialog



if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)



#MAIN_Windows#############################################################################################################################################    
class Agenda_Bureau(QMainWindow, Ui_Dialog):

    def __init__(self, parent=None):
        super(Agenda_Bureau, self).__init__()
        self.setupUi(self)



        # Mainwindow: Titre - Icon:
        self.setWindowTitle('Agenda')
        
        # Déterminer le répertoire de base selon le mode d'exécution
        if getattr(sys, 'frozen', False):
            # Mode compilé (PyInstaller)
            base_dir = sys._MEIPASS
            print(f"Mode compilé - Base directory: {base_dir}")
        else:
            # Mode Python direct
            script_dir = os.path.dirname(os.path.abspath(__file__))
            base_dir = os.path.dirname(script_dir)
            print(f"Mode Python - Base directory: {base_dir}")
        
        # Chercher l'icône dans plusieurs emplacements possibles
        icon_candidates = [
            os.path.join(base_dir, 'Agenda.ico'),      # Dans le répertoire de base
            os.path.join(base_dir, 'Agenda.png'),      # PNG dans le répertoire de base
            os.path.join(base_dir, 'Compilation', 'Annexes', 'Agenda.ico'),  # Dans Compilation/Annexes
        ]
        
        icon_path = None
        for path in icon_candidates:
            if os.path.exists(path):
                icon_path = path
                break
        
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))
            print(f"✓ Icône chargée : {icon_path}")
        else:
            print(f"⚠ Icône non trouvée dans : {icon_candidates}")

        

        self.Folder = "Agenda_Event"
        self.path_local_appdata = os.getenv('LOCALAPPDATA')


        ######################################################################################################
        #Activer avant COMPACTER
        self.current_path = os.path.join(self.path_local_appdata,self.Folder) #= LOCALAPPDATA\Quant

        #DESACTIVER avant COMPACTER
        #self.current_path = os.path.dirname(self.script_dir)
        print("Current path: ",self.current_path)
        ######################################################################################################



        self.pushButton.clicked.connect(self.New) 

        # Populer combobox:
        self.List_Jours = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        self.List_Mois = ['01','02','03','04','05','06','07','08','09','10','11','12']
        self.List_Annee = ['Repeat','2026','2027','2028','2029','2030','2031','2032',]

        self.comboBox_jour.addItems(self.List_Jours)
        self.comboBox_mois.addItems(self.List_Mois)
        self.comboBox_annee.addItems(self.List_Annee)
        self.textEdit.setText(str(""))



    def New(self):
        print('New ok')

        # Datas séléctionnés:
        self.Jour = str(self.comboBox_jour.currentText())
        self.Mois = str(self.comboBox_mois.currentText())
        self.Annee = str(self.comboBox_annee.currentText())
        self.Texte = self.textEdit.toPlainText()

        self.New_Dico = {'Jours':self.Jour,'mois':self.Mois,'annee':self.Annee,'Texte':self.Texte}
        print("New_Dico: ",self.New_Dico)


        #Extraction JSON:         
        self.PATH_Event = os.path.join(self.current_path, 'Agenda_Terminator_JSON.json')
        try:
            with open(self.PATH_Event, encoding='utf-8') as json_file:
                self.List_data = json.load(json_file)
        except FileNotFoundError:
            print(f"Erreur: Fichier {self.PATH_Event} non trouvé")
            return False

        # Ajout nouveau Dico dans List existante (Extraction JSON):
        dictionary_copy = self.New_Dico.copy()
        self.List_data.append(dictionary_copy)
            

        #Sauvegarde json file
        self.PATH_Event = os.path.join(self.current_path, 'Agenda_Terminator_JSON.json')
        with open(self.PATH_Event, "w", encoding='utf-8') as file:
            json.dump(self.List_data, file, indent=4, sort_keys=False, ensure_ascii=False)


        reply = QMessageBox.question(None, "Agenda/Terminator",                                                          
            "Mise à jour saisie",
            QMessageBox.Ok) 
        return False


    
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    recherche = Agenda_Bureau()  
    recherche.show()
    sys.exit(app.exec_())
