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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY,
            city_id INTEGER,
            weather TEXT,
            temperature REAL,
            feels_like REAL,
            temperature_min REAL,
            temperature_max REAL,
            FOREIGN KEY (city_id) REFERENCES cities (id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conditions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pressure INTEGER,
            humidity INTEGER,
            wind_speed REAL,
            wind_direction_deg INTEGER,
            cloud_cover INTEGER,
            rain REAL,
            snow REAL,
            FOREIGN KEY (id) REFERENCES weather (id)
        )
    """)
    connection.commit()

if __name__ == "__main__":
    db_schema()