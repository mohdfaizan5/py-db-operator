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
