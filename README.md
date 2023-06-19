<h1 align="center"> Flight Booking Management Project </h1>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Installtion"> Installtion </a></li>
    <li><a href="#Introduction"> Introduction </a></li>
    <li><a href="#Components of the Database Design">  Components of the Database Design </a></li>
    <ul>
      <li><a href="#Payment">  Payment </a></li>
      <li><a href="#Flights">  Flights </a></li>
      <li><a href="#Cancellation">  Cancellation </a></li>
      <li><a href="#Company">  Company </a></li>
      <li><a href="#Initial Account Info">  Initial Account Info </a></li>
      <li><a href="#Full Account Info">  Full Account Info </a></li>
      <li><a href="#Indivo, Nistara, MetAirways, Picejet">  Indivo, Nistara, MetAirways, Picejet </a></li>
      <li><a href="#Cust_Choice-Flight">  Customer Choice Flight </a></li>
      <li><a href="#Customer">  Customer </a></li>
    </ul>
    <li><a href="#Entity Relationship Diagram">  Entity Relationship Diagram </a></li>
    <li><a href="#Relational Model"> Relational Model </a></li>
    <li><a href="#Normalization"> Normalization </a></li>
    <li><a href="#Learning from the Project"> Learning from the Project </a></li>
    <li><a href="#Challenges Faced"> Challenges Faced </a></li>
    <li><a href="#Conclusion"> Conclusion </a></li>
    <li><a href="#Contributing">  Contributing </a></li>
    <li><a href="#ToDo">  To Do </a></li>
    <li><a href="#Video Demo">  Video Demo </a></li>

  </ol>
</details>
<hr>




<h2 id="Installation"> 📦 Installation </h2>

<p align="justify">

## Installation

To install and set up the Flight Booking Management System project, please follow these steps:

1. **Requirements**: Make sure you have Python installed on your machine. You can check if Python is installed by running `python --version` in your command prompt or terminal. Additionally, ensure that you have MySQL Workbench or a compatible MySQL client installed.

2. **Download Dependencies**: The project's required Python packages and libraries are listed in the `requirements.txt` file. You can install these dependencies by running the following command in your command prompt or terminal:

   ```bash
   pip install -r requirements.txt
   ```

   This will automatically download and install all the necessary packages.

3. **SQL Database Setup**: I have provided an SQL script that includes the necessary commands to create the database and tables. Open the SQL script file and execute each statement one by one in your MySQL Workbench or preferred MySQL client. The database name used in the script is `dbms_project`.

4. **Configure MySQL Connection**: Open the Python file of the project and locate the section where the MySQL connection details are specified. Update the values for the root username and password, as well as the localhost information, to match your MySQL configuration.

5. **Run the Application**: You are now ready to run the Flight Booking Management System. Execute the Python file in your preferred Python environment by running the following command:

   ```bash
   python main.py
   ```

   The application will start, and you can begin exploring its features.

By following these steps, you will have successfully installed and set up the Flight Booking Management System on your local machine. Enjoy using the application to manage flight bookings!

</p>
<hr>



<h2 id="Introduction"> :pencil: Introduction </h2>

