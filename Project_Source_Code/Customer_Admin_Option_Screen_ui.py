# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Customer_Admin_Option_Screen.ui'
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
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 1201, 801))
        self.bgwidget.setStyleSheet(u"")
        self.Header_Title = QLabel(self.bgwidget)
        self.Header_Title.setObjectName(u"Header_Title")
        self.Header_Title.setGeometry(QRect(350, 80, 531, 91))
        self.Header_Title.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";")
        self.Login_Sign_Up_Label = QLabel(self.bgwidget)
        self.Login_Sign_Up_Label.setObjectName(u"Login_Sign_Up_Label")
        self.Login_Sign_Up_Label.setGeometry(QRect(520, 160, 191, 61))
        self.Login_Sign_Up_Label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.Customer = QPushButton(self.bgwidget)
        self.Customer.setObjectName(u"Customer")
        self.Customer.setGeometry(QRect(490, 570, 241, 71))
        self.Customer.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"	\n"
"	background-color: rgb(85, 255, 127);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.Admin = QPushButton(self.bgwidget)
        self.Admin.setObjectName(u"Admin")
        self.Admin.setGeometry(QRect(490, 675, 241, 71))
        self.Admin.setStyleSheet(u"/*\n"
"border: 12px  solid rgb(170, 255, 127);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"*/\n"
"\n"
"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"	\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.Flight_Gif_Label = QLabel(self.bgwidget)
        self.Flight_Gif_Label.setObjectName(u"Flight_Gif_Label")
        self.Flight_Gif_Label.setGeometry(QRect(90, 260, 1051, 261))
        self.Flight_Gif_Label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Header_Title.setText(QCoreApplication.translate("Dialog", u"Flight Booking Management System", None))
        self.Login_Sign_Up_Label.setText(QCoreApplication.translate("Dialog", u"Login/Sign Up Page", None))
#if QT_CONFIG(whatsthis)
        self.Customer.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Customer.setText(QCoreApplication.translate("Dialog", u"Customer", None))
        self.Admin.setText(QCoreApplication.translate("Dialog", u"Admin", None))
        self.Flight_Gif_Label.setText("")
    # retranslateUi

