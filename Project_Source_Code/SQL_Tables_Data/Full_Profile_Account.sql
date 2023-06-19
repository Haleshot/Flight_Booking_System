SELECT * FROM dbms_project.full_profile_account;























DESC full_profile_account;

SELECT * FROM full_profile_account ORDER BY Customer_ID desc LIMIT 10;

DELETE FROM full_profile_account WHERE Customer_ID = 13;
DELETE FROM full_profile_account ORDER BY Customer_ID desc LIMIT 1;

ALTER table full_profile_account modify Column Customer_Pincode VARCHAR(10);


SELECT * FROM dbms_project.full_profile_account;
SELECT * FROM dbms_project.flights;
SELECT * FROM dbms_project.Payment;
SELECT * FROM dbms_project.initial_info_account;
SELECT * FROM dbms_project.cust_choice_flight;
SELECT * FROM dbms_project.company;
SELECT * FROM dbms_project.cancellation;
SELECT * FROM dbms_project.nistara;

select distinct F_Company, F_Dept_Time
from flights
where F_Dept_Location = 'Mumbai' and F_Arr_Location = 'Bangalore' and F_Dept_Time < '2022-10-01 15:10:00' ;

CREATE VIEW FULL_CUSTOMER_INFORMATION as
(SELECT Customer_Name, Customer_State, Customer_Country, Customer_Pincode, Date_Of_Birth, Customer_Gender, PhoneNumber FROM initial_info_account iia, FULL_PROFILE_ACCOUNT ffa WHERE iia.Username = ffa.Customer_Name);


SELECT * FROM FULL_CUSTOMER_INFORMATION;



DELETE iia, ffa FROM initial_info_accouninitial_info_accountt iia INNER JOIN FULL_PROFILE_ACCOUNT ffa
ON(iia.Username = ffa.Customer_Name)
WHERE ffa.Customer_Name =
(SELECT * FROM (SELECT Customer_Name FROM FULL_PROFILE_ACCOUNT ffa WHERE ffa.Customer_Name = 'Adils' LIMIT 1) FULL_PROFILE_ACCOUNT);

SELECT Customer_Name FROM FULL_PROFILE_ACCOUNT ffa WHERE ffa.Customer_Name = 'Adils' LIMIT 1;

SELECT * FROM initial_info_account iia INNER JOIN FULL_PROFILE_ACCOUNT ffa ON(iia.Username = ffa.Customer_Name);

INSERT INTO full_profile_account VALUES(1, "Haleshot", "TN", "IND", 4007, "2003-09-09", "Male", "995745");
INSERT INTO full_profile_account VALUES(2, "Sri", "MH", "IND", 403407, "2003-01-10", "Male", "3432");