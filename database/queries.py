def test_get_all_cities(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM conditions LIMIT 5")
    return cursor.fetchall()
