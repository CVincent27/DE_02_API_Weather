import csv

def insert_data_from_csv(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO cities (city, country) VALUES (?, ?)
            """, (row['city'], row['country']))
    connection.commit()

if __name__ == "__main__":
    insert_data_from_csv()