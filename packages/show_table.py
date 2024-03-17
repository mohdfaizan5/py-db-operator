import csv

def show_table(connection_instance):

  with connection_instance as connection:
    cursor = connection.cursor()

    try:
      with open("inputs/show_tables.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        
        firstVisit = False
      
        for row in csv_reader:

          firstVisit = True          
          cursor.execute(f"SELECT * FROM {row[0]}")
          table_data = cursor.fetchall()

          for row in table_data:
            print(row)

        if(not firstVisit):
          print("No tables mentioned to display.")
          return  # Exit the function if no tables are specified
          

    except Exception as err:
      print(err)
