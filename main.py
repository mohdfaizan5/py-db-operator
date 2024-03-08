from packages.db_connect import DatabaseConnection
from packages.insert import insert
from packages.show_table import show_table
from packages.update import update
from packages.delete import delete
from packages.get_connection_details import get_connection_details

connection_details = get_connection_details()
connection_instance = DatabaseConnection(**connection_details) # ignore the error


########### START HERE 👇👇👇 #########

# insert(connection_instance)
show_table(connection_instance)
# update(connection_instance)
# delete(connection_instance)



# connection_instance.commit()