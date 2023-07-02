# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Indivo_Admin_Options.ui'
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
        self.HeaderLabel.setGeometry(QRect(196, 2, 821, 51))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 30pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Payments_Button = QPushButton(Dialog)
        self.Payments_Button.setObjectName(u"Payments_Button")
        self.Payments_Button.setGeometry(QRect(490, 300, 211, 91))
        self.Payments_Button.setStyleSheet(u"/*\n"
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
        self.Cancellations_Button = QPushButton(Dialog)
        self.Cancellations_Button.setObjectName(u"Cancellations_Button")
        self.Cancellations_Button.setGeometry(QRect(490, 420, 211, 91))
        self.Cancellations_Button.setStyleSheet(u"/*\n"
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
        self.Check_Flights_Button = QPushButton(Dialog)
        self.Check_Flights_Button.setObjectName(u"Check_Flights_Button")
        self.Check_Flights_Button.setGeometry(QRect(490, 180, 211, 91))
        self.Check_Flights_Button.setStyleSheet(u"/*\n"
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"Indivo ADMIN ", None))
        self.Payments_Button.setText(QCoreApplication.translate("Dialog", u"Payments", None))
        self.Cancellations_Button.setText(QCoreApplication.translate("Dialog", u"Cancellations", None))
        self.Check_Flights_Button.setText(QCoreApplication.translate("Dialog", u"Check Flights", None))
    # retranslateUi

