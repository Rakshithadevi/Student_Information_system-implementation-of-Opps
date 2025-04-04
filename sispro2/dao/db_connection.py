import mysql.connector

class DBConnection:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"  # Change to your MySQL username
        self.password = "rakshi430"  # Change to your MySQL password
        self.database = "sis_db1"  # Change to your database name
        self.conn = None
        self.cursor = None

    def get_connection(self):
        """Returns a new database connection."""
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        """Execute a SQL query with optional parameters."""
        self.get_connection()
        self.cursor.execute(query, params or ())
        self.conn.commit()
        self.disconnect()

    def fetch_results(self, query, params=None):
        """Fetch query results."""
        self.get_connection()
        self.cursor.execute(query, params or ())
        results = self.cursor.fetchall()
        self.disconnect()
        return results
