# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Payment_Info_Screen.ui'
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
        self.Asterisk_4 = QLabel(bgWidget)
        self.Asterisk_4.setObjectName(u"Asterisk_4")
        self.Asterisk_4.setGeometry(QRect(510, 300, 21, 16))
        self.Asterisk_4.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_9 = QLabel(bgWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 420, 81, 21))
        self.label_9.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(bgWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 540, 121, 21))
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Confirm_Payment = QPushButton(bgWidget)
        self.Confirm_Payment.setObjectName(u"Confirm_Payment")
        self.Confirm_Payment.setGeometry(QRect(470, 690, 241, 71))
        self.Confirm_Payment.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Asterisk_5 = QLabel(bgWidget)
        self.Asterisk_5.setObjectName(u"Asterisk_5")
        self.Asterisk_5.setGeometry(QRect(510, 540, 21, 16))
        self.Asterisk_5.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.Error_Popup_Message = QLabel(bgWidget)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(420, 660, 371, 31))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)
        self.Customer_Card_Type = QComboBox(bgWidget)
        self.Customer_Card_Type.addItem("")
        self.Customer_Card_Type.addItem("")
        self.Customer_Card_Type.addItem("")
        self.Customer_Card_Type.addItem("")
        self.Customer_Card_Type.addItem("")
        self.Customer_Card_Type.addItem("")
        self.Customer_Card_Type.setObjectName(u"Customer_Card_Type")
        self.Customer_Card_Type.setGeometry(QRect(410, 450, 381, 61))
        self.Customer_Card_Type.setAutoFillBackground(False)
        self.Customer_Card_Type.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.HeaderLabel = QLabel(bgWidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(350, 20, 491, 61))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Customer_Number = QLineEdit(bgWidget)
        self.Customer_Number.setObjectName(u"Customer_Number")
        self.Customer_Number.setGeometry(QRect(410, 570, 381, 61))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Customer_Number.setFont(font)
        self.Customer_Number.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Customer_ID = QLineEdit(bgWidget)
        self.Customer_ID.setObjectName(u"Customer_ID")
        self.Customer_ID.setGeometry(QRect(410, 330, 381, 61))
        self.Customer_ID.setFont(font)
        self.Customer_ID.setStyleSheet(u"border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.Asterisk_9 = QLabel(bgWidget)
        self.Asterisk_9.setObjectName(u"Asterisk_9")
        self.Asterisk_9.setGeometry(QRect(490, 420, 16, 16))
        self.Asterisk_9.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_4 = QLabel(bgWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 300, 101, 21))
        self.label_4.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Total_Cost_Info_TableWidget = QTableWidget(bgWidget)
        if (self.Total_Cost_Info_TableWidget.columnCount() < 3):
            self.Total_Cost_Info_TableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.Total_Cost_Info_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Total_Cost_Info_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Total_Cost_Info_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.Total_Cost_Info_TableWidget.setObjectName(u"Total_Cost_Info_TableWidget")
        self.Total_Cost_Info_TableWidget.setGeometry(QRect(20, 130, 1151, 111))

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"Dialog", None))
        self.Asterisk_4.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.label_9.setText(QCoreApplication.translate("bgWidget", u"Card Type", None))
        self.label_5.setText(QCoreApplication.translate("bgWidget", u"Card Number", None))
        self.Confirm_Payment.setText(QCoreApplication.translate("bgWidget", u"Confirm Payment", None))
        self.Asterisk_5.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.Error_Popup_Message.setText("")
        self.Customer_Card_Type.setItemText(0, QCoreApplication.translate("bgWidget", u"Debit Card", None))
        self.Customer_Card_Type.setItemText(1, QCoreApplication.translate("bgWidget", u"Credit Card", None))
        self.Customer_Card_Type.setItemText(2, QCoreApplication.translate("bgWidget", u"Rupay", None))
        self.Customer_Card_Type.setItemText(3, QCoreApplication.translate("bgWidget", u"Net Banking", None))
        self.Customer_Card_Type.setItemText(4, QCoreApplication.translate("bgWidget", u"UPI", None))
        self.Customer_Card_Type.setItemText(5, QCoreApplication.translate("bgWidget", u"Cash", None))

        self.Customer_Card_Type.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter your Gender...", None))
        self.HeaderLabel.setText(QCoreApplication.translate("bgWidget", u"Payment Info", None))
        self.Customer_Number.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter your Card Number...", None))
        self.Customer_ID.setPlaceholderText(QCoreApplication.translate("bgWidget", u"Enter your Customer ID...", None))
        self.Asterisk_9.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.label_4.setText(QCoreApplication.translate("bgWidget", u"Customer ID", None))
        ___qtablewidgetitem = self.Total_Cost_Info_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bgWidget", u"Ticket Fare", None));
        ___qtablewidgetitem1 = self.Total_Cost_Info_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bgWidget", u"Net Tax", None));
        ___qtablewidgetitem2 = self.Total_Cost_Info_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bgWidget", u"Date", None));
    # retranslateUi

