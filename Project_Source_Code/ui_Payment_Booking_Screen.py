# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Payment_Booking_Screen.ui'
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
        self.SUMMARY_Label = QLabel(bgWidget)
        self.SUMMARY_Label.setObjectName(u"SUMMARY_Label")
        self.SUMMARY_Label.setGeometry(QRect(180, 20, 821, 51))
        self.SUMMARY_Label.setStyleSheet(u"\n"
"font: 30pt \"MS Shell Dlg 2\";")
        self.SUMMARY_Label.setAlignment(Qt.AlignCenter)
        self.Proceed_To_Summary_Button = QPushButton(bgWidget)
        self.Proceed_To_Summary_Button.setObjectName(u"Proceed_To_Summary_Button")
        self.Proceed_To_Summary_Button.setGeometry(QRect(450, 650, 331, 81))
        self.Proceed_To_Summary_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.User_Flight_Details = QTableWidget(bgWidget)
        if (self.User_Flight_Details.columnCount() < 9):
            self.User_Flight_Details.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.User_Flight_Details.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.User_Flight_Details.setObjectName(u"User_Flight_Details")
        self.User_Flight_Details.setGeometry(QRect(10, 210, 1171, 421))
        self.label_3 = QLabel(bgWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 160, 191, 21))
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.Enter_Flight_ID_Label = QLabel(bgWidget)
        self.Enter_Flight_ID_Label.setObjectName(u"Enter_Flight_ID_Label")
        self.Enter_Flight_ID_Label.setGeometry(QRect(250, 120, 221, 41))
        self.Enter_Flight_ID_Label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.Flight_ID = QLineEdit(bgWidget)
        self.Flight_ID.setObjectName(u"Flight_ID")
        self.Flight_ID.setGeometry(QRect(490, 120, 231, 51))
        self.Flight_ID.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.User_Input_Flight_ID = QPushButton(bgWidget)
        self.User_Input_Flight_ID.setObjectName(u"User_Input_Flight_ID")
        self.User_Input_Flight_ID.setGeometry(QRect(760, 120, 281, 51))
        self.User_Input_Flight_ID.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.label = QLabel(bgWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 740, 491, 21))
        self.Error_Popup_Message = QLabel(bgWidget)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(430, 180, 391, 21))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"Dialog", None))
        self.SUMMARY_Label.setText(QCoreApplication.translate("bgWidget", u"CONFIRM FLIGHT DETAILS", None))
        self.Proceed_To_Summary_Button.setText(QCoreApplication.translate("bgWidget", u"Proceed to Summary", None))
        ___qtablewidgetitem = self.User_Flight_Details.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bgWidget", u"Flight ID", None));
        ___qtablewidgetitem1 = self.User_Flight_Details.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bgWidget", u"Flight Departure", None));
        ___qtablewidgetitem2 = self.User_Flight_Details.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bgWidget", u"Flight Arrival", None));
        ___qtablewidgetitem3 = self.User_Flight_Details.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("bgWidget", u"Flight Company", None));
        ___qtablewidgetitem4 = self.User_Flight_Details.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("bgWidget", u"Flight Duration", None));
        ___qtablewidgetitem5 = self.User_Flight_Details.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("bgWidget", u"Departure Time", None));
        ___qtablewidgetitem6 = self.User_Flight_Details.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("bgWidget", u"Arrival Time", None));
        ___qtablewidgetitem7 = self.User_Flight_Details.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("bgWidget", u"Seats", None));
        ___qtablewidgetitem8 = self.User_Flight_Details.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("bgWidget", u"Company ID", None));
        self.label_3.setText(QCoreApplication.translate("bgWidget", u"(To proceed to Payment)", None))
        self.Enter_Flight_ID_Label.setText(QCoreApplication.translate("bgWidget", u"Enter Flight ID :", None))
        self.User_Input_Flight_ID.setText(QCoreApplication.translate("bgWidget", u"Load Details", None))
        self.label.setText(QCoreApplication.translate("bgWidget", u"Note - Selects the displayed Flight ID. Can be changed later in the Summary Screen.", None))
        self.Error_Popup_Message.setText("")
    # retranslateUi

