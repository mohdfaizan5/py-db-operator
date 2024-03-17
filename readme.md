# SQL server

```shell
pip install mysql-connector-python
```

```py
import mysql.connector # Importing it

db = mysql.connector.connect( # connect to database with these details
    host="localhost",
    user="faizan",
    password="root",
    database="employee_database"
)


mycursor = db.cursor()

```

```py
# Create a new Database
mycursor.execute("CREATE DATABASE database_name")
```

```py
# You can execute sql queries here
mycursor.execute("YOUR SQL QUERIES")
```

https://g.co/gemini/share/a14478b1314a


Todo's

- [ ] Create detailed_design_document.md and explain all working with little technical details.


# How to use SQL
After configuring and logging in for SQL,

# List all databases
```sql
SHOW DATABASES;
```

## Select a database
```sql
USE database_name;
```


# List all databases
```sql
SHOW DATABASES;
```

## Select a database
```sql
USE database_name;
```

--- 

## FRom client talk

1a. Universal database connection function
 * success and failure messages
 * Accept cred from excel sheet csv
 * should work for all  the databases like oracle postgress and mysql

1b. closing the db_function()

2. Inserting a record in a table (universal function)
 * call the "1.Universal database connection function"
 * Make table name, attribute name as global
 * Success and failure message (check if table exist or not, if table doesnt exist - "table doesnt exist {table_name}")
 * check if csv is blank "nothing to insert"
  * display how many rows inserted ""
  * commit after insertion
 * closing the db_function()
 
NOTES
* [to be confirmed - Not optimized approach and unneccesary quries and connections] data should connect create instance commit and close
 

```
db connect > cursor obj > [queries] > commit cursor > db commit > db close

db connect > cursor obj >

....

commit cursor > db commit > db close

```

3. Updating a record in a table (universal function)
 * call the "1.Universal database connection function"
 * Make table name, attribute name as global
 * Success and failure message (check if table exist or not, if table doesnt exist - "table doesnt exist {table_name}")
 * check if csv is blank "nothing to update
  * display how many rows updated ""
  * commit after updation
 * closing the db_function()


4. Deleting a record in a table (universal function)
 * call the "1.Universal database connection function"
 * Make table name, attribute name as global
 * Success and failure message (check if table exist or not, if table doesnt exist - "table doesnt exist {table_name}")
 * check if csv is blank "nothing to delete
  * display how many rows deleted  ""
  * commit after deletion
 * closing the db_function()



-------------------

## DB creadentials
```csv
host,user,password,database
mysql,localhost,faizan,root,employee_database
oracle,cloud.o,faizan,root,employee_database
```

## Insert

insert.csv
```csv
name,phone_no,address
Sehwag,9000010005,delhi
```
* Dont hard code anywhere 
* The first parameter should be, on what basis to update it.
* if no such data is found based on parameter then it should show ""
* Take sql return message something like "8 rows in set (0.00 sec)"


## Update

```csv
name,phone_no,address
Sehwag,9000010005,delhi
```

## Dont hard code anywhere 
## The first parameter should be, on what basis to update it.
## if no such data is found based on parameter then it should show ""
## Take sql return message something like "8 rows in set (0.00 sec)"

## Delete
```csv
name
Sehwag
```
* Deleting 
* Dont hard code anywhere 
* The first parameter should be, on what basis to delete it.
* if no such data is found based on parameter then it should show  return message""
* Take sql return message something like "8 rows in set (0.00 sec)"

---


 csv file -> database_cred.csv 
 one fucn for db connection -> message "successfully connected to {database host link}"


>> Make all of them as individual fn within package

1. Inserting a record in a table

  * For now id also should be in csv
\


- [] Change update


# TODO

- [ ] make a "detailed_design_document"


