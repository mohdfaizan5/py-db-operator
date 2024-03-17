import csv

def delete(db_connection):
    with db_connection as connection:
        cursor = connection.cursor()

        try:
            with open("inputs/delete_row.csv", "r") as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)
                table_name = headers[0]
                target_column = headers[1]
                
                visited = False

                for row in csv_reader:
                    visited = True
                    table_name = row[0]
                    target_value = row[1]

                    # Construct dynamic query with BINARY keyword for case-insensitive comparison
                    query = f"DELETE FROM {table_name} WHERE BINARY {target_column} = %s"

                    # Execute query with parameter binding
                    cursor.execute(query, (target_value,))  # Tuple with target value

                    rows_deleted = cursor.rowcount

                    if rows_deleted > 0:
                        print(f"Deleted {rows_deleted} row(s) from {table_name}.")
                    else:
                        print(f"Target value ({target_value}) not found in {table_name} to delete.")

                if(not visited):
                    print("No input data mentioned to delete.")
                    return  # Exit the function if no tables are specified

            connection.commit()

        except Exception as error:
            print(error)

        finally:
            cursor.close()
