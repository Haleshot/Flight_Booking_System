# import libraries used in this project
import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QMovie
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QMessageBox, QInputDialog
import mysql.connector
from datetime import date
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import QCoreApplication
import random
from twilio.rest import Client


class Customer_Admin_Option_Screen(QDialog):
    def __init__(self):
        super(Customer_Admin_Option_Screen, self).__init__()
        loadUi(r"Project_Source_Code\Customer_Admin_Option_Screen.ui", self)

        # Displaying the Flight Gif on the label
        self.movie = QMovie("Project_Source_Code\Flight Gif.gif")
        self.Flight_Gif_Label.setMovie(self.movie)
  
        self.startAnimation()
        self.movie.start()
    
    # For the Gif in the Welcome Screen to keep playing.
    def startAnimation(self):
        self.movie.start()
        self.Customer.clicked.connect(self.gotoCustomer)
        self.Admin.clicked.connect(self.gotoAdmin)

    def gotoCustomer(self):
        customer = Welcome_screen()
        widget.addWidget(customer)
        widget.setCurrentIndex(widget.currentIndex() + 1) # Creating a whole bunch/ list of widgets across windows/ screens
        # Helps in displaying the next window on being clicked
    
    def gotoAdmin(self):
        admin = Admin_Screen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)





class Admin_Screen(QDialog):
    def __init__(self):
        super(Admin_Screen, self).__init__()
        loadUi(r"Project_Source_Code\Admin_Screen.ui", self)

        self.Nistara.clicked.connect(self.gotoNistara)
        self.MetAirways.clicked.connect(self.gotoMetAirways)
        self.PiceJet.clicked.connect(self.gotoPiceJet)
        self.Indivo.clicked.connect(self.gotoIndivo)

    def gotoNistara(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter Password")
        msg.setText("Password Field")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Cancel)
        
        x = msg.exec_()


    def gotoMetAirways(self):
        pass

    def gotoPiceJet(self):
        pass

    def gotoIndivo(self):
        pass

    def InputDialog(self):
        pass

    def showPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Enter Password")
        msg.setText("Password Field")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setDefault(QMessageBox.Cancel)

class Welcome_screen(QDialog):
    def __init__(self):
        super(Welcome_screen, self).__init__()
        loadUi(r"Project_Source_Code\Welcome_UI_Screen.ui", self)

        
        # Displaying the Flight Gif on the label
        self.movie = QMovie("Project_Source_Code\Flight Gif.gif")
        self.Flight_Gif_Label.setMovie(self.movie)
  
        self.startAnimation()
        self.movie.start()
    
    # For the Gif in the Welcome Screen to keep playing.
    def startAnimation(self):
        self.movie.start()
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


# Declaring these variables for inserting to the Customer table while inside the Full Profile class.
Email_Field = ""
Password_Field = ""


class Login_screen(QDialog):
    
    def __init__(self):
        super(Login_screen, self).__init__()
        loadUi(r"Project_Source_Code\Login_UI.ui", self)
        self.login.clicked.connect(self.Login_Function)

    def Login_Function(self):
        global Email_Field, Password_Field
        EmailField = self.EmailField.text() # From the text box user entered in the GUI.
        PasswordField = self.PasswordField.text()
        
        Email_Field = EmailField
        Password_Field = PasswordField


        if len(EmailField) == 0 or len(PasswordField) == 0:
            self.Error_Popup_Message.setText("Please input all * fields!")

        else:
            
            db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
            cursor = db.cursor(buffered=True) # Creating an instance to execute various queries
            # buffered = true as results are lazily fetched if buffered = True is not used.
            # Using the same cursor again and again leads to hasty fetching of data by the cursor during execution.
            # buffered = True resolves this issue.

            # query = 'SELECT Password FROM Initial_Info_Account WHERE Username =\''+EmailField+"\'"

            query = """
            SELECT Password FROM Initial_Info_Account WHERE Username = %s
            """

            tpl = (EmailField, )   
            cursor.execute(query, tpl)

            result = cursor.fetchone()

            if result == None:
                self.Error_Popup_Message.setText("Account with this Username doesn't exist! Create Account...") # If account doesn't exist

            else:
                if result[0] == PasswordField: # Checking whether the Value converted from Tuple(fetchone) matches Password or not.
                    print("Sucessfully Logged In!") # Prints this in Terminal

                    query_1 = """
                    SELECT COUNT(*) FROM initial_info_account WHERE PASSWORD IN 
                    (SELECT Password FROM initial_info_account);
                    """

                    cursor.execute(query_1)
                    result = cursor.fetchone()
                    for i in result:
                        print(i)

                    self.Error_Popup_Message.setText("")
                    db.commit()
                    db.close()
                    flight = Flight_Booking_Screen()
                    widget.addWidget(flight)
                    widget.setCurrentIndex(widget.currentIndex() + 1)

                else:
                    self.Error_Popup_Message.setText("Invalid Password!") # Checking Validity of Password



