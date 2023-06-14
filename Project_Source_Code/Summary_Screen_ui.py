# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Summary_Screen.ui'
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
        self.HeaderLabel.setGeometry(QRect(490, 20, 271, 71))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.Yes_Button = QPushButton(bgWidget)
        self.Yes_Button.setObjectName(u"Yes_Button")
        self.Yes_Button.setGeometry(QRect(446, 631, 281, 51))
        self.Yes_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.label_2 = QLabel(bgWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(346, 571, 511, 51))
        self.label_2.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.Customer_Info_TableWidget = QTableWidget(bgWidget)
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
        self.Customer_Info_TableWidget.setGeometry(QRect(20, 130, 1151, 111))
        self.label = QLabel(bgWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 311, 31))
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.No_Button = QPushButton(bgWidget)
        self.No_Button.setObjectName(u"No_Button")
        self.No_Button.setGeometry(QRect(446, 710, 281, 51))
        self.No_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.label_3 = QLabel(bgWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 320, 261, 41))
        self.label_3.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.User_Selected_Flights_TableWidget = QTableWidget(bgWidget)
        if (self.User_Selected_Flights_TableWidget.columnCount() < 9):
            self.User_Selected_Flights_TableWidget.setColumnCount(9)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.User_Selected_Flights_TableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        self.User_Selected_Flights_TableWidget.setObjectName(u"User_Selected_Flights_TableWidget")
        self.User_Selected_Flights_TableWidget.setGeometry(QRect(20, 380, 1151, 111))
        self.label_4 = QLabel(bgWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 759, 331, 31))
        self.Yes_Button_2 = QPushButton(bgWidget)
        self.Yes_Button_2.setObjectName(u"Yes_Button_2")
        self.Yes_Button_2.setGeometry(QRect(1210, 850, 281, 51))
        self.Yes_Button_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.label_5 = QLabel(bgWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1110, 790, 511, 51))
        self.label_5.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.No_Button_2 = QPushButton(bgWidget)
        self.No_Button_2.setObjectName(u"No_Button_2")
        self.No_Button_2.setGeometry(QRect(1210, 940, 281, 51))
        self.No_Button_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"")
        self.label_6 = QLabel(bgWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(1504, 949, 331, 31))
        self.label_7 = QLabel(bgWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 240, 421, 41))
        self.label_7.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.Customer_Info_pushButton = QPushButton(bgWidget)
        self.Customer_Info_pushButton.setObjectName(u"Customer_Info_pushButton")
        self.Customer_Info_pushButton.setGeometry(QRect(470, 250, 161, 31))
        self.Customer_Info_pushButton.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.label_8 = QLabel(bgWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 500, 421, 41))
        self.label_8.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.Flight_Info_pushButton = QPushButton(bgWidget)
        self.Flight_Info_pushButton.setObjectName(u"Flight_Info_pushButton")
        self.Flight_Info_pushButton.setGeometry(QRect(470, 510, 161, 31))
        self.Flight_Info_pushButton.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.See_Additional_Info_button = QPushButton(bgWidget)
        self.See_Additional_Info_button.setObjectName(u"See_Additional_Info_button")
        self.See_Additional_Info_button.setGeometry(QRect(900, 510, 271, 41))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.See_Additional_Info_button.setFont(font)
        self.See_Additional_Info_button.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("bgWidget", u"Summary", None))
        self.Yes_Button.setText(QCoreApplication.translate("bgWidget", u"Yes", None))
        self.label_2.setText(QCoreApplication.translate("bgWidget", u"Do you want to proceed to Payment ?", None))
        ___qtablewidgetitem = self.Customer_Info_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bgWidget", u"Name", None));
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem.setWhatsThis(QCoreApplication.translate("bgWidget", u"fgdfg", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem1 = self.Customer_Info_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bgWidget", u"State", None));
        ___qtablewidgetitem2 = self.Customer_Info_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bgWidget", u"Country", None));
        ___qtablewidgetitem3 = self.Customer_Info_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("bgWidget", u"Pincode", None));
        ___qtablewidgetitem4 = self.Customer_Info_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("bgWidget", u"Date Of Birth", None));
        ___qtablewidgetitem5 = self.Customer_Info_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("bgWidget", u"Gender", None));
        ___qtablewidgetitem6 = self.Customer_Info_TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("bgWidget", u"Phone Number", None));
        self.label.setText(QCoreApplication.translate("bgWidget", u"Customer Information:", None))
        self.No_Button.setText(QCoreApplication.translate("bgWidget", u"No", None))
        self.label_3.setText(QCoreApplication.translate("bgWidget", u"Flight Information:", None))
        ___qtablewidgetitem7 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("bgWidget", u"Flight ID", None));
        ___qtablewidgetitem8 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("bgWidget", u"Flight Departure", None));
        ___qtablewidgetitem9 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("bgWidget", u"Flight Arrival", None));
        ___qtablewidgetitem10 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("bgWidget", u"Flight Company", None));
        ___qtablewidgetitem11 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("bgWidget", u"Flight Duration", None));
        ___qtablewidgetitem12 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("bgWidget", u"Departure Time", None));
        ___qtablewidgetitem13 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("bgWidget", u"Arrival Time", None));
        ___qtablewidgetitem14 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("bgWidget", u"Seats", None));
        ___qtablewidgetitem15 = self.User_Selected_Flights_TableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("bgWidget", u"Company ID", None));
        self.label_4.setText(QCoreApplication.translate("bgWidget", u"(Takes you to see list of available flights to choose from)", None))
        self.Yes_Button_2.setText(QCoreApplication.translate("bgWidget", u"Yes", None))
        self.label_5.setText(QCoreApplication.translate("bgWidget", u"Do you want to proceed to Payment ?", None))
        self.No_Button_2.setText(QCoreApplication.translate("bgWidget", u"No", None))
        self.label_6.setText(QCoreApplication.translate("bgWidget", u"(Takes you to see list of available flights to choose from)", None))
        self.label_7.setText(QCoreApplication.translate("bgWidget", u"Do you want to change Customer Information?", None))
        self.Customer_Info_pushButton.setText(QCoreApplication.translate("bgWidget", u"Yes", None))
        self.label_8.setText(QCoreApplication.translate("bgWidget", u"Do you want to change Flight Information?", None))
        self.Flight_Info_pushButton.setText(QCoreApplication.translate("bgWidget", u"Yes", None))
        self.See_Additional_Info_button.setText(QCoreApplication.translate("bgWidget", u"See additional Flight Information", None))
    # retranslateUi

