from db_connection import DatabaseConnection
import csv

def insert_data():  

  db_connection = DatabaseConnection("localhost", "your_username", "your_password", "your_database_name")

  db = db_connection.connect()

  cursor = db.cursor()

  # ✅ make it universal <table name> and take parameter names from the csv header
    # if some paramter is not given make default as "null"
  insert_query = f"INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s)"
  # "INSERT INTO {table_name} ({extract from csv headers}) VALUES (%s, %s, %s, %s)"

  try:
    with open("inputs/insert_rows.csv", "r") as file:
      all_data = csv.reader(file)
      next(all_data, None)

      for row in all_data:
        print(row)
        cursor.execute(insert_query, row)

  except Exception as error:
    print(error)




def insert_new_tables():
  
  db_connection = DatabaseConnection("localhost", "your_username", "your_password", "your_database_name")

  db = db_connection.connect()

  cursor = db.cursor()

  # Create the employees table (if it doesn't exist)
  cursor.execute(f"""CREATE TABLE IF NOT EXISTS employees (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      phone_no VARCHAR(20) NOT NULL UNIQUE,
      address VARCHAR(255) NOT NULL,
      dob DATE NOT NULL
  )""")

  # Prepare the INSERT statement
  sql = """INSERT INTO employees (id, name, phone_no, address, dob) VALUES (%s, %s, %s, %s, %s)"""

  # User data
  employees = [
      (1001, "Sachin", "9000010001", "Mumbai", "1991-01-01"),
      (1002, "Sourav", "9000010002", "Kolkata", "1992-02-01"),
      (1003, "Dhoni", "9000010003", "Chennai", "1995-03-01"),
      (1004, "Yuvraj", "9000010004", "Punjab", "1994-04-01"),
      (1005, "Sehwag", "9000010005", "Delhi", "1995-05-01"),
  ]

  # Insert the user data
  cursor.executemany(sql, employees)

  # Commit the changes to the database
  db.commit()
