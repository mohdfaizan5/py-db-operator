import mysql.connector

class DatabaseConnection:

    def __init__(self, host, user, password, database):
        self.connection = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        if not self.connection:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_val:
                # Handle potential errors during execution
                print(f"Error: {exc_val}")
            self.connection.close()
            self.connection = None

        
    # def connect(self):
    #     if not self.connection:
    #         self.connection = mysql.connector.connect(
    #             host=self.host,
    #             user=self.user,
    #             password=self.password,
    #             database=self.database
    #         )
    #     return self.connection

    # def close(self):
    #     if self.connection:
    #         self.connection.close()
    #         self.connection = None