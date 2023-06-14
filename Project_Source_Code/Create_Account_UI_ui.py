# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Create_Account_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_bgWidget(object):
    def setupUi(self, bgWidget):
        if not bgWidget.objectName():
            bgWidget.setObjectName(u"bgWidget")
        bgWidget.resize(1223, 897)
        self.HeaderLabel = QLabel(bgWidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(370, 60, 491, 61))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Next_Button = QPushButton(bgWidget)
        self.Next_Button.setObjectName(u"Next_Button")
        self.Next_Button.setGeometry(QRect(490, 680, 241, 71))
        self.Next_Button.setStyleSheet(u"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.PasswordField = QLineEdit(bgWidget)
        self.PasswordField.setObjectName(u"PasswordField")
        self.PasswordField.setGeometry(QRect(420, 370, 381, 61))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PasswordField.setFont(font)
        self.PasswordField.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.PasswordField.setEchoMode(QLineEdit.Password)
        self.Asterisk_2 = QLabel(bgWidget)
        self.Asterisk_2.setObjectName(u"Asterisk_2")
        self.Asterisk_2.setGeometry(QRect(495, 340, 21, 16))
        self.Asterisk_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label = QLabel(bgWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 220, 151, 21))
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.EmailField = QLineEdit(bgWidget)
        self.EmailField.setObjectName(u"EmailField")
        self.EmailField.setGeometry(QRect(420, 250, 381, 61))
        self.EmailField.setFont(font)
        self.EmailField.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.label_2 = QLabel(bgWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 340, 81, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Asterisk_1 = QLabel(bgWidget)
        self.Asterisk_1.setObjectName(u"Asterisk_1")
        self.Asterisk_1.setGeometry(QRect(570, 220, 21, 16))
        self.Asterisk_1.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Confirm_Your_Password_Field = QLineEdit(bgWidget)
        self.Confirm_Your_Password_Field.setObjectName(u"Confirm_Your_Password_Field")
        self.Confirm_Your_Password_Field.setGeometry(QRect(420, 490, 381, 61))
        self.Confirm_Your_Password_Field.setFont(font)
        self.Confirm_Your_Password_Field.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Confirm_Your_Password_Field.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(bgWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 460, 171, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Asterisk_3 = QLabel(bgWidget)
        self.Asterisk_3.setObjectName(u"Asterisk_3")
        self.Asterisk_3.setGeometry(QRect(590, 460, 21, 16))
        self.Asterisk_3.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Error_Popup_Message = QLabel(bgWidget)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(290, 570, 681, 31))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("bgWidget", u"Create an Account", None))
        self.Next_Button.setText(QCoreApplication.translate("bgWidget", u"Next", None))
        self.PasswordField.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter your Password...", None))
        self.Asterisk_2.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.label.setText(QCoreApplication.translate("bgWidget", u"Username/Email ID", None))
        self.EmailField.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter your Username...", None))
        self.label_2.setText(QCoreApplication.translate("bgWidget", u"Password", None))
        self.Asterisk_1.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.Confirm_Your_Password_Field.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Confirm Your Password...", None))
        self.label_3.setText(QCoreApplication.translate("bgWidget", u"Confirm your Password", None))
        self.Asterisk_3.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.Error_Popup_Message.setText("")
    # retranslateUi

