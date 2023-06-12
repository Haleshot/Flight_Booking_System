# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_UI.ui'
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
        Dialog.resize(1201, 844)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 1201, 801))
        self.bgwidget.setStyleSheet(u"background-color: white;")
        self.HeaderLabel = QLabel(self.bgwidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(505, 100, 211, 111))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 48pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Login_Sign_Up_Label = QLabel(self.bgwidget)
        self.Login_Sign_Up_Label.setObjectName(u"Login_Sign_Up_Label")
        self.Login_Sign_Up_Label.setGeometry(QRect(470, 210, 291, 61))
        self.Login_Sign_Up_Label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.Login_Sign_Up_Label.setAlignment(Qt.AlignCenter)
        self.login = QPushButton(self.bgwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(510, 630, 241, 71))
        self.login.setStyleSheet(u"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.EmailField = QLineEdit(self.bgwidget)
        self.EmailField.setObjectName(u"EmailField")
        self.EmailField.setGeometry(QRect(450, 400, 381, 61))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.EmailField.setFont(font)
        self.EmailField.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.PasswordField = QLineEdit(self.bgwidget)
        self.PasswordField.setObjectName(u"PasswordField")
        self.PasswordField.setGeometry(QRect(450, 510, 381, 61))
        self.PasswordField.setFont(font)
        self.PasswordField.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.PasswordField.setEchoMode(QLineEdit.Password)
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 370, 151, 21))
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_2 = QLabel(self.bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 480, 151, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Error_Popup_Message = QLabel(self.bgwidget)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(310, 590, 651, 31))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)
        self.Asterisk_1 = QLabel(self.bgwidget)
        self.Asterisk_1.setObjectName(u"Asterisk_1")
        self.Asterisk_1.setGeometry(QRect(600, 370, 21, 16))
        self.Asterisk_1.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Asterisk_2 = QLabel(self.bgwidget)
        self.Asterisk_2.setObjectName(u"Asterisk_2")
        self.Asterisk_2.setGeometry(QRect(525, 480, 21, 16))
        self.Asterisk_2.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.Login_Sign_Up_Label.setText(QCoreApplication.translate("Dialog", u"Sign in to your existing account", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Username/Email ID", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.Error_Popup_Message.setText("")
        self.Asterisk_1.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.Asterisk_2.setText(QCoreApplication.translate("Dialog", u"*", None))
    # retranslateUi

