# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OTP_Screen.ui'
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
        bgWidget.resize(1201, 801)
        self.HeaderLabel = QLabel(bgWidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(360, 120, 491, 61))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Asterisk_14 = QLabel(bgWidget)
        self.Asterisk_14.setObjectName(u"Asterisk_14")
        self.Asterisk_14.setGeometry(QRect(520, 290, 16, 16))
        self.Asterisk_14.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Customer_Phone_Number = QLineEdit(bgWidget)
        self.Customer_Phone_Number.setObjectName(u"Customer_Phone_Number")
        self.Customer_Phone_Number.setGeometry(QRect(410, 320, 381, 61))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_Phone_Number.setFont(font)
        self.Customer_Phone_Number.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.label_14 = QLabel(bgWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(410, 290, 171, 21))
        self.label_14.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Send_OTP_Button = QPushButton(bgWidget)
        self.Send_OTP_Button.setObjectName(u"Send_OTP_Button")
        self.Send_OTP_Button.setGeometry(QRect(820, 320, 181, 61))
        self.Send_OTP_Button.setStyleSheet(u"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.Error_Popup_Message_1 = QLabel(bgWidget)
        self.Error_Popup_Message_1.setObjectName(u"Error_Popup_Message_1")
        self.Error_Popup_Message_1.setGeometry(QRect(410, 550, 401, 31))
        self.Error_Popup_Message_1.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message_1.setAlignment(Qt.AlignCenter)
        self.Error_Popup_Message_3 = QLabel(bgWidget)
        self.Error_Popup_Message_3.setObjectName(u"Error_Popup_Message_3")
        self.Error_Popup_Message_3.setGeometry(QRect(410, 400, 391, 21))
        self.Error_Popup_Message_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 255, 0);")
        self.Error_Popup_Message_3.setAlignment(Qt.AlignCenter)
        self.Check_OTP_Button = QPushButton(bgWidget)
        self.Check_OTP_Button.setObjectName(u"Check_OTP_Button")
        self.Check_OTP_Button.setGeometry(QRect(470, 600, 241, 71))
        self.Check_OTP_Button.setStyleSheet(u"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.label_13 = QLabel(bgWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(410, 450, 31, 21))
        self.label_13.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.OTP_Text_Box = QLineEdit(bgWidget)
        self.OTP_Text_Box.setObjectName(u"OTP_Text_Box")
        self.OTP_Text_Box.setGeometry(QRect(410, 480, 381, 61))
        self.OTP_Text_Box.setFont(font)
        self.OTP_Text_Box.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Asterisk_13 = QLabel(bgWidget)
        self.Asterisk_13.setObjectName(u"Asterisk_13")
        self.Asterisk_13.setGeometry(QRect(440, 450, 16, 16))
        self.Asterisk_13.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Next_Button_2 = QPushButton(bgWidget)
        self.Next_Button_2.setObjectName(u"Next_Button_2")
        self.Next_Button_2.setGeometry(QRect(470, 700, 241, 71))
        self.Next_Button_2.setStyleSheet(u"border-radius: 20px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 127);\n"
"")
        self.Error_Popup_Message_2 = QLabel(bgWidget)
        self.Error_Popup_Message_2.setObjectName(u"Error_Popup_Message_2")
        self.Error_Popup_Message_2.setGeometry(QRect(730, 620, 401, 31))
        self.Error_Popup_Message_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 255, 0);")
        self.Error_Popup_Message_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("bgWidget", u"OTP Confirmation", None))
        self.Asterisk_14.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.Customer_Phone_Number.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter your Phone No...", None))
        self.label_14.setText(QCoreApplication.translate("bgWidget", u"Phone Number", None))
        self.Send_OTP_Button.setText(QCoreApplication.translate("bgWidget", u"Send OTP", None))
        self.Error_Popup_Message_1.setText("")
        self.Error_Popup_Message_3.setText("")
        self.Check_OTP_Button.setText(QCoreApplication.translate("bgWidget", u"Check OTP", None))
        self.label_13.setText(QCoreApplication.translate("bgWidget", u"OTP", None))
        self.OTP_Text_Box.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter OTP send to your Phone No...", None))
        self.Asterisk_13.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.Next_Button_2.setText(QCoreApplication.translate("bgWidget", u"Next", None))
        self.Error_Popup_Message_2.setText("")
    # retranslateUi

