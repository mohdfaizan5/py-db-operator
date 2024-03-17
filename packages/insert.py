import csv
import datetime  # For date format validation
import mysql.connector 

def insert(db_connection):
    with db_connection as connection:
        cursor = connection.cursor()
   
        try:
            with open("inputs/insert_rows.csv", "r") as file:
                csv_reader = csv.reader(file, skipinitialspace=True, quotechar='"')
                headers = next(csv_reader) 
                print(headers)
                
                for row in csv_reader:
                    if row:  # Skip empty lines
                        try:
                            table_name = row[0]

                            print("\n\n" , row)
                            # Handle missing values
                            values = fill_empty_values_with_defaults(cursor, table_name, row[1:])
                            print(values)

                            # Validate date format
                            date_values = [value for value in values if isinstance(value, str) and "-" in value]
                            for date_value in date_values:
                                try:
                                    datetime.datetime.strptime(date_value, "%Y-%m-%d")
                                except ValueError:
                                    raise ValueError(f"Invalid date format: '{date_value}'. Please use YYYY-MM-DD.")


                            # Get database columns and adjust placeholders
                            db_columns = get_database_columns(cursor, table_name)
                            print(db_columns)
                            
                            placeholders = ", ".join(["%s"] * len(db_columns))
                            print(placeholders)

                            # Ensure enough placeholders for all columns
                            if len(values) < len(db_columns):
                                values.extend(["EMPTY"] * (len(db_columns) - len(values)))  # Add missing values
                            print(values)

                            query = f"INSERT INTO {table_name} ({', '.join(db_columns)}) VALUES ({placeholders})"
                            print(query)

                            # return
                            # return``
                            cursor.execute(query, values)

                        except ValueError as e:
                            print(f"Error in row: {row}\n{e}")
                            continue  # Skip to the next row
                        except mysql.connector.Error as err:
                            # print(err)
                            # print(err.errno)
                            if int(err.errno) == 1062:  # Check for specific error code
                                print(f"❌ Duplicate entry error on primary key:\n {err}")
                                # Handle the duplicate entry here (e.g., log the error, retry with a different id)
                            else:
                                print(f"Unexpected error: {err}")
                                # Handle other unexpected errors
                       
                        except Exception as e:
                            print(f"Unexpected error: {e}")
                            raise  # Re-raise to prevent further execution

                db_connection.commit()

                
        except Exception as error:
            print(error)


        finally:
            cursor.close()



def fill_empty_values_with_defaults(cursor, table_name, values):
    """Fills empty values in a row with appropriate defaults based on column data types."""
    db_columns = get_database_columns(cursor, table_name)

    for i, value in enumerate(values):
        if not value:  # Empty value
            column_type = get_column_type(cursor, table_name, db_columns[i])
            if column_type in ["int", "tinyint", "smallint", "mediumint", "bigint"]:
                values[i] = 0
            elif column_type in ["varchar", "char", "text"]:
                values[i] = " "
            elif column_type in ["date", "datetime"]:
                values[i] = "1499-12-01"
                """
                ❌ here when NULL is given date is throwing this error
                    ```
                    Unexpected error: 1048 (23000): Column 'dob' cannot be null
                    ```
                ❌ when some random date was given then 
                """
                # Or a specific default date value if needed
            elif column_type == "timestamp":
                # MySQL automatically sets current timestamp for NULL values
                values[i] = None
            else:
                pass

    return values

def get_database_columns(cursor, table_name):
    """Retrieves column names from the database table."""
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    return [column[0] for column in cursor.fetchall()]





def get_column_type(cursor, table_name, column_name):
    """Retrieves the data type of a column from the database table."""
    cursor.execute(f"DESCRIBE {table_name} {column_name}")
    return cursor.fetchone()[1]










# def insert_new_tables():
  
#   db_connection = DatabaseConnection("localhost", "your_username", "your_password", "your_database_name")

#   db = db_connection.connect()

#   cursor = db.cursor()

#   # Create the employees table (if it doesn't exist)
#   cursor.execute(f"""CREATE TABLE IF NOT EXISTS employees (
#       id INT AUTO_INCREMENT PRIMARY KEY,
#       name VARCHAR(255) NOT NULL,
#       phone_no VARCHAR(20) NOT NULL UNIQUE,
#       address VARCHAR(255) NOT NULL,
#       dob DATE NOT NULL
#   )""")

#   # Prepare the INSERT statement
#   sql = """INSERT INTO employees (id, name, phone_no, address, dob) VALUES (%s, %s, %s, %s, %s)"""

#   # User data
#   employees = [
#       (1001, "Sachin", "9000010001", "Mumbai", "1991-01-01"),
#       (1002, "Sourav", "9000010002", "Kolkata", "1992-02-01"),
#       (1003, "Dhoni", "9000010003", "Chennai", "1995-03-01"),
#       (1004, "Yuvraj", "9000010004", "Punjab", "1994-04-01"),
#       (1005, "Sehwag", "9000010005", "Delhi", "1995-05-01"),
#   ]

#   # Insert the user data
#   cursor.executemany(sql, employees)

#   # Commit the changes to the database
#   db.commit()
