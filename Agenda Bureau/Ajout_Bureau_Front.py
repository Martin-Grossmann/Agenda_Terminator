# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ajout_Bureau.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(670, 258)
        self.comboBox_jour = QtWidgets.QComboBox(Dialog)
        self.comboBox_jour.setGeometry(QtCore.QRect(53, 68, 161, 22))
        self.comboBox_jour.setObjectName("comboBox_jour")
        self.comboBox_mois = QtWidgets.QComboBox(Dialog)
        self.comboBox_mois.setGeometry(QtCore.QRect(257, 68, 161, 22))
        self.comboBox_mois.setObjectName("comboBox_mois")
        self.comboBox_annee = QtWidgets.QComboBox(Dialog)
        self.comboBox_annee.setGeometry(QtCore.QRect(458, 67, 161, 22))
        self.comboBox_annee.setObjectName("comboBox_annee")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 160, 571, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 210, 221, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 34, 37, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(324, 36, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(517, 33, 55, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 130, 46, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Ajouter Event"))
        self.label.setText(_translate("Dialog", "Jour"))
        self.label_2.setText(_translate("Dialog", "Mois"))
        self.label_3.setText(_translate("Dialog", "Année"))
        self.label_4.setText(_translate("Dialog", "Texte"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

