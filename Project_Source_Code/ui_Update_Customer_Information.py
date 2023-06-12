# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Update_Customer_Information.ui'
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
        self.HeaderLabel = QLabel(Dialog)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(200, 20, 821, 71))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 230, 181, 31))
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.Reenter_Button = QPushButton(Dialog)
        self.Reenter_Button.setObjectName(u"Reenter_Button")
        self.Reenter_Button.setGeometry(QRect(430, 270, 291, 81))
        self.Reenter_Button.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"Update Customer Information", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Update Information:", None))
        self.Reenter_Button.setText(QCoreApplication.translate("Dialog", u"Re-enter", None))
    # retranslateUi

