from db_connection import DatabaseConnection

def show_table():

  db_connection = DatabaseConnection("localhost", "your_username", "your_password", "your_database_name")

  db = db_connection.connect()

  cursor = db.cursor()


  cursor.execute("SELECT * FROM employees")
  employees = cursor.fetchall()

  for employee in employees:
    print(employee)