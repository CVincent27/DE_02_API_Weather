import csv
import sqlite3
from config import DB_PATH

def insert_data_from_csv(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO cities (city, country) VALUES (?, ?)
            """, (row['city'], row['country']))

            cursor.execute("""
                INSERT INTO weather (weather, temperature,
            feels_like, temperature_min, temperature_max) VALUES (?, ?, ?, ?, ?)
            """, (row['weather'], row['temperature'],row['feels_like'],
                  row['temperature_min'], row['temperature_max']))
    connection.commit()

if __name__ == "__main__":
    connection = sqlite3.connect(DB_PATH)
    insert_data_from_csv(connection, 'data_csv/weather_data.csv')
    connection.close()