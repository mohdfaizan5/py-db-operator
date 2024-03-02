import mysql.connector
import csv

db = mysql.connector.connect(
    host="localhost",
    user="faizan",
    password="root",
    database="employee_database"
)

cursor = db.cursor()

# print("\n\n")

def insert_new_tables():

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

def insert_one_row():
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


def show_all_tables():
  cursor.execute("SELECT * FROM employees")
  employees = cursor.fetchall()

  for employee in employees:
    print(employee)







# ////////////////////////////////////
    
def update_multiple_fields(table_name='employees'):
  """
  Updates multiple fields in a MySQL table based on user-provided information.

  Args:
      database_name (str): Name of the database containing the table.
      table_name (str): Name of the table to update data in.
      user (str): Username for accessing the MySQL database.
      password (str): Password for accessing the MySQL database.
      host (str, optional): Hostname or IP address of the MySQL server. Defaults to "localhost".
  """

  try:


    # Get user input for update details
    condition_column = input("Enter the column name for the condition: ")
    condition_value = input("Enter the value to filter the condition (e.g., 'John' for name): ")

    # Get user input for fields to update
    fields_to_update = []
    while True:
      field = input("Enter the name of a field to update (or 'done' to finish): ")
      if field.lower() == "done":
        break
      fields_to_update.append(field)

    # Construct the UPDATE query dynamically
    placeholder_list = ", ".join(["%s"] * len(fields_to_update))
    update_query = f"UPDATE {table_name} SET {', '.join(fields_to_update)} = {placeholder_list} WHERE {condition_column} = %s"

    # Get user input for new values
    values = []
    for field in fields_to_update:
      new_value = input(f"Enter the new value for '{field}': ")
      values.append(new_value)

    # Execute the update query with all user-provided values
    cursor.execute(update_query, values + [condition_value])

    # Commit the changes
    db.commit()

    print(f"Successfully updated {', '.join(fields_to_update)} in {table_name} based on the specified condition.")

  except mysql.connector.Error as err:
    print(f"Error updating data: {err}")

# ////////////////////////////////////


def delete_row():
  try:
    column_name = input("Enter the column name for the deletion criteria: ")
    value = input("Enter the value to identify the row to delete: ")

    # Construct the DELETE query
    delete_query = f"DELETE FROM employees WHERE {column_name} = %s"

    # Execute the delete query
    cursor.execute(delete_query, (value,))

    # Commit the changes
    db.commit()

    # Check if rows were affected
    rows_deleted = cursor.rowcount
    if rows_deleted > 0:
      print(f"Successfully deleted {rows_deleted} row(s).")
    else:
      print(f"No rows found matching the given criteria.")

  except mysql.connector.Error as err:
    print(f"Error deleting data: {err}")



def update_row_by_name():
      with open("./inputs/update_rows.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip the header row again

        update_query = f"UPDATE employees SET phone_no = %s, address = %s, dob= %s WHERE name = %s"

        # Read data from CSV file and update rows
        with open("./inputs/update_rows.csv", 'r') as file:
          reader = csv.DictReader(file)
          for row in reader:
            # Execute the update query with values from the CSV row
            cursor.execute(update_query, (row['phone_no'], row['address']), row['dob'], row['name'])

      # Commit the changes
      db.commit()


# print("\n\nQuery successfull!✅")

isRunning = True

while isRunning:

  ch = int(input("\n-------------------------\n1.Insert row  2.Update Row  3.Delete Row  4.Read all rows  5.Exit \nEnter your choice: "))

  if(ch == 1):
    print("Inserting new row from file")
    insert_one_row()

  elif(ch == 2):
    print("Updating Row")
    # update_row_by_name()
    update_multiple_fields()

  elif(ch == 3):
    print("Deleting a row")
    delete_row()
  
  elif(ch == 4):
    print("Showing all rows")
    show_all_tables()

  elif(ch == 5):
    print("Exiting")

    isRunning = False


# Close the connection to the database
cursor.close()
db.commit()
db.close()