class Create_Screen(QDialog):
    def __init__(self):
        super(Create_Screen, self).__init__()
        loadUi(r"Project_Source_Code\Create_Account_UI.ui", self)
        self.Next_Button.clicked.connect(self.gotoSignUp)


    def gotoSignUp(self):
        global Email_Field, Password_Field
        EmailField = self.EmailField.text()
        PasswordField = self.PasswordField.text()

        Email_Field = EmailField
        Password_Field = PasswordField

        ConfirmPasswordField = self.Confirm_Your_Password_Field.text()
        if len(EmailField) == 0 or len(PasswordField) == 0 or len(ConfirmPasswordField) == 0:
            self.Error_Popup_Message.setText("Please input all * fields!")

        elif PasswordField != ConfirmPasswordField:
            self.Error_Popup_Message.setText("Passwords do not match!")
        
        else:
            
            db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
            cursor = db.cursor(buffered=True)
            Customer_Info = [EmailField, PasswordField]

            query = """
            SELECT Username FROM Initial_Info_Account WHERE Username = %s
            """

            tpl = (EmailField, )   
            cursor.execute(query, tpl)

            result = cursor.fetchone()

            if result != None:
                self.Error_Popup_Message.setText("Account with this Username already exists! Change Username...") # If account doesn't exist

            else:

                cursor.execute('INSERT INTO Initial_Info_Account VALUES (%s, %s);', Customer_Info)
                db.commit()
                db.close()

                fp = Full_Profile_Screen()
                widget.addWidget(fp)
                widget.setCurrentIndex(widget.currentIndex() + 1)

                

        

def Function_for_Returning_to_Full_Profile_Account():
    return Create_Screen()

class Full_Profile_Screen(QDialog):
    def __init__(self):
        super(Full_Profile_Screen, self).__init__()
        
        loadUi(r"Project_Source_Code\Full_Profile_Screen.ui", self)
        self.Sign_Up.clicked.connect(self.SignUp_Function)

        
    def SignUp_Function(self):
        global Email_Field, Password_Field
        
        # Insert values of Username and Password from user into database like how it was done in Login_Function
        
        # Customer_ID = self.Customer_ID.text() as we should not take Customer ID as input from Customer, rather it is incremented by us from MAX Value in Customer ID.
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
        
        
        if len(Customer_Name) == 0 or len(Customer_Gender) == 0 or len(Customer_State) == 0 or len(Customer_Country) == 0 or len(self.Customer_Pincode.text()) == 0 or len(Customer_DOB) == 0 or len(Customer_Phone_Number) == 0:
            self.Error_Popup_Message.setText("Please input all * fields!")

        else:

            db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
            cursor = db.cursor(buffered=True)

            Customer_ID = random.randint(234234, 9345345)


            print(Customer_ID)
            Customer_info_Full_Profile_Account = [Customer_ID, Customer_Name, Customer_State, Customer_Country, Customer_Pincode, Customer_DOB, Customer_Gender, Customer_Phone_Number]

            cursor.execute('INSERT INTO Full_Profile_Account VALUES (%s, %s, %s, %s, %s, %s, %s, %s);', Customer_info_Full_Profile_Account)

            
            Customer_info = [Customer_ID, Customer_Name, Customer_Gender, Customer_DOB, Customer_State, Customer_Country, Customer_Pincode, Email_Field, Password_Field, Customer_Phone_Number]
            print(Customer_info)
            cursor.execute('INSERT INTO Customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', Customer_info)
            
            print()
            print("Succesfully inserted values in the Customer relation") # Displaying in VS Terminal for the developers to know client side
            print(cursor.statement)
            print()

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
        
        loadUi(r"Project_Source_Code\OTP_Screen.ui", self)
        
        
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

        
            account_sid = ''
            auth_token = ''
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
            self.Error_Popup_Message_1.setText("")
            self.Error_Popup_Message_3.setText("OTP Sent to your Mobile Phone!")

            print(message.sid)




    
    def gotoConfirmationOTP(self):

            OTP_Entered = self.OTP_Text_Box.text()
            if len(OTP_Entered) == 0:
                self.Error_Popup_Message_1.setText("Please input all * fields!")

            else:

                OTP_Entered = self.OTP_Text_Box.text()
                print(OTP_Entered)
                self.Error_Popup_Message_1.setText("")

                if int(OTP_Entered) == OTP_Generated:
                    self.Error_Popup_Message_2.setText("Success! Account Created!")
                    self.Next_Button_2.clicked.connect(self.Flight_Screen)

                
                elif OTP_Entered != OTP_Generated:
                    self.Error_Popup_Message_1.setText("Invalid OTP!!")
    

    def Flight_Screen(self):
        flight = Flight_Booking_Screen()
        widget.addWidget(flight)

        widget.setCurrentIndex(widget.currentIndex() + 1)


        

