from db_connection import DatabaseConnection


def delete_row():
  try:

    db_connection = DatabaseConnection("localhost", "your_username", "your_password", "your_database_name")

    db = db_connection.connect()

    cursor = db.cursor()
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