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
                
                for row in csv_reader:
                    print(row)
                    table_name = row[0]
                    target_value = row[1]

                    # Construct dynamic query
                    query = f"DELETE FROM {table_name} WHERE {target_column} = %s"

                    # Execute query with target value
                    cursor.execute(query, [target_value])
                    rows_deleted = cursor.rowcount

                    if rows_deleted > 0:
                        print(f"Deleted {rows_deleted} row(s) from {table_name}.")
                    else:
                        print(f"Target value not found in {table_name}.")

                db_connection.commit()

        except Exception as error:
            print(error)

        finally:
            cursor.close()
