# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nistara_Payments_Info.ui'
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
        self.Flight_Info_TableWidget = QTableWidget(Dialog)
        if (self.Flight_Info_TableWidget.columnCount() < 8):
            self.Flight_Info_TableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Flight_Info_TableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.Flight_Info_TableWidget.setObjectName(u"Flight_Info_TableWidget")
        self.Flight_Info_TableWidget.setGeometry(QRect(30, 190, 1151, 111))
        self.HeaderLabel = QLabel(Dialog)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(210, 30, 771, 71))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Back_To_Summary_Button = QPushButton(Dialog)
        self.Back_To_Summary_Button.setObjectName(u"Back_To_Summary_Button")
        self.Back_To_Summary_Button.setGeometry(QRect(470, 660, 281, 51))
        self.Back_To_Summary_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.Flight_Info_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Payment ID", None));
        ___qtablewidgetitem1 = self.Flight_Info_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Payment Customer ID", None));
        ___qtablewidgetitem2 = self.Flight_Info_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Payment Cost", None));
        ___qtablewidgetitem3 = self.Flight_Info_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Payment Tax", None));
        ___qtablewidgetitem4 = self.Flight_Info_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Payment Date", None));
        ___qtablewidgetitem5 = self.Flight_Info_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Payment Type", None));
        ___qtablewidgetitem6 = self.Flight_Info_TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Payment Card Number", None));
        ___qtablewidgetitem7 = self.Flight_Info_TableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Flight Company", None));
        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"Nistara Payments Info", None))
        self.Back_To_Summary_Button.setText(QCoreApplication.translate("Dialog", u"Back to Summary", None))
    # retranslateUi

