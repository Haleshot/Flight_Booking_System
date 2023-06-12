# DBMS Project
# Updated till 17/09/2022

# import libraries used in this project
from re import A
from sqlite3 import Cursor, connect
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox
from PyQt5.QtGui import QPixmap
import sql
import mysql.connector


import os
import random
import twilio
import twilio.rest
from twilio.rest import Client



"""
Check out this video : 
https://www.youtube.com/watch?v=ksW59gYEl6Q&ab_channel=PyTutorials
"""



"""
TO DO:
1. Transfer information from the initial profile account table and final profile account table to the Customer Table if needed.
3. Handle error when giving integer input for Customer ID and Pincode in Full_Profile_Screen.
4. You can declare all the variables of self.textboxes of Initial Profile Account in init function so you can access all variables in Full Profile account
5. When user creates new account, make sure that when he logs in with the Username and password he created during creation stage,
back to Initial Profile Account.
6. Send user to Flight Booking Screen once he clicks on next after checking OTP.


IMPORTANT:
1 and 4 do combined -> IMPORTANT. INSERT VALUES INTO CUSTOMERS IN FULL PROFILE ACCOUNT CLASS BY GETTING VALUES OF USERNAME
AND PASSWORD FROM Initial Login Account Class. Define those variables in init function.

"""




class Welcome_screen(QDialog):
    def __init__(self):
        super(Welcome_screen, self).__init__()
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\Welcome_UI_Screen.ui", self)
        # Relative Path - loadUi(r"Project_Source_Code\Welcome_UI_Screen.ui", self")
        self.Login.clicked.connect(self.gotoLogin)
        self.Create_an_Account.clicked.connect(self.gotoCreate)

    def gotoLogin(self):
        login = Login_screen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1) # Creating a whole bunch/ list of widgets across windows/ screens
        # Helps in displaying the next window on being clicked
    
    def gotoCreate(self):
        create = Create_Screen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Login_screen(QDialog):
    
    def __init__(self):
        super(Login_screen, self).__init__()
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\Login_UI.ui", self)
        # Relative Path - loadUi(r"Project_Source_Code\Login_UI.ui", self")
        self.login.clicked.connect(self.Login_Function)

    def Login_Function(self):
        EmailField = self.EmailField.text()
        PasswordField = self.PasswordField.text()


        if len(EmailField) == 0 or len(PasswordField) == 0:
            self.Error_Popup_Message.setText("Please input all * fields!")

        else:
            
            db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
            cursor = db.cursor(buffered=True) # Creating an instance to execute various queries
            # buffered = true as results are lazily fetched if buffered = True is not used.
            # Using the same cursor again and again leads to hasty fetching of data by the cursor during execution.
            # buffered = True resolves this issue.

            query = 'SELECT Password FROM Initial_Info_Account WHERE Username =\''+EmailField+"\'"
            cursor.execute(query)
            result = cursor.fetchone()


            if result == None:
                self.Error_Popup_Message.setText("Account with this Username doesn't exist! Create Account...") # If account doesn't exist

            else:
                if result[0] == PasswordField: # Checking whether the Value converted from Tuple(fetchone) matches Password or not.
                    print("Sucessfully Logged In!") # Prints this in Terminal
                    self.Error_Popup_Message.setText("")
                    db.commit()
                    db.close()
                    self.login.clicked.connect(self.Flight_Screen)


                    

                else:
                    self.Error_Popup_Message.setText("Invalid Username or Password!") # Checking Validity of Password


    def Flight_Screen(self):
        flight = Flight_Booking_Screen()
        widget.addWidget(flight)
        widget.setCurrentIndex(widget.currentIndex() + 1)
            
