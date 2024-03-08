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
