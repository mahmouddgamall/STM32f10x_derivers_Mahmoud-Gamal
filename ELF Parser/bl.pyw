# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bl_Design.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys,re
import os.path
from pathlib import Path
import time
import os

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(638, 415)
        self.PinSelect_comboBox = QComboBox(Form)
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.addItem(str())
        self.PinSelect_comboBox.setObjectName(u"PinSelect_comboBox")
        self.PinSelect_comboBox.setGeometry(QRect(70, 30, 111, 31))
        self.SelectButton = QPushButton(Form)
        self.SelectButton.setObjectName(u"SelectButton")
        self.SelectButton.setGeometry(QRect(440, 30, 112, 34))
        font = QFont()
        font.setBold(True)
        font.setWeight(75);
        self.SelectButton.setFont(font)
        self.pathLbl = QLabel(Form)
        self.pathLbl.setObjectName(u"pathLbl")
        self.pathLbl.setGeometry(QRect(20, 140, 131, 21))
        self.pathLb2 = QLabel(Form)
        self.pathLb2.setObjectName(u"pathLb2")
        self.pathLb2.setGeometry(QRect(250, 270, 200, 21))
        
        self.CreateButton = QPushButton(Form)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setGeometry(QRect(220, 310, 181, 41))
        self.CreateButton.setFont(font)
        self.CreateButton.setStyleSheet(u"color: rgb(35, 35, 35);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pathTxt = QLineEdit(Form)
        self.pathTxt.setObjectName(u"pathTxt")
        self.pathTxt.setGeometry(QRect(70, 190, 481, 41))
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(170, 100, 281, 23))
        self.progressBar.setValue(0)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
        self.CreateButton.clicked.connect(self.FlashNewAppFunction)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PinSelect_comboBox.setItemText(0, QCoreApplication.translate("Form", u"COM1", None))
        self.PinSelect_comboBox.setItemText(1, QCoreApplication.translate("Form", u"COM2", None))
        self.PinSelect_comboBox.setItemText(2, QCoreApplication.translate("Form", u"COM3", None))
        self.PinSelect_comboBox.setItemText(3, QCoreApplication.translate("Form", u"COM4", None))
        self.PinSelect_comboBox.setItemText(4, QCoreApplication.translate("Form", u"COM5", None))
        self.PinSelect_comboBox.setItemText(5, QCoreApplication.translate("Form", u"COM6", None))
        self.PinSelect_comboBox.setItemText(6, QCoreApplication.translate("Form", u"COM7", None))
        self.PinSelect_comboBox.setItemText(7, QCoreApplication.translate("Form", u"COM8", None))
        self.PinSelect_comboBox.setItemText(8, QCoreApplication.translate("Form", u"COM9", None))
        self.PinSelect_comboBox.setItemText(9, QCoreApplication.translate("Form", u"COM10", None))
        self.PinSelect_comboBox.setItemText(10, QCoreApplication.translate("Form", u"COM12", None))
        self.PinSelect_comboBox.setItemText(11, QCoreApplication.translate("Form", u"COM13", None))
        self.PinSelect_comboBox.setItemText(12, QCoreApplication.translate("Form", u"COM14", None))

        self.SelectButton.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pathLbl.setText(QCoreApplication.translate("Form", u"Input File Path", None))
        self.pathLb2.setText(QCoreApplication.translate("Form", u" ", None))
        self.CreateButton.setText(QCoreApplication.translate("Form", u"Flash New Aplication", None))
    # retranslateUi
    def FlashNewAppFunction(self):
       count=0
       print(self.PinSelect_comboBox.currentText())
       if self.pathTxt.text() == '':
           print("Plz enter the file Path")
       else:
           print(self.pathTxt.text())
           #call C appication
           self.progressBar.setValue(20)
           os.system("ELF.exe "+self.pathTxt.text()+" "+self.PinSelect_comboBox.currentText())
           self.progressBar.setValue(100)
           f = open("gui.txt", "r")
           #print(f.readline())
           self.pathLb2.setText(QCoreApplication.translate("Form", f.readline(), None))

app =QApplication(sys.argv)
Widget=QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())

