import csv

def show_table(connection_instance):

  with connection_instance as connection:
    cursor = connection.cursor()
 
    try:
      with open("inputs/show_tables.csv", "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:

          
          cursor.execute(f"SELECT * FROM {row["table_name"]}")
          table_data = cursor.fetchall()

          for row in table_data:
            print(row)

    except Exception as err:
      print(err)
