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
                print(f"Error: {exc_val}")
            else:
                self.connection.commit()  # Commit changes before closing
            self.connection.close()
            self.connection = None

    def commit(self):
        """Explicitly commits changes to the database."""
        if self.connection:
            self.connection.commit()
            print("Changes committed successfully.")