class Create_Screen(QDialog):
    def __init__(self):
        super(Create_Screen, self).__init__()
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\Create_Account_UI.ui", self)
        # Relative Path - loadUi(r"Project_Source_Code\Create_Account_UI.ui", self")
        self.Next_Button.clicked.connect(self.gotoSignUp)

    def gotoSignUp(self):
        
        EmailField = self.EmailField.text()
        PasswordField = self.PasswordField.text()
        ConfirmPasswordField = self.Confirm_Your_Password_Field.text()
        if len(EmailField) == 0 or len(PasswordField) == 0 or len(ConfirmPasswordField) == 0:
            self.Error_Popup_Message.setText("Please input all * fields!")

        elif PasswordField != ConfirmPasswordField:
            self.Error_Popup_Message.setText("Passwords do not match!")
        
        else:
            db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
            cursor = db.cursor(buffered=True)
            Customer_Info = [EmailField, PasswordField]

            cursor.execute('INSERT INTO Initial_Info_Account VALUES (%s, %s);', Customer_Info)
            db.commit()
            db.close()
            self.Next_Button.clicked.connect(self.gotoFull_Login)


    def gotoFull_Login(self):
        fp = Full_Profile_Screen()
        widget.addWidget(fp)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Full_Profile_Screen(QDialog):
    def __init__(self):
        super(Full_Profile_Screen, self).__init__()
        
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\Full_Profile_Screen.ui", self)
        # Relative Path - loadUi(r"Project_Source_Code\Full_Profile_Screen.ui", self")
        self.Sign_Up.clicked.connect(self.SignUp_Function)

        
    def SignUp_Function(self):
        # Insert values of Username and Password from user into database like how it was done in Login_Function
        
        Customer_ID = self.Customer_ID.text()
        Customer_Name = self.Customer_Name.text()
        Customer_Gender = self.Customer_Gender.currentText()
        Customer_State = self.Customer_State.text()
        Customer_Country = self.Customer_Country.text()
        Customer_Pincode = self.Customer_Pincode.text()
        Customer_Phone_Number = self.Customer_Phone_Number.text()
        Customer_DOB = str(self.Customer_DOB.text())
        l = []
        l = Customer_DOB.split("-")
        year = l[2]
        month = l[1]
        day = l[0]
        Customer_DOB = year+ "-" + month+ "-" + day # # Reversing the DOB before inserting into the MySQL database to adhere to the MYSQL Syntax


        if len(Customer_ID) == 0 or len(Customer_Name) == 0 or len(Customer_Gender) == 0 or len(Customer_State) == 0 or len(Customer_Country) == 0 or len(Customer_Pincode) == 0 or len(Customer_DOB) == 0 or len(Customer_Phone_Number) == 0:
            self.Error_Popup_Message.setText("Please input all * fields!")

        else:

            db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
            cursor = db.cursor(buffered=True)
            Customer_info = [Customer_ID, Customer_Name, Customer_State, Customer_Country, Customer_Pincode, Customer_DOB, Customer_Gender, Customer_Phone_Number]

            cursor.execute('INSERT INTO Full_Profile_Account VALUES (%s, %s, %s, %s, %s, %s, %s, %s);', Customer_info)


            db.commit()
            db.close()

            # Loading the OTP Screen after this.

            OTP = OTP_Screen()
            widget.addWidget(OTP)
            widget.setCurrentIndex(widget.currentIndex() + 1)


            
            

            
# Creating a global variable for OTP Generation
OTP_Generated = random.randint(1000, 99343)
class OTP_Screen(QDialog):
    def __init__(self):
        super(OTP_Screen, self).__init__()
        
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\OTP_Screen.ui", self)
        # Relative Path - loadUi(r"OTP_Screen.ui", self")
        
        
        print(OTP_Generated)


        self.Send_OTP_Button.clicked.connect(self.OTP_Function)
        self.Check_OTP_Button.clicked.connect(self.gotoConfirmationOTP)

        

    def OTP_Function(self):


        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        Customer_Phone_Number = self.Customer_Phone_Number.text()
        if len(Customer_Phone_Number) == 0:
            self.Error_Popup_Message_1.setText("Please input all * fields!")

        else:

        
            account_sid = 'AC57dc85c6338df700cdb094d3b3b707f3'
            auth_token = 'bdc2d0df15eb75bf9c6ca329f6a016ff'
            client = Client(account_sid, auth_token)

            # WORK ON SENDING OTP TO PHONE ENTERED BY USER.
            
            Customer_Phone_Number = self.Customer_Phone_Number.text()
            Customer_Phone_Number = "+91" + Customer_Phone_Number

            print(OTP_Generated)
            message = client.messages.create(
                                body="Thank you for choosing our Flight Management System! Your OTP is : "+ str(OTP_Generated),
                                from_='+18329798726',
                                to=Customer_Phone_Number
                            )

            self.Error_Popup_Message_3.setText("OTP Sent to your Mobile Phone!")

            print(message.sid)




    
    def gotoConfirmationOTP(self):

            OTP_Entered = self.OTP_Text_Box.text()
            if len(OTP_Entered) == 0:
                self.Error_Popup_Message_1.setText("Please input all * fields!")

            else:

                OTP_Entered = self.OTP_Text_Box.text()
                print(type(OTP_Entered))
                print(OTP_Entered)

                if int(OTP_Entered) == OTP_Generated:
                    self.Error_Popup_Message_2.setText("Success! Account Created!")
                    self.Next_Button_2.clicked.connect(self.gotoConfirmationOTP)

                
                elif OTP_Entered != OTP_Generated:
                    self.Error_Popup_Message_1.setText("Invalid OTP!!")
    

    def Flight_Screen(self):
        flight = Flight_Booking_Screen()
        widget.addWidget(flight)

        widget.setCurrentIndex(widget.currentIndex() + 1)


        