class Flight_Booking_Screen(QDialog):
    def __init__(self):
        super(Flight_Booking_Screen, self).__init__()
        loadUi(r"Project_Source_Code\Flight_Booking_Screen.ui", self)

        self.Find_Flights_Button.clicked.connect(self.gotoFindFlights)




    def gotoFindFlights(self):


        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)

        Departure = self.From_Combo_Box.currentText()
        Arrival = self.To_Combo_Box.currentText()

        Timing = self.Timings_Combo_Box.currentText()
        Airline_Company = self.Airlines_Combo_Box.currentText()


        if Departure == "Select" or Arrival == "Select":
            self.Error_Popup_Message.setText("Please input all * fields!")




        else:
            self.Error_Popup_Message.setText("")
            self.Available_Flights_Table_Widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            if Timing == "Select" and Airline_Company == "Select":
                # query = 'SELECT Password FROM Initial_Info_Account WHERE Username =\''+EmailField+"\'"

                # query = 'SELECT F_arr_Location FROM flights WHERE F_Dept_Location =\''+Departure+"\'"
                query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s"
                print()
                tuple_1 = (Departure, Arrival)
                cursor.execute(query, tuple_1)

                print(cursor.statement)
                print()
                self.Available_Flights_Table_Widget.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
                self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


                result = cursor.fetchall()
                if cursor.rowcount == 0:
                    self.Error_Popup_Message.setText("No Data to fetch from!")
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
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                elif Timing == "Evening/Night":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
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
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



                elif Airline_Company == "MetAirways":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND (F_Company = 'MetAirways' or F_Company = 'MetAir')"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


                elif Airline_Company == "Picejet":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Picejet'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
                    for row_number, row_data in enumerate(result):
                        self.Available_Flights_Table_Widget.insertRow(row_number)

                        for column_number, data in enumerate(row_data):
                            self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


                elif Airline_Company == "Nistara":
                    query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Nistara'"
                
                    tuple_1 = (Departure, Arrival)
                    cursor.execute(query, tuple_1)

                    print(cursor.statement)
                    print()
                    self.Available_Flights_Table_Widget.setRowCount(0)
                    self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
    

                    result = cursor.fetchall()
                    if cursor.rowcount == 0:
                        self.Error_Popup_Message.setText("No Data to fetch from!")
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
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "MetAirways":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'MetAirways' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "Picejet":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'PiceJet' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "Nistara":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Nistara' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%'"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
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
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "MetAirways":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'MetAirways' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                        
                    elif Airline_Company == "Picejet":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'PiceJet' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                    elif Airline_Company == "Nistara":
                        query = "SELECT * FROM flights WHERE F_Dept_Location = %s AND F_Arr_Location = %s AND F_Company = 'Nistara' AND (F_Dept_Time LIKE '%18:10%' or F_Dept_Time LIKE '%19:30%' or F_Dept_Time LIKE '%20:00%' or F_Dept_Time LIKE '%21:00%')"
                    
                        tuple_1 = (Departure, Arrival)
                        cursor.execute(query, tuple_1)

                        print(cursor.statement)
                        print()
                        self.Available_Flights_Table_Widget.setRowCount(0)
                        self.Available_Flights_Table_Widget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.
        

                        result = cursor.fetchall()
                        if cursor.rowcount == 0:
                            self.Error_Popup_Message.setText("No Data to fetch from!")
                        for row_number, row_data in enumerate(result):
                            self.Available_Flights_Table_Widget.insertRow(row_number)

                            for column_number, data in enumerate(row_data):
                                self.Available_Flights_Table_Widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            self.Next_Button.clicked.connect(self.gotoConfirmCustomerPage)
            
    

    def gotoConfirmCustomerPage(self):
        conf = Confirm_Customer_Information()
        widget.addWidget(conf)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    
