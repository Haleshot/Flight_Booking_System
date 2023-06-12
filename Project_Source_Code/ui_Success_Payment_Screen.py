# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Success_Payment_Screen.ui'
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
        self.label = QLabel(bgWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 160, 211, 231))
        self.label.setPixmap(QPixmap(u"Icons/payment-success.png"))
        self.label_2 = QLabel(bgWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 90, 251, 61))
        self.label_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.Quit_Button = QPushButton(bgWidget)
        self.Quit_Button.setObjectName(u"Quit_Button")
        self.Quit_Button.setGeometry(QRect(460, 639, 281, 51))
        self.Quit_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.label_3 = QLabel(bgWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 500, 581, 51))
        self.label_3.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.Yes_Button = QPushButton(bgWidget)
        self.Yes_Button.setObjectName(u"Yes_Button")
        self.Yes_Button.setGeometry(QRect(460, 560, 281, 51))
        self.Yes_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"")

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("bgWidget", u"Payment Successful!", None))
        self.Quit_Button.setText(QCoreApplication.translate("bgWidget", u"Quit", None))
        self.label_3.setText(QCoreApplication.translate("bgWidget", u"Do you want to cancel/refund to Payment ?", None))
        self.Yes_Button.setText(QCoreApplication.translate("bgWidget", u"Yes", None))
    # retranslateUi

