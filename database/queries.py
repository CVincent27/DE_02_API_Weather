def get_all_cities(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cities LIMIT 5")
    return cursor.fetchall()