```sh
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| employee_database  |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.02 sec)

mysql> USE employee_database
Database changed
mysql> SELECT * FROM ^C
mysql> ^C
mysql> ^C
mysql> SHOW TABLES;
+-----------------------------+
| Tables_in_employee_database |
+-----------------------------+
| employees                   |
| users                       |
+-----------------------------+
2 rows in set (0.01 sec)

mysql> SELECT * FROM employees;
+------+-----------+-------------+-----------+------------+
| id   | name      | phone_no    | address   | dob        |
+------+-----------+-------------+-----------+------------+
| 1001 | Sachin    | 9000010001  | Mumbai    | 1991-01-01 |
| 1002 | Sourav    | 9000010002  | Kolkata   | 1998-08-08 |
| 1003 | Dhoni     | 9000010003  | Chennai   | 1993-03-01 |
| 1004 | Yuvraj    | 9000010004  | Punjab    | 1994-04-01 |
| 1005 | Sehwag    | 9000010005  | delhi     | 1995-05-01 |
| 1006 | Shouib    | 9000010008  | Pakistan  | 1998-08-08 |
| 1012 | Kapil dev | 90000100011 | India     | 1980-11-02 |
| 1019 | Tahir     | 90000100013 | JK        | 1980-12-03 |
| 1020 | Faizan    | 9379692863  | bangalore | 1980-12-03 |
| 1021 | Rohit     | 90000100013 | JK        | 1980-12-03 |
| 1022 | Tahir     | 90000100013 | JK        | 1980-12-03 |
| 1023 | Faizan    | 9379692863  | bangalore | 1980-12-03 |
| 1024 | Rohit     | 90000100013 | JK        | 1980-12-03 |
+------+-----------+-------------+-----------+------------+
13 rows in set (0.02 sec)

mysql> DELETE FROM employees where id > 1005;
Query OK, 8 rows affected (0.01 sec)

mysql> SELECT * FROM employees;
+------+--------+------------+---------+------------+
| id   | name   | phone_no   | address | dob        |
+------+--------+------------+---------+------------+
| 1001 | Sachin | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav | 9000010002 | Kolkata | 1998-08-08 |
| 1003 | Dhoni  | 9000010003 | Chennai | 1993-03-01 |
| 1004 | Yuvraj | 9000010004 | Punjab  | 1994-04-01 |
| 1005 | Sehwag | 9000010005 | delhi   | 1995-05-01 |
+------+--------+------------+---------+------------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+--------+------------+---------+------------+
| id   | name   | phone_no   | address | dob        |
+------+--------+------------+---------+------------+
| 1001 | Sachin | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav | 9000010002 | Kolkata | 1992-02-01 |
| 1003 | Dhoni  | 9000010003 | Chennai | 1995-03-01 |
| 1004 | Yuvraj | 9000010004 | Punjab  | 1994-04-01 |
| 1005 | Sehwag | 9000010005 | Delhi   | 1995-05-01 |
+------+--------+------------+---------+------------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+--------------+------------+---------+------------+
| id   | name         | phone_no   | address | dob        |
+------+--------------+------------+---------+------------+
| 1001 | Sachin       | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav       | 9000010002 | Kolkata | 1998-08-08 |
| 1003 | Dhoni        | 9000010003 | Chennai | 1993-03-01 |
| 1004 | Yuvraj       | 9000010004 | Punjab  | 1994-04-01 |
| 1005 | Sehwag       | 9000010005 | delhi   | 1995-05-01 |
| 1026 | Rohit Sharma | 9000010006 | Mumbai  | 1980-12-03 |
+------+--------------+------------+---------+------------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+---------------+------------+-----------+------------+
| id   | name          | phone_no   | address   | dob        |
+------+---------------+------------+-----------+------------+
| 1001 | Sachin        | 9000010001 | Mumbai    | 1991-01-01 |
| 1002 | Sourav        | 9000010002 | Kolkata   | 1998-08-08 |
| 1003 | Dhoni         | 9000010003 | Chennai   | 1993-03-01 |
| 1004 | Yuvraj        | 9000010004 | Punjab    | 1994-04-01 |
| 1005 | Sehwag        | 9000010005 | delhi     | 1995-05-01 |
| 1026 | Rohit Sharma  | 9000010006 | Mumbai    | 1980-12-03 |
| 1027 | Ishant Sharma | 9000010007 | Delhi     | 1980-12-03 |
| 1028 | Ishan Kishan  | 9000010008 | Jharkhand | 1980-12-03 |
+------+---------------+------------+-----------+------------+
8 rows in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+------------------+------------+-----------+------------+
| id   | name             | phone_no   | address   | dob        |
+------+------------------+------------+-----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai    | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata   | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai   | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab    | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi     | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai    | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi     | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010008 | Jharkhand | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP        | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar     | 1980-12-03 |
+------+------------------+------------+-----------+------------+
10 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+---------------+------------+---------+------------+
| id   | name          | phone_no   | address | dob        |
+------+---------------+------------+---------+------------+
| 1001 | Sachin        | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav        | 9000010002 | Kolkata | 1992-02-01 |
| 1003 | Dhoni         | 9000010003 | Chennai | 1995-03-01 |
| 1004 | Yuvraj        | 9000010004 | Punjab  | 1994-04-01 |
| 1005 | Sehwag        | 9000010005 | Delhi   | 1995-05-01 |
| 1006 | Mohammed Kaif | 9000010011 | UP      | 1980-12-03 |
+------+---------------+------------+---------+------------+
6 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+--------+------------+---------+------------+
| id   | name   | phone_no   | address | dob        |
+------+--------+------------+---------+------------+
| 1001 | Sachin | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav | 9000010002 | Kolkata | 1992-02-01 |
| 1003 | Dhoni  | 9000010003 | Chennai | 1995-03-01 |
| 1004 | Yuvraj | 9000010004 | Punjab  | 1994-04-01 |
| 1005 | Sehwag | 9000010005 | Delhi   | 1995-05-01 |
+------+--------+------------+---------+------------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+--------+------------+---------+------------+
| id   | name   | phone_no   | address | dob        |
+------+--------+------------+---------+------------+
| 1001 | Sachin | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav | 9000010002 | Kolkata | 1992-02-01 |
| 1003 | Dhoni  | 9000010003 | Chennai | 1995-03-01 |
| 1004 | Yuvraj | 9000010004 | Punjab  | 1994-04-01 |
+------+--------+------------+---------+------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+--------+------------+---------+------------+
| id   | name   | phone_no   | address | dob        |
+------+--------+------------+---------+------------+
| 1001 | Sachin | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav | 9000010002 | Kolkata | 1992-02-01 |
| 1003 | Dhoni  | 9000010003 | Chennai | 1995-03-01 |
| 1004 | Yuvraj | 9000010004 | Punjab  | 1994-04-01 |
+------+--------+------------+---------+------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+--------+------------+---------+------------+
| id   | name   | phone_no   | address | dob        |
+------+--------+------------+---------+------------+
| 1001 | Sachin | 9000010001 | Mumbai  | 1991-01-01 |
| 1002 | Sourav | 9000010002 | Kolkata | 1992-02-01 |
| 1003 | Dhoni  | 9000010003 | Chennai | 1995-03-01 |
+------+--------+------------+---------+------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+-------+------------+---------+------------+
| id   | name  | phone_no   | address | dob        |
+------+-------+------------+---------+------------+
| 1003 | Dhoni | 9000010003 | Chennai | 1995-03-01 |
+------+-------+------------+---------+------------+
1 row in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+------------------+------------+-----------+------------+
| id   | name             | phone_no   | address   | dob        |
+------+------------------+------------+-----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai    | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata   | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai   | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab    | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi     | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai    | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi     | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010008 | Jharkhand | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP        | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar     | 1980-12-03 |
| 1031 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1032 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1033 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1034 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1035 | Azhar            | this is no | Gujrath   | 1991-01-01 |
+------+------------------+------------+-----------+------------+
15 rows in set (0.00 sec)

mysql> desc employees;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| name     | varchar(255) | NO   |     | NULL    |                |
| phone_no | varchar(20)  | NO   |     | NULL    |                |
| address  | varchar(255) | NO   |     | NULL    |                |
| dob      | date         | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)

mysql> alter employees phone_no int;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'employees phone_no int' at line 1
mysql> alter^Cmployees phone_no int;
mysql> alteralteralteralter^C
mysql> ^C
mysql> ALTER TABLE employees Modify column phone_no int(10);
ERROR 1264 (22003): Out of range value for column 'phone_no' at row 1
mysql> ALTER TABLE employees Modify column phone_no int(10);
ERROR 1264 (22003): Out of range value for column 'phone_no' at row 1
mysql> ALTER TABLE employees Modify column phone_no int(15);
ERROR 1264 (22003): Out of range value for column 'phone_no' at row 1
mysql> SELECT * FROM employees;
+------+------------------+------------+-----------+------------+
| id   | name             | phone_no   | address   | dob        |
+------+------------------+------------+-----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai    | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata   | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai   | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab    | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi     | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai    | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi     | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010008 | Jharkhand | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP        | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar     | 1980-12-03 |
| 1031 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1032 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1033 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1034 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1035 | Azhar            | this is no | Gujrath   | 1991-01-01 |
+------+------------------+------------+-----------+------------+
15 rows in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+------------------+------------+-----------+------------+
| id   | name             | phone_no   | address   | dob        |
+------+------------------+------------+-----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai    | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata   | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai   | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab    | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi     | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai    | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi     | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010008 | Jharkhand | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP        | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar     | 1980-12-03 |
| 1031 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1032 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1033 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1034 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1035 | Azhar            | 9379692863 | Gujrath   | 1991-01-01 |
+------+------------------+------------+-----------+------------+
15 rows in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+------------------+------------+-----------+------------+
| id   | name             | phone_no   | address   | dob        |
+------+------------------+------------+-----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai    | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata   | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai   | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab    | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi     | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai    | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi     | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010008 | Jharkhand | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP        | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar     | 1980-12-03 |
| 1031 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1032 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1033 | Irfan Pathan     | 9000010005 | Gujrath   | 1991-01-01 |
| 1034 | Yousuf Pathan    | 9000010006 | Gujrath   | 1991-01-01 |
| 1035 | Azhar            | 9000010005 | Hydrabad  | 1991-01-01 |
+------+------------------+------------+-----------+------------+
15 rows in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+------------------+------------+-----------+------------+
| id   | name             | phone_no   | address   | dob        |
+------+------------------+------------+-----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai    | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata   | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai   | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab    | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi     | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai    | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi     | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010008 | Jharkhand | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP        | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar     | 1980-12-03 |
| 1031 | Irfan Pathan     | 9000010005 | Hydrabad  | 1991-01-01 |
| 1032 | Yousuf Pathan    | 9000010005 | Hydrabad  | 1991-01-01 |
| 1033 | Irfan Pathan     | 9000010005 | Hydrabad  | 1991-01-01 |
| 1034 | Yousuf Pathan    | 9000010005 | Hydrabad  | 1991-01-01 |
| 1035 | Azhar            | 9000010005 | Hydrabad  | 1991-01-01 |
+------+------------------+------------+-----------+------------+
15 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+---------------+------------+---------+------------+
| id   | name          | phone_no   | address | dob        |
+------+---------------+------------+---------+------------+
| 1003 | Dhoni         | 9000010003 | Chennai | 1995-03-01 |
| 1007 | Irfan Pathan  | 9000010005 | Gujrath | 1991-01-01 |
| 1008 | Yousuf Pathan | 9000010006 | Gujrath | 1991-01-01 |
+------+---------------+------------+---------+------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+------+---------------+------------+----------+------------+
| id   | name          | phone_no   | address  | dob        |
+------+---------------+------------+----------+------------+
| 1003 | Dhoni         | 9000010004 | Hydrabad | 1995-03-01 |
| 1007 | Irfan Pathan  | 9000010005 | Gujrath  | 1991-01-01 |
| 1008 | Yousuf Pathan | 9000010006 | Gujrath  | 1991-01-01 |
+------+---------------+------------+----------+------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM employees;
+------+------------------+------------+----------+------------+
| id   | name             | phone_no   | address  | dob        |
+------+------------------+------------+----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai   | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata  | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai  | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab   | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi    | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai   | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi    | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010005 | Hydrabad | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP       | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar    | 1980-12-03 |
| 1031 | Irfan Pathan     | 9000010005 | Hydrabad | 1991-01-01 |
| 1032 | Yousuf Pathan    | 9000010005 | Hydrabad | 1991-01-01 |
| 1033 | Irfan Pathan     | 9000010005 | Hydrabad | 1991-01-01 |
| 1034 | Yousuf Pathan    | 9000010005 | Hydrabad | 1991-01-01 |
| 1035 | Azhar            | 9000010005 | Hydrabad | 1991-01-01 |
+------+------------------+------------+----------+------------+
15 rows in set (0.00 sec)

mysql>
```
PS D:\Code\SQL python> python .\main.py
(1003, 'Dhoni', '9000010003', 'Chennai', datetime.date(1993, 3, 1))
(1004, 'Yuvraj', '9000010004', 'Punjab', datetime.date(1994, 4, 1))
(1005, 'Sehwag', '9000010005', 'delhi', datetime.date(1995, 5, 1))
(1001, 'Sachin', '9000010001', 'Mumbai', datetime.date(1991, 1, 1))
(1003, 'Dhoni', '9000010003', 'Chennai', datetime.date(1995, 3, 1))
(1004, 'Yuvraj', '9000010004', 'Punjab', datetime.date(1994, 4, 1))
(1005, 'Sehwag', '9000010005', 'Delhi', datetime.date(1995, 5, 1))
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) [None, 'Rohit Sharma', '9000010006', 'Mumbai', '1980-12-03']
Not all parameters were used in the SQL statement
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
'9000010006', 'Mumbai', '1980-12-03']
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Ishant Sharma', '9000010007', 'Delhi', '1980-12-03']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Ishan Kishan', 
'9000010008', 'Jharkhand', '1980-12-03']
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Praveen Kumar', '9000010009', 'UP', '1980-12-03']
r', '9000010010', 'Bihar', '1980-12-03']
INSERT INTO users (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Mohammed Kaif', '9000010011', 'UP', '1980-12-03']
Changes committed successfully.
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Irfan Pathan', 
None, 'Gujrath', '1980-12-03']
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address']
INSERT INTO employees (name, phone_no, address) VALUES (%s, %s, %s) ['Irfan Pathan', '900001001364 (HY000): Field 'dob' doesn't have a default value
PS D:\Code\SQL python> python .\main.py
['users', 'Mohammed Kaif']
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
['users', 'SEHWAG']
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
['users', '']
Target value not found in users.
Changes committed successfully.
['USERS', 'Yuvraj']
Deleted 1 row(s) from USERS.
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
Deleted 1 row(s) from USERS.
['USERS', 'Sourav']
Deleted 1 row(s) from USERS.
Changes committed successfully.
headers, ['table_name', 'name', 'phone_no', 'address']
INSERT INTO users (name, phone_no, address) VALUES (%s, %s, %s) ['Irfan Pathan', '9000010005', 'Gujrath']
1364 (HY000): Field 'dob' doesn't have a default value
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
0010005', 'Gujrath', '12-10-1999']
1292 (22007): Incorrect date value: '12-10-1999' for column 'dob' at row 1
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
INSERT INTO users (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Irfan Pathan', '9000010005', 'Gujrath', '1991-01-01']
00010006', 'Gujrath', '1991-01-01']
list index out of range
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Irfan Pathan', 
'9000010005', 'Gujrath', '1991-01-01']
 '9000010006', 'Gujrath', '1991-01-01']
