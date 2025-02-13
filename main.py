from api.geo_data import geo_data_fetch_save
from api.weather import weather_data_fetch_save

from database.schema import db_schema, connection, DB_PATH
from database.create_tables import initialize_database
from database.insert_data import insert_data_from_csv
from database.queries import get_all_cities



def main():

    # Recup geoloc
    geo_data_fetch_save()
    # Recup data cities
    weather_data_fetch_save()

    # Initialiser la base de données
    db_schema(connection)
    initialize_database(DB_PATH)

    # Insérer des données à partir d'un fichier CSV
    insert_data_from_csv(connection, 'data_csv/weather_data.csv')

    # Exécuter une requête
    users = get_all_cities(connection)
    print(users)

    # Fermer la connexion
    connection.close()

if __name__ == "__main__":
    main()
