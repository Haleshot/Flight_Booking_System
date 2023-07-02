# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nistara_Flight_Options.ui'
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
        self.Available_Flights_Table_Widget = QTableWidget(Dialog)
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
        self.Available_Flights_Table_Widget.setGeometry(QRect(13, 290, 1171, 421))
        self.Timings_Combo_Box = QComboBox(Dialog)
        self.Timings_Combo_Box.addItem("")
        self.Timings_Combo_Box.addItem("")
        self.Timings_Combo_Box.addItem("")
        self.Timings_Combo_Box.setObjectName(u"Timings_Combo_Box")
        self.Timings_Combo_Box.setGeometry(QRect(113, 220, 281, 51))
        self.Timings_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.HeaderLabel = QLabel(Dialog)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        self.HeaderLabel.setGeometry(QRect(203, 10, 821, 51))
        self.HeaderLabel.setStyleSheet(u"\n"
"font: 30pt \"MS Shell Dlg 2\";")
        self.HeaderLabel.setAlignment(Qt.AlignCenter)
        self.From_Combo_Box = QComboBox(Dialog)
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.addItem("")
        self.From_Combo_Box.setObjectName(u"From_Combo_Box")
        self.From_Combo_Box.setGeometry(QRect(113, 110, 281, 51))
        self.From_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.Next_Button = QPushButton(Dialog)
        self.Next_Button.setObjectName(u"Next_Button")
        self.Next_Button.setGeometry(QRect(463, 730, 281, 51))
        self.Next_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.To_Combo_Box = QComboBox(Dialog)
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.addItem("")
        self.To_Combo_Box.setObjectName(u"To_Combo_Box")
        self.To_Combo_Box.setGeometry(QRect(813, 110, 281, 51))
        self.To_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(163, 80, 21, 16))
        self.label.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(833, 80, 16, 16))
        self.label_2.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.Find_Flights_Button = QPushButton(Dialog)
        self.Find_Flights_Button.setObjectName(u"Find_Flights_Button")
        self.Find_Flights_Button.setGeometry(QRect(813, 220, 281, 51))
        self.Find_Flights_Button.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"")
        self.Error_Popup_Message = QLabel(Dialog)
        self.Error_Popup_Message.setObjectName(u"Error_Popup_Message")
        self.Error_Popup_Message.setGeometry(QRect(413, 100, 391, 31))
        self.Error_Popup_Message.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")
        self.Error_Popup_Message.setAlignment(Qt.AlignCenter)
        self.From_Label = QLabel(Dialog)
        self.From_Label.setObjectName(u"From_Label")
        self.From_Label.setGeometry(QRect(117, 78, 51, 31))
        self.From_Label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.From_Label_2 = QLabel(Dialog)
        self.From_Label_2.setObjectName(u"From_Label_2")
        self.From_Label_2.setGeometry(QRect(113, 180, 61, 31))
        self.From_Label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.To_Label = QLabel(Dialog)
        self.To_Label.setObjectName(u"To_Label")
        self.To_Label.setGeometry(QRect(810, 70, 31, 41))
        self.To_Label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.Airlines_Combo_Box = QComboBox(Dialog)
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.addItem("")
        self.Airlines_Combo_Box.setObjectName(u"Airlines_Combo_Box")
        self.Airlines_Combo_Box.setGeometry(QRect(460, 220, 281, 51))
        self.Airlines_Combo_Box.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.From_Label_3 = QLabel(Dialog)
        self.From_Label_3.setObjectName(u"From_Label_3")
        self.From_Label_3.setGeometry(QRect(460, 180, 121, 31))
        self.From_Label_3.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtablewidgetitem = self.Available_Flights_Table_Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Flight ID", None));
        ___qtablewidgetitem1 = self.Available_Flights_Table_Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Flight Departure", None));
        ___qtablewidgetitem2 = self.Available_Flights_Table_Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Flight Arrival", None));
        ___qtablewidgetitem3 = self.Available_Flights_Table_Widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Flight Company", None));
        ___qtablewidgetitem4 = self.Available_Flights_Table_Widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Flight Duration", None));
        ___qtablewidgetitem5 = self.Available_Flights_Table_Widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Departure Time", None));
        ___qtablewidgetitem6 = self.Available_Flights_Table_Widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Arrival Time", None));
        ___qtablewidgetitem7 = self.Available_Flights_Table_Widget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Seats", None));
        ___qtablewidgetitem8 = self.Available_Flights_Table_Widget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Company ID", None));
        self.Timings_Combo_Box.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.Timings_Combo_Box.setItemText(1, QCoreApplication.translate("Dialog", u"Day", None))
        self.Timings_Combo_Box.setItemText(2, QCoreApplication.translate("Dialog", u"Evening/Night", None))

        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"FLIGHT BOOKING TICKET SYSTEM", None))
        self.From_Combo_Box.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.From_Combo_Box.setItemText(1, QCoreApplication.translate("Dialog", u"Chennai", None))
        self.From_Combo_Box.setItemText(2, QCoreApplication.translate("Dialog", u"Mumbai", None))
        self.From_Combo_Box.setItemText(3, QCoreApplication.translate("Dialog", u"Delhi", None))
        self.From_Combo_Box.setItemText(4, QCoreApplication.translate("Dialog", u"Bangalore", None))

        self.Next_Button.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.To_Combo_Box.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.To_Combo_Box.setItemText(1, QCoreApplication.translate("Dialog", u"Chennai", None))
        self.To_Combo_Box.setItemText(2, QCoreApplication.translate("Dialog", u"Mumbai", None))
        self.To_Combo_Box.setItemText(3, QCoreApplication.translate("Dialog", u"Delhi", None))
        self.To_Combo_Box.setItemText(4, QCoreApplication.translate("Dialog", u"Bangalore", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.Find_Flights_Button.setText(QCoreApplication.translate("Dialog", u"Find Flights", None))
        self.Error_Popup_Message.setText("")
        self.From_Label.setText(QCoreApplication.translate("Dialog", u"FROM", None))
        self.From_Label_2.setText(QCoreApplication.translate("Dialog", u"Timings", None))
        self.To_Label.setText(QCoreApplication.translate("Dialog", u"TO", None))
        self.Airlines_Combo_Box.setItemText(0, QCoreApplication.translate("Dialog", u"Select", None))
        self.Airlines_Combo_Box.setItemText(1, QCoreApplication.translate("Dialog", u"Indivo", None))
        self.Airlines_Combo_Box.setItemText(2, QCoreApplication.translate("Dialog", u"MetAirways", None))
        self.Airlines_Combo_Box.setItemText(3, QCoreApplication.translate("Dialog", u"Picejet", None))
        self.Airlines_Combo_Box.setItemText(4, QCoreApplication.translate("Dialog", u"Nistara", None))

        self.From_Label_3.setText(QCoreApplication.translate("Dialog", u"Airline Company", None))
    # retranslateUi

