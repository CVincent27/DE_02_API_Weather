import sqlite3
import os

db_path = os.path.join('tests', 'test.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")

cursor.execute("INSERT INTO example VALUES (1, 'alice', 20)")
cursor.execute("INSERT INTO example VALUES (2, ’bob’, 30)")
cursor.execute("INSERT INTO example VALUES (3, ’eve’, 40)")

connection.commit()