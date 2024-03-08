import csv

def get_connection_details():
  with open("inputs/database_cred.csv", "r") as file:
    all_data = csv.DictReader(file)
    
    for d in all_data:
      # print(d, d["host"])
      return {
        "host": d["host"],
        "user": d["user"],
        "password": d["password"],
        "database": d["database"]
    }
      
      