class Flight_Booking_Screen(QDialog):
    def __init__(self):
        super(Flight_Booking_Screen, self).__init__()
        
        loadUi(r"F:\New_Laptop_Documents\NMIMS_College_Docs\2nd_Year\1st_Semester\DBMS\Project\Project_Source_Code\Flight_Booking_Screen.ui", self)
        # Relative Path - loadUi(r"Flight_Booking_Screen.ui", self")

        

        self.Find_Flights_Button.clicked.connect(self.gotoFindFlights)



    def gotoFindFlights(self):


        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)

        Departure = self.From_Combo_Box.currentText()
        Arrival = self.To_Combo_Box.currentText()

        Timing = self.Timings_Combo_Box.currentText()
        Airline_Company = self.Airlines_Combo_Box.currentText()



        if Departure == "Select" or Arrival == "Select" :
            self.Error_Popup_Message.setText("Please input all * fields!")

        else:
            if Timing == "Select" and Airline_Company == "Select":
                # query = 'SELECT Password FROM Initial_Info_Account WHERE Username =\''+EmailField+"\'"

                # query = 'SELECT F_arr_Location FROM flights WHERE F_Dept_Location =\''+Departure+"\'"
                query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s"
                
                tuple_1 = (Departure, Arrival)
                cursor.execute(query, tuple_1)

                print(cursor.statement)
                self.Available_Flights_Table_Widget.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
                self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.Available_Flights_Table_Widget.insertRow(row_number)

                    for column_number, data in enumerate(row_data):
                        self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



                db.commit()

            elif Timing != "Select" and Airline_Company == "Select":
                if Timing == "Day":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                elif Timing == "Evening/Night":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            elif Timing == "Select" and Airline_Company != "Select":

                if Airline_Company == "Indivo":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Indivo'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



                elif Airline_Company == "MetAirways":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND (F_Company = 'MetAirways' or F_Company = 'MetAir')"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


                elif Airline_Company == "Picejet":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Picejet'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


                elif Airline_Company == "Nistara":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Nistara'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


            elif Timing != "Select" and Airline_Company != "Select":
                if Timing == "Day":
                    if Airline_Company == "Indivo":

                    
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Indivo' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "MetAirways":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'MetAirways' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "PiceJet":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'PiceJet' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "Nistara":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Nistara' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                
                
                elif Timing == "Evening/Night":

                    if Airline_Company == "Indivo":
                        
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Indivo' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "MetAirways":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'MetAirways' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                        
                    elif Airline_Company == "PiceJet":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'PiceJet' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "Nistara":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Nistara' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))





# Main
app = QApplication(sys.argv) # Launching the app with this variable
welcome = Welcome_screen() # Creating an instance for the class created above

widget = QStackedWidget() # Helps in moving between various screens/windows
widget.addWidget(welcome)
widget.setFixedHeight(800) # Fixing the Height of the GUI Window to 800
widget.setFixedWidth(1200) # Fixing the Width of the GUI Window to 1200
widget.show() # Displaying the whole Application

try: # In case the app doesn't exit.
    sys.exit(app.exec())
except:
    print("Exiting...") # Printing confirmation message of Application exit in VS Terminal.