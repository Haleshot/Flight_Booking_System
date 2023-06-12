# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Welcome_UI_Screen.ui'
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
        Dialog.resize(1200, 862)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 1201, 801))
        self.bgwidget.setStyleSheet(u"background-color: white;")
        self.Header_Title = QLabel(self.bgwidget)
        self.Header_Title.setObjectName(u"Header_Title")
        self.Header_Title.setGeometry(QRect(350, 80, 621, 91))
        self.Header_Title.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";")
        self.Login_Sign_Up_Label = QLabel(self.bgwidget)
        self.Login_Sign_Up_Label.setObjectName(u"Login_Sign_Up_Label")
        self.Login_Sign_Up_Label.setGeometry(QRect(520, 160, 191, 61))
        self.Login_Sign_Up_Label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.Login = QPushButton(self.bgwidget)
        self.Login.setObjectName(u"Login")
        self.Login.setGeometry(QRect(490, 570, 241, 71))
        self.Login.setStyleSheet(u"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.Create_an_Account = QPushButton(self.bgwidget)
        self.Create_an_Account.setObjectName(u"Create_an_Account")
        self.Create_an_Account.setGeometry(QRect(490, 675, 241, 71))
        self.Create_an_Account.setStyleSheet(u"\n"
"border: 12px  solid rgb(170, 255, 127);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Header_Title.setText(QCoreApplication.translate("Dialog", u"Flight Booking Management System", None))
        self.Login_Sign_Up_Label.setText(QCoreApplication.translate("Dialog", u"Login/Sign Up Page", None))
        self.Login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.Create_an_Account.setText(QCoreApplication.translate("Dialog", u"Create an Account", None))
    # retranslateUi

