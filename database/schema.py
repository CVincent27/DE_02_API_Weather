import sqlite3
import os

def db_schema(connection):
    db_path = os.path.join('database', 'data_weather.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            country TEXT NOT NULL
        )
    """)
    
    connection.commit()
