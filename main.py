from packages.db_connect import DatabaseConnection
from packages.insert import insert
from packages.show_table import show_table
from packages.update import update
from packages.delete import delete
from packages.get_connection_details import get_connection_details

connection_details = get_connection_details()
connection_instance = DatabaseConnection(**connection_details) # ignore the error


########### START HERE 👇👇👇 #########

# show_table(connection_instance)
insert(connection_instance)
  # If column is not specified then It should by default take value 'NULL'
  # if value is not given for a column name then it should take it as NULL  
    # write a if condition for pre check the data if data == "" then make it "NULL"
  # if the datatype and values specified is more than table defination 
    #"INSERT INTO employees (name, phone_no, address, dob) VALUES (%s, %s, %s, %s) ['Yousuf Pathan', '9000010006', 'Gujrath', '1991-01-01']
    # list index out of range"


# update(connection_instance)
# delete(connection_instance)

# v1 = ["emp", "faizan", "935", "", "lkasdf23"]

# new_v1 = [value if value else "Empty" for value in v1[1:]]

# print(new_v1)

connection_instance.commit()