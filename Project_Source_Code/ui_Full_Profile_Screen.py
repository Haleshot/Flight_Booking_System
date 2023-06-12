# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Full_Profile_Screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_bgwidget(object):
    def setupUi(self, bgwidget):
        if not bgwidget.objectName():
            bgwidget.setObjectName(u"bgwidget")
        bgwidget.resize(1201, 801)
        self.Sign_Up = QPushButton(bgwidget)
        self.Sign_Up.setObjectName(u"Sign_Up")
        self.Sign_Up.setGeometry(QRect(490, 710, 241, 71))
        self.Sign_Up.setStyleSheet(u"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.label_5 = QLabel(bgwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 160, 121, 21))
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Customer_Country = QLineEdit(bgwidget)
        self.Customer_Country.setObjectName(u"Customer_Country")
        self.Customer_Country.setGeometry(QRect(30, 400, 381, 61))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_Country.setFont(font)
        self.Customer_Country.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.label_10 = QLabel(bgwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(760, 370, 101, 21))
        self.label_10.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Customer_Pincode = QLineEdit(bgwidget)
        self.Customer_Pincode.setObjectName(u"Customer_Pincode")
        self.Customer_Pincode.setGeometry(QRect(760, 190, 381, 61))
        self.Customer_Pincode.setFont(font)
        self.Customer_Pincode.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Asterisk_10 = QLabel(bgwidget)
        self.Asterisk_10.setObjectName(u"Asterisk_10")
        self.Asterisk_10.setGeometry(QRect(860, 370, 21, 16))
        self.Asterisk_10.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Customer_State = QLineEdit(bgwidget)
        self.Customer_State.setObjectName(u"Customer_State")
        self.Customer_State.setGeometry(QRect(30, 290, 381, 61))
        self.Customer_State.setFont(font)
        self.Customer_State.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.label_8 = QLabel(bgwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(760, 160, 61, 21))
        self.label_8.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Customer_DOB = QDateEdit(bgwidget)
        self.Customer_DOB.setObjectName(u"Customer_DOB")
        self.Customer_DOB.setGeometry(QRect(760, 400, 381, 61))
        self.Customer_DOB.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Customer_DOB.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.HeaderLabel = QLabel(bgwidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(350, 20, 491, 61))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Customer_Name = QLineEdit(bgwidget)
        self.Customer_Name.setObjectName(u"Customer_Name")
        self.Customer_Name.setGeometry(QRect(30, 190, 381, 61))
        self.Customer_Name.setFont(font)
        self.Customer_Name.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Asterisk_9 = QLabel(bgwidget)
        self.Asterisk_9.setObjectName(u"Asterisk_9")
        self.Asterisk_9.setGeometry(QRect(810, 270, 16, 16))
        self.Asterisk_9.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_9 = QLabel(bgwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(760, 270, 51, 21))
        self.label_9.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Customer_Gender = QComboBox(bgwidget)
        self.Customer_Gender.addItem("")
        self.Customer_Gender.addItem("")
        self.Customer_Gender.addItem("")
        self.Customer_Gender.addItem("")
        self.Customer_Gender.addItem("")
        self.Customer_Gender.addItem("")
        self.Customer_Gender.setObjectName(u"Customer_Gender")
        self.Customer_Gender.setGeometry(QRect(760, 300, 381, 61))
        self.Customer_Gender.setAutoFillBackground(False)
        self.Customer_Gender.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Asterisk_8 = QLabel(bgwidget)
        self.Asterisk_8.setObjectName(u"Asterisk_8")
        self.Asterisk_8.setGeometry(QRect(820, 160, 21, 16))
        self.Asterisk_8.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Asterisk_5 = QLabel(bgwidget)
        self.Asterisk_5.setObjectName(u"Asterisk_5")
        self.Asterisk_5.setGeometry(QRect(150, 160, 21, 16))
        self.Asterisk_5.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Asterisk_11 = QLabel(bgwidget)
        self.Asterisk_11.setObjectName(u"Asterisk_11")
        self.Asterisk_11.setGeometry(QRect(90, 370, 21, 16))
        self.Asterisk_11.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_11 = QLabel(bgwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 260, 41, 21))
        self.label_11.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_12 = QLabel(bgwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 370, 61, 21))
        self.label_12.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Asterisk_12 = QLabel(bgwidget)
        self.Asterisk_12.setObjectName(u"Asterisk_12")
        self.Asterisk_12.setGeometry(QRect(70, 260, 21, 16))
        self.Asterisk_12.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Error_Popup_Message = QLabel(bgwidget)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(420, 610, 371, 31))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(bgwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(410, 490, 111, 21))
        self.label_13.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Asterisk_13 = QLabel(bgwidget)
        self.Asterisk_13.setObjectName(u"Asterisk_13")
        self.Asterisk_13.setGeometry(QRect(520, 490, 21, 16))
        self.Asterisk_13.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Customer_Phone_Number = QLineEdit(bgwidget)
        self.Customer_Phone_Number.setObjectName(u"Customer_Phone_Number")
        self.Customer_Phone_Number.setGeometry(QRect(410, 520, 381, 61))
        self.Customer_Phone_Number.setFont(font)
        self.Customer_Phone_Number.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")

        self.retranslateUi(bgwidget)

        QMetaObject.connectSlotsByName(bgwidget)
    # setupUi

    def retranslateUi(self, bgwidget):
        bgwidget.setWindowTitle(QCoreApplication.translate("bgwidget", u"Dialog", None))
        self.Sign_Up.setText(QCoreApplication.translate("bgwidget", u"Sign up", None))
        self.label_5.setText(QCoreApplication.translate("bgwidget", u"Customer Name", None))
        self.Customer_Country.setPlaceholderText(QCoreApplication.translate("bgwidget", u"Enter your Country...", None))
        self.label_10.setText(QCoreApplication.translate("bgwidget", u"Date Of Birth", None))
        self.Customer_Pincode.setPlaceholderText(QCoreApplication.translate("bgwidget", u"Enter your Pincode...", None))
        self.Asterisk_10.setText(QCoreApplication.translate("bgwidget", u"*", None))
        self.Customer_State.setPlaceholderText(QCoreApplication.translate("bgwidget", u"Enter your State...", None))
        self.label_8.setText(QCoreApplication.translate("bgwidget", u"Pincode", None))
        self.HeaderLabel.setText(QCoreApplication.translate("bgwidget", u"Profile Details", None))
        self.Customer_Name.setPlaceholderText(QCoreApplication.translate("bgwidget", u"Enter your Customer Name...", None))
        self.Asterisk_9.setText(QCoreApplication.translate("bgwidget", u"*", None))
        self.label_9.setText(QCoreApplication.translate("bgwidget", u"Gender", None))
        self.Customer_Gender.setItemText(0, QCoreApplication.translate("bgwidget", u"Male", None))
        self.Customer_Gender.setItemText(1, QCoreApplication.translate("bgwidget", u"Female", None))
        self.Customer_Gender.setItemText(2, QCoreApplication.translate("bgwidget", u"Transgender", None))
        self.Customer_Gender.setItemText(3, QCoreApplication.translate("bgwidget", u"Non Binary", None))
        self.Customer_Gender.setItemText(4, QCoreApplication.translate("bgwidget", u"Intersex", None))
        self.Customer_Gender.setItemText(5, QCoreApplication.translate("bgwidget", u"I prefer not to say", None))

        self.Customer_Gender.setPlaceholderText(QCoreApplication.translate("bgwidget", u"Enter your Gender...", None))
        self.Asterisk_8.setText(QCoreApplication.translate("bgwidget", u"*", None))
        self.Asterisk_5.setText(QCoreApplication.translate("bgwidget", u"*", None))
        self.Asterisk_11.setText(QCoreApplication.translate("bgwidget", u"*", None))
        self.label_11.setText(QCoreApplication.translate("bgwidget", u"State", None))
        self.label_12.setText(QCoreApplication.translate("bgwidget", u"Country", None))
        self.Asterisk_12.setText(QCoreApplication.translate("bgwidget", u"*", None))
        self.Error_Popup_Message.setText("")
        self.label_13.setText(QCoreApplication.translate("bgwidget", u"Phone Number", None))
        self.Asterisk_13.setText(QCoreApplication.translate("bgwidget", u"*", None))
        self.Customer_Phone_Number.setPlaceholderText(QCoreApplication.translate("bgwidget", u"Enter your Phone Number...", None))
    # retranslateUi