list index out of range
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
'9000010005', 'Gujrath', '1991-01-01']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Yousuf Pathan', '9000010006', 'Gujrath', '1991-01-01']
Changes committed successfully.
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Azhar', 'this is no', 'Gujrath', '1991-01-01']
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
headers, ['table_name', 'name', 'phone_no', 'address', 'dob']
o', 'Gujrath', 'this is data']
1292 (22007): Incorrect date value: 'this is data' for column 'dob' at row 1
PS D:\Code\SQL python> python .\main.py
['table_name', 'name', 'phone_no'] name ['phone_no']
phone_no = %s
employees
UPDATE employees SET phone_no = %s WHERE name = %s ['Azhar', '9379692863', 'Azhar']
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
['table_name', 'name', 'phone_no', 'address'] name ['phone_no', 'address']
phone_no = %s, address = %s
employees
UPDATE employees SET phone_no = %s, address = %s WHERE name = %s ['Azhar', '9000010005', 'Hydrabad', 'Azhar']
Updated 1 row(s) in employees.
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
['table_name', 'name', 'phone_no', 'address'] name ['phone_no', 'address']
phone_no = %s, address = %s
employees
UPDATE employees SET phone_no = %s, address = %s WHERE name = %s ['Azhar', '9000010005', 'Hydrabad', 'Azhar']
employees
UPDATE employees SET phone_no = %s, address = %s WHERE name = %s ['Irfan Pathan', '9000010005', 'Hydrabad', 'Irfan Pathan']
Updated 2 row(s) in employees.
employees
UPDATE employees SET phone_no = %s, address = %s WHERE name = %s ['Yousuf Pathan', '9000010005', 'Hydrabad', 'Yousuf Pathan']
Updated 2 row(s) in employees.
Changes committed successfully.
PS D:\Code\SQL python> python .\main.py
['table_name', 'name', 'phone_no', 'address'] name ['phone_no', 'address']
phone_no = %s, address = %s
employees
UPDATE employees SET phone_no = %s, address = %s WHERE name = %s ['Ishan Kishan', '9000010005', 'Hydrabad', 'Ishan Kishan']
Updated 1 row(s) in employees.
USERS
UPDATE USERS SET phone_no = %s, address = %s WHERE name = %s ['Dhoni', '9000010004', 'Hydrabad', 'Dhoni']
Updated 1 row(s) in USERS.
Changes committed successfully.
```sh

```

