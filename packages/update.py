from db_connection import DatabaseConnection



def update_row(table_name='employees'):
  """
  Updates multiple fields in a MySQL table based on user-provided information.

  Args:
      database_name (str): Name of the database containing the table.
      table_name (str): Name of the table to update data in.
      user (str): Username for accessing the MySQL database.
      password (str): Password for accessing the MySQL database.
      host (str, optional): Hostname or IP address of the MySQL server. Defaults to "localhost".
  """

  db_connection = DatabaseConnection("localhost", "your_username", "your_password", "your_database_name")

  db = db_connection.connect()

  cursor = db.cursor()
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




# def update_row_by_name():
#       with open("./inputs/update_rows.csv", 'r') as file:
#         reader = csv.reader(file)
#         next(reader, None)  # Skip the header row again

#         update_query = f"UPDATE employees SET phone_no = %s, address = %s, dob= %s WHERE name = %s"

#         # Read data from CSV file and update rows
#         with open("./inputs/update_rows.csv", 'r') as file:
#           reader = csv.DictReader(file)
#           for row in reader:
#             # Execute the update query with values from the CSV row
#             cursor.execute(update_query, (row['phone_no'], row['address']), row['dob'], row['name'])

#       # Commit the changes
#       db.commit()