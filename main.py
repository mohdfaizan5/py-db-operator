from packages.db_connection import DatabaseConnection
from packages.insert import insert_data
from packages.delete import delete_row
from packages.show_table import show_table
from packages.update import update_row

connection_details = {
    "host":"localhost",
    "user":"faizan",
    "password":"root",
    "database":"employee_database"
}
db_connection = DatabaseConnection(**connection_details)

########### START HERE 👇👇👇 #########

insert_data(db_connection)












# cursor = db_connection.cursor()

# cursor.close()
# db_connection.commit()
# db_connection.close()