<p align="justify">
Welcome to the Flight Booking Management System! This project was developed as part of my DBMS course, combining my knowledge of Python-SQL connectivity and the PyQt5 GUI library to create a user-friendly and visually appealing application. The system allows users to create accounts, log in, and confirm their identity through OTP verification (with occasional help from Twilio, if it's in the mood!). Once logged in, users can easily access and view flight details, including arrival and departure times and locations, presented in a well-organized table format. While the payment and cancellation functionalities are currently in prototype stage, they demonstrate the system's potential for future expansion. Through this project, I have gained valuable experience in working with MySQL and improving my understanding of Python-SQL connectivity, enhancing my skills in database management and application development.

</p>
<hr>




<h2 id="Components of the Database Design"> :cloud: Components of the Database Design </h2>
<p align="justify">

Description of all entities along with their attributes here along with the primary keys for each entity. 

Description of all relationships among various entities along with the specification of the cardinality and participation for all relationships (present in ERD and Relational Schema). 


<h2 id="Payment"> :cloud: Payment </h2>
<p align="justify">

![image](https://user-images.githubusercontent.com/57552973/209421134-a697cee7-2f66-4ac9-92c5-75f3e1fed289.png)

</p>
<hr>

<h2 id="Flights"> :cloud: Flights </h2>
<p align="justify">

![image](https://user-images.githubusercontent.com/57552973/209421140-bb437b5b-6136-460c-bbf6-4ef833094841.png)

</p>
<hr>


<h2 id="Cancellation"> :cloud: Cancellation </h2>
<p align="justify">

![image](https://user-images.githubusercontent.com/57552973/209421148-75a19dd3-cfae-4fa1-bf6b-8c295cd70a6a.png)

</p>
<hr>


<h2 id="Company"> :cloud: Company </h2>
<p align="justify">

![image](https://user-images.githubusercontent.com/57552973/209421152-574e15f2-e9b9-48b3-91cf-d5fb55266c53.png)

</p>
<hr>

<h2 id="Initial Account Info"> :cloud: Initial Account Info </h2>
<p align="justify">

![image](https://github.com/Haleshot/Flight_Booking_System/assets/57552973/bc9fb9ad-f075-4964-b166-97dad8af8821)

</p>
<hr>

<h2 id="Full Account Info"> :cloud: Full Account Info </h2>
<p align="justify">

![image](https://github.com/Haleshot/Flight_Booking_System/assets/57552973/478bc416-ec6f-4e2b-abec-296a38f61256)

</p>
<hr>


<h2 id="Indivo, Nistara, MetAirways, Picejet"> :cloud: Indivo, Nistara, MetAirways, Picejet </h2>
<p align="justify">

### Seperate relations for each of these companies with same attributes.
![image](https://github.com/Haleshot/Flight_Booking_System/assets/57552973/91f256d9-6d74-4bff-90a8-604456f48471)

</p>
<hr>



<h2 id="Cust_Choice-Flight"> :cloud: Customer Choice Flight </h2>
<p align="justify">

![image](https://user-images.githubusercontent.com/57552973/209421173-f2453cc5-9d0f-40b2-95d5-e4ceb4917ea0.png)

</p>
<hr>


<h2 id="Customer"> :cloud: Customer </h2>
<p align="justify">

![image](https://github.com/Haleshot/Flight_Booking_System/assets/57552973/6b8557a2-72d5-468b-855d-b1b9f05940f4)

</p>
<hr>



<h2 id="Entity Relationship Diagram"> :cloud: Entity Relationship Diagram  </h2>
<p align="justify">

### Note - needs to be updated to latest version.

![image](https://user-images.githubusercontent.com/57552973/209421185-3885ed37-5ee9-4246-a15e-8cc76f49ea4a.png)

</p>
<hr>


<h2 id="Relational Model"> :cloud: Relational Model  </h2>
<p align="justify">

### Note - needs to be updated to latest version.


![image](https://user-images.githubusercontent.com/57552973/209421204-84efe978-1ab4-4766-8661-87ffc3528041.png)


</p>
<hr>


<h2 id="Normalization"> :cloud: Normalization  </h2>
<p align="justify">

![image](https://user-images.githubusercontent.com/57552973/209421213-d47ee8d4-8094-4fc8-9300-b264b950985e.png)




![image](https://user-images.githubusercontent.com/57552973/209421217-e957867f-4622-46b5-bcb0-41bd364d6c2c.png)




![image](https://user-images.githubusercontent.com/57552973/209421219-0881e7c7-fb31-437e-b4de-4ec2cf854a93.png)



![image](https://user-images.githubusercontent.com/57552973/209421222-7b23b106-50a1-41b8-8d34-b148b2033482.png)

</p>
<hr>


<h2 id="Learning from the Project"> :cloud: Learning from the Project</h2>
<p align="justify">

Through the development of the Flight Booking Management System, several key learning points were obtained:

- Understanding the Ticket Management/Booking system and its overall process.
- Gaining insight into the integration of front-end (GUI) and back-end (Database) components.
- Efficient retrieval and modification of data based on user preferences.
- Clearer understanding of database management systems, including concepts such as normalization, weak entities, SQL commands, relationship cardinalities, and attribute constraints.
- Exposure to new errors and problems not encountered in weekly labs, leading to enhanced problem-solving skills and a better grasp of MySQL.
- Learning the PyQt5 + Qt Designer interface, enabling the creation of seamless UI screens (screenshots of respective screens shown above).
- Integration of front-end with back-end, extracting user data through GUI elements (text boxes, interactive buttons), and merging them into the respective database relations.

These aspects of the project have contributed to an expanded knowledge base and improved skills in building user-friendly interfaces and effectively managing data within a database system.
</p>
<hr>


<h2 id="Challenges Faced"> :cloud: Challenges Faced</h2>
<p align="justify">
  
During the development of the Flight Booking Management System, the following challenges were encountered:

- Integrating the front end with the back end proved to be a complex task, requiring meticulous attention to detail.
- OTP verification occasionally failed, requiring thorough debugging and refinement of the implementation.
- Data loss and modification issues arose during the merging process to the back end, necessitating rigorous testing and validation procedures.
- Connectivity issues with the MySQL Connector library posed obstacles, requiring extensive research and troubleshooting.
- Some relations within the database fetched incorrect tuples, demanding careful examination and rectification.
- Adding certain values resulted in unexpected program crashes due to primary key errors.
- Ensuring the normalization of tables proved challenging and required meticulous design and restructuring of the database schema.
- Certain buttons in the graphical user interface did not function as intended, and labels were not displayed correctly on their respective screens.
- Importing the appropriate libraries for the project required attention to detail and resolution of any library-related issues.

Overcoming these challenges contributed to the development of a more robust and functional Flight Booking Management System.
</p>
<hr>


<h2 id="Conclusion"> :cloud: Conclusion</h2>
<p align="justify">

In conclusion, the Flight Booking Management System has been successfully implemented, providing customers with a convenient platform for booking flights according to their requirements. Throughout the development process, valuable lessons and accomplishments have been gained, including:

- Acquiring knowledge and experience in integrating the front end (PyQt5) with the back end (Database), resulting in a seamless user interface.
- Enhancing coding skills in Python and effectively applying concepts learned in the DBMS course to develop robust functionalities within the project.
- Deepening understanding of MySQL queries and their implementation, leading to improved database management skills.
- Recognizing the significance of various applications that play a crucial role in our day-to-day lives and comprehending the intricate workings of both front-end and back-end components.
- This project has provided an opportunity for growth and improvement in both technical and problem-solving abilities, setting a solid foundation for future endeavors.

Overall, the Flight Booking Management System has served as a valuable project, not only in terms of learning and implementing key concepts but also in delivering a practical solution for flight ticket booking needs.
</p>
<hr>





<!-- Contributing -->
<h2 id="Contributing"> Contributing </h2>

<p align="justify">

See [the contributing guide](CONTRIBUTING.md) for detailed instructions on how to get started with our project.

If you're looking for a way to contribute, you can scan through our [existing issues](https://github.com/Haleshot/Flight_Booking_System/issues) for something to work on. When ready, check out [Getting Started with Contributing](CONTRIBUTING.md) for detailed instructions.


Click on these badges to see how you might be able to help:

<div align="center" markdown="1">

[![GitHub repo Issues](https://img.shields.io/github/issues/Haleshot/Flight_Booking_System?style=flat&logo=github&logoColor=red&label=Issues)](https://github.com/Haleshot/Flight_Booking_System/issues) [![GitHub repo PRs](https://img.shields.io/github/issues-pr/Haleshot/Flight_Booking_System?style=flat&logo=github&logoColor=orange&label=PRs)](https://github.com/Haleshot/Flight_Booking_System/pulls) [![GitHub repo Merged PRs](https://img.shields.io/github/issues-search/Haleshot/Flight_Booking_System?style=flat&logo=github&logoColor=green&label=Merged%20PRs&query=is%3Amerged)](https://github.com/Haleshot/Flight_Booking_System/pulls?q=is%3Apr+is%3Amerged)

</div>

Simple terms:

1. `Fork` this repository
2. Create a `branch`
3. `Commit` your changes
4. `Push` your `commits` to the `branch`
5. Submit a `pull request`

</p>
<hr>



<!-- To Do -->
<h2 id="ToDo"> To Do </h2>
<p align="justify">


- [ ] Refine UI more
  - [ ] PyQt5 Editor
- [ ] Do Bug testing for all screens.

### In Progress

- [ ] Showing user, which file to run as main file - portraying user flow.
- [ ] Add a Video demo in the form of Gif Link for viewers to easily see the working.

### Done ✓
- [x] Improve README guides, contributing guides, etc.
 Transfer information from the initial profile account table and final profile account table to the Customer Table.
- [x] If SQL fetches no data, print no data near table pop up.
- [x] Create a Rollable screen in which you display a Summary of Customer Details as well as Flight details and give buttons to modify both before proceeding
to Payments Page.
- [x] Try adding unique key constraint or primary key to Username in initial_info_account and full_info_account without getting errors of duplicate entry.
- [x] If user enters string pincode, program crashes, handle that.

</p>
<hr>

<h2 id="Video Demo"> Video Demo </h2>

<img src="https://media.tenor.com/hB9OTbewrikAAAAi/work-work-in-progress.gif" width="200" height="300" /> 

<hr>

<!--
<p align="center"> 
 
 <img src="https://media.tenor.com/hB9OTbewrikAAAAi/work-work-in-progress.gif" width="200" height="300" /> 
 
</p>
--->
