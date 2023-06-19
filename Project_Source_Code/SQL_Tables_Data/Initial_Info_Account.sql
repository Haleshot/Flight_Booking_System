SELECT * FROM dbms_project.initial_info_account;
DESC initial_info_account;

DELETE FROM initial_info_account WHERE USERNAME = "testusername";
SELECT * FROM full_profile_account where Customer_Name IN (SELECT Username FROM initial_info_account);

INSERT INTO initial_info_account VALUES("Haleshot", "ggs");
INSERT INTO initial_info_account VALUES("Sri", "a");

SELECT * FROM flights WHERE F_Dept_Location = 'Mumbai' AND F_Arr_Location = 'Chennai' AND F_Company = 'Picejet' AND (F_Dept_Time LIKE '%10:10%' or F_Dept_Time LIKE '%06:00%' or F_Dept_Time LIKE '%08:00%' or F_Dept_Time LIKE '%14:00%' or F_Dept_Time LIKE '%16:00%' or F_Dept_Time LIKE '%12:00%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%12:45%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%04:00%' or F_Dept_Time LIKE '%10:00%' or F_Dept_Time LIKE '%14:20%' or F_Dept_Time LIKE '%10:30%' or F_Dept_Time LIKE '%14:10%' or F_Dept_Time LIKE '%12:40%' or F_Dept_Time LIKE '%15:20%') and F_Dept_Time NOT LIKE '%18:10%';

SELECT COUNT(*) FROM initial_info_account WHERE PASSWORD IN
(SELECT Password FROM initial_info_accocompanyunt);

ALTER table initial_info_account ADD PRIMARY KEY(Username);


SELECT * FROM FULL_CUSTOMER_INFORMATION WHERE Customer_Name = 'username';