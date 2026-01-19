# -*- coding: utf-8 -*-
import sys
import os
import json
from datetime import datetime

from PyQt5.QtWidgets import (QMainWindow, QApplication, QDialog,
                              QTableWidget, QTableWidgetItem, QGraphicsDropShadowEffect, QLabel)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QRect, QSize

from Agenda_Demarage_Front import Ui_MainWindow



if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)



#MAIN_Windows#############################################################################################################################################    
class Agenda_Demarage(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Agenda_Demarage, self).__init__()
        self.setupUi(self)


        #Mainwindow: Titre - Icon:
        self.setWindowTitle('Agenda')
        # Chemin du répertoire courant pour les ressources
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(self.script_dir)
        icon_path = os.path.join(parent_dir, 'Agenda.png')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.Folder = "Agenda_Event"
        self.path_local_appdata = os.getenv('LOCALAPPDATA')


        ######################################################################################################
        #Activer avant COMPACTER
        #self.current_path = os.path.join(self.path_local_appdata,self.Folder) #= LOCALAPPDATA

        #DESACTIVER avant COMPACTER
        self.current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print("Current path: ",self.current_path)
        ######################################################################################################


        self.Recherche_JsonFile()
        self.Comparateur_de_Dates()        


    def Recherche_JsonFile(self):
        print("Recherche_JsonFile ok")

        
        #Extraction JSON:
        self.PATH_Event = os.path.join(self.current_path, 'Agenda_Terminator_JSON.json')
        try:
            with open(self.PATH_Event, encoding='utf-8') as json_data:
                self.json_data_2 = json.load(json_data)
            print("self.json_data_2: ",self.json_data_2)
        except FileNotFoundError:
            print(f"Erreur: Fichier {self.PATH_Event} non trouvé")
            self.json_data_2 = []
        
        self.Suppression_old_Datas()    



    def Suppression_old_Datas(self):
        print("\nSuppression_old_Datas ok")    

        # Supprime toutes les Datas des années précédantes:
        self.Current_year = datetime.today().strftime("%Y")
        self.json_data = [i for i in self.json_data_2 if not (i['annee'] < self.Current_year) or not (i['annee'] != 'Repeat')]    #or not (i['annee'] != 'Repeat')

        # Compare le nombre de dico dans les deux listes:
        LenList_2 = len(self.json_data_2)
        LenList = len(self.json_data)

        # Si différance est plus grand que 0: il y a eu une suppression:
        self.CompareLenList = int(LenList_2) - int(LenList)
        print("self.CompareLenList: ",self.CompareLenList)
           
        # Donc il faut sauver la nouvelle List dans le json_file:
        if self.CompareLenList != 0:
            #Sauvegarde json file
            self.PATH_Event = os.path.join(self.current_path, 'Agenda_Terminator_JSON.json')
            with open(self.PATH_Event, "w", encoding='utf-8') as file:
                json.dump(self.json_data, file, indent=4, sort_keys=False, ensure_ascii=False)        


    def Comparateur_de_Dates(self):
        print("\nComparateur_de_Dates ok")


        # Date to Day: (year - month - day)
        self.Current_year = datetime.today().strftime("%Y")
        self.Current_month = datetime.today().strftime("%m")
        self.Current_day = datetime.today().strftime("%d")

        
        self.List = []
        for i in self.json_data_2:
            self.counter = 0
            

            for k,v in i.items():
                
                if k == 'Jours':
                    if  v == str(self.Current_day):
                        #print("k: ",k,"/v: ",v)
                        self.counter = self.counter + 1

                if k == 'mois':
                    if  v == str(self.Current_month):
                        self.counter = self.counter + 1
                
                if k == 'annee':
                    if  str(v) == str(self.Current_year) or v == str("Repeat"):                        
                        ##print("k: ",k,"/v: ",v)
                        self.counter = self.counter + 1

                #print("Résultat Counter: ",self.counter)
                if self.counter == 3 and k == 'Texte':
                    self.List.append(v)

                if self.counter == 3 :    
                    self.show()


        self.Incorporation_dynamique()






    def Incorporation_dynamique(self):
        print("Incorporation_dynamique ok")


        self.len_List = len(self.List)
        self.Counter = 1 
 
        # Suppression items (CheckBox, Label_espace, PushButton, label):
        CountLabel = (self.gridLayout.count()-1)/1
       
        if self.len_List != 0:            
            for x in range(0,int(CountLabel)):
                self.label_2.deleteLater()

        for x in self.List:           
            for i in range(0, self.len_List):            
                # 1.) Creation items (CheckBox, Label_espace, PushButton, label):            
                self.label_2 = QLabel()  

                # 2.) Size:
                self.label_2.setMinimumSize(QSize(100, 10))         # Largeur/hauteur
                self.label_2.setMaximumSize(QSize(800, 70))         # Largeur/hauteur

            # 4.) Mise en Forme  (voir CSS Style):
            # label: = QtWidgets.QLabel()
            self.label_2.setStyleSheet("background-color: rgb(0, 0, 0);\
                                      color: rgb(0, 255, 127);\
                                      font: 14pt \"Arial\";\
                                      font-weight:bold;\
                                      font-style: italic;\
                                      border-style: outset;\
                                      border-width: 3px;\
                                      border-radius: 10px;\
                                      border-color: rgb(255, 255, 255);")          # Mise en Forme Label       

            # 3.) Annotation:
            self.label_2.setText(str(x))

            # 5.) Incorporation dans Grid (self.counter = no row,  O,1,2,3,4 = no colonne):
            self.gridLayout.addWidget(self.label_2, self.Counter, 0)
 
            self.Counter = self.Counter + 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    recherche = Agenda_Demarage()  
    #recherche.show()
    sys.exit(app.exec_())
