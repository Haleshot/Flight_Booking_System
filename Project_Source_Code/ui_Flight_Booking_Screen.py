# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Flight_Booking_Screen.ui'
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
        self.HeaderLabel.setGeometry(QRect(200, 10, 821, 51))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 30pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.From_Combo_Box = QComboBox(bgWidget)
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.setObjectName(u"From_Combo_Box")
        self.From_Combo_Box.setGeometry(QRect(110, 110, 281, 51))
        self.From_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.From_Label = QLabel(bgWidget)
        self.From_Label.setObjectName(u"From_Label")
        self.From_Label.setGeometry(QRect(114, 78, 51, 31))
        self.From_Label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Available_Flights_Table_Widget = QTableWidget(bgWidget)
        if (self.Available_Flights_Table_Widget.columnCount() < 9):
            self.Available_Flights_Table_Widget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Available_Flights_Table_Widget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.Available_Flights_Table_Widget.setObjectName(u"Available_Flights_Table_Widget")
        self.Available_Flights_Table_Widget.setGeometry(QRect(10, 290, 1171, 421))
        self.To_Combo_Box = QComboBox(bgWidget)
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.setObjectName(u"To_Combo_Box")
        self.To_Combo_Box.setGeometry(QRect(810, 110, 281, 51))
        self.To_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.To_Label = QLabel(bgWidget)
        self.To_Label.setObjectName(u"To_Label")
        self.To_Label.setGeometry(QRect(807, 70, 31, 41))
        self.To_Label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Timings_Combo_Box = QComboBox(bgWidget)
        self.Timings_Combo_Box.addItem("")
        self.Timings_Combo_Box.addItem("")
        self.Timings_Combo_Box.addItem("")
        self.Timings_Combo_Box.setObjectName(u"Timings_Combo_Box")
        self.Timings_Combo_Box.setGeometry(QRect(110, 220, 281, 51))
        self.Timings_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.Airlines_Combo_Box = QComboBox(bgWidget)
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.setObjectName(u"Airlines_Combo_Box")
        self.Airlines_Combo_Box.setGeometry(QRect(460, 220, 281, 51))
        self.Airlines_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.From_Label_2 = QLabel(bgWidget)
        self.From_Label_2.setObjectName(u"From_Label_2")
        self.From_Label_2.setGeometry(QRect(110, 180, 61, 31))
        self.From_Label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.From_Label_3 = QLabel(bgWidget)
        self.From_Label_3.setObjectName(u"From_Label_3")
        self.From_Label_3.setGeometry(QRect(460, 180, 121, 31))
        self.From_Label_3.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label = QLabel(bgWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 80, 21, 16))
        self.label.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.label_2 = QLabel(bgWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(830, 80, 16, 16))
        self.label_2.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.Find_Flights_Button = QPushButton(bgWidget)
        self.Find_Flights_Button.setObjectName(u"Find_Flights_Button")
        self.Find_Flights_Button.setGeometry(QRect(810, 220, 281, 51))
        self.Find_Flights_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Error_Popup_Message = QLabel(bgWidget)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(410, 100, 391, 31))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)
        self.Next_Button = QPushButton(bgWidget)
        self.Next_Button.setObjectName(u"Next_Button")
        self.Next_Button.setGeometry(QRect(460, 730, 281, 51))
        self.Next_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")

        self.retranslateUi(bgWidget)

        QMetaObject.connectSlotsByName(bgWidget)
    # setupUi

    def retranslateUi(self, bgWidget):
        bgWidget.setWindowTitle(QCoreApplication.translate("bgWidget", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("bgWidget", u"FLIGHT BOOKING TICKET SYSTEM", None))
        self.From_Combo_Box.setItemText(0, QCoreApplication.translate("bgWidget", u"Select", None))
        self.From_Combo_Box.setItemText(1, QCoreApplication.translate("bgWidget", u"Chennai", None))
        self.From_Combo_Box.setItemText(2, QCoreApplication.translate("bgWidget", u"Mumbai", None))
        self.From_Combo_Box.setItemText(3, QCoreApplication.translate("bgWidget", u"Delhi", None))
        self.From_Combo_Box.setItemText(4, QCoreApplication.translate("bgWidget", u"Bangalore", None))

        self.From_Label.setText(QCoreApplication.translate("bgWidget", u"FROM", None))
        ___qtablewidgetitem = self.Available_Flights_Table_Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("bgWidget", u"Flight ID", None));
        ___qtablewidgetitem1 = self.Available_Flights_Table_Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("bgWidget", u"Flight Departure", None));
        ___qtablewidgetitem2 = self.Available_Flights_Table_Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("bgWidget", u"Flight Arrival", None));
        ___qtablewidgetitem3 = self.Available_Flights_Table_Widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("bgWidget", u"Flight Company", None));
        ___qtablewidgetitem4 = self.Available_Flights_Table_Widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("bgWidget", u"Flight Duration", None));
        ___qtablewidgetitem5 = self.Available_Flights_Table_Widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("bgWidget", u"Departure Time", None));
        ___qtablewidgetitem6 = self.Available_Flights_Table_Widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("bgWidget", u"Arrival Time", None));
        ___qtablewidgetitem7 = self.Available_Flights_Table_Widget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("bgWidget", u"Seats", None));
        ___qtablewidgetitem8 = self.Available_Flights_Table_Widget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("bgWidget", u"Company ID", None));
        self.To_Combo_Box.setItemText(0, QCoreApplication.translate("bgWidget", u"Select", None))
        self.To_Combo_Box.setItemText(1, QCoreApplication.translate("bgWidget", u"Chennai", None))
        self.To_Combo_Box.setItemText(2, QCoreApplication.translate("bgWidget", u"Mumbai", None))
        self.To_Combo_Box.setItemText(3, QCoreApplication.translate("bgWidget", u"Delhi", None))
        self.To_Combo_Box.setItemText(4, QCoreApplication.translate("bgWidget", u"Bangalore", None))

        self.To_Label.setText(QCoreApplication.translate("bgWidget", u"TO", None))
        self.Timings_Combo_Box.setItemText(0, QCoreApplication.translate("bgWidget", u"Select", None))
        self.Timings_Combo_Box.setItemText(1, QCoreApplication.translate("bgWidget", u"Day", None))
        self.Timings_Combo_Box.setItemText(2, QCoreApplication.translate("bgWidget", u"Evening/Night", None))

        self.Airlines_Combo_Box.setItemText(0, QCoreApplication.translate("bgWidget", u"Select", None))
        self.Airlines_Combo_Box.setItemText(1, QCoreApplication.translate("bgWidget", u"Indivo", None))
        self.Airlines_Combo_Box.setItemText(2, QCoreApplication.translate("bgWidget", u"MetAirways", None))
        self.Airlines_Combo_Box.setItemText(3, QCoreApplication.translate("bgWidget", u"Picejet", None))
        self.Airlines_Combo_Box.setItemText(4, QCoreApplication.translate("bgWidget", u"Nistara", None))

        self.From_Label_2.setText(QCoreApplication.translate("bgWidget", u"Timings", None))
        self.From_Label_3.setText(QCoreApplication.translate("bgWidget", u"Airline Company", None))
        self.label.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.label_2.setText(QCoreApplication.translate("bgWidget", u"*", None))
        self.Find_Flights_Button.setText(QCoreApplication.translate("bgWidget", u"Find Flights", None))
        self.Error_Popup_Message.setText("")
        self.Next_Button.setText(QCoreApplication.translate("bgWidget", u"Next", None))
    # retranslateUi

