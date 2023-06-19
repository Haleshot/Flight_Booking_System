## SQL Database Setup

<h1 align="center"> Flight Booking Management Project </h1>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Database Creation"> Database Creation </a></li>
    <li><a href="#Table Creation"> Table Creation </a></li>
    <li><a href="Insert Sample Data"> Insert Sample Data </a></li> 
    <li><a href="#Configuration"> Configuration </a></li>


  </ol>
</details>
<hr>


<p align="justify">
  
To set up the SQL database and create the necessary tables for the Flight Booking Management System, please follow these steps:

1. **Database Creation**: Execute the SQL statement to create the database.

```bash
CREATE DATABASE `dbms_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
```
</p>
<hr>

<p align="justify">

2. **Table Creation** : Execute the SQL statements to create the required tables.

Payment:
```bash
CREATE TABLE `payment` (
  `Payment_ID` int NOT NULL,
  `Payment_Customer_ID` int NOT NULL,
  `Payment_Cost` float NOT NULL,
  `Payment_Tax` float NOT NULL,
  `Payment_Date` date NOT NULL,
  `Payment_Type` varchar(15) NOT NULL,
  `Payment_Card_No` int NOT NULL,
  PRIMARY KEY (`Payment_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Flights:
```bash
CREATE TABLE `flights` (
  `F_ID` int NOT NULL,
  `F_Dept_Location` varchar(25) NOT NULL,
  `F_Arr_Location` varchar(25) NOT NULL,
  `F_Company` varchar(25) NOT NULL,
  `F_Duration` int NOT NULL,
  `F_Dept_Time` datetime NOT NULL,
  `F_Arr_Time` datetime NOT NULL,
  `F_Seats` int NOT NULL,
  `C_ID` int DEFAULT NULL,
  PRIMARY KEY (`F_ID`),
  KEY `C_ID` (`C_ID`),
  CONSTRAINT `flights_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `company` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Cancellation:
```bash
CREATE TABLE `cancellation` (
  `Canc_ID` int NOT NULL,
  `Canc_Payment_ID` int NOT NULL,
  `Canc_Refund` float NOT NULL,
  `Canc_Date` date NOT NULL,
  PRIMARY KEY (`Canc_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Company:
```bash
CREATE TABLE `company` (
  `C_Name` varchar(25) NOT NULL,
  `C_Type` varchar(25) NOT NULL,
  `C_ID` int NOT NULL,
  PRIMARY KEY (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Initial Account Info:
```bash
CREATE TABLE `initial_info_account` (
  `Username` varchar(20) NOT NULL,
  `Password` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Full Account Info:
```bash
CREATE TABLE `full_profile_account` (
  `Customer_ID` int NOT NULL,
  `Customer_Name` varchar(20) DEFAULT NULL,
  `Customer_State` varchar(15) DEFAULT NULL,
  `Customer_Country` varchar(15) DEFAULT NULL,
  `Customer_Pincode` varchar(10) DEFAULT NULL,
  `Date_Of_Birth` date DEFAULT NULL,
  `Customer_Gender` varchar(40) DEFAULT NULL,
  `PhoneNumber` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Customer_ID`),
  UNIQUE KEY `Customer_Name` (`Customer_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Indivo:
```bash
CREATE TABLE `indivo` (
  `C_ID` int NOT NULL,
  `COMPANY_NAME` varchar(20) DEFAULT NULL,
  `COMPANY_HISTORY` varchar(200) DEFAULT NULL,
  `C_TYPE` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`C_ID`),
  CONSTRAINT `indivo_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `company` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Nistara:
```bash
CREATE TABLE `nistara` (
  `C_ID` int NOT NULL,
  `COMPANY_NAME` varchar(20) DEFAULT NULL,
  `COMPANY_HISTORY` varchar(200) DEFAULT NULL,
  `C_TYPE` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`C_ID`),
  CONSTRAINT `nistara_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `company` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
MetAirways:
```bash
CREATE TABLE `metairways` (
  `C_ID` int NOT NULL,
  `COMPANY_NAME` varchar(20) DEFAULT NULL,
  `COMPANY_HISTORY` varchar(200) DEFAULT NULL,
  `C_TYPE` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`C_ID`),
  CONSTRAINT `metairways_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `company` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Picejet:
```bash
CREATE TABLE `picejet` (
  `C_ID` int NOT NULL,
  `COMPANY_NAME` varchar(20) DEFAULT NULL,
  `COMPANY_HISTORY` varchar(200) DEFAULT NULL,
  `C_TYPE` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`C_ID`),
  CONSTRAINT `picejet_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `company` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Customer Choice Flight:
```bash
CREATE TABLE `cust_choice_flight` (
  `F_ID` int NOT NULL,
  `F_Dept_Location` varchar(25) NOT NULL,
  `F_Arr_Location` varchar(25) NOT NULL,
  `F_Company` varchar(25) NOT NULL,
  `F_Duration` int NOT NULL,
  `F_Dept_Time` datetime NOT NULL,
  `F_Arr_Time` datetime NOT NULL,
  `F_Seats` int NOT NULL,
  `C_ID` int DEFAULT NULL,
  KEY `C_ID` (`C_ID`),
  CONSTRAINT `cust_choice_flight_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `company` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```
Customer:
```bash
CREATE TABLE `customer` (
  `Cust_ID` int NOT NULL AUTO_INCREMENT,
  `Cust_Name` varchar(35) NOT NULL,
  `Cust_Gender` varchar(35) DEFAULT NULL,
  `Cust_DOB` date NOT NULL,
  `Cust_State` varchar(30) NOT NULL,
  `Cust_Country` varchar(30) NOT NULL,
  `Cust_Pincode` varchar(35) DEFAULT NULL,
  `Cust_Login` varchar(25) NOT NULL,
  `Cust_Password` varchar(20) NOT NULL,
  `PhoneNumber` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`Cust_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```

</p>
<hr>

<p align="justify">
  
3. **Insert Sample Data**:

Insert Data for the following tables:

## Flights:
The data for flights insertion can be found [here](https://github.com/Haleshot/Flight_Booking_System/tree/main/Project_Source_Code/SQL_Entries_Flight)

Add data from all 4 text files.


## Initial Profile Account:

```bash
INSERT INTO initial_info_account VALUES("Haleshot", "ggs");
```


## Full Profile Account:

```bash
INSERT INTO full_profile_account VALUES(1, "Haleshot", "TN", "IND", 4007, "2003-09-09", "Male", "995745");
```


## Company:

```bash
INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(Indivo,
Airbus 380,
1);

INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(MetAirways,
Airbus 380,
2);

INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(Picejet,
Airbus 380,
3);

INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(Nistara,
Airbus 380,
4);

INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(Indivo,
Boeing 707,
5);

INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(MetAirways,
Boeing 707,
6);

INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(Picejet,
Boeing 707,
8);

INSERT INTO `dbms_project`.`company`
(`C_Name`,
`C_Type`,
`C_ID`)
VALUES
(Nistara,
Boeing 707,
8);



```


## Nistara:

```bash
INSERT INTO `dbms_project`.`nistara`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(4,
"Nistara",
'Tata SIA Airlines Limited, operating as Nistara, is an Indian full-service airline, based in Gurgaon, with its hub at Indira Gandhi International Airport.',
"Airbus 380"
);




INSERT INTO `dbms_project`.`nistara`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(8,
"Nistara",
'Tata SIA Airlines Limited, operating as Nistara, is an Indian full-service airline, based in Gurgaon, with its hub at Indira Gandhi International Airport.',
"Airbus 380"
);

```


## Indivo:
```bash

INSERT INTO `dbms_project`.`indivo`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(1,
"Indivo",
"The airline was founded as a private company by Rahul Bhatia of InterGlobe Enterprises and Rakesh Gangwal in 2006.",
"Airbus 380");


INSERT INTO `dbms_project`.`indivo`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(5,
"Indivo",
"The airline was founded as a private company by Rahul Bhatia of InterGlobe Enterprises and Rakesh Gangwal in 2006.",
"Boeing 707");

```

## Met Airways:

```bash

INSERT INTO `dbms_project`.`metairways`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(2,
"Met Airways",
'Launched in 1993, Met Airways grew to become the airline of choice for discerning travellers in India. The famous tagline “The Joy of Flying” became synonymous with Jet Airways',
"Airbus 380");

INSERT INTO `dbms_project`.`metairways`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(6,
"Met Airways",
'Launched in 1993, Met Airways grew to become the airline of choice for discerning travellers in India. The famous tagline “The Joy of Flying” became synonymous with Jet Airways',
"Boeing 707");
```

## PiceJetL

```bash

INSERT INTO `dbms_project`.`picejet`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(3,
"PiceJet",
'The origins of PiceJet can be tracked back to March 1984 when the company was established by Indian industrialist S. K. Modi to provide private air taxi services.',
"Airbus 380");

INSERT INTO `dbms_project`.`picejet`
(`C_ID`,
`COMPANY_NAME`,
`COMPANY_HISTORY`,
`C_TYPE`)
VALUES
(6,
"PiceJet",
'The origins of PiceJet can be tracked back to March 1984 when the company was established by Indian industrialist S. K. Modi to provide private air taxi services.',
"Boeing 707");
```


</p>
<hr>

<p align="justify">
  
4. **Configuration**: Update the Python file of the project to specify the MySQL connection details.

By following these steps, you will have successfully set up the SQL database and created the required tables for the Flight Booking Management System.


</p>
<hr>