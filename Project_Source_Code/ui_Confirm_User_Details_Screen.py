# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Confirm_User_Details_Screen.ui'
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
        self.HeaderLabel = QLabel(bgwidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(190, 30, 821, 61))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Customer_Info_TableWidget = QTableWidget(bgwidget)
        if (self.Customer_Info_TableWidget.columnCount() < 7):
            self.Customer_Info_TableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.Customer_Info_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Customer_Info_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Customer_Info_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Customer_Info_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Customer_Info_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Customer_Info_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Customer_Info_TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.Customer_Info_TableWidget.setObjectName(u"Customer_Info_TableWidget")
        self.Customer_Info_TableWidget.setGeometry(QRect(20, 180, 1151, 211))
        self.label = QLabel(bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 140, 311, 31))
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.Yes_Button = QPushButton(bgwidget)
        self.Yes_Button.setObjectName(u"Yes_Button")
        self.Yes_Button.setGeometry(QRect(460, 600, 281, 51))
        self.Yes_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.label_2 = QLabel(bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 540, 621, 51))
        self.label_2.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.No_Button = QPushButton(bgwidget)
        self.No_Button.setObjectName(u"No_Button")
        self.No_Button.setGeometry(QRect(460, 690, 281, 51))
        self.No_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"")

        self.retranslateUi(bgwidget)

        QMetaObject.connectSlotsByName(bgwidget)
    # setupUi

    def retranslateUi(self, bgwidget):
        bgwidget.setWindowTitle(QCoreApplication.translate("bgwidget", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("bgwidget", u"Update Customer Information", None))
        ___qtablewidgetitem = self.Customer_Info_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bgwidget", u"Name", None));
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem.setWhatsThis(QCoreApplication.translate("bgwidget", u"fgdfg", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem1 = self.Customer_Info_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bgwidget", u"State", None));
        ___qtablewidgetitem2 = self.Customer_Info_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bgwidget", u"Country", None));
        ___qtablewidgetitem3 = self.Customer_Info_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("bgwidget", u"Pincode", None));
        ___qtablewidgetitem4 = self.Customer_Info_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("bgwidget", u"Date Of Birth", None));
        ___qtablewidgetitem5 = self.Customer_Info_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("bgwidget", u"Gender", None));
        ___qtablewidgetitem6 = self.Customer_Info_TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("bgwidget", u"Phone Number", None));
        self.label.setText(QCoreApplication.translate("bgwidget", u"Customer Information:", None))
        self.Yes_Button.setText(QCoreApplication.translate("bgwidget", u"Yes", None))
        self.label_2.setText(QCoreApplication.translate("bgwidget", u"Do you want to change Customer Information?", None))
        self.No_Button.setText(QCoreApplication.translate("bgwidget", u"No", None))
    # retranslateUi