class Confirm_Customer_Information(QDialog):
    def __init__(self):
        super(Confirm_Customer_Information, self).__init__()
        loadUi(r"Project_Source_Code\Confirm_User_Details_Screen.ui", self)

        self.Customer_Info_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Customer_Info_TableWidget.setColumnWidth(0, 175)
        self.Customer_Info_TableWidget.setColumnWidth(1, 175)
        self.Customer_Info_TableWidget.setColumnWidth(3, 175)
        self.Customer_Info_TableWidget.setColumnWidth(4, 175)

        self.Customer_Info_TableWidget.setColumnWidth(5, 175)
        self.Customer_Info_TableWidget.setColumnWidth(6, 175)
        self.Customer_Info_TableWidget.setColumnWidth(7, 175)
        self.Customer_Info_TableWidget.setColumnWidth(8, 175)


        self.Yes_Button.clicked.connect(self.gotoUpdateCustomer)
        self.No_Button.clicked.connect(self.gotoPaymentPage)

        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)

        query = "SELECT * FROM FULL_CUSTOMER_INFORMATION WHERE Customer_Name = %s;" # Displaying the Information from the VIEW FULL_CUSTOMER_INFORMATION which includes a cartesian product of 
        # the tables initial_info_account and full_profile_account where the Username of Customer_Name columns of the respective relations match.
        tpl = (Email_Field, )           
        cursor.execute(query, tpl)

        print(cursor.statement)
        print()
        self.Customer_Info_TableWidget.setRowCount(0)
        self.Customer_Info_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        result = cursor.fetchall()
        for row_number, row_data in enumerate(result):
            self.Customer_Info_TableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.Customer_Info_TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def gotoUpdateCustomer(self):
        update = Update_Customer_Information()
        widget.addWidget(update)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoPaymentPage(self):
        Pay = Payment_Booking()
        widget.addWidget(Pay)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    
class Update_Customer_Information(QDialog):
    def __init__(self):
        super(Update_Customer_Information, self).__init__()
        loadUi(r"Project_Source_Code\Update_Customer_Information.ui", self)
                
        self.Reenter_Button.clicked.connect(self.gotoReenterDetails)


    def gotoReenterDetails(self):
        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)

        query = """
        DELETE iia, ffa FROM initial_info_account iia INNER JOIN FULL_PROFILE_ACCOUNT ffa
        ON(iia.Username = ffa.Customer_Name)
        WHERE ffa.Customer_Name =
        (SELECT * FROM (SELECT Customer_Name FROM FULL_PROFILE_ACCOUNT ffa WHERE ffa.Customer_Name = %s LIMIT 1) FULL_PROFILE_ACCOUNT);

        """
        
        tpl = (Email_Field, )
                    
        cursor.execute(query, tpl)

        print(cursor.statement)
        print()

        cursor.close()
        db.commit()

        create = Create_Screen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    
Company_ID = 0 # Global variable for accessing chosen Company ID of customer across various classes.
FlightID = 0 # Global variable for accessing chosen Flight ID of customer across various classes.

class Payment_Booking(QDialog):
    def __init__(self):
        super(Payment_Booking, self).__init__()
        loadUi(r"Project_Source_Code\Payment_Booking_Screen.ui", self)
        
        self.User_Input_Flight_ID.clicked.connect(self.Display_User_Flight_ID)
        self.Proceed_To_Summary_Button.clicked.connect(self.gotoSummary_Information)

        
    def Display_User_Flight_ID(self):


        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)
        User_input_Flight_ID = self.Flight_ID.text()


        if len(User_input_Flight_ID) != 0:
            query = "SELECT * FROM flights WHERE F_ID = %s"

            tuple_1 = (User_input_Flight_ID)
            cursor.execute(query, (tuple_1, ))
            

            print(cursor.statement)

            self.User_Flight_Details.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
            self.User_Flight_Details.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


            result = cursor.fetchall()
            
            if cursor.rowcount == 0:
                self.Error_Popup_Message.setText("No Data to fetch from!")
            print(result)
            for row_number, row_data in enumerate(result):
                self.User_Flight_Details.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.User_Flight_Details.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



            db.commit()

    def gotoSummary_Information(self):
        global FlightID
        global Company_ID
        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)
        User_input_Flight_ID = self.Flight_ID.text()


        if len(User_input_Flight_ID) != 0:
            query = "SELECT * FROM flights WHERE F_ID = %s"

            tuple_1 = (User_input_Flight_ID)
            cursor.execute(query, (tuple_1, ))
            result = cursor.fetchall()
            if cursor.rowcount == 0:
                self.Error_Popup_Message.setText("No Data to fetch from!")

            else:
                self.Error_Popup_Message.setText("")
                F_ID = result[0][0]
                F_Dept_Location = result[0][1]
                F_Arr_Location = result[0][2]
                F_Company = result[0][3]
                F_Duration = result[0][4]
                F_Dept_Time = result[0][5]
                F_Arr_Time = result[0][6]
                F_Seats = result[0][7]
                C_ID = result[0][8]

                FlightID = F_ID
                Company_ID = C_ID
                

                F_Info_Customer = [F_ID, F_Dept_Location, F_Arr_Location, F_Company, F_Duration, str(F_Dept_Time), str(F_Arr_Time), F_Seats, C_ID]
                cursor.execute('INSERT INTO Cust_Choice_Flight VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);', F_Info_Customer)

                db.commit()
                db.close()

                print("Succesfully inserted values in the Customer Choice Flight relation") # Displaying in VS Terminal for the developers to know client side

                print(cursor.statement)

                
                sum = Summary()
                widget.addWidget(sum)
                widget.setCurrentIndex(widget.currentIndex() + 1)

Payment_ID = random.randint(3244,54354) # Global variable for accessing generated Payment ID of customer across various classes.
class Payment_Info(QDialog):
    def __init__(self):
        global Payment_ID
        super(Payment_Info, self).__init__()
        loadUi(r"Project_Source_Code\Payment_Info_Screen.ui", self)

        self.Confirm_Payment.clicked.connect(self.confirm)

        self.Total_Cost_Info_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.Total_Cost_Info_TableWidget.setColumnWidth(0, 400)
        self.Total_Cost_Info_TableWidget.setColumnWidth(1, 400)
        self.Total_Cost_Info_TableWidget.setColumnWidth(2, 400)

        self.Payment_Cost = random.randint(3244,6111)
        self.Payment_tax = int(0.1 * self.Payment_Cost)
        self.Payment_Date = str(date.today())

        

        print(self.Payment_Cost, self.Payment_tax, self.Payment_Date)
        print()
        
        self.Total_Cost_Info_TableWidget.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
        self.Total_Cost_Info_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        data = [{"Ticket Fare" : self.Payment_Cost, "Net Tax" : self.Payment_tax, "Date" : self.Payment_Date}]
        row = 0

        self.Total_Cost_Info_TableWidget.setRowCount(len(data) + 1)

        for d in data:
            print()
            self.Total_Cost_Info_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d["Ticket Fare"])))
            self.Total_Cost_Info_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(d["Net Tax"])))
            self.Total_Cost_Info_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(d["Date"]))
            row += 1

        


    def confirm(self):
        Customer_ID = self.Customer_ID.text()
        Customer_Card_Type = self.Customer_Card_Type.currentText()
        Customer_Number = self.Customer_Number.text()


        if len(Customer_ID) == 0 or len(Customer_Card_Type) == 0 or len(Customer_Number) == 0 or not Customer_ID.isdigit():
            self.Error_Popup_Message.setText("Please input all * fields!")

        if Customer_ID.isalpha():
            Customer_ID = random.randint(23334,53342)
        
        if Customer_Number.isalpha():
            Customer_Number = random.randint(23334,53342)
        


        else:
            db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
            cursor = db.cursor(buffered=True)
            Payment_ID = random.randint(3244,54354)

            Payment_Info_Customer = [Payment_ID, Customer_ID, self.Payment_Cost, self.Payment_tax, self.Payment_Date, Customer_Card_Type, Customer_Number]

            cursor.execute('INSERT INTO Payment VALUES (%s, %s, %s, %s, %s, %s, %s);', Payment_Info_Customer)


            db.commit()
            db.close()
            print("Succesfully inserted values in the Payments relation") # Displaying in VS Terminal for the developers to know client side
            success = Success()
            widget.addWidget(success)
            widget.setCurrentIndex(widget.currentIndex() + 1)



