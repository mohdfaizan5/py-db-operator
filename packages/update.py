import csv

def update(db_connection):
    with db_connection as connection:
        cursor = connection.cursor()

        try:
            with open("inputs/update_rows.csv", "r") as file:
                csv_reader = csv.reader(file)

                # Read headers (assuming the first row contains them)
                headers = next(csv_reader)
                target_column = headers[1]  # Assuming the second column is the target
                update_columns = headers[2:]  # Update columns from the third column onwards

                # Construct dynamic SET clause based on update columns
                set_clause = ", ".join([f"{col} = %s" for col in update_columns])

                print(headers, target_column, update_columns)
                print(set_clause)

                # Iterate over data rows (skipping the header row)
                for row in csv_reader:
                    table_name = row[0]  # Now correctly access table name from each row
                    print(table_name)
                    # Construct and execute dynamic query
                    query = f"UPDATE {table_name} SET {set_clause} WHERE {target_column} = %s"
                    update_values = [value for value in row[1:]]  # Update values (excluding target)
                    
                    print(query, update_values + [row[1]])

                    cursor.execute(query, update_values[1:] + [row[1]])  # Add target value after update values
                    rows_affected = cursor.rowcount

                    if rows_affected > 0:
                        print(f"Updated {rows_affected} row(s) in {table_name}.")
                    else:
                        print(f"Target value not found in {table_name}.")

                db_connection.commit()

        except Exception as error:
            print(error)

        finally:
            cursor.close()
