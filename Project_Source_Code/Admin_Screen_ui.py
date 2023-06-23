# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_Screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1201, 801)
        self.Nistara = QPushButton(Dialog)
        self.Nistara.setObjectName(u"Nistara")
        self.Nistara.setGeometry(QRect(510, 160, 211, 91))
        self.PiceJet = QPushButton(Dialog)
        self.PiceJet.setObjectName(u"PiceJet")
        self.PiceJet.setGeometry(QRect(510, 280, 211, 91))
        self.MetAirways = QPushButton(Dialog)
        self.MetAirways.setObjectName(u"MetAirways")
        self.MetAirways.setGeometry(QRect(510, 400, 211, 91))
        self.Indivo = QPushButton(Dialog)
        self.Indivo.setObjectName(u"Indivo")
        self.Indivo.setGeometry(QRect(510, 520, 211, 91))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Nistara.setText(QCoreApplication.translate("Dialog", u"Nistara", None))
        self.PiceJet.setText(QCoreApplication.translate("Dialog", u"PiceJet", None))
        self.MetAirways.setText(QCoreApplication.translate("Dialog", u"MetAirways", None))
        self.Indivo.setText(QCoreApplication.translate("Dialog", u"Indivo", None))
    # retranslateUi