class Update_Flight_Info(QDialog):
    def __init__(self):
        super(Update_Flight_Info, self).__init__()
        loadUi(r"Project_Source_Code\Update_Flight_Information.ui", self)
    
        self.User_Input_Flight_ID.clicked.connect(self.Display_User_Flight_ID)
        self.Proceed_To_Summary_Button.clicked.connect(self.gotoSummary_Information)

    
    def Display_User_Flight_ID(self):


        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)
        User_input_Flight_ID = self.Flight_ID.text()


        if len(User_input_Flight_ID) != 0:
            query = "SELECT * FROM flights WHERE F_ID = %s"

            tuple_1 = (User_input_Flight_ID)
            cursor.execute(query, (tuple_1, ))
            

            print(cursor.statement)
            print()


            self.User_Flight_Details.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.User_Flight_Details.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
            self.User_Flight_Details.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


            result = cursor.fetchall()
            print(result)
            for row_number, row_data in enumerate(result):
                self.User_Flight_Details.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.User_Flight_Details.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



            db.commit()

    def gotoSummary_Information(self):
        global FlightID
        global Company_ID
        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)
        User_input_Flight_ID = self.Flight_ID.text()


        if len(User_input_Flight_ID) != 0:
            query = "SELECT * FROM flights WHERE F_ID = %s"

            tuple_1 = (User_input_Flight_ID)
            cursor.execute(query, (tuple_1, ))
            result = cursor.fetchall()
            User_input_Flight_ID = self.Flight_ID.text()
            F_ID = User_input_Flight_ID
            F_Dept_Location = result[0][1]
            F_Arr_Location = result[0][2]
            F_Company = result[0][3]
            F_Duration = result[0][4]
            F_Dept_Time = result[0][5]
            F_Arr_Time = result[0][6]
            F_Seats = result[0][7]
            C_ID = result[0][8]

            Company_ID = C_ID
            

            F_Info_Customer = [F_ID, F_Dept_Location, F_Arr_Location, F_Company, F_Duration, str(F_Dept_Time), str(F_Arr_Time), F_Seats, C_ID, FlightID]


            query = "UPDATE Cust_Choice_Flight SET F_ID = %s, F_Dept_Location = %s, F_Arr_Location = %s, F_Company = %s, F_Duration = %s, F_Dept_Time = %s, F_Arr_Time = %s, F_Seats = %s, C_ID = %s WHERE F_ID = %s"
            print()

            cursor.execute(query, F_Info_Customer)

            db.commit()
            db.close()

            FlightID = F_ID
            print("Succesfully Updated values of the Customer Choice Flight relation") # Displaying in VS Terminal for the developers to know client side

            print(cursor.statement)

            
            sum = Summary()
            widget.addWidget(sum)
            widget.setCurrentIndex(widget.currentIndex() + 1)



class Summary(QDialog):
    def __init__(self):

        super(Summary, self).__init__()
        loadUi(r"Project_Source_Code\Summary_Screen.ui", self)
        
        self.Customer_Info_pushButton.clicked.connect(self.gotoUpdateCustomerInfo)
        self.Flight_Info_pushButton.clicked.connect(self.gotoUpdateFlightInfo)
        self.Yes_Button.clicked.connect(self.gotoPaymentInfo)
        self.No_Button.clicked.connect(self.gotoPaymentBooking_Screen)

        self.See_Additional_Info_button.clicked.connect(self.gotoAdditionalFlightInfo)
        

        # Declaing the use of Global variables here.
        global Email_Field
        global FlightID

        self.Customer_Info_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.User_Selected_Flights_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        self.Customer_Info_TableWidget.setColumnWidth(0, 175)
        self.Customer_Info_TableWidget.setColumnWidth(1, 175)
        self.Customer_Info_TableWidget.setColumnWidth(3, 175)
        self.Customer_Info_TableWidget.setColumnWidth(4, 175)

        self.Customer_Info_TableWidget.setColumnWidth(5, 175)
        self.Customer_Info_TableWidget.setColumnWidth(6, 175)
        self.Customer_Info_TableWidget.setColumnWidth(7, 175)
        self.Customer_Info_TableWidget.setColumnWidth(8, 175)


        self.User_Selected_Flights_TableWidget.setColumnWidth(0, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(1, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(2, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(3, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(4, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(5, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(6, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(7, 175)
        self.User_Selected_Flights_TableWidget.setColumnWidth(8, 175)
        

        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)

        query = "SELECT * FROM FULL_CUSTOMER_INFORMATION WHERE Customer_Name = %s;" # Displaying the Information from the VIEW FULL_CUSTOMER_INFORMATION which includes a cartesian product of 
        # the tables initial_info_account and full_profile_account where the Username of Customer_Name columns of the respective relations match.
        tpl = (Email_Field, )           
        cursor.execute(query, tpl)

        print(cursor.statement)
        print()
        self.Customer_Info_TableWidget.setRowCount(0)
        self.Customer_Info_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        result = cursor.fetchall()
        for row_number, row_data in enumerate(result):
            self.Customer_Info_TableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.Customer_Info_TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


        
        query = "SELECT * FROM flights WHERE F_ID = %s"

        tuple_1 = (FlightID)
        cursor.execute(query, (tuple_1, ))
        

        print(cursor.statement)

        self.User_Selected_Flights_TableWidget.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
        self.User_Selected_Flights_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        result = cursor.fetchall()
        print(result)
        for row_number, row_data in enumerate(result):
            self.User_Selected_Flights_TableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.User_Selected_Flights_TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



            db.commit()
        
    def gotoUpdateCustomerInfo(self):
        update = Update_Customer_Information()
        widget.addWidget(update)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotoUpdateFlightInfo(self):
        update = Update_Flight_Info()
        widget.addWidget(update)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    
    def gotoPaymentInfo(self):
        pay = Payment_Info()
        widget.addWidget(pay)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoAdditionalFlightInfo(self):
        Additional = Additional_Info()
        widget.addWidget(Additional)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def gotoPaymentBooking_Screen(self):
        Pay = Payment_Booking()
        widget.addWidget(Pay)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    
class Additional_Info(QDialog):
    def __init__(self):

        super(Additional_Info, self).__init__()
        loadUi(r"Project_Source_Code\More_Flight_Details_Screen.ui", self)
        self.Back_To_Summary_Button.clicked.connect(self.gotoSummary)
        
        self.Flight_Info_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Flight_Info_TableWidget.setColumnWidth(0, 150)
        self.Flight_Info_TableWidget.setColumnWidth(1, 150)
        self.Flight_Info_TableWidget.setColumnWidth(2, 0)        
        self.Flight_Info_TableWidget.setColumnWidth(3, 150)        
        self.Flight_Info_TableWidget.setColumnWidth(4, 400)
        

        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)

        query = "SELECT * FROM COMPANY WHERE C_ID = %s;"
        tpl = (Company_ID, )           
        cursor.execute(query, tpl)

        print(cursor.statement)
        print()

        result = cursor.fetchall()
        C_Name = result[0][0]
        print(C_Name)
        print()
        print()

        query = "SELECT * FROM COMPANY NATURAL JOIN\t" 
        
        query_that_contains = query[:35] + C_Name + query[35:]

        query = query_that_contains + " WHERE C_ID = %s;"

        tpl = (Company_ID,)           
        cursor.execute(query, tpl)

        print(cursor.statement)
        print()

        result = cursor.fetchall()


        self.Flight_Info_TableWidget.setRowCount(0)
        self.Flight_Info_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        print(result)
        print()


        for row_number, row_data in enumerate(result):
            self.Flight_Info_TableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.Flight_Info_TableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            db.commit()

    def gotoSummary(self):
        sum = Summary()
        widget.addWidget(sum)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Success(QDialog):
    def __init__(self):

        super(Success, self).__init__()
        loadUi(r"Project_Source_Code\Success_Payment_Screen.ui", self)

        self.Yes_Button.clicked.connect(self.gotoRefund)
        self.Quit_Button.clicked.connect(QCoreApplication.instance().quit)
        

    def gotoRefund(self):
        cancellation = Cancellation()
        widget.addWidget(cancellation)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Cancellation(QDialog):
    def __init__(self):

        super(Cancellation, self).__init__()
        loadUi(r"Project_Source_Code\Cancellation_Refund_Screen.ui", self)
        self.Quit_Button.clicked.connect(QCoreApplication.instance().quit)

        global Payment_ID

        self.Cancellation_Info_TableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Cancellation_Info_TableWidget.setColumnWidth(0, 350)
        self.Cancellation_Info_TableWidget.setColumnWidth(1, 350)
        self.Cancellation_Info_TableWidget.setColumnWidth(2, 350)
        self.Cancellation_Info_TableWidget.setColumnWidth(3, 350)
        
        self.Cancellation_ID = random.randint(3244,54354)
        self.Refund_Cost = random.randint(1233, 2500)
        self.Cancellation_Date = str(date.today())
        


        
        self.Cancellation_Info_TableWidget.setRowCount(0) # Setting the rowcount as zero so the QTableWidget refreshes everytime according to the applied filters.
        self.Cancellation_Info_TableWidget.verticalHeader().setVisible(False)  #Hiding the Row Count Numbers displayed on the side.


        data = [{"Cancellation ID" : self.Cancellation_ID, "Cancellation Payment ID" : Payment_ID, "Cancellation Refund": self.Refund_Cost, "Cancellation Date" : self.Cancellation_Date}]
        row = 0

        self.Cancellation_Info_TableWidget.setRowCount(len(data) + 1)

        for d in data:
            print()
            self.Cancellation_Info_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d["Cancellation ID"])))
            self.Cancellation_Info_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(d["Cancellation Payment ID"])))
            self.Cancellation_Info_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(d["Cancellation Refund"])))
            self.Cancellation_Info_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(d["Cancellation Date"])))
            row += 1


        db = mysql.connector.connect(host = 'localhost', database='DBMS_PROJECT', user = 'root', password = 'Haleshot@2003')
        cursor = db.cursor(buffered=True)



        Refund_Info_Customer = [self.Cancellation_ID, Payment_ID, self.Refund_Cost, self.Cancellation_Date]

        cursor.execute('INSERT INTO Cancellation VALUES (%s, %s, %s, %s);', Refund_Info_Customer)


        db.commit()
        db.close()
        print("Succesfully inserted values in the Cancellation relation") # Displaying in VS Terminal for the developers to know client side
            





# Main
app = QApplication(sys.argv) # Launching the app with this variable
choice_option = Customer_Admin_Option_Screen() # Creating an instance for the class created above

widget = QStackedWidget() # Helps in moving between various screens/windows
widget.addWidget(choice_option)
widget.setFixedHeight(801) # Fixing the Height of the GUI Window to 800
widget.setFixedWidth(1201) # Fixing the Width of the GUI Window to 1200
widget.setWindowTitle("Flight Booking") # Setting Window Title
widget.show() # Displaying the whole Application

try: # In case the app doesn't exit.
    sys.exit(app.exec())
except:
    print("Exiting...") # Printing confirmation message of Application exit in VS Terminal.