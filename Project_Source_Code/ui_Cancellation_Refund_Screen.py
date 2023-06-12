# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cancellation_Refund_Screen.ui'
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
        self.Cancellation_Info_TableWidget = QTableWidget(Dialog)
        if (self.Cancellation_Info_TableWidget.columnCount() < 4):
            self.Cancellation_Info_TableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.Cancellation_Info_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Cancellation_Info_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Cancellation_Info_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Cancellation_Info_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.Cancellation_Info_TableWidget.setObjectName(u"Cancellation_Info_TableWidget")
        self.Cancellation_Info_TableWidget.setGeometry(QRect(20, 420, 1151, 111))
        self.HeaderLabel = QLabel(Dialog)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(400, 110, 351, 61))
        self.HeaderLabel.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Quit_Button = QPushButton(Dialog)
        self.Quit_Button.setObjectName(u"Quit_Button")
        self.Quit_Button.setGeometry(QRect(460, 650, 281, 51))
        self.Quit_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 170, 211, 231))
        self.label.setPixmap(QPixmap(u"Icons/payment-success.png"))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 160, 321, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.Cancellation_Info_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Cancellation ID", None));
        ___qtablewidgetitem1 = self.Cancellation_Info_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Payment ID", None));
        ___qtablewidgetitem2 = self.Cancellation_Info_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Refund", None));
        ___qtablewidgetitem3 = self.Cancellation_Info_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Date", None));
        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"Cancellation/Refund initiated", None))
        self.Quit_Button.setText(QCoreApplication.translate("Dialog", u"Quit", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Note - Amount should be refunded in 3-5 business days", None))
    # retranslateUi