```
+------+------------------+------------+----------+------------+
| id   | name             | phone_no   | address  | dob        |
+------+------------------+------------+----------+------------+
| 1001 | Sachin           | 9000010001 | Mumbai   | 1991-01-01 |
| 1002 | Sourav           | 9000010002 | Kolkata  | 1998-08-08 |
| 1003 | Dhoni            | 9000010003 | Chennai  | 1993-03-01 |
| 1004 | Yuvraj           | 9000010004 | Punjab   | 1994-04-01 |
| 1005 | Sehwag           | 9000010005 | delhi    | 1995-05-01 |
| 1026 | Rohit Sharma     | 9000010006 | Mumbai   | 1980-12-03 |
| 1027 | Ishant Sharma    | 9000010007 | Delhi    | 1980-12-03 |
| 1028 | Ishan Kishan     | 9000010005 | Hydrabad | 1980-12-03 |
| 1029 | Praveen Kumar    | 9000010009 | UP       | 1980-12-03 |
| 1030 | Bhuneshwar Kumar | 9000010010 | Bihar    | 1980-12-03 |
| 1031 | Irfan Pathan     | 9000010005 | Hydrabad | 1991-01-01 |
| 1032 | Yousuf Pathan    | 9000010005 | Hydrabad | 1991-01-01 |
| 1033 | Irfan Pathan     | 9000010005 | Hydrabad | 1991-01-01 |
| 1034 | Yousuf Pathan    | 9000010005 | Hydrabad | 1991-01-01 |
| 1035 | Azhar            | 9000010005 | Hydrabad | 1991-01-01 |
+------+------------------+------------+----------+------------+
```