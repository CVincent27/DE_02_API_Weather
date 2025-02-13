import sqlite3
from config import DB_PATH

connection = sqlite3.connect(DB_PATH)

def db_schema(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            country TEXT NOT NULL
        )
    """)
    
    connection.commit()

if __name__ == "__main__":
    db_schema()