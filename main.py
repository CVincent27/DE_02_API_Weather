import sqlite3
from database.create_tables import initialize_database
from database.insert_data import insert_data_from_csv
from database.queries import get_all_users
import os


def main():
    # Initialiser la base de données
    db_path = os.path.join('database', 'data_weather.db')
    initialize_database(db_path)

    # Connexion à la base de données
    connection = sqlite3.connect(db_path)

    # Insérer des données à partir d'un fichier CSV
    insert_data_from_csv(connection, 'data_csv/weather_data.csv')

    # Exécuter une requête
    users = get_all_users(connection)
    print(users)

    # Fermer la connexion
    connection.close()

if __name__ == "__main__":
    